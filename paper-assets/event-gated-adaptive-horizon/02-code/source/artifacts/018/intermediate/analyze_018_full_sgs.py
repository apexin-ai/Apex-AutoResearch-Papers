#!/usr/bin/env python3
"""Exp-018 Full-SGS analysis: eval curves, NVE trajectories, CIVO verdict.

Compares exp_018 (full_sgs=True, 93% gradient detach) against reference
experiments to determine whether CIVO is gradient-level or representation-level.

Outputs:
  - 018_eval_comparison.{pdf,png}   — learning curves overlay
  - 018_nve_comparison.{pdf,png}    — NVE trajectories with 1.5x threshold
  - 018_summary.json                — machine-readable results
  - stdout summary table
"""

import argparse
import json
import os
import sys
from collections import OrderedDict

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker


# ---------------------------------------------------------------------------
# Data loading
# ---------------------------------------------------------------------------

def load_metrics_jsonl(logdir):
    path = os.path.join(logdir, "metrics.jsonl")
    if not os.path.exists(path):
        return None, None
    eval_returns = {}
    value_means = {}
    with open(path) as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            d = json.loads(line)
            step = d.get("step")
            if step is None:
                continue
            if "eval_return" in d:
                eval_returns[step] = d["eval_return"]
            if "value_mean" in d:
                value_means[step] = d["value_mean"]
    return eval_returns, value_means


def load_eval_returns(logdir):
    er, _ = load_metrics_jsonl(logdir)
    if er is None:
        print(f"WARNING: no metrics.jsonl in {logdir}", file=sys.stderr)
        return {}
    return er


def load_ve_data(logdir):
    er, vm = load_metrics_jsonl(logdir)
    if er is None or vm is None:
        return {}
    common = sorted(set(er) & set(vm))
    ratios = {}
    for s in common:
        if abs(er[s]) > 1e-8:
            ratios[s] = vm[s] / er[s]
    return ratios


# ---------------------------------------------------------------------------
# NVE computation
# ---------------------------------------------------------------------------

def compute_nve_series(exp_ve, baseline_ve):
    """NVE = exp_ve_ratio / baseline_ve_ratio at nearest-neighbor steps."""
    if not baseline_ve or not exp_ve:
        return {}
    bl_steps = sorted(baseline_ve.keys())
    nve = {}
    for s in sorted(exp_ve.keys()):
        nearest = min(bl_steps, key=lambda bs: abs(bs - s))
        bl_val = baseline_ve[nearest]
        if abs(bl_val) > 1e-8:
            nve[s] = exp_ve[s] / bl_val
    return nve


def max_nve(nve_dict):
    if not nve_dict:
        return float("nan")
    return max(nve_dict.values())


# ---------------------------------------------------------------------------
# CIVO verdict
# ---------------------------------------------------------------------------

def civo_verdict(nve_dict, threshold=1.5, min_consecutive=2):
    """Determine CIVO status from NVE trajectory.

    Returns: ("CIVO_PRESENT", "CIVO_ABSENT", or "CIVO_TRANSIENT"), detail string
    """
    if not nve_dict:
        return "NO_DATA", "insufficient NVE data"

    steps = sorted(nve_dict.keys())
    above = [s for s in steps if nve_dict[s] > threshold]

    if not above:
        max_val = max(nve_dict[s] for s in steps)
        return "CIVO_ABSENT", f"NVE always <= {threshold}x (max {max_val:.3f}x)"

    consecutive_runs = []
    current_run = [above[0]]
    for i in range(1, len(above)):
        prev_idx = steps.index(above[i - 1])
        curr_idx = steps.index(above[i])
        if curr_idx == prev_idx + 1:
            current_run.append(above[i])
        else:
            consecutive_runs.append(current_run)
            current_run = [above[i]]
    consecutive_runs.append(current_run)

    max_run = max(len(r) for r in consecutive_runs)
    max_nve_val = max(nve_dict[s] for s in above)

    if max_run >= min_consecutive:
        last_step = steps[-1]
        last_above = above[-1]
        if last_above == last_step or steps.index(last_above) >= len(steps) - 2:
            return "CIVO_PRESENT", (
                f"NVE > {threshold}x for {max_run} consecutive checkpoints "
                f"(max {max_nve_val:.3f}x), persists to end"
            )
        else:
            return "CIVO_TRANSIENT", (
                f"NVE > {threshold}x for {max_run} consecutive checkpoints "
                f"(max {max_nve_val:.3f}x), but recovers after step {last_above}"
            )
    else:
        return "CIVO_TRANSIENT", (
            f"NVE > {threshold}x at {len(above)} step(s) but never "
            f"{min_consecutive}+ consecutive (max {max_nve_val:.3f}x)"
        )


# ---------------------------------------------------------------------------
# Plotting
# ---------------------------------------------------------------------------

