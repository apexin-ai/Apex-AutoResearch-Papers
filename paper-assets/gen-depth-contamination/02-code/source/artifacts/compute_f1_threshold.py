"""
Compute F1@optimal-threshold for all depth pairs using OOF predictions.

For each config × depth pair:
  1. Build binary dataset (depth k → 0, depth k+1 → 1)
  2. 5-fold GroupKFold LightGBM → OOF predicted probabilities
  3. Sweep thresholds 0.01–0.99 to find F1-maximizing threshold
  4. Report F1*, threshold*, precision, recall, and reference AUC
"""

import csv
import json
import os
import time
from pathlib import Path

import numpy as np
import lightgbm as lgb
from sklearn.model_selection import GroupKFold
from sklearn.metrics import roc_auc_score, f1_score, precision_score, recall_score

BASE = Path("/root/autodl-tmp/gen-depth-contamination")
OUT_DIR = BASE / "results" / "f1_optimal_threshold"
OUT_DIR.mkdir(parents=True, exist_ok=True)

FEAT_COLS = [
    "surp_mean", "surp_std", "surp_skew", "surp_kurt",
    "surp_d1_mean", "surp_d1_std", "surp_d1_skew",
    "surp_d2_mean", "surp_d2_std",
    "ttr", "hapax_ratio", "self_bleu",
    "freq_kurtosis", "freq_entropy", "low_freq_ratio",
]

CONFIGS = {
    "Qwen-base":      BASE / "data_exp016_qwen_base" / "features.csv",
    "Pythia-nuc0.9":   BASE / "data_exp020_pythia_nuc09" / "features.csv",
    "Pythia-greedy":   BASE / "data_exp020_pythia_greedy" / "features.csv",
    "Pythia-T0.7":     BASE / "data_exp020_pythia_t07" / "features.csv",
    "Pythia-T1.2":     BASE / "data_exp020_pythia_t12" / "features.csv",
    "Mistral-7B":      BASE / "data_exp019_mistral7b" / "features.csv",
    "LLaMA-8B":        BASE / "data" / "exp_018_llama8b" / "features.csv",
}

DEPTH_PAIRS = [(0,1), (1,2), (2,3), (3,4), (4,5)]
THRESHOLDS = np.arange(0.01, 1.00, 0.01)


def load_features(path):
    with open(path) as f:
        rows = list(csv.DictReader(f))
    depths = np.array([int(r["depth"]) for r in rows])
    doc_ids = np.array([int(r["doc_id"]) for r in rows])
    X = np.array(
        [[float(r[c]) if r[c] not in ("", "nan") else np.nan for c in FEAT_COLS]
         for r in rows]
    )
    col_means = np.nanmean(X, axis=0)
    for j in range(X.shape[1]):
        mask = np.isnan(X[:, j])
        X[mask, j] = col_means[j]
    return X, depths, doc_ids


def get_oof_predictions(X, y, groups):
    gkf = GroupKFold(n_splits=5)
    oof_proba = np.zeros(len(y))
    for train_idx, test_idx in gkf.split(X, y, groups=groups):
        clf = lgb.LGBMClassifier(
            n_estimators=200, max_depth=6, learning_rate=0.05,
            num_leaves=31, verbose=-1, n_jobs=-1,
        )
        clf.fit(X[train_idx], y[train_idx])
        oof_proba[test_idx] = clf.predict_proba(X[test_idx])[:, 1]
    return oof_proba


def optimal_f1(y_true, proba, thresholds):
    best_f1, best_thr, best_p, best_r = 0.0, 0.5, 0.0, 0.0
    for thr in thresholds:
        y_pred = (proba >= thr).astype(int)
        if y_pred.sum() == 0 or y_pred.sum() == len(y_pred):
            continue
        f1 = f1_score(y_true, y_pred)
        if f1 > best_f1:
            best_f1 = f1
            best_thr = thr
            best_p = precision_score(y_true, y_pred)
            best_r = recall_score(y_true, y_pred)
    return best_f1, best_thr, best_p, best_r


def main():
    t0 = time.time()
    all_results = {}

    for config_name, feat_path in CONFIGS.items():
        if not feat_path.exists():
            print(f"SKIP {config_name}: {feat_path} not found")
            continue
        print(f"\n{'='*60}")
        print(f"Config: {config_name}")
        print(f"{'='*60}")

        X_all, depths_all, doc_ids_all = load_features(feat_path)
        config_results = {}

        for d_lo, d_hi in DEPTH_PAIRS:
            pair_key = f"{d_lo}v{d_hi}"
            mask = (depths_all == d_lo) | (depths_all == d_hi)
            if mask.sum() == 0:
                print(f"  {pair_key}: no data")
                continue

            X = X_all[mask]
            y = (depths_all[mask] == d_hi).astype(int)
            groups = doc_ids_all[mask]

            oof_proba = get_oof_predictions(X, y, groups)
            auc = roc_auc_score(y, oof_proba)
            f1, thr, prec, rec = optimal_f1(y, oof_proba, THRESHOLDS)

            config_results[pair_key] = {
                "auc": round(auc, 4),
                "f1_optimal": round(f1, 4),
                "threshold": round(thr, 2),
                "precision": round(prec, 4),
                "recall": round(rec, 4),
            }
            print(f"  {pair_key}: AUC={auc:.4f}  F1*={f1:.4f} @thr={thr:.2f}  P={prec:.4f} R={rec:.4f}")

        all_results[config_name] = config_results

    # Save JSON
    out_json = OUT_DIR / "f1_optimal_results.json"
    with open(out_json, "w") as f:
        json.dump(all_results, f, indent=2)
    print(f"\nSaved: {out_json}")

    # Print summary table
    print(f"\n{'='*100}")
    print("SUMMARY TABLE: F1@optimal-threshold (threshold)")
    print(f"{'='*100}")
    header = f"{'Config':<18}"
    for d_lo, d_hi in DEPTH_PAIRS:
        header += f" {'%dv%d F1 (thr)' % (d_lo, d_hi):>16}"
    print(header)
    print("-" * 100)

    for config_name, res in all_results.items():
        row = f"{config_name:<18}"
        for d_lo, d_hi in DEPTH_PAIRS:
            pk = f"{d_lo}v{d_hi}"
            if pk in res:
                r = res[pk]
                row += f" {r['f1_optimal']:.4f} ({r['threshold']:.2f})"
            else:
                row += f" {'—':>16}"
        print(row)

    # Also print AUC comparison
    print(f"\n{'='*100}")
    print("REFERENCE: Pairwise AUC (for comparison)")
    print(f"{'='*100}")
    header = f"{'Config':<18}"
    for d_lo, d_hi in DEPTH_PAIRS:
        header += f" {'%dv%d AUC' % (d_lo, d_hi):>12}"
    print(header)
    print("-" * 100)
    for config_name, res in all_results.items():
        row = f"{config_name:<18}"
        for d_lo, d_hi in DEPTH_PAIRS:
            pk = f"{d_lo}v{d_hi}"
            if pk in res:
                row += f" {res[pk]['auc']:>12.4f}"
            else:
                row += f" {'—':>12}"
        print(row)

    print(f"\nTotal time: {time.time()-t0:.1f}s")


if __name__ == "__main__":
    main()
