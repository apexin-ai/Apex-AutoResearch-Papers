#!/usr/bin/env python3
"""Cartpole experiment analysis (exp_060/061/062): ve_ratio, NVE, CIVO detection.

Computes ve_ratio = value_mean / eval_return from metrics.jsonl, then
baseline-normalized NVE = ve_ratio(treatment) / ve_ratio(baseline).
CIVO is flagged when NVE > 1.5x at any evaluation step.

Input:
  --exp060  One or more logdir paths for exp_060_cartpole_baseline seeds
  --exp061  One or more logdir paths for exp_061_cartpole_civo_trigger seeds
  --exp062  One or more logdir paths for exp_062_cartpole_control seeds
  Each logdir must contain metrics.jsonl with fields:
    eval lines:  {step, eval_return, eval_length, eval_episodes}
    train lines: {step, value_mean, value_std, ...}

Output (in --output-dir):
  fig1_ve_ratio_timeline.{png,pdf}   ve_ratio over training steps
  fig2_nve_bar.{png,pdf}             NVE bar chart across experiments
  fig3_learning_curves.{png,pdf}     eval_return learning curves
  cartpole_results.json              numeric results

Dependencies: numpy, matplotlib (no torch needed — uses metrics.jsonl only)

Example:
  python cartpole_analysis.py \
    --exp060 logdir/exp_060_cartpole_baseline_s{0,1,2} \
    --exp061 logdir/exp_061_cartpole_civo_trigger_s{0,1,2} \
    --exp062 logdir/exp_062_cartpole_control_s{0,1,2} \
    --output-dir ./cartpole_analysis_output
"""

import argparse
import json
import os
import sys
from collections import defaultdict

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams.update({
    "font.family": "DejaVu Sans",
    "font.size": 11,
    "axes.titlesize": 13,
    "axes.labelsize": 12,
    "xtick.labelsize": 10,
    "ytick.labelsize": 10,
    "legend.fontsize": 9,
    "figure.dpi": 300,
    "savefig.dpi": 300,
    "savefig.bbox": "tight",
    "savefig.pad_inches": 0.05,
    "axes.spines.top": False,
    "axes.spines.right": False,
    "lines.linewidth": 1.8,
})

COLORS = {
    "exp060": "#2196F3",  # blue — baseline
    "exp061": "#D55E00",  # red-orange — CIVO trigger
    "exp062": "#4CAF50",  # green — control
}
LABELS = {
    "exp060": "Baseline (dt=1)",
    "exp061": "Trained dt_emb (CIVO trigger)",
    "exp062": "No dt_emb control",
}
NVE_THRESHOLD = 1.5


# ---------------------------------------------------------------------------
# Data loading
# ---------------------------------------------------------------------------

def load_metrics_jsonl(logdir):
    """Parse metrics.jsonl into {step: {field: value}} dicts by line type."""
    path = os.path.join(logdir, "metrics.jsonl")
    if not os.path.exists(path):
        print(f"WARNING: {path} not found", file=sys.stderr)
        return None

    eval_returns = {}
    value_means = {}
    train_returns = defaultdict(list)

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
            if "train_return" in d:
                train_returns[step].append(d["train_return"])

    train_return_mean = {s: np.mean(v) for s, v in train_returns.items()}
    return {
        "eval_return": eval_returns,
        "value_mean": value_means,
        "train_return": train_return_mean,
    }


def load_experiment(logdirs):
    """Load all seeds for one experiment. Returns list of per-seed dicts."""
    seeds = []
    for ld in logdirs:
        data = load_metrics_jsonl(ld)
        if data is None:
            print(f"SKIP: {ld}", file=sys.stderr)
            continue
        data["logdir"] = ld
        data["seed_name"] = os.path.basename(ld.rstrip("/"))
        seeds.append(data)
    return seeds


# ---------------------------------------------------------------------------
# Metric computation
# ---------------------------------------------------------------------------

def compute_ve_ratio_series(seed_data):
    """Compute ve_ratio = value_mean / eval_return at each eval step."""
    eval_ret = seed_data["eval_return"]
    val_mean = seed_data["value_mean"]
    common = sorted(set(eval_ret) & set(val_mean))
    steps, ratios = [], []
    for s in common:
        er = eval_ret[s]
        vm = val_mean[s]
        if er <= 0:
            continue
        steps.append(s)
        ratios.append(vm / er)
    return np.array(steps), np.array(ratios)


