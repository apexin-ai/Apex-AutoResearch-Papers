# compare_phase2.py — 对比 ThreadGate vs Uniform Gate 结果
# 用法: python compare_phase2.py --tg-results results/tg_s42_gar.json --ug-results results/ug_s42_gar.json
# 输出: 对比表格 + 双曲线图 + Pass/Fail 判断

import argparse
import json
import os
import sys

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt


def load_results(path):
    with open(path) as f:
        return json.load(f)


def print_gar_table(tg, ug, baseline_gar=None):
    """Print turn-by-turn GAR comparison table with raw and normalized."""
    tg_gar = tg["avg_gar_per_turn"]
    ug_gar = ug["avg_gar_per_turn"]
    min_turns = min(len(tg_gar), len(ug_gar))

    tg_norm = tg.get("avg_normalized_gar_per_turn", [])
    ug_norm = ug.get("avg_normalized_gar_per_turn", [])
    has_norm = len(tg_norm) >= min_turns and len(ug_norm) >= min_turns

    header = f"{'Turn':>6}  {'TG_raw':>9}  {'UG_raw':>9}  {'Diff_raw':>9}"
    if has_norm:
        header += f"  {'TG_norm':>9}  {'UG_norm':>9}  {'Diff_norm':>10}"
    print(header)
    print("-" * len(header))

    for i in range(min_turns):
        diff_raw = tg_gar[i] - ug_gar[i]
        row = f"{i+1:>6}  {tg_gar[i]:>9.4f}  {ug_gar[i]:>9.4f}  {diff_raw:>+9.4f}"
        if has_norm:
            diff_norm = tg_norm[i] - ug_norm[i]
            row += f"  {tg_norm[i]:>9.4f}  {ug_norm[i]:>9.4f}  {diff_norm:>+10.4f}"
        print(row)

    print("-" * len(header))
    tg_mid = tg["mid_turns_avg_gar"]
    ug_mid = ug["mid_turns_avg_gar"]
    diff_mid = tg_mid - ug_mid
    row = f"{'Mid':>6}  {tg_mid:>9.4f}  {ug_mid:>9.4f}  {diff_mid:>+9.4f}"
    if has_norm:
        tg_mid_n = tg.get("mid_turns_avg_normalized_gar", 0)
        ug_mid_n = ug.get("mid_turns_avg_normalized_gar", 0)
        diff_mid_n = tg_mid_n - ug_mid_n
        row += f"  {tg_mid_n:>9.4f}  {ug_mid_n:>9.4f}  {diff_mid_n:>+10.4f}"
    print(row)


