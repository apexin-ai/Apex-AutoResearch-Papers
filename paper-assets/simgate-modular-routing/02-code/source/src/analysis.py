"""Phase 1 results analysis: bootstrap CIs, pass/fail judgment per ROADMAP criteria.

Reads results/mvp/*/summary.json, computes:
  - Per task: mean ± std for 3 modes
  - Bootstrap 90% CI for (oracle - always-internal)
  - Pass / Conditional / Fail judgment

Usage: python src/analysis.py --results_dir results/mvp/
"""

import argparse
import json
import os
import sys
import glob
from typing import Dict, List, Any, Tuple

import numpy as np


def bootstrap_ci(diffs: List[float], ci: float = 0.90, n_boot: int = 10000,
                 seed: int = 42) -> Tuple[float, float, float]:
    """Bootstrap confidence interval for mean of diffs.

    Returns (lower, mean, upper).
    """
    rng = np.random.RandomState(seed)
    diffs = np.array(diffs)
    n = len(diffs)
    if n == 0:
        return (0.0, 0.0, 0.0)

    boot_means = np.array([
        rng.choice(diffs, size=n, replace=True).mean()
        for _ in range(n_boot)
    ])
    alpha = 1 - ci
    lower = float(np.percentile(boot_means, 100 * alpha / 2))
    upper = float(np.percentile(boot_means, 100 * (1 - alpha / 2)))
    mean = float(np.mean(diffs))
    return (lower, mean, upper)


def load_summaries(results_dir: str) -> Dict[str, dict]:
    """Load all summary.json files from results directory."""
    summaries = {}
    pattern = os.path.join(results_dir, "*", "summary.json")
    for path in sorted(glob.glob(pattern)):
        with open(path) as f:
            data = json.load(f)
        task_name = data.get("task_name", os.path.basename(os.path.dirname(path)))
        summaries[task_name] = data
    return summaries


def analyze_task(task_name: str, summary: dict) -> dict:
    """Analyze a single task's results."""
    diffs_oracle_internal = summary.get("oracle_minus_internal", {}).get("diffs", [])
    diffs_oracle_det = summary.get("oracle_minus_det", {}).get("diffs", [])

    ci_lower, ci_mean, ci_upper = bootstrap_ci(diffs_oracle_internal)
    ci_det_lower, ci_det_mean, ci_det_upper = bootstrap_ci(diffs_oracle_det)

    # Effect direction: is oracle > internal on average?
    effect_positive = ci_mean > 0

    # CI excludes zero → significant
    ci_excludes_zero = ci_lower > 0

    # Judgment for this task
    if ci_excludes_zero:
        judgment = "SIGNIFICANT_POSITIVE"
    elif effect_positive:
        judgment = "POSITIVE_TREND"
    else:
        judgment = "NO_EFFECT"

    return {
        "task_name": task_name,
        "n_episodes": summary.get("n_episodes", 0),
        "internal_mean": summary["always_internal"]["mean"],
        "internal_std": summary["always_internal"]["std"],
        "det_mean": summary["always_deterministic"]["mean"],
        "det_std": summary["always_deterministic"]["std"],
        "oracle_mean": summary["oracle_routing"]["mean"],
        "oracle_std": summary["oracle_routing"]["std"],
        "oracle_minus_internal_mean": ci_mean,
        "oracle_minus_internal_ci90": (ci_lower, ci_upper),
        "oracle_minus_det_mean": ci_det_mean,
        "oracle_minus_det_ci90": (ci_det_lower, ci_det_upper),
        "effect_positive": effect_positive,
        "ci_excludes_zero": ci_excludes_zero,
        "judgment": judgment,
    }