def compute_eval_return_series(seed_data):
    """Extract eval_return as (steps, values) arrays."""
    items = sorted(seed_data["eval_return"].items())
    if not items:
        return np.array([]), np.array([])
    steps, vals = zip(*items)
    return np.array(steps), np.array(vals)


def align_seeds_to_common_steps(all_steps_arrays, all_value_arrays):
    """Align multiple seeds to their common step set, return (steps, 2D array)."""
    if not all_steps_arrays:
        return np.array([]), np.array([]).reshape(0, 0)
    step_sets = [set(s.tolist()) for s in all_steps_arrays]
    common = sorted(set.intersection(*step_sets))
    if not common:
        return np.array([]), np.array([]).reshape(0, 0)
    common = np.array(common)
    matrix = np.zeros((len(all_steps_arrays), len(common)))
    for i, (steps, vals) in enumerate(zip(all_steps_arrays, all_value_arrays)):
        step_to_val = dict(zip(steps.tolist(), vals.tolist()))
        for j, s in enumerate(common):
            matrix[i, j] = step_to_val[s]
    return common, matrix


def compute_nve_per_seed(baseline_seeds, treatment_seeds):
    """Compute baseline-normalized NVE for each treatment seed.

    NVE(step) = ve_ratio_treatment(step) / ve_ratio_baseline_mean(step).
    Returns (steps, nve_matrix[n_treatment_seeds x n_steps]).
    """
    bl_steps_list, bl_ratio_list = [], []
    for sd in baseline_seeds:
        s, r = compute_ve_ratio_series(sd)
        if len(s) > 0:
            bl_steps_list.append(s)
            bl_ratio_list.append(r)

    if not bl_steps_list:
        return np.array([]), np.array([]).reshape(0, 0)

    bl_common, bl_matrix = align_seeds_to_common_steps(bl_steps_list, bl_ratio_list)
    if len(bl_common) == 0:
        return np.array([]), np.array([]).reshape(0, 0)
    bl_mean = bl_matrix.mean(axis=0)

    tr_steps_list, tr_ratio_list = [], []
    for sd in treatment_seeds:
        s, r = compute_ve_ratio_series(sd)
        if len(s) > 0:
            tr_steps_list.append(s)
            tr_ratio_list.append(r)

    if not tr_steps_list:
        return np.array([]), np.array([]).reshape(0, 0)

    bl_step_to_val = dict(zip(bl_common.tolist(), bl_mean.tolist()))

    nve_steps_list, nve_vals_list = [], []
    for s_arr, r_arr in zip(tr_steps_list, tr_ratio_list):
        steps_out, nve_out = [], []
        for s, r in zip(s_arr, r_arr):
            bv = bl_step_to_val.get(s)
            if bv is not None and bv > 1e-6:
                steps_out.append(s)
                nve_out.append(r / bv)
        if steps_out:
            nve_steps_list.append(np.array(steps_out))
            nve_vals_list.append(np.array(nve_out))

    if not nve_steps_list:
        return np.array([]), np.array([]).reshape(0, 0)

    return align_seeds_to_common_steps(nve_steps_list, nve_vals_list)


def compute_peak_nve(nve_steps, nve_matrix):
    """Peak NVE across training (per seed), return (mean, std, per_seed_peaks)."""
    if nve_matrix.size == 0:
        return float("nan"), float("nan"), []
    peaks = nve_matrix.max(axis=1)
    return float(np.mean(peaks)), float(np.std(peaks)), peaks.tolist()


def compute_final_nve(nve_steps, nve_matrix, window=5):
    """NVE averaged over last `window` eval steps (per seed)."""
    if nve_matrix.size == 0:
        return float("nan"), float("nan")
    tail = nve_matrix[:, -window:] if nve_matrix.shape[1] >= window else nve_matrix
    per_seed = tail.mean(axis=1)
    return float(np.mean(per_seed)), float(np.std(per_seed))


# ---------------------------------------------------------------------------
# Figures
# ---------------------------------------------------------------------------

def _mean_shade(ax, steps_k, matrix, color, label, alpha=0.15):
    """Plot mean line with ±1 std shading."""
    mean = matrix.mean(axis=0)
    std = matrix.std(axis=0)
    ax.plot(steps_k, mean, color=color, label=label)
    ax.fill_between(steps_k, mean - std, mean + std, color=color, alpha=alpha)


