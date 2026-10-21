"""exp-005: Contamination Magnitude Calibration.

Compares real-data fitted c_n (from exp-003/003b) against MVP synthetic DGP c_n
to determine whether real contamination is weak (~mvp_001, sigma=0.5) or strong
(~mvp_002/003, sigma=1.5), and whether it is large enough to affect rankings.

Usage:
  python run_exp005.py --exp003-dir /root/gated_mfrm_judge_bias/exp003/results \
                       --exp004-results /root/gated_mfrm_judge_bias/exp004/results/results.json \
                       --output-dir /root/gated_mfrm_judge_bias/exp005/results

  python run_exp005.py --help

Dependencies: numpy, scipy, pandas, matplotlib, json
"""

import argparse
import json
import sys
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats


# --- MVP DGP parameters (from mvp/data_gen.py and mvp/run_mvp_002.py) ---
MVP_DGP = {
    "mvp_001": {
        "label": "MVP-001 (weak)",
        "c_distribution": "HalfNormal",
        "sigma": 0.5,
        "N": 20,
        "description": "c ~ |N(0, 0.5)|",
    },
    "mvp_002": {
        "label": "MVP-002 (strong)",
        "c_distribution": "HalfNormal",
        "sigma": 1.5,
        "N": 50,
        "description": "c ~ |N(0, 1.5)|",
    },
    "mvp_003": {
        "label": "MVP-003 (strong, tuned MCMC)",
        "c_distribution": "HalfNormal",
        "sigma": 1.5,
        "N": 50,
        "description": "c ~ |N(0, 1.5)|, same DGP as MVP-002",
    },
}


def load_real_cn(exp003_dir: str) -> dict:
    """Load per-model c_n from exp-003 results (joint_gmfrm and sequential)."""
    d = Path(exp003_dir)

    result = {}

    joint_path = d / "joint_gmfrm_c.npy"
    if joint_path.exists():
        result["joint_gmfrm"] = np.load(joint_path)
    else:
        print(f"  WARNING: {joint_path} not found")

    seq_path = d / "sequential_c.npy"
    if seq_path.exists():
        result["sequential"] = np.load(seq_path)
    else:
        print(f"  WARNING: {seq_path} not found")

    # Also load model names from results.json for labeling
    rj = d / "results.json"
    if rj.exists():
        with open(rj) as f:
            rdata = json.load(f)
        if "arena_correlation" in rdata and "joint_gmfrm" in rdata["arena_correlation"]:
            result["model_names"] = rdata["arena_correlation"]["joint_gmfrm"]["matched_models"]

    return result


def load_exp003b_cn(exp003b_dir: str) -> dict:
    """Load per-model c_n from exp-003b if available."""
    d = Path(exp003b_dir)
    if not d.exists():
        return {}

    result = {}
    for fname in ["joint_gmfrm_c.npy", "sequential_c.npy"]:
        fpath = d / fname
        if fpath.exists():
            key = fname.replace("_c.npy", "") + "_003b"
            result[key] = np.load(fpath)

    return result


def sample_halfnormal(sigma: float, n_samples: int = 10000, seed: int = 42) -> np.ndarray:
    """Generate samples from HalfNormal(sigma) for comparison."""
    rng = np.random.default_rng(seed)
    return np.abs(rng.normal(0, sigma, size=n_samples))


def compute_scale_comparison(real_cn: dict) -> dict:
    """Compare real c_n statistics against MVP DGP theoretical values."""
    results = {}

    for method, cn in real_cn.items():
        if method == "model_names":
            continue
        cn = np.asarray(cn)
        results[method] = {
            "n": len(cn),
            "mean": float(cn.mean()),
            "std": float(cn.std()),
            "median": float(np.median(cn)),
            "min": float(cn.min()),
            "max": float(cn.max()),
            "q25": float(np.percentile(cn, 25)),
            "q75": float(np.percentile(cn, 75)),
        }

    # Theoretical HalfNormal moments for comparison
    for key, dgp in MVP_DGP.items():
        sigma = dgp["sigma"]
        hn_mean = sigma * np.sqrt(2 / np.pi)
        hn_std = sigma * np.sqrt(1 - 2 / np.pi)
        results[f"{key}_theoretical"] = {
            "sigma": sigma,
            "mean": float(hn_mean),
            "std": float(hn_std),
            "median": float(sigma * 0.6745),  # median of HalfNormal
        }

    return results


