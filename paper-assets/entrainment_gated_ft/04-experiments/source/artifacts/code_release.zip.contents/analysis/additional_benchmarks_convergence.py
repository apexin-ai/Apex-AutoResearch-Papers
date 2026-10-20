#!/usr/bin/env python3
"""exp-011: Additional benchmark convergence analysis.
Cross-arch std + exact permutation Spearman test.
"""
import json
import os
import glob
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from itertools import permutations
from scipy.stats import spearmanr

RESULT_DIR = "/root/entrainment_gated_ft/lm_eval_clean/exp011"
OUTPUT_DIR = "/root/entrainment_gated_ft/analysis"
BENCHMARKS = ["boolq", "copa", "piqa", "sciq"]
METRIC_KEY = "acc,none"

ARCHS = ["GatedDeltaNet", "RetNet", "HGRN2"]
VARIANTS = ["pure", "hybrid-24-1", "hybrid-12-1", "hybrid-6-1", "hybrid-3-1"]
ATTENTION_RATIOS = {
    "pure": 0.0,
    "hybrid-24-1": 1/25,
    "hybrid-12-1": 1/13,
    "hybrid-6-1": 1/7,
    "hybrid-3-1": 1/4,
}

def exact_spearman_p(x, y):
    rho_obs = spearmanr(x, y).statistic
    n = len(x)
    all_perms = list(permutations(range(n)))
    count = sum(1 for perm in all_perms
                if abs(spearmanr(x, [y[i] for i in perm]).statistic) >= abs(rho_obs))
    return rho_obs, count / len(all_perms)

def load_results():
    rows = []
    for arch in ARCHS:
        for variant in VARIANTS:
            model_name = f"1.3B-100B-{arch}-{variant}"
            fpath = os.path.join(RESULT_DIR, f"{model_name}.json")
            if not os.path.exists(fpath):
                print(f"WARNING: missing {fpath}")
                continue
            with open(fpath) as f:
                data = json.load(f)
            results = data.get("results", {})
            for bench in BENCHMARKS:
                if bench in results:
                    acc = results[bench].get(METRIC_KEY)
                    if acc is not None:
                        rows.append({
                            "arch": arch,
                            "variant": variant,
                            "attention_ratio": ATTENTION_RATIOS[variant],
                            "benchmark": bench,
                            "acc": acc,
                        })
    # Transformer baseline
    tf_path = os.path.join(RESULT_DIR, "transformer_1.3B_baseline.json")
    if os.path.exists(tf_path):
        with open(tf_path) as f:
            data = json.load(f)
        results = data.get("results", {})
        for bench in BENCHMARKS:
            if bench in results:
                acc = results[bench].get(METRIC_KEY)
                if acc is not None:
                    rows.append({
                        "arch": "Transformer",
                        "variant": "baseline",
                        "attention_ratio": 1.0,
                        "benchmark": bench,
                        "acc": acc,
                    })
    return pd.DataFrame(rows)

def compute_cross_arch_std(df):
    hybrid_df = df[df["arch"].isin(ARCHS)]
    grouped = hybrid_df.groupby(["variant", "attention_ratio", "benchmark"])["acc"]
    stats = grouped.agg(["mean", "std", "count"]).reset_index()
    return stats

def run_spearman_tests(df):
    hybrid_df = df[df["arch"].isin(ARCHS)]
    results = {}
    for bench in BENCHMARKS:
        bench_df = hybrid_df[hybrid_df["benchmark"] == bench]
        avg_by_ratio = bench_df.groupby("attention_ratio")["acc"].mean().reset_index()
        avg_by_ratio = avg_by_ratio.sort_values("attention_ratio")
        x = avg_by_ratio["attention_ratio"].values
        y = avg_by_ratio["acc"].values
        rho, exact_p = exact_spearman_p(x, y)
        results[bench] = {"rho": rho, "exact_p": exact_p}
    n_tests = len(results)
    for bench in results:
        results[bench]["bonferroni_adj_p"] = min(results[bench]["exact_p"] * n_tests, 1.0)
    return results

