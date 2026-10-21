"""
eval_sim.py — Success rate evaluation in aloha_sim_insertion

Usage:
    CUDA_VISIBLE_DEVICES=1 python eval_sim.py --mode baseline --n_episodes 50 --gpu 0
    CUDA_VISIBLE_DEVICES=1 python eval_sim.py --mode acis_prune --n_episodes 50 --gpu 0
    CUDA_VISIBLE_DEVICES=1 python eval_sim.py --mode bypass --n_episodes 50 --gpu 0
"""

from __future__ import annotations

import argparse
import json
import logging
import os
import sys
import time as time_mod
from pathlib import Path

os.environ.setdefault("MUJOCO_GL", "egl")
os.environ.setdefault("TRANSFORMERS_OFFLINE", "1")
os.environ.setdefault("HF_HUB_OFFLINE", "1")

import numpy as np
import torch

ARTIFACTS_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(ARTIFACTS_DIR))

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
log = logging.getLogger(__name__)

TASK_TEXT = "Insert the peg into the socket.\n"


def parse_args():
    p = argparse.ArgumentParser()
    p.add_argument("--mode", choices=["baseline", "acis_prune", "bypass"], required=True)
    p.add_argument("--n_episodes", type=int, default=50)
    p.add_argument("--gpu", type=int, default=0)
    p.add_argument("--max_steps", type=int, default=400)
    p.add_argument("--action_horizon", type=int, default=50,
                   help="Actions to execute per chunk before re-planning")
    p.add_argument("--seed", type=int, default=42)
    p.add_argument("--output", type=str, default="eval_results/sim_success_rate.json")
    return p.parse_args()


# ─── Config loading ────────────────────────────────────────────────────────────

def load_config(config_path: str) -> dict:
    import copy
    import yaml
    config_path = Path(config_path)
    with open(config_path) as f:
        config = yaml.safe_load(f)
    if "_base_" in config:
        base_path = config_path.parent / config.pop("_base_")
        base_config = load_config(str(base_path))
        for k, v in config.items():
            if k in base_config and isinstance(base_config[k], dict) and isinstance(v, dict):
                base_config[k].update(v)
            else:
                base_config[k] = v
        return base_config
    return config


# ─── Model loading ─────────────────────────────────────────────────────────────

def load_model(mode: str, device: torch.device):
    """Returns (policy, wrapper_or_None, config)."""
    from train import load_smolvla_policy, wrap_with_imm

    if mode == "baseline":
        config = load_config("configs/baseline.yaml")
        policy = load_smolvla_policy(config, device)
        ckpt = torch.load(
            "checkpoints/baseline/latest/checkpoint.pt",
            map_location=device, weights_only=False,
        )
        policy.load_state_dict(ckpt["model_state_dict"], strict=False)
        policy.eval()
        return policy, None, config

    config = load_config("configs/imm_anchor_v8b_twostage.yaml")
    policy = load_smolvla_policy(config, device)
    wrapper = wrap_with_imm(policy, config)
    wrapper.to(device)
    ckpt = torch.load(
        "checkpoints/imm_anchor_v8b_twostage/final/checkpoint.pt",
        map_location=device, weights_only=False,
    )
    wrapper.load_state_dict(ckpt["model_state_dict"], strict=False)
    wrapper.eval()
    return wrapper.policy, wrapper, config


# ─── Observation → batch conversion ───────────────────────────────────────────

def obs_to_batch(obs: dict, tokenizer, device: torch.device) -> dict:
    img = obs["pixels"]["top"]  # (480, 640, 3) uint8
    state = obs["agent_pos"]    # (14,) float64

    img_t = torch.from_numpy(np.asarray(img)).permute(2, 0, 1).float() / 255.0
    img_t = img_t.unsqueeze(0).to(device)

    state_t = torch.from_numpy(np.asarray(state, dtype=np.float32)).unsqueeze(0).to(device)

    encoded = tokenizer(
        [TASK_TEXT], padding="longest", max_length=48,
        truncation=True, return_tensors="pt",
    )
    lang_tokens = encoded["input_ids"].to(device)
    lang_mask = encoded["attention_mask"].bool().to(device)

    return {
        "observation.images.top": img_t,
        "observation.state": state_t,
        "observation.language.tokens": lang_tokens,
        "observation.language.attention_mask": lang_mask,
    }


# ─── ACIS pruning hook ────────────────────────────────────────────────────────

def find_connector(model):
    for name, module in model.named_modules():
        if name.endswith(".connector") or "multi_modal_projector" in name:
            return module
    return None


@torch.no_grad()
def compute_acis_mask(wrapper, batch: dict, device: torch.device) -> torch.Tensor:
    bm = wrapper.base_model
    images, _ = wrapper.policy.prepare_images(batch)
    vis_tokens, _ = wrapper._get_visual_tokens(images)

    B = vis_tokens.shape[0]
    noise = bm.sample_noise(
        (B, bm.config.chunk_size, bm.config.max_action_dim), device
    )
    time = torch.ones(B, device=device)
    suffix_embs, _, _ = bm.embed_suffix(noise, time)

    scores = wrapper.acis(suffix_embs, vis_tokens)

    N_vis = vis_tokens.shape[1]
    k = max(1, int(N_vis * wrapper.k_ratio))
    _, topk_idx = torch.topk(scores, k, dim=-1)
    mask = torch.zeros(B, N_vis, device=device)
    mask.scatter_(1, topk_idx, 1.0)
    return mask


