#!/usr/bin/env python3
"""2×2 Factorial ANOVA for OCC auxiliary head ablation study.

Factors:
  A (gradient_flow): Full OCC (ON) vs Detach (OFF)
  B (norm_type): BatchNorm vs LayerNorm

DV: CAR (Collision Avoidance Rate, 0-1)
"""

import argparse
import json
import sys
import warnings
from pathlib import Path

import numpy as np
from scipy import stats
from statsmodels.stats.anova import AnovaRM
from statsmodels.stats.multicomp import pairwise_tukeyhsd
import statsmodels.api as sm
from statsmodels.formula.api import ols


def load_data(args):
    if args.json:
        data = json.loads(args.json)
    elif args.input:
        with open(args.input) as f:
            data = json.load(f)
    else:
        print("ERROR: provide --json or --input", file=sys.stderr)
        sys.exit(1)

    required = {"full_occ_bn", "full_occ_ln", "detach_bn", "detach_ln"}
    missing = required - set(data.keys())
    if missing:
        print(f"ERROR: missing keys: {missing}", file=sys.stderr)
        sys.exit(1)

    return data


def build_long_format(data):
    rows = []
    mapping = {
        "full_occ_bn": ("ON", "BN"),
        "full_occ_ln": ("ON", "LN"),
        "detach_bn": ("OFF", "BN"),
        "detach_ln": ("OFF", "LN"),
    }
    for key, (grad, norm) in mapping.items():
        for val in data[key]:
            rows.append({
                "gradient_flow": grad,
                "norm_type": norm,
                "car": float(val),
            })
    return rows


def run_anova(rows):
    import pandas as pd

    df = pd.DataFrame(rows)

    model = ols("car ~ C(gradient_flow) * C(norm_type)", data=df).fit()
    anova_table = sm.stats.anova_lm(model, typ=2)

    ss = anova_table["sum_sq"]
    ss_resid = ss["Residual"]

    results = {}
    for effect, label in [
        ("C(gradient_flow)", "gradient_flow"),
        ("C(norm_type)", "norm_type"),
        ("C(gradient_flow):C(norm_type)", "interaction"),
    ]:
        row = anova_table.loc[effect]
        eta_sq = row["sum_sq"] / (row["sum_sq"] + ss_resid)
        results[label] = {
            "F": float(row["F"]),
            "p": float(row["PR(>F)"]),
            "df": float(row["df"]),
            "SS": float(row["sum_sq"]),
            "partial_eta_squared": float(eta_sq),
        }

    results["residual"] = {
        "df": float(anova_table.loc["Residual", "df"]),
        "SS": float(ss_resid),
    }

    return results, df


def run_tukey(df):
    df = df.copy()
    df["cell"] = df["gradient_flow"] + "_" + df["norm_type"]
    tukey = pairwise_tukeyhsd(df["car"], df["cell"], alpha=0.05)

    comparisons = []
    for i in range(len(tukey.summary().data) - 1):
        row = tukey.summary().data[i + 1]
        comparisons.append({
            "group1": str(row[0]),
            "group2": str(row[1]),
            "meandiff": float(row[2]),
            "p_adj": float(row[3]),
            "lower": float(row[4]),
            "upper": float(row[5]),
            "reject": bool(row[6]),
        })
    return comparisons


def descriptive_stats(data):
    cell_stats = {}
    for key, values in data.items():
        arr = np.array(values, dtype=float)
        cell_stats[key] = {
            "mean": float(np.mean(arr)),
            "std": float(np.std(arr, ddof=1)) if len(arr) > 1 else 0.0,
            "n": len(arr),
        }
    return cell_stats


def decision_helper(anova_results):
    lines = []
    alpha = 0.05

    p_int = anova_results["interaction"]["p"]
    p_grad = anova_results["gradient_flow"]["p"]
    p_norm = anova_results["norm_type"]["p"]

    if p_int < alpha:
        lines.append(
            f"INTERACTION SIGNIFICANT (p={p_int:.4f}) — "
            "Plan A: gradient_flow × norm_type interaction narrative"
        )
    else:
        lines.append(
            f"NO SIGNIFICANT INTERACTION (p={p_int:.4f}) — "
            "Plan B needed. Check main effects."
        )

    if p_grad < alpha:
        lines.append(
            f"Gradient flow main effect significant (p={p_grad:.4f}, "
            f"η²={anova_results['gradient_flow']['partial_eta_squared']:.3f})"
        )
    if p_norm < alpha:
        lines.append(
            f"Norm type main effect significant (p={p_norm:.4f}, "
            f"η²={anova_results['norm_type']['partial_eta_squared']:.3f})"
        )

    return lines


