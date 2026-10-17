"""Verbosity length confound analysis.

Tests whether verbosity style effect in GEE survives after controlling
for text length — the key rebuttal to "verbose bias = length bias".
"""

import json
import numpy as np
import pandas as pd
import statsmodels.api as sm
from statsmodels.genmod.generalized_estimating_equations import GEE
from statsmodels.genmod.cov_struct import Exchangeable
from statsmodels.genmod.families import Binomial
from pathlib import Path

DATA_DIR = Path(__file__).resolve().parent.parent / "data"
NLI_THRESHOLD = 0.90


def load_jsonl(path):
    records = []
    with open(path) as f:
        for line in f:
            if line.strip():
                records.append(json.loads(line))
    return records


def build_length_lookup(verified_records):
    """Build id -> (len_verbose, len_concise) from verified data."""
    lookup = {}
    for rec in verified_records:
        rid = rec["id"]
        orig_pole = rec.get("original_verbosity")
        orig_text = rec.get("original_text", "")
        cf_text = rec.get("counterfactual_text", "")

        if orig_pole == "verbose":
            len_verbose = len(orig_text)
            len_concise = len(cf_text)
        elif orig_pole == "concise":
            len_verbose = len(cf_text)
            len_concise = len(orig_text)
        else:
            continue

        lookup[rid] = {
            "len_verbose": len_verbose,
            "len_concise": len_concise,
            "len_verbose_words": len(orig_text.split()) if orig_pole == "verbose" else len(cf_text.split()),
            "len_concise_words": len(orig_text.split()) if orig_pole == "concise" else len(cf_text.split()),
        }
    return lookup


def build_dataframe(pairwise_records, length_lookup):
    """Build GEE dataframe with length covariates."""
    rows = []
    pair_idx = 0

    for rec in pairwise_records:
        if not rec.get("trial1_choice") or not rec.get("trial2_choice"):
            continue
        if rec.get("nli_cf", 0) < NLI_THRESHOLD:
            continue

        original_pole = rec.get("original_verbosity")
        if original_pole not in ("verbose", "concise"):
            continue

        rid = rec["id"]
        if rid not in length_lookup:
            continue

        lengths = length_lookup[rid]
        len_verbose = lengths["len_verbose"]
        len_concise = lengths["len_concise"]
        length_ratio = len_verbose / len_concise if len_concise > 0 else 1.0
        length_diff = len_verbose - len_concise
        log_length_ratio = np.log(length_ratio) if length_ratio > 0 else 0.0

        # Trial 1: A=verbose, B=concise
        rows.append({
            "chose_A": 1.0 if rec["trial1_choice"] == "A" else 0.0,
            "is_verbose_in_A": 1.0,
            "is_original_in_A": 1.0 if original_pole == "verbose" else 0.0,
            "length_ratio": length_ratio,
            "length_diff": length_diff,
            "log_length_ratio": log_length_ratio,
            "len_verbose": len_verbose,
            "len_concise": len_concise,
            "pair_id": pair_idx,
        })

        # Trial 2: A=concise, B=verbose
        rows.append({
            "chose_A": 1.0 if rec["trial2_choice"] == "A" else 0.0,
            "is_verbose_in_A": 0.0,
            "is_original_in_A": 1.0 if original_pole == "concise" else 0.0,
            "length_ratio": length_ratio,
            "length_diff": length_diff,
            "log_length_ratio": log_length_ratio,
            "len_verbose": len_verbose,
            "len_concise": len_concise,
            "pair_id": pair_idx,
        })

        pair_idx += 1

    return pd.DataFrame(rows)


def standardize(series):
    """Z-score standardization."""
    m = series.mean()
    s = series.std()
    if s == 0:
        return series - m
    return (series - m) / s


