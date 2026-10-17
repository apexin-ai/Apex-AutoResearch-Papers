"""W2: Realistic practical effect calculation for BCS-accuracy relationship.

Input: FewRel 80-pool 16-sub 100 random batches (results_incremental.jsonl)
Output: Typical BCS range (IQR), expected accuracy gap under typical conditions
Method: Compute Q1/Q3 of random batch BCS, use regression slope for expected gap
"""

import json
import logging
from pathlib import Path

import numpy as np
from scipy import stats

ROOT = Path(".")
DATA_FILE = ROOT / "artifacts" / "fewrel_80pool_16sub" / "results_incremental.jsonl"
CI_FILE = ROOT / "artifacts" / "fewrel_80pool_16sub" / "bootstrap_ci.json"
OUTPUT = ROOT / "scripts" / "d037" / "w2_practical_effect_results.json"
SEED = 42
B = 10_000

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(message)s")
logger = logging.getLogger(__name__)


def main():
    # Load raw batch data
    batches = []
    with open(DATA_FILE) as f:
        for line in f:
            if line.strip():
                batches.append(json.loads(line))
    logger.info("Loaded %d batches", len(batches))

    bcs_arr = np.array([b["bcs"] for b in batches])
    acc_arr = np.array([b["accuracy"] for b in batches])

    # Load pre-computed regression
    with open(CI_FILE) as f:
        ci_data = json.load(f)
    slope_info = ci_data["regression_slope"]

    # BCS distribution
    bcs_q1 = float(np.percentile(bcs_arr, 25))
    bcs_q3 = float(np.percentile(bcs_arr, 75))
    bcs_iqr = bcs_q3 - bcs_q1
    bcs_p10 = float(np.percentile(bcs_arr, 10))
    bcs_p90 = float(np.percentile(bcs_arr, 90))

    # Accuracy distribution
    acc_q1 = float(np.percentile(acc_arr, 25))
    acc_q3 = float(np.percentile(acc_arr, 75))
    acc_iqr_pp = (acc_q3 - acc_q1) * 100

    # Regression-based expected gap
    slope = slope_info["slope"]
    expected_gap_iqr_pp = abs(slope) * bcs_iqr * 100
    expected_gap_p10_p90_pp = abs(slope) * (bcs_p90 - bcs_p10) * 100

    # Direct accuracy gap: compare Q1-BCS batches vs Q3-BCS batches
    low_bcs_mask = bcs_arr <= bcs_q1
    high_bcs_mask = bcs_arr >= bcs_q3
    acc_low_bcs = float(np.mean(acc_arr[low_bcs_mask]))
    acc_high_bcs = float(np.mean(acc_arr[high_bcs_mask]))
    direct_gap_pp = (acc_low_bcs - acc_high_bcs) * 100

    # Bootstrap CI for the IQR-based gap
    rng = np.random.RandomState(SEED)
    boot_gaps = np.empty(B)
    n = len(bcs_arr)
    for i in range(B):
        idx = rng.randint(0, n, size=n)
        b_bcs = bcs_arr[idx]
        b_acc = acc_arr[idx]
        b_slope = stats.linregress(b_bcs, b_acc).slope
        b_q1 = np.percentile(b_bcs, 25)
        b_q3 = np.percentile(b_bcs, 75)
        boot_gaps[i] = abs(b_slope) * (b_q3 - b_q1) * 100

    results = {
        "n_batches": len(batches),
        "bcs_distribution": {
            "mean": round(float(np.mean(bcs_arr)), 4),
            "std": round(float(np.std(bcs_arr)), 4),
            "Q1": round(bcs_q1, 4),
            "median": round(float(np.median(bcs_arr)), 4),
            "Q3": round(bcs_q3, 4),
            "IQR": round(bcs_iqr, 4),
            "P10": round(bcs_p10, 4),
            "P90": round(bcs_p90, 4),
            "min": round(float(np.min(bcs_arr)), 4),
            "max": round(float(np.max(bcs_arr)), 4),
        },
        "accuracy_distribution": {
            "mean": round(float(np.mean(acc_arr)), 4),
            "std": round(float(np.std(acc_arr)), 4),
            "Q1": round(acc_q1, 4),
            "median": round(float(np.median(acc_arr)), 4),
            "Q3": round(acc_q3, 4),
            "IQR_pp": round(acc_iqr_pp, 2),
        },
        "regression": {
            "slope": round(slope, 4),
            "slope_ci_95": [round(slope_info["bootstrap_ci_95"][0], 4),
                            round(slope_info["bootstrap_ci_95"][1], 4)],
            "r_value": round(slope_info["r_value"], 4),
            "p_value": round(slope_info["p_value"], 6),
        },
        "typical_effect_iqr": {
            "bcs_span": round(bcs_iqr, 4),
            "expected_acc_gap_pp": round(expected_gap_iqr_pp, 2),
            "bootstrap_ci_pp": [round(float(np.percentile(boot_gaps, 2.5)), 2),
                                round(float(np.percentile(boot_gaps, 97.5)), 2)],
            "note": "Expected accuracy gap from BCS Q1 to Q3 via regression slope",
        },
        "typical_effect_p10_p90": {
            "bcs_span": round(float(bcs_p90 - bcs_p10), 4),
            "expected_acc_gap_pp": round(expected_gap_p10_p90_pp, 2),
        },
        "direct_quartile_comparison": {
            "n_low_bcs": int(np.sum(low_bcs_mask)),
            "n_high_bcs": int(np.sum(high_bcs_mask)),
            "mean_acc_low_bcs": round(acc_low_bcs, 4),
            "mean_acc_high_bcs": round(acc_high_bcs, 4),
            "direct_gap_pp": round(direct_gap_pp, 2),
        },
        "extreme_batch_reference": {
            "gap_pp": 31.2,
            "note": "From min-BCS vs max-BCS batches in 80-rel pool (not typical)",
        },
        "ratio_typical_to_extreme": round(expected_gap_iqr_pp / 31.2, 2),
    }

    with open(OUTPUT, "w") as f:
        json.dump(results, f, indent=2)
    logger.info("Saved -> %s", OUTPUT)

    print("\n" + "=" * 70)
    print("W2: REALISTIC PRACTICAL EFFECT (B=%d)" % B)
    print("=" * 70)
    bd = results["bcs_distribution"]
    print(f"\nBCS distribution (n={results['n_batches']} random batches):")
    print(f"  Q1={bd['Q1']:.4f}, median={bd['median']:.4f}, Q3={bd['Q3']:.4f}, IQR={bd['IQR']:.4f}")
    print(f"  P10={bd['P10']:.4f}, P90={bd['P90']:.4f}")
    te = results["typical_effect_iqr"]
    print(f"\nTypical effect (IQR-based):")
    print(f"  BCS span (Q1->Q3): {te['bcs_span']:.4f}")
    print(f"  Expected accuracy gap: {te['expected_acc_gap_pp']:.2f}pp [{te['bootstrap_ci_pp'][0]:.2f}, {te['bootstrap_ci_pp'][1]:.2f}]pp")
    te2 = results["typical_effect_p10_p90"]
    print(f"\nWider range (P10->P90):")
    print(f"  BCS span: {te2['bcs_span']:.4f}")
    print(f"  Expected accuracy gap: {te2['expected_acc_gap_pp']:.2f}pp")
    dq = results["direct_quartile_comparison"]
    print(f"\nDirect quartile comparison:")
    print(f"  Low BCS batches (n={dq['n_low_bcs']}): mean acc={dq['mean_acc_low_bcs']:.4f}")
    print(f"  High BCS batches (n={dq['n_high_bcs']}): mean acc={dq['mean_acc_high_bcs']:.4f}")
    print(f"  Direct gap: {dq['direct_gap_pp']:.2f}pp")
    print(f"\nExtreme batch gap: {results['extreme_batch_reference']['gap_pp']}pp")
    print(f"Ratio typical/extreme: {results['ratio_typical_to_extreme']:.2f}")
    print("=" * 70)


if __name__ == "__main__":
    main()
