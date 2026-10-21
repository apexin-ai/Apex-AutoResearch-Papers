"""
analyze_instruct.py — Analyze differential depth response for instruct model.

Computes Spearman ρ for each feature vs depth, compares against base model.
"""

import argparse
import json
import sys
from collections import defaultdict

import numpy as np
import pandas as pd
from scipy import stats


BASE_MODEL_RHO = {
    "hapax_ratio": -0.6696,
    "ttr": -0.6523,
    "entropy_mean": -0.6022,
    "entropy_std": -0.1882,
    "entropy_max": 0.0884,
    "entropy_min": -0.4062,
    "tail_decay": -0.0698,
}

DRIFTING_FEATURES = {"hapax_ratio", "ttr", "entropy_mean"}
SHAPE_FEATURES = {"entropy_std", "tail_decay"}
DRIFT_THRESHOLD = 0.3
SHAPE_THRESHOLD = 0.15


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True, help="Features CSV path")
    parser.add_argument("--output", required=True, help="Output JSON path")
    parser.add_argument("--model-name", default="Qwen3-1.7B-Instruct")
    args = parser.parse_args()

    df = pd.read_csv(args.input)
    print(f"Loaded {len(df)} records, columns: {list(df.columns)}")

    feature_cols = ["hapax_ratio", "ttr", "entropy_mean", "entropy_std",
                    "entropy_max", "entropy_min", "tail_decay"]

    depth_dist = df["depth"].value_counts().sort_index().to_dict()
    depth_dist = {str(k): int(v) for k, v in depth_dist.items()}
    print(f"Depth distribution: {depth_dist}")

    spearman_rho = {}
    spearman_p = {}
    for feat in feature_cols:
        if feat not in df.columns:
            print(f"WARNING: {feat} not in columns, skipping")
            continue
        rho, p = stats.spearmanr(df["depth"], df[feat])
        spearman_rho[feat] = round(float(rho), 4)
        spearman_p[feat] = float(p)
        print(f"  {feat}: ρ={rho:.4f}, p={p:.2e}")

    # Check differential depth response criteria
    drift_ok = all(
        abs(spearman_rho.get(f, 0)) > DRIFT_THRESHOLD
        for f in DRIFTING_FEATURES
        if f in spearman_rho
    )
    shape_ok = all(
        abs(spearman_rho.get(f, 0)) < SHAPE_THRESHOLD
        for f in SHAPE_FEATURES
        if f in spearman_rho
    )
    differential_depth_response = drift_ok and shape_ok

    # Comparison vs base
    comparison = {}
    for feat in feature_cols:
        if feat in spearman_rho and feat in BASE_MODEL_RHO and BASE_MODEL_RHO[feat] is not None:
            comparison[feat] = {
                "instruct": spearman_rho[feat],
                "base": BASE_MODEL_RHO[feat],
                "delta": round(spearman_rho[feat] - BASE_MODEL_RHO[feat], 4),
            }

    # Per-depth feature means
    depth_means = {}
    for d in sorted(df["depth"].unique()):
        subset = df[df["depth"] == d]
        depth_means[str(int(d))] = {
            feat: round(float(subset[feat].mean()), 4)
            for feat in feature_cols if feat in df.columns
        }

    result = {
        "model": args.model_name,
        "n_records": len(df),
        "depth_distribution": depth_dist,
        "spearman_rho": spearman_rho,
        "spearman_p": {k: f"{v:.2e}" for k, v in spearman_p.items()},
        "differential_depth_response": differential_depth_response,
        "drift_check": {f: abs(spearman_rho.get(f, 0)) > DRIFT_THRESHOLD for f in DRIFTING_FEATURES},
        "shape_check": {f: abs(spearman_rho.get(f, 0)) < SHAPE_THRESHOLD for f in SHAPE_FEATURES},
        "comparison_vs_base": comparison,
        "depth_means": depth_means,
    }

    with open(args.output, "w") as f:
        json.dump(result, f, indent=2, ensure_ascii=False)
    print(f"\nResults saved to {args.output}")
    print(f"Differential depth response: {differential_depth_response}")

    # Summary
    print(f"\n{'='*60}")
    print(f"Model: {args.model_name}")
    print(f"N records: {len(df)}")
    print(f"\nSpearman ρ (feature vs depth):")
    for feat in feature_cols:
        if feat in spearman_rho:
            marker = ""
            if feat in DRIFTING_FEATURES:
                marker = " ✓" if abs(spearman_rho[feat]) > DRIFT_THRESHOLD else " ✗"
            elif feat in SHAPE_FEATURES:
                marker = " ✓" if abs(spearman_rho[feat]) < SHAPE_THRESHOLD else " ✗"
            print(f"  {feat:15s}: {spearman_rho[feat]:+.4f}{marker}")
    if comparison:
        print(f"\nComparison vs base (Qwen3-1.7B-Base):")
        for feat, vals in comparison.items():
            print(f"  {feat:15s}: instruct={vals['instruct']:+.4f}  base={vals['base']:+.4f}  Δ={vals['delta']:+.4f}")


if __name__ == "__main__":
    main()