def plot_comparison(tg, ug, baseline_gar, output_path):
    """Plot raw GAR (top) and normalized GAR (bottom)."""
    tg_gar = tg["avg_gar_per_turn"]
    ug_gar = ug["avg_gar_per_turn"]
    min_turns = min(len(tg_gar), len(ug_gar))
    turns_x = list(range(1, min_turns + 1))

    tg_norm = tg.get("avg_normalized_gar_per_turn", [])
    ug_norm = ug.get("avg_normalized_gar_per_turn", [])
    has_norm = len(tg_norm) >= min_turns and len(ug_norm) >= min_turns

    nrows = 2 if has_norm else 1
    fig, axes = plt.subplots(nrows, 1, figsize=(10, 5.5 * nrows), sharex=True)
    if nrows == 1:
        axes = [axes]

    ax = axes[0]
    if baseline_gar:
        b = baseline_gar[:min_turns]
        ax.plot(turns_x, b, "r-s", linewidth=2, markersize=5, label="Baseline (no gate)", alpha=0.8)
    ax.plot(turns_x, ug_gar[:min_turns], "g-^", linewidth=2, markersize=5, label="Uniform Gate", alpha=0.8)
    ax.plot(turns_x, tg_gar[:min_turns], "b-o", linewidth=2.5, markersize=6, label="ThreadGate")

    tg_mid = tg["mid_turns_avg_gar"]
    ug_mid = ug["mid_turns_avg_gar"]
    ax.axhline(y=tg_mid, color="blue", linestyle="--", alpha=0.3)
    ax.axhline(y=ug_mid, color="green", linestyle="--", alpha=0.3)

    delta_pp = (tg_mid - ug_mid) * 100
    passed = delta_pp > 3.0
    ax.set_ylabel("Raw GAR", fontsize=12)
    ax.set_title(
        f"ThreadGate vs Uniform Gate GAR Comparison\n"
        f"TG mid: {tg_mid:.4f}, UG mid: {ug_mid:.4f}, "
        f"delta: {delta_pp:+.1f}pp ({'PASS' if passed else 'FAIL'}: >3pp required)",
        fontsize=11,
    )
    ax.legend(fontsize=10)
    ax.set_xticks(turns_x)
    ax.grid(True, alpha=0.3)

    if has_norm:
        ax2 = axes[1]
        ax2.plot(turns_x, ug_norm[:min_turns], "g-^", linewidth=2, markersize=5, label="Uniform Gate", alpha=0.8)
        ax2.plot(turns_x, tg_norm[:min_turns], "b-o", linewidth=2.5, markersize=6, label="ThreadGate")

        tg_mid_n = tg.get("mid_turns_avg_normalized_gar", 0)
        ug_mid_n = ug.get("mid_turns_avg_normalized_gar", 0)
        ax2.axhline(y=tg_mid_n, color="blue", linestyle="--", alpha=0.3)
        ax2.axhline(y=ug_mid_n, color="green", linestyle="--", alpha=0.3)

        delta_norm_pp = (tg_mid_n - ug_mid_n) * 100
        ax2.set_ylabel("Normalized GAR", fontsize=12)
        ax2.set_title(
            f"Normalized GAR: TG mid: {tg_mid_n:.4f}, UG mid: {ug_mid_n:.4f}, "
            f"delta: {delta_norm_pp:+.1f}pp",
            fontsize=11,
        )
        ax2.legend(fontsize=10)
        ax2.set_xticks(turns_x)
        ax2.grid(True, alpha=0.3)
        ax2.set_xlabel("Turn Index", fontsize=12)
    else:
        axes[0].set_xlabel("Turn Index", fontsize=12)

    fig.tight_layout()
    fig.savefig(output_path, dpi=150, bbox_inches="tight")
    plt.close()


def compare_mtbench(tg_mt_path, ug_mt_path):
    """Compare MT-Bench results if available."""
    if not (os.path.exists(tg_mt_path) and os.path.exists(ug_mt_path)):
        return None

    tg_mt = load_results(tg_mt_path)
    ug_mt = load_results(ug_mt_path)

    tg_overall = tg_mt["trained"]["summary"]["overall_avg"]
    ug_overall = ug_mt["trained"]["summary"]["overall_avg"]
    tg_t2 = tg_mt["trained"]["summary"]["turn2_avg"]
    ug_t2 = ug_mt["trained"]["summary"]["turn2_avg"]
    baseline_overall = tg_mt["baseline"]["summary"]["overall_avg"]
    baseline_t2 = tg_mt["baseline"]["summary"]["turn2_avg"]

    return {
        "threadgate": {"overall": tg_overall, "turn2": tg_t2},
        "uniform": {"overall": ug_overall, "turn2": ug_t2},
        "baseline": {"overall": baseline_overall, "turn2": baseline_t2},
    }


