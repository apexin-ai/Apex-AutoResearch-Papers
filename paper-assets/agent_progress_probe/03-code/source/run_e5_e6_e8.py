#!/usr/bin/env python3
"""E5 + E6 + E8 statistical tests batch.

E5: 11 vs 30 features paired bootstrap (cross-agent)
E6: κ bootstrap CIs (Fleiss + pairwise Cohen's) on N=52 3-annotator windows
E8: GB on Set A (conf≥3) stagnation breakdown
"""

import csv
import json
import sys
from collections import defaultdict
from pathlib import Path

import numpy as np

BASE = Path(__file__).parent
GOLD_DIR = BASE / "artifacts" / "gold_set"


# ====================================================================
# E6: κ Bootstrap CI
# ====================================================================

def load_annotations_by_batch():
    """Load annotations from 3 batches (= 3 annotators).
    batch1 = b1, batch2 = b2, batch3a+batch3b = b3.
    Returns dict: window_key -> {b1: label, b2: label, b3: label}
    """
    def read_batch(path):
        rows = {}
        with open(path) as f:
            reader = csv.DictReader(f)
            for row in reader:
                tid = row["trajectory_id"].strip('"')
                widx = int(row["window_idx"])
                key = f"{tid}__w{widx}"
                label = 1 if row["annotator_label"] == "progress" else 0
                rows[key] = label
        return rows

    b1 = read_batch(GOLD_DIR / "annotation_unknown_2026-05-15.csv")
    b2 = read_batch(GOLD_DIR / "annotation_unknown_2026-05-15_batch2.csv")
    b3a = read_batch(GOLD_DIR / "annotation_unknown_2026-05-15_batch3a.csv")
    b3b = read_batch(GOLD_DIR / "annotation_unknown_2026-05-15_batch3b.csv")
    b3 = {**b3a, **b3b}

    all_keys = set(b1) | set(b2) | set(b3)
    three_annotator_keys = sorted(set(b1) & set(b2) & set(b3))

    annotations = {}
    for key in three_annotator_keys:
        annotations[key] = [b1[key], b2[key], b3[key]]

    return annotations, b1, b2, b3


def fleiss_kappa(ratings_matrix):
    """Compute Fleiss' kappa for a ratings matrix (n_subjects x n_categories)."""
    n, k = ratings_matrix.shape
    N = ratings_matrix.sum(axis=1)[0]  # number of raters per subject

    p_j = ratings_matrix.sum(axis=0) / (n * N)
    P_i = (ratings_matrix ** 2).sum(axis=1) - N
    P_i = P_i / (N * (N - 1))

    P_bar = P_i.mean()
    P_e = (p_j ** 2).sum()

    if P_e == 1.0:
        return 1.0
    return (P_bar - P_e) / (1.0 - P_e)


def cohens_kappa(labels_a, labels_b):
    """Compute Cohen's kappa for two annotators."""
    n = len(labels_a)
    assert n == len(labels_b)
    agree = sum(a == b for a, b in zip(labels_a, labels_b))
    p_o = agree / n

    cats = sorted(set(labels_a) | set(labels_b))
    p_e = 0
    for c in cats:
        p_a = sum(1 for x in labels_a if x == c) / n
        p_b = sum(1 for x in labels_b if x == c) / n
        p_e += p_a * p_b

    if p_e == 1.0:
        return 1.0
    return (p_o - p_e) / (1.0 - p_e)


def build_fleiss_matrix(annotations_list):
    """Build Fleiss ratings matrix from list of [b1, b2, b3] labels."""
    n = len(annotations_list)
    matrix = np.zeros((n, 2), dtype=float)  # 2 categories: 0=stag, 1=prog
    for i, labels in enumerate(annotations_list):
        for l in labels:
            matrix[i, l] += 1
    return matrix


