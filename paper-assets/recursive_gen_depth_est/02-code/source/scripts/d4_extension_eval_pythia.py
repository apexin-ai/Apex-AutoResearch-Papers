# Pythia-1.4B nucleus d4 depth extension: 5-class RF evaluation.
# d4 data and features already exist. This script runs evaluation only.

import json
import os
import shutil
import numpy as np
from scipy.stats import skew, kurtosis, entropy
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import StratifiedKFold
from sklearn.metrics import roc_auc_score

SEED = 42
np.random.seed(SEED)

BASE = "/root/autodl-tmp/recursive_gen_depth_est"
DATA_DIR = os.path.join(BASE, "data")
OUTPUT_DIR = os.path.join(BASE, "results/d4_extension_pythia")

FEATURES_D0D3 = os.path.join(DATA_DIR, "features_all.jsonl")
FEATURES_D4 = os.path.join(DATA_DIR, "features_depth_4.jsonl")
D4_TEXT = os.path.join(DATA_DIR, "depth_4.jsonl")

RESULTS_OUT = os.path.join(OUTPUT_DIR, "d4_extension_results.json")

FEATURE_NAMES = [
    "mean_ppl", "var_ppl", "skewness_ppl", "kurtosis_ppl",
    "p10_ppl", "p25_ppl", "p50_ppl", "p75_ppl", "p90_ppl",
    "mean_surprisal", "var_surprisal", "entropy_of_surprisal",
    "type_token_ratio", "hapax_ratio", "bigram_entropy", "trigram_entropy",
    "rep_2gram", "rep_3gram", "rep_4gram",
]

N_FOLDS = 5
N_ESTIMATORS = 200


def load_jsonl(path):
    records = []
    with open(path) as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            records.append(json.loads(line))
    return records


def load_features_matrix(records):
    X = np.array([[r[k] for k in FEATURE_NAMES] for r in records], dtype=np.float64)
    y = np.array([r["depth"] for r in records], dtype=np.int64)
    X = np.clip(X, -1e10, 1e10)
    X = np.nan_to_num(X, nan=0.0, posinf=1e10, neginf=-1e10)
    return X, y


def bootstrap_ci(scores, n_boot=2000, ci=0.95):
    rng = np.random.RandomState(SEED)
    boot_means = []
    for _ in range(n_boot):
        idx = rng.choice(len(scores), len(scores), replace=True)
        boot_means.append(np.mean(np.array(scores)[idx]))
    lo = np.percentile(boot_means, (1 - ci) / 2 * 100)
    hi = np.percentile(boot_means, (1 + ci) / 2 * 100)
    return float(lo), float(hi)


