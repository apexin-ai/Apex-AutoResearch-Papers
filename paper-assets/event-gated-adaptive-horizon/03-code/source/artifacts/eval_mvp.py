#!/usr/bin/env python3
"""
MVP Pass/Fail evaluation for Event-Gated Adaptive-Horizon RSSM.
Reads baseline and event-gated training logs, computes 4 MVP criteria.
"""
import argparse
import json
import math
import os
import sys
from collections import defaultdict

import numpy as np


def load_metrics(logdir):
    path = os.path.join(logdir, "metrics.jsonl")
    if not os.path.exists(path):
        print(f"WARNING: {path} not found")
        return []
    rows = []
    with open(path) as f:
        for line in f:
            line = line.strip()
            if line:
                rows.append(json.loads(line))
    return rows


def split_rows(rows):
    episode_rows = []
    train_rows = []
    for r in rows:
        if "model_loss" in r or "gate_dt_mean" in r:
            train_rows.append(r)
        else:
            episode_rows.append(r)
    return episode_rows, train_rows


def last_fraction(values, frac=0.1):
    if not values:
        return []
    n = max(1, int(len(values) * frac))
    return values[-n:]


def compute_return(episode_rows):
    if not episode_rows:
        return None
    returns = [r["train_return"] for r in episode_rows if "train_return" in r]
    if not returns:
        return None
    tail = last_fraction(returns)
    return float(np.mean(tail))


def criterion_1_return(baseline_ep, gated_ep):
    bl_ret = compute_return(baseline_ep)
    eg_ret = compute_return(gated_ep)
    ratio = None
    passed = None
    if bl_ret is not None and eg_ret is not None and bl_ret > 0:
        ratio = eg_ret / bl_ret
        passed = ratio >= 0.8
    print("Criterion 1 (Return >= 80% baseline):", fmt_pass(passed))
    print(f"  Baseline final return: {fmt_val(bl_ret)}")
    print(f"  Event-gated final return: {fmt_val(eg_ret)}")
    print(f"  Ratio: {fmt_val(ratio)}")
    return passed


def criterion_2_entropy(gated_train):
    ents = [r["gate_empirical_entropy"] for r in gated_train if "gate_empirical_entropy" in r]
    if not ents:
        ratios = [r["gate_entropy_ratio"] for r in gated_train if "gate_entropy_ratio" in r]
        tail = last_fraction(ratios) if ratios else []
        mean_ratio = float(np.mean(tail)) if tail else None
        threshold = 0.3 / math.log(8)
        passed = mean_ratio > threshold if mean_ratio is not None else None
        print("Criterion 2 (Gate entropy > 0.3 nats):", fmt_pass(passed))
        print(f"  Mean gate_entropy_ratio (last 10%): {fmt_val(mean_ratio)} (threshold {threshold:.4f})")
        return passed
    tail = last_fraction(ents)
    mean_ent = float(np.mean(tail))
    passed = mean_ent > 0.3
    print("Criterion 2 (Gate entropy > 0.3 nats):", fmt_pass(passed))
    print(f"  Mean gate entropy (last 10%): {mean_ent:.4f} nats")
    return passed


def criterion_3_horizon(gated_train):
    dts = [r["gate_dt_mean"] for r in gated_train if "gate_dt_mean" in r]
    if not dts:
        print("Criterion 3 (H_eff > 1.2 x H_nominal):", fmt_pass(None))
        print("  gate_dt_mean: N/A")
        return None
    tail = last_fraction(dts)
    mean_dt = float(np.mean(tail))
    passed = mean_dt > 1.2
    print("Criterion 3 (H_eff > 1.2 x H_nominal):", fmt_pass(passed))
    print(f"  Mean dt (last 10%): {mean_dt:.4f}")
    print(f"  H_eff / H_nominal: {mean_dt:.4f}")
    return passed


