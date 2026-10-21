"""
Extract per-class metrics with bootstrap CIs for cross-model chains experiment.
Uses 5-gen mixed-chain data from data/cross-model-chains/features.csv.
"""

import json
import os
import numpy as np
import pandas as pd
from xgboost import XGBClassifier
from sklearn.metrics import f1_score, precision_score, recall_score, confusion_matrix
from sklearn.model_selection import StratifiedKFold

SEED = 42
FEATURES = ["entropy_mean", "entropy_std", "entropy_min", "entropy_max",
            "tail_decay", "ttr", "hapax_ratio"]
CLASS_MAP = {0: 0, 1: 1, 2: 2, 3: 2, 4: 2}
XGB_PARAMS = dict(n_estimators=200, max_depth=6, learning_rate=0.1,
                  random_state=SEED, eval_metric="mlogloss",
                  use_label_encoder=False)

ROOT = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(ROOT, "data")
RESULTS_DIR = os.path.join(ROOT, "results")


def balance_dataset(df):
    counts = df["label"].value_counts()
    min_n = counts.min()
    rng = np.random.RandomState(SEED)
    parts = []
    for lbl in sorted(counts.index):
        sub = df[df["label"] == lbl]
        parts.append(sub.sample(n=min_n, random_state=rng, replace=False))
    return pd.concat(parts, ignore_index=True)


def run_cv(X, y, n_splits=5):
    skf = StratifiedKFold(n_splits=n_splits, shuffle=True, random_state=SEED)
    oof_preds = np.full(len(y), -1, dtype=int)
    fold_f1s = []
    for train_idx, test_idx in skf.split(X, y):
        clf = XGBClassifier(**XGB_PARAMS)
        clf.fit(X[train_idx], y[train_idx])
        preds = clf.predict(X[test_idx])
        oof_preds[test_idx] = preds
        fold_f1s.append(f1_score(y[test_idx], preds, average="macro"))
    return fold_f1s, oof_preds


def bootstrap_metrics(y_true, y_pred, n_boot=2000, seed=42):
    rng = np.random.RandomState(seed)
    n = len(y_true)
    labels_3 = sorted(set(y_true))

    macro_f1s = []
    per_class_p = {l: [] for l in labels_3}
    per_class_r = {l: [] for l in labels_3}
    per_class_f = {l: [] for l in labels_3}

    for _ in range(n_boot):
        idx = rng.choice(n, n, replace=True)
        yt, yp = y_true[idx], y_pred[idx]
        macro_f1s.append(f1_score(yt, yp, average="macro", zero_division=0))
        for l in labels_3:
            mask = (yt == l)
            tp = ((yp == l) & mask).sum()
            fp = ((yp == l) & ~mask).sum()
            fn = ((yp != l) & mask).sum()
            p = tp / (tp + fp) if (tp + fp) > 0 else 0.0
            r = tp / (tp + fn) if (tp + fn) > 0 else 0.0
            f = 2 * p * r / (p + r) if (p + r) > 0 else 0.0
            per_class_p[l].append(p)
            per_class_r[l].append(r)
            per_class_f[l].append(f)

    def ci(arr):
        return [round(float(np.percentile(arr, 2.5)), 4),
                round(float(np.percentile(arr, 97.5)), 4)]

    return {
        "macro_f1_ci95": ci(macro_f1s),
        "per_class_ci": {
            l: {"precision_ci95": ci(per_class_p[l]),
                "recall_ci95": ci(per_class_r[l]),
                "f1_ci95": ci(per_class_f[l])}
            for l in labels_3
        }
    }


