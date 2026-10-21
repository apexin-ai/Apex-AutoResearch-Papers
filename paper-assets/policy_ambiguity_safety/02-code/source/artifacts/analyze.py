#!/usr/bin/env python3
"""Statistical analysis module for policy ambiguity safety experiments.

Implements the dual-track analysis (D004):
  Primary: ambiguous-only cross-type comparison (χ², pairwise Fisher, Cramér's V)
  Secondary: matched-pair within-type effect sizes (McNemar / Wilcoxon)
"""

import argparse
import json
import sys
from collections import defaultdict
from pathlib import Path

import numpy as np
import pandas as pd
from scipy import stats

import config

# ---------------------------------------------------------------------------
# Data loading
# ---------------------------------------------------------------------------

def load_judgments(judgments_dir: Path) -> pd.DataFrame:
    records = []
    for jsonl_file in judgments_dir.glob("*.jsonl"):
        with open(jsonl_file) as f:
            for line in f:
                if not line.strip():
                    continue
                rec = json.loads(line)
                flat = {
                    "episode_id": rec["episode_id"],
                    "clause_id": rec["clause_id"],
                    "ambiguity_type": rec["ambiguity_type"],
                    "condition": rec["condition"],
                    "model": rec["model"],
                    "violation_level": rec["judgment"]["violation_level"],
                    "confidence": rec["judgment"]["confidence"],
                }
                records.append(flat)
    df = pd.DataFrame(records)
    if df.empty:
        return df
    level_order = pd.CategoricalDtype(categories=config.VIOLATION_LEVELS, ordered=True)
    df["violation_level"] = df["violation_level"].astype(level_order)
    return df


def load_clauses(path: str) -> pd.DataFrame:
    with open(path) as f:
        raw = json.load(f)
    clause_list = raw if isinstance(raw, list) else raw.get("clauses", raw)
    return pd.DataFrame(clause_list)


def binarize_violations(df: pd.DataFrame) -> pd.Series:
    """Convert violation levels to binary (moderate+ = 1)."""
    threshold_idx = config.VIOLATION_LEVELS.index(config.VIOLATION_BINARY_THRESHOLD)
    return df["violation_level"].cat.codes >= threshold_idx


# ---------------------------------------------------------------------------
# Primary analysis: ambiguous-only cross-type comparison
# ---------------------------------------------------------------------------

def cramers_v(contingency_table: np.ndarray) -> float:
    chi2 = stats.chi2_contingency(contingency_table)[0]
    n = contingency_table.sum()
    min_dim = min(contingency_table.shape) - 1
    if min_dim == 0 or n == 0:
        return 0.0
    return np.sqrt(chi2 / (n * min_dim))


def primary_analysis(df: pd.DataFrame, alpha: float) -> dict:
    """Ambiguous-only cross-type comparison."""
    amb = df[df["condition"] == "ambiguous"].copy()
    if amb.empty:
        return {"error": "No ambiguous episodes found"}

    amb["violated"] = binarize_violations(amb)

    type_rates = amb.groupby("ambiguity_type")["violated"].agg(["mean", "sum", "count"])
    type_rates.columns = ["violation_rate", "n_violations", "n_total"]

    # χ² omnibus test (3×2 contingency: type × violated)
    contingency = pd.crosstab(amb["ambiguity_type"], amb["violated"])
    ct_array = contingency.values
    if ct_array.shape[0] < 2 or ct_array.shape[1] < 2:
        omnibus = {"chi2": np.nan, "p": 1.0, "dof": 0}
    else:
        chi2_stat, p_val, dof, _ = stats.chi2_contingency(ct_array)
        omnibus = {"chi2": float(chi2_stat), "p": float(p_val), "dof": int(dof)}

    # Pairwise Fisher exact tests + Bonferroni + Cramér's V
    types = sorted(amb["ambiguity_type"].unique())
    n_pairs = len(types) * (len(types) - 1) // 2
    pairwise = []
    for i in range(len(types)):
        for j in range(i + 1, len(types)):
            t1, t2 = types[i], types[j]
            sub = amb[amb["ambiguity_type"].isin([t1, t2])]
            pair_ct = pd.crosstab(sub["ambiguity_type"], sub["violated"]).values
            if pair_ct.shape == (2, 2):
                _, fisher_p = stats.fisher_exact(pair_ct)
                v = cramers_v(pair_ct)
            else:
                fisher_p = 1.0
                v = 0.0
            pairwise.append({
                "type_1": t1,
                "type_2": t2,
                "fisher_p": float(fisher_p),
                "bonferroni_p": float(min(fisher_p * n_pairs, 1.0)),
                "cramers_v": float(v),
            })

    # Per-model breakdown
    model_results = {}
    for model_name, model_df in amb.groupby("model"):
        model_type_rates = model_df.groupby("ambiguity_type")["violated"].agg(["mean", "sum", "count"])
        model_type_rates.columns = ["violation_rate", "n_violations", "n_total"]
        model_results[model_name] = model_type_rates.to_dict(orient="index")

    return {
        "overall_rates": type_rates.to_dict(orient="index"),
        "omnibus_chi2": omnibus,
        "pairwise": pairwise,
        "per_model": model_results,
    }


