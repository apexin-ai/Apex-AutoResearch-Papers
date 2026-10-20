#!/usr/bin/env python3
"""Compute LP range CDF and within-instance LP-F1 correlation.

For reviewer C3 rebuttal: provides epsilon-free evidence that most instances
have tightly clustered log-probabilities across N=8 samples.
"""

import json
import sys
import os
import numpy as np
from scipy.stats import spearmanr, pointbiserialr

sys.path.insert(0, '/root/autodl-tmp/struct_self_consist_ie/code')
from evaluation import per_instance_f1

DATA_PATH = "/root/autodl-tmp/struct_self_consist_ie/output/exp_012_rerun_1024/samples_with_logprobs.jsonl"
OUT_JSON = "/root/autodl-tmp/struct_self_consist_ie/output/analysis_lp_range_cdf.json"
OUT_FIG_DIR = "/root/autodl-tmp/struct_self_consist_ie/output/figures"
OUT_FIG = os.path.join(OUT_FIG_DIR, "lp_range_cdf.pdf")


def load_data(path):
    with open(path) as f:
        return [json.loads(line) for line in f if line.strip()]


def compute_instance_stats(inst):
    """For one instance, compute LP range and per-sample F1s."""
    logprobs = np.array(inst["logprobs"], dtype=float)
    lp_range = float(np.max(logprobs) - np.min(logprobs))
    lp_std = float(np.std(logprobs))

    gold = inst["gold"]
    samples = inst["samples"]
    f1s = np.array([per_instance_f1(s, gold, "ner") for s in samples])
    f1_range = float(np.max(f1s) - np.min(f1s))
    f1_std = float(np.std(f1s))

    return {
        "id": inst["id"],
        "logprobs": logprobs.tolist(),
        "f1s": f1s.tolist(),
        "lp_range": lp_range,
        "lp_std": lp_std,
        "lp_mean": float(np.mean(logprobs)),
        "f1_range": f1_range,
        "f1_std": f1_std,
        "f1_mean": float(np.mean(f1s)),
    }


def compute_within_instance_correlations(stats_list):
    """Compute within-instance LP-F1 correlation.
    
    N=8 is too small for per-instance Spearman. Instead:
    1. Pooled: all (LP, F1) pairs across all instances (ignoring instance structure)
    2. Instance-level: Spearman(LP_range, F1_range) and Spearman(LP_std, F1_std)
    3. Per-instance point-biserial: LP vs (F1 == max_F1) for binary quality indicator
    """
    # Pooled correlation
    all_lps = []
    all_f1s = []
    for s in stats_list:
        all_lps.extend(s["logprobs"])
        all_f1s.extend(s["f1s"])
    all_lps = np.array(all_lps)
    all_f1s = np.array(all_f1s)
    pooled_rho, pooled_p = spearmanr(all_lps, all_f1s)

    # Instance-level: LP_range vs F1_range
    lp_ranges = np.array([s["lp_range"] for s in stats_list])
    f1_ranges = np.array([s["f1_range"] for s in stats_list])
    lp_stds = np.array([s["lp_std"] for s in stats_list])
    f1_stds = np.array([s["f1_std"] for s in stats_list])
    
    range_rho, range_p = spearmanr(lp_ranges, f1_ranges)
    std_rho, std_p = spearmanr(lp_stds, f1_stds)

    # Per-instance Spearman (N=8, limited power but report distribution)
    per_inst_rhos = []
    per_inst_ps = []
    n_computable = 0
    n_significant = 0
    for s in stats_list:
        lps = np.array(s["logprobs"])
        f1s = np.array(s["f1s"])
        # Need variance in both arrays
        if np.std(lps) < 1e-12 or np.std(f1s) < 1e-12:
            continue
        n_computable += 1
        rho, p = spearmanr(lps, f1s)
        if np.isfinite(rho):
            per_inst_rhos.append(float(rho))
            per_inst_ps.append(float(p))
            if p < 0.05:
                n_significant += 1

    return {
        "pooled": {
            "rho": float(pooled_rho), "p": float(pooled_p),
            "n_pairs": len(all_lps),
        },
        "instance_level_range": {
            "rho": float(range_rho), "p": float(range_p),
            "description": "Spearman(LP_range, F1_range) across instances",
        },
        "instance_level_std": {
            "rho": float(std_rho), "p": float(std_p),
            "description": "Spearman(LP_std, F1_std) across instances",
        },
        "per_instance_spearman": {
            "n_computable": n_computable,
            "n_significant_p05": n_significant,
            "frac_significant": n_significant / n_computable if n_computable > 0 else 0.0,
            "mean_rho": float(np.mean(per_inst_rhos)) if per_inst_rhos else float("nan"),
            "median_rho": float(np.median(per_inst_rhos)) if per_inst_rhos else float("nan"),
            "std_rho": float(np.std(per_inst_rhos)) if per_inst_rhos else float("nan"),
        },
    }


def compute_cdf_data(lp_ranges):
    """Compute CDF: sorted values and cumulative fractions."""
    sorted_vals = np.sort(lp_ranges)
    cdf = np.arange(1, len(sorted_vals) + 1) / len(sorted_vals)
    return sorted_vals.tolist(), cdf.tolist()