def main():
    feat_path = os.path.join(DATA_DIR, "cross-model-chains", "features.csv")
    df = pd.read_csv(feat_path)
    df["label"] = df["depth"].map(CLASS_MAP)
    df = df.dropna(subset=FEATURES + ["label"])

    balanced = balance_dataset(df)
    X = balanced[FEATURES].values
    y = balanced["label"].values.astype(int)

    print(f"Balanced dataset: {len(balanced)} samples")
    print(f"Per-class counts: {dict(zip(*np.unique(y, return_counts=True)))}")

    # 3-class evaluation
    fold_f1s, oof_preds = run_cv(X, y)
    macro_f1 = round(float(np.mean(fold_f1s)), 4)

    cm = confusion_matrix(y, oof_preds)
    class_names = {0: "gen-0", 1: "gen-1", 2: "gen-2+"}

    per_class_3 = {}
    for l, name in class_names.items():
        tp = cm[l, l]
        fp = cm[:, l].sum() - tp
        fn = cm[l, :].sum() - tp
        support = cm[l, :].sum()
        p = tp / (tp + fp) if (tp + fp) > 0 else 0.0
        r = tp / (tp + fn) if (tp + fn) > 0 else 0.0
        f = 2 * p * r / (p + r) if (p + r) > 0 else 0.0
        per_class_3[name] = {
            "precision": round(p, 4),
            "recall": round(r, 4),
            "f1": round(f, 4),
            "support": int(support)
        }

    # Bootstrap CIs for 3-class
    print("Running bootstrap (2000 iterations)...")
    boot = bootstrap_metrics(y, oof_preds)
    for l, name in class_names.items():
        per_class_3[name].update(boot["per_class_ci"][l])

    # Binary: gen-0 vs gen-1+
    y_bin = (y >= 1).astype(int)
    oof_bin = (oof_preds >= 1).astype(int)
    binary_f1 = round(float(f1_score(y_bin, oof_bin, average="macro", zero_division=0)), 4)

    cm_bin = confusion_matrix(y_bin, oof_bin)
    bin_names = {0: "gen-0", 1: "gen-1+"}
    per_class_bin = {}
    for l, name in bin_names.items():
        tp = cm_bin[l, l]
        fp = cm_bin[:, l].sum() - tp
        fn = cm_bin[l, :].sum() - tp
        support = cm_bin[l, :].sum()
        p = tp / (tp + fp) if (tp + fp) > 0 else 0.0
        r = tp / (tp + fn) if (tp + fn) > 0 else 0.0
        f = 2 * p * r / (p + r) if (p + r) > 0 else 0.0
        per_class_bin[name] = {
            "precision": round(p, 4),
            "recall": round(r, 4),
            "f1": round(f, 4),
            "support": int(support)
        }

    # Bootstrap CI for binary
    boot_bin_f1s = []
    rng = np.random.RandomState(SEED)
    n = len(y_bin)
    for _ in range(2000):
        idx = rng.choice(n, n, replace=True)
        boot_bin_f1s.append(f1_score(y_bin[idx], oof_bin[idx], average="macro", zero_division=0))
    binary_ci = [round(float(np.percentile(boot_bin_f1s, 2.5)), 4),
                 round(float(np.percentile(boot_bin_f1s, 97.5)), 4)]

    results = {
        "experiment": "cross_model_chains_per_class",
        "date": "2026-05-17",
        "n_samples": int(len(balanced)),
        "generator_pool": ["pythia-2.8b", "pythia-1b", "olmo-2-1b", "qwen3-0.6b", "qwen3-1.7b"],
        "three_class": {
            "macro_f1": macro_f1,
            "ci95": boot["macro_f1_ci95"],
            "per_class": per_class_3,
            "confusion_matrix": cm.tolist()
        },
        "binary": {
            "task": "gen-0 vs gen-1+",
            "f1": binary_f1,
            "ci95": binary_ci,
            "per_class": per_class_bin,
            "confusion_matrix": cm_bin.tolist()
        }
    }

    os.makedirs(RESULTS_DIR, exist_ok=True)
    out_path = os.path.join(RESULTS_DIR, "cross_model_chains_per_class.json")
    with open(out_path, "w") as f:
        json.dump(results, f, indent=2)
    print(f"\nSaved to {out_path}")
    print(json.dumps(results, indent=2))


if __name__ == "__main__":
    main()
