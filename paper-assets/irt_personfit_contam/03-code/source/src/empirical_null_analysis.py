"""Bootstrap empirical null analysis for lz* person-fit statistic.

Diagnoses systematic bias of lz* on real LLM data by re-running bootstrap
and saving full null distributions for each (model, benchmark) cell.
"""

import json
import os
import sys
import time
from multiprocessing import Pool, cpu_count

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy import stats

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from person_fit import (
    estimate_theta_mle, compute_lz_star, filter_valid_items,
    generate_response, _estimate_theta_mle_batch,
)

PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
COMBINE_CSV = os.path.join(PROJECT_DIR, "artifacts", "psn_irt_phase_b", "combine.csv")
PARAMS_DIR = os.path.join(PROJECT_DIR, "artifacts", "psn_irt_params")
V2_PVALUES = os.path.join(PROJECT_DIR, "artifacts", "phase_b_two_sided_v2", "empirical_pvalues.csv")
OUTPUT_DIR = os.path.join(PROJECT_DIR, "artifacts", "empirical_null_analysis")

N_BOOT = 1000
SEED_BASE = 42

MODEL_NAMES = {
    0: "360GPT2-Pro", 1: "DeepSeek-V3", 2: "Doubao-pro", 3: "Gemini-1.5",
    4: "Gemma-2B-it", 5: "Hunyuan-Turbo", 6: "Mistral-7B-Instruct-v0.1",
    7: "Moonshot-v1", 8: "Qwen-Plus", 9: "Qwen2.5-3B-Instruct",
    10: "Vicuna-7B-v1.3", 11: "Yi-Lightning",
}

BENCHMARK_SLICES = {
    'arc_c':     (0, 295),
    'gsm8k':     (10004, 11323),
    'hellaswag': (11323, 21365),
    'humaneval': (21365, 21529),
    'mmlu':      (27029, 41071),
}

BENCHMARKS = sorted(BENCHMARK_SLICES.keys())

UNFLAGGED_CELLS = [
    (11, "arc_c"),      # Yi-Lightning/arc_c
    (0, "humaneval"),   # 360GPT2-Pro/humaneval
    (11, "humaneval"),  # Yi-Lightning/humaneval
]


def load_params(benchmark):
    path = os.path.join(PARAMS_DIR, f"{benchmark}_params.csv")
    df = pd.read_csv(path)
    return (df["a_discrimination"].values, df["b_difficulty"].values,
            df["c_guessing"].values, df["d_feasibility"].values)


def bootstrap_one_cell(args):
    """Bootstrap and return full null lz* distribution for one cell."""
    sid, benchmark, x_obs, a, b, c, d, valid_mask, theta_bench, lz_star_obs, seed, n_boot = args

    a_v = a[valid_mask]
    b_v = b[valid_mask]
    c_v = c[valid_mask]
    d_v = d[valid_mask]
    rng = np.random.default_rng(seed)

    X_boot = generate_response(np.full(n_boot, theta_bench), a_v, b_v, c_v, d_v, rng=rng)
    thetas_boot = _estimate_theta_mle_batch(X_boot, a_v, b_v, c_v, d_v)
    lz_star_boot = compute_lz_star(X_boot, thetas_boot[:, None], a_v, b_v, c_v, d_v)

    abs_obs = abs(lz_star_obs)
    p_value = float(np.mean(np.abs(lz_star_boot) >= abs_obs))

    return {
        "sid": sid,
        "benchmark": benchmark,
        "theta_bench": theta_bench,
        "lz_star_obs": lz_star_obs,
        "p_value": p_value,
        "lz_star_boot": lz_star_boot.astype(np.float32),
    }


