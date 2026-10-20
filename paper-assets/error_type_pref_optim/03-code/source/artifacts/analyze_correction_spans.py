#!/usr/bin/env python3
"""
Phase A Step 4: Analyze correction horizons by error type.

Input:  data/correction_measured_trajectories.jsonl  (from measure_correction_horizon.py)
Output:
  - data/correction_analysis_summary.json   (statistics)
  - data/correction_boxplot.pdf             (boxplot)
  - data/correction_histogram.pdf           (histogram)
  - stdout: summary table + warnings

Dependencies: scipy, matplotlib, numpy
Usage:
    python analyze_correction_spans.py
    python analyze_correction_spans.py --input data/correction_measured_trajectories.jsonl
"""

import json
import argparse
import logging
from pathlib import Path
from collections import defaultdict
from typing import Dict, List, Any, Optional

import numpy as np

PROJECT_ROOT = Path("/root/error_type_pref_optim")
DATA_DIR = PROJECT_ROOT / "data"

logger = logging.getLogger("analyze_correction_spans")

EXPECTED_MEANS = {
    "action": 1.2,
    "verification": 3.1,
    "planning": 5.8,
}

ERROR_TYPES = ["action", "verification", "planning"]


def load_data(input_path: str) -> Dict[str, List[float]]:
    """Load correction horizons grouped by error type."""
    horizons_by_type: Dict[str, List[float]] = defaultdict(list)
    uncorrectable_by_type: Dict[str, int] = defaultdict(int)
    total_failures = 0

    with open(input_path) as f:
        for line in f:
            if not line.strip():
                continue
            traj = json.loads(line)
            for step in traj["steps"]:
                if not step.get("is_failure"):
                    continue
                total_failures += 1
                ec = step.get("error_classification", {})
                if not ec:
                    continue
                etype = ec.get("primary_error_type")
                if etype not in ERROR_TYPES:
                    continue

                cm = step.get("correction_measurement")
                if not cm:
                    continue

                if cm.get("is_uncorrectable"):
                    uncorrectable_by_type[etype] += 1
                else:
                    h = cm.get("min_correction_horizon")
                    if h is not None:
                        horizons_by_type[etype].append(float(h))

    return horizons_by_type, uncorrectable_by_type, total_failures


def compute_statistics(horizons_by_type: Dict[str, List[float]]) -> Dict[str, Dict[str, Any]]:
    stats = {}
    for etype in ERROR_TYPES:
        values = horizons_by_type.get(etype, [])
        if not values:
            stats[etype] = {"n": 0, "mean": None, "median": None, "std": None,
                            "min": None, "max": None, "q25": None, "q75": None}
            continue
        arr = np.array(values)
        stats[etype] = {
            "n": len(values),
            "mean": round(float(np.mean(arr)), 3),
            "median": round(float(np.median(arr)), 3),
            "std": round(float(np.std(arr, ddof=1)), 3) if len(values) > 1 else 0.0,
            "min": float(np.min(arr)),
            "max": float(np.max(arr)),
            "q25": round(float(np.percentile(arr, 25)), 3),
            "q75": round(float(np.percentile(arr, 75)), 3),
        }
    return stats


def pairwise_mann_whitney(horizons_by_type: Dict[str, List[float]]) -> Dict[str, Dict[str, Any]]:
    from scipy.stats import mannwhitneyu
    results = {}
    pairs = [("action", "verification"), ("action", "planning"), ("verification", "planning")]
    for a, b in pairs:
        va = horizons_by_type.get(a, [])
        vb = horizons_by_type.get(b, [])
        key = f"{a}_vs_{b}"
        if len(va) < 2 or len(vb) < 2:
            results[key] = {"U": None, "p_value": None, "significant": None,
                            "note": f"insufficient data (n_{a}={len(va)}, n_{b}={len(vb)})"}
            continue
        U, p = mannwhitneyu(va, vb, alternative="two-sided")
        results[key] = {
            "U": round(float(U), 2),
            "p_value": round(float(p), 6),
            "significant_0.05": p < 0.05,
            "significant_0.01": p < 0.01,
        }
    return results


def check_expected_distribution(stats: Dict, expected: Dict) -> List[str]:
    warnings = []
    for etype, expected_mean in expected.items():
        s = stats.get(etype, {})
        if s.get("mean") is None:
            warnings.append(f"WARNING: No data for {etype} errors")
            continue
        observed = s["mean"]
        deviation = abs(observed - expected_mean) / expected_mean
        if deviation > 0.5:
            warnings.append(
                f"WARNING: {etype} mean correction horizon = {observed:.2f}, "
                f"expected ~{expected_mean:.1f} (deviation {deviation*100:.0f}%)"
            )
        elif deviation > 0.25:
            warnings.append(
                f"NOTE: {etype} mean correction horizon = {observed:.2f}, "
                f"expected ~{expected_mean:.1f} (deviation {deviation*100:.0f}%)"
            )
    return warnings


# ---------------------------------------------------------------------------
# Visualization
# ---------------------------------------------------------------------------
def plot_boxplot(horizons_by_type: Dict[str, List[float]], output_path: str):
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    fig, ax = plt.subplots(figsize=(8, 5))

    data = [horizons_by_type.get(t, []) for t in ERROR_TYPES]
    labels = [f"{t}\n(n={len(d)})" for t, d in zip(ERROR_TYPES, data)]

    bp = ax.boxplot(data, labels=labels, patch_artist=True, showmeans=True,
                    meanprops=dict(marker="D", markerfacecolor="red", markersize=6))

    colors = ["#66c2a5", "#fc8d62", "#8da0cb"]
    for patch, color in zip(bp["boxes"], colors):
        patch.set_facecolor(color)
        patch.set_alpha(0.7)

    for i, (etype, expected) in enumerate(EXPECTED_MEANS.items()):
        ax.scatter(i + 1, expected, marker="*", s=200, c="gold", zorder=5,
                   edgecolors="black", linewidths=0.5,
                   label=f"Expected {etype}" if i == 0 else "")

    ax.set_ylabel("Correction Horizon (agent turns)")
    ax.set_title("Correction Horizon by Error Type")
    ax.legend(["Expected mean"], loc="upper left")
    ax.grid(axis="y", alpha=0.3)

    plt.tight_layout()
    plt.savefig(output_path, dpi=150, bbox_inches="tight")
    plt.close()
    logger.info(f"Boxplot saved to {output_path}")


