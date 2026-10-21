"""
EXP-B: 14D Ablation — drop self_bleu, retrain OBD-LightGBM, report K* and pairwise AUC.
Addresses Reviewer FR-3.
"""

import csv
import json
import sys
from pathlib import Path

import numpy as np
import lightgbm as lgb
from sklearn.model_selection import GroupKFold
from sklearn.metrics import roc_auc_score

ALL_15D = [
    "surp_mean", "surp_std", "surp_skew", "surp_kurt",
    "surp_d1_mean", "surp_d1_std", "surp_d1_skew",
    "surp_d2_mean", "surp_d2_std",
    "ttr", "hapax_ratio", "self_bleu",
    "freq_kurtosis", "freq_entropy", "low_freq_ratio",
]

ALL_14D = [c for c in ALL_15D if c != "self_bleu"]

DATASETS = {
    "qwen_rw":   "/root/autodl-tmp/gen-depth-contamination/data/features.csv",
    "pythia":    "/root/autodl-tmp/gen-depth-contamination/data_exp001_pythia/features.csv",
    "olmo":      "/root/autodl-tmp/gen-depth-contamination/data_exp002_olmo/features.csv",
    "qwen_cont": "/root/autodl-tmp/gen-depth-contamination/data_exp017_qwen_cont/features.csv",
}

REFERENCE_15D = {
    "qwen_rw":   {"0v1": 0.9956, "1v2": 0.6955, "2v3": 0.5893, "3v4": None, "4v5": None},
    "pythia":    {"0v1": 0.9932, "1v2": 0.6539, "2v3": 0.5514, "3v4": None, "4v5": None},
    "olmo":      {"0v1": 0.9970, "1v2": 0.6145, "2v3": 0.5496, "3v4": None, "4v5": None},
    "qwen_cont": {"0v1": 0.9971, "1v2": 0.6112, "2v3": 0.5609, "3v4": None, "4v5": None},
}

LGB_PARAMS = dict(
    n_estimators=200, max_depth=6, learning_rate=0.05,
    num_leaves=31, verbose=-1, n_jobs=-1,
)

THETA = 0.60


def load_data(csv_path, feat_cols):
    with open(csv_path) as f:
        reader = csv.DictReader(f)
        rows = list(reader)
    depths = np.array([int(r["depth"]) for r in rows])
    doc_ids = np.array([int(r["doc_id"]) for r in rows])
    feat = np.array(
        [[float(r[c]) if r[c] not in ("", "nan") else np.nan for c in feat_cols] for r in rows]
    )
    col_means = np.nanmean(feat, axis=0)
    for j in range(feat.shape[1]):
        mask = np.isnan(feat[:, j])
        feat[mask, j] = col_means[j]
    return depths, doc_ids, feat


def pairwise_auc_and_kstar(depths, doc_ids, feat, max_depth=5):
    pairwise = {}
    for k in range(1, max_depth + 1):
        mask = (depths == k - 1) | (depths == k)
        X = feat[mask]
        y = (depths[mask] == k).astype(int)
        if len(np.unique(y)) < 2:
            pairwise[f"{k-1}v{k}"] = float("nan")
            continue
        gkf = GroupKFold(n_splits=5)
        groups = doc_ids[mask]
        fold_aucs = []
        for train_idx, test_idx in gkf.split(X, y, groups=groups):
            clf = lgb.LGBMClassifier(**LGB_PARAMS)
            clf.fit(X[train_idx], y[train_idx])
            proba = clf.predict_proba(X[test_idx])[:, 1]
            fold_aucs.append(roc_auc_score(y[test_idx], proba))
        pairwise[f"{k-1}v{k}"] = round(float(np.mean(fold_aucs)), 4)

    k_star = 0
    for k in range(1, max_depth + 1):
        if pairwise.get(f"{k-1}v{k}", 0) > THETA:
            k_star = k
    return pairwise, k_star


def main():
    out_path = Path("/root/autodl-tmp/gen-depth-contamination/artifacts/exp_B_14d_ablation.json")
    out_path.parent.mkdir(parents=True, exist_ok=True)

    results = {}
    for name, csv_path in DATASETS.items():
        print(f"\n{'='*60}")
        print(f"  {name}: {csv_path}")
        print(f"{'='*60}")

        if not Path(csv_path).exists():
            print(f"  SKIP: file not found")
            results[name] = {"error": "file not found"}
            continue

        depths, doc_ids, feat_15d = load_data(csv_path, ALL_15D)
        depths_14, doc_ids_14, feat_14d = load_data(csv_path, ALL_14D)

        max_depth = int(depths.max())

        print(f"  Samples: {len(depths)}, max_depth={max_depth}")
        print(f"  Running 15D (for local comparison)...")
        auc_15d, kstar_15d = pairwise_auc_and_kstar(depths, doc_ids, feat_15d, max_depth)
        print(f"    15D pairwise AUC: {auc_15d}")
        print(f"    15D K*={kstar_15d}")

        print(f"  Running 14D (no self_bleu)...")
        auc_14d, kstar_14d = pairwise_auc_and_kstar(depths_14, doc_ids_14, feat_14d, max_depth)
        print(f"    14D pairwise AUC: {auc_14d}")
        print(f"    14D K*={kstar_14d}")

        delta = {}
        for key in auc_14d:
            v15 = auc_15d.get(key)
            v14 = auc_14d.get(key)
            if v15 is not None and v14 is not None and not (np.isnan(v15) or np.isnan(v14)):
                delta[key] = round(v14 - v15, 4)

        results[name] = {
            "14d": {"k_star": kstar_14d, "pairwise_auc": auc_14d},
            "15d": {"k_star": kstar_15d, "pairwise_auc": auc_15d},
            "delta": delta,
        }

    all_deltas = []
    for name, r in results.items():
        if "delta" in r:
            for k, v in r["delta"].items():
                all_deltas.append(v)

    mean_delta = round(float(np.mean(all_deltas)), 4) if all_deltas else None

    kstar_unchanged = all(
        r.get("14d", {}).get("k_star") == r.get("15d", {}).get("k_star")
        for r in results.values() if "14d" in r
    )

    if kstar_unchanged and mean_delta is not None and abs(mean_delta) < 0.01:
        conclusion = (
            f"Removing self_bleu has negligible impact: mean AUC delta = {mean_delta:.4f}, "
            f"K* unchanged across all 4 configs. The 15D→14D reduction is safe."
        )
    elif kstar_unchanged:
        conclusion = (
            f"K* unchanged across all 4 configs. Mean AUC delta = {mean_delta:.4f}."
        )
    else:
        conclusion = (
            f"K* changed in some configs. Mean AUC delta = {mean_delta}. "
            f"self_bleu removal has non-trivial impact."
        )

    results["mean_auc_delta"] = mean_delta
    results["conclusion"] = conclusion

    with open(out_path, "w") as f:
        json.dump(results, f, indent=2)
    print(f"\nResults saved to {out_path}")
    print(f"Conclusion: {conclusion}")


if __name__ == "__main__":
    main()
