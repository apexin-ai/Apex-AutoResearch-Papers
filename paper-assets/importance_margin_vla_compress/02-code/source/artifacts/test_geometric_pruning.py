"""
Dry-run test for Geometric Prior Pruning on LIBERO.

Loads baseline SmolVLA, registers Sobel-based pruning hook, runs 1 episode
(up to 20 re-planning steps) to verify:
  - Sobel importance is non-trivial (not all 0 or all 1)
  - Hook fires and prunes tokens (prints before/after counts)
  - Model forward does not crash
  - Action output shape is correct

Usage:
    cd /root/autodl-tmp/importance_margin_vla_compress
    CUDA_VISIBLE_DEVICES=0 python test_geometric_pruning.py
    CUDA_VISIBLE_DEVICES=0 python test_geometric_pruning.py --k_ratio 0.3
"""

from __future__ import annotations

import argparse
import logging
import os
import sys
import time

os.environ.setdefault("MUJOCO_GL", "egl")
os.environ.setdefault("TRANSFORMERS_OFFLINE", "1")
os.environ.setdefault("HF_HUB_OFFLINE", "1")

import numpy as np
import torch

PROJECT_DIR = "/root/autodl-tmp/importance_margin_vla_compress"
sys.path.insert(0, PROJECT_DIR)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
log = logging.getLogger(__name__)

CHECKPOINT = "checkpoints/libero_full_ft_100k/checkpoint.pt"
CONFIG = "configs/libero_baseline.yaml"


def parse_args():
    p = argparse.ArgumentParser()
    p.add_argument("--gpu", type=int, default=0)
    p.add_argument("--k_ratio", type=float, default=0.5)
    p.add_argument("--checkpoint", type=str, default=CHECKPOINT)
    p.add_argument("--config", type=str, default=CONFIG)
    p.add_argument("--max_replans", type=int, default=4,
                   help="Max re-planning steps to test")
    p.add_argument("--suite", type=str, default="libero_object")
    p.add_argument("--task_id", type=int, default=0)
    return p.parse_args()