# ---------------------------------------------------------------------------
# Secondary analysis: matched-pair within-type effect
# ---------------------------------------------------------------------------

def secondary_analysis(df: pd.DataFrame, alpha: float) -> dict:
    """Matched-pair within-type: ambiguous vs unambiguous per type."""
    df = df.copy()
    df["violated"] = binarize_violations(df)

    results = {}
    for atype in config.AMBIGUITY_TYPES:
        type_df = df[df["ambiguity_type"] == atype]
        if type_df.empty:
            continue

        amb = type_df[type_df["condition"] == "ambiguous"]
        unamb = type_df[type_df["condition"] == "unambiguous"]

        amb_rate = amb["violated"].mean() if len(amb) > 0 else np.nan
        unamb_rate = unamb["violated"].mean() if len(unamb) > 0 else np.nan

        # Match by clause_id + model for paired test
        merged = pd.merge(
            amb[["clause_id", "model", "violated"]],
            unamb[["clause_id", "model", "violated"]],
            on=["clause_id", "model"],
            suffixes=("_amb", "_unamb"),
        )

        if len(merged) >= 5:
            # McNemar test for paired binary data
            b = ((merged["violated_amb"]) & (~merged["violated_unamb"])).sum()  # amb=1, unamb=0
            c = ((~merged["violated_amb"]) & (merged["violated_unamb"])).sum()  # amb=0, unamb=1

            if b + c > 0:
                mcnemar_stat = (abs(b - c) - 1) ** 2 / (b + c) if (b + c) >= 25 else np.nan
                mcnemar_p = stats.binomtest(b, b + c, 0.5).pvalue if (b + c) < 25 else float(1 - stats.chi2.cdf(mcnemar_stat, 1))
            else:
                mcnemar_stat = 0.0
                mcnemar_p = 1.0

            # Wilcoxon signed-rank on violation level codes
            amb_levels = pd.merge(
                amb[["clause_id", "model", "violation_level"]],
                unamb[["clause_id", "model", "violation_level"]],
                on=["clause_id", "model"],
                suffixes=("_amb", "_unamb"),
            )
            diff = amb_levels["violation_level_amb"].cat.codes - amb_levels["violation_level_unamb"].cat.codes
            nonzero_diff = diff[diff != 0]
            if len(nonzero_diff) >= 5:
                wilcoxon_stat, wilcoxon_p = stats.wilcoxon(nonzero_diff)
            else:
                wilcoxon_stat, wilcoxon_p = np.nan, np.nan
        else:
            mcnemar_stat, mcnemar_p = np.nan, np.nan
            wilcoxon_stat, wilcoxon_p = np.nan, np.nan
            b, c = np.nan, np.nan

        results[atype] = {
            "ambiguous_violation_rate": float(amb_rate) if not np.isnan(amb_rate) else None,
            "unambiguous_violation_rate": float(unamb_rate) if not np.isnan(unamb_rate) else None,
            "rate_difference": float(amb_rate - unamb_rate) if not (np.isnan(amb_rate) or np.isnan(unamb_rate)) else None,
            "n_pairs": int(len(merged)) if isinstance(merged, pd.DataFrame) else 0,
            "mcnemar": {
                "b_amb_only": int(b) if not np.isnan(b) else None,
                "c_unamb_only": int(c) if not np.isnan(c) else None,
                "statistic": float(mcnemar_stat) if not np.isnan(mcnemar_stat) else None,
                "p": float(mcnemar_p) if not np.isnan(mcnemar_p) else None,
            },
            "wilcoxon": {
                "statistic": float(wilcoxon_stat) if not np.isnan(wilcoxon_stat) else None,
                "p": float(wilcoxon_p) if not np.isnan(wilcoxon_p) else None,
            },
        }

    return results


