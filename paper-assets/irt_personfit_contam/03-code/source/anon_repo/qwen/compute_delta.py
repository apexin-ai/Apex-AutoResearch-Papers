"""
compute_delta.py — Aggregate results from 4 conditions, compute delta-lz* and summary statistics.

Reads {condition}_results.json for all 4 conditions, computes:
  - Delta lz* = lz*(condition) - mean(lz*(clean_s1), lz*(clean_s2))
  - Cohen's d
  - Memorization fraction = (acc_seen - acc_unseen) / (1 - acc_unseen)
"""

import json
import os

import numpy as np

BASE_DIR = "/path/to/project/qwen"
RESULTS_DIR = os.path.join(BASE_DIR, "results")
CONDITIONS = ["clean_s1", "clean_s2", "contam_15", "contam_50"]


def main():
    results = {}
    for cond in CONDITIONS:
        path = os.path.join(RESULTS_DIR, f"{cond}_results.json")
        with open(path) as f:
            results[cond] = json.load(f)

    # Baseline lz* (mean of two clean conditions)
    lz_clean_1 = results["clean_s1"]["lz_star"]
    lz_clean_2 = results["clean_s2"]["lz_star"]
    lz_baseline = (lz_clean_1 + lz_clean_2) / 2.0

    # Std of clean lz* (for Cohen's d denominator)
    lz_clean_std = np.std([lz_clean_1, lz_clean_2], ddof=1)

    print("=" * 70)
    print("CONTROLLED CONTAMINATION PILOT — SUMMARY")
    print("=" * 70)

    print(f"\n{'Condition':<15} {'Acc':>8} {'Acc_seen':>10} {'Acc_unseen':>12} {'theta':>8} {'lz*':>8} {'Δlz*':>8}")
    print("-" * 70)

    summary = {}
    for cond in CONDITIONS:
        r = results[cond]
        delta_lz = r["lz_star"] - lz_baseline
        acc_seen_str = f"{r['accuracy_seen']:.4f}" if r["accuracy_seen"] is not None else "N/A"
        acc_unseen_str = f"{r['accuracy_unseen']:.4f}" if r["accuracy_unseen"] is not None else "N/A"

        print(f"{cond:<15} {r['accuracy_overall']:>8.4f} {acc_seen_str:>10} {acc_unseen_str:>12} "
              f"{r['theta_mle']:>8.4f} {r['lz_star']:>8.4f} {delta_lz:>8.4f}")

        # Memorization fraction
        mem_frac = None
        if r["accuracy_seen"] is not None and r["accuracy_unseen"] is not None:
            if r["accuracy_unseen"] < 1.0:
                mem_frac = (r["accuracy_seen"] - r["accuracy_unseen"]) / (1.0 - r["accuracy_unseen"])

        # Cohen's d (using clean std)
        cohens_d = None
        if lz_clean_std > 0:
            cohens_d = delta_lz / lz_clean_std

        summary[cond] = {
            "accuracy_overall": r["accuracy_overall"],
            "accuracy_seen": r["accuracy_seen"],
            "accuracy_unseen": r["accuracy_unseen"],
            "theta_mle": r["theta_mle"],
            "lz_star": r["lz_star"],
            "delta_lz_star": delta_lz,
            "cohens_d": cohens_d,
            "memorization_fraction": mem_frac,
            "lz_star_seen": r.get("lz_star_seen"),
            "lz_star_unseen": r.get("lz_star_unseen"),
        }

    print(f"\n{'Condition':<15} {'Cohen_d':>10} {'Mem_frac':>10} {'lz*_seen':>10} {'lz*_unseen':>12}")
    print("-" * 60)
    for cond in CONDITIONS:
        s = summary[cond]
        cd_str = f"{s['cohens_d']:.4f}" if s["cohens_d"] is not None else "N/A"
        mf_str = f"{s['memorization_fraction']:.4f}" if s["memorization_fraction"] is not None else "N/A"
        ls_str = f"{s['lz_star_seen']:.4f}" if s["lz_star_seen"] is not None else "N/A"
        lu_str = f"{s['lz_star_unseen']:.4f}" if s["lz_star_unseen"] is not None else "N/A"
        print(f"{cond:<15} {cd_str:>10} {mf_str:>10} {ls_str:>10} {lu_str:>12}")

    print(f"\nBaseline lz* (mean of clean): {lz_baseline:.4f}")
    print(f"Clean lz* std: {lz_clean_std:.4f}")

    # Save summary
    out_path = os.path.join(RESULTS_DIR, "summary.json")
    with open(out_path, "w") as f:
        json.dump(summary, f, indent=2)
    print(f"\nSummary saved to {out_path}")


if __name__ == "__main__":
    main()