def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    # Copy d4 text and features to output dir
    shutil.copy2(D4_TEXT, os.path.join(OUTPUT_DIR, "depth_4.jsonl"))
    shutil.copy2(FEATURES_D4, os.path.join(OUTPUT_DIR, "features_d4.jsonl"))
    print(f"Copied depth_4.jsonl and features to {OUTPUT_DIR}")

    # Load features
    d0d3_records = load_jsonl(FEATURES_D0D3)
    d4_records = load_jsonl(FEATURES_D4)
    print(f"Loaded {len(d0d3_records)} d0-d3 features + {len(d4_records)} d4 features")

    # Filter d0-d3 only (features_all might have other depths)
    d0d3_records = [r for r in d0d3_records if r["depth"] <= 3]
    all_records = d0d3_records + d4_records
    X, y = load_features_matrix(all_records)
    labels = sorted(np.unique(y))
    print(f"Total: {len(y)} samples, classes={labels}")
    for d in labels:
        print(f"  d{d}: {np.sum(y == d)} samples")

    # 5-fold CV
    skf = StratifiedKFold(n_splits=N_FOLDS, shuffle=True, random_state=SEED)
    fold_accs = []
    all_preds = np.zeros(len(y), dtype=np.int64)
    all_probs = np.zeros((len(y), len(labels)), dtype=np.float64)
    importances = np.zeros(X.shape[1])

    for fold_i, (train_idx, test_idx) in enumerate(skf.split(X, y)):
        rf = RandomForestClassifier(n_estimators=N_ESTIMATORS, random_state=SEED, n_jobs=-1)
        rf.fit(X[train_idx], y[train_idx])
        preds = rf.predict(X[test_idx])
        probs = rf.predict_proba(X[test_idx])
        acc = np.mean(preds == y[test_idx])
        fold_accs.append(acc)
        all_preds[test_idx] = preds
        all_probs[test_idx] = probs
        importances += rf.feature_importances_
        print(f"  Fold {fold_i+1}: acc={acc:.4f}")

    importances /= N_FOLDS
    mean_acc = float(np.mean(fold_accs))
    ci_lo, ci_hi = bootstrap_ci(fold_accs)
    print(f"\n5-class accuracy: {mean_acc:.4f} [{ci_lo:.4f}, {ci_hi:.4f}]")

    # Per-class recall
    per_class_recall = {}
    for d in labels:
        mask = (y == d)
        per_class_recall[f"d{d}"] = round(float(np.mean(all_preds[mask] == d)), 4)
    print(f"Per-class recall: {per_class_recall}")

    # d3 vs d4 pairwise AUC
    d3v4_auc = None
    mask_34 = np.isin(y, [3, 4])
    if mask_34.sum() > 0:
        yt = (y[mask_34] == 4).astype(int)
        d4_idx = list(labels).index(4)
        yp = all_probs[mask_34, d4_idx]
        if len(np.unique(yt)) == 2:
            d3v4_auc = float(roc_auc_score(yt, yp))
    print(f"d3 vs d4 AUC: {d3v4_auc}")

    # All pairwise AUCs
    pairwise_aucs = {}
    for i, di in enumerate(labels):
        for j, dj in enumerate(labels):
            if di >= dj:
                continue
            mask_ij = np.isin(y, [di, dj])
            if mask_ij.sum() > 0:
                yt = (y[mask_ij] == dj).astype(int)
                dj_idx = list(labels).index(dj)
                yp = all_probs[mask_ij, dj_idx]
                if len(np.unique(yt)) == 2:
                    auc = float(roc_auc_score(yt, yp))
                    pairwise_aucs[f"d{di}v{dj}"] = round(auc, 4)

    # Feature trends
    feature_trends = {}
    for feat_name in ["p90_ppl", "var_surprisal", "mean_ppl"]:
        feat_idx = FEATURE_NAMES.index(feat_name)
        trend = {}
        for d in labels:
            mask = (y == d)
            vals = X[mask, feat_idx]
            trend[f"d{d}"] = round(float(np.mean(vals)), 4)
        feature_trends[feat_name] = trend
        vals_str = ", ".join([f"d{d}={trend[f'd{d}']:.2f}" for d in labels])
        print(f"{feat_name} trend: {vals_str}")

    # Top features
    top_idx = np.argsort(importances)[::-1][:5]
    top_features = [(FEATURE_NAMES[i], round(float(importances[i]), 4)) for i in top_idx]

    results = {
        "d3v4_auc": round(d3v4_auc, 4) if d3v4_auc else None,
        "rf_5class_acc": round(mean_acc, 4),
        "rf_5class_ci": [round(ci_lo, 4), round(ci_hi, 4)],
        "fold_accs": [round(a, 4) for a in fold_accs],
        "per_class_recall": per_class_recall,
        "pairwise_aucs": pairwise_aucs,
        "feature_trends": feature_trends,
        "top_features": top_features,
        "n_samples": int(len(y)),
        "class_dist": {f"d{d}": int(np.sum(y == d)) for d in labels},
        "seed": SEED,
        "n_estimators": N_ESTIMATORS,
        "n_folds": N_FOLDS,
        "ref_model": "pythia-1.4b",
        "model": "pythia-1.4b",
        "decoding": "nucleus_p0.95",
    }

    with open(RESULTS_OUT, "w") as f:
        json.dump(results, f, indent=2)
    print(f"\nResults saved to {RESULTS_OUT}")
    print(json.dumps(results, indent=2))


if __name__ == "__main__":
    main()
