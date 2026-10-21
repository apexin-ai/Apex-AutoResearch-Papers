#!/usr/bin/env python3
"""Worked example: confounding topology with K=3 confusion matrix.

Demonstrates the full annot_sensitivity workflow:
  1. Define a K=3 confusion matrix
  2. Compute bias
  3. Compute ASV
  4. Get correction recommendation
  5. (Optional) Plot bias curve
"""

import numpy as np
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))

from annot_sensitivity import (
    compute_bias,
    compute_asv,
    recommend_correction,
    predefined_matrices,
    validate_confusion_matrix,
)


def main():
    print("=" * 60)
    print("annot_sensitivity: Confounding K=3 Example")
    print("=" * 60)

    # 1. Define confusion matrix
    C = np.array([
        [0.80, 0.10, 0.10],
        [0.10, 0.80, 0.10],
        [0.10, 0.10, 0.80],
    ])
    print(f"\nConfusion matrix C (column-stochastic):")
    print(C)
    print(f"Valid: {validate_confusion_matrix(C)}")
    print(f"Condition number: {np.linalg.cond(C):.1f}")

    # 2. Compute bias
    print("\n--- Bias Analysis ---")
    result = compute_bias("confounding", C)
    print(f"tau_true  (no misclassification): {result['tau_true']:.4f}")
    print(f"tau_biased (with C):              {result['tau_biased']:.4f}")
    print(f"bias:                             {result['bias']:+.4f}")
    print(f"bias_pct:                         {result['bias_pct']:+.2f}%")

    # Try all predefined matrices
    print(f"\nBias across predefined matrices:")
    print(f"  {'Matrix':<22} {'tau_biased':>10} {'bias':>10} {'bias_pct':>10}")
    print(f"  {'-'*55}")
    for name, Ci in predefined_matrices().items():
        r = compute_bias("confounding", Ci)
        print(f"  {name:<22} {r['tau_biased']:>10.4f} {r['bias']:>+10.4f} "
              f"{r['bias_pct']:>+9.2f}%")

    # 3. Compute ASV
    print("\n--- ASV Analysis ---")
    C0 = C.copy()
    asv_result = compute_asv("confounding", C0, threshold_type="magnitude",
                             threshold_value=0.1)
    asv_val = asv_result["asv"]
    print(f"tau_true:      {asv_result['tau_true']:.4f}")
    if asv_val is not None:
        print(f"Magnitude ASV: {asv_val:.3f} "
              f"(bias exceeds 10% of tau at delta={asv_val:.3f})")
    else:
        print(f"Magnitude ASV: None (threshold never crossed)")

    asv_sf = compute_asv("confounding", C0, threshold_type="sign_flip")
    sf_val = asv_sf["asv"]
    if sf_val is not None:
        print(f"Sign-flip ASV: {sf_val:.3f}")
    else:
        print(f"Sign-flip ASV: None (sign never flips)")

    # 4. Correction recommendation
    print("\n--- Correction Recommendation ---")
    rec_gold = recommend_correction("confounding", C, has_gold=True,
                                    gold_fraction=0.1)
    print(f"With gold labels:    {rec_gold['recommended']}")
    for note in rec_gold["notes"]:
        print(f"  - {note}")

    rec_no_gold = recommend_correction("confounding", C, has_gold=False)
    print(f"Without gold labels: {rec_no_gold['recommended']}")
    for note in rec_no_gold["notes"]:
        print(f"  - {note}")

    print(f"\nMethod ranking (with gold):")
    for m in rec_gold["ranking"]:
        app = "Y" if m["applicable"] else "N"
        print(f"  {m['method']:<16} applicable={app}  "
              f"expected_bias_reduction={m['expected_bias_reduction']:+.1%}")

    # 5. Optional: plot bias curve
    try:
        import matplotlib
        matplotlib.use("Agg")
        import matplotlib.pyplot as plt

        fig, ax = plt.subplots(1, 1, figsize=(6, 4))
        deltas = asv_result["deltas"]
        ax.plot(deltas, asv_result["bias_curve"], "b-", alpha=0.4,
                label="Pointwise |bias|")
        ax.plot(deltas, asv_result["envelope"], "r-", linewidth=2,
                label="Monotone envelope")
        thresh = 0.1 * abs(asv_result["tau_true"])
        ax.axhline(thresh, color="gray", linestyle="--", label=f"10% threshold")
        if asv_val is not None:
            ax.axvline(asv_val, color="green", linestyle=":", label=f"ASV={asv_val:.2f}")
        ax.set_xlabel(r"$\delta$ (interpolation parameter)")
        ax.set_ylabel("|Bias|")
        ax.set_title("Confounding K=3: ASV Bias Curve")
        ax.legend(fontsize=8)
        ax.set_xlim(0, min(deltas[-1], 5))

        out_path = os.path.join(os.path.dirname(__file__), "..", "..",
                                "artifacts", "example_bias_curve.png")
        os.makedirs(os.path.dirname(out_path), exist_ok=True)
        fig.savefig(out_path, dpi=150, bbox_inches="tight")
        plt.close()
        print(f"\nPlot saved to {out_path}")
    except ImportError:
        print("\nmatplotlib not available, skipping plot")

    print("\nDone.")


if __name__ == "__main__":
    main()
