"""Lerobot-native precompute for ACR-VLA CRM training.

Uses lerobot's official SmolVLA inference path (same as eval), ensuring
action distribution consistency between precompute and eval.

Key differences from SmolVLAWrapper-based precompute:
  - Image 180° flip (both H and W) matching lerobot's LiberoProcessorStep
  - Uses lerobot's prepare_images / prepare_state pipeline directly
  - Language tokenization with smolvla_new_line_processor convention
  - Action unnormalization via dataset MEAN_STD stats

Model is called only at decision points (every chunk_size=50 env steps),
not at every env step. A 280-step episode has ~6 decision points.

Input:  LIBERO env + SmolVLA policy (lerobot/smolvla_libero)
Output: Per-decision-point .pt with {obs_features, actions_K, expert_action}
"""
import argparse
import functools
builtins_print = print
print = functools.partial(builtins_print, flush=True)
import os
os.environ.setdefault("HF_HUB_OFFLINE", "1")
os.environ.setdefault("TRANSFORMERS_OFFLINE", "1")
import sys
import time
from pathlib import Path

import torch
import numpy as np
from torchvision import transforms as T
from safetensors.torch import load_file
from robosuite.utils.transform_utils import quat2axisangle

from lerobot.policies.smolvla.modeling_smolvla import (
    SmolVLAPolicy,
    VLAFlowMatching,
    make_att_2d_masks,
)
from lerobot.utils.constants import OBS_STATE, OBS_LANGUAGE_TOKENS, OBS_LANGUAGE_ATTENTION_MASK

FULL_ACTION_DIM = 7
CORRECTION_DIM = 6

SUITE_MAX_STEPS = {"object": 280, "spatial": 280, "goal": 300, "long": 520, "90": 400}
BENCHMARK_MAP = {
    "spatial": "libero_spatial",
    "object": "libero_object",
    "goal": "libero_goal",
    "long": "libero_10",
    "90": "libero_90",
}


def parse_args():
    p = argparse.ArgumentParser(description="Lerobot-native precompute for CRM training")
    p.add_argument("--policy_path", type=str, default="/root/autodl-tmp/models/smolvla_libero/")
    p.add_argument("--suite", "--benchmark", type=str, default="object",
                   choices=["object", "spatial", "goal", "long", "90"])
    p.add_argument("--K", type=int, default=10)
    p.add_argument("--n_episodes", type=int, default=10)
    p.add_argument("--output_dir", type=str, required=True)
    p.add_argument("--seed", type=int, default=42)
    p.add_argument("--device", type=str, default="cuda")
    p.add_argument("--max_steps", type=int, default=None,
                   help="Override max steps per episode (default: suite-specific)")
    return p.parse_args()


def get_robot_state(obs):
    """8D robot state: eef_pos(3) + eef_axisangle(3) + gripper_qpos(2)."""
    eef_pos = obs["robot0_eef_pos"]
    eef_axisangle = quat2axisangle(obs["robot0_eef_quat"])
    gripper_qpos = obs["robot0_gripper_qpos"]
    return np.concatenate([eef_pos, eef_axisangle, gripper_qpos]).astype(np.float64)


def load_libero_env(suite_name):
    from libero.libero import benchmark as bm
    from libero.libero.envs import OffScreenRenderEnv

    bm_name = BENCHMARK_MAP[suite_name]
    benchmark_instance = bm.get_benchmark(bm_name)()

    task_envs = []
    for task_idx in range(benchmark_instance.n_tasks):
        task = benchmark_instance.get_task(task_idx)
        task_bddl = benchmark_instance.get_task_bddl_file_path(task_idx)
        env_args = {
            "bddl_file_name": task_bddl,
            "camera_heights": 256,
            "camera_widths": 256,
            "camera_names": ["agentview", "robot0_eye_in_hand"],
            "render_gpu_device_id": int(os.environ.get("MUJOCO_EGL_DEVICE_ID", "0")),
        }
        env = OffScreenRenderEnv(**env_args)
        env.seed(42)
        task_envs.append({
            "task_name": task.name,
            "task_description": task.language,
            "env": env,
            "init_states": benchmark_instance.get_task_init_states(task_idx),
        })
    return task_envs


