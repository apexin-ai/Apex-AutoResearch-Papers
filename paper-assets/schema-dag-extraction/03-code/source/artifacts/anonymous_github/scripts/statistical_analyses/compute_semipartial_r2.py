#!/usr/bin/env python3
"""Semipartial R² for BCS after controlling for degree centrality.

Computes the unique variance in batch-level RE accuracy explained by BCS
beyond what degree centrality already explains:
  ΔR²_BCS = R²_full(acc ~ BCS + centrality) - R²_centrality_only(acc ~ centrality)

Input: JSON with per-batch records, each containing:
  - "bcs": float (Batch Confusability Score)
  - "accuracy": float (RE accuracy)
  - "degree_centrality": float (mean off-diagonal SCS, proxy for node centrality)

Output: JSON with R² decomposition, VIF, partial correlations.

Usage:
  python compute_semipartial_r2.py --input data/fewrel_batches.json --output results/semipartial_r2.json
"""
import argparse
import json

import numpy as np
from scipy import stats


def compute_r2(X, y):
    """OLS R² for design matrix X (with intercept) predicting y."""
    X = np.column_stack([np.ones(len(y)), X])
    beta = np.linalg.lstsq(X, y, rcond=None)[0]
    y_hat = X @ beta
    ss_res = np.sum((y - y_hat) ** 2)
    ss_tot = np.sum((y - np.mean(y)) ** 2)
    return 1.0 - ss_res / ss_tot


def partial_correlation(x, y, z):
    """Partial Pearson r between x and y, controlling for z."""
    r_xy = np.corrcoef(x, y)[0, 1]
    r_xz = np.corrcoef(x, z)[0, 1]
    r_yz = np.corrcoef(y, z)[0, 1]
    num = r_xy - r_xz * r_yz
    den = np.sqrt((1 - r_xz**2) * (1 - r_yz**2))
    return num / den if den > 0 else 0.0


def main():
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--input", required=True, help="JSON file with per-batch BCS, accuracy, degree_centrality")
    parser.add_argument("--output", required=True, help="Output JSON path")
    args = parser.parse_args()

    with open(args.input) as f:
        data = json.load(f)

    if isinstance(data, dict):
        records = list(data.values())
    else:
        records = data

    bcs = np.array([r["bcs"] for r in records])
    acc = np.array([r["accuracy"] for r in records])
    cent = np.array([r["degree_centrality"] for r in records])
    n = len(bcs)

    r2_full = compute_r2(np.column_stack([bcs, cent]), acc)
    r2_cent_only = compute_r2(cent.reshape(-1, 1), acc)
    r2_bcs_only = compute_r2(bcs.reshape(-1, 1), acc)

    delta_r2_bcs = r2_full - r2_cent_only
    delta_r2_cent = r2_full - r2_bcs_only
    shared = r2_full - delta_r2_bcs - delta_r2_cent

    r_bcs_cent = np.corrcoef(bcs, cent)[0, 1]
    vif = 1.0 / (1.0 - r_bcs_cent**2) if abs(r_bcs_cent) < 1.0 else float("inf")

    r_bcs_acc = np.corrcoef(bcs, acc)[0, 1]
    r_cent_acc = np.corrcoef(cent, acc)[0, 1]
    partial_r_bcs = partial_correlation(bcs, acc, cent)

    result = {
        "n_batches": n,
        "R2_full": round(r2_full, 6),
        "R2_centrality_only": round(r2_cent_only, 6),
        "R2_BCS_only": round(r2_bcs_only, 6),
        "semipartial_R2_BCS": round(delta_r2_bcs, 6),
        "semipartial_R2_centrality": round(delta_r2_cent, 6),
        "shared_variance": round(shared, 6),
        "zero_order_r_BCS": round(r_bcs_acc, 4),
        "zero_order_r_centrality": round(r_cent_acc, 4),
        "partial_r_BCS": round(partial_r_bcs, 4),
        "corr_BCS_centrality": round(r_bcs_cent, 4),
        "VIF": round(vif, 2),
    }

    with open(args.output, "w") as f:
        json.dump(result, f, indent=2)

    print(f"n={n}")
    print(f"Semipartial R²(BCS) = {delta_r2_bcs:.4f}")
    print(f"VIF = {vif:.2f}")
    print(f"Partial r(BCS|centrality) = {partial_r_bcs:.4f}")
    print(f"Results saved to {args.output}")


if __name__ == "__main__":
    main()