def run_bootstrap(combine, n_boot):
    """Run bootstrap for all 60 cells, return list of result dicts."""
    args_list = []
    for bm in BENCHMARKS:
        col_start, col_end = BENCHMARK_SLICES[bm]
        a, b, c, d = load_params(bm)
        valid_mask = filter_valid_items(a, b, c, d, min_a=0.0)
        a_v, b_v, c_v, d_v = a[valid_mask], b[valid_mask], c[valid_mask], d[valid_mask]
        n_valid = int(valid_mask.sum())
        print(f"  {bm}: {col_end - col_start} items, {n_valid} valid")

        for sid in range(12):
            x_full = combine[sid, col_start:col_end]
            x = x_full[valid_mask]
            theta_bench = estimate_theta_mle(x, a_v, b_v, c_v, d_v)
            lz_star_obs = float(compute_lz_star(x, theta_bench, a_v, b_v, c_v, d_v))

            bm_idx = BENCHMARKS.index(bm)
            seed = sid * 100 + bm_idx * 10 + SEED_BASE
            args_list.append((
                sid, bm, x, a, b, c, d, valid_mask, theta_bench, lz_star_obs, seed, n_boot
            ))

    n_workers = min(cpu_count(), 8)
    print(f"  Running {len(args_list)} cells × {n_boot} bootstrap, {n_workers} workers...")
    with Pool(n_workers) as pool:
        results = pool.map(bootstrap_one_cell, args_list)
    return results


def make_qq_plots(results):
    """Q-Q plots: bootstrap null lz* vs N(0,1), one panel per benchmark."""
    fig, axes = plt.subplots(1, 5, figsize=(20, 4.5), sharey=True)
    colors = plt.cm.tab20(np.linspace(0, 1, 12))

    for idx, bm in enumerate(BENCHMARKS):
        ax = axes[idx]
        cells = [r for r in results if r["benchmark"] == bm]
        for r in cells:
            boot = np.sort(r["lz_star_boot"])
            n = len(boot)
            theoretical = stats.norm.ppf(np.linspace(1/(n+1), n/(n+1), n))
            ax.plot(theoretical, boot, '.', color=colors[r["sid"]],
                    alpha=0.4, markersize=1.5, label=MODEL_NAMES[r["sid"]])

        lim = max(abs(ax.get_xlim()[0]), abs(ax.get_xlim()[1]),
                  abs(ax.get_ylim()[0]), abs(ax.get_ylim()[1]))
        lim = min(lim, 8)
        ax.plot([-lim, lim], [-lim, lim], 'k--', linewidth=0.8, alpha=0.5)
        ax.set_xlim(-lim, lim)
        ax.set_ylim(-lim, lim)
        ax.set_title(bm, fontsize=11)
        ax.set_xlabel("N(0,1) quantiles", fontsize=9)
        if idx == 0:
            ax.set_ylabel("Bootstrap lz* quantiles", fontsize=9)
        ax.set_aspect('equal')
        ax.tick_params(labelsize=8)

    handles = [plt.Line2D([0], [0], marker='o', color='w',
               markerfacecolor=colors[i], markersize=5, label=MODEL_NAMES[i])
               for i in range(12)]
    fig.legend(handles=handles, loc='lower center', ncol=6, fontsize=7,
               bbox_to_anchor=(0.5, -0.08), frameon=False)
    fig.suptitle("Q-Q: Bootstrap Null lz* vs N(0,1)", fontsize=13, y=1.02)
    plt.tight_layout()
    path = os.path.join(OUTPUT_DIR, "qq_plots_by_benchmark.png")
    fig.savefig(path, dpi=200, bbox_inches="tight")
    plt.close(fig)
    print(f"  Saved {path}")


def make_ks_table(results):
    """KS test of bootstrap null lz* against N(0,1)."""
    rows = []
    for r in results:
        ks_stat, ks_p = stats.kstest(r["lz_star_boot"], 'norm')
        rows.append({
            "model": MODEL_NAMES[r["sid"]],
            "benchmark": r["benchmark"],
            "ks_statistic": round(ks_stat, 6),
            "ks_pvalue": ks_p,
            "reject_normal": ks_p < 0.05,
        })
    df = pd.DataFrame(rows)
    path = os.path.join(OUTPUT_DIR, "ks_test_results.csv")
    df.to_csv(path, index=False)
    print(f"  Saved {path}")
    return df