class LerobotNativePrecomputer:
    """Precompute using lerobot's official SmolVLA inference path.

    Replicates the exact preprocessing pipeline from lerobot eval:
      1. Images: ToTensor [0,1] → prepare_images (resize_with_pad + normalize [-1,1])
      2. State: 8D → MEAN_STD normalize → prepare_state (pad to 32D)
      3. Language: append \\n → tokenize (max_length=48, padding=max_length)
    Then uses VLAFlowMatching.sample_actions for action generation (same as
    SmolVLAPolicy._get_action_chunk → model.sample_actions).
    """

    def __init__(self, policy_path, device="cuda"):
        self.device = torch.device(device)

        print(f"Loading SmolVLA from {policy_path}...")
        self.policy = SmolVLAPolicy.from_pretrained(policy_path)
        self.policy.to(self.device)
        self.policy.eval()
        for p in self.policy.parameters():
            p.requires_grad = False

        self.flow: VLAFlowMatching = self.policy.model
        self.config = self.policy.config
        self.processor = self.flow.vlm_with_expert.processor
        self.tokenizer = self.processor.tokenizer

        model_dir = Path(policy_path)
        pre_stats = load_file(str(model_dir / "policy_preprocessor_step_5_normalizer_processor.safetensors"))
        post_stats = load_file(str(model_dir / "policy_postprocessor_step_0_unnormalizer_processor.safetensors"))

        self.state_mean = pre_stats["observation.state.mean"].to(self.device)
        self.state_std = pre_stats["observation.state.std"].to(self.device)
        self.action_mean = post_stats["action.mean"].to(self.device)
        self.action_std = post_stats["action.std"].to(self.device)

        self.vlm_hidden_size = self.flow.vlm_with_expert.config.text_config.hidden_size
        self._to_tensor = T.ToTensor()

        print(f"  hidden_size={self.vlm_hidden_size}, "
              f"expert_hidden_size={self.flow.vlm_with_expert.expert_hidden_size}, "
              f"chunk_size={self.config.chunk_size}, "
              f"action_dim={self.config.action_feature.shape[0]}")

    def _normalize_state(self, state_raw):
        D = state_raw.shape[-1]
        return (state_raw - self.state_mean[:D]) / (self.state_std[:D] + 1e-8)

    def _unnormalize_action(self, action_norm):
        return action_norm * self.action_std + self.action_mean

    @torch.no_grad()
    def build_batch(self, obs, task_description):
        """Convert raw LIBERO obs → lerobot batch dict.

        Matches the lerobot preprocessor pipeline exactly:
          rename_observations → to_batch → smolvla_new_line → tokenizer → device → normalizer
        """
        dev = self.device
        batch = {}

        # Images: HWC uint8 → CHW float [0,1] → flip 180° (matching LiberoProcessorStep)
        agentview = self._to_tensor(obs["agentview_image"]).unsqueeze(0).to(dev)
        agentview = torch.flip(agentview, dims=[2, 3])
        batch["observation.images.camera1"] = agentview

        eye_in_hand = self._to_tensor(obs["robot0_eye_in_hand_image"]).unsqueeze(0).to(dev)
        eye_in_hand = torch.flip(eye_in_hand, dims=[2, 3])
        batch["observation.images.camera2"] = eye_in_hand

        # State: 8D → MEAN_STD normalize
        robot_state = get_robot_state(obs)
        state_t = torch.tensor(robot_state, dtype=torch.float32, device=dev)
        state_norm = self._normalize_state(state_t)
        batch[OBS_STATE] = state_norm.unsqueeze(0)

        # Language: append \n then tokenize (matches smolvla_new_line_processor + tokenizer_processor)
        task_text = task_description if task_description.endswith("\n") else f"{task_description}\n"
        tokens = self.tokenizer(
            task_text,
            return_tensors="pt",
            padding="max_length",
            max_length=self.config.tokenizer_max_length,
            truncation=True,
        )
        batch[OBS_LANGUAGE_TOKENS] = tokens["input_ids"].to(dev)
        batch[OBS_LANGUAGE_ATTENTION_MASK] = tokens["attention_mask"].to(dev).bool()

        return batch

    @torch.no_grad()
    def precompute_step(self, batch, K):
        """One precompute step: obs → (obs_features, K action chunks).

        Uses lerobot's prepare_images + prepare_state, then:
          1. embed_prefix → VLM forward → obs_features (mean-pooled) + KV cache
          2. K × denoise loop with fresh noise → K unnormalized action chunks

        The KV cache stores the deterministic prefix representation. Only the
        action denoising noise varies across K samples, matching model.sample_actions
        semantics exactly.
        """
        images, img_masks = self.policy.prepare_images(batch)
        state = self.policy.prepare_state(batch)
        lang_tokens = batch[OBS_LANGUAGE_TOKENS]
        lang_masks = batch[OBS_LANGUAGE_ATTENTION_MASK]

        # --- prefix encoding (run once) ---
        prefix_embs, prefix_pad_masks, prefix_att_masks = self.flow.embed_prefix(
            images, img_masks, lang_tokens, lang_masks, state=state
        )
        prefix_att_2d_masks = make_att_2d_masks(prefix_pad_masks, prefix_att_masks)
        prefix_position_ids = torch.cumsum(prefix_pad_masks, dim=1) - 1

        outputs_embeds, past_key_values = self.flow.vlm_with_expert.forward(
            attention_mask=prefix_att_2d_masks,
            position_ids=prefix_position_ids,
            past_key_values=None,
            inputs_embeds=[prefix_embs, None],
            use_cache=self.config.use_cache,
            fill_kv_cache=True,
        )

        # obs_features: mean-pool VLM hidden states over valid prefix tokens
        vlm_hidden = outputs_embeds[0]  # (B, seq_len, hidden_size)
        mask = prefix_pad_masks.unsqueeze(-1).float()
        obs_features = (vlm_hidden.float() * mask).sum(1) / mask.sum(1).clamp(min=1)

        # --- K action samples via cached prefix ---
        B = prefix_pad_masks.shape[0]
        chunk_size = self.config.chunk_size
        max_action_dim = self.config.max_action_dim
        original_dim = self.config.action_feature.shape[0]
        num_steps = self.config.num_steps
        dt = -1.0 / num_steps
        dev = prefix_pad_masks.device

        all_actions = []
        for _ in range(K):
            noise = self.flow.sample_noise((B, chunk_size, max_action_dim), dev)
            x_t = noise
            for step in range(num_steps):
                t = 1.0 + step * dt
                time_tensor = torch.tensor(t, dtype=torch.float32, device=dev).expand(B)
                v_t = self.flow.denoise_step(
                    x_t=x_t,
                    prefix_pad_masks=prefix_pad_masks,
                    past_key_values=past_key_values,
                    timestep=time_tensor,
                )
                x_t = x_t + dt * v_t

            actions = x_t[:, :, :original_dim]
            actions = self._unnormalize_action(actions)
            all_actions.append(actions)

        actions_K = torch.stack(all_actions, dim=1)  # (B, K, chunk_size, action_dim)
        return obs_features, actions_K


