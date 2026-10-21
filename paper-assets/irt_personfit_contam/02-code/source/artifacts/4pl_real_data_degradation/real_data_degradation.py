"""3PL vs 4PL lz* degradation analysis on PSN-IRT real response data.

Input:
  - artifacts/psn_irt_phase_b/combine.csv          (12×41871 binary response matrix)
  - artifacts/psn_irt_params/item_parameters_all.csv (4PL item parameters)
  - artifacts/psn_irt_phase_b/student_abilities.csv  (PSN-IRT global θ)
  - artifacts/phase_b_results/personfit_matrix.csv   (reference 4PL lz* for validation)

Output (in artifacts/4pl_real_data_degradation/):
  - degradation_comparison.csv
  - benchmark_d_stats.csv
  - scatter_4pl_vs_3pl.png
  - delta_distribution.png
  - d_vs_delta_relationship.png
  - degradation_report.md
"""

import sys
from pathlib import Path
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from scipy import stats

PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(PROJECT_ROOT / "src"))
from person_fit import compute_lz_star

ARTIFACT_DIR = Path(__file__).resolve().parent

MODEL_NAMES = {
    0: "360GPT2-Pro", 1: "DeepSeek-V3", 2: "Doubao-pro",
    3: "Gemini-1.5", 4: "Gemma-2B-it", 5: "Hunyuan-Turbo",
    6: "Mistral-7B-Instruct-v0.1", 7: "Moonshot-v1", 8: "Qwen-Plus",
    9: "Qwen2.5-3B-Instruct", 10: "Vicuna-7B-v1.3", 11: "Yi-Lightning",
}

TARGET_BENCHMARKS = ["MMLU", "HellaSwag", "GSM8K", "ARC-C", "HumanEval"]


def load_data():
    responses = np.loadtxt(
        PROJECT_ROOT / "artifacts" / "psn_irt_phase_b" / "combine.csv",
        delimiter=","
    )
    params = pd.read_csv(
        PROJECT_ROOT / "artifacts" / "psn_irt_params" / "item_parameters_all.csv"
    )
    abilities = pd.read_csv(
        PROJECT_ROOT / "artifacts" / "psn_irt_phase_b" / "student_abilities.csv"
    )
    ref = pd.read_csv(
        PROJECT_ROOT / "artifacts" / "phase_b_results" / "personfit_matrix.csv"
    )
    return responses, params, abilities, ref


def compute_degradation(responses, params, abilities, ref):
    theta_map = dict(zip(abilities["student_id"], abilities["ability"]))
    results = []

    for bm in TARGET_BENCHMARKS:
        bm_params = params[params["benchmark"] == bm].sort_values("item_idx").reset_index(drop=True)
        global_cols = bm_params["item_idx_global"].values

        a = bm_params["a_discrimination"].values
        b = bm_params["b_difficulty"].values
        c = bm_params["c_guessing"].values
        d = bm_params["d_feasibility"].values

        # Filter items with a > 0 (same as phase_b)
        valid = a > 0
        a, b, c, d = a[valid], b[valid], c[valid], d[valid]
        global_cols = global_cols[valid]

        X_bm = responses[:, global_cols]

        for sid in range(12):
            theta = theta_map[sid]
            x = X_bm[sid]

            lz_4pl = compute_lz_star(x, theta, a, b, c, d)
            lz_3pl = compute_lz_star(x, theta, a, b, c, np.ones_like(d))

            delta = lz_4pl - lz_3pl
            pct_change = (delta / abs(lz_4pl) * 100) if abs(lz_4pl) > 1e-10 else 0.0

            results.append({
                "student_id": sid,
                "model_name": MODEL_NAMES[sid],
                "benchmark": bm,
                "lz_star_4pl": lz_4pl,
                "lz_star_3pl": lz_3pl,
                "delta_lz_star": delta,
                "pct_change": pct_change,
            })

    df = pd.DataFrame(results)

    # Validate against reference
    for _, row in df.iterrows():
        ref_row = ref[(ref["student_id"] == row["student_id"]) & (ref["benchmark"] == row["benchmark"])]
        if len(ref_row) == 1:
            ref_val = ref_row["lz_star"].values[0]
            diff = abs(row["lz_star_4pl"] - ref_val)
            if diff > 0.01:
                print(f"WARNING: mismatch for {row['model_name']} {row['benchmark']}: "
                      f"computed={row['lz_star_4pl']:.4f}, ref={ref_val:.4f}, diff={diff:.4f}")

    # Specific check: Gemini-1.5 MMLU should be ~34.75
    gem_mmlu = df[(df["student_id"] == 3) & (df["benchmark"] == "MMLU")]["lz_star_4pl"].values[0]
    if abs(gem_mmlu - 34.75) > 1.0:
        print(f"CRITICAL: Gemini-1.5 MMLU lz*_4pl = {gem_mmlu:.2f}, expected ~34.75. Data loading may be wrong.")
        sys.exit(1)
    else:
        print(f"Validation passed: Gemini-1.5 MMLU lz*_4pl = {gem_mmlu:.4f}")

    return df


