#!/usr/bin/env python3
"""Gate dt distribution analysis for event-gated DreamerV3 experiments.

Reads gate_dt_*_frac fields from metrics.jsonl, computes distribution statistics
over training, and checks for gate degeneration (dt=1 fraction > 95%).

Compatible with both DMC and ManiSkill3 metrics formats.

Input:  one or more logdir paths containing metrics.jsonl
Output: dt distribution stats table + optional bar chart (--plot)
"""

import argparse
import json
import os
import sys


def load_gate_metrics(logdir):
    """Load gate dt fraction and stats from metrics.jsonl."""
    path = os.path.join(logdir, "metrics.jsonl")
    if not os.path.exists(path):
        print(f"ERROR: {path} not found", file=sys.stderr)
        return []

    records = []
    with open(path) as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            d = json.loads(line)
            if "gate_dt_1_frac" in d or "gate_dt_mean" in d:
                records.append(d)
    return records


def extract_dt_fracs(record):
    """Extract dt fraction dict {1: frac, 2: frac, ...} from a single record."""
    fracs = {}
    for i in range(1, 17):
        key = f"gate_dt_{i}_frac"
        if key in record:
            fracs[i] = record[key]
    return fracs


def analyze_logdir(logdir, label):
    """Analyze dt distribution for one experiment."""
    records = load_gate_metrics(logdir)
    if not records:
        print(f"\n[{label}] No gate metrics found — likely a baseline (no event gate).")
        return None

    all_fracs = []
    steps = []
    for r in records:
        fracs = extract_dt_fracs(r)
        if fracs:
            all_fracs.append(fracs)
            steps.append(r.get("step", 0))

    if not all_fracs:
        print(f"\n[{label}] gate_dt_*_frac fields not found in metrics.")
        return None

    dt_keys = sorted(set().union(*[f.keys() for f in all_fracs]))

    # Overall mean distribution (average across all logged steps)
    mean_dist = {}
    for k in dt_keys:
        vals = [f.get(k, 0.0) for f in all_fracs]
        mean_dist[k] = sum(vals) / len(vals)

    # Last-10% distribution
    n_tail = max(1, len(all_fracs) // 10)
    tail_fracs = all_fracs[-n_tail:]
    tail_dist = {}
    for k in dt_keys:
        vals = [f.get(k, 0.0) for f in tail_fracs]
        tail_dist[k] = sum(vals) / len(vals)

    # dt stats from logged fields
    dt_means = [r["gate_dt_mean"] for r in records if "gate_dt_mean" in r]
    dt_stds = [r["gate_dt_std"] for r in records if "gate_dt_std" in r]
    entropies = [r["gate_empirical_entropy"] for r in records if "gate_empirical_entropy" in r]

    # Degeneration check
    dt1_tail = tail_dist.get(1, 0.0)
    degenerated = dt1_tail > 0.95

    result = {
        "label": label,
        "n_records": len(records),
        "dt_keys": dt_keys,
        "mean_dist": mean_dist,
        "tail_dist": tail_dist,
        "dt1_tail_frac": dt1_tail,
        "degenerated": degenerated,
        "dt_mean_final": dt_means[-1] if dt_means else None,
        "dt_std_final": dt_stds[-1] if dt_stds else None,
        "entropy_final": entropies[-1] if entropies else None,
        "steps": steps,
        "all_fracs": all_fracs,
    }

    # Print results
    print(f"\n{'=' * 65}")
    print(f"  {label}")
    print(f"{'=' * 65}")

    print(f"\n  Distribution (overall mean / last 10%):")
    print(f"  {'dt':>4s}  {'mean':>8s}  {'last10%':>8s}  bar (last 10%)")
    print(f"  {'----':>4s}  {'--------':>8s}  {'--------':>8s}  ----")
    for k in dt_keys:
        m = mean_dist[k]
        t = tail_dist[k]
        bar_len = int(t * 40)
        print(f"  dt={k:<2d}  {m:>7.1%}  {t:>7.1%}  {'█' * bar_len}{'░' * (40 - bar_len)}")

    print(f"\n  dt_mean (final): {result['dt_mean_final']:.4f}" if result['dt_mean_final'] is not None else "")
    print(f"  dt_std  (final): {result['dt_std_final']:.4f}" if result['dt_std_final'] is not None else "")
    print(f"  entropy (final): {result['entropy_final']:.4f}" if result['entropy_final'] is not None else "")
    print(f"\n  dt=1 fraction (last 10%): {dt1_tail:.1%}")
    if degenerated:
        print(f"  *** GATE DEGENERATED — dt=1 > 95% ***")
    else:
        print(f"  Gate active (dt=1 <= 95%)")

    return result


def save_plot(results, output_path):
    """Save dt distribution bar chart for all experiments."""
    try:
        import matplotlib
        matplotlib.use("Agg")
        import matplotlib.pyplot as plt
        import numpy as np
    except ImportError:
        print("WARNING: matplotlib not available, skipping plot", file=sys.stderr)
        return

    n_exp = len(results)
    if n_exp == 0:
        return

    all_dt_keys = sorted(set().union(*[set(r["dt_keys"]) for r in results]))
    n_dt = len(all_dt_keys)

    fig, axes = plt.subplots(1, n_exp, figsize=(5 * n_exp, 4), squeeze=False)

    colors = plt.cm.viridis(np.linspace(0.15, 0.85, max(n_dt, 1)))

    for idx, res in enumerate(results):
        ax = axes[0][idx]
        dist = res["tail_dist"]
        vals = [dist.get(k, 0.0) for k in all_dt_keys]
        bars = ax.bar([f"dt={k}" for k in all_dt_keys], vals, color=colors[:len(vals)])

        for bar, v in zip(bars, vals):
            if v > 0.02:
                ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 0.01,
                        f"{v:.1%}", ha="center", va="bottom", fontsize=8)

        ax.set_ylim(0, 1.1)
        ax.set_ylabel("Fraction" if idx == 0 else "")
        ax.set_title(res["label"], fontsize=10)
        ax.grid(axis="y", alpha=0.3)

        if res["degenerated"]:
            ax.set_facecolor("#fff0f0")
            ax.set_title(f"{res['label']}\n(DEGENERATED)", fontsize=10, color="red")

    fig.suptitle("Gate dt Distribution (last 10% of training)", fontsize=12)
    fig.tight_layout()
    os.makedirs(os.path.dirname(os.path.abspath(output_path)), exist_ok=True)
    fig.savefig(output_path, dpi=150, bbox_inches="tight")
    plt.close(fig)
    print(f"\nSaved plot to {output_path}")


