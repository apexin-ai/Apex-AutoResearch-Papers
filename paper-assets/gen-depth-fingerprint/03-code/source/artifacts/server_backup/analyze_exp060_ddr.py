"""exp_060: DDR feature-level analysis for Qwen3-14B-Base."""

import json
import os
import sys

import numpy as np
import pandas as pd
from scipy.stats import spearmanr

FEATURES = ["entropy_mean", "entropy_std", "entropy_max", "entropy_min", "ttr", "hapax_ratio", "tail_decay"]

EXPECTED_DRIFTING = {"entropy_mean", "ttr", "hapax_ratio"}
EXPECTED_STATIONARY = {"entropy_max", "entropy_min", "tail_decay"}


def cohens_d(g1, g2):
    n1, n2 = len(g1), len(g2)
    if n1 < 2 or n2 < 2:
        return np.nan
    m1, m2 = g1.mean(), g2.mean()
    s1, s2 = g1.std(ddof=1), g2.std(ddof=1)
    pooled = np.sqrt(((n1 - 1) * s1**2 + (n2 - 1) * s2**2) / (n1 + n2 - 2))
    if pooled == 0:
        return 0.0
    return (m2 - m1) / pooled


def main():
    features_csv = sys.argv[1] if len(sys.argv) > 1 else "/root/gen-depth-fingerprint/data/features_qwen3-14b-base.csv"
    output_json = sys.argv[2] if len(sys.argv) > 2 else "/root/gen-depth-fingerprint/results/exp_060_14b_ddr.json"

    df = pd.read_csv(features_csv)
    n_samples = len(df)
    n_seeds = df["seed_id"].nunique()
    print(f"Loaded {n_samples} samples from {n_seeds} seeds")
    print(f"Depth distribution:\n{df['depth'].value_counts().sort_index()}\n")

    gen0 = df[df["depth"] == 0]
    gen2p = df[df["depth"] >= 2]

    feat_results = {}
    for feat in FEATURES:
        rho, rho_p = spearmanr(df[feat], df["depth"])
        d = cohens_d(gen0[feat].dropna(), gen2p[feat].dropna())
        abs_rho = abs(rho)
        abs_d = abs(d)

        if abs_rho > 0.3 and abs_d > 0.5:
            group = "drifting"
        elif abs_d < 0.2:
            group = "stationary"
        else:
            group = "intermediate"

        feat_results[feat] = {
            "rho": round(rho, 4),
            "rho_p": round(rho_p, 6),
            "d_gen0_vs_gen2p": round(d, 4),
            "abs_rho": round(abs_rho, 4),
            "abs_d": round(abs_d, 4),
            "group": group,
        }
        print(f"{feat:15s}  rho={rho:+.4f} (p={rho_p:.2e})  d={d:+.4f}  -> {group}")

    actual_drifting = {f for f, v in feat_results.items() if v["group"] == "drifting"}
    actual_stationary = {f for f, v in feat_results.items() if v["group"] == "stationary"}

    drift_match = EXPECTED_DRIFTING.issubset(actual_drifting)
    stat_match = EXPECTED_STATIONARY.issubset(actual_stationary)
    ddr_pattern_match = drift_match and stat_match

    summary_parts = []
    summary_parts.append(f"Drifting: {sorted(actual_drifting)} ({'match' if drift_match else 'MISMATCH'})")
    summary_parts.append(f"Stationary: {sorted(actual_stationary)} ({'match' if stat_match else 'MISMATCH'})")
    summary_parts.append(f"DDR pattern holds at 14B: {ddr_pattern_match}")
    summary = "; ".join(summary_parts)

    print(f"\n{summary}")

    result = {
        "generator": "qwen3-14b-base",
        "params_b": 14.7,
        "n_seeds": n_seeds,
        "n_samples": n_samples,
        "features": feat_results,
        "ddr_pattern_match": ddr_pattern_match,
        "drift_match": drift_match,
        "stat_match": stat_match,
        "summary": summary,
    }

    os.makedirs(os.path.dirname(output_json), exist_ok=True)
    with open(output_json, "w") as f:
        json.dump(result, f, indent=2)
    print(f"\nSaved to {output_json}")


if __name__ == "__main__":
    main()