# ---------------------------------------------------------------------------
# Pass / Fail judgment
# ---------------------------------------------------------------------------

def pass_fail_judgment(primary: dict, alpha: float, min_v: float) -> dict:
    omnibus_p = primary.get("omnibus_chi2", {}).get("p", 1.0)
    if np.isnan(omnibus_p):
        omnibus_p = 1.0

    omnibus_sig = omnibus_p < alpha

    pairwise = primary.get("pairwise", [])
    any_v_above = any(pw["cramers_v"] >= min_v for pw in pairwise)
    sig_pairs = [
        pw for pw in pairwise
        if pw["bonferroni_p"] < alpha and pw["cramers_v"] >= min_v
    ]

    passed = omnibus_sig and any_v_above

    reasons = []
    reasons.append(
        f"Omnibus χ² p={omnibus_p:.4f} {'<' if omnibus_sig else '>='} α={alpha} → {'PASS' if omnibus_sig else 'FAIL'}"
    )
    if pairwise:
        max_v_pair = max(pairwise, key=lambda pw: pw["cramers_v"])
        reasons.append(
            f"Max Cramér's V={max_v_pair['cramers_v']:.3f} ({max_v_pair['type_1']} vs {max_v_pair['type_2']}) "
            f"{'≥' if max_v_pair['cramers_v'] >= min_v else '<'} {min_v} → {'PASS' if any_v_above else 'FAIL'}"
        )
    else:
        reasons.append("No pairwise comparisons available → FAIL")

    if sig_pairs:
        for sp in sig_pairs:
            reasons.append(
                f"  Significant pair: {sp['type_1']} vs {sp['type_2']} "
                f"(V={sp['cramers_v']:.3f}, p_bonf={sp['bonferroni_p']:.4f})"
            )

    return {
        "pass": passed,
        "omnibus_significant": omnibus_sig,
        "any_v_above_threshold": any_v_above,
        "n_significant_pairs": len(sig_pairs),
        "reasons": reasons,
    }


# ---------------------------------------------------------------------------
# Per-clause summary CSV
# ---------------------------------------------------------------------------

