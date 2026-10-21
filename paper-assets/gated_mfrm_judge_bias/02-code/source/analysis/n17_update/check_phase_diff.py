"""Check Phase 1 vs Phase 2 MCMC estimate differences.

Input:
  --phase1-dir: Phase 1 MCMC output directory
  --phase2-dir: Phase 2 MCMC output directory
  --output:     Output CSV path (default: phase_diff.csv in phase2-dir)

Output:
  CSV with parameter-level diff stats.
  Safety assessment: SAFE / CAUTION / UNSAFE based on thresholds:
    - theta rank tau > 0.95 and max |delta_theta| < 0.1 → SAFE
    - theta rank tau > 0.90 or max |delta_theta| < 0.2 → CAUTION
    - otherwise → UNSAFE
"""

import argparse
import csv
import json
import os
import sys

import numpy as np
from scipy.stats import kendalltau, spearmanr

METHODS = ["raw_average", "mfrm_only", "sequential", "joint_gmfrm"]


def load_results(path):
    results_path = os.path.join(path, "results.json")
    if not os.path.exists(results_path):
        print(f"ERROR: {results_path} not found.")
        sys.exit(1)
    with open(results_path) as f:
        return json.load(f)


def compare_param(p1_dict, p2_dict, label="param"):
    shared = sorted(set(p1_dict.keys()) & set(p2_dict.keys()))
    if len(shared) < 2:
        return None

    v1 = np.array([p1_dict[k] for k in shared])
    v2 = np.array([p2_dict[k] for k in shared])
    diff = v2 - v1

    tau, p_tau = kendalltau(v1, v2)
    rho, p_rho = spearmanr(v1, v2)
    corr = np.corrcoef(v1, v2)[0, 1]

    return {
        "label": label,
        "n": len(shared),
        "rank_tau": tau,
        "rank_rho": rho,
        "pearson_r": corr,
        "max_abs_diff": float(np.max(np.abs(diff))),
        "mean_abs_diff": float(np.mean(np.abs(diff))),
        "max_rel_diff": float(np.max(np.abs(diff) / (np.abs(v1) + 1e-8))),
        "per_key": {shared[i]: {"p1": float(v1[i]), "p2": float(v2[i]), "diff": float(diff[i])} for i in range(len(shared))},
    }


def assess_safety(comparisons):
    gmfrm_theta = None
    for c in comparisons:
        if c and c["label"] == "joint_gmfrm_theta":
            gmfrm_theta = c
            break

    if gmfrm_theta is None:
        return "UNKNOWN", "No joint_gmfrm theta comparison available"

    tau = gmfrm_theta["rank_tau"]
    max_diff = gmfrm_theta["max_abs_diff"]

    if tau > 0.95 and max_diff < 0.1:
        return "SAFE", f"rank_tau={tau:.3f} > 0.95, max|delta|={max_diff:.3f} < 0.1"
    elif tau > 0.90 or max_diff < 0.2:
        return "CAUTION", f"rank_tau={tau:.3f}, max|delta|={max_diff:.3f} — borderline"
    else:
        return "UNSAFE", f"rank_tau={tau:.3f} <= 0.90, max|delta|={max_diff:.3f} >= 0.2"


