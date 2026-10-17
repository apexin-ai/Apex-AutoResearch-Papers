"""OpenVLA Vision Token Pruning Evaluation on LIBERO.

Prunes vision tokens by L2 norm after the projector (before LLM),
evaluates on LIBERO suites using the official OpenVLA action prediction API.

Usage:
    CUDA_VISIBLE_DEVICES=0 MUJOCO_GL=egl python eval_openvla_pruning_libero.py \
        --model_path /root/autodl-tmp/openvla-libero-spatial \
        --suite libero_spatial \
        --keep_ratio 0.9 \
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
from functools import wraps
from pathlib import Path

os.environ.setdefault("MUJOCO_GL", "egl")
os.environ.setdefault("TRANSFORMERS_OFFLINE", "1")
os.environ.setdefault("HF_HUB_OFFLINE", "1")

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
    "libero_spatial": 280,
    "libero_object": 280,
    "libero_goal": 300,
    "libero_10": 520,
    "libero_90": 400,
}

OPENVLA_PROMPT_TEMPLATE = "In: What action should the robot take to {task}?\nOut:"


def parse_args():
    p = argparse.ArgumentParser(description="OpenVLA vision token pruning eval on LIBERO")
    p.add_argument("--model_path", type=str, required=True,
                   help="Path to fine-tuned OpenVLA model directory")
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
    p.add_argument("--mode", type=str, default="l2_norm",
                   choices=["l2_norm", "random"],
                   help="Pruning method")
    return p.parse_args()


# ---------------------------------------------------------------------------
# Pruning hook — patches the projector to prune after projection
# ---------------------------------------------------------------------------

def get_n_vision_tokens(model):
    img_sizes = model.config.image_sizes
    patch_size = 14
    n_patches = (img_sizes[0] // patch_size) * (img_sizes[1] // patch_size)
    return n_patches


def install_vision_pruning(model, keep_ratio: float, mode: str = "l2_norm"):
    n_tokens = get_n_vision_tokens(model)
    k_tokens = max(1, int(keep_ratio * n_tokens))

    if keep_ratio >= 1.0:
        log.info("keep_ratio=%.2f, no pruning applied (%d tokens)", keep_ratio, n_tokens)
        return n_tokens, n_tokens

    original_forward = model.projector.forward

    @wraps(original_forward)
    def pruned_forward(img_patches):
        projected = original_forward(img_patches)
        B, N, D = projected.shape
        k = max(1, int(keep_ratio * N))
        if k >= N:
            return projected
        if mode == "l2_norm":
            norms = projected.norm(dim=-1)
            _, indices = norms.topk(k, dim=-1)
        elif mode == "random":
            indices = torch.stack([
                torch.randperm(N, device=projected.device)[:k]
                for _ in range(B)
            ], dim=0)
        indices_sorted = indices.sort(dim=-1).values
        pruned = projected.gather(
            1, indices_sorted.unsqueeze(-1).expand(-1, -1, D)
        )
        return pruned

    model.projector.forward = pruned_forward

    log.info("Vision pruning installed: keep_ratio=%.2f, mode=%s, %d→%d tokens",
             keep_ratio, mode, n_tokens, k_tokens)
    return n_tokens, k_tokens


def load_model(model_path: str, device: torch.device):
    from transformers import AutoModelForVision2Seq, AutoProcessor

    log.info("Loading OpenVLA from %s", model_path)
    model = AutoModelForVision2Seq.from_pretrained(
        model_path,
        torch_dtype=torch.bfloat16,
        trust_remote_code=True,
        low_cpu_mem_usage=True,
    ).to(device)
    processor = AutoProcessor.from_pretrained(model_path, trust_remote_code=True)
    model.eval()

    n_params = sum(p.numel() for p in model.parameters())
    log.info("Model loaded: %.1fB params, dtype=%s", n_params / 1e9, next(model.parameters()).dtype)
    return model, processor


def wilson_ci(successes, total, z=1.96):
    if total == 0:
        return 0.0, 0.0, 0.0
    p_hat = successes / total
    denom = 1 + z**2 / total
    center = (p_hat + z**2 / (2 * total)) / denom
    margin = z * np.sqrt((p_hat * (1 - p_hat) + z**2 / (4 * total)) / total) / denom
    return center, max(0, center - margin), min(1, center + margin)


def get_unnorm_key(model, suite: str) -> str:
    norm_stats = model.norm_stats
    suite_to_key = {
        "libero_spatial": "libero_spatial",
        "libero_object": "libero_object",
        "libero_goal": "libero_goal",
        "libero_10": "libero_10",
        "libero_90": "libero_90",
    }
    key = suite_to_key.get(suite, suite)
    if key in norm_stats:
        return key
    if len(norm_stats) == 1:
        only_key = next(iter(norm_stats.keys()))
        log.warning("Suite '%s' not in norm_stats, using '%s'", suite, only_key)
        return only_key
    raise ValueError(f"Cannot find norm_stats for suite '{suite}', available: {list(norm_stats.keys())}")


@torch.no_grad()
def predict_action(model, processor, image: Image.Image, task_text: str,
                   unnorm_key: str, device: torch.device) -> np.ndarray:
    prompt = OPENVLA_PROMPT_TEMPLATE.format(task=task_text)
    inputs = processor(prompt, image).to(device, dtype=torch.bfloat16)
    action = model.predict_action(
        **inputs,
        unnorm_key=unnorm_key,
        do_sample=False,
    )
    return action


def run_evaluation(args):
    device = torch.device(f"cuda:{args.gpu}" if torch.cuda.is_available() else "cpu")
    log.info("Device: %s", device)

    model, processor = load_model(args.model_path, device)
    unnorm_key = get_unnorm_key(model, args.suite)
    log.info("Using unnorm_key='%s' for suite '%s'", unnorm_key, args.suite)

    n_vis_tokens, k_tokens = install_vision_pruning(model, args.keep_ratio, args.mode)

    max_steps = args.max_steps or SUITE_MAX_STEPS.get(args.suite, 300)

    output_path = Path(args.output) if args.output else Path(
        f"eval_results/openvla_{args.mode}_k{args.keep_ratio}_{args.suite}_seed{args.seed}.json")

    log.info("Suite: %s | Device: %s | keep_ratio=%.2f | Episodes/task: %d | Max steps: %d",
             args.suite, device, args.keep_ratio, args.num_episodes, max_steps)

    # Load LIBERO benchmark
    from lerobot.common.envs.factory import make_env_from_cfg
    from libero.libero.benchmark import get_benchmark
    benchmark = get_benchmark(args.suite)()
    n_tasks = benchmark.n_tasks
    task_ids = list(range(n_tasks))
    if args.task_ids:
        task_ids = [int(x) for x in args.task_ids.split(",")]
    log.info("Tasks: %d total, evaluating: %s", n_tasks, task_ids)

    from lerobot.common.envs.libero.env import LiberoEnv

    eval_start = time_mod.time()
    total_successes = 0
    total_episodes = 0
    all_task_results = {}

    for task_id in task_ids:
        task_suite = benchmark
        task = benchmark.get_task(task_id)
        task_desc = task.language
        log.info("--- Task %d: %s ---", task_id, task_desc)

        env = LiberoEnv(
            task_suite=task_suite,
            task_id=task_id,
            task_suite_name=args.suite,
            camera_name="agentview_image",
            obs_type="pixels_agent_pos",
            observation_width=224,
            observation_height=224,
            init_states=True,
            n_envs=args.num_episodes,
            episode_index=0,
            control_mode="relative",
        )

        task_successes = []
        task_lengths = []

        for ep in range(args.num_episodes):
            obs, info = env.reset(seed=args.seed + task_id * 1000 + ep)
            success = False

            for step in range(max_steps):
                if step < 3 or step % 50 == 0:
                    log.info("  Step %d/%d", step, max_steps)

                # Extract image from observation
                img = obs.get("agentview_image", obs.get("pixels", {}).get("agentview_image", None))
                if img is None:
                    for k, v in obs.items():
                        if "agentview" in k and isinstance(v, np.ndarray):
                            img = v
                            break
                if img is None:
                    raise ValueError(f"Cannot find agentview image in obs keys: {list(obs.keys())}")

                if isinstance(img, np.ndarray):
                    if img.dtype in (np.float32, np.float64):
                        img = (np.clip(img, 0, 1) * 255).astype(np.uint8)
                    pil_img = Image.fromarray(img)
                else:
                    pil_img = img

                action = predict_action(model, processor, pil_img, task_desc, unnorm_key, device)
                action = np.clip(action, -1.0, 1.0).astype(np.float32)

                obs, reward, terminated, truncated, info = env.step(action)

                if info.get("is_success", False):
                    success = True
                    break
                if terminated or truncated:
                    break

            ep_steps = step + 1
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
    log.info("SUITE: %s | MODEL: openvla | keep_ratio: %.2f | mode: %s",
             args.suite, args.keep_ratio, args.mode)
    log.info("Overall SR: %d/%d (%.1f%%)", total_successes, total_episodes, overall_sr * 100)
    log.info("95%% Wilson CI: [%.1f%%, %.1f%%]", ci_lo * 100, ci_hi * 100)
    for tid, tr in sorted(all_task_results.items()):
        log.info("  Task %d: %.0f%% (%d/%d) -- %s",
                 tid, tr["success_rate"] * 100, tr["success_count"],
                 tr["total_episodes"], tr["task_description"])
    log.info("Elapsed: %.1f min", elapsed / 60)
    log.info("=" * 60)

    summary = {
        "model": "openvla",
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
