#!/usr/bin/env python3
"""SmolVLA fine-tuning on LIBERO via LeRobot's standard BC pipeline.

MVP-0: produces a SmolVLA-LIBERO checkpoint for baseline eval.
Skip this if using the official HuggingFaceVLA/smolvla_libero checkpoint.

Two modes:
  1. CLI mode (recommended): wraps lerobot-train with correct args
  2. Programmatic mode: direct Python training loop (fallback)

Usage:
    # CLI mode (default) — uses lerobot-train under the hood
    python scripts/finetune_smolvla.py \
        --dataset_id HuggingFaceVLA/libero \
        --env_task libero_10 \
        --steps 20000 \
        --batch_size 64 \
        --gpu 0 \
        --output_dir /root/acib/outputs/smolvla_libero

    # All 4 suites sequentially
    for suite in libero_spatial libero_object libero_goal libero_10; do
        python scripts/finetune_smolvla.py --env_task $suite --steps 20000
    done
"""

import argparse
import os
import subprocess
import sys


def parse_args():
    parser = argparse.ArgumentParser(description="SmolVLA fine-tuning on LIBERO")
    parser.add_argument("--model_id", type=str, default="lerobot/smolvla_base",
                        help="Base model HF repo ID")
    parser.add_argument("--dataset_id", type=str, default="HuggingFaceVLA/libero",
                        help="LIBERO dataset HF repo ID")
    parser.add_argument("--env_task", type=str, default="libero_10",
                        choices=["libero_spatial", "libero_object", "libero_goal", "libero_10"],
                        help="LIBERO task suite to train on")
    parser.add_argument("--steps", type=int, default=20000)
    parser.add_argument("--batch_size", type=int, default=64)
    parser.add_argument("--lr", type=float, default=1e-4)
    parser.add_argument("--warmup_steps", type=int, default=1000)
    parser.add_argument("--grad_clip", type=float, default=10.0)
    parser.add_argument("--gpu", type=int, default=0)
    parser.add_argument("--output_dir", type=str, default="/root/acib/outputs/smolvla_libero")
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--wandb_project", type=str, default="")
    parser.add_argument("--eval_freq", type=int, default=2000)
    parser.add_argument("--eval_episodes", type=int, default=10)
    parser.add_argument("--dtype", type=str, default="bfloat16",
                        choices=["float32", "bfloat16"])
    return parser.parse_args()


def run_lerobot_train(args):
    """Use lerobot-train CLI for standard BC fine-tuning."""
    os.environ["CUDA_VISIBLE_DEVICES"] = str(args.gpu)
    os.environ["MUJOCO_GL"] = os.environ.get("MUJOCO_GL", "egl")

    cmd = [
        "lerobot-train",
        f"--policy.path={args.model_id}",
        f"--dataset.repo_id={args.dataset_id}",
        f"--env.type=libero",
        f"--env.task={args.env_task}",
        f"--batch_size={args.batch_size}",
        f"--steps={args.steps}",
        f"--output_dir={args.output_dir}",
        f"--eval.batch_size=1",
        f"--eval.n_episodes={args.eval_episodes}",
        f"--eval_freq={args.eval_freq}",
        f"--env.max_parallel_tasks=1",
        f"--policy.load_vlm_weights=true",
        f"--seed={args.seed}",
    ]

    if args.dtype == "bfloat16":
        cmd.append("--policy.dtype=bfloat16")

    if args.wandb_project:
        cmd.extend([
            "--wandb.enable=true",
            f"--wandb.project={args.wandb_project}",
        ])

    print(f"Running lerobot-train:")
    print(f"  Model: {args.model_id}")
    print(f"  Dataset: {args.dataset_id}")
    print(f"  Task: {args.env_task}")
    print(f"  Steps: {args.steps}, Batch: {args.batch_size}")
    print(f"  GPU: {args.gpu}")
    print(f"  Output: {args.output_dir}")
    print(f"\nCommand: {' '.join(cmd)}\n")

    result = subprocess.run(cmd, env=os.environ)

    if result.returncode != 0:
        print(f"\nlerobot-train failed with code {result.returncode}")
        print("Check if lerobot-train is installed: pip show lerobot")
        sys.exit(1)

    print(f"\nFine-tuning complete. Checkpoint saved to {args.output_dir}")


if __name__ == "__main__":
    args = parse_args()
    run_lerobot_train(args)