COLORS = {
    "018": "#d62728",
    "008d": "#ff7f0e",
    "008f": "#2ca02c",
    "016e": "#9467bd",
    "baseline": "#1f77b4",
}

LABELS = {
    "018": "018 Full-SGS (93% detach)",
    "008d": "008d CIVO collapse",
    "008f": "008f no dt_embed",
    "016e": "016e reward-only SGS",
    "baseline": "baseline",
}


def plot_eval_curves(curves, output_dir):
    fig, ax = plt.subplots(figsize=(8, 5))
    for key, data in curves.items():
        if not data:
            continue
        steps = sorted(data.keys())
        vals = [data[s] for s in steps]
        ax.plot(
            [s / 1000 for s in steps], vals,
            color=COLORS.get(key, "gray"),
            label=LABELS.get(key, key),
            linewidth=2 if key == "018" else 1.5,
            alpha=1.0 if key == "018" else 0.7,
            marker="o" if key == "018" else None,
            markersize=4,
        )
    ax.set_xlabel("Environment Steps (×1000)")
    ax.set_ylabel("Eval Return")
    ax.set_title("Exp-018 Full-SGS: Learning Curves Comparison")
    ax.legend(fontsize=9, loc="best")
    ax.grid(True, alpha=0.3)
    ax.xaxis.set_major_locator(ticker.MaxNLocator(integer=True))
    fig.tight_layout()
    for ext in ["pdf", "png"]:
        path = os.path.join(output_dir, f"018_eval_comparison.{ext}")
        fig.savefig(path, dpi=150, bbox_inches="tight")
    plt.close(fig)
    print(f"Saved eval curves to {output_dir}/018_eval_comparison.{{pdf,png}}")


def plot_nve_curves(nve_series, output_dir, threshold=1.5):
    fig, ax = plt.subplots(figsize=(8, 5))
    for key, data in nve_series.items():
        if not data:
            continue
        steps = sorted(data.keys())
        vals = [data[s] for s in steps]
        ax.plot(
            [s / 1000 for s in steps], vals,
            color=COLORS.get(key, "gray"),
            label=LABELS.get(key, key),
            linewidth=2 if key == "018" else 1.5,
            alpha=1.0 if key == "018" else 0.7,
            marker="o" if key == "018" else None,
            markersize=4,
        )
    ax.axhline(y=threshold, color="red", linestyle="--", linewidth=1, alpha=0.6,
               label=f"CIVO threshold ({threshold}x)")
    ax.axhline(y=1.0, color="gray", linestyle=":", linewidth=0.8, alpha=0.5)
    ax.set_xlabel("Environment Steps (×1000)")
    ax.set_ylabel("NVE (baseline-normalized)")
    ax.set_title("Exp-018 Full-SGS: NVE Trajectories")
    ax.legend(fontsize=9, loc="best")
    ax.grid(True, alpha=0.3)
    ax.xaxis.set_major_locator(ticker.MaxNLocator(integer=True))
    fig.tight_layout()
    for ext in ["pdf", "png"]:
        path = os.path.join(output_dir, f"018_nve_comparison.{ext}")
        fig.savefig(path, dpi=150, bbox_inches="tight")
    plt.close(fig)
    print(f"Saved NVE curves to {output_dir}/018_nve_comparison.{{pdf,png}}")


# ---------------------------------------------------------------------------
# Summary table
# ---------------------------------------------------------------------------

def compute_summary(label, eval_returns, nve_dict):
    steps = sorted(eval_returns.keys())
    if not steps:
        return {"exp_id": label, "peak_eval": None, "final_eval": None,
                "max_NVE": None, "CIVO_verdict": "NO_DATA"}
    peak = max(eval_returns.values())
    final = eval_returns[steps[-1]]
    mnve = max_nve(nve_dict) if nve_dict else None
    verdict, _ = civo_verdict(nve_dict) if nve_dict else ("N/A", "")
    return {
        "exp_id": label,
        "peak_eval": round(peak, 2),
        "final_eval": round(final, 2),
        "max_NVE": round(mnve, 4) if mnve and mnve == mnve else None,
        "CIVO_verdict": verdict,
    }