def fig1_ve_ratio_timeline(experiments, output_dir):
    """ve_ratio over training steps for all three experiments."""
    fig, ax = plt.subplots(figsize=(10, 5))

    for exp_key in ["exp060", "exp061", "exp062"]:
        seeds = experiments.get(exp_key, [])
        if not seeds:
            continue
        steps_list, ratio_list = [], []
        for sd in seeds:
            s, r = compute_ve_ratio_series(sd)
            if len(s) > 0:
                steps_list.append(s)
                ratio_list.append(r)
        if not steps_list:
            continue
        common, matrix = align_seeds_to_common_steps(steps_list, ratio_list)
        if len(common) == 0:
            continue
        _mean_shade(ax, common / 1000, matrix, COLORS[exp_key], LABELS[exp_key])

    ax.axhline(y=1.0, color="gray", linestyle="--", lw=1, alpha=0.5, label="Perfect (V/E=1)")
    ax.set_xlabel("Training Steps (K)")
    ax.set_ylabel("ve_ratio (value_mean / eval_return)")
    ax.set_title("Value / Episode Return Ratio — Cartpole Swingup")
    ax.legend(loc="upper left")
    ax.grid(True, alpha=0.3)

    for fmt in ["png", "pdf"]:
        fig.savefig(os.path.join(output_dir, f"fig1_ve_ratio_timeline.{fmt}"))
    plt.close(fig)
    print(f"  fig1_ve_ratio_timeline saved")


def fig2_nve_bar(experiments, output_dir):
    """NVE bar chart: peak and final NVE for treatment vs control."""
    baseline = experiments.get("exp060", [])
    if not baseline:
        print("  SKIP fig2: no baseline data", file=sys.stderr)
        return {}

    results = {}
    exp_keys = ["exp061", "exp062"]
    bar_labels = [LABELS[k] for k in exp_keys]
    bar_colors = [COLORS[k] for k in exp_keys]

    peak_means, peak_stds = [], []
    final_means, final_stds = [], []

    for ek in exp_keys:
        treatment = experiments.get(ek, [])
        if not treatment:
            peak_means.append(0)
            peak_stds.append(0)
            final_means.append(0)
            final_stds.append(0)
            results[ek] = {"peak_nve": "N/A", "final_nve": "N/A"}
            continue

        nve_steps, nve_matrix = compute_nve_per_seed(baseline, treatment)
        pm, ps, per_seed = compute_peak_nve(nve_steps, nve_matrix)
        fm, fs = compute_final_nve(nve_steps, nve_matrix)
        peak_means.append(pm)
        peak_stds.append(ps)
        final_means.append(fm)
        final_stds.append(fs)
        results[ek] = {
            "peak_nve_mean": pm, "peak_nve_std": ps,
            "final_nve_mean": fm, "final_nve_std": fs,
            "peak_nve_per_seed": per_seed,
            "civo_detected": pm > NVE_THRESHOLD,
            "n_seeds": nve_matrix.shape[0],
        }

    x = np.arange(len(exp_keys))
    width = 0.35
    fig, ax = plt.subplots(figsize=(7, 5))
    ax.bar(x - width / 2, peak_means, width, yerr=peak_stds,
           color=[COLORS[k] for k in exp_keys], alpha=0.8,
           label="Peak NVE", edgecolor="black", linewidth=0.5, capsize=4)
    ax.bar(x + width / 2, final_means, width, yerr=final_stds,
           color=[COLORS[k] for k in exp_keys], alpha=0.4,
           label="Final NVE (last 5 evals)", edgecolor="black",
           linewidth=0.5, capsize=4, hatch="//")

    ax.axhline(y=NVE_THRESHOLD, color="red", linestyle="--", lw=1.5,
               label=f"CIVO threshold ({NVE_THRESHOLD}x)")
    ax.axhline(y=1.0, color="gray", linestyle=":", lw=1, alpha=0.5)
    ax.set_xticks(x)
    ax.set_xticklabels(bar_labels, fontsize=10)
    ax.set_ylabel("Baseline-Normalized NVE")
    ax.set_title("NVE: CIVO Trigger vs Control — Cartpole Swingup")
    ax.legend()
    ax.grid(True, alpha=0.3, axis="y")

    for fmt in ["png", "pdf"]:
        fig.savefig(os.path.join(output_dir, f"fig2_nve_bar.{fmt}"))
    plt.close(fig)
    print(f"  fig2_nve_bar saved")
    return results