def make_bias_table(results):
    """Null distribution bias: mean, std, skew, kurtosis per cell + benchmark aggregation."""
    rows = []
    for r in results:
        boot = r["lz_star_boot"]
        rows.append({
            "model": MODEL_NAMES[r["sid"]],
            "benchmark": r["benchmark"],
            "null_mean": round(float(np.mean(boot)), 4),
            "null_std": round(float(np.std(boot, ddof=1)), 4),
            "null_skew": round(float(stats.skew(boot)), 4),
            "null_kurtosis": round(float(stats.kurtosis(boot)), 4),
        })
    df = pd.DataFrame(rows)

    agg_rows = []
    for bm in BENCHMARKS:
        sub = df[df["benchmark"] == bm]
        agg_rows.append({
            "model": f"[{bm} avg]",
            "benchmark": bm,
            "null_mean": round(float(sub["null_mean"].mean()), 4),
            "null_std": round(float(sub["null_std"].mean()), 4),
            "null_skew": round(float(sub["null_skew"].mean()), 4),
            "null_kurtosis": round(float(sub["null_kurtosis"].mean()), 4),
        })
    df_full = pd.concat([df, pd.DataFrame(agg_rows)], ignore_index=True)
    path = os.path.join(OUTPUT_DIR, "null_bias_table.csv")
    df_full.to_csv(path, index=False)
    print(f"  Saved {path}")
    return df


def make_unflagged_analysis(results):
    """Deep analysis of the 3 unflagged cells."""
    v2_df = pd.read_csv(V2_PVALUES)
    lines = ["# Unflagged Cells Deep Analysis\n"]

    for sid, bm in UNFLAGGED_CELLS:
        name = MODEL_NAMES[sid]
        r = next(x for x in results if x["sid"] == sid and x["benchmark"] == bm)
        boot = r["lz_star_boot"]
        obs = r["lz_star_obs"]

        v2_row = v2_df[(v2_df["student_id"] == sid) & (v2_df["benchmark"] == bm)].iloc[0]
        emp_p = v2_row["empirical_p"]
        adj_p = v2_row["bh_adjusted_p"]

        percentile = float(np.mean(boot <= obs) * 100)
        abs_percentile = float(np.mean(np.abs(boot) >= abs(obs)) * 100)

        ks_stat, ks_p = stats.kstest(boot, 'norm')

        lines.append(f"## {name} / {bm}\n")
        lines.append(f"- **Observed lz***: {obs:.4f}")
        lines.append(f"- **Empirical p-value** (v2): {emp_p:.4f}")
        lines.append(f"- **BH-adjusted p-value**: {adj_p:.4f}")
        lines.append(f"- **Bootstrap null**: mean={np.mean(boot):.4f}, std={np.std(boot, ddof=1):.4f}, "
                      f"skew={stats.skew(boot):.4f}, kurtosis={stats.kurtosis(boot):.4f}")
        lines.append(f"- **KS test vs N(0,1)**: D={ks_stat:.4f}, p={ks_p:.4g}")
        lines.append(f"- **Observed lz* percentile** in null: {percentile:.1f}%")
        lines.append(f"- **P(|lz*| >= |obs|)**: {abs_percentile:.1f}%")
        lines.append("")

        if abs(obs) < 2.0:
            lines.append(f"The observed lz* ({obs:.3f}) is moderate — within the range that the "
                          "bootstrap null can plausibly produce. Unlike most other cells where "
                          "|lz*| >> 3, this cell's response pattern is not dramatically inconsistent "
                          "with the 4PL model.")
        else:
            lines.append(f"The observed lz* ({obs:.3f}) is elevated but the bootstrap null distribution "
                          f"has sufficient variance (std={np.std(boot, ddof=1):.3f}) that the empirical "
                          f"p-value ({emp_p:.3f}) does not survive BH correction.")

        n_items = BENCHMARK_SLICES[bm][1] - BENCHMARK_SLICES[bm][0]
        lines.append(f"\n{bm} has {n_items} items. ", )
        if bm == "humaneval":
            lines.append("HumanEval's small item count (164) limits the power of lz* — "
                          "fewer items mean higher variance in the statistic, making it harder "
                          "to reject the null even when some misfit exists.")
        elif bm == "arc_c":
            lines.append("ARC-Challenge has 295 items — moderate size. Yi-Lightning's lz* is "
                          "positive but not extreme enough to reject after multiple testing correction.")
        lines.append("\n")

    path = os.path.join(OUTPUT_DIR, "unflagged_analysis.md")
    with open(path, "w") as f:
        f.write("\n".join(lines))
    print(f"  Saved {path}")


