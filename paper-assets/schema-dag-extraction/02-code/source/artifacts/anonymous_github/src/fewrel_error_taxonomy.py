"""FewRel error taxonomy analysis: classify predictions by BCS bin.

Adapts NER error taxonomy (exp-007) to Relation Extraction.
For RE, errors are:
  - correct: prediction == ground_truth
  - wrong_type_intra: prediction != ground_truth, prediction in batch_types
  - wrong_type_extra: prediction != ground_truth, prediction not in batch_types, prediction != "none"
  - missed: prediction == "none" (or empty)

Input:
  - artifacts/fewrel_formal_full/predictions_exp1.json
  - artifacts/fewrel_formal_full/predictions_exp2.json
Output:
  - artifacts/fewrel_80rel_error_taxonomy.json
"""

import json
import os
from collections import defaultdict

import numpy as np
from scipy.stats import spearmanr

BASE_DIR = "."
ARTIFACTS_DIR = os.path.join(BASE_DIR, "artifacts", "fewrel_formal_full")
OUT_PATH = os.path.join(BASE_DIR, "artifacts", "fewrel_80rel_error_taxonomy.json")

BCS_BINS = [
    ("zero",      0.0,   0.001),
    ("low",       0.001, 0.65),
    ("medium",    0.65,  0.80),
    ("high",      0.80,  0.95),
    ("very_high", 0.95,  1.001),
]


def classify_prediction(pred):
    gt = pred["ground_truth"].strip().lower()
    p = pred["prediction"].strip().lower()
    batch_types = {t.strip().lower() for t in pred["batch_types"]}

    if p == gt:
        return "correct"
    if p in ("none", ""):
        return "missed"
    if p in batch_types:
        return "wrong_type_intra"
    return "wrong_type_extra"


def get_bin(bcs):
    for name, lo, hi in BCS_BINS:
        if lo <= bcs < hi:
            return name
    return "unknown"