def classify_contamination_regime(real_cn: dict) -> dict:
    """Determine which MVP regime real c_n is closest to."""
    classification = {}

    for method, cn in real_cn.items():
        if method == "model_names":
            continue
        cn = np.asarray(cn)
        real_mean = cn.mean()

        # Compare to each MVP regime
        distances = {}
        for key, dgp in MVP_DGP.items():
            sigma = dgp["sigma"]
            expected_mean = sigma * np.sqrt(2 / np.pi)
            distances[key] = abs(real_mean - expected_mean)

        closest = min(distances, key=distances.get)

        # KS test against HalfNormal distributions
        ks_results = {}
        for key, dgp in MVP_DGP.items():
            sigma = dgp["sigma"]
            synth = sample_halfnormal(sigma, n_samples=10000)
            stat, p = stats.ks_2samp(cn, synth)
            ks_results[key] = {"statistic": float(stat), "p_value": float(p)}

        # Ratio to MVP thresholds
        weak_mean = MVP_DGP["mvp_001"]["sigma"] * np.sqrt(2 / np.pi)
        strong_mean = MVP_DGP["mvp_002"]["sigma"] * np.sqrt(2 / np.pi)

        classification[method] = {
            "real_mean": float(real_mean),
            "closest_regime": closest,
            "distances_to_regime_means": {k: float(v) for k, v in distances.items()},
            "ks_tests": ks_results,
            "ratio_to_weak": float(real_mean / weak_mean) if weak_mean > 0 else None,
            "ratio_to_strong": float(real_mean / strong_mean) if strong_mean > 0 else None,
        }

    return classification


def analyze_ranking_impact(real_cn: dict, exp004_path: str) -> dict:
    """Combine c_n magnitude with exp-004 ranking results."""
    analysis = {}

    if not Path(exp004_path).exists():
        analysis["warning"] = f"{exp004_path} not found, skipping ranking impact analysis"
        return analysis

    with open(exp004_path) as f:
        exp004 = json.load(f)

    # Extract tau values from exp-004
    exp003_cmp = exp004.get("exp003_comparison", {})
    baselines = exp004.get("baselines", {})

    analysis["exp003_taus"] = {
        method: data.get("kendall_tau")
        for method, data in exp003_cmp.items()
    }
    analysis["baseline_taus"] = {
        method: data.get("arena_correlation", {}).get("kendall_tau")
        for method, data in baselines.items()
    }

    # Compute the tau improvement from joint_gmfrm
    joint_tau = exp003_cmp.get("joint_gmfrm", {}).get("kendall_tau")
    raw_tau = exp003_cmp.get("raw_average", {}).get("kendall_tau")

    if joint_tau and raw_tau:
        analysis["tau_improvement_joint_vs_raw"] = float(joint_tau - raw_tau)
        analysis["tau_relative_improvement"] = float((joint_tau - raw_tau) / raw_tau * 100)

    # Is contamination strong enough to matter?
    for method, cn in real_cn.items():
        if method == "model_names":
            continue
        cn = np.asarray(cn)
        analysis[f"{method}_magnitude_assessment"] = {
            "mean_cn": float(cn.mean()),
            "max_cn": float(cn.max()),
            "n_models_with_cn_gt_0.5": int((cn > 0.5).sum()),
            "n_models_with_cn_gt_1.0": int((cn > 1.0).sum()),
            "strong_enough_for_ranking": bool(cn.max() > 0.3),
        }

    return analysis