def make_null_distributions_plot(results):
    """Violin/histogram of bootstrap null lz* distributions per benchmark."""
    fig, axes = plt.subplots(1, 5, figsize=(22, 5), sharey=True)
    colors = plt.cm.tab20(np.linspace(0, 1, 12))

    for idx, bm in enumerate(BENCHMARKS):
        ax = axes[idx]
        cells = sorted([r for r in results if r["benchmark"] == bm], key=lambda r: r["sid"])

        positions = np.arange(len(cells))
        violin_data = [r["lz_star_boot"] for r in cells]

        parts = ax.violinplot(violin_data, positions=positions, showmeans=True,
                              showmedians=True, widths=0.7)
        for i, pc in enumerate(parts['bodies']):
            pc.set_facecolor(colors[cells[i]["sid"]])
            pc.set_alpha(0.6)
        for key in ['cmeans', 'cmedians', 'cbars', 'cmins', 'cmaxes']:
            if key in parts:
                parts[key].set_linewidth(0.5)

        x_ref = np.linspace(-4, 4, 200)
        y_ref = stats.norm.pdf(x_ref)
        y_ref_scaled = y_ref / y_ref.max() * 0.35
        for pos in positions:
            ax.plot(pos + y_ref_scaled, x_ref, 'k-', alpha=0.15, linewidth=0.5)
            ax.plot(pos - y_ref_scaled, x_ref, 'k-', alpha=0.15, linewidth=0.5)

        ax.axhline(0, color='gray', linewidth=0.5, linestyle='--')
        ax.set_xticks(positions)
        ax.set_xticklabels([MODEL_NAMES[c["sid"]] for c in cells],
                           rotation=90, fontsize=6)
        ax.set_title(bm, fontsize=11)
        if idx == 0:
            ax.set_ylabel("Bootstrap null lz*", fontsize=10)
        ax.tick_params(axis='y', labelsize=8)

    fig.suptitle("Bootstrap Null lz* Distributions (N=1000 per cell)\nBlack outlines = N(0,1) reference",
                 fontsize=12, y=1.04)
    plt.tight_layout()
    path = os.path.join(OUTPUT_DIR, "null_distributions.png")
    fig.savefig(path, dpi=200, bbox_inches="tight")
    plt.close(fig)
    print(f"  Saved {path}")


def make_summary_json(results, ks_df, bias_df):
    """Summary JSON with key numbers for the paper."""
    summary = {"n_boot": N_BOOT, "n_cells": len(results), "by_benchmark": {}, "overall": {}}

    all_means = []
    all_stds = []
    all_ks_reject = []

    for bm in BENCHMARKS:
        bm_results = [r for r in results if r["benchmark"] == bm]
        bm_ks = ks_df[ks_df["benchmark"] == bm]
        bm_bias = bias_df[bias_df["benchmark"] == bm]

        mean_bias = float(bm_bias["null_mean"].mean())
        mean_std = float(bm_bias["null_std"].mean())
        ks_reject_rate = float(bm_ks["reject_normal"].mean())
        mean_skew = float(bm_bias["null_skew"].mean())
        mean_kurtosis = float(bm_bias["null_kurtosis"].mean())

        all_means.append(mean_bias)
        all_stds.append(mean_std)
        all_ks_reject.append(ks_reject_rate)

        summary["by_benchmark"][bm] = {
            "n_items": BENCHMARK_SLICES[bm][1] - BENCHMARK_SLICES[bm][0],
            "mean_null_bias": round(mean_bias, 4),
            "mean_null_std": round(mean_std, 4),
            "mean_null_skew": round(mean_skew, 4),
            "mean_null_kurtosis": round(mean_kurtosis, 4),
            "ks_reject_rate": round(ks_reject_rate, 4),
        }

    summary["overall"] = {
        "mean_null_bias": round(float(np.mean(all_means)), 4),
        "mean_null_std": round(float(np.mean(all_stds)), 4),
        "ks_reject_rate": round(float(np.mean(all_ks_reject)), 4),
        "key_findings": [
            f"Bootstrap null lz* distributions deviate from N(0,1) in "
            f"{int(ks_df['reject_normal'].sum())}/60 cells (KS test, α=0.05)",
            f"Mean null bias across benchmarks: {np.mean(all_means):.4f} (expected: 0)",
            f"Mean null std across benchmarks: {np.mean(all_stds):.4f} (expected: 1)",
        ],
    }

    path = os.path.join(OUTPUT_DIR, "empirical_null_summary.json")
    with open(path, "w") as f:
        json.dump(summary, f, indent=2)
    print(f"  Saved {path}")
    return summary


