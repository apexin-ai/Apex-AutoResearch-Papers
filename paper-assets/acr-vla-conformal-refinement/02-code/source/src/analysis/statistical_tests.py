"""
Statistical analysis and visualization for ACR-VLA Object Benchmark.

Functions:
  fisher_test         — One-sided Fisher exact test (H1: method A > method B)
  bootstrap_ci        — Bootstrap confidence interval for mean success rate
  plot_magnitude_curve — Magnitude sensitivity curve (obs_only vs perdof)
  comparison_table    — Formatted benchmark table with pairwise Fisher tests

Inputs:  per-task success rates (%), (successes, total) counts
Outputs: p-values, CIs to stdout; magnitude curve to PDF/PNG
"""

import os
from typing import Dict, List, Optional, Tuple

import numpy as np
from scipy import stats
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt


def fisher_test(
    a_success: int, a_total: int,
    b_success: int, b_total: int,
) -> float:
    """One-sided Fisher exact test. H1: method A has higher success rate than B.

    Args:
        a_success, a_total: successes and total trials for method A
        b_success, b_total: successes and total trials for method B

    Returns:
        One-sided p-value (P[observed or more extreme | H0: equal rates])
    """
    table = np.array([
        [a_success, a_total - a_success],
        [b_success, b_total - b_success],
    ])
    _, p_two = stats.fisher_exact(table, alternative="greater")
    return p_two


def bootstrap_ci(
    per_task_sr: List[float],
    n_bootstrap: int = 10000,
    ci: float = 0.95,
    seed: int = 0,
) -> Tuple[float, float, float]:
    """Bootstrap CI for mean success rate across tasks.

    Uses percentile method. Resamples tasks (preserves inter-task variance).

    Args:
        per_task_sr: list of per-task success rates (0-100 scale)
        n_bootstrap: number of resamples
        ci: confidence level
        seed: random seed

    Returns:
        (mean, ci_low, ci_high)
    """
    rng = np.random.RandomState(seed)
    arr = np.array(per_task_sr, dtype=float)
    n = len(arr)
    means = np.empty(n_bootstrap)
    for i in range(n_bootstrap):
        idx = rng.randint(0, n, size=n)
        means[i] = arr[idx].mean()
    alpha = 1 - ci
    lo = np.percentile(means, 100 * alpha / 2)
    hi = np.percentile(means, 100 * (1 - alpha / 2))
    return float(arr.mean()), float(lo), float(hi)


def plot_magnitude_curve(
    sweep: Dict[float, Dict[str, Optional[float]]],
    baseline_sr: float = 34.0,
    save_dir: str = ".",
    filename: str = "magnitude_curve_draft",
) -> str:
    """Plot magnitude sensitivity curve: obs_only vs perdof across norms.

    Args:
        sweep: {norm: {"obs_only": SR_or_None, "perdof": SR_or_None}}
        baseline_sr: argmin baseline SR (horizontal line)
        save_dir: output directory
        filename: output filename (without extension)

    Returns:
        Path to saved PNG
    """
    norms = sorted(sweep.keys())

    obs_norms, obs_sr = [], []
    per_norms, per_sr = [], []
    for n in norms:
        v = sweep[n]
        if v.get("obs_only") is not None:
            obs_norms.append(n)
            obs_sr.append(v["obs_only"])
        if v.get("perdof") is not None:
            per_norms.append(n)
            per_sr.append(v["perdof"])

    fig, ax = plt.subplots(figsize=(6, 4))

    ax.plot(obs_norms, obs_sr, "o-", color="#1f77b4", linewidth=2,
            markersize=7, label="obs_only CRM", zorder=3)
    ax.plot(per_norms, per_sr, "s--", color="#d62728", linewidth=2,
            markersize=7, label="perdof CRM", zorder=3)
    ax.axhline(baseline_sr, color="gray", linestyle=":", linewidth=1.5,
               label=f"argmin baseline ({baseline_sr:.0f}%)", zorder=2)

    offset = 1.5
    for x, y in zip(obs_norms, obs_sr):
        ax.annotate(f"{y:.1f}", (x, y), textcoords="offset points",
                    xytext=(0, 8), ha="center", fontsize=9, color="#1f77b4")
    for x, y in zip(per_norms, per_sr):
        ax.annotate(f"{y:.1f}", (x, y), textcoords="offset points",
                    xytext=(0, -12), ha="center", fontsize=9, color="#d62728")

    # Catastrophic failure point: unbounded CRM
    ax.plot(1.42, 0, "X", color="black", markersize=12, zorder=4)
    ax.annotate("catastrophic\nfailure", (1.42, 0), textcoords="offset points",
                xytext=(0, 14), ha="center", fontsize=8, color="black",
                fontstyle="italic")

    ax.set_xscale("log")
    ax.set_xlabel(r"Correction magnitude ($\varepsilon$)", fontsize=12)
    ax.set_ylabel("Success Rate (%)", fontsize=12)
    ax.set_title("Magnitude Sensitivity: obs_only vs perdof CRM", fontsize=13)
    ax.legend(fontsize=10, loc="best")
    ax.tick_params(labelsize=11)
    ax.set_ylim(0, max(max(obs_sr, default=0), max(per_sr, default=0)) + 15)
    ax.grid(True, alpha=0.3)

    fig.tight_layout()

    os.makedirs(save_dir, exist_ok=True)
    png_path = os.path.join(save_dir, f"{filename}.png")
    pdf_path = os.path.join(save_dir, f"{filename}.pdf")
    fig.savefig(png_path, dpi=300, bbox_inches="tight")
    fig.savefig(pdf_path, bbox_inches="tight")
    plt.close(fig)
    return png_path


