from __future__ import annotations
"""ATE (Average Treatment Effect) analysis for style bias quantification.

Supports multiple style axes: formality (formal/casual), verbosity (verbose/concise).
ATE = score(pole_a) - score(pole_b), where pole_a is the expected-preferred pole.

Input:  scored.jsonl (with score_original, score_counterfactual, score_double_rewrite)
Output: CSV summary + visualizations (ATE bar chart, score violin plot)
Deps:   scipy, pandas, numpy, matplotlib, seaborn
"""

import argparse
import json
import os

AXIS_CONFIG = {
    "formality": {"poles": ("formal", "casual"), "field": "original_formality"},
    "verbosity": {"poles": ("verbose", "concise"), "field": "original_verbosity"},
    "tone": {"poles": ("assertive", "hedging"), "field": "original_tone"},
    "rate_control": {"poles": ("original", "rewritten"), "field": "rate_role"},
    "register": {"poles": ("academic", "conversational"), "field": "original_register"},
}

_AXIS = "formality"


def load_scored(path: str) -> pd.DataFrame:
    records = []
    with open(path) as f:
        for line in f:
            if line.strip():
                records.append(json.loads(line))
    df = pd.DataFrame(records)
    # Drop rows with missing scores
    for col in ["score_original", "score_counterfactual", "score_double_rewrite"]:
        df = df[df[col].notna()]
    df["score_original"] = df["score_original"].astype(float)
    df["score_counterfactual"] = df["score_counterfactual"].astype(float)
    df["score_double_rewrite"] = df["score_double_rewrite"].astype(float)
    return df


def compute_ate(df: pd.DataFrame, alpha: float = 0.05) -> dict:
    """ATE as style premium: score(pole_a) - score(pole_b)."""
    cfg = AXIS_CONFIG[_AXIS]
    pole_b = cfg["poles"][1]
    field = cfg["field"]
    is_pole_b = (df[field] == pole_b).values

    score_formal = np.where(is_pole_b, df["score_counterfactual"].values, df["score_original"].values)
    score_casual = np.where(is_pole_b, df["score_original"].values, df["score_counterfactual"].values)
    diff = pd.Series(score_formal - score_casual, index=df.index)

    n = len(diff)
    raw_ate = diff.mean()
    raw_se = diff.std(ddof=1) / np.sqrt(n)
    t_crit = stats.t.ppf(1 - alpha / 2, df=n - 1)
    raw_ci = (raw_ate - t_crit * raw_se, raw_ate + t_crit * raw_se)
    _, p_val = stats.ttest_1samp(diff, 0)
    cohens_d = raw_ate / diff.std(ddof=1) if diff.std(ddof=1) > 0 else 0.0

    # RATE correction: flip rewrite bias for pole_a originals so direction matches
    raw_rewrite_bias = (df["score_double_rewrite"] - df["score_original"]).values
    rewrite_bias_vec = pd.Series(np.where(is_pole_b, raw_rewrite_bias, -raw_rewrite_bias), index=df.index)
    rewrite_bias = rewrite_bias_vec.mean()
    corrected_ate = raw_ate - rewrite_bias

    corrected_diff = diff - rewrite_bias_vec
    corrected_se = corrected_diff.std(ddof=1) / np.sqrt(n)
    corrected_ci = (corrected_ate - t_crit * corrected_se, corrected_ate + t_crit * corrected_se)
    _, p_corr = stats.ttest_1samp(corrected_diff, 0)
    cohens_d_corr = corrected_ate / corrected_diff.std(ddof=1) if corrected_diff.std(ddof=1) > 0 else 0.0

    return {
        "n": n,
        "raw_ate": raw_ate,
        "raw_se": raw_se,
        "raw_ci_lo": raw_ci[0],
        "raw_ci_hi": raw_ci[1],
        "raw_p": p_val,
        "raw_cohens_d": cohens_d,
        "rewrite_bias": rewrite_bias,
        "corrected_ate": corrected_ate,
        "corrected_se": corrected_se,
        "corrected_ci_lo": corrected_ci[0],
        "corrected_ci_hi": corrected_ci[1],
        "corrected_p": p_corr,
        "corrected_cohens_d": cohens_d_corr,
    }