def main():
    parser = argparse.ArgumentParser(
        description="Analyze gate dt distribution from DreamerV3 event-gated experiments")
    parser.add_argument("--logdirs", nargs="+", required=True,
                        help="One or more experiment logdir paths")
    parser.add_argument("--labels", nargs="+", default=None,
                        help="Labels for each logdir (default: directory names)")
    parser.add_argument("--plot", default=None,
                        help="Save distribution bar chart to this path (e.g. dt_dist.png)")
    parser.add_argument("--output", default=None,
                        help="Save results as JSON to this path")
    args = parser.parse_args()

    if args.labels and len(args.labels) != len(args.logdirs):
        print("ERROR: --labels count must match --logdirs count", file=sys.stderr)
        sys.exit(1)

    labels = args.labels or [os.path.basename(d.rstrip("/")) for d in args.logdirs]
    results = []

    for logdir, label in zip(args.logdirs, labels):
        res = analyze_logdir(logdir, label)
        if res is not None:
            results.append(res)

    if args.plot and results:
        save_plot(results, args.plot)

    if args.output:
        serializable = []
        for res in results:
            serializable.append({
                "label": res["label"],
                "n_records": res["n_records"],
                "mean_distribution": {str(k): round(v, 6) for k, v in res["mean_dist"].items()},
                "tail_distribution": {str(k): round(v, 6) for k, v in res["tail_dist"].items()},
                "dt1_tail_frac": round(res["dt1_tail_frac"], 6),
                "degenerated": res["degenerated"],
                "dt_mean_final": res["dt_mean_final"],
                "dt_std_final": res["dt_std_final"],
                "entropy_final": res["entropy_final"],
            })
        os.makedirs(os.path.dirname(os.path.abspath(args.output)), exist_ok=True)
        with open(args.output, "w") as f:
            json.dump(serializable, f, indent=2)
        print(f"\nSaved JSON to {args.output}")

    if not results:
        print("\nNo experiments with gate metrics found.")


if __name__ == "__main__":
    main()