def overall_judgment(task_analyses: List[dict]) -> str:
    """Apply ROADMAP pass/fail criteria across all tasks.

    Pass: >= 2/5 tasks with 90% CI lower > 0
    Conditional: >= 3/5 positive direction but CI contains 0
    Fail: < 2/5 positive, or oracle ≈ always-deterministic
    """
    n_tasks = len(task_analyses)
    n_significant = sum(1 for t in task_analyses if t["ci_excludes_zero"])
    n_positive = sum(1 for t in task_analyses if t["effect_positive"])

    # oracle ≈ always-deterministic if oracle-det 90% CI contains 0 for all tasks
    oracle_eq_det = all(
        t["oracle_minus_det_ci90"][0] <= 0 <= t["oracle_minus_det_ci90"][1]
        for t in task_analyses
    )

    if n_significant >= 2 and not oracle_eq_det:
        return "PASS"
    elif n_positive >= 3 and not oracle_eq_det:
        return "CONDITIONAL_PASS"
    else:
        return "FAIL"


def print_results(task_analyses: List[dict], verdict: str):
    """Print formatted results table."""
    print("\n" + "=" * 90)
    print("PHASE 1 RESULTS ANALYSIS")
    print("=" * 90)

    # Table header
    header = f"{'Task':<35} {'Internal':>10} {'Determ.':>10} {'Oracle':>10} {'Δ(O-I)':>10} {'90% CI':>18} {'Judgment':>12}"
    print(header)
    print("-" * 90)

    for t in task_analyses:
        ci = t["oracle_minus_internal_ci90"]
        print(
            f"{t['task_name']:<35} "
            f"{t['internal_mean']:>8.1f}±{t['internal_std']:<4.1f}"
            f"{t['det_mean']:>8.1f}±{t['det_std']:<4.1f}"
            f"{t['oracle_mean']:>8.1f}±{t['oracle_std']:<4.1f}"
            f"{t['oracle_minus_internal_mean']:>+9.1f} "
            f"[{ci[0]:+.1f}, {ci[1]:+.1f}] "
            f"{t['judgment']:>12}"
        )

    print("-" * 90)

    n_sig = sum(1 for t in task_analyses if t["ci_excludes_zero"])
    n_pos = sum(1 for t in task_analyses if t["effect_positive"])
    print(f"\nSignificant positive (CI > 0): {n_sig}/{len(task_analyses)}")
    print(f"Positive direction:           {n_pos}/{len(task_analyses)}")

    # Oracle vs deterministic check
    print(f"\nOracle vs Deterministic (routing incremental value):")
    for t in task_analyses:
        ci_det = t["oracle_minus_det_ci90"]
        print(f"  {t['task_name']:<35} Δ(O-D)={t['oracle_minus_det_mean']:+.1f}  "
              f"90% CI [{ci_det[0]:+.1f}, {ci_det[1]:+.1f}]")

    print(f"\n{'='*90}")
    print(f"OVERALL VERDICT: {verdict}")
    print(f"{'='*90}")

    if verdict == "PASS":
        print("→ Proceed to full research phase")
    elif verdict == "CONDITIONAL_PASS":
        print("→ Proceed with narrowed claim scope; collect more episodes if time permits")
    else:
        print("→ Kill project or pivot approach")


def main():
    parser = argparse.ArgumentParser(description="Phase 1 results analysis")
    parser.add_argument("--results_dir", type=str, default="results/mvp/")
    parser.add_argument("--output", type=str, default=None,
                        help="Save analysis JSON to this path")
    args = parser.parse_args()

    summaries = load_summaries(args.results_dir)
    if not summaries:
        print(f"ERROR: No summary.json files found in {args.results_dir}/*/")
        sys.exit(1)

    task_analyses = []
    for task_name, summary in summaries.items():
        analysis = analyze_task(task_name, summary)
        task_analyses.append(analysis)

    verdict = overall_judgment(task_analyses)
    print_results(task_analyses, verdict)

    # Save analysis
    output_path = args.output or os.path.join(args.results_dir, "analysis.json")
    analysis_output = {
        "verdict": verdict,
        "tasks": task_analyses,
    }
    # Convert tuples to lists for JSON serialization
    for t in analysis_output["tasks"]:
        t["oracle_minus_internal_ci90"] = list(t["oracle_minus_internal_ci90"])
        t["oracle_minus_det_ci90"] = list(t["oracle_minus_det_ci90"])

    with open(output_path, "w") as f:
        json.dump(analysis_output, f, indent=2)
    print(f"\nAnalysis saved to {output_path}")


if __name__ == "__main__":
    main()
