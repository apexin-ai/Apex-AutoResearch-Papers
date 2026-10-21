"""X-VLA Vision Token Pruning Evaluation on LIBERO.

Prunes vision tokens by L2 norm after Florence2's image encoder + linear projection,
before they enter the Florence2 language encoder. Evaluates on LIBERO suites.

Follows official X-VLA evaluation protocol:
  - Absolute EEF control (use_delta=False)
  - 20D action space: [arm1: pos(3)+rot6d(6)+grip(1)] + [arm2: zeros(10)]
  - 20D proprio: [pos(3)+rot6d(6)+0.0] + zeros(10)
  - domain_id=3 for LIBERO
  - Closed-loop proprio update from last predicted action

Usage:
    CUDA_VISIBLE_DEVICES=0 MUJOCO_GL=egl python eval_xvla_pruning_libero.py \
        --model_path /path/to/X-VLA-Libero \
        --suite libero_object \
        --keep_ratio 0.5 \
        --num_episodes 50 \
        --gpu 0
"""

from __future__ import annotations

import argparse
import json
import logging
import os
import sys
import time as time_mod
from pathlib import Path
from functools import wraps

os.environ.setdefault("MUJOCO_GL", "egl")

import numpy as np
import torch
from PIL import Image

sys.path.insert(0, str(Path(__file__).resolve().parent))

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
log = logging.getLogger(__name__)

SUITE_MAX_STEPS = {
    "libero_spatial": 800,
    "libero_object": 800,
    "libero_goal": 800,
    "libero_10": 900,
    "libero_90": 800,
}

EPS = 1e-6


def parse_args():
    p = argparse.ArgumentParser(description="X-VLA pruning eval on LIBERO")
    p.add_argument("--model_path", type=str, default="2toINF/X-VLA-Libero",
                   help="HuggingFace model path or local dir")
    p.add_argument("--suite", type=str, default="libero_object",
                   choices=list(SUITE_MAX_STEPS.keys()))
    p.add_argument("--keep_ratio", type=float, default=1.0,
                   help="Fraction of vision tokens to keep (1.0 = no pruning)")
    p.add_argument("--num_episodes", type=int, default=50)
    p.add_argument("--gpu", type=int, default=0)
    p.add_argument("--seed", type=int, default=42)
    p.add_argument("--max_steps", type=int, default=None)
    p.add_argument("--output", type=str, default=None)
    p.add_argument("--task_ids", type=str, default=None)
    p.add_argument("--domain_id", type=int, default=3)
    p.add_argument("--denoise_steps", type=int, default=10,
                   help="Flow matching denoising steps")
    p.add_argument("--mode", type=str, default="l2_norm",
                   choices=["l2_norm", "random"],
                   help="Pruning method: l2_norm (keep highest L2 norm tokens) or random (random selection)")
    return p.parse_args()


# ---------------------------------------------------------------------------
# Pruning hook
# ---------------------------------------------------------------------------

def install_vision_pruning(model, keep_ratio: float, mode: str = "l2_norm"):
    if keep_ratio >= 1.0:
        log.info("keep_ratio=%.2f, no pruning applied", keep_ratio)
        return

    original_encode = model.vlm._encode_image

    @wraps(original_encode)
    def pruned_encode(pixel_values):
        features = original_encode(pixel_values)
        N = features.shape[1]
        k = max(1, int(keep_ratio * N))
        if k >= N:
            return features
        if mode == "l2_norm":
            norms = features.norm(dim=-1)
            _, indices = norms.topk(k, dim=-1)
        elif mode == "random":
            indices = torch.stack([
                torch.randperm(N, device=features.device)[:k]
                for _ in range(features.shape[0])
            ], dim=0)
        indices_sorted = indices.sort(dim=-1).values
        pruned = features.gather(
            1, indices_sorted.unsqueeze(-1).expand(-1, -1, features.shape[-1])
        )
        return pruned

    model.vlm._encode_image = pruned_encode
    log.info("Vision pruning installed: keep_ratio=%.2f, mode=%s", keep_ratio, mode)


# ---------------------------------------------------------------------------
# Model loading
# ---------------------------------------------------------------------------

