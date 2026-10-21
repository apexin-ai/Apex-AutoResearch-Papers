"""
Training entry point for STORM on DMC Walker Walk (proprioceptive).

Usage:
  python train_dmc.py -n walker_walk_baseline -seed 0 \
      -config_path config/dmc_walker.yaml

Unchanged logic from original STORM train.py:
- Joint training loop (world model + agent)
- Imagination-based actor-critic update
- Context-conditioned action selection

Changes:
- DMC vec env instead of Atari
- Continuous obs/action handling (no /255, no image rearrange)
- action is (num_envs, action_dim) not (num_envs,) scalar
"""
import argparse
import os
import shutil
import random
import json

import numpy as np
import torch
import torch.nn as nn
import torch.nn.functional as F
from collections import deque
from tqdm import tqdm
import colorama

from utils import seed_np_torch, Logger
from replay_buffer import ReplayBuffer
import agents
from sub_models.world_models import WorldModel
from envs.dmc_env import build_dmc_vec_env, build_single_dmc_env

try:
    import wandb
    HAS_WANDB = True
except ImportError:
    HAS_WANDB = False

# ---------------------------------------------------------------------------
# Config loading (extends original STORM's yacs config with DMC fields)
# ---------------------------------------------------------------------------
from yacs.config import CfgNode as CN


def load_dmc_config(config_path):
    conf = CN()
    conf.Task = ""

    conf.BasicSettings = CN()
    conf.BasicSettings.Seed = 0
    conf.BasicSettings.ReplayBufferOnGPU = False

    conf.Models = CN()

    conf.Models.WorldModel = CN()
    conf.Models.WorldModel.ObsDim = 24
    conf.Models.WorldModel.ActionDim = 6
    conf.Models.WorldModel.EncoderHiddenDim = 256
    conf.Models.WorldModel.TransformerMaxLength = 64
    conf.Models.WorldModel.TransformerHiddenDim = 512
    conf.Models.WorldModel.TransformerNumLayers = 2
    conf.Models.WorldModel.TransformerNumHeads = 8
    conf.Models.WorldModel.LearningRate = 1e-4

    conf.Models.Agent = CN()
    conf.Models.Agent.NumLayers = 2
    conf.Models.Agent.HiddenDim = 512
    conf.Models.Agent.Gamma = 0.997
    conf.Models.Agent.Lambda = 0.95
    conf.Models.Agent.EntropyCoef = 1e-4
    conf.Models.Agent.LearningRate = 3e-5

    conf.JointTrainAgent = CN()
    conf.JointTrainAgent.SampleMaxSteps = 500000
    conf.JointTrainAgent.BufferMaxLength = 1000000
    conf.JointTrainAgent.BufferWarmUp = 5000
    conf.JointTrainAgent.NumEnvs = 1
    conf.JointTrainAgent.BatchSize = 16
    conf.JointTrainAgent.DemonstrationBatchSize = 0
    conf.JointTrainAgent.BatchLength = 64
    conf.JointTrainAgent.ImagineBatchSize = 256
    conf.JointTrainAgent.ImagineDemonstrationBatchSize = 0
    conf.JointTrainAgent.ImagineContextLength = 8
    conf.JointTrainAgent.ImagineBatchLength = 15
    conf.JointTrainAgent.TrainDynamicsEverySteps = 1
    conf.JointTrainAgent.TrainAgentEverySteps = 1
    conf.JointTrainAgent.SaveEverySteps = 10000
    conf.JointTrainAgent.UseDemonstration = False

    conf.defrost()
    conf.merge_from_file(config_path)
    conf.freeze()
    return conf


# ---------------------------------------------------------------------------
# Build functions
# ---------------------------------------------------------------------------
def build_world_model(conf):
    wm_conf = conf.Models.WorldModel
    return WorldModel(
        obs_dim=wm_conf.ObsDim,
        action_dim=wm_conf.ActionDim,
        encoder_hidden_dim=wm_conf.EncoderHiddenDim,
        transformer_max_length=wm_conf.TransformerMaxLength,
        transformer_hidden_dim=wm_conf.TransformerHiddenDim,
        transformer_num_layers=wm_conf.TransformerNumLayers,
        transformer_num_heads=wm_conf.TransformerNumHeads,
        wm_lr=wm_conf.LearningRate,
    ).cuda()