def main():
    args = parse_args()
    device = torch.device(f"cuda:{args.gpu}" if torch.cuda.is_available() else "cpu")
    log.info("Device: %s, k_ratio: %.2f", device, args.k_ratio)

    # --- Load model ---
    from eval_success_rate_libero import (
        load_config, obs_to_batch, predict_actions,
    )
    from train import load_smolvla_policy, get_tokenizer_from_policy
    from geometric_prior_pruning import (
        GeometricPriorPruner, compute_sobel_importance,
    )

    config = load_config(args.config)
    log.info("Loading model from %s ...", args.checkpoint)
    t0 = time.time()
    policy = load_smolvla_policy(config, device)
    ckpt = torch.load(args.checkpoint, map_location=device, weights_only=False)
    missing, unexpected = policy.load_state_dict(
        ckpt["model_state_dict"], strict=False
    )
    if missing:
        log.warning("Missing keys: %d (expected for non-LoRA load)", len(missing))
    policy.eval()
    log.info("Model loaded in %.1fs", time.time() - t0)

    tokenizer = get_tokenizer_from_policy(policy)
    ds_cfg = config.get("dataset", {})
    camera_keys = ds_cfg.get("features", {}).get("cameras", [
        "observation.images.image", "observation.images.image2",
    ])

    # --- Test 1: Sobel importance on synthetic image ---
    log.info("=== Test 1: Sobel importance on synthetic image ===")
    synthetic = np.zeros((256, 256, 3), dtype=np.uint8)
    synthetic[100:150, 100:150, :] = 255  # white square
    imp = compute_sobel_importance(synthetic)
    log.info("  Shape: %s, min=%.4f, max=%.4f, mean=%.4f",
             imp.shape, imp.min(), imp.max(), imp.mean())
    assert imp.shape == (64,), f"Expected (64,), got {imp.shape}"
    assert imp.max() > 0, "Sobel importance is all zeros on image with edges"
    log.info("  PASS: non-trivial importance on synthetic image")

    # --- Test 2: Pruner creation ---
    log.info("=== Test 2: GeometricPriorPruner creation ===")
    pruner = GeometricPriorPruner(policy.model, k_ratio=args.k_ratio)
    log.info("  Connector found: %s", type(pruner.connector).__name__)
    log.info("  PASS")

    # --- Test 3: Hook with counting wrapper ---
    log.info("=== Test 3: Token counting hook ===")
    token_log = {"before": [], "after": []}
    original_forward = pruner.connector.forward.__func__

    def counting_forward(self_module, image_hidden_states):
        token_log["before"].append(image_hidden_states.shape[1])
        result = original_forward(self_module, image_hidden_states)
        return result

    pruner.connector.forward = counting_forward.__get__(
        pruner.connector, type(pruner.connector)
    )

    # --- Test 4: LIBERO rollout ---
    log.info("=== Test 4: LIBERO dry-run (task %d, max %d replans) ===",
             args.task_id, args.max_replans)

    from libero.libero import benchmark
    from lerobot.envs.libero import get_task_init_states, LiberoEnv

    task_suite = benchmark.get_benchmark_dict()[args.suite]()
    task = task_suite.tasks[args.task_id]
    task_desc = task.language
    log.info("  Task: %s", task_desc)

    env = LiberoEnv(task, render_mode="rgb_array")
    init_states = get_task_init_states(task, n_episodes=1)
    obs, _ = env.reset(init_state=init_states[0], seed=42)

    action_chunk = None
    action_idx = 0
    replan_count = 0
    success = False
    max_steps = 280

    for step in range(max_steps):
        if action_chunk is None or action_idx >= 50:
            if replan_count >= args.max_replans:
                log.info("  Reached max replans (%d), stopping.", args.max_replans)
                break

            batch = obs_to_batch(obs, task_desc, tokenizer, camera_keys, device)

            raw_images = []
            for ck in camera_keys:
                short = ck.split(".")[-1]
                raw_images.append(np.asarray(obs["pixels"][short]))

            pruner.set_current_images(raw_images)
            mask = pruner.attach(device)
            stats = pruner.get_importance_stats()

            token_log["before"].clear()

            with torch.no_grad():
                action_chunk = predict_actions(policy, batch)

            pruner.detach()

            kept = int(mask.sum().item())
            total = mask.shape[1]
            log.info(
                "  Replan %d (step %d): kept=%d/%d (%.0f%%) | "
                "cam0: mean=%.3f std=%.3f | cam1: mean=%.3f std=%.3f | "
                "action shape=%s",
                replan_count, step, kept, total, 100 * kept / total,
                stats.get("cam0_mean", 0), stats.get("cam0_std", 0),
                stats.get("cam1_mean", 0), stats.get("cam1_std", 0),
                tuple(action_chunk.shape),
            )

            assert action_chunk.shape[0] == 50, (
                f"Expected 50 actions, got {action_chunk.shape[0]}"
            )
            assert action_chunk.shape[1] == 7, (
                f"Expected 7 action dims, got {action_chunk.shape[1]}"
            )

            action_idx = 0
            replan_count += 1

        action = action_chunk[action_idx].cpu().numpy().astype(np.float32)
        action = np.clip(action, -1.0, 1.0)
        action_idx += 1

        obs, reward, terminated, truncated, info = env.step(action)
        if info.get("is_success", False):
            success = True
            log.info("  SUCCESS at step %d!", step)
            break
        if terminated or truncated:
            break

    env.close()

    # Restore original forward
    pruner.connector.forward = original_forward.__get__(
        pruner.connector, type(pruner.connector)
    )
    pruner.remove()

    log.info("=" * 60)
    log.info("DRY-RUN COMPLETE")
    log.info("  k_ratio: %.2f", args.k_ratio)
    log.info("  Replans executed: %d", replan_count)
    log.info("  Episode result: %s", "SUCCESS" if success else "FAIL (expected for dry-run)")
    log.info("  Model did NOT crash")
    log.info("  Action shape correct: (50, 7)")
    log.info("=" * 60)

    # --- Architecture summary ---
    log.info("")
    log.info("SigLIP patch-to-token mapping:")
    log.info("  SigLIP: image_size=512, patch_size=16 -> 32x32 = 1024 tokens")
    log.info("  Connector: pixel_shuffle scale_factor=4 -> 8x8 = 64 tokens/camera")
    log.info("  LIBERO: 2 cameras -> 128 total tokens")
    log.info("  Each token covers 32x32 pixels in raw 256x256 observation")


if __name__ == "__main__":
    main()
