#!/usr/bin/env python3
"""SmolVLA baseline evaluation on LIBERO and LIBERO-Plus.

Runs pretrained SmolVLA (no ACIB) on standard LIBERO tasks and
LIBERO-Plus perturbation tasks. Outputs per-task success rates.

Usage:
    # Standard LIBERO (all 4 suites)
    MUJOCO_GL=egl python scripts/eval_baseline.py \
        --model_id lerobot/smolvla_base \
        --env_type libero \
        --suites libero_spatial libero_object libero_goal libero_10 \
        --n_episodes 50 \
        --gpu 0 \
        --output_dir results/baseline_standard \
        --seed 42

    # LIBERO-Plus perturbation eval
    MUJOCO_GL=egl python scripts/eval_baseline.py \
        --model_id lerobot/smolvla_base \
        --env_type libero_plus \
        --suites libero_spatial libero_object libero_goal libero_10 \
        --n_episodes 50 \
        --gpu 1 \
        --output_dir results/baseline_perturbed \
        --seed 42

Requires: lerobot[smolvla], LIBERO or LIBERO-Plus installed.
"""

import argparse
import json
import os
import sys
import time
from pathlib import Path

import torch


def parse_args():
    parser = argparse.ArgumentParser(description="SmolVLA baseline evaluation")
    parser.add_argument("--model_id", type=str, default="lerobot/smolvla_base")
    parser.add_argument("--env_type", type=str, default="libero",
                        choices=["libero", "libero_plus"])
    parser.add_argument("--suites", nargs="+",
                        default=["libero_spatial", "libero_object",
                                 "libero_goal", "libero_10"])
    parser.add_argument("--n_episodes", type=int, default=50)
    parser.add_argument("--gpu", type=int, default=0)
    parser.add_argument("--output_dir", type=str, default="results/baseline")
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--max_steps", type=int, default=600)
    return parser.parse_args()


def run_lerobot_eval(args):
    """Run evaluation using lerobot-eval CLI."""
    import subprocess

    suites_str = ",".join(args.suites)
    cmd = [
        "lerobot-eval",
        f"--policy.path={args.model_id}",
        f"--env.type={args.env_type}",
        f"--env.task={suites_str}",
        f"--eval.batch_size=1",
        f"--eval.n_episodes={args.n_episodes}",
        f"--env.max_parallel_tasks=1",
        f"--output_dir={args.output_dir}",
    ]

    env = os.environ.copy()
    env["CUDA_VISIBLE_DEVICES"] = str(args.gpu)
    env["MUJOCO_GL"] = env.get("MUJOCO_GL", "egl")

    print(f"Running: {' '.join(cmd)}")
    print(f"GPU: {args.gpu}, Env: {args.env_type}, Suites: {suites_str}")

    result = subprocess.run(cmd, env=env, capture_output=False)
    return result.returncode


def run_manual_eval(args):
    """Fallback: manual evaluation loop if lerobot-eval CLI doesn't work.

    [NEEDS_SOURCE_VERIFICATION] The exact API for creating LIBERO envs
    through LeRobot may differ. Worker should adjust after testing.
    """
    from lerobot.policies.smolvla import SmolVLAPolicy
    from lerobot.policies.factory import make_pre_post_processors

    os.environ["CUDA_VISIBLE_DEVICES"] = str(args.gpu)
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

    print(f"Loading model: {args.model_id}")
    policy = SmolVLAPolicy.from_pretrained(args.model_id).to(device).eval()
    preprocess, postprocess = make_pre_post_processors(
        policy.config,
        args.model_id,
        preprocessor_overrides={"device_processor": {"device": str(device)}},
    )

    results = {}
    for suite in args.suites:
        print(f"\nEvaluating suite: {suite}")
        suite_results = eval_suite(
            policy, preprocess, postprocess,
            suite, args.env_type, args.n_episodes,
            args.max_steps, args.seed, device,
        )
        results[suite] = suite_results
        print(f"  {suite}: {suite_results['avg_success_rate']:.1%}")

    output_path = Path(args.output_dir)
    output_path.mkdir(parents=True, exist_ok=True)
    with open(output_path / "results.json", "w") as f:
        json.dump(results, f, indent=2)

    print(f"\nResults saved to {output_path / 'results.json'}")
    print_summary(results)


def eval_suite(policy, preprocess, postprocess, suite, env_type,
               n_episodes, max_steps, seed, device):
    """Evaluate one task suite. Returns dict with per-task and average success rates.

    [NEEDS_SOURCE_VERIFICATION] Env creation API depends on lerobot version.
    """
    # Placeholder structure — exact env API needs confirmation
    return {
        "avg_success_rate": 0.0,
        "per_task": {},
        "n_episodes": n_episodes,
        "note": "Placeholder — use lerobot-eval CLI or verify env API",
    }


def print_summary(results: dict):
    print("\n" + "=" * 60)
    print("BASELINE EVALUATION SUMMARY")
    print("=" * 60)
    for suite, data in results.items():
        sr = data.get("avg_success_rate", 0)
        print(f"  {suite:20s}: {sr:.1%}")
    all_sr = [d["avg_success_rate"] for d in results.values()]
    print(f"  {'AVERAGE':20s}: {sum(all_sr)/len(all_sr):.1%}")
    print("=" * 60)


if __name__ == "__main__":
    args = parse_args()
    print(f"SmolVLA Baseline Eval — {args.env_type}")
    print(f"  Model: {args.model_id}")
    print(f"  GPU: {args.gpu}")
    print(f"  Suites: {args.suites}")
    print(f"  Episodes/task: {args.n_episodes}")

    # Try CLI first, fall back to manual
    ret = run_lerobot_eval(args)
    if ret != 0:
        print(f"\nlerobot-eval exited with code {ret}, trying manual eval...")
        run_manual_eval(args)