def main():
    args = parse_args()
    torch.manual_seed(args.seed)
    np.random.seed(args.seed)

    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    precomputer = LerobotNativePrecomputer(args.policy_path, device=args.device)

    print(f"Loading LIBERO {args.suite} envs...")
    task_envs = load_libero_env(args.suite)
    print(f"Loaded {len(task_envs)} tasks")

    max_steps = args.max_steps or SUITE_MAX_STEPS.get(args.suite, 300)

    all_obs_features = []
    all_actions_K = []
    all_expert_actions = []
    total_decision_points = 0
    total_env_steps = 0
    t0 = time.time()
    chunk_size = precomputer.config.chunk_size

    for task_idx, task_info in enumerate(task_envs):
        task_desc = task_info["task_description"]
        env = task_info["env"]
        init_states = task_info["init_states"]
        n_eps = min(args.n_episodes, len(init_states))
        print(f"\nTask {task_idx}: {task_desc} ({n_eps} eps, max_steps={max_steps}, chunk_size={chunk_size})")

        for ep_idx in range(n_eps):
            env.reset()
            obs = env.set_init_state(init_states[ep_idx])
            # Warmup: let physics settle after init state placement (lerobot convention)
            for _ in range(10):
                obs, _, _, _ = env.step(np.array([0, 0, 0, 0, 0, 0, -1], dtype=np.float64))
            precomputer.policy.reset()

            ep_env_steps = 0
            ep_decision_points = 0
            done = False
            ep_t0 = time.time()

            while ep_env_steps < max_steps and not done:
                batch = precomputer.build_batch(obs, task_desc)
                obs_feat, actions_K = precomputer.precompute_step(batch, K=args.K)
                expert_chunk = actions_K[:, 0]  # (1, chunk_size, action_dim)

                all_obs_features.append(obs_feat.cpu().squeeze(0))
                all_actions_K.append(actions_K.cpu().squeeze(0))
                all_expert_actions.append(expert_chunk.cpu().squeeze(0))
                ep_decision_points += 1
                total_decision_points += 1

                for cs in range(chunk_size):
                    if ep_env_steps >= max_steps:
                        break
                    action_np = expert_chunk[0, cs].cpu().numpy()
                    obs, reward, done, info = env.step(action_np)
                    ep_env_steps += 1
                    if done:
                        break

            total_env_steps += ep_env_steps
            success = env.check_success()
            ep_elapsed = time.time() - ep_t0
            print(f"  ep {ep_idx}: {ep_env_steps} env steps, {ep_decision_points} decision points, "
                  f"success={success}, {ep_elapsed:.1f}s")

        env.close()

    elapsed = time.time() - t0

    obs_features_all = torch.stack(all_obs_features)
    actions_K_all = torch.stack(all_actions_K)
    expert_actions_all = torch.stack(all_expert_actions)

    save_path = output_dir / "precomputed.pt"
    torch.save({
        "obs_features": obs_features_all,
        "actions_K": actions_K_all,
        "expert_action": expert_actions_all,
        "metadata": {
            "suite": args.suite,
            "K": args.K,
            "n_episodes": args.n_episodes,
            "total_decision_points": total_decision_points,
            "total_env_steps": total_env_steps,
            "chunk_size": chunk_size,
            "action_dim": int(precomputer.config.action_feature.shape[0]),
            "obs_dim": precomputer.vlm_hidden_size,
            "seed": args.seed,
        }
    }, save_path)

    print(f"\n{'='*60}")
    print(f"Saved to {save_path}")
    print(f"obs_features:  {obs_features_all.shape}")
    print(f"actions_K:     {actions_K_all.shape}")
    print(f"expert_action: {expert_actions_all.shape}")
    print(f"Decision pts:  {total_decision_points}")
    print(f"Env steps:     {total_env_steps}")
    print(f"Elapsed:       {elapsed:.1f}s ({elapsed/max(total_decision_points,1):.2f}s/decision_point)")

    # --- Sanity checks ---
    print(f"\n{'='*60}")
    print("Sanity Checks")
    print(f"  obs_features range: [{obs_features_all.min():.4f}, {obs_features_all.max():.4f}]")
    print(f"  obs_features NaN: {obs_features_all.isnan().any().item()}")
    print(f"  obs_features Inf: {obs_features_all.isinf().any().item()}")
    print(f"  actions_K range:  [{actions_K_all.min():.4f}, {actions_K_all.max():.4f}]")
    print(f"  actions_K NaN:    {actions_K_all.isnan().any().item()}")

    # K-sample diversity: pairwise L2 on first chunk step
    a = actions_K_all[:, :, 0, :]  # (N, K, 7) — first step of each chunk
    K = args.K
    dists = []
    for i in range(K):
        for j in range(i + 1, K):
            d = (a[:, i] - a[:, j]).norm(dim=-1)
            dists.append(d.mean().item())
    mean_pw_l2 = np.mean(dists) if dists else 0
    print(f"  Pairwise L2 (K={K}, step 0): {mean_pw_l2:.6f}")

    # Per-DOF std across K samples
    per_dof_std = actions_K_all[:, :, 0, :].std(dim=1).mean(dim=0)
    print(f"  Per-DOF std (K samples, step 0): {per_dof_std.tolist()}")


if __name__ == "__main__":
    main()