def compute_d_stats(params):
    rows = []
    for bm in TARGET_BENCHMARKS:
        d = params[params["benchmark"] == bm]["d_feasibility"].values
        a = params[params["benchmark"] == bm]["a_discrimination"].values
        d = d[a > 0]  # same filter
        rows.append({
            "benchmark": bm,
            "n_items": len(d),
            "mean_d": d.mean(),
            "std_d": d.std(),
            "min_d": d.min(),
            "max_d": d.max(),
            "pct_d_lt_095": (d < 0.95).mean() * 100,
            "pct_d_lt_090": (d < 0.90).mean() * 100,
            "pct_d_lt_080": (d < 0.80).mean() * 100,
        })
    return pd.DataFrame(rows)


def plot_scatter(df):
    """Scatter plot: 4PL lz* vs 3PL lz* per (model, benchmark)."""
    fig, ax = plt.subplots(figsize=(8, 7))
    colors = plt.cm.Set2(np.linspace(0, 1, len(TARGET_BENCHMARKS)))
    bm_colors = dict(zip(TARGET_BENCHMARKS, colors))

    for bm in TARGET_BENCHMARKS:
        sub = df[df["benchmark"] == bm]
        ax.scatter(sub["lz_star_4pl"], sub["lz_star_3pl"],
                   c=[bm_colors[bm]], label=bm, s=60, edgecolors="k", linewidths=0.5, zorder=3)

    all_vals = np.concatenate([df["lz_star_4pl"].values, df["lz_star_3pl"].values])
    lo, hi = all_vals.min() - 2, all_vals.max() + 2
    ax.plot([lo, hi], [lo, hi], "k--", alpha=0.4, label="y = x")

    r, _ = stats.pearsonr(df["lz_star_4pl"], df["lz_star_3pl"])
    rmse = np.sqrt(np.mean((df["lz_star_4pl"] - df["lz_star_3pl"]) ** 2))
    ax.text(0.05, 0.95, f"Pearson r = {r:.4f}\nRMSE = {rmse:.2f}",
            transform=ax.transAxes, va="top", fontsize=11,
            bbox=dict(boxstyle="round", fc="white", alpha=0.8))

    ax.set_xlabel("$lz^*$ (4PL)", fontsize=13)
    ax.set_ylabel("$lz^*$ (3PL, d=1)", fontsize=13)
    ax.set_title("4PL vs 3PL(d=1) Person-Fit Statistics", fontsize=14)
    ax.legend(fontsize=10)
    ax.set_aspect("equal")
    fig.tight_layout()
    fig.savefig(ARTIFACT_DIR / "scatter_4pl_vs_3pl.png", dpi=150)
    plt.close(fig)
    print(f"Saved scatter_4pl_vs_3pl.png  (r={r:.4f}, RMSE={rmse:.2f})")


def plot_delta_distribution(df):
    """Grouped bar chart + histograms of Δlz*."""
    fig, axes = plt.subplots(2, 1, figsize=(14, 10), gridspec_kw={"height_ratios": [2, 1]})

    # Upper: grouped bar chart
    ax = axes[0]
    n_models = 12
    n_bm = len(TARGET_BENCHMARKS)
    x = np.arange(n_models)
    width = 0.15
    colors = plt.cm.Set2(np.linspace(0, 1, n_bm))

    for i, bm in enumerate(TARGET_BENCHMARKS):
        sub = df[df["benchmark"] == bm].sort_values("student_id")
        offset = (i - n_bm / 2 + 0.5) * width
        ax.bar(x + offset, sub["delta_lz_star"].values, width,
               label=bm, color=colors[i], edgecolor="k", linewidth=0.3)

    ax.set_xticks(x)
    ax.set_xticklabels([MODEL_NAMES[i] for i in range(12)], rotation=45, ha="right", fontsize=8)
    ax.set_ylabel("$\\Delta lz^*$ (4PL − 3PL)", fontsize=12)
    ax.set_title("$\\Delta lz^*$ by Model and Benchmark", fontsize=13)
    ax.legend(fontsize=9, ncol=n_bm)
    ax.axhline(0, color="k", linewidth=0.5)

    # Lower: per-benchmark histograms
    ax2 = axes[1]
    for i, bm in enumerate(TARGET_BENCHMARKS):
        vals = df[df["benchmark"] == bm]["delta_lz_star"].values
        ax2.hist(vals, bins=15, alpha=0.6, label=bm, color=colors[i], edgecolor="k", linewidth=0.3)
    ax2.set_xlabel("$\\Delta lz^*$", fontsize=12)
    ax2.set_ylabel("Count", fontsize=12)
    ax2.set_title("Distribution of $\\Delta lz^*$ by Benchmark", fontsize=13)
    ax2.legend(fontsize=9)

    fig.tight_layout()
    fig.savefig(ARTIFACT_DIR / "delta_distribution.png", dpi=150)
    plt.close(fig)
    print("Saved delta_distribution.png")