def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    t0 = time.time()

    # Check for test mode
    test_mode = "--test" in sys.argv
    n_boot = 10 if test_mode else N_BOOT
    if test_mode:
        print("=== TEST MODE: 1 model × 1 benchmark × 10 bootstrap ===")

    print("Loading data...")
    combine = pd.read_csv(COMBINE_CSV, header=None).values
    print(f"  combine.csv: {combine.shape}")

    print(f"\nBootstrapping (N={n_boot})...")
    if test_mode:
        bm = "arc_c"
        col_start, col_end = BENCHMARK_SLICES[bm]
        a, b, c, d = load_params(bm)
        valid_mask = filter_valid_items(a, b, c, d, min_a=0.0)
        a_v, b_v, c_v, d_v = a[valid_mask], b[valid_mask], c[valid_mask], d[valid_mask]
        sid = 0
        x = combine[sid, col_start:col_end][valid_mask]
        theta = estimate_theta_mle(x, a_v, b_v, c_v, d_v)
        lz_obs = float(compute_lz_star(x, theta, a_v, b_v, c_v, d_v))
        result = bootstrap_one_cell((sid, bm, x, a, b, c, d, valid_mask, theta, lz_obs, 42, n_boot))
        print(f"  Test cell: {MODEL_NAMES[sid]}/{bm}")
        print(f"    theta={result['theta_bench']:.4f}, lz*_obs={result['lz_star_obs']:.4f}")
        print(f"    bootstrap null: mean={np.mean(result['lz_star_boot']):.4f}, "
              f"std={np.std(result['lz_star_boot'], ddof=1):.4f}")
        print(f"    p_value={result['p_value']:.4f}")
        print(f"\nTest passed in {time.time()-t0:.1f}s. Run without --test for full analysis.")
        return

    results = run_bootstrap(combine, n_boot)

    print("\nGenerating outputs...")
    print("  Q-Q plots...")
    make_qq_plots(results)
    print("  KS test table...")
    ks_df = make_ks_table(results)
    print("  Bias table...")
    bias_df = make_bias_table(results)
    print("  Unflagged analysis...")
    make_unflagged_analysis(results)
    print("  Null distribution plots...")
    make_null_distributions_plot(results)
    print("  Summary JSON...")
    summary = make_summary_json(results, ks_df, bias_df)

    elapsed = time.time() - t0
    print(f"\nDone in {elapsed:.1f}s. Output: {OUTPUT_DIR}")
    print(f"\nKey numbers:")
    print(f"  KS reject rate: {summary['overall']['ks_reject_rate']:.1%}")
    print(f"  Mean null bias: {summary['overall']['mean_null_bias']:.4f}")
    print(f"  Mean null std:  {summary['overall']['mean_null_std']:.4f}")
    for finding in summary["overall"]["key_findings"]:
        print(f"  → {finding}")


if __name__ == "__main__":
    main()