def criterion_4_temporal(gated_train):
    dt_stds = [r["gate_dt_std"] for r in gated_train if "gate_dt_std" in r]
    if not dt_stds:
        print("Criterion 4 (dt temporal structure):", fmt_pass(None))
        print("  gate_dt_std: N/A")
        return None
    tail = last_fraction(dt_stds)
    mean_std = float(np.mean(tail))
    dt_means = [r["gate_dt_mean"] for r in gated_train if "gate_dt_mean" in r]
    autocorr = None
    if len(dt_means) >= 4:
        arr = np.array(dt_means)
        arr = arr - arr.mean()
        if np.std(arr) > 1e-9:
            autocorr = float(np.corrcoef(arr[:-1], arr[1:])[0, 1])
    passed_std = mean_std > 0.5
    passed_ac = autocorr is not None and autocorr > 0.15
    passed = passed_std or passed_ac
    print("Criterion 4 (dt temporal structure):", fmt_pass(passed))
    print(f"  dt std (last 10%): {mean_std:.4f} (threshold 0.5)")
    print(f"  Lag-1 autocorrelation: {fmt_val(autocorr)} (threshold 0.15)")
    return passed


def fmt_pass(v):
    if v is None:
        return "N/A (insufficient data)"
    return "PASS" if v else "FAIL"


def fmt_val(v):
    if v is None:
        return "N/A"
    return f"{v:.4f}"