def comparison_table(
    methods: Dict[str, Dict[str, float]],
    reference: str = "argmin",
    trials_per_task: int = 10,
) -> None:
    """Print formatted comparison table with Fisher test p-values vs reference.

    Args:
        methods: {method_name: {task_name: SR_percent}}
        reference: baseline method name for pairwise tests
        trials_per_task: number of rollouts per task (to convert SR% -> counts)
    """
    all_tasks = set()
    for v in methods.values():
        all_tasks.update(v.keys())
    all_tasks = sorted(all_tasks)

    def aggregate(task_dict):
        tasks_present = [t for t in all_tasks if t in task_dict]
        n_tasks = len(tasks_present)
        total_success = sum(round(task_dict[t] / 100 * trials_per_task) for t in tasks_present)
        total_trials = n_tasks * trials_per_task
        rates = [task_dict[t] for t in tasks_present]
        mean_sr = np.mean(rates) if rates else 0
        return total_success, total_trials, mean_sr, n_tasks

    ref_succ, ref_total, ref_sr, ref_n = aggregate(methods[reference])

    print(f"\n{'='*72}")
    print(f"  Object Benchmark Comparison (reference: {reference})")
    print(f"{'='*72}")
    print(f"  {'Method':<20} {'Tasks':>5} {'Mean SR':>8} {'Succ/Total':>12} {'p-value':>10}")
    print(f"  {'-'*20} {'-'*5} {'-'*8} {'-'*12} {'-'*10}")

    for name in sorted(methods.keys()):
        succ, total, sr, n = aggregate(methods[name])
        if name == reference:
            p_str = "   (ref)"
        else:
            p = fisher_test(succ, total, ref_succ, ref_total)
            p_str = f"   {p:.4f}"
            if p < 0.05:
                p_str += " *"
            if p < 0.01:
                p_str = p_str.rstrip(" *") + " **"
        print(f"  {name:<20} {n:>5} {sr:>7.1f}% {succ:>5}/{total:<5} {p_str}")

    print(f"{'='*72}\n")


if __name__ == "__main__":
    import argparse
    import json

    parser = argparse.ArgumentParser(
        description="Statistical tests for ACR-VLA Object Benchmark. "
        "Reads per-task SR data from JSON files (stat_analysis.py output)."
    )
    parser.add_argument(
        "--comparison-json", required=True,
        help="Path to comparison.json from stat_analysis.py (contains comparison_table with per-method per-seed results)",
    )
    parser.add_argument(
        "--method-a", default="obs_only",
        help="Method A for Fisher test (default: obs_only)",
    )
    parser.add_argument(
        "--method-b", default="argmin",
        help="Method B / reference for Fisher test (default: argmin)",
    )
    parser.add_argument(
        "--trials-per-task", type=int, default=10,
        help="Rollouts per task (default: 10)",
    )
    parser.add_argument(
        "--magnitude-json", default=None,
        help="Path to magnitude_sweep_summary.json for magnitude curve plot",
    )
    parser.add_argument(
        "--output-dir", default="artifacts",
        help="Output directory for figures (default: artifacts)",
    )
    args = parser.parse_args()

    with open(args.comparison_json) as f:
        comp_data = json.load(f)

    comp = comp_data.get("comparison_table", comp_data)
    methods = {}
    for method_name, seeds in comp.items():
        merged_tasks = {}
        for seed, seed_data in seeds.items():
            for task, info in seed_data.get("per_task", {}).items():
                if task not in merged_tasks:
                    merged_tasks[task] = {"successes": 0, "total": 0}
                merged_tasks[task]["successes"] += info["successes"]
                merged_tasks[task]["total"] += info["total"]
        methods[method_name] = {
            t: (v["successes"] / v["total"] * 100) if v["total"] > 0 else 0
            for t, v in merged_tasks.items()
        }

    if args.method_a in methods and args.method_b in methods:
        all_tasks = sorted(set().union(*methods.values()))
        a_succ = sum(round(methods[args.method_a].get(t, 0) / 100 * args.trials_per_task) for t in all_tasks if t in methods[args.method_a])
        a_total = sum(args.trials_per_task for t in all_tasks if t in methods[args.method_a])
        b_succ = sum(round(methods[args.method_b].get(t, 0) / 100 * args.trials_per_task) for t in all_tasks if t in methods[args.method_b])
        b_total = sum(args.trials_per_task for t in all_tasks if t in methods[args.method_b])

        p = fisher_test(a_succ, a_total, b_succ, b_total)
        print(f"Fisher test: {args.method_a} ({a_succ}/{a_total}) vs {args.method_b} ({b_succ}/{b_total}): p = {p:.4f}")

    for name in sorted(methods.keys()):
        rates = list(methods[name].values())
        if rates:
            mean, lo, hi = bootstrap_ci(rates, n_bootstrap=10000)
            print(f"  {name:<20}: mean={mean:.1f}%  95% CI=[{lo:.1f}, {hi:.1f}]")

    comparison_table(methods, reference=args.method_b, trials_per_task=args.trials_per_task)

    if args.magnitude_json:
        with open(args.magnitude_json) as f:
            mag_data = json.load(f)
        sweep = {}
        for norm_str, info in mag_data.get("obs_only", {}).items():
            n = float(norm_str)
            sweep.setdefault(n, {})["obs_only"] = info["sr"] * 100
        for norm_str, info in mag_data.get("perdof", {}).items():
            n = float(norm_str)
            sweep.setdefault(n, {})["perdof"] = info["sr"] * 100
        baseline = mag_data.get("baselines", {}).get("argmin", 0.34) * 100
        png = plot_magnitude_curve(sweep, baseline_sr=baseline, save_dir=args.output_dir)
        print(f"  Magnitude curve saved: {png}")