def directional_analysis(df: pd.DataFrame, alpha: float) -> pd.DataFrame:
    cfg = AXIS_CONFIG[_AXIS]
    pole_a, pole_b = cfg["poles"]
    field = cfg["field"]
    rows = []
    for direction in [pole_a, pole_b]:
        sub = df[df[field] == direction]
        if len(sub) < 2:
            continue
        result = compute_ate(sub, alpha)
        target = pole_b if direction == pole_a else pole_a
        result["direction"] = f"{direction}→{target}"
        rows.append(result)
    return pd.DataFrame(rows)


def plot_ate_bar(results: dict, dir_df: pd.DataFrame, output_dir: str):
    fig, ax = plt.subplots(figsize=(8, 5))

    labels = ["Overall (raw)", "Overall (corrected)"]
    ates = [results["raw_ate"], results["corrected_ate"]]
    errors = [
        [results["raw_ate"] - results["raw_ci_lo"]],
        [results["corrected_ate"] - results["corrected_ci_lo"]],
    ]
    errors_hi = [
        [results["raw_ci_hi"] - results["raw_ate"]],
        [results["corrected_ci_hi"] - results["corrected_ate"]],
    ]

    for _, row in dir_df.iterrows():
        labels.append(row["direction"])
        ates.append(row["corrected_ate"])
        errors.append([row["corrected_ate"] - row["corrected_ci_lo"]])
        errors_hi.append([row["corrected_ci_hi"] - row["corrected_ate"]])

    err_lo = [e[0] for e in errors]
    err_hi = [e[0] for e in errors_hi]

    x = np.arange(len(labels))
    colors = ["#4C72B0", "#DD8452"] + ["#55A868"] * len(dir_df)
    ax.barh(x, ates, xerr=[err_lo, err_hi], color=colors[:len(labels)], capsize=4, height=0.6)
    ax.axvline(0, color="black", linewidth=0.8, linestyle="--")
    ax.set_yticks(x)
    ax.set_yticklabels(labels)
    ax.set_xlabel("ATE (score difference)")
    ax.set_title("Style Bias: Average Treatment Effect")
    plt.tight_layout()
    fig.savefig(os.path.join(output_dir, "ate_bar.png"), dpi=150)
    plt.close(fig)


def plot_score_violin(df: pd.DataFrame, output_dir: str):
    fig, ax = plt.subplots(figsize=(8, 5))

    plot_data = pd.DataFrame({
        "Score": pd.concat([df["score_original"], df["score_counterfactual"]], ignore_index=True),
        "Version": ["Original"] * len(df) + ["Counterfactual"] * len(df),
    })

    sns.violinplot(data=plot_data, x="Version", y="Score", ax=ax, inner="box", palette="Set2")
    ax.set_title("Score Distribution: Original vs Counterfactual")
    ax.set_ylim(0.5, 10.5)
    plt.tight_layout()
    fig.savefig(os.path.join(output_dir, "score_violin.png"), dpi=150)
    plt.close(fig)