def run_e6():
    print("=" * 60)
    print("E6: κ Bootstrap CI (N=52, 3 annotators)")
    print("=" * 60)

    annotations, b1, b2, b3 = load_annotations_by_batch()
    keys = sorted(annotations.keys())
    n = len(keys)
    print(f"Three-annotator windows: {n}")

    labels_b1 = [annotations[k][0] for k in keys]
    labels_b2 = [annotations[k][1] for k in keys]
    labels_b3 = [annotations[k][2] for k in keys]

    # Point estimates
    matrix = build_fleiss_matrix([annotations[k] for k in keys])
    fk = fleiss_kappa(matrix)
    ck_12 = cohens_kappa(labels_b1, labels_b2)
    ck_13 = cohens_kappa(labels_b1, labels_b3)
    ck_23 = cohens_kappa(labels_b2, labels_b3)

    print(f"\nPoint estimates:")
    print(f"  Fleiss κ     = {fk:.4f}")
    print(f"  Cohen κ b1-b2 = {ck_12:.4f}")
    print(f"  Cohen κ b1-b3 = {ck_13:.4f}")
    print(f"  Cohen κ b2-b3 = {ck_23:.4f}")

    # Verify against IAA report
    print(f"\n  (IAA report reference: Fleiss=0.39, b1-b2=0.4851, b1-b3=0.4062, b2-b3=0.3297)")

    # Bootstrap
    B = 10000
    seed = 42
    rng = np.random.RandomState(seed)

    boot_fleiss = []
    boot_ck12 = []
    boot_ck13 = []
    boot_ck23 = []

    all_annotations = [annotations[k] for k in keys]

    for _ in range(B):
        idx = rng.choice(n, n, replace=True)
        sample = [all_annotations[i] for i in idx]

        m = build_fleiss_matrix(sample)
        boot_fleiss.append(fleiss_kappa(m))

        s_b1 = [sample[i][0] for i in range(n)]
        s_b2 = [sample[i][1] for i in range(n)]
        s_b3 = [sample[i][2] for i in range(n)]
        boot_ck12.append(cohens_kappa(s_b1, s_b2))
        boot_ck13.append(cohens_kappa(s_b1, s_b3))
        boot_ck23.append(cohens_kappa(s_b2, s_b3))

    boot_fleiss = np.array(boot_fleiss)
    boot_ck12 = np.array(boot_ck12)
    boot_ck13 = np.array(boot_ck13)
    boot_ck23 = np.array(boot_ck23)

    def ci(arr, point_est, name):
        lo, hi = np.percentile(arr, [2.5, 97.5])
        mean = arr.mean()
        std = arr.std()
        print(f"  {name:20s}: {point_est:.4f}  95% CI [{lo:.4f}, {hi:.4f}]  (mean={mean:.4f}, sd={std:.4f})")
        return {"point": round(float(point_est), 4),
                "ci_lo": round(float(lo), 4),
                "ci_hi": round(float(hi), 4),
                "mean": round(float(mean), 4),
                "std": round(float(std), 4)}

    print(f"\nBootstrap CIs (B={B}, seed={seed}):")
    results = {}
    results["fleiss_kappa"] = ci(boot_fleiss, fk, "Fleiss κ")
    results["cohen_b1_b2"] = ci(boot_ck12, ck_12, "Cohen κ (b1-b2)")
    results["cohen_b1_b3"] = ci(boot_ck13, ck_13, "Cohen κ (b1-b3)")
    results["cohen_b2_b3"] = ci(boot_ck23, ck_23, "Cohen κ (b2-b3)")

    # Distribution summary
    n_prog = sum(1 for k in keys if sum(annotations[k]) >= 2)
    n_stag = n - n_prog
    n_unanimous = sum(1 for k in keys if len(set(annotations[k])) == 1)
    print(f"\n  Label distribution (MV): prog={n_prog}, stag={n_stag}")
    print(f"  Unanimous: {n_unanimous}/{n} ({100*n_unanimous/n:.1f}%)")
    print(f"  Majority 2:1: {n - n_unanimous}/{n} ({100*(n-n_unanimous)/n:.1f}%)")

    results["n"] = n
    results["n_bootstrap"] = B
    results["seed"] = seed
    results["n_unanimous"] = n_unanimous
    results["n_majority_21"] = n - n_unanimous

    # Agreement rates
    agree_12 = sum(a == b for a, b in zip(labels_b1, labels_b2)) / n
    agree_13 = sum(a == b for a, b in zip(labels_b1, labels_b3)) / n
    agree_23 = sum(a == b for a, b in zip(labels_b2, labels_b3)) / n
    print(f"\n  Pairwise agreement: b1-b2={agree_12:.4f}, b1-b3={agree_13:.4f}, b2-b3={agree_23:.4f}")
    results["pairwise_agreement"] = {
        "b1_b2": round(agree_12, 4),
        "b1_b3": round(agree_13, 4),
        "b2_b3": round(agree_23, 4),
    }

    return results


# ====================================================================
# E8: GB on Set A — stagnation breakdown
# ====================================================================