def plot_cn_distributions(real_cn: dict, output_dir: Path):
    """Plot c_n distribution comparison: real vs MVP regimes."""
    fig, axes = plt.subplots(1, 2, figsize=(14, 5))

    colors = {
        "joint_gmfrm": "#2196F3",
        "sequential": "#4CAF50",
        "mvp_001": "#FF9800",
        "mvp_002": "#F44336",
        "mvp_003": "#9C27B0",
    }

    # --- Panel A: Histogram/KDE comparison ---
    ax = axes[0]
    x_range = np.linspace(0, 4.0, 200)

    for method, cn in real_cn.items():
        if method == "model_names":
            continue
        cn = np.asarray(cn)
        label = f"Real ({method}, N={len(cn)})"
        ax.hist(cn, bins=max(5, len(cn) // 2), density=True, alpha=0.4,
                color=colors.get(method, "gray"), label=label, edgecolor="white")

    for key, dgp in MVP_DGP.items():
        if key == "mvp_003":
            continue  # same DGP as mvp_002
        sigma = dgp["sigma"]
        pdf = 2 * stats.norm.pdf(x_range, 0, sigma)
        pdf[x_range < 0] = 0
        ax.plot(x_range, pdf, "--", color=colors.get(key, "gray"),
                label=f'{dgp["label"]} (σ={sigma})', linewidth=2)

    ax.set_xlabel("Contamination susceptibility $c_n$", fontsize=12)
    ax.set_ylabel("Density", fontsize=12)
    ax.set_title("(a) $c_n$ distribution: Real data vs MVP DGP", fontsize=13)
    ax.legend(fontsize=9, loc="upper right")
    ax.set_xlim(0, 4.0)

    # --- Panel B: Per-model c_n bar chart ---
    ax = axes[1]
    model_names = real_cn.get("model_names", None)

    bar_data = {}
    for method, cn in real_cn.items():
        if method == "model_names":
            continue
        bar_data[method] = np.asarray(cn)

    if bar_data:
        n_methods = len(bar_data)
        n_models = len(list(bar_data.values())[0])
        x = np.arange(n_models)
        width = 0.8 / n_methods

        for i, (method, cn) in enumerate(bar_data.items()):
            labels = model_names if model_names else [f"M{j}" for j in range(n_models)]
            ax.bar(x + i * width - 0.4 + width / 2, cn, width,
                   label=method, color=colors.get(method, "gray"), alpha=0.8)

        if model_names:
            ax.set_xticks(x)
            ax.set_xticklabels(model_names, rotation=45, ha="right", fontsize=8)

        # Reference lines for MVP DGP means
        for key, dgp in MVP_DGP.items():
            if key == "mvp_003":
                continue
            sigma = dgp["sigma"]
            hn_mean = sigma * np.sqrt(2 / np.pi)
            ax.axhline(hn_mean, color=colors.get(key, "gray"), linestyle="--",
                       alpha=0.6, label=f'{dgp["label"]} mean')

    ax.set_ylabel("$c_n$", fontsize=12)
    ax.set_title("(b) Per-model contamination susceptibility", fontsize=13)
    ax.legend(fontsize=8, loc="upper right")

    plt.tight_layout()
    fig.savefig(output_dir / "calibration_comparison.png", dpi=150, bbox_inches="tight")
    fig.savefig(output_dir / "calibration_comparison.pdf", bbox_inches="tight")
    plt.close(fig)
    print(f"  Saved calibration_comparison.{{png,pdf}}")


def plot_ranking_impact(analysis: dict, output_dir: Path):
    """Plot ranking correlation comparison across methods."""
    exp003_taus = analysis.get("exp003_taus", {})
    baseline_taus = analysis.get("baseline_taus", {})

    if not exp003_taus and not baseline_taus:
        print("  Skipping ranking impact plot (no data)")
        return

    all_methods = {}
    for m, t in baseline_taus.items():
        if t is not None:
            all_methods[m] = t
    for m, t in exp003_taus.items():
        if t is not None:
            all_methods[f"exp003_{m}"] = t

    if not all_methods:
        return

    fig, ax = plt.subplots(figsize=(10, 5))
    names = list(all_methods.keys())
    taus = list(all_methods.values())

    colors_bar = ["#FF9800" if "exp003" not in n else "#2196F3" for n in names]
    bars = ax.barh(range(len(names)), taus, color=colors_bar, alpha=0.8, edgecolor="white")
    ax.set_yticks(range(len(names)))
    ax.set_yticklabels(names, fontsize=9)
    ax.set_xlabel("Kendall τ vs Arena", fontsize=12)
    ax.set_title("Ranking correlation: Baselines vs G-MFRM methods", fontsize=13)
    ax.set_xlim(0.5, 1.0)

    for bar, tau in zip(bars, taus):
        ax.text(bar.get_width() + 0.005, bar.get_y() + bar.get_height() / 2,
                f"{tau:.4f}", va="center", fontsize=9)

    plt.tight_layout()
    fig.savefig(output_dir / "ranking_impact.png", dpi=150, bbox_inches="tight")
    plt.close(fig)
    print(f"  Saved ranking_impact.png")


def main():
    parser = argparse.ArgumentParser(
        description="exp-005: Contamination Magnitude Calibration",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""Examples:
  python run_exp005.py  # use default paths
  python run_exp005.py --exp003-dir /path/to/exp003/results
  python run_exp005.py --dry-run  # validate imports and data loading only""",
    )
    parser.add_argument("--exp003-dir", default="/root/gated_mfrm_judge_bias/exp003/results")
    parser.add_argument("--exp003b-dir", default="/root/gated_mfrm_judge_bias/exp003/output_003b")
    parser.add_argument("--exp004-results", default="/root/gated_mfrm_judge_bias/exp004/results/results.json")
    parser.add_argument("--output-dir", default="/root/gated_mfrm_judge_bias/exp005/results")
    parser.add_argument("--dry-run", action="store_true", help="Only validate imports and data paths")
    args = parser.parse_args()

    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    # Step 1: Load real c_n
    print("=" * 60)
    print("exp-005: Contamination Magnitude Calibration")
    print("=" * 60)

    print("\n[1/5] Loading real c_n from exp-003...")
    real_cn = load_real_cn(args.exp003_dir)
    for method, cn in real_cn.items():
        if method == "model_names":
            print(f"  Models: {cn}")
        else:
            cn = np.asarray(cn)
            print(f"  {method}: shape={cn.shape}, mean={cn.mean():.4f}, std={cn.std():.4f}, "
                  f"range=[{cn.min():.4f}, {cn.max():.4f}]")

    # Step 1b: Load exp-003b if available
    print("\n  Loading exp-003b c_n...")
    cn_003b = load_exp003b_cn(args.exp003b_dir)
    if cn_003b:
        for method, cn in cn_003b.items():
            cn = np.asarray(cn)
            print(f"  {method}: shape={cn.shape}, mean={cn.mean():.4f}, std={cn.std():.4f}")
            real_cn[method] = cn
    else:
        print("  exp-003b data not available yet")

    if args.dry_run:
        print("\n[DRY RUN] Import and data loading OK. Exiting.")
        return

    # Step 2: Scale comparison
    print("\n[2/5] Computing scale comparison...")
    scale_cmp = compute_scale_comparison(real_cn)
    for key, stats_dict in scale_cmp.items():
        print(f"  {key}: {stats_dict}")

    # Step 3: Regime classification
    print("\n[3/5] Classifying contamination regime...")
    classification = classify_contamination_regime(real_cn)
    for method, cls in classification.items():
        print(f"\n  {method}:")
        print(f"    Real mean c_n = {cls['real_mean']:.4f}")
        print(f"    Closest regime: {cls['closest_regime']}")
        print(f"    Ratio to weak (mvp_001): {cls['ratio_to_weak']:.2f}x")
        print(f"    Ratio to strong (mvp_002): {cls['ratio_to_strong']:.2f}x")
        for regime, ks in cls["ks_tests"].items():
            print(f"    KS vs {regime}: D={ks['statistic']:.4f}, p={ks['p_value']:.4f}")

    # Step 4: Ranking impact analysis
    print("\n[4/5] Analyzing ranking impact...")
    ranking_analysis = analyze_ranking_impact(real_cn, args.exp004_results)
    if "warning" in ranking_analysis:
        print(f"  {ranking_analysis['warning']}")
    else:
        if "tau_improvement_joint_vs_raw" in ranking_analysis:
            print(f"  τ improvement (joint vs raw): "
                  f"{ranking_analysis['tau_improvement_joint_vs_raw']:+.4f} "
                  f"({ranking_analysis['tau_relative_improvement']:+.1f}%)")
        for key, val in ranking_analysis.items():
            if key.endswith("_magnitude_assessment"):
                method = key.replace("_magnitude_assessment", "")
                print(f"  {method}: mean_cn={val['mean_cn']:.4f}, max_cn={val['max_cn']:.4f}, "
                      f"strong_enough={val['strong_enough_for_ranking']}")

    # Step 5: Generate plots
    print("\n[5/5] Generating plots...")
    plot_cn_distributions(real_cn, output_dir)
    plot_ranking_impact(ranking_analysis, output_dir)

    # Save full results
    full_results = {
        "scale_comparison": scale_cmp,
        "regime_classification": classification,
        "ranking_impact": ranking_analysis,
        "mvp_dgp_reference": {k: {kk: vv for kk, vv in v.items() if kk != "N"}
                              for k, v in MVP_DGP.items()},
    }
    results_path = output_dir / "results.json"
    with open(results_path, "w") as f:
        json.dump(full_results, f, indent=2, default=str)
    print(f"\n  Saved results to {results_path}")

    # Summary
    print("\n" + "=" * 60)
    print("SUMMARY")
    print("=" * 60)
    for method, cls in classification.items():
        regime = cls["closest_regime"]
        regime_label = MVP_DGP[regime]["label"]
        print(f"  {method}: real c_n ≈ {regime_label} "
              f"(mean={cls['real_mean']:.4f}, "
              f"weak_ratio={cls['ratio_to_weak']:.2f}x, "
              f"strong_ratio={cls['ratio_to_strong']:.2f}x)")


if __name__ == "__main__":
    main()