def run_analysis(df: pd.DataFrame, alpha: float, output_dir: str, prefix: str = "ate"):
    """Run full ATE analysis pipeline on a dataframe and save results."""
    os.makedirs(output_dir, exist_ok=True)

    results = compute_ate(df, alpha)

    print(f"\n{'='*60}")
    print(f"  Overall ATE Analysis — {prefix}")
    print(f"{'='*60}")
    print(f"  N = {results['n']}")
    print(f"  Raw ATE          = {results['raw_ate']:+.4f}  (SE={results['raw_se']:.4f})")
    print(f"  Raw 95% CI       = [{results['raw_ci_lo']:+.4f}, {results['raw_ci_hi']:+.4f}]")
    print(f"  Raw p-value      = {results['raw_p']:.6f}")
    print(f"  Raw Cohen's d    = {results['raw_cohens_d']:+.4f}")
    print(f"  Rewrite bias     = {results['rewrite_bias']:+.4f}")
    print(f"  Corrected ATE    = {results['corrected_ate']:+.4f}  (SE={results['corrected_se']:.4f})")
    print(f"  Corrected 95% CI = [{results['corrected_ci_lo']:+.4f}, {results['corrected_ci_hi']:+.4f}]")
    print(f"  Corrected p      = {results['corrected_p']:.6f}")
    print(f"  Corrected d      = {results['corrected_cohens_d']:+.4f}")

    dir_df = directional_analysis(df, alpha)
    if not dir_df.empty:
        print(f"\n{'='*60}")
        print("  Directional Analysis")
        print(f"{'='*60}")
        for _, row in dir_df.iterrows():
            print(f"\n  {row['direction']}  (n={row['n']})")
            print(f"    Corrected ATE = {row['corrected_ate']:+.4f}, p = {row['corrected_p']:.6f}, d = {row['corrected_cohens_d']:+.4f}")

    strat_rows = []
    if "nli_cf" in df.columns:
        nli_sub = df[df["nli_cf"] >= 0.90]
        label = "primary: nli_cf≥0.90 (n={})".format(len(nli_sub))
        if len(nli_sub) >= 3:
            nli_result = compute_ate(nli_sub, alpha)
            nli_result["group"] = label
            strat_rows.append(nli_result)

    if "bertscore_cf" in df.columns:
        for bs_thresh in [0.85, 0.88, 0.90, 0.92]:
            sub = df[df["bertscore_cf"] >= bs_thresh]
            label = "secondary: bertscore_cf≥{:.2f} (n={})".format(bs_thresh, len(sub))
            if len(sub) >= 3:
                bs_result = compute_ate(sub, alpha)
                bs_result["group"] = label
                strat_rows.append(bs_result)

    all_label = "tertiary: all (n={})".format(len(df))
    all_result = compute_ate(df, alpha)
    all_result["group"] = all_label
    strat_rows.append(all_result)

    print(f"\n{'='*60}")
    print("  Stratified Analysis")
    print(f"{'='*60}")
    for row in strat_rows:
        print(f"  {row['group']}: ATE={row['corrected_ate']:+.4f}, p={row['corrected_p']:.6f}, d={row['corrected_cohens_d']:+.4f}")

    summary_rows = [{"group": "overall", **results}]
    for _, row in dir_df.iterrows():
        summary_rows.append({"group": row["direction"], **row.to_dict()})
    for row in strat_rows:
        summary_rows.append(row)
    summary_df = pd.DataFrame(summary_rows)
    csv_path = os.path.join(output_dir, f"{prefix}_summary.csv")
    summary_df.to_csv(csv_path, index=False)
    print(f"\nSaved summary to {csv_path}")

    plot_ate_bar(results, dir_df, output_dir)
    plot_score_violin(df, output_dir)
    print(f"Saved plots to {output_dir}/")

    return results, dir_df, strat_rows