def load_model(model_path: str, device: torch.device):
    model_dir = str(Path(model_path).resolve())
    sys.path.insert(0, model_dir)

    from configuration_xvla import XVLAConfig
    from modeling_xvla import XVLA
    from processing_xvla import XVLAProcessor
    from safetensors.torch import load_file

    log.info("Loading X-VLA from %s", model_dir)
    config = XVLAConfig.from_pretrained(model_dir)
    model = XVLA(config)

    safetensors_path = Path(model_dir) / "model.safetensors"
    if safetensors_path.exists():
        state_dict = load_file(str(safetensors_path))
    else:
        import torch as _torch
        state_dict = _torch.load(Path(model_dir) / "pytorch_model.bin", map_location="cpu")
    model.load_state_dict(state_dict, strict=False)
    model = model.to(device).eval()

    processor = XVLAProcessor.from_pretrained(model_dir, trust_remote_code=True)
    if processor.tokenizer.pad_token is None:
        processor.tokenizer.pad_token = "<pad>"
        processor.tokenizer.pad_token_id = 1

    n_params = sum(p.numel() for p in model.parameters())
    log.info("Model loaded: %.1fM params, dtype=%s", n_params / 1e6, model.dtype)
    return model, processor


# ---------------------------------------------------------------------------
# 6D rotation utilities (following X-VLA's convention)
# ---------------------------------------------------------------------------

def mat_to_rot6d(R: np.ndarray) -> np.ndarray:
    """Extract 6D rotation from 3x3 rotation matrix: first two columns."""
    return np.concatenate([R[:3, 0], R[:3, 1]], axis=-1).astype(np.float32)


def rot6d_to_axis_angle(r6d: np.ndarray) -> np.ndarray:
    """Convert 6D rotation representation to axis-angle via Gram-Schmidt."""
    import robosuite.utils.transform_utils as T

    single = r6d.ndim == 1
    if single:
        r6d = r6d[None, :]

    a1 = r6d[:, 0:3]
    a2 = r6d[:, 3:6]

    b1 = a1 / (np.linalg.norm(a1, axis=-1, keepdims=True) + EPS)
    dot_prod = np.sum(b1 * a2, axis=-1, keepdims=True)
    b2_orth = a2 - dot_prod * b1
    b2 = b2_orth / (np.linalg.norm(b2_orth, axis=-1, keepdims=True) + EPS)
    b3 = np.cross(b1, b2, axis=-1)

    R = np.stack([b1, b2, b3], axis=-1)  # (N, 3, 3)

    results = []
    for i in range(R.shape[0]):
        quat = T.mat2quat(R[i])
        aa = T.quat2axisangle(quat)
        results.append(aa)

    result = np.stack(results, axis=0)
    return result[0] if single else result


# ---------------------------------------------------------------------------
# Observation processing
# ---------------------------------------------------------------------------

def extract_proprio_20d(env) -> np.ndarray:
    """Extract 20D proprio: [pos(3)+rot6d(6)+0.0] + zeros(10) from env robot state."""
    robot = env.env.robots[0]
    ee_pos = robot.controller.ee_pos.copy()         # (3,)
    ee_ori_mat = robot.controller.ee_ori_mat.copy()  # (3, 3)
    ee_rot6d = mat_to_rot6d(ee_ori_mat)              # (6,)

    arm1 = np.concatenate([ee_pos, ee_rot6d, np.array([0.0], dtype=np.float32)])  # (10,)
    arm2 = np.zeros(10, dtype=np.float32)
    return np.concatenate([arm1, arm2])  # (20,)


def decode_action_20d_to_7d(action_20d: np.ndarray) -> np.ndarray:
    """Convert 20D X-VLA action to 7D LIBERO action.

    Input:  [pos(3), rot6d(6), grip(1), arm2(10)]  — only arm1 used
    Output: [pos(3), axis_angle(3), grip(1)]
    """
    single = action_20d.ndim == 1
    if single:
        action_20d = action_20d[None, :]

    pos = action_20d[:, :3]
    rot6d = action_20d[:, 3:9]
    grip = action_20d[:, 9:10]

    axis_angle = rot6d_to_axis_angle(rot6d)

    # Discretize gripper: >0.5 → 1.0 (open), else -1.0 (close)
    grip_disc = np.where(grip > 0.5, 1.0, -1.0)

    result = np.concatenate([pos, axis_angle, grip_disc], axis=-1).astype(np.float32)
    return result[0] if single else result


