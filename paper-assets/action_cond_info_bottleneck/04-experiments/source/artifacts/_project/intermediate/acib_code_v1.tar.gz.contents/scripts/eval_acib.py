#!/usr/bin/env python3
"""ACIB model evaluation on LIBERO and LIBERO-Plus.

Evaluates a trained ACIBPolicy checkpoint. Supports:
- Standard LIBERO tasks (nominal performance)
- LIBERO-Plus perturbation tasks (robustness)
- A/B comparison: ACIB enabled vs disabled on same model

Usage:
    # ACIB eval on standard LIBERO
    MUJOCO_GL=egl python scripts/eval_acib.py \
        --checkpoint outputs/acib_s_h64/checkpoint-20000/checkpoint.pt \
        --env_type libero \
        --suites libero_spatial libero_object libero_goal libero_10 \
        --n_episodes 50 \
        --gpu 0 \
        --output_dir results/acib_s_standard \
        --seed 42

    # A/B test (ACIB on vs off)
    MUJOCO_GL=egl python scripts/eval_acib.py \
        --checkpoint outputs/acib_s_h64/checkpoint-20000/checkpoint.pt \
        --env_type libero_plus \
        --ab_test \
        --n_episodes 50 \
        --gpu 1

Requires: lerobot[smolvla], LIBERO or LIBERO-Plus installed.
"""

import argparse
import json
import os
import sys
from pathlib import Path

import torch

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from acib.config import ACIBConfig
from acib.acib_policy import ACIBPolicy


def parse_args():
    parser = argparse.ArgumentParser(description="ACIB evaluation")
    parser.add_argument("--checkpoint", type=str, required=True)
    parser.add_argument("--model_id", type=str, default="lerobot/smolvla_base")
    parser.add_argument("--env_type", type=str, default="libero",
                        choices=["libero", "libero_plus"])
    parser.add_argument("--suites", nargs="+",
                        default=["libero_spatial", "libero_object",
                                 "libero_goal", "libero_10"])
    parser.add_argument("--n_episodes", type=int, default=50)
    parser.add_argument("--gpu", type=int, default=0)
    parser.add_argument("--output_dir", type=str, default="results/acib_eval")
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--ab_test", action="store_true",
                        help="Run with ACIB on and off for comparison")
    return parser.parse_args()


def load_acib_policy(args) -> ACIBPolicy:
    """Load ACIBPolicy from checkpoint."""
    ckpt = torch.load(args.checkpoint, map_location="cpu", weights_only=False)
    ckpt_config = ckpt.get("config", {})

    acib_config = ACIBConfig(
        hidden_dim=ckpt_config.get("hidden_dim", 64),
        alpha=ckpt_config.get("alpha", 1.0),
        beta=ckpt_config.get("beta", 0.01),
        mode=ckpt_config.get("mode", "soft"),
        top_k_ratio=ckpt_config.get("top_k_ratio", 0.8),
        condition_source=ckpt_config.get("condition_source", "language"),
    )

    policy = ACIBPolicy.from_pretrained(args.model_id, acib_config)
    policy.load_state_dict(ckpt["policy_state_dict"])
    return policy


def evaluate(policy, args, acib_enabled=True):
    """Run evaluation with ACIB enabled or disabled.

    [NEEDS_SOURCE_VERIFICATION] Same env API caveats as eval_baseline.py.
    Prefer lerobot-eval CLI if available; fall back to manual loop.
    """
    policy.toggle_acib(acib_enabled)
    mode_str = "ACIB_ON" if acib_enabled else "ACIB_OFF"
    print(f"\nEvaluating: {mode_str}")

    results = {}
    for suite in args.suites:
        print(f"  Suite: {suite}")
        # [NEEDS_SOURCE_VERIFICATION] Use lerobot eval API
        results[suite] = {
            "avg_success_rate": 0.0,
            "note": f"Placeholder — implement after verifying lerobot eval API ({mode_str})",
        }

    return results


def main():
    args = parse_args()
    os.environ["CUDA_VISIBLE_DEVICES"] = str(args.gpu)
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    print(f"Loading checkpoint: {args.checkpoint}")
    policy = load_acib_policy(args).to(device).eval()

    if args.ab_test:
        results_on = evaluate(policy, args, acib_enabled=True)
        results_off = evaluate(policy, args, acib_enabled=False)

        combined = {
            "acib_on": results_on,
            "acib_off": results_off,
            "comparison": {},
        }

        for suite in args.suites:
            sr_on = results_on[suite]["avg_success_rate"]
            sr_off = results_off[suite]["avg_success_rate"]
            combined["comparison"][suite] = {
                "acib_on": sr_on,
                "acib_off": sr_off,
                "delta": sr_on - sr_off,
            }

        with open(output_dir / "ab_results.json", "w") as f:
            json.dump(combined, f, indent=2)
        print(f"\nA/B results saved to {output_dir / 'ab_results.json'}")

        print("\n" + "=" * 60)
        print("A/B TEST SUMMARY")
        print("=" * 60)
        for suite, comp in combined["comparison"].items():
            delta = comp["delta"]
            sign = "+" if delta > 0 else ""
            print(f"  {suite:20s}: ON={comp['acib_on']:.1%} OFF={comp['acib_off']:.1%} "
                  f"({sign}{delta:.1%})")
    else:
        results = evaluate(policy, args, acib_enabled=True)
        with open(output_dir / "results.json", "w") as f:
            json.dump(results, f, indent=2)
        print(f"\nResults saved to {output_dir / 'results.json'}")


if __name__ == "__main__":
    main()