def main():
    parser = argparse.ArgumentParser(
        description="2×2 Factorial ANOVA: gradient_flow × norm_type → CAR"
    )
    parser.add_argument("--json", type=str, help="JSON string with 4 cell arrays")
    parser.add_argument("--input", type=str, help="Path to JSON file with cell data")
    parser.add_argument(
        "--output", type=str, default="anova_results.json",
        help="Output JSON path (default: anova_results.json)"
    )
    args = parser.parse_args()

    if not args.json and not args.input:
        parser.print_help()
        sys.exit(1)

    data = load_data(args)
    cell_stats = descriptive_stats(data)

    min_n = min(s["n"] for s in cell_stats.values())
    if min_n < 5:
        print(f"\n⚠  WARNING: min cell n={min_n} < 5 — underpowered, interpret with caution\n")

    total_n = sum(s["n"] for s in cell_stats.values())
    if total_n < 8:
        print("ERROR: need at least 2 observations per cell for ANOVA", file=sys.stderr)
        sys.exit(1)

    rows = build_long_format(data)
    anova_results, df = run_anova(rows)
    tukey = run_tukey(df)
    decisions = decision_helper(anova_results)

    print("=" * 60)
    print("  2×2 Factorial ANOVA: gradient_flow × norm_type → CAR")
    print("=" * 60)

    print("\n── Descriptive Statistics ──")
    for key, s in cell_stats.items():
        print(f"  {key:15s}  mean={s['mean']:.4f}  std={s['std']:.4f}  n={s['n']}")

    print("\n── ANOVA Results ──")
    for effect in ["gradient_flow", "norm_type", "interaction"]:
        r = anova_results[effect]
        sig = "*" if r["p"] < 0.05 else ""
        print(
            f"  {effect:20s}  F({r['df']:.0f},{anova_results['residual']['df']:.0f})"
            f"={r['F']:8.3f}  p={r['p']:.4f}{sig}  η²={r['partial_eta_squared']:.3f}"
        )

    print("\n── Tukey HSD Post-hoc ──")
    for c in tukey:
        sig = "*" if c["reject"] else ""
        print(
            f"  {c['group1']:8s} vs {c['group2']:8s}  "
            f"diff={c['meandiff']:+.4f}  p={c['p_adj']:.4f}{sig}  "
            f"CI=[{c['lower']:.4f}, {c['upper']:.4f}]"
        )

    print("\n── Decision Helper ──")
    for line in decisions:
        print(f"  → {line}")
    print()

    output = {
        "factors": {
            "A": "gradient_flow (ON=Full OCC, OFF=Detach)",
            "B": "norm_type (BN=BatchNorm, LN=LayerNorm)",
        },
        "cell_means": {k: v["mean"] for k, v in cell_stats.items()},
        "cell_stds": {k: v["std"] for k, v in cell_stats.items()},
        "cell_ns": {k: v["n"] for k, v in cell_stats.items()},
        "anova": {
            "gradient_flow": anova_results["gradient_flow"],
            "norm_type": anova_results["norm_type"],
            "interaction": anova_results["interaction"],
        },
        "p_values": {
            "gradient_flow": anova_results["gradient_flow"]["p"],
            "norm_type": anova_results["norm_type"]["p"],
            "interaction": anova_results["interaction"]["p"],
        },
        "F_stats": {
            "gradient_flow": anova_results["gradient_flow"]["F"],
            "norm_type": anova_results["norm_type"]["F"],
            "interaction": anova_results["interaction"]["F"],
        },
        "eta_squared": {
            "gradient_flow": anova_results["gradient_flow"]["partial_eta_squared"],
            "norm_type": anova_results["norm_type"]["partial_eta_squared"],
            "interaction": anova_results["interaction"]["partial_eta_squared"],
        },
        "significant_interactions": anova_results["interaction"]["p"] < 0.05,
        "tukey_hsd": tukey,
        "decisions": decisions,
        "interpretation_hint": decisions[0],
    }

    Path(args.output).write_text(json.dumps(output, indent=2, ensure_ascii=False))
    print(f"Results saved to {args.output}")


if __name__ == "__main__":
    main()