def build_agent(conf):
    wm_conf = conf.Models.WorldModel
    ag_conf = conf.Models.Agent
    feat_dim = 32 * 32 + wm_conf.TransformerHiddenDim  # stoch_flat + hidden
    return agents.ActorCriticAgent(
        feat_dim=feat_dim,
        num_layers=ag_conf.NumLayers,
        hidden_dim=ag_conf.HiddenDim,
        action_dim=wm_conf.ActionDim,
        gamma=ag_conf.Gamma,
        lambd=ag_conf.Lambda,
        entropy_coef=ag_conf.EntropyCoef,
        agent_lr=ag_conf.LearningRate,
    ).cuda()


# ---------------------------------------------------------------------------
# Training steps (same structure as original STORM)
# ---------------------------------------------------------------------------
def train_world_model_step(replay_buffer, world_model, batch_size, batch_length, logger):
    obs, action, reward, termination = replay_buffer.sample(batch_size, 0, batch_length)
    world_model.update(obs, action, reward, termination, logger=logger)


@torch.no_grad()
def world_model_imagine_data(replay_buffer, world_model, agent,
                             imagine_batch_size, imagine_context_length,
                             imagine_batch_length, logger):
    world_model.eval()
    agent.eval()
    sample_obs, sample_action, sample_reward, sample_termination = replay_buffer.sample(
        imagine_batch_size, 0, imagine_context_length
    )
    latent, action, reward_hat, termination_hat = world_model.imagine_data(
        agent, sample_obs, sample_action,
        imagine_batch_size=imagine_batch_size,
        imagine_batch_length=imagine_batch_length,
        log_video=False,
        logger=logger,
    )
    return latent, action, None, None, reward_hat, termination_hat


# ---------------------------------------------------------------------------
# Evaluation
# ---------------------------------------------------------------------------
@torch.no_grad()
def evaluate(world_model, agent, num_episodes=10, domain="walker", task="walk", seed=9999):
    """Greedy deterministic evaluation. Returns per-episode returns."""
    world_model.eval()
    agent.eval()
    eval_env = build_single_dmc_env(domain, task, seed=seed)
    returns = []
    for ep in range(num_episodes):
        obs, _ = eval_env.reset(seed=seed + ep)
        context_obs = deque(maxlen=16)
        context_action = deque(maxlen=16)
        ep_return = 0.0
        done = False
        while not done:
            obs_t = torch.from_numpy(obs).float().cuda().unsqueeze(0).unsqueeze(0)  # (1,1,obs_dim)
            if len(context_action) == 0:
                action = eval_env.action_space.sample()
            else:
                ctx_obs_tensor = torch.cat(list(context_obs), dim=1)
                context_latent = world_model.encode_obs(ctx_obs_tensor)
                model_ctx_action = np.stack(list(context_action), axis=1)
                model_ctx_action = torch.from_numpy(model_ctx_action).float().cuda()
                prior_flat, last_dist_feat = world_model.calc_last_dist_feat(
                    context_latent, model_ctx_action
                )
                action = agent.sample_as_env_action(
                    torch.cat([prior_flat, last_dist_feat], dim=-1),
                    greedy=True,
                )
                action = action[0]  # (action_dim,)
            context_obs.append(obs_t)
            context_action.append(action[np.newaxis])  # (1, action_dim)
            obs, reward, terminated, truncated, _ = eval_env.step(action)
            ep_return += reward
            done = terminated or truncated
        returns.append(ep_return)
    eval_env.close()
    return np.array(returns)