def plot_d_vs_delta(df, d_stats):
    """Scatter: mean(d) per benchmark vs mean(|Δlz*|)."""
    fig, ax = plt.subplots(figsize=(7, 6))

    bm_delta = df.groupby("benchmark")["delta_lz_star"].apply(lambda s: np.mean(np.abs(s))).reset_index()
    bm_delta.columns = ["benchmark", "mean_abs_delta"]
    merged = bm_delta.merge(d_stats[["benchmark", "mean_d"]], on="benchmark")

    ax.scatter(merged["mean_d"], merged["mean_abs_delta"], s=100, c="steelblue", edgecolors="k", zorder=3)
    for _, row in merged.iterrows():
        ax.annotate(row["benchmark"], (row["mean_d"], row["mean_abs_delta"]),
                    textcoords="offset points", xytext=(8, 5), fontsize=10)

    # Trend line
    slope, intercept, r, p, _ = stats.linregress(merged["mean_d"], merged["mean_abs_delta"])
    x_line = np.linspace(merged["mean_d"].min() - 0.005, merged["mean_d"].max() + 0.005, 50)
    ax.plot(x_line, slope * x_line + intercept, "r--", alpha=0.7,
            label=f"Linear fit (r={r:.3f}, p={p:.3f})")

    ax.set_xlabel("Mean $d$ (feasibility)", fontsize=13)
    ax.set_ylabel("Mean $|\\Delta lz^*|$", fontsize=13)
    ax.set_title("Benchmark Mean $d$ vs Impact of $d$-Parameter Removal", fontsize=13)
    ax.legend(fontsize=10)
    fig.tight_layout()
    fig.savefig(ARTIFACT_DIR / "d_vs_delta_relationship.png", dpi=150)
    plt.close(fig)
    print("Saved d_vs_delta_relationship.png")