def get_images_from_obs(obs) -> list:
    """Extract camera images from LIBERO observation, apply agentview flip."""
    images = []
    for cam_name in ["agentview_image", "robot0_eye_in_hand_image"]:
        img = obs.get(cam_name, None)
        if img is None:
            for k, v in obs.items():
                if cam_name in k and isinstance(v, np.ndarray):
                    img = v
                    break
        if img is not None:
            if img.dtype in (np.float32, np.float64):
                img = (np.clip(img, 0, 1) * 255).astype(np.uint8)
            if cam_name == "agentview_image":
                img = np.flip(np.flip(img, 0), 1).copy()
            images.append(Image.fromarray(img))
    return images


# ---------------------------------------------------------------------------
# Action prediction
# ---------------------------------------------------------------------------

@torch.no_grad()
def predict_actions(model, processor, images, task_desc, proprio_20d, domain_id,
                    device, denoise_steps=10):
    inputs = processor(images=images, language_instruction=task_desc)

    proprio_t = torch.tensor(proprio_20d, dtype=torch.float32).unsqueeze(0).to(device)
    domain_t = torch.tensor([domain_id], dtype=torch.long).to(device)

    for k, v in inputs.items():
        if isinstance(v, torch.Tensor):
            if v.is_floating_point():
                inputs[k] = v.to(device=device, dtype=torch.float32)
            else:
                inputs[k] = v.to(device=device)

    actions = model.generate_actions(
        input_ids=inputs["input_ids"],
        image_input=inputs["image_input"],
        image_mask=inputs["image_mask"],
        proprio=proprio_t,
        domain_id=domain_t,
        steps=denoise_steps,
    )  # [1, 30, 20]

    return actions.squeeze(0).float().cpu().numpy()  # [30, 20]


# ---------------------------------------------------------------------------
# Wilson CI
# ---------------------------------------------------------------------------

def wilson_ci(successes, total, z=1.96):
    if total == 0:
        return 0.0, 0.0, 1.0
    p = successes / total
    denom = 1 + z ** 2 / total
    center = (p + z ** 2 / (2 * total)) / denom
    spread = z * np.sqrt((p * (1 - p) + z ** 2 / (4 * total)) / total) / denom
    return center, max(0.0, center - spread), min(1.0, center + spread)


# ---------------------------------------------------------------------------
# Main evaluation
# ---------------------------------------------------------------------------