def main():
    parser = argparse.ArgumentParser(description="Compare ThreadGate vs Uniform Gate results")
    parser.add_argument("--tg-results", required=True, help="ThreadGate GAR results JSON")
    parser.add_argument("--ug-results", required=True, help="Uniform Gate GAR results JSON")
    parser.add_argument("--baseline-results", default="/root/turn_residual_gating/results/phase1_gar_results.json")
    parser.add_argument("--output-dir", default="/root/turn_residual_gating/results/")
    args = parser.parse_args()

    os.makedirs(args.output_dir, exist_ok=True)

    tg = load_results(args.tg_results)
    ug = load_results(args.ug_results)

    tg_source = tg.get("conversations_source", "unknown")
    ug_source = ug.get("conversations_source", "unknown")
    if tg_source != ug_source:
        print(f"WARNING: conversation sources differ! TG={tg_source}, UG={ug_source}")
        print("Results may not be directly comparable.")
    else:
        print(f"Conversations source: {tg_source}")

    baseline_gar = None
    if os.path.exists(args.baseline_results):
        baseline = load_results(args.baseline_results)
        baseline_gar = baseline["avg_gar_per_turn"]

    # GAR comparison table
    print(f"\n{'='*60}")
    print("GAR Turn-by-Turn Comparison")
    print(f"{'='*60}")
    print_gar_table(tg, ug, baseline_gar)

    # Pass/Fail
    tg_mid = tg["mid_turns_avg_gar"]
    ug_mid = ug["mid_turns_avg_gar"]
    delta_pp = (tg_mid - ug_mid) * 100
    passed = delta_pp > 3.0

    print(f"\n{'='*60}")
    print("Pass/Fail Criteria")
    print(f"{'='*60}")
    print(f"ThreadGate mid-turn GAR: {tg_mid:.4f}")
    print(f"Uniform mid-turn GAR:    {ug_mid:.4f}")
    print(f"Delta:                   {delta_pp:+.2f}pp")
    print(f"Criterion (>3pp):        {'PASS' if passed else 'FAIL'}")

    if tg.get("gar_recovery_pp") is not None:
        print(f"\nThreadGate GAR recovery vs baseline: {tg['gar_recovery_pp']:+.2f}pp")
    if ug.get("gar_recovery_pp") is not None:
        print(f"Uniform GAR recovery vs baseline:    {ug['gar_recovery_pp']:+.2f}pp")

    tg_norm_mid = tg.get("mid_turns_avg_normalized_gar")
    ug_norm_mid = ug.get("mid_turns_avg_normalized_gar")
    if tg_norm_mid is not None and ug_norm_mid is not None:
        norm_delta_pp = (tg_norm_mid - ug_norm_mid) * 100
        print(f"\nNormalized GAR:")
        print(f"ThreadGate mid-turn nGAR: {tg_norm_mid:.4f}")
        print(f"Uniform mid-turn nGAR:    {ug_norm_mid:.4f}")
        print(f"Delta:                    {norm_delta_pp:+.2f}pp")

    # MT-Bench comparison
    tg_mt_path = args.tg_results.replace("_gar.json", "_mtbench.json")
    ug_mt_path = args.ug_results.replace("_gar.json", "_mtbench.json")
    mt_results = compare_mtbench(tg_mt_path, ug_mt_path)

    if mt_results:
        print(f"\n{'='*60}")
        print("MT-Bench Style Scores")
        print(f"{'='*60}")
        print(f"                  ThreadGate  Uniform  Baseline")
        print(f"Overall avg:      {mt_results['threadgate']['overall']:.2f}        {mt_results['uniform']['overall']:.2f}     {mt_results['baseline']['overall']:.2f}")
        print(f"Turn 2 avg:       {mt_results['threadgate']['turn2']:.2f}        {mt_results['uniform']['turn2']:.2f}     {mt_results['baseline']['turn2']:.2f}")
        mt_improvement = mt_results["threadgate"]["turn2"] - mt_results["baseline"]["turn2"]
        print(f"TG turn2 improvement vs baseline: {mt_improvement:+.2f}pp")

    # Plot
    plot_path = os.path.join(args.output_dir, "phase2_gar_comparison.png")
    plot_comparison(tg, ug, baseline_gar, plot_path)
    print(f"\nComparison plot saved to {plot_path}")

    # Save combined summary
    summary = {
        "gar": {
            "threadgate_mid": tg_mid,
            "uniform_mid": ug_mid,
            "delta_pp": delta_pp,
            "pass": passed,
            "threadgate_recovery_pp": tg.get("gar_recovery_pp"),
            "uniform_recovery_pp": ug.get("gar_recovery_pp"),
        },
        "normalized_gar": {
            "threadgate_mid": tg.get("mid_turns_avg_normalized_gar"),
            "uniform_mid": ug.get("mid_turns_avg_normalized_gar"),
            "delta_pp": (
                (tg.get("mid_turns_avg_normalized_gar", 0) - ug.get("mid_turns_avg_normalized_gar", 0)) * 100
            ),
        },
    }
    if mt_results:
        summary["mtbench"] = mt_results

    summary["conversations_source"] = {
        "threadgate": tg_source,
        "uniform": ug_source,
        "consistent": tg_source == ug_source,
    }

    summary_path = os.path.join(args.output_dir, "phase2_comparison_summary.json")
    with open(summary_path, "w") as f:
        json.dump(summary, f, indent=2)
    print(f"Summary saved to {summary_path}")


if __name__ == "__main__":
    main()
