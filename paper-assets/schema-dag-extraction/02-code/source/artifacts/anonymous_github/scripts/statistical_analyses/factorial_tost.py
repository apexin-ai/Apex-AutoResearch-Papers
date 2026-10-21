#!/usr/bin/env python3
"""TOST equivalence test for Count × BCS interaction in RE accuracy.

Tests whether the interaction between schema count and batch confusability
is practically negligible (within ±delta pp of zero) using:
  1. Regression-based TOST (Schuirmann, 1987; Lakens, 2017)
  2. 2×2 factorial ANOVA with TOST on the interaction term

Input: JSON with per-batch records, each containing:
  - "count_key": str (e.g., "count_4", "count_8", "count_16", ...)
  - "bcs": float (Batch Confusability Score)
  - "accuracy": float (RE accuracy)

Usage:
  python factorial_tost.py --input data/fewrel_batches.json --output results/tost.json --delta 3.0
  python factorial_tost.py --input data/fewrel_batches.json --output results/tost.json --delta 3.0 --count-levels 8 16
"""
import argparse
import json

import numpy as np
from scipy import stats


def regression_tost(count_vals, bcs_vals, acc_vals, delta_pp):
    """Regression-based TOST: acc ~ log2(count) + BCS + count×BCS interaction.

    Returns interaction coefficient, SE, and TOST p-value against ±delta_pp.
    """
    log_count = np.log2(count_vals)
    X = np.column_stack([
        np.ones(len(acc_vals)),
        log_count,
        bcs_vals,
        log_count * bcs_vals,
    ])
    y = acc_vals * 100  # work in pp

    beta = np.linalg.lstsq(X, y, rcond=None)[0]
    y_hat = X @ beta
    residuals = y - y_hat
    n, p = X.shape
    mse = np.sum(residuals**2) / (n - p)
    cov = mse * np.linalg.inv(X.T @ X)
    se = np.sqrt(np.diag(cov))

    interaction_coef = beta[3]
    interaction_se = se[3]
    interaction_t = interaction_coef / interaction_se
    interaction_p = 2 * stats.t.sf(abs(interaction_t), df=n - p)

    r2 = 1.0 - np.sum(residuals**2) / np.sum((y - np.mean(y))**2)

    t_upper = (interaction_coef - delta_pp) / interaction_se
    t_lower = (interaction_coef + delta_pp) / interaction_se
    p_upper = stats.t.cdf(t_upper, df=n - p)
    p_lower = 1.0 - stats.t.cdf(t_lower, df=n - p)
    p_tost = max(p_upper, p_lower)

    return {
        "method": "regression_tost",
        "n": int(n),
        "interaction_coef_pp": round(float(interaction_coef), 4),
        "interaction_se_pp": round(float(interaction_se), 4),
        "interaction_t": round(float(interaction_t), 4),
        "interaction_p": round(float(interaction_p), 4),
        "R2": round(float(r2), 4),
        "equivalence_margin_pp": delta_pp,
        "tost_p_upper": round(float(p_upper), 4),
        "tost_p_lower": round(float(p_lower), 4),
        "tost_p": round(float(p_tost), 4),
        "equivalent": bool(p_tost < 0.05),
        "count_coef_pp": round(float(beta[1]), 4),
        "bcs_coef_pp": round(float(beta[2]), 4),
    }


def factorial_tost(count_vals, bcs_vals, acc_vals, delta_pp, count_levels):
    """2×2 factorial TOST: split by median BCS within each count level."""
    cells = {}
    for cl in count_levels:
        mask = count_vals == cl
        b = bcs_vals[mask]
        a = acc_vals[mask]
        median_bcs = np.median(b)
        low_mask = b <= median_bcs
        cells[f"count_{cl}_low"] = a[low_mask] * 100
        cells[f"count_{cl}_high"] = a[~low_mask] * 100

    cl0, cl1 = count_levels
    effect_0 = np.mean(cells[f"count_{cl0}_high"]) - np.mean(cells[f"count_{cl0}_low"])
    effect_1 = np.mean(cells[f"count_{cl1}_high"]) - np.mean(cells[f"count_{cl1}_low"])
    interaction = effect_0 - effect_1

    all_residuals = []
    for key, vals in cells.items():
        all_residuals.extend(vals - np.mean(vals))
    mse = np.mean(np.array(all_residuals)**2)
    ns = [len(cells[k]) for k in cells]
    se_interaction = np.sqrt(mse * sum(1.0 / n for n in ns))

    t_obs = interaction / se_interaction
    df = sum(ns) - len(cells)
    p_obs = 2 * stats.t.sf(abs(t_obs), df=df)

    t_upper = (interaction - delta_pp) / se_interaction
    t_lower = (interaction + delta_pp) / se_interaction
    p_upper = stats.t.cdf(t_upper, df=df)
    p_lower = 1.0 - stats.t.cdf(t_lower, df=df)
    p_tost = max(p_upper, p_lower)

    return {
        "method": "factorial_2x2_tost",
        "count_levels": count_levels,
        "interaction_pp": round(float(interaction), 4),
        "interaction_se_pp": round(float(se_interaction), 4),
        "interaction_t": round(float(t_obs), 4),
        "interaction_p": round(float(p_obs), 4),
        "equivalence_margin_pp": delta_pp,
        "tost_p_upper": round(float(p_upper), 4),
        "tost_p_lower": round(float(p_lower), 4),
        "tost_p": round(float(p_tost), 4),
        "equivalent": bool(p_tost < 0.05),
        "cell_means_pct": {k: round(float(np.mean(v)), 2) for k, v in cells.items()},
        "cell_sizes": {k: len(v) for k, v in cells.items()},
        "df": int(df),
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--input", required=True, help="JSON with per-batch count_key, bcs, accuracy")
    parser.add_argument("--output", required=True, help="Output JSON path")
    parser.add_argument("--delta", type=float, default=3.0, help="Equivalence margin in pp (default: 3.0)")
    parser.add_argument("--count-levels", type=int, nargs=2, default=None,
                        help="Two count levels for 2×2 factorial (default: auto-detect)")
    args = parser.parse_args()

    with open(args.input) as f:
        data = json.load(f)

    records = list(data.values()) if isinstance(data, dict) else data

    count_vals = np.array([int(r["count_key"].replace("count_", "")) for r in records])
    bcs_vals = np.array([r["bcs"] for r in records])
    acc_vals = np.array([r["accuracy"] for r in records])

    results = {}

    results["regression"] = regression_tost(count_vals, bcs_vals, acc_vals, args.delta)
    print(f"Regression TOST: interaction={results['regression']['interaction_coef_pp']:.2f}pp, "
          f"p_TOST={results['regression']['tost_p']:.4f}, equivalent={results['regression']['equivalent']}")

    if args.count_levels:
        cl = args.count_levels
    else:
        unique_counts = sorted(np.unique(count_vals))
        if len(unique_counts) >= 2:
            cl = [unique_counts[0], unique_counts[-1]]
        else:
            cl = None

    if cl:
        mask = np.isin(count_vals, cl)
        results["factorial"] = factorial_tost(
            count_vals[mask], bcs_vals[mask], acc_vals[mask], args.delta, cl
        )
        print(f"Factorial TOST: interaction={results['factorial']['interaction_pp']:.2f}pp, "
              f"p_TOST={results['factorial']['tost_p']:.4f}, equivalent={results['factorial']['equivalent']}")

    with open(args.output, "w") as f:
        json.dump(results, f, indent=2)
    print(f"Saved to {args.output}")


if __name__ == "__main__":
    main()