def run_evaluation(args):
    device = torch.device(f"cuda:{args.gpu}" if torch.cuda.is_available() else "cpu")
    max_steps = args.max_steps or SUITE_MAX_STEPS.get(args.suite, 800)
    output_path = Path(args.output or
                       f"eval_results/xvla_prune_k{args.keep_ratio}_{args.suite}.json")

    log.info("Suite: %s | Device: %s | keep_ratio=%.2f | Episodes/task: %d | Max steps: %d",
             args.suite, device, args.keep_ratio, args.num_episodes, max_steps)

    np.random.seed(args.seed)
    torch.manual_seed(args.seed)

    t0 = time_mod.time()
    model, processor = load_model(args.model_path, device)
    log.info("Model loaded in %.1fs", time_mod.time() - t0)

    dummy_img = torch.randn(1, 3, 224, 224, device=device)
    with torch.no_grad():
        dummy_feats = model.vlm._encode_image(dummy_img)
    n_vis_tokens = dummy_feats.shape[1]
    k_tokens = max(1, int(args.keep_ratio * n_vis_tokens))
    log.info("Vision tokens: %d total, keeping %d (%.0f%%)",
             n_vis_tokens, k_tokens, args.keep_ratio * 100)

    install_vision_pruning(model, args.keep_ratio, args.mode)

    num_actions_per_chunk = model.num_actions  # 30

    # LIBERO setup — use OffScreenRenderEnv directly (matching official X-VLA eval)
    from libero.libero import benchmark, get_libero_path
    from libero.libero.envs import OffScreenRenderEnv

    task_suite = benchmark.get_benchmark(args.suite)()
    n_tasks = task_suite.n_tasks

    if args.task_ids:
        task_id_list = [int(x) for x in args.task_ids.split(",")]
    else:
        task_id_list = list(range(n_tasks))

    eval_start = time_mod.time()
    all_task_results = {}
    total_successes = 0
    total_episodes = 0

    for task_id in task_id_list:
        task = task_suite.get_task(task_id)
        task_desc = task.language
        task_bddl = os.path.join(
            get_libero_path("bddl_files"), task.problem_folder, task.bddl_file
        )
        log.info("--- Task %d: %s ---", task_id, task_desc)

        init_states = task_suite.get_task_init_states(task_id)

        task_successes = []
        task_lengths = []

        for ep in range(args.num_episodes):
            env = OffScreenRenderEnv(
                bddl_file_name=task_bddl,
                camera_heights=256,
                camera_widths=256,
            )
            env.seed(args.seed + ep + 100)
            obs = env.reset()

            init_state_id = ep % init_states.shape[0]
            obs = env.set_init_state(init_states[init_state_id])

            # Settle the robot with neutral actions
            for _ in range(10):
                neutral = np.array([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -1.0], dtype=np.float32)
                obs, _, _, _ = env.step(neutral)

            # Switch to absolute control
            for robot in env.env.robots:
                robot.controller.use_delta = False

            action_queue = []
            proprio_state = None
            success = False

            for step_idx in range(max_steps):
                if not action_queue:
                    # Extract proprio from env
                    proprio_20d = extract_proprio_20d(env)
                    if proprio_state is not None:
                        proprio_20d[:9] = proprio_state[:9]

                    images = get_images_from_obs(obs)
                    if not images:
                        raise ValueError(f"No images found in obs keys: {list(obs.keys())}")

                    raw_actions = predict_actions(
                        model, processor, images, task_desc, proprio_20d,
                        args.domain_id, device, args.denoise_steps,
                    )  # [30, 20]

                    # Update closed-loop proprio with last predicted action
                    proprio_state = proprio_20d.copy()
                    proprio_state[:9] = raw_actions[-1, :9].copy()

                    actions_7d = decode_action_20d_to_7d(raw_actions)  # [30, 7]
                    action_queue = list(actions_7d)

                action = action_queue.pop(0)
                obs, reward, done, info = env.step(action)

                if done or reward > 0.5:
                    success = True
                    break

            ep_steps = step_idx + 1
            task_successes.append(success)
            task_lengths.append(ep_steps)
            log.info("  Ep %d/%d | %s | steps=%d",
                     ep + 1, args.num_episodes,
                     "SUCCESS" if success else "FAIL", ep_steps)

            env.close()

        n_succ = sum(task_successes)
        n_total = len(task_successes)
        sr = n_succ / n_total if n_total > 0 else 0.0

        all_task_results[task_id] = {
            "task_id": task_id,
            "task_description": task_desc,
            "success_count": n_succ,
            "total_episodes": n_total,
            "success_rate": round(sr, 4),
            "mean_steps": round(float(np.mean(task_lengths)), 1),
        }
        total_successes += n_succ
        total_episodes += n_total
        log.info("  Task %d SR: %d/%d (%.1f%%)", task_id, n_succ, n_total, sr * 100)

    elapsed = time_mod.time() - eval_start
    overall_sr = total_successes / total_episodes if total_episodes > 0 else 0.0
    _, ci_lo, ci_hi = wilson_ci(total_successes, total_episodes)

    log.info("=" * 60)
    log.info("SUITE: %s | MODEL: xvla | keep_ratio: %.2f", args.suite, args.keep_ratio)
    log.info("Overall SR: %d/%d (%.1f%%)", total_successes, total_episodes, overall_sr * 100)
    log.info("95%% Wilson CI: [%.1f%%, %.1f%%]", ci_lo * 100, ci_hi * 100)
    for tid, tr in sorted(all_task_results.items()):
        log.info("  Task %d: %.0f%% (%d/%d) -- %s",
                 tid, tr["success_rate"] * 100, tr["success_count"],
                 tr["total_episodes"], tr["task_description"])
    log.info("Elapsed: %.1f min", elapsed / 60)
    log.info("=" * 60)

    summary = {
        "model": "xvla",
        "model_path": args.model_path,
        "mode": args.mode,
        "suite": args.suite,
        "keep_ratio": args.keep_ratio,
        "n_vision_tokens_original": n_vis_tokens,
        "n_vision_tokens_kept": k_tokens,
        "total_episodes": total_episodes,
        "total_successes": total_successes,
        "overall_success_rate": round(overall_sr, 4),
        "wilson_ci_95": [round(ci_lo, 4), round(ci_hi, 4)],
        "num_episodes_per_task": args.num_episodes,
        "max_steps": max_steps,
        "num_actions_per_chunk": num_actions_per_chunk,
        "domain_id": args.domain_id,
        "denoise_steps": args.denoise_steps,
        "seed": args.seed,
        "elapsed_seconds": round(elapsed, 1),
        "per_task": all_task_results,
    }

    output_path.parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(summary, f, indent=2)
    log.info("Results saved to %s", output_path)

    return summary


if __name__ == "__main__":
    args = parse_args()
    run_evaluation(args)