# ---------------------------------------------------------------------------
# Main training loop
# ---------------------------------------------------------------------------
def joint_train(conf, args, logger):
    wm_conf = conf.Models.WorldModel
    jt = conf.JointTrainAgent
    num_envs = jt.NumEnvs
    action_dim = wm_conf.ActionDim
    obs_dim = wm_conf.ObsDim

    os.makedirs(f"ckpt/{args.n}", exist_ok=True)

    # wandb init (optional)
    if HAS_WANDB:
        wandb.init(
            project="storm-dmc-civo",
            name=args.n,
            config={
                "seed": conf.BasicSettings.Seed,
                "obs_dim": wm_conf.ObsDim,
                "action_dim": wm_conf.ActionDim,
                "wm_lr": wm_conf.LearningRate,
                "agent_lr": conf.Models.Agent.LearningRate,
                "gamma": conf.Models.Agent.Gamma,
                "batch_size": jt.BatchSize,
                "imagine_horizon": jt.ImagineBatchLength,
                "max_steps": jt.SampleMaxSteps,
            },
        )

    # Build env, world model, agent, replay buffer
    vec_env = build_dmc_vec_env(
        domain="walker", task="walk", num_envs=num_envs, seed=conf.BasicSettings.Seed
    )
    print(colorama.Fore.YELLOW + "DMC Walker Walk" + colorama.Style.RESET_ALL)

    world_model = build_world_model(conf)
    agent = build_agent(conf)

    replay_buffer = ReplayBuffer(
        obs_dim=obs_dim,
        action_dim=action_dim,
        num_envs=num_envs,
        max_length=jt.BufferMaxLength,
        warmup_length=jt.BufferWarmUp,
        store_on_gpu=conf.BasicSettings.ReplayBufferOnGPU,
    )

    # Reset
    sum_reward = np.zeros(num_envs)
    current_obs, current_info = vec_env.reset()
    context_obs = deque(maxlen=16)
    context_action = deque(maxlen=16)

    for total_steps in tqdm(range(jt.SampleMaxSteps // num_envs)):
        # ---- Sample from environment ----
        if replay_buffer.ready():
            world_model.eval()
            agent.eval()
            with torch.no_grad():
                if len(context_action) == 0:
                    action = vec_env.action_space.sample()  # (num_envs, action_dim)
                else:
                    # Encode context observations
                    ctx_obs_tensor = torch.cat(list(context_obs), dim=1)  # (num_envs, ctx_len, obs_dim)
                    context_latent = world_model.encode_obs(ctx_obs_tensor)
                    # Stack context actions: each is (num_envs, action_dim)
                    model_context_action = np.stack(list(context_action), axis=1)  # (num_envs, ctx_len, action_dim)
                    model_context_action = torch.Tensor(model_context_action).cuda()
                    prior_flattened_sample, last_dist_feat = world_model.calc_last_dist_feat(
                        context_latent, model_context_action
                    )
                    action = agent.sample_as_env_action(
                        torch.cat([prior_flattened_sample, last_dist_feat], dim=-1),
                        greedy=False,
                    )

            # Append context: obs (num_envs, obs_dim) → (num_envs, 1, obs_dim)
            context_obs.append(torch.Tensor(current_obs).cuda().unsqueeze(1))
            context_action.append(action)
        else:
            action = vec_env.action_space.sample()  # (num_envs, action_dim)

        obs, reward, terminated, truncated, info = vec_env.step(action)
        # Only true task failures zero the bootstrap; truncation preserves value
        termination_for_buffer = terminated.astype(np.float32)
        replay_buffer.append(current_obs, action, reward, termination_for_buffer)

        done_flag = np.logical_or(terminated, truncated)
        if done_flag.any():
            for i in range(num_envs):
                if done_flag[i]:
                    ep_return = sum_reward[i]
                    env_steps = total_steps * num_envs
                    logger.log("sample/walker_walk_reward", ep_return)
                    logger.log("replay_buffer/length", len(replay_buffer))
                    if HAS_WANDB and wandb.run is not None:
                        wandb.log({"train/episode_return": ep_return,
                                   "env_steps": env_steps}, step=env_steps)
                    sum_reward[i] = 0
                    context_obs.clear()
                    context_action.clear()

        sum_reward += reward
        current_obs = obs
        current_info = info

        # ---- Train world model ----
        if replay_buffer.ready() and total_steps % (jt.TrainDynamicsEverySteps // num_envs) == 0:
            train_world_model_step(
                replay_buffer=replay_buffer,
                world_model=world_model,
                batch_size=jt.BatchSize,
                batch_length=jt.BatchLength,
                logger=logger,
            )

        # ---- Train agent (imagination) ----
        if replay_buffer.ready() and total_steps % (jt.TrainAgentEverySteps // num_envs) == 0:
            imagine_latent, agent_action, _, _, imagine_reward, imagine_termination = world_model_imagine_data(
                replay_buffer=replay_buffer,
                world_model=world_model,
                agent=agent,
                imagine_batch_size=jt.ImagineBatchSize,
                imagine_context_length=jt.ImagineContextLength,
                imagine_batch_length=jt.ImagineBatchLength,
                logger=logger,
            )
            agent.update(
                latent=imagine_latent,
                action=agent_action,
                old_logprob=None,
                old_value=None,
                reward=imagine_reward,
                termination=imagine_termination,
                logger=logger,
            )

        # ---- Evaluate (every 10K env steps) ----
        eval_every = 10000 // num_envs
        if replay_buffer.ready() and total_steps % eval_every == 0 and total_steps > 0:
            eval_returns = evaluate(world_model, agent, num_episodes=10)
            eval_mean = eval_returns.mean()
            eval_std = eval_returns.std()
            env_steps = total_steps * num_envs
            print(colorama.Fore.CYAN +
                  f"[Eval @ {env_steps}] return = {eval_mean:.1f} ± {eval_std:.1f}" +
                  colorama.Style.RESET_ALL)
            logger.log("eval/return_mean", eval_mean)
            logger.log("eval/return_std", eval_std)
            if HAS_WANDB and wandb.run is not None:
                wandb.log({"eval/return_mean": eval_mean, "eval/return_std": eval_std,
                           "env_steps": env_steps}, step=env_steps)

        # ---- Save checkpoint ----
        if total_steps % (jt.SaveEverySteps // num_envs) == 0 and total_steps > 0:
            print(colorama.Fore.GREEN + f"Saving at step {total_steps * num_envs}" + colorama.Style.RESET_ALL)
            torch.save(world_model.state_dict(), f"ckpt/{args.n}/world_model_{total_steps}.pth")
            torch.save(agent.state_dict(), f"ckpt/{args.n}/agent_{total_steps}.pth")

    # Final eval
    eval_returns = evaluate(world_model, agent, num_episodes=10)
    print(colorama.Fore.CYAN +
          f"[Final Eval] return = {eval_returns.mean():.1f} ± {eval_returns.std():.1f}" +
          colorama.Style.RESET_ALL)

    # Final save
    torch.save(world_model.state_dict(), f"ckpt/{args.n}/world_model_final.pth")
    torch.save(agent.state_dict(), f"ckpt/{args.n}/agent_final.pth")

    if HAS_WANDB and wandb.run is not None:
        wandb.finish()


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    import warnings
    warnings.filterwarnings("ignore")
    torch.backends.cuda.matmul.allow_tf32 = True
    torch.backends.cudnn.allow_tf32 = True

    parser = argparse.ArgumentParser()
    parser.add_argument("-n", type=str, required=True, help="Experiment name")
    parser.add_argument("-seed", type=int, default=0)
    parser.add_argument("-config_path", type=str, default="config/dmc_walker.yaml")
    parser.add_argument("--no-wandb", action="store_true", help="Disable wandb logging")
    args = parser.parse_args()

    if args.no_wandb:
        HAS_WANDB = False

    conf = load_dmc_config(args.config_path)
    print(colorama.Fore.RED + str(args) + colorama.Style.RESET_ALL)

    seed_np_torch(seed=args.seed)
    logger = Logger(path=f"runs/{args.n}")
    shutil.copy(args.config_path, f"runs/{args.n}/config.yaml")

    if conf.Task == "JointTrainAgent":
        joint_train(conf, args, logger)
    else:
        raise NotImplementedError(f"Task {conf.Task} not implemented")
