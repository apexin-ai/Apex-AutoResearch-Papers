#!/usr/bin/env python3
"""Range-matched interaction analysis for DocRED Count × BCS.

DocRED's apparent sub-additive interaction arises partly from different BCS
ranges at different count levels. This script restricts both count levels to
the overlapping BCS range and recomputes the interaction, testing whether it
reduces to near-zero.

Input: JSON with per-batch records, each containing:
  - "count_key": str (e.g., "count_16", "count_32")
  - "bcs": float
  - "accuracy": float

Usage:
  python bcs_range_matched_interaction.py --input data/docred_batches.json --output results/range_matched.json
  python bcs_range_matched_interaction.py --input data/docred_batches.json --output results/range_matched.json --count-levels 16 32
"""
import argparse
import json

import numpy as np
from scipy import stats


def compute_bcs_effect(bcs, acc):
    """Simple OLS slope of accuracy on BCS, in pp."""
    if len(bcs) < 3:
        return float("nan"), float("nan"), float("nan")
    slope, intercept, r, p, se = stats.linregress(bcs, acc * 100)
    rho, rho_p = stats.spearmanr(bcs, acc)
    return slope, r, rho


def interaction_with_ci(low_a, high_a, low_b, high_b, n_boot=10000, seed=42):
    """Bootstrap CI for the 2×2 interaction (in pp)."""
    effect_a = np.mean(high_a) - np.mean(low_a)
    effect_b = np.mean(high_b) - np.mean(low_b)
    obs = (effect_a - effect_b) * 100

    rng = np.random.default_rng(seed)
    boot = np.empty(n_boot)
    for i in range(n_boot):
        la = np.mean(rng.choice(low_a, len(low_a), replace=True))
        ha = np.mean(rng.choice(high_a, len(high_a), replace=True))
        lb = np.mean(rng.choice(low_b, len(low_b), replace=True))
        hb = np.mean(rng.choice(high_b, len(high_b), replace=True))
        boot[i] = ((ha - la) - (hb - lb)) * 100

    ci = [float(np.percentile(boot, 2.5)), float(np.percentile(boot, 97.5))]
    return obs, ci


def main():
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--input", required=True, help="JSON with per-batch records")
    parser.add_argument("--output", required=True, help="Output JSON path")
    parser.add_argument("--count-levels", type=int, nargs=2, default=[16, 32])
    args = parser.parse_args()

    with open(args.input) as f:
        data = json.load(f)

    records = list(data.values()) if isinstance(data, dict) else data

    cl_a, cl_b = args.count_levels
    batches_a = [(r["bcs"], r["accuracy"]) for r in records
                 if r["count_key"] == f"count_{cl_a}"]
    batches_b = [(r["bcs"], r["accuracy"]) for r in records
                 if r["count_key"] == f"count_{cl_b}"]

    bcs_a = np.array([b for b, _ in batches_a])
    acc_a = np.array([a for _, a in batches_a])
    bcs_b = np.array([b for b, _ in batches_b])
    acc_b = np.array([a for _, a in batches_b])

    # Before range matching: median split interaction
    med_a = np.median(bcs_a)
    med_b = np.median(bcs_b)
    before_obs, before_ci = interaction_with_ci(
        acc_a[bcs_a <= med_a], acc_a[bcs_a > med_a],
        acc_b[bcs_b <= med_b], acc_b[bcs_b > med_b],
    )

    # Overlapping BCS range
    overlap_lo = max(bcs_a.min(), bcs_b.min())
    overlap_hi = min(bcs_a.max(), bcs_b.max())

    mask_a = (bcs_a >= overlap_lo) & (bcs_a <= overlap_hi)
    mask_b = (bcs_b >= overlap_lo) & (bcs_b <= overlap_hi)

    bcs_a_m = bcs_a[mask_a]
    acc_a_m = acc_a[mask_a]
    bcs_b_m = bcs_b[mask_b]
    acc_b_m = acc_b[mask_b]

    # After range matching: median split interaction
    med_am = np.median(bcs_a_m)
    med_bm = np.median(bcs_b_m)
    after_obs, after_ci = interaction_with_ci(
        acc_a_m[bcs_a_m <= med_am], acc_a_m[bcs_a_m > med_am],
        acc_b_m[bcs_b_m <= med_bm], acc_b_m[bcs_b_m > med_bm],
    )

    # Per-count BCS slopes
    slope_a, r_a, rho_a = compute_bcs_effect(bcs_a_m, acc_a_m)
    slope_b, r_b, rho_b = compute_bcs_effect(bcs_b_m, acc_b_m)

    result = {
        "count_levels": args.count_levels,
        "before_matching": {
            "n_a": len(batches_a),
            "n_b": len(batches_b),
            "bcs_range_a": [round(float(bcs_a.min()), 4), round(float(bcs_a.max()), 4)],
            "bcs_range_b": [round(float(bcs_b.min()), 4), round(float(bcs_b.max()), 4)],
            "interaction_pp": round(before_obs, 2),
            "interaction_ci_95": [round(c, 2) for c in before_ci],
        },
        "overlap_bcs_range": [round(overlap_lo, 4), round(overlap_hi, 4)],
        "after_matching": {
            "n_a": int(mask_a.sum()),
            "n_b": int(mask_b.sum()),
            "interaction_pp": round(after_obs, 2),
            "interaction_ci_95": [round(c, 2) for c in after_ci],
            f"count_{cl_a}_slope": round(slope_a, 4),
            f"count_{cl_a}_rho": round(rho_a, 4),
            f"count_{cl_b}_slope": round(slope_b, 4),
            f"count_{cl_b}_rho": round(rho_b, 4),
        },
        "reduction_pp": round(abs(before_obs) - abs(after_obs), 2),
    }

    with open(args.output, "w") as f:
        json.dump(result, f, indent=2)

    print(f"Before range matching: interaction={before_obs:.2f}pp, CI={before_ci}")
    print(f"Overlap BCS range: [{overlap_lo:.4f}, {overlap_hi:.4f}]")
    print(f"After range matching: interaction={after_obs:.2f}pp, CI={after_ci}")
    print(f"Reduction: {abs(before_obs) - abs(after_obs):.2f}pp")
    print(f"Saved to {args.output}")


if __name__ == "__main__":
    main()
