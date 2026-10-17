#!/usr/bin/env python3
"""Permutation-based equivalence test for Count × BCS interaction.

Nonparametric complement to the parametric TOST. Permutes BCS group
assignments within each count level to build a null distribution of the
interaction effect, then applies two one-sided permutation tests against
a ±delta equivalence margin.

Input: JSON with per-batch records, each containing:
  - "count_key": str (e.g., "count_8", "count_16")
  - "bcs": float
  - "accuracy": float

Usage:
  python permutation_equivalence_test.py --input data/fewrel_batches.json --output results/perm_equiv.json
  python permutation_equivalence_test.py --input data/fewrel_batches.json --output results/perm_equiv.json --delta 3.0 --n-perm 10000 --count-levels 8 16
"""
import argparse
import json

import numpy as np


def compute_interaction(low_a, high_a, low_b, high_b):
    """Interaction = (high_a - low_a) - (high_b - low_b), in raw scale."""
    return (np.mean(high_a) - np.mean(low_a)) - (np.mean(high_b) - np.mean(low_b))


def split_by_median_bcs(bcs_vals, acc_vals):
    median_bcs = np.median(bcs_vals)
    low_mask = bcs_vals <= median_bcs
    return acc_vals[low_mask], acc_vals[~low_mask], float(median_bcs)


def main():
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--input", required=True, help="JSON with per-batch records")
    parser.add_argument("--output", required=True, help="Output JSON path")
    parser.add_argument("--delta", type=float, default=3.0, help="Equivalence margin in pp (default: 3.0)")
    parser.add_argument("--n-perm", type=int, default=10000, help="Number of permutations")
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--count-levels", type=int, nargs=2, default=[8, 16],
                        help="Two count levels to compare")
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

    low_a, high_a, med_a = split_by_median_bcs(bcs_a, acc_a)
    low_b, high_b, med_b = split_by_median_bcs(bcs_b, acc_b)

    obs_interaction = compute_interaction(low_a, high_a, low_b, high_b) * 100
    n_low_a, n_low_b = len(low_a), len(low_b)

    rng = np.random.default_rng(args.seed)
    perm_interactions = np.empty(args.n_perm)
    for i in range(args.n_perm):
        pa = rng.permutation(acc_a)
        pb = rng.permutation(acc_b)
        pi = compute_interaction(pa[:n_low_a], pa[n_low_a:],
                                 pb[:n_low_b], pb[n_low_b:]) * 100
        perm_interactions[i] = pi

    perm_se = float(np.std(perm_interactions))
    ci_lower = float(np.percentile(perm_interactions, 2.5))
    ci_upper = float(np.percentile(perm_interactions, 97.5))

    ci_se_lower = obs_interaction - 1.96 * perm_se
    ci_se_upper = obs_interaction + 1.96 * perm_se

    p_reject_upper = float(np.mean(perm_interactions <= (obs_interaction - args.delta)))
    p_reject_lower = float(np.mean(perm_interactions >= (obs_interaction + args.delta)))
    p_tost = max(p_reject_upper, p_reject_lower)

    p_h0_zero = float(np.mean(np.abs(perm_interactions) >= abs(obs_interaction)))

    result = {
        "count_levels": args.count_levels,
        "n_batches": {"count_a": len(batches_a), "count_b": len(batches_b)},
        "cell_sizes": {
            f"count_{cl_a}_low": int(n_low_a),
            f"count_{cl_a}_high": int(len(high_a)),
            f"count_{cl_b}_low": int(n_low_b),
            f"count_{cl_b}_high": int(len(high_b)),
        },
        "cell_means_pct": {
            f"count_{cl_a}_low": round(float(np.mean(low_a) * 100), 2),
            f"count_{cl_a}_high": round(float(np.mean(high_a) * 100), 2),
            f"count_{cl_b}_low": round(float(np.mean(low_b) * 100), 2),
            f"count_{cl_b}_high": round(float(np.mean(high_b) * 100), 2),
        },
        "observed_interaction_pp": round(obs_interaction, 4),
        "n_permutations": args.n_perm,
        "null_sd_pp": round(perm_se, 4),
        "ci_95_percentile_pp": [round(ci_lower, 4), round(ci_upper, 4)],
        "ci_95_se_based_pp": [round(ci_se_lower, 4), round(ci_se_upper, 4)],
        "equivalence_margin_pp": args.delta,
        "tost_p_upper": round(p_reject_upper, 4),
        "tost_p_lower": round(p_reject_lower, 4),
        "tost_p": round(p_tost, 4),
        "p_h0_zero": round(p_h0_zero, 4),
        "equivalent": bool(p_tost < 0.05),
    }

    with open(args.output, "w") as f:
        json.dump(result, f, indent=2)

    print(f"Observed interaction: {obs_interaction:.2f} pp")
    print(f"Permutation TOST p={p_tost:.4f} (margin=±{args.delta}pp)")
    print(f"Equivalent: {result['equivalent']}")
    print(f"Saved to {args.output}")


if __name__ == "__main__":
    main()