def main():
    all_preds = []
    for fname in ["predictions_exp1.json", "predictions_exp2.json"]:
        path = os.path.join(ARTIFACTS_DIR, fname)
        with open(path) as f:
            preds = json.load(f)
        for p in preds:
            p["_source"] = fname.replace("predictions_", "").replace(".json", "")
        all_preds.extend(preds)
        print(f"Loaded {len(preds)} predictions from {fname}")

    print(f"Total predictions: {len(all_preds)}")

    # Classify each prediction
    for p in all_preds:
        p["_error_type"] = classify_prediction(p)

    # === Per-batch aggregation ===
    batch_data = defaultdict(lambda: {"preds": [], "bcs": None})
    for p in all_preds:
        bid = p["batch_id"]
        batch_data[bid]["preds"].append(p)
        batch_data[bid]["bcs"] = p["batch_bcs"]

    batch_stats = []
    for bid, bd in sorted(batch_data.items()):
        counts = defaultdict(int)
        for p in bd["preds"]:
            counts[p["_error_type"]] += 1
        total = len(bd["preds"])
        wrong_type = counts["wrong_type_intra"] + counts["wrong_type_extra"]
        batch_stats.append({
            "batch_id": bid,
            "bcs": bd["bcs"],
            "total": total,
            "correct": counts["correct"],
            "wrong_type_intra": counts["wrong_type_intra"],
            "wrong_type_extra": counts["wrong_type_extra"],
            "missed": counts["missed"],
            "wrong_type_rate": wrong_type / total if total > 0 else 0,
            "intra_sub_rate": counts["wrong_type_intra"] / total if total > 0 else 0,
            "accuracy": counts["correct"] / total if total > 0 else 0,
        })

    # === BCS bin aggregation ===
    bin_agg = {name: {"correct": 0, "wrong_type_intra": 0, "wrong_type_extra": 0,
                       "missed": 0, "total": 0, "bcs_values": [], "n_batches": 0}
               for name, _, _ in BCS_BINS}

    for bs in batch_stats:
        b = get_bin(bs["bcs"])
        if b == "unknown":
            continue
        agg = bin_agg[b]
        agg["correct"] += bs["correct"]
        agg["wrong_type_intra"] += bs["wrong_type_intra"]
        agg["wrong_type_extra"] += bs["wrong_type_extra"]
        agg["missed"] += bs["missed"]
        agg["total"] += bs["total"]
        agg["bcs_values"].append(bs["bcs"])
        agg["n_batches"] += 1

    bin_results = []
    for name, lo, hi in BCS_BINS:
        agg = bin_agg[name]
        t = agg["total"]
        if t == 0:
            continue
        wt = agg["wrong_type_intra"] + agg["wrong_type_extra"]
        bin_results.append({
            "bin": name,
            "bcs_range": [lo, hi],
            "mean_bcs": float(np.mean(agg["bcs_values"])) if agg["bcs_values"] else 0,
            "n_batches": agg["n_batches"],
            "total": t,
            "correct": agg["correct"],
            "correct_rate": round(agg["correct"] / t, 4),
            "wrong_type_intra": agg["wrong_type_intra"],
            "wrong_type_extra": agg["wrong_type_extra"],
            "wrong_type_total": wt,
            "wrong_type_rate": round(wt / t, 4),
            "intra_sub_rate": round(agg["wrong_type_intra"] / t, 4),
            "missed": agg["missed"],
            "missed_rate": round(agg["missed"] / t, 4),
        })

    # === Spearman correlations (per-batch level) ===
    bcs_arr = np.array([bs["bcs"] for bs in batch_stats])
    wt_rate_arr = np.array([bs["wrong_type_rate"] for bs in batch_stats])
    intra_rate_arr = np.array([bs["intra_sub_rate"] for bs in batch_stats])
    acc_arr = np.array([bs["accuracy"] for bs in batch_stats])

    rho_wt, p_wt = spearmanr(bcs_arr, wt_rate_arr)
    rho_intra, p_intra = spearmanr(bcs_arr, intra_rate_arr)
    rho_acc, p_acc = spearmanr(bcs_arr, acc_arr)

    correlations = {
        "wrong_type_rate_vs_bcs": {"rho": round(rho_wt, 4), "p": round(p_wt, 6)},
        "intra_sub_rate_vs_bcs": {"rho": round(rho_intra, 4), "p": round(p_intra, 6)},
        "accuracy_vs_bcs": {"rho": round(rho_acc, 4), "p": round(p_acc, 6)},
        "n_batches": len(batch_stats),
    }

    # === Print summary ===
    print("\n" + "=" * 80)
    print("FewRel 80-rel Error Taxonomy by BCS Bin")
    print("=" * 80)
    header = f"{'Bin':<12} {'BCS_mean':>8} {'N':>5} {'Total':>6} {'Correct%':>9} {'WrongType%':>11} {'IntraSub%':>10} {'Missed%':>8}"
    print(header)
    print("-" * 80)
    for br in bin_results:
        print(f"{br['bin']:<12} {br['mean_bcs']:>8.4f} {br['n_batches']:>5} {br['total']:>6} "
              f"{br['correct_rate']:>9.4f} {br['wrong_type_rate']:>11.4f} "
              f"{br['intra_sub_rate']:>10.4f} {br['missed_rate']:>8.4f}")

    print("\n" + "=" * 80)
    print("Spearman Correlations (per-batch)")
    print("=" * 80)
    for k, v in correlations.items():
        if k == "n_batches":
            print(f"  n_batches = {v}")
        else:
            print(f"  {k}: rho={v['rho']:.4f}, p={v['p']:.6f}")

    # === Save ===
    output = {
        "task": "FewRel_80rel",
        "analysis": "error_taxonomy_by_bcs",
        "bin_results": bin_results,
        "correlations": correlations,
        "per_batch_stats": batch_stats,
    }
    with open(OUT_PATH, "w") as f:
        json.dump(output, f, indent=2, ensure_ascii=False)
    print(f"\nSaved to {OUT_PATH}")


if __name__ == "__main__":
    main()