def plot_histogram(horizons_by_type: Dict[str, List[float]], output_path: str):
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    fig, axes = plt.subplots(1, 3, figsize=(15, 4), sharey=True)
    colors = ["#66c2a5", "#fc8d62", "#8da0cb"]

    for ax, etype, color in zip(axes, ERROR_TYPES, colors):
        values = horizons_by_type.get(etype, [])
        if not values:
            ax.text(0.5, 0.5, "No data", ha="center", va="center", transform=ax.transAxes)
            ax.set_title(f"{etype} (n=0)")
            continue

        max_val = max(values)
        bins = np.arange(0.5, max_val + 1.5, 1)
        ax.hist(values, bins=bins, color=color, alpha=0.7, edgecolor="black", linewidth=0.5)
        ax.axvline(np.mean(values), color="red", linestyle="--", linewidth=1.5, label=f"Mean={np.mean(values):.2f}")
        ax.axvline(EXPECTED_MEANS[etype], color="gold", linestyle=":", linewidth=2, label=f"Expected={EXPECTED_MEANS[etype]}")
        ax.set_title(f"{etype} (n={len(values)})")
        ax.set_xlabel("Correction Horizon")
        ax.legend(fontsize=8)

    axes[0].set_ylabel("Count")
    plt.suptitle("Distribution of Correction Horizons by Error Type", fontsize=13)
    plt.tight_layout()
    plt.savefig(output_path, dpi=150, bbox_inches="tight")
    plt.close()
    logger.info(f"Histogram saved to {output_path}")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
def main():
    parser = argparse.ArgumentParser(description="Analyze correction horizons by error type")
    parser.add_argument("--input", type=str, default=str(DATA_DIR / "correction_measured_trajectories.jsonl"))
    parser.add_argument("--output_dir", type=str, default=str(DATA_DIR))
    parser.add_argument("--no_plots", action="store_true")
    args = parser.parse_args()

    logging.basicConfig(level=logging.INFO, format="%(asctime)s %(name)s %(levelname)s %(message)s")

    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    horizons_by_type, uncorrectable_by_type, total_failures = load_data(args.input)

    # --- Statistics ---
    stats = compute_statistics(horizons_by_type)
    mw_results = pairwise_mann_whitney(horizons_by_type)
    warnings = check_expected_distribution(stats, EXPECTED_MEANS)

    # --- Print summary ---
    print("\n" + "=" * 70)
    print("CORRECTION HORIZON ANALYSIS SUMMARY")
    print("=" * 70)
    print(f"\nTotal failure steps analyzed: {total_failures}")
    print(f"Uncorrectable: {dict(uncorrectable_by_type)}")

    print(f"\n{'Type':<15} {'N':>5} {'Mean':>7} {'Median':>7} {'Std':>7} {'Min':>5} {'Max':>5} {'Expected':>9}")
    print("-" * 70)
    for etype in ERROR_TYPES:
        s = stats[etype]
        if s["n"] == 0:
            print(f"{etype:<15} {'0':>5} {'N/A':>7} {'N/A':>7} {'N/A':>7} {'N/A':>5} {'N/A':>5} {EXPECTED_MEANS[etype]:>9.1f}")
        else:
            print(f"{etype:<15} {s['n']:>5} {s['mean']:>7.2f} {s['median']:>7.2f} {s['std']:>7.2f} "
                  f"{s['min']:>5.0f} {s['max']:>5.0f} {EXPECTED_MEANS[etype]:>9.1f}")

    print("\nMann-Whitney U Tests (pairwise):")
    print("-" * 70)
    for key, result in mw_results.items():
        if result.get("note"):
            print(f"  {key}: {result['note']}")
        else:
            sig = "***" if result["significant_0.01"] else ("*" if result["significant_0.05"] else "ns")
            print(f"  {key}: U={result['U']:.1f}, p={result['p_value']:.6f} {sig}")

    if warnings:
        print("\nDistribution Warnings:")
        for w in warnings:
            print(f"  {w}")
    else:
        print("\nAll error types within expected range.")

    print("=" * 70)

    # --- Save summary JSON ---
    summary = {
        "statistics": stats,
        "mann_whitney_tests": mw_results,
        "expected_means": EXPECTED_MEANS,
        "uncorrectable_counts": dict(uncorrectable_by_type),
        "total_failures": total_failures,
        "warnings": warnings,
    }
    summary_path = output_dir / "correction_analysis_summary.json"
    with open(summary_path, "w") as f:
        json.dump(summary, f, indent=2, ensure_ascii=False)
    logger.info(f"Summary saved to {summary_path}")

    # --- Plots ---
    if not args.no_plots:
        try:
            plot_boxplot(horizons_by_type, str(output_dir / "correction_boxplot.pdf"))
            plot_histogram(horizons_by_type, str(output_dir / "correction_histogram.pdf"))
        except ImportError as e:
            logger.warning(f"Skipping plots (missing dependency): {e}")


if __name__ == "__main__":
    main()