def fig3_learning_curves(experiments, output_dir):
    """Eval return learning curves for all three experiments."""
    fig, ax = plt.subplots(figsize=(10, 5))

    for exp_key in ["exp060", "exp061", "exp062"]:
        seeds = experiments.get(exp_key, [])
        if not seeds:
            continue
        steps_list, ret_list = [], []
        for sd in seeds:
            s, r = compute_eval_return_series(sd)
            if len(s) > 0:
                steps_list.append(s)
                ret_list.append(r)
        if not steps_list:
            continue
        common, matrix = align_seeds_to_common_steps(steps_list, ret_list)
        if len(common) == 0:
            continue
        _mean_shade(ax, common / 1000, matrix, COLORS[exp_key], LABELS[exp_key])

    ax.set_xlabel("Training Steps (K)")
    ax.set_ylabel("Eval Return")
    ax.set_title("Learning Curves — Cartpole Swingup")
    ax.legend(loc="lower right")
    ax.grid(True, alpha=0.3)

    for fmt in ["png", "pdf"]:
        fig.savefig(os.path.join(output_dir, f"fig3_learning_curves.{fmt}"))
    plt.close(fig)
    print(f"  fig3_learning_curves saved")


# ---------------------------------------------------------------------------
# Summary table
# ---------------------------------------------------------------------------