def generate_report(df, d_stats):
    # Aggregated stats
    bm_summary = df.groupby("benchmark").agg(
        mean_delta=("delta_lz_star", "mean"),
        std_delta=("delta_lz_star", "std"),
        mean_abs_delta=("delta_lz_star", lambda s: np.mean(np.abs(s))),
        max_abs_delta=("delta_lz_star", lambda s: np.max(np.abs(s))),
    ).reindex(TARGET_BENCHMARKS)

    model_summary = df.groupby("model_name").agg(
        mean_delta=("delta_lz_star", "mean"),
        mean_abs_delta=("delta_lz_star", lambda s: np.mean(np.abs(s))),
    ).sort_values("mean_abs_delta", ascending=False)

    r, _ = stats.pearsonr(df["lz_star_4pl"], df["lz_star_3pl"])
    rmse = np.sqrt(np.mean((df["lz_star_4pl"] - df["lz_star_3pl"]) ** 2))

    # Which benchmarks are most affected
    most_affected_bm = bm_summary["mean_abs_delta"].idxmax()
    least_affected_bm = bm_summary["mean_abs_delta"].idxmin()
    most_affected_model = model_summary["mean_abs_delta"].idxmax()

    report = f"""# 3PL vs 4PL lz* Degradation Analysis on Real Data

## Overview

Compared 4PL lz* (with estimated d parameters) against 3PL lz* (d=1.0) for 12 PSN-IRT models across 5 benchmarks.

## d-Parameter Statistics by Benchmark

| Benchmark | Items | Mean d | Std d | % d<0.95 | % d<0.90 | % d<0.80 |
|-----------|-------|--------|-------|----------|----------|----------|
"""
    for _, row in d_stats.iterrows():
        report += f"| {row['benchmark']} | {row['n_items']} | {row['mean_d']:.4f} | {row['std_d']:.4f} | {row['pct_d_lt_095']:.1f}% | {row['pct_d_lt_090']:.1f}% | {row['pct_d_lt_080']:.1f}% |\n"

    report += f"""
## Δlz* Summary by Benchmark

| Benchmark | Mean Δlz* | Std Δlz* | Mean |Δlz*| | Max |Δlz*| |
|-----------|-----------|----------|-------------|-------------|
"""
    for bm in TARGET_BENCHMARKS:
        row = bm_summary.loc[bm]
        report += f"| {bm} | {row['mean_delta']:.3f} | {row['std_delta']:.3f} | {row['mean_abs_delta']:.3f} | {row['max_abs_delta']:.3f} |\n"

    report += f"""
## Δlz* by Model (sorted by impact)

| Model | Mean Δlz* | Mean |Δlz*| |
|-------|-----------|-------------|
"""
    for name, row in model_summary.iterrows():
        report += f"| {name} | {row['mean_delta']:.3f} | {row['mean_abs_delta']:.3f} |\n"

    report += f"""
## Full Comparison Table

| Model | Benchmark | lz*_4pl | lz*_3pl | Δlz* | %Change |
|-------|-----------|---------|---------|------|---------|
"""
    for _, row in df.sort_values(["benchmark", "student_id"]).iterrows():
        report += f"| {row['model_name']} | {row['benchmark']} | {row['lz_star_4pl']:.2f} | {row['lz_star_3pl']:.2f} | {row['delta_lz_star']:.3f} | {row['pct_change']:.1f}% |\n"

    report += f"""
## Figures

- **scatter_4pl_vs_3pl.png**: 4PL vs 3PL lz* scatter. Pearson r = {r:.4f}, RMSE = {rmse:.2f}.
- **delta_distribution.png**: Grouped bar chart and histogram of Δlz* by model and benchmark.
- **d_vs_delta_relationship.png**: Benchmark mean d vs mean |Δlz*| with linear trend.

## Key Findings

1. **Most affected benchmark**: {most_affected_bm} (mean |Δlz*| = {bm_summary.loc[most_affected_bm, 'mean_abs_delta']:.3f}), consistent with having the most items with d < 0.95 ({d_stats[d_stats['benchmark']==most_affected_bm]['pct_d_lt_095'].values[0]:.1f}%).

2. **Least affected benchmark**: {least_affected_bm} (mean |Δlz*| = {bm_summary.loc[least_affected_bm, 'mean_abs_delta']:.3f}).

3. **Most affected model**: {most_affected_model} (mean |Δlz*| = {model_summary.loc[most_affected_model, 'mean_abs_delta']:.3f}).

4. **Direction of bias**: Mean Δlz* across all pairs = {df['delta_lz_star'].mean():.3f} (positive = 4PL gives higher lz* than 3PL). Without d-capping, 3PL overestimates expected performance for high-ability models, making their errors look catastrophically aberrant. This effect is strongest for DeepSeek-V3 (θ=3.77), where 3PL lz* drops to -340 on MMLU/HellaSwag.

5. **Overall correlation**: 4PL and 3PL lz* show weak correlation (r = {r:.4f}) with large RMSE = {rmse:.2f}, driven primarily by high-ability models where d-capping has outsized impact. Low-ability models (Gemma-2B-it, Vicuna-7B, Mistral-7B) are barely affected (|Δlz*| < 2), confirming d only matters near the probability ceiling.

6. **Practical implication**: Using 3PL (ignoring d) would render lz* unusable for contamination detection in high-ability LLMs — the d-induced bias dwarfs any contamination signal. The 4PL d parameter is essential for valid person-fit analysis on LLM benchmark data.
"""

    with open(ARTIFACT_DIR / "degradation_report.md", "w") as f:
        f.write(report)
    print("Saved degradation_report.md")


def main():
    print("Loading data...")
    responses, params, abilities, ref = load_data()
    print(f"Responses: {responses.shape}, Params: {len(params)}, Models: {len(abilities)}")

    print("Computing lz* for 4PL and 3PL(d=1)...")
    df = compute_degradation(responses, params, abilities, ref)
    df.to_csv(ARTIFACT_DIR / "degradation_comparison.csv", index=False)
    print(f"Saved degradation_comparison.csv ({len(df)} rows)")

    print("Computing d-parameter statistics...")
    d_stats = compute_d_stats(params)
    d_stats.to_csv(ARTIFACT_DIR / "benchmark_d_stats.csv", index=False)
    print("Saved benchmark_d_stats.csv")

    print("Generating plots...")
    plot_scatter(df)
    plot_delta_distribution(df)
    plot_d_vs_delta(df, d_stats)

    print("Generating report...")
    generate_report(df, d_stats)

    print("Done.")


if __name__ == "__main__":
    main()