def winsorize_score_diff(df: pd.DataFrame, sigma: float = 3.0) -> pd.DataFrame:
    """Winsorize the pole_a-pole_b score difference at ±sigma standard deviations."""
    cfg = AXIS_CONFIG[_AXIS]
    pole_b = cfg["poles"][1]
    field = cfg["field"]
    df = df.copy()
    is_pole_b = (df[field] == pole_b).values
    score_formal = np.where(is_pole_b, df["score_counterfactual"].values, df["score_original"].values)
    score_casual = np.where(is_pole_b, df["score_original"].values, df["score_counterfactual"].values)
    diff = score_formal - score_casual

    mu, sd = diff.mean(), diff.std(ddof=1)
    lo, hi = mu - sigma * sd, mu + sigma * sd
    clipped = np.clip(diff, lo, hi)
    n_clipped = int(np.sum((diff < lo) | (diff > hi)))
    print(f"  Winsorize at {sigma}σ: bounds=[{lo:+.2f}, {hi:+.2f}], clipped {n_clipped} values")

    new_formal = score_casual + clipped
    df.loc[is_pole_b, "score_counterfactual"] = new_formal[is_pole_b]
    df.loc[~is_pole_b, "score_original"] = new_formal[~is_pole_b]

    # Also winsorize double_rewrite diff
    dr_diff = df["score_double_rewrite"].values - df["score_original"].values
    dr_mu, dr_sd = dr_diff.mean(), dr_diff.std(ddof=1)
    dr_lo, dr_hi = dr_mu - sigma * dr_sd, dr_mu + sigma * dr_sd
    dr_clipped = np.clip(dr_diff, dr_lo, dr_hi)
    df["score_double_rewrite"] = df["score_original"].values + dr_clipped

    return df


def main():
    parser = argparse.ArgumentParser(description="ATE analysis for style bias")
    parser.add_argument("--input-file", required=True)
    parser.add_argument("--output-dir", required=True)
    parser.add_argument("--alpha", type=float, default=0.05)
    parser.add_argument("--sensitivity", action="store_true",
                        help="Run pre-registered sensitivity analyses (primary + sens1 + sens2)")
    parser.add_argument("--axis", default="formality", choices=list(AXIS_CONFIG.keys()),
                        help="Style axis (default: formality)")
    args = parser.parse_args()

    global _AXIS
    _AXIS = args.axis

    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    import numpy as np
    import pandas as pd
    import seaborn as sns
    from scipy import stats

    for name, obj in [("pd", pd), ("np", np), ("stats", stats), ("plt", plt), ("sns", sns)]:
        globals()[name] = obj

    os.makedirs(args.output_dir, exist_ok=True)

    df = load_scored(args.input_file)
    print(f"Loaded {len(df)} scored records")

    if not args.sensitivity:
        run_analysis(df, args.alpha, args.output_dir, prefix="ate")
    else:
        # Pre-registered exclusion protocol: 3 analysis sets
        # Primary: NLI ≥ 0.90, no exclusion
        if "nli_cf" in df.columns:
            df_primary = df[df["nli_cf"] >= 0.90].copy()
        else:
            df_primary = df.copy()
        print(f"\n{'#'*60}")
        print(f"  PRIMARY ANALYSIS (NLI≥0.90, n={len(df_primary)})")
        print(f"{'#'*60}")
        run_analysis(df_primary, args.alpha, args.output_dir, prefix="ate_primary")

        # Sensitivity 1: primary + exclude NLI < 0.50
        if "nli_cf" in df.columns:
            df_sens1 = df[(df["nli_cf"] >= 0.90) & (df["nli_cf"] >= 0.50)].copy()
        else:
            df_sens1 = df_primary.copy()
        print(f"\n{'#'*60}")
        print(f"  SENSITIVITY 1: exclude NLI<0.50 (n={len(df_sens1)})")
        print(f"{'#'*60}")
        run_analysis(df_sens1, args.alpha, args.output_dir, prefix="ate_sens1")

        # Sensitivity 2: primary + winsorize score_diff at 3σ
        df_sens2 = winsorize_score_diff(df_primary, sigma=3.0)
        print(f"\n{'#'*60}")
        print(f"  SENSITIVITY 2: winsorize at 3σ (n={len(df_sens2)})")
        print(f"{'#'*60}")
        run_analysis(df_sens2, args.alpha, args.output_dir, prefix="ate_sens2")

        # Also run on ALL records for reference
        print(f"\n{'#'*60}")
        print(f"  REFERENCE: all records (n={len(df)})")
        print(f"{'#'*60}")
        run_analysis(df, args.alpha, args.output_dir, prefix="ate_all")


if __name__ == "__main__":
    main()