def register_acis_hook(connector, mask: torch.Tensor):
    def hook_fn(module, input, output):
        tokens = output[0] if isinstance(output, tuple) else output
        if tokens.dim() != 3 or tokens.shape[1] != mask.shape[1]:
            return output
        masked = tokens * mask[: tokens.shape[0]].unsqueeze(-1)
        if isinstance(output, tuple):
            return (masked,) + output[1:]
        return masked

    return connector.register_forward_hook(hook_fn)


# ─── Action prediction ─────────────────────────────────────────────────────────

@torch.no_grad()
def predict_actions(policy, batch: dict) -> torch.Tensor:
    """Returns (chunk_size, action_dim) actions for batch_size=1."""
    images, img_masks = policy.prepare_images(batch)
    state = policy.prepare_state(batch)
    lang_tokens = batch["observation.language.tokens"]
    lang_masks = batch["observation.language.attention_mask"]

    actions = policy.model.sample_actions(
        images, img_masks, lang_tokens, lang_masks, state
    )
    original_action_dim = policy.config.action_feature.shape[0]
    return actions[0, :, :original_action_dim]  # (chunk_size, action_dim)


# ─── Statistics ────────────────────────────────────────────────────────────────

def wilson_ci(successes: int, total: int, z: float = 1.96):
    if total == 0:
        return 0.0, 0.0, 1.0
    p = successes / total
    denom = 1 + z ** 2 / total
    center = (p + z ** 2 / (2 * total)) / denom
    spread = z * np.sqrt((p * (1 - p) + z ** 2 / (4 * total)) / total) / denom
    return center, max(0.0, center - spread), min(1.0, center + spread)


# ─── Main evaluation loop ─────────────────────────────────────────────────────

def run_evaluation(args):
    device = torch.device(f"cuda:{args.gpu}" if torch.cuda.is_available() else "cpu")
    log.info("Device: %s | Mode: %s | Episodes: %d", device, args.mode, args.n_episodes)

    np.random.seed(args.seed)
    torch.manual_seed(args.seed)

    log.info("Loading model...")
    t0 = time_mod.time()
    policy, wrapper, config = load_model(args.mode, device)
    log.info("Model loaded in %.1fs", time_mod.time() - t0)

    from train import get_tokenizer_from_policy
    tokenizer = get_tokenizer_from_policy(policy)

    connector = None
    if args.mode == "acis_prune":
        connector = find_connector(policy.model)
        if connector is None:
            raise RuntimeError("Cannot find visual connector for ACIS hook")
        log.info("Connector found for ACIS pruning")

    import gymnasium as gym
    import gym_aloha
    env = gym.make("gym_aloha/AlohaInsertion-v0", obs_type="pixels_agent_pos")

    successes = []
    episode_lengths = []
    rewards_all = []

    for ep in range(args.n_episodes):
        obs, info = env.reset(seed=args.seed + ep)
        action_chunk = None
        action_idx = 0
        total_reward = 0.0
        success = False

        for step in range(args.max_steps):
            if action_chunk is None or action_idx >= args.action_horizon:
                batch = obs_to_batch(obs, tokenizer, device)

                if args.mode == "acis_prune":
                    mask = compute_acis_mask(wrapper, batch, device)
                    hook_handle = register_acis_hook(connector, mask)
                    action_chunk = predict_actions(policy, batch)
                    hook_handle.remove()
                else:
                    action_chunk = predict_actions(policy, batch)

                action_idx = 0

            action = action_chunk[action_idx].cpu().numpy().astype(np.float32)
            action = np.clip(action, -1.0, 1.0)
            action_idx += 1

            obs, reward, terminated, truncated, info = env.step(action)
            total_reward += reward

            if info.get("is_success", False):
                success = True
                break

            if terminated or truncated:
                break

        successes.append(success)
        episode_lengths.append(step + 1)
        rewards_all.append(total_reward)

        if (ep + 1) % 10 == 0 or (ep + 1) == args.n_episodes:
            sr = sum(successes) / len(successes)
            log.info(
                "Ep %d/%d | last=%s steps=%d | running SR=%.1f%%",
                ep + 1, args.n_episodes, success, step + 1, sr * 100,
            )

    env.close()

    n_success = sum(successes)
    n_total = len(successes)
    rate = n_success / n_total
    _, ci_lo, ci_hi = wilson_ci(n_success, n_total)

    succ_lengths = [l for s, l in zip(successes, episode_lengths) if s]
    mean_succ_len = float(np.mean(succ_lengths)) if succ_lengths else float("nan")

    summary = {
        "mode": args.mode,
        "n_episodes": n_total,
        "success_count": n_success,
        "success_rate": rate,
        "wilson_ci_95": [round(ci_lo, 4), round(ci_hi, 4)],
        "mean_episode_length_successful": round(mean_succ_len, 1),
        "mean_reward": round(float(np.mean(rewards_all)), 4),
        "seed": args.seed,
        "action_horizon": args.action_horizon,
    }

    log.info("═══ %s ═══", args.mode.upper())
    log.info("Success: %d/%d (%.1f%%)", n_success, n_total, rate * 100)
    log.info("95%% Wilson CI: [%.1f%%, %.1f%%]", ci_lo * 100, ci_hi * 100)
    log.info("Mean ep length (success): %.1f", mean_succ_len)
    log.info("Mean reward: %.4f", float(np.mean(rewards_all)))

    output_path = Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    all_results = {}
    if output_path.exists():
        with open(output_path) as f:
            all_results = json.load(f)
    all_results[args.mode] = summary

    with open(output_path, "w") as f:
        json.dump(all_results, f, indent=2)
    log.info("Saved to %s", output_path)

    return summary


if __name__ == "__main__":
    args = parse_args()
    run_evaluation(args)