def per_clause_summary(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df["violated"] = binarize_violations(df)
    summary = df.groupby(["clause_id", "ambiguity_type", "condition", "model"]).agg(
        violation_rate=("violated", "mean"),
        n_episodes=("violated", "count"),
        n_violations=("violated", "sum"),
        modal_level=("violation_level", lambda x: x.mode().iloc[0] if len(x) > 0 else "none"),
    ).reset_index()
    return summary


# ---------------------------------------------------------------------------
# Console report
# ---------------------------------------------------------------------------

def print_report(primary: dict, secondary: dict, judgment: dict):
    print("\n" + "=" * 70)
    print("POLICY AMBIGUITY SAFETY — STATISTICAL ANALYSIS REPORT")
    print("=" * 70)
    print("\n  [Cross-judge design: Claude episodes judged by GPT, GPT episodes judged by Claude]")

    print("\n── PRIMARY ANALYSIS: Ambiguous-only Cross-type Comparison ──\n")
    rates = primary.get("overall_rates", {})
    if rates:
        print(f"  {'Type':<20} {'Violation Rate':>15} {'N violations':>13} {'N total':>10}")
        print(f"  {'-'*20} {'-'*15} {'-'*13} {'-'*10}")
        for atype in config.AMBIGUITY_TYPES:
            if atype in rates:
                r = rates[atype]
                print(f"  {atype:<20} {r['violation_rate']:>14.1%} {r['n_violations']:>13.0f} {r['n_total']:>10.0f}")

    omnibus = primary.get("omnibus_chi2", {})
    print(f"\n  Omnibus χ²: {omnibus.get('chi2', 'N/A'):.3f}, p = {omnibus.get('p', 'N/A'):.4f}, dof = {omnibus.get('dof', 'N/A')}")

    print(f"\n  {'Pair':<35} {'Fisher p':>10} {'Bonf. p':>10} {'Cramér V':>10}")
    print(f"  {'-'*35} {'-'*10} {'-'*10} {'-'*10}")
    for pw in primary.get("pairwise", []):
        pair_label = f"{pw['type_1']} vs {pw['type_2']}"
        print(f"  {pair_label:<35} {pw['fisher_p']:>10.4f} {pw['bonferroni_p']:>10.4f} {pw['cramers_v']:>10.3f}")

    print("\n── SECONDARY ANALYSIS: Within-type Matched-pair Effects ──\n")
    for atype in config.AMBIGUITY_TYPES:
        if atype in secondary:
            s = secondary[atype]
            amb_r = s.get("ambiguous_violation_rate")
            unamb_r = s.get("unambiguous_violation_rate")
            diff = s.get("rate_difference")
            print(f"  {atype}:")
            print(f"    Ambiguous: {amb_r:.1%}  Unambiguous: {unamb_r:.1%}  Δ = {diff:+.1%}" if diff is not None else f"    Insufficient data")
            mcn = s.get("mcnemar", {})
            if mcn.get("p") is not None:
                print(f"    McNemar p = {mcn['p']:.4f} (b={mcn['b_amb_only']}, c={mcn['c_unamb_only']})")
            wlc = s.get("wilcoxon", {})
            if wlc.get("p") is not None:
                print(f"    Wilcoxon p = {wlc['p']:.4f}")
            print()

    print("── PASS / FAIL JUDGMENT ──\n")
    verdict = "PASS ✓" if judgment["pass"] else "FAIL ✗"
    print(f"  Result: {verdict}\n")
    for reason in judgment.get("reasons", []):
        print(f"  {reason}")
    print("\n" + "=" * 70)


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Statistical analysis of policy ambiguity safety experiment results."
    )
    parser.add_argument(
        "--judgments", required=True,
        help="Directory containing judgment JSONL files from judge.py.",
    )
    parser.add_argument(
        "--clauses", required=True,
        help="Path to clauses JSON file.",
    )
    parser.add_argument(
        "--output", default=str(config.DEFAULT_ANALYSIS_DIR),
        help="Output directory for analysis results.",
    )
    parser.add_argument(
        "--alpha", type=float, default=config.DEFAULT_ALPHA,
        help=f"Significance level (default: {config.DEFAULT_ALPHA}).",
    )
    parser.add_argument(
        "--min-v", type=float, default=config.DEFAULT_MIN_V,
        help=f"Minimum Cramér's V for practical significance (default: {config.DEFAULT_MIN_V}).",
    )
    return parser.parse_args(argv)


def main(argv: list[str] | None = None):
    args = parse_args(argv)

    df = load_judgments(Path(args.judgments))
    if df.empty:
        print(f"No judgments found in {args.judgments}")
        sys.exit(1)

    output_dir = Path(args.output)
    output_dir.mkdir(parents=True, exist_ok=True)

    # Run analyses
    primary = primary_analysis(df, args.alpha)
    secondary = secondary_analysis(df, args.alpha)
    judgment = pass_fail_judgment(primary, args.alpha, args.min_v)

    # Write outputs
    summary_df = per_clause_summary(df)
    summary_df.to_csv(output_dir / "results_summary.csv", index=False)

    with open(output_dir / "statistics_report.json", "w") as f:
        json.dump({"primary": primary, "secondary": secondary}, f, indent=2, default=str)

    with open(output_dir / "pass_fail_judgment.json", "w") as f:
        json.dump(judgment, f, indent=2)

    # Console report
    print_report(primary, secondary, judgment)

    print(f"\nOutputs written to {output_dir}/")
    print(f"  - results_summary.csv")
    print(f"  - statistics_report.json")
    print(f"  - pass_fail_judgment.json")


if __name__ == "__main__":
    main()