def make_figure(df, spearman_results, cross_arch_stats):
    fig, axes = plt.subplots(2, 2, figsize=(12, 10))
    axes = axes.flatten()
    colors = {"GatedDeltaNet": "#1f77b4", "RetNet": "#ff7f0e", "HGRN2": "#2ca02c", "Transformer": "#d62728"}
    markers = {"GatedDeltaNet": "o", "RetNet": "s", "HGRN2": "^", "Transformer": "D"}

    for idx, bench in enumerate(BENCHMARKS):
        ax = axes[idx]
        bench_df = df[df["benchmark"] == bench]
        for arch in ARCHS + ["Transformer"]:
            arch_df = bench_df[bench_df["arch"] == arch].sort_values("attention_ratio")
            if len(arch_df) == 0:
                continue
            ax.plot(arch_df["attention_ratio"], arch_df["acc"],
                    marker=markers[arch], color=colors[arch], label=arch,
                    linewidth=1.5, markersize=6, alpha=0.8)

        # Cross-arch mean
        hybrid_bench = bench_df[bench_df["arch"].isin(ARCHS)]
        mean_by_ratio = hybrid_bench.groupby("attention_ratio")["acc"].mean().reset_index()
        mean_by_ratio = mean_by_ratio.sort_values("attention_ratio")
        ax.plot(mean_by_ratio["attention_ratio"], mean_by_ratio["acc"],
                "k--", linewidth=2, alpha=0.5, label="Cross-arch mean")

        sr = spearman_results.get(bench, {})
        rho = sr.get("rho", float("nan"))
        p_adj = sr.get("bonferroni_adj_p", float("nan"))
        sig = "*" if p_adj < 0.05 else ""
        ax.set_title(f"{bench}\n" + r"$\rho$" + f"={rho:.3f}, p_adj={p_adj:.4f}{sig}", fontsize=11)
        ax.set_xlabel("Attention Ratio")
        ax.set_ylabel("Accuracy")
        ax.legend(fontsize=8)
        ax.grid(True, alpha=0.3)

    plt.suptitle("exp-011: Additional Benchmarks — Accuracy vs Attention Ratio", fontsize=14, y=1.02)
    plt.tight_layout()
    fig_path = os.path.join(OUTPUT_DIR, "additional_benchmarks_convergence.png")
    plt.savefig(fig_path, dpi=150, bbox_inches="tight")
    print(f"Figure saved: {fig_path}")
    return fig_path

def main():
    df = load_results()
    print(f"Loaded {len(df)} data points")
    print(df.groupby(["arch", "variant"]).size().unstack(fill_value=0))

    csv_path = os.path.join(OUTPUT_DIR, "additional_benchmarks_results.csv")
    df.to_csv(csv_path, index=False)
    print(f"CSV saved: {csv_path}")

    cross_arch = compute_cross_arch_std(df)
    print("\nCross-arch std by variant and benchmark:")
    print(cross_arch.to_string(index=False))

    spearman_results = run_spearman_tests(df)
    print("\nSpearman tests (exact permutation, two-tailed):")
    for bench, r in spearman_results.items():
        sig = "***" if r["bonferroni_adj_p"] < 0.001 else "**" if r["bonferroni_adj_p"] < 0.01 else "*" if r["bonferroni_adj_p"] < 0.05 else ""
        print(f"  {bench}: rho={r['rho']:.4f}, exact_p={r['exact_p']:.4f}, bonferroni_adj_p={r['bonferroni_adj_p']:.4f} {sig}")

    summary = {
        "benchmarks": BENCHMARKS,
        "n_archs": len(ARCHS),
        "n_variants": len(VARIANTS),
        "spearman_results": {b: {k: float(v) for k, v in r.items()} for b, r in spearman_results.items()},
        "any_significant_after_bonferroni": any(r["bonferroni_adj_p"] < 0.05 for r in spearman_results.values()),
        "cross_arch_std": cross_arch.to_dict(orient="records"),
    }
    summary_path = os.path.join(OUTPUT_DIR, "additional_benchmarks_summary.json")
    with open(summary_path, "w") as f:
        json.dump(summary, f, indent=2)
    print(f"\nSummary saved: {summary_path}")

    make_figure(df, spearman_results, cross_arch)

if __name__ == "__main__":
    main()