def run_e8_from_existing():
    """Analyze Set A results from existing worker output."""
    print("\n" + "=" * 60)
    print("E8: GB on Set A (conf≥3, 3-annotator) — Stagnation Breakdown")
    print("=" * 60)

    # Load Set A gold labels
    gold_a = {}
    with open(GOLD_DIR / "gold_3annotator_A.csv") as f:
        reader = csv.DictReader(f)
        for row in reader:
            gold_a[row["window_id"]] = int(row["gold_label"])

    n_total = len(gold_a)
    n_stag = sum(1 for v in gold_a.values() if v == 0)
    n_prog = sum(1 for v in gold_a.values() if v == 1)

    print(f"\nSet A: {n_total} windows ({n_prog} progress, {n_stag} stagnation)")

    # Load 3-annotator data to identify unanimous vs majority
    annotations, _, _, _ = load_annotations_by_batch()
    unanimous_keys = set()
    majority_keys = set()
    for k, labels in annotations.items():
        if len(set(labels)) == 1:
            unanimous_keys.add(k)
        else:
            majority_keys.add(k)

    # Map gold_a window_ids to annotation keys (they should match)
    gold_keys_set = set(gold_a.keys())
    anno_keys_set = set(annotations.keys())
    overlap = gold_keys_set & anno_keys_set
    print(f"  Gold-annotation overlap: {len(overlap)}/{n_total}")

    unanimous_stag = sum(1 for k in unanimous_keys if k in gold_a and gold_a[k] == 0)
    unanimous_prog = sum(1 for k in unanimous_keys if k in gold_a and gold_a[k] == 1)
    majority_stag = sum(1 for k in majority_keys if k in gold_a and gold_a[k] == 0)
    majority_prog = sum(1 for k in majority_keys if k in gold_a and gold_a[k] == 1)

    print(f"\n  Unanimous (conf=3): {len(unanimous_keys)} windows")
    print(f"    progress: {unanimous_prog}, stagnation: {unanimous_stag}")
    print(f"  Majority 2:1 (conf=2): {len(majority_keys)} windows")
    print(f"    progress: {majority_prog}, stagnation: {majority_stag}")

    # Report from worker result
    print(f"\n  From worker eval:")
    print(f"    GB on Set A: macro-F1 = 0.7210 (n=50)")
    print(f"    GB = MV on Set A (p=1.000, Δ=0)")
    print(f"    Note: Set A too small for significance (all p>0.25)")

    results = {
        "set_a_total": n_total,
        "set_a_prog": n_prog,
        "set_a_stag": n_stag,
        "unanimous_n": len(unanimous_keys),
        "unanimous_prog": unanimous_prog,
        "unanimous_stag": unanimous_stag,
        "majority_n": len(majority_keys),
        "majority_prog": majority_prog,
        "majority_stag": majority_stag,
        "gb_macro_f1_set_a": 0.7210,
        "gb_n_evaluated": 50,
        "note": "Per-window stag/prog breakdown requires server recomputation (trajectory data needed)"
    }

    return results


# ====================================================================
# E5: 11 vs 30 features (needs server data — report existing results)
# ====================================================================

def run_e5_from_existing():
    """Report E5 from existing ablation results."""
    print("\n" + "=" * 60)
    print("E5: 11 vs 30 Features Significance Test")
    print("=" * 60)

    # From worker results
    print(f"""
  Feature ablation results (from worker):

  | Feature Set    | #Feat | In-Domain F1 | Cross-Agent F1 |
  |----------------|-------|-------------|----------------|
  | Full (all 30)  |  30   |   0.9951    |    0.9674      |
  | LF-overlap     |  11   |   0.9937    |    0.9770      |
  | Residual only  |  19   |   0.9515    |    0.5656      |

  Δ (11-feat − 30-feat) = +0.0096 cross-agent

  Per-window predictions needed for paired bootstrap — data on server.
  Pointer: /root/autodl-tmp/agent_progress_probe/artifacts/feature-overlap-ablation/
    """)

    return {
        "full_30_cross_agent_f1": 0.9674,
        "lf_overlap_11_cross_agent_f1": 0.9770,
        "residual_19_cross_agent_f1": 0.5656,
        "delta_11_minus_30": 0.0096,
        "note": "Paired bootstrap requires server — per-window predictions stored there"
    }


# ====================================================================
# Main
# ====================================================================

if __name__ == "__main__":
    all_results = {}

    # E6 — can run fully locally
    all_results["E6_kappa_bootstrap"] = run_e6()

    # E8 — partial local analysis
    all_results["E8_set_a_breakdown"] = run_e8_from_existing()

    # E5 — needs server for bootstrap
    all_results["E5_feature_ablation"] = run_e5_from_existing()

    out_path = BASE / "artifacts" / "e5_e6_e8_results.json"
    out_path.parent.mkdir(parents=True, exist_ok=True)
    with open(out_path, "w") as f:
        json.dump(all_results, f, indent=2)
    print(f"\nResults saved: {out_path}")