def plot_cdf(lp_ranges, out_path, epsilon=0.05):
    """Generate publication-quality CDF plot."""
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    from matplotlib import rcParams

    rcParams["font.family"] = "serif"
    rcParams["font.size"] = 10
    rcParams["axes.linewidth"] = 0.8
    rcParams["xtick.major.width"] = 0.8
    rcParams["ytick.major.width"] = 0.8

    sorted_vals = np.sort(lp_ranges)
    cdf = np.arange(1, len(sorted_vals) + 1) / len(sorted_vals)

    # Key percentiles
    median_val = np.median(lp_ranges)
    p75 = np.percentile(lp_ranges, 75)
    p90 = np.percentile(lp_ranges, 90)
    
    # Fraction below epsilon
    frac_below_eps = float(np.mean(lp_ranges < epsilon))

    fig, ax = plt.subplots(figsize=(3.5, 2.8))

    # Main CDF line
    ax.step(sorted_vals, cdf, where="post", color="#2166ac", linewidth=1.5, zorder=3)

    # Epsilon reference line
    ax.axvline(x=epsilon, color="#b2182b", linestyle="--", linewidth=1.0, alpha=0.8, zorder=2)
    ax.text(epsilon + 0.003, 0.15, f"ε = {epsilon}",
            color="#b2182b", fontsize=8, ha="left", va="bottom")

    # Percentile annotations
    for pval, plabel, yoff in [(median_val, "median", 0.02), (p75, "75th", 0.02), (p90, "90th", 0.02)]:
        y_at_p = float(np.mean(lp_ranges <= pval))
        ax.plot(pval, y_at_p, "o", color="#2166ac", markersize=3.5, zorder=4)
        ax.annotate(f"{plabel}\n({pval:.3f})",
                    xy=(pval, y_at_p), xytext=(12, -8),
                    textcoords="offset points", fontsize=7,
                    color="#333333",
                    arrowprops=dict(arrowstyle="-", color="#999999", lw=0.5))

    ax.set_xlabel("Within-instance LP range (nats)", fontsize=10)
    ax.set_ylabel("Cumulative fraction of instances", fontsize=10)
    ax.set_xlim(left=0)
    ax.set_ylim(0, 1.02)

    # Remove top/right spines
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)

    ax.tick_params(labelsize=9)
    
    plt.tight_layout()
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    fig.savefig(out_path, dpi=300, bbox_inches="tight")
    fig.savefig(out_path.replace(".pdf", ".png"), dpi=300, bbox_inches="tight")
    plt.close(fig)
    print(f"Saved: {out_path}")
    print(f"Saved: {out_path.replace('.pdf', '.png')}")


def main():
    print("Loading data...")
    instances = load_data(DATA_PATH)
    print(f"  {len(instances)} instances loaded")

    # Compute per-instance stats
    print("Computing per-instance LP range and F1...")
    stats_list = [compute_instance_stats(inst) for inst in instances]

    lp_ranges = np.array([s["lp_range"] for s in stats_list])

    # CDF data
    cdf_x, cdf_y = compute_cdf_data(lp_ranges)

    # Key statistics
    percentiles = {
        "p10": float(np.percentile(lp_ranges, 10)),
        "p25": float(np.percentile(lp_ranges, 25)),
        "median": float(np.median(lp_ranges)),
        "p75": float(np.percentile(lp_ranges, 75)),
        "p90": float(np.percentile(lp_ranges, 90)),
        "p95": float(np.percentile(lp_ranges, 95)),
        "p99": float(np.percentile(lp_ranges, 99)),
        "mean": float(np.mean(lp_ranges)),
        "std": float(np.std(lp_ranges)),
        "min": float(np.min(lp_ranges)),
        "max": float(np.max(lp_ranges)),
    }

    # Fraction below various epsilon thresholds
    epsilon_fractions = {}
    for eps in [0.01, 0.02, 0.03, 0.05, 0.10, 0.15, 0.20]:
        frac = float(np.mean(lp_ranges < eps))
        epsilon_fractions[f"eps_{eps:.2f}"] = frac
    
    print("\n=== LP Range Distribution ===")
    for k, v in percentiles.items():
        print(f"  {k}: {v:.4f}")
    print("\n=== Fraction below epsilon ===")
    for k, v in epsilon_fractions.items():
        print(f"  {k}: {v:.3f} ({v*100:.1f}%)")

    # Correlations
    print("\nComputing correlations...")
    correlations = compute_within_instance_correlations(stats_list)
    
    print("\n=== Correlations ===")
    print(f"  Pooled Spearman(LP, F1): rho={correlations['pooled']['rho']:.4f}, "
          f"p={correlations['pooled']['p']:.2e}, n={correlations['pooled']['n_pairs']}")
    print(f"  Instance-level Spearman(LP_range, F1_range): "
          f"rho={correlations['instance_level_range']['rho']:.4f}, "
          f"p={correlations['instance_level_range']['p']:.2e}")
    print(f"  Per-instance Spearman: "
          f"computable={correlations['per_instance_spearman']['n_computable']}, "
          f"significant(p<0.05)={correlations['per_instance_spearman']['n_significant_p05']} "
          f"({correlations['per_instance_spearman']['frac_significant']*100:.1f}%), "
          f"mean_rho={correlations['per_instance_spearman']['mean_rho']:.4f}")

    # Save JSON
    output = {
        "n_instances": len(instances),
        "n_samples_per_instance": 8,
        "lp_range_percentiles": percentiles,
        "epsilon_fractions": epsilon_fractions,
        "correlations": correlations,
        "cdf": {"x": cdf_x, "y": cdf_y},
        "per_instance": [
            {"id": s["id"], "lp_range": s["lp_range"], "lp_std": s["lp_std"],
             "lp_mean": s["lp_mean"], "f1_range": s["f1_range"], "f1_mean": s["f1_mean"]}
            for s in stats_list
        ],
    }

    with open(OUT_JSON, "w") as f:
        json.dump(output, f, indent=2)
    print(f"\nSaved JSON: {OUT_JSON}")

    # Plot
    print("Generating CDF plot...")
    plot_cdf(lp_ranges, OUT_FIG, epsilon=0.05)

    print("\nDone.")


if __name__ == "__main__":
    main()