def save_plots(baseline_ep, gated_ep, gated_train, outdir):
    try:
        import matplotlib
        matplotlib.use("Agg")
        import matplotlib.pyplot as plt
    except ImportError:
        print("\nmatplotlib not available, skipping plots.")
        return

    os.makedirs(outdir, exist_ok=True)

    # Return curves
    fig, ax = plt.subplots(figsize=(10, 5))
    if baseline_ep:
        baseline_ep = [r for r in baseline_ep if "train_return" in r]
        steps_b = [r.get("step", i) for i, r in enumerate(baseline_ep)]
        rets_b = [r["train_return"] for r in baseline_ep]
        ax.plot(steps_b, rets_b, alpha=0.4, color="blue", label="Baseline")
        if len(rets_b) >= 5:
            win = max(3, len(rets_b) // 10)
            smooth = np.convolve(rets_b, np.ones(win) / win, mode="valid")
            ax.plot(steps_b[win - 1:], smooth, color="blue", linewidth=2)
    if gated_ep:
        gated_ep = [r for r in gated_ep if "train_return" in r]
        steps_g = [r.get("step", i) for i, r in enumerate(gated_ep)]
        rets_g = [r["train_return"] for r in gated_ep]
        ax.plot(steps_g, rets_g, alpha=0.4, color="red", label="Event-gated")
        if len(rets_g) >= 5:
            win = max(3, len(rets_g) // 10)
            smooth = np.convolve(rets_g, np.ones(win) / win, mode="valid")
            ax.plot(steps_g[win - 1:], smooth, color="red", linewidth=2)
    ax.set_xlabel("Step")
    ax.set_ylabel("Train Return")
    ax.set_title("Return Curves")
    ax.legend()
    ax.grid(True, alpha=0.3)
    fig.tight_layout()
    fig.savefig(os.path.join(outdir, "return_curves.png"), dpi=150)
    plt.close(fig)
    print(f"  Saved {outdir}/return_curves.png")

    if not gated_train:
        return

    # Gate entropy over training
    steps_t = [r["step"] for r in gated_train if "gate_empirical_entropy" in r]
    ents = [r["gate_empirical_entropy"] for r in gated_train if "gate_empirical_entropy" in r]
    if steps_t:
        fig, ax = plt.subplots(figsize=(10, 4))
        ax.plot(steps_t, ents, "o-", color="green")
        ax.axhline(0.3, color="red", linestyle="--", label="Threshold (0.3 nats)")
        ax.set_xlabel("Step")
        ax.set_ylabel("Gate Empirical Entropy (nats)")
        ax.set_title("Gate Entropy over Training")
        ax.legend()
        ax.grid(True, alpha=0.3)
        fig.tight_layout()
        fig.savefig(os.path.join(outdir, "gate_entropy.png"), dpi=150)
        plt.close(fig)
        print(f"  Saved {outdir}/gate_entropy.png")

    # dt distribution over training
    dt_keys = [f"gate_dt_{i}_frac" for i in range(1, 9)]
    steps_dt = []
    fracs = defaultdict(list)
    for r in gated_train:
        if "gate_dt_1_frac" in r:
            steps_dt.append(r["step"])
            for k in dt_keys:
                fracs[k].append(r.get(k, 0.0))
    if steps_dt:
        fig, ax = plt.subplots(figsize=(10, 5))
        bottom = np.zeros(len(steps_dt))
        colors = plt.cm.viridis(np.linspace(0.1, 0.9, 8))
        for i, k in enumerate(dt_keys):
            vals = np.array(fracs[k])
            ax.bar(range(len(steps_dt)), vals, bottom=bottom, color=colors[i],
                   label=f"dt={i + 1}", width=0.8)
            bottom += vals
        ax.set_xticks(range(len(steps_dt)))
        ax.set_xticklabels([str(s) for s in steps_dt], rotation=45)
        ax.set_xlabel("Step")
        ax.set_ylabel("Fraction")
        ax.set_title("Δt Distribution over Training")
        ax.legend(loc="upper right", ncol=4, fontsize=8)
        ax.grid(True, alpha=0.3, axis="y")
        fig.tight_layout()
        fig.savefig(os.path.join(outdir, "dt_distribution.png"), dpi=150)
        plt.close(fig)
        print(f"  Saved {outdir}/dt_distribution.png")

    # gate_dt_mean over training
    steps_m = [r["step"] for r in gated_train if "gate_dt_mean" in r]
    dt_means = [r["gate_dt_mean"] for r in gated_train if "gate_dt_mean" in r]
    if steps_m:
        fig, ax = plt.subplots(figsize=(10, 4))
        ax.plot(steps_m, dt_means, "s-", color="purple")
        ax.axhline(1.2, color="red", linestyle="--", label="Threshold (1.2)")
        ax.set_xlabel("Step")
        ax.set_ylabel("Mean Δt")
        ax.set_title("Gate Δt Mean over Training")
        ax.legend()
        ax.grid(True, alpha=0.3)
        fig.tight_layout()
        fig.savefig(os.path.join(outdir, "dt_mean.png"), dpi=150)
        plt.close(fig)
        print(f"  Saved {outdir}/dt_mean.png")


def main():
    parser = argparse.ArgumentParser(description="MVP evaluation for event-gated RSSM")
    parser.add_argument("--baseline_dir", required=True, help="Path to baseline logdir")
    parser.add_argument("--gated_dir", required=True, help="Path to event-gated logdir")
    parser.add_argument("--plot_dir", default=None, help="Directory to save plots (default: gated_dir/eval_plots)")
    args = parser.parse_args()

    baseline_rows = load_metrics(args.baseline_dir)
    gated_rows = load_metrics(args.gated_dir)

    baseline_ep, baseline_train = split_rows(baseline_rows)
    gated_ep, gated_train = split_rows(gated_rows)

    print(f"Loaded {len(baseline_rows)} baseline rows ({len(baseline_ep)} episodes, {len(baseline_train)} train)")
    print(f"Loaded {len(gated_rows)} event-gated rows ({len(gated_ep)} episodes, {len(gated_train)} train)")

    bl_steps = set(r.get("step", -1) for r in baseline_rows)
    eg_steps = set(r.get("step", -1) for r in gated_rows)
    print(f"Baseline step range: {min(bl_steps)}-{max(bl_steps)}")
    print(f"Event-gated step range: {min(eg_steps)}-{max(eg_steps)}")
    print()

    print("=" * 50)
    print("         MVP Evaluation Results")
    print("=" * 50)
    print()

    results = []
    results.append(criterion_1_return(baseline_ep, gated_ep))
    print()
    results.append(criterion_2_entropy(gated_train))
    print()
    results.append(criterion_3_horizon(gated_train))
    print()
    results.append(criterion_4_temporal(gated_train))
    print()

    n_pass = sum(1 for r in results if r is True)
    n_eval = sum(1 for r in results if r is not None)
    print("=" * 50)
    print(f"Overall: {n_pass}/{n_eval} PASS ({len(results) - n_eval} criteria had insufficient data)")
    print("=" * 50)

    plot_dir = args.plot_dir or os.path.join(args.gated_dir, "eval_plots")
    print(f"\nGenerating plots to {plot_dir} ...")
    save_plots(baseline_ep, gated_ep, gated_train, plot_dir)
    print("\nDone.")


if __name__ == "__main__":
    main()
