"""Seed validation analysis: compare PI controller vs fixed-ratio baseline across multiple seeds.

Usage:
    python analyze_seed_validation.py --base-dir /root/autodl-tmp/ --seeds 42 123 456

Input:
    - output_seed_{seed}_pi/   directories with PI controller results
    - output_seed_{seed}_fixed/ directories with fixed-ratio results
    Each contains G0/, G1/, G2/ subdirectories with metrics.jsonl,
    and PI dirs also contain control_log.jsonl.

Output:
    - Printed summary table (mean ± std across seeds)
    - JSON report saved to --output (default: seed_validation_report.json)
"""

import argparse
import json
import os
import sys
from pathlib import Path

import numpy as np


def read_last_metrics(metrics_path: str) -> dict:
    """Read the last line from a metrics.jsonl file."""
    last_line = None
    with open(metrics_path) as f:
        for line in f:
            line = line.strip()
            if line:
                last_line = line
    if last_line is None:
        raise ValueError(f"Empty metrics file: {metrics_path}")
    return json.loads(last_line)


def read_control_log(control_log_path: str) -> list[float]:
    """Read w_t values from control_log.jsonl."""
    w_values = []
    with open(control_log_path) as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            entry = json.loads(line)
            if "w_t" in entry:
                w_values.append(entry["w_t"])
            elif "w" in entry:
                w_values.append(entry["w"])
    return w_values


def collect_run_metrics(run_dir: str) -> dict:
    """Collect final metrics from a single run directory (G0/G1/G2)."""
    run_path = Path(run_dir)
    result = {}

    for gen in ["G0", "G1", "G2"]:
        metrics_file = run_path / gen / "metrics.jsonl"
        if not metrics_file.exists():
            raise FileNotFoundError(f"Missing {metrics_file}")
        m = read_last_metrics(str(metrics_file))
        result[gen] = {
            "eff_rank": m.get("eff_rank", m.get("effective_rank")),
            "ppl": m.get("ppl", m.get("perplexity")),
            "vocab_coverage": m.get("vocab_coverage", m.get("coverage")),
        }

    # w_t trajectory (PI runs only)
    control_log = run_path / "control_log.jsonl"
    if control_log.exists():
        result["w_t_trajectory"] = read_control_log(str(control_log))

    return result


def compute_stats(values: list[float]) -> tuple[float, float]:
    """Return (mean, std) for a list of values."""
    arr = np.array(values)
    return float(np.mean(arr)), float(np.std(arr, ddof=1))


def fmt(mean: float, std: float, decimals: int = 3) -> str:
    """Format mean ± std."""
    return f"{mean:.{decimals}f} ± {std:.{decimals}f}"


def main():
    parser = argparse.ArgumentParser(description="Analyze seed validation results")
    parser.add_argument("--base-dir", required=True, help="Base directory containing output_seed_* dirs")
    parser.add_argument("--seeds", nargs="+", type=int, default=[42, 123, 456])
    parser.add_argument("--output", default="seed_validation_report.json", help="Output JSON report path")
    args = parser.parse_args()

    base = Path(args.base_dir)
    seeds = args.seeds

    pi_metrics = []
    fixed_metrics = []

    for seed in seeds:
        pi_dir = base / f"output_seed_{seed}_pi"
        fixed_dir = base / f"output_seed_{seed}_fixed"

        if not pi_dir.exists():
            print(f"WARNING: {pi_dir} not found, skipping seed {seed} PI", file=sys.stderr)
            continue
        if not fixed_dir.exists():
            print(f"WARNING: {fixed_dir} not found, skipping seed {seed} fixed", file=sys.stderr)
            continue

        pi_metrics.append({"seed": seed, **collect_run_metrics(str(pi_dir))})
        fixed_metrics.append({"seed": seed, **collect_run_metrics(str(fixed_dir))})

    if not pi_metrics or not fixed_metrics:
        print("ERROR: No complete seed pairs found.", file=sys.stderr)
        sys.exit(1)

    # Compute per-seed derived metrics
    def extract(runs, key, gen="G2"):
        return [r[gen][key] for r in runs]

    def retention(runs):
        return [r["G2"]["eff_rank"] / r["G0"]["eff_rank"] for r in runs]

    pi_rank = compute_stats(extract(pi_metrics, "eff_rank"))
    fi_rank = compute_stats(extract(fixed_metrics, "eff_rank"))
    pi_ppl = compute_stats(extract(pi_metrics, "ppl"))
    fi_ppl = compute_stats(extract(fixed_metrics, "ppl"))
    pi_cov = compute_stats(extract(pi_metrics, "vocab_coverage"))
    fi_cov = compute_stats(extract(fixed_metrics, "vocab_coverage"))
    pi_ret = compute_stats(retention(pi_metrics))
    fi_ret = compute_stats(retention(fixed_metrics))

    # PI w_t stats: mean of per-run means, std of per-run means
    pi_w_means = [float(np.mean(r["w_t_trajectory"])) for r in pi_metrics if "w_t_trajectory" in r]
    pi_w_stats = compute_stats(pi_w_means) if pi_w_means else (float("nan"), float("nan"))

    # Print table
    seed_str = ", ".join(str(s) for s in seeds)
    print(f"\nSeed Validation Results ({len(seeds)} seeds: {seed_str})")
    print("=" * 60)
    print(f"{'Metric':<20} | {'PI Controller':<18} | {'Fixed (w={})'.format(os.environ.get('FIXED_RATIO', '0.5')):<18}")
    print("-" * 60)
    print(f"{'final_eff_rank':<20} | {fmt(*pi_rank, 1):<18} | {fmt(*fi_rank, 1):<18}")
    print(f"{'final_ppl':<20} | {fmt(*pi_ppl, 1):<18} | {fmt(*fi_ppl, 1):<18}")
    print(f"{'final_coverage':<20} | {fmt(*pi_cov):<18} | {fmt(*fi_cov):<18}")
    print(f"{'rank_retention':<20} | {fmt(*pi_ret):<18} | {fmt(*fi_ret):<18}")
    print(f"{'pi_w_mean':<20} | {fmt(*pi_w_stats):<18} | {'N/A':<18}")

    # Build JSON report
    report = {
        "seeds": seeds,
        "n_seeds": len(seeds),
        "pi_controller": {
            "final_eff_rank": {"mean": pi_rank[0], "std": pi_rank[1]},
            "final_ppl": {"mean": pi_ppl[0], "std": pi_ppl[1]},
            "final_coverage": {"mean": pi_cov[0], "std": pi_cov[1]},
            "rank_retention": {"mean": pi_ret[0], "std": pi_ret[1]},
            "w_t_mean": {"mean": pi_w_stats[0], "std": pi_w_stats[1]},
            "per_seed": pi_metrics,
        },
        "fixed_ratio": {
            "final_eff_rank": {"mean": fi_rank[0], "std": fi_rank[1]},
            "final_ppl": {"mean": fi_ppl[0], "std": fi_ppl[1]},
            "final_coverage": {"mean": fi_cov[0], "std": fi_cov[1]},
            "rank_retention": {"mean": fi_ret[0], "std": fi_ret[1]},
            "per_seed": fixed_metrics,
        },
    }

    with open(args.output, "w") as f:
        json.dump(report, f, indent=2, default=str)
    print(f"\nJSON report saved to {args.output}")


if __name__ == "__main__":
    main()