def print_summary(experiments, nve_results):
    print("\n" + "=" * 80)
    print("CARTPOLE ANALYSIS SUMMARY")
    print("=" * 80)

    for exp_key in ["exp060", "exp061", "exp062"]:
        seeds = experiments.get(exp_key, [])
        if not seeds:
            print(f"\n  [{LABELS[exp_key]}] — no data")
            continue
        print(f"\n  [{LABELS[exp_key]}]  ({len(seeds)} seeds)")

        final_returns = []
        for sd in seeds:
            er = sd["eval_return"]
            if er:
                last_step = max(er.keys())
                final_returns.append(er[last_step])
        if final_returns:
            print(f"    Final eval_return: {np.mean(final_returns):.1f} "
                  f"± {np.std(final_returns):.1f}")

        steps_list, ratio_list = [], []
        for sd in seeds:
            s, r = compute_ve_ratio_series(sd)
            if len(s) > 0:
                steps_list.append(s)
                ratio_list.append(r)
        if steps_list:
            common, matrix = align_seeds_to_common_steps(steps_list, ratio_list)
            if len(common) > 0:
                final_ve = matrix[:, -1]
                peak_ve = matrix.max(axis=1)
                print(f"    Final ve_ratio:   {np.mean(final_ve):.4f} "
                      f"± {np.std(final_ve):.4f}")
                print(f"    Peak ve_ratio:    {np.mean(peak_ve):.4f} "
                      f"± {np.std(peak_ve):.4f}")

        nr = nve_results.get(exp_key, {})
        if isinstance(nr, dict) and "peak_nve_mean" in nr:
            print(f"    Peak NVE:         {nr['peak_nve_mean']:.4f} "
                  f"± {nr['peak_nve_std']:.4f}")
            print(f"    Final NVE:        {nr['final_nve_mean']:.4f} "
                  f"± {nr['final_nve_std']:.4f}")
            civo = "YES" if nr["civo_detected"] else "NO"
            print(f"    CIVO detected:    {civo} "
                  f"(threshold={NVE_THRESHOLD}x)")

    print("\n" + "=" * 80)
    print("CIVO DETECTION TABLE")
    print("=" * 80)
    print(f"  {'Experiment':<35s} {'NVE (peak)':>12s} {'CIVO':>6s} {'Seeds':>6s}")
    print(f"  {'-' * 35} {'-' * 12} {'-' * 6} {'-' * 6}")
    for exp_key, label in [("exp061", "CIVO trigger"), ("exp062", "Control")]:
        nr = nve_results.get(exp_key, {})
        if isinstance(nr, dict) and "peak_nve_mean" in nr:
            nve_str = f"{nr['peak_nve_mean']:.3f}±{nr['peak_nve_std']:.3f}"
            civo_str = "YES" if nr["civo_detected"] else "NO"
            n_str = str(nr["n_seeds"])
        else:
            nve_str = "N/A"
            civo_str = "N/A"
            n_str = "0"
        print(f"  {label:<35s} {nve_str:>12s} {civo_str:>6s} {n_str:>6s}")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(
        description="Cartpole experiment analysis (exp_060/061/062)")
    parser.add_argument("--exp060", nargs="+", default=[],
                        help="Logdir paths for exp_060 baseline seeds")
    parser.add_argument("--exp061", nargs="+", default=[],
                        help="Logdir paths for exp_061 CIVO trigger seeds")
    parser.add_argument("--exp062", nargs="+", default=[],
                        help="Logdir paths for exp_062 control seeds")
    parser.add_argument("--logdir-base", default=None,
                        help="Auto-discover exp_06{0,1,2}_* under this directory")
    parser.add_argument("--output-dir", default="./cartpole_analysis_output",
                        help="Output directory for figures and results")
    parser.add_argument("--threshold", type=float, default=NVE_THRESHOLD,
                        help="CIVO detection threshold (default: 1.5)")
    args = parser.parse_args()

    global NVE_THRESHOLD
    NVE_THRESHOLD = args.threshold

    if args.logdir_base:
        for entry in sorted(os.listdir(args.logdir_base)):
            full = os.path.join(args.logdir_base, entry)
            if not os.path.isdir(full):
                continue
            if entry.startswith("exp_060_cartpole"):
                args.exp060.append(full)
            elif entry.startswith("exp_061_cartpole"):
                args.exp061.append(full)
            elif entry.startswith("exp_062_cartpole"):
                args.exp062.append(full)

    if not any([args.exp060, args.exp061, args.exp062]):
        print("ERROR: provide --exp060/--exp061/--exp062 or --logdir-base",
              file=sys.stderr)
        sys.exit(1)

    print("Loading experiments...")
    experiments = {
        "exp060": load_experiment(args.exp060),
        "exp061": load_experiment(args.exp061),
        "exp062": load_experiment(args.exp062),
    }
    for k, v in experiments.items():
        print(f"  {k}: {len(v)} seeds loaded")

    os.makedirs(args.output_dir, exist_ok=True)

    print("\nGenerating figures...")
    fig1_ve_ratio_timeline(experiments, args.output_dir)
    nve_results = fig2_nve_bar(experiments, args.output_dir)
    fig3_learning_curves(experiments, args.output_dir)

    print_summary(experiments, nve_results)

    json_out = {
        "experiment": "cartpole_060_061_062",
        "threshold": NVE_THRESHOLD,
        "experiments": {},
    }
    for exp_key in ["exp060", "exp061", "exp062"]:
        seeds = experiments[exp_key]
        seed_info = []
        for sd in seeds:
            s, r = compute_ve_ratio_series(sd)
            er_s, er_v = compute_eval_return_series(sd)
            seed_info.append({
                "seed_name": sd["seed_name"],
                "n_eval_steps": len(er_s),
                "final_eval_return": float(er_v[-1]) if len(er_v) > 0 else None,
                "final_ve_ratio": float(r[-1]) if len(r) > 0 else None,
                "peak_ve_ratio": float(r.max()) if len(r) > 0 else None,
                "ve_ratio_trajectory": [
                    {"step": int(st), "ve_ratio": round(float(v), 6)}
                    for st, v in zip(s, r)
                ] if len(s) > 0 else [],
                "eval_return_trajectory": [
                    {"step": int(st), "eval_return": round(float(v), 4)}
                    for st, v in zip(er_s, er_v)
                ] if len(er_s) > 0 else [],
            })
        exp_entry = {
            "label": LABELS[exp_key],
            "n_seeds": len(seeds),
            "seeds": seed_info,
        }
        nr = nve_results.get(exp_key, {})
        if isinstance(nr, dict) and "peak_nve_mean" in nr:
            exp_entry["nve"] = {
                "peak_mean": nr["peak_nve_mean"],
                "peak_std": nr["peak_nve_std"],
                "final_mean": nr["final_nve_mean"],
                "final_std": nr["final_nve_std"],
                "civo_detected": nr["civo_detected"],
            }
        json_out["experiments"][exp_key] = exp_entry

    out_path = os.path.join(args.output_dir, "cartpole_results.json")
    with open(out_path, "w") as f:
        json.dump(json_out, f, indent=2)
    print(f"\nResults JSON saved to {out_path}")


if __name__ == "__main__":
    main()