def print_summary_table(summaries):
    print("\n" + "=" * 90)
    print("  SUMMARY TABLE")
    print("=" * 90)
    hdr = f"  {'Exp':30s} {'Peak Eval':>10s} {'Final Eval':>11s} {'Max NVE':>9s}  {'Verdict'}"
    print(hdr)
    print("  " + "-" * 86)
    for s in summaries:
        peak = f"{s['peak_eval']:.1f}" if s["peak_eval"] is not None else "N/A"
        final = f"{s['final_eval']:.1f}" if s["final_eval"] is not None else "N/A"
        mnve = f"{s['max_NVE']:.4f}" if s["max_NVE"] is not None else "N/A"
        print(f"  {s['exp_id']:30s} {peak:>10s} {final:>11s} {mnve:>9s}  {s['CIVO_verdict']}")
    print()


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(
        description="Analyze exp-018 Full-SGS results vs reference experiments")
    parser.add_argument("--logdir-018", required=True,
                        help="Logdir for exp_018 (full_sgs)")
    parser.add_argument("--logdir-008d", default=None,
                        help="Logdir for exp_008d (CIVO collapse ref)")
    parser.add_argument("--logdir-008f", default=None,
                        help="Logdir for exp_008f (no dt_embed ref)")
    parser.add_argument("--logdir-016e", default=None,
                        help="Logdir for exp_016e (reward-only SGS ref)")
    parser.add_argument("--baseline-logdir", required=True,
                        help="Baseline logdir for NVE normalization")
    parser.add_argument("--output-dir", default=".",
                        help="Output directory for plots and JSON")
    parser.add_argument("--nve-threshold", type=float, default=1.5,
                        help="CIVO NVE threshold (default: 1.5)")
    parser.add_argument("--min-consecutive", type=int, default=2,
                        help="Min consecutive checkpoints above threshold (default: 2)")
    args = parser.parse_args()

    os.makedirs(args.output_dir, exist_ok=True)

    experiments = OrderedDict()
    experiments["018"] = args.logdir_018
    if args.logdir_008d:
        experiments["008d"] = args.logdir_008d
    if args.logdir_008f:
        experiments["008f"] = args.logdir_008f
    if args.logdir_016e:
        experiments["016e"] = args.logdir_016e
    experiments["baseline"] = args.baseline_logdir

    # Load data
    eval_curves = {}
    ve_ratios = {}
    for key, logdir in experiments.items():
        eval_curves[key] = load_eval_returns(logdir)
        ve_ratios[key] = load_ve_data(logdir)

    baseline_ve = ve_ratios["baseline"]

    # Compute NVE
    nve_series = {}
    for key in experiments:
        if key == "baseline":
            nve_series[key] = {s: 1.0 for s in baseline_ve}
        else:
            nve_series[key] = compute_nve_series(ve_ratios[key], baseline_ve)

    # Verdict for 018
    verdict_018, detail_018 = civo_verdict(
        nve_series.get("018", {}), args.nve_threshold, args.min_consecutive)

    print("\n" + "=" * 90)
    print("  EXP-018 FULL-SGS ANALYSIS")
    print("=" * 90)
    print(f"\n  018 verdict: {verdict_018}")
    print(f"  Detail: {detail_018}")

    if verdict_018 == "CIVO_ABSENT":
        print("\n  → CIVO is GRADIENT-LEVEL: removing 93% of gradients eliminates collapse")
        print("    → obs decoder gradients are a necessary condition for CIVO")
        print("    → Paper claim C2 strengthened")
    elif verdict_018 == "CIVO_PRESENT":
        print("\n  → CIVO is REPRESENTATION-LEVEL: collapse persists despite 93% gradient removal")
        print("    → KL training alone maintains harmful dt_emb representation")
        print("    → Intervention must target representation, not just gradients")
    elif verdict_018 == "CIVO_TRANSIENT":
        print("\n  → PARTIAL gradient effect: obs decoder contributes but is not sole cause")
        print("    → Need finer-grained ablation to isolate components")

    # Summary table
    summaries = []
    for key in experiments:
        summaries.append(compute_summary(key, eval_curves[key], nve_series.get(key, {})))
    print_summary_table(summaries)

    # Plots
    plot_eval_curves(eval_curves, args.output_dir)
    plot_nve_curves(
        {k: v for k, v in nve_series.items() if k != "baseline"},
        args.output_dir, args.nve_threshold,
    )

    # JSON output
    json_out = {
        "experiment": "018_full_sgs",
        "nve_threshold": args.nve_threshold,
        "min_consecutive_checkpoints": args.min_consecutive,
        "verdict_018": verdict_018,
        "verdict_detail": detail_018,
        "interpretation": {
            "CIVO_ABSENT": "gradient-level: Full-SGS eliminates CIVO",
            "CIVO_PRESENT": "representation-level: CIVO persists despite gradient removal",
            "CIVO_TRANSIENT": "partial: obs decoder contributes but not sole cause",
        }.get(verdict_018, "unknown"),
        "summaries": summaries,
        "nve_trajectories": {
            key: {str(s): round(v, 6) for s, v in sorted(data.items())}
            for key, data in nve_series.items() if data
        },
    }
    json_path = os.path.join(args.output_dir, "018_summary.json")
    with open(json_path, "w") as f:
        json.dump(json_out, f, indent=2)
    print(f"Saved JSON summary to {json_path}")


if __name__ == "__main__":
    main()
