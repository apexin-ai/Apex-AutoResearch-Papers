"""Visualize exp_018 Full-SGS results vs controls — eval curves + NVE trajectories."""
import argparse
import json
import os
import sys

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

# === CONFIGURE THESE PATHS ===
LOGDIR_018 = "/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_018_full_sgs_walker_s1"  # UPDATE when ready
LOGDIR_008D = "/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_008d_factorial_walker_s1"
LOGDIR_008F = "/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_008f_factorial_walker_s1"
LOGDIR_BASELINE = "/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_001_baseline_walker_s1"
OUTPUT_DIR = "/root/autodl-tmp/event-gated-adaptive-horizon/figures/paper/"
# ==============================

EXPERIMENTS = {
    "018": {"logdir": LOGDIR_018, "color": "tab:red", "ls": "--", "label": "018 Full-SGS"},
    "008d": {"logdir": LOGDIR_008D, "color": "tab:red", "ls": "-", "label": "008d (trained+exposed)"},
    "008f": {"logdir": LOGDIR_008F, "color": "tab:green", "ls": "-", "label": "008f (removed)"},
    "baseline": {"logdir": LOGDIR_BASELINE, "color": "black", "ls": "-", "label": "Baseline"},
}

STEP_MAX = 105_000
NVE_WINDOW_START = 35_000
NVE_PATHOLOGICAL = 1.5


def load_metrics(logdir):
    path = os.path.join(logdir, "metrics.jsonl")
    eval_returns = {}
    value_means = {}
    with open(path) as f:
        for line in f:
            row = json.loads(line)
            step = int(row["step"])
            if "eval_return" in row:
                eval_returns[step] = float(row["eval_return"])
            if "value_mean" in row:
                value_means[step] = float(row["value_mean"])
    return eval_returns, value_means


def compute_ve_ratio(eval_returns, value_means):
    common = sorted(set(eval_returns) & set(value_means))
    steps, ratios = [], []
    for s in common:
        er = eval_returns[s]
        if abs(er) < 1e-8:
            continue
        steps.append(s)
        ratios.append(value_means[s] / er)
    return np.array(steps), np.array(ratios)


def compute_nve(steps, ratios, bl_steps, bl_ratios):
    bl_interp = np.interp(steps, bl_steps, bl_ratios)
    mask = bl_interp != 0
    nve = np.full_like(ratios, np.nan)
    nve[mask] = ratios[mask] / bl_interp[mask]
    return nve


def setup_style():
    plt.rcParams.update({
        "font.size": 13,
        "axes.labelsize": 14,
        "axes.titlesize": 15,
        "legend.fontsize": 11,
        "xtick.labelsize": 11,
        "ytick.labelsize": 11,
        "axes.spines.top": False,
        "axes.spines.right": False,
        "figure.dpi": 150,
        "savefig.bbox": "tight",
        "savefig.pad_inches": 0.1,
    })


def plot_eval_curves(data):
    fig, ax = plt.subplots(figsize=(8, 5))
    for key in ["baseline", "008d", "008f", "018"]:
        cfg = EXPERIMENTS[key]
        er = data[key]["eval_returns"]
        steps = sorted(s for s in er if s <= STEP_MAX)
        vals = [er[s] for s in steps]
        ax.plot(steps, vals, color=cfg["color"], ls=cfg["ls"], lw=2, label=cfg["label"])
    ax.set_xlabel("Training Steps")
    ax.set_ylabel("Eval Return")
    ax.set_title("Full-SGS (exp_018) vs Controls")
    ax.set_xlim(0, STEP_MAX)
    ax.legend(loc="best", frameon=False)
    out = os.path.join(OUTPUT_DIR, "fig_018_eval_curves.pdf")
    fig.savefig(out)
    plt.close(fig)
    print(f"Saved: {out}")


def plot_nve_trajectories(data):
    bl_steps, bl_ratios = data["baseline"]["ve_steps"], data["baseline"]["ve_ratios"]

    fig, ax = plt.subplots(figsize=(8, 5))
    for key in ["baseline", "008d", "008f", "018"]:
        cfg = EXPERIMENTS[key]
        steps = data[key]["ve_steps"]
        ratios = data[key]["ve_ratios"]
        nve = compute_nve(steps, ratios, bl_steps, bl_ratios)
        mask = steps >= NVE_WINDOW_START
        ax.plot(steps[mask], nve[mask], color=cfg["color"], ls=cfg["ls"], lw=2, label=cfg["label"])
        data[key]["nve_35k"] = nve[mask]
        data[key]["nve_steps_35k"] = steps[mask]

    ax.axhline(NVE_PATHOLOGICAL, color="red", ls=":", lw=1.2, label="Pathological threshold")
    ax.axhline(1.0, color="gray", ls=":", lw=1.0, label="Baseline reference")
    ax.set_xlabel("Training Steps")
    ax.set_ylabel("NVE")
    ax.set_title("NVE Trajectories — 018 vs Controls")
    ax.set_xlim(NVE_WINDOW_START, STEP_MAX)
    ax.legend(loc="best", frameon=False)
    out = os.path.join(OUTPUT_DIR, "fig_018_nve_trajectories.pdf")
    fig.savefig(out)
    plt.close(fig)
    print(f"Saved: {out}")


def print_verdict(data):
    print("\n" + "=" * 60)
    print("VERDICT SUMMARY — exp_018 Full-SGS")
    print("=" * 60)

    for key in ["018", "008d", "008f", "baseline"]:
        cfg = EXPERIMENTS[key]
        er = data[key]["eval_returns"]
        final_step = max(er.keys())
        final_eval = er[final_step]

        nve_35k = data[key].get("nve_35k")
        if nve_35k is not None and len(nve_35k) > 0:
            peak_nve = float(np.nanmax(nve_35k))
        else:
            peak_nve = float("nan")

        print(f"\n  {cfg['label']}:")
        print(f"    Final eval (step {final_step}): {final_eval:.1f}")
        print(f"    Peak NVE (35K+):  {peak_nve:.3f}")

    nve_018 = data["018"].get("nve_35k")
    if nve_018 is not None and len(nve_018) > 0:
        peak = float(np.nanmax(nve_018))
        print("\n" + "-" * 60)
        if peak > NVE_PATHOLOGICAL:
            print(f"  CIVO DETECTED — peak NVE = {peak:.3f} > {NVE_PATHOLOGICAL}")
            print("  Mechanism: Version B (representation-level)")
        else:
            print(f"  CIVO PREVENTED — peak NVE = {peak:.3f} <= {NVE_PATHOLOGICAL}")
            print("  Mechanism: Version A (gradient-level)")
    print("=" * 60)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--verdict", action="store_true", help="Print CIVO verdict summary")
    args = parser.parse_args()

    setup_style()
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    data = {}
    for key, cfg in EXPERIMENTS.items():
        logdir = cfg["logdir"]
        if not os.path.exists(os.path.join(logdir, "metrics.jsonl")):
            print(f"WARNING: metrics.jsonl not found for {key} at {logdir}", file=sys.stderr)
            sys.exit(1)
        er, vm = load_metrics(logdir)
        ve_steps, ve_ratios = compute_ve_ratio(er, vm)
        data[key] = {
            "eval_returns": er,
            "value_means": vm,
            "ve_steps": ve_steps,
            "ve_ratios": ve_ratios,
        }

    plot_eval_curves(data)
    plot_nve_trajectories(data)

    if args.verdict:
        print_verdict(data)


if __name__ == "__main__":
    main()