def main():
    parser = argparse.ArgumentParser(
        description="Check Phase 1 vs Phase 2 MCMC differences"
    )
    parser.add_argument(
        "--phase1-dir", required=True, help="Phase 1 MCMC output directory"
    )
    parser.add_argument(
        "--phase2-dir", required=True, help="Phase 2 MCMC output directory"
    )
    parser.add_argument(
        "--output",
        default=None,
        help="Output CSV path (default: phase_diff.csv in phase2-dir)",
    )
    args = parser.parse_args()

    p1 = load_results(args.phase1_dir)
    p2 = load_results(args.phase2_dir)
    output_path = args.output or os.path.join(args.phase2_dir, "phase_diff.csv")

    print("=" * 70)
    print("Phase 1 vs Phase 2 Difference Check")
    print("=" * 70)

    comparisons = []
    rows = []

    for method in METHODS:
        p1_params = p1.get("parameters", {}).get(method, {})
        p2_params = p2.get("parameters", {}).get(method, {})

        # theta
        t1 = p1_params.get("theta_values", {})
        t2 = p2_params.get("theta_values", {})
        if t1 and t2:
            comp = compare_param(t1, t2, f"{method}_theta")
            comparisons.append(comp)
            if comp:
                print(f"\n--- {method} theta ---")
                print(f"  n={comp['n']}, rank_tau={comp['rank_tau']:.3f}, "
                      f"pearson_r={comp['pearson_r']:.4f}")
                print(f"  max|diff|={comp['max_abs_diff']:.4f}, "
                      f"mean|diff|={comp['mean_abs_diff']:.4f}")
                rows.append({
                    "parameter": f"{method}_theta",
                    "n": comp["n"],
                    "rank_tau": f"{comp['rank_tau']:.4f}",
                    "rank_rho": f"{comp['rank_rho']:.4f}",
                    "pearson_r": f"{comp['pearson_r']:.4f}",
                    "max_abs_diff": f"{comp['max_abs_diff']:.4f}",
                    "mean_abs_diff": f"{comp['mean_abs_diff']:.4f}",
                })

        # c
        c1 = p1_params.get("c_values", {})
        c2 = p2_params.get("c_values", {})
        if c1 and c2:
            comp = compare_param(c1, c2, f"{method}_c")
            comparisons.append(comp)
            if comp:
                print(f"\n--- {method} c ---")
                print(f"  n={comp['n']}, rank_tau={comp['rank_tau']:.3f}, "
                      f"max|diff|={comp['max_abs_diff']:.4f}")
                rows.append({
                    "parameter": f"{method}_c",
                    "n": comp["n"],
                    "rank_tau": f"{comp['rank_tau']:.4f}",
                    "rank_rho": f"{comp['rank_rho']:.4f}",
                    "pearson_r": f"{comp['pearson_r']:.4f}",
                    "max_abs_diff": f"{comp['max_abs_diff']:.4f}",
                    "mean_abs_diff": f"{comp['mean_abs_diff']:.4f}",
                })

        # d
        d1 = p1_params.get("d_values", {})
        d2 = p2_params.get("d_values", {})
        if d1 and d2:
            comp = compare_param(d1, d2, f"{method}_d")
            comparisons.append(comp)
            if comp:
                print(f"\n--- {method} d ---")
                print(f"  n={comp['n']}, rank_tau={comp['rank_tau']:.3f}, "
                      f"max|diff|={comp['max_abs_diff']:.4f}")
                rows.append({
                    "parameter": f"{method}_d",
                    "n": comp["n"],
                    "rank_tau": f"{comp['rank_tau']:.4f}",
                    "rank_rho": f"{comp['rank_rho']:.4f}",
                    "pearson_r": f"{comp['pearson_r']:.4f}",
                    "max_abs_diff": f"{comp['max_abs_diff']:.4f}",
                    "mean_abs_diff": f"{comp['mean_abs_diff']:.4f}",
                })

    # Safety assessment
    assessment, reason = assess_safety(comparisons)
    print(f"\n{'=' * 70}")
    print(f"SAFETY ASSESSMENT: {assessment}")
    print(f"  {reason}")
    print(f"{'=' * 70}")

    rows.append({
        "parameter": "ASSESSMENT",
        "n": assessment,
        "rank_tau": reason,
        "rank_rho": "",
        "pearson_r": "",
        "max_abs_diff": "",
        "mean_abs_diff": "",
    })

    fieldnames = ["parameter", "n", "rank_tau", "rank_rho", "pearson_r", "max_abs_diff", "mean_abs_diff"]
    with open(output_path, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

    print(f"\nSaved to {output_path}")

    if assessment == "UNSAFE":
        sys.exit(1)


if __name__ == "__main__":
    main()