def run_gee_models(df, judge_name):
    """Run 3 GEE models and print comparison table."""
    df = df.copy()
    df["length_ratio_z"] = standardize(df["length_ratio"])
    df["length_diff_z"] = standardize(df["length_diff"])
    df["log_length_ratio_z"] = standardize(df["log_length_ratio"])

    n_pairs = df["pair_id"].nunique()
    n_obs = len(df)

    # Descriptive stats on length
    pair_df = df.drop_duplicates(subset=["pair_id"])
    mean_ratio = pair_df["length_ratio"].mean()
    median_ratio = pair_df["length_ratio"].median()
    mean_diff = pair_df["length_diff"].mean()
    median_diff = pair_df["length_diff"].median()

    print(f"\n--- {judge_name} ---")
    print(f"Pairs: {n_pairs}, Observations: {n_obs}")
    print(f"Length ratio (verbose/concise): mean={mean_ratio:.2f}, median={median_ratio:.2f}")
    print(f"Length diff (verbose-concise): mean={mean_diff:.0f}, median={median_diff:.0f} chars")

    models = [
        ("A: No length", ["is_verbose_in_A", "is_original_in_A"]),
        ("B: + length_ratio", ["is_verbose_in_A", "is_original_in_A", "length_ratio_z"]),
        ("C: + length_diff", ["is_verbose_in_A", "is_original_in_A", "length_diff_z"]),
        ("D: + log_length_ratio", ["is_verbose_in_A", "is_original_in_A", "log_length_ratio_z"]),
    ]

    results = []
    for model_name, cols in models:
        exog = sm.add_constant(df[cols])
        gee = GEE(
            df["chose_A"], exog, groups=df["pair_id"],
            family=Binomial(), cov_struct=Exchangeable(),
        )
        fit = gee.fit()

        row = {"model": model_name}
        for col in cols:
            idx = list(exog.columns).index(col)
            coef = fit.params.iloc[idx]
            p = fit.pvalues.iloc[idx]
            ci = fit.conf_int().iloc[idx]
            or_val = np.exp(coef)
            or_lo = np.exp(ci.iloc[0])
            or_hi = np.exp(ci.iloc[1])

            short = col.replace("is_verbose_in_A", "style") \
                       .replace("is_original_in_A", "orig") \
                       .replace("length_ratio_z", "len_ratio") \
                       .replace("length_diff_z", "len_diff") \
                       .replace("log_length_ratio_z", "log_len_ratio")

            row[f"{short}_OR"] = or_val
            row[f"{short}_CI"] = f"[{or_lo:.2f}, {or_hi:.2f}]"
            row[f"{short}_p"] = p

        results.append(row)

    # Print table
    print(f"\n{'Model':<25} {'Style OR':>10} {'Style 95% CI':>18} {'Style p':>12} {'Orig OR':>10} {'Orig p':>12} {'Length OR':>12} {'Length p':>12}")
    print("-" * 125)

    for r in results:
        style_or = f"{r['style_OR']:.4f}"
        style_ci = r["style_CI"]
        style_p = f"{r['style_p']:.2e}"
        orig_or = f"{r['orig_OR']:.4f}"
        orig_p = f"{r['orig_p']:.2e}"

        # Find length column
        len_or = "—"
        len_p = "—"
        for key in r:
            if key.startswith("len_") and key.endswith("_OR"):
                len_or = f"{r[key]:.4f}"
            if key.startswith("len_") and key.endswith("_p"):
                len_p = f"{r[key]:.2e}"
            if key.startswith("log_len") and key.endswith("_OR"):
                len_or = f"{r[key]:.4f}"
            if key.startswith("log_len") and key.endswith("_p"):
                len_p = f"{r[key]:.2e}"

        print(f"{r['model']:<25} {style_or:>10} {style_ci:>18} {style_p:>12} {orig_or:>10} {orig_p:>12} {len_or:>12} {len_p:>12}")

    # Change analysis
    baseline_or = results[0]["style_OR"]
    print(f"\nStyle OR change from baseline ({baseline_or:.4f}):")
    for r in results[1:]:
        pct = (r["style_OR"] - baseline_or) / baseline_or * 100
        sig = "YES" if r["style_p"] < 0.05 else "NO"
        print(f"  {r['model']}: OR={r['style_OR']:.4f} (Δ={pct:+.1f}%), still significant: {sig} (p={r['style_p']:.2e})")

    return results


def main():
    print("=" * 70)
    print("  Verbosity Length Confound Analysis")
    print("  Does style effect survive after controlling for text length?")
    print("=" * 70)

    verified = load_jsonl(DATA_DIR / "verified_verbosity.jsonl")
    length_lookup = build_length_lookup(verified)
    print(f"\nVerified records with length data: {len(length_lookup)}")

    # Descriptive: overall length distribution
    all_ratios = [v["len_verbose"] / v["len_concise"] for v in length_lookup.values() if v["len_concise"] > 0]
    all_diffs = [v["len_verbose"] - v["len_concise"] for v in length_lookup.values()]
    print(f"Overall verbose/concise ratio: mean={np.mean(all_ratios):.2f}, std={np.std(all_ratios):.2f}, range=[{np.min(all_ratios):.2f}, {np.max(all_ratios):.2f}]")
    print(f"Overall length diff (chars): mean={np.mean(all_diffs):.0f}, std={np.std(all_diffs):.0f}")

    all_results = {}

    for judge_name, filename in [
        ("Qwen3-32B", "pairwise_results_qwen32b_verbosity.jsonl"),
        ("GPT-4o", "pairwise_results_gpt4o_verbosity.jsonl"),
    ]:
        pairwise = load_jsonl(DATA_DIR / filename)
        df = build_dataframe(pairwise, length_lookup)
        if len(df) == 0:
            print(f"\n--- {judge_name} --- NO DATA after filtering")
            continue
        all_results[judge_name] = run_gee_models(df, judge_name)

    # Conclusion
    print(f"\n{'=' * 70}")
    print("  CONCLUSION")
    print(f"{'=' * 70}")

    for judge_name, results in all_results.items():
        baseline = results[0]
        survived = all(r["style_p"] < 0.05 for r in results[1:])
        max_drop = max(
            abs(r["style_OR"] - baseline["style_OR"]) / baseline["style_OR"] * 100
            for r in results[1:]
        )
        if survived:
            print(f"\n{judge_name}: Style effect SURVIVES length control.")
            print(f"  Max OR change: {max_drop:.1f}%. Verbosity bias is NOT reducible to length bias.")
        else:
            print(f"\n{judge_name}: Style effect does NOT survive length control.")
            print(f"  Verbosity finding may be confounded by length.")


if __name__ == "__main__":
    main()
