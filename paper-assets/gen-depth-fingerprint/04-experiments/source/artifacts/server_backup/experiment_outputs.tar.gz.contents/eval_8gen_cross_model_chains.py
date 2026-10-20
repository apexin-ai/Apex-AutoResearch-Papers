"""
eval_8gen_cross_model_chains.py — 8-gen cross-model chain extension.

The original 5-gen cross-model chain experiment (plan_007) generated actual
mixed-chain data where each depth step uses a randomly selected generator.
True 8-gen mixed-chain data does not exist (impractical to load 7B/8B models
alternately per depth step).

This script provides two complementary evaluations:
  1. Pooled 5-fold CV on all 8 generators' single-model data — analogous to
     the cross-model chain evaluation methodology (same features, XGBoost, etc.)
  2. 8-fold LOGO — leave-one-generator-out cross-validation

Both are compared against the original 5-gen mixed-chain results.
"""

import json
import os
import numpy as np
import pandas as pd
from xgboost import XGBClassifier
from sklearn.metrics import f1_score, classification_report, confusion_matrix
from sklearn.model_selection import StratifiedKFold
from scipy.stats import kruskal

SEED = 42
FEATURES = ["entropy_mean", "entropy_std", "entropy_min", "entropy_max",
            "tail_decay", "ttr", "hapax_ratio"]

XGB_PARAMS = dict(n_estimators=200, max_depth=6, learning_rate=0.1,
                  random_state=SEED, eval_metric="mlogloss",
                  use_label_encoder=False)

CLASS_MAP = {0: 0, 1: 1, 2: 2, 3: 2, 4: 2}

ROOT = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(ROOT, "data")
RESULTS_DIR = os.path.join(ROOT, "results")


def load_8gen_data():
    df_base = pd.read_csv(os.path.join(DATA_DIR, "features_all_models.csv"))
    df_base = df_base.rename(columns={"model_name": "generator"})

    new_gens = [
        ("llama-3.2-3b", os.path.join(DATA_DIR, "llama-3.2-3b", "features_pythia410m.jsonl")),
        ("mistral-7b-v0.3", os.path.join(DATA_DIR, "mistral-7b-v0.3", "features_pythia410m.jsonl")),
    ]
    dfs = [df_base]
    for gen_name, path in new_gens:
        records = []
        with open(path) as f:
            for line in f:
                rec = json.loads(line)
                rec["generator"] = gen_name
                records.append(rec)
        dfs.append(pd.DataFrame(records))

    cols = ["generator", "seed_id", "depth"] + FEATURES
    df = pd.concat([d[cols] for d in dfs], ignore_index=True)
    df["label"] = df["depth"].map(CLASS_MAP)
    df = df.dropna(subset=FEATURES + ["label"])
    return df


def balance_dataset(df):
    counts = df["label"].value_counts()
    min_n = counts.min()
    rng = np.random.RandomState(SEED)
    parts = []
    for lbl in sorted(counts.index):
        sub = df[df["label"] == lbl]
        parts.append(sub.sample(n=min_n, random_state=rng, replace=False))
    return pd.concat(parts, ignore_index=True)


def run_pooled_cv(df, n_folds=5):
    """Pooled 5-fold stratified CV across all 8 generators — analogous to
    cross-model chain evaluation."""
    balanced = balance_dataset(df)
    X = balanced[FEATURES].values
    y = balanced["label"].values.astype(int)

    skf = StratifiedKFold(n_splits=n_folds, shuffle=True, random_state=SEED)
    fold_f1s = []
    oof_preds = np.zeros(len(y), dtype=int)

    for train_idx, test_idx in skf.split(X, y):
        clf = XGBClassifier(**XGB_PARAMS)
        clf.fit(X[train_idx], y[train_idx])
        preds = clf.predict(X[test_idx])
        oof_preds[test_idx] = preds
        fold_f1s.append(f1_score(y[test_idx], preds, average="macro"))

    # Binary F1: gen-1 vs gen-2+
    mask_binary = np.isin(y, [1, 2])
    y_bin = (y[mask_binary] == 2).astype(int)
    p_bin = (oof_preds[mask_binary] == 2).astype(int)
    binary_f1 = f1_score(y_bin, p_bin)

    cm = confusion_matrix(y, oof_preds).tolist()
    report = classification_report(y, oof_preds, output_dict=True, zero_division=0)

    # Feature importance (full retrain)
    clf_full = XGBClassifier(**XGB_PARAMS)
    clf_full.fit(X, y)
    importance = dict(zip(FEATURES, [round(float(x), 4) for x in clf_full.feature_importances_]))

    return {
        "macro_f1_mean": round(float(np.mean(fold_f1s)), 4),
        "macro_f1_std": round(float(np.std(fold_f1s)), 4),
        "binary_f1": round(float(binary_f1), 4),
        "fold_f1s": [round(f, 4) for f in fold_f1s],
        "n_samples": len(balanced),
        "confusion_matrix": cm,
        "per_class": {
            cls_name: {
                "precision": round(report[str(cls_label)]["precision"], 4),
                "recall": round(report[str(cls_label)]["recall"], 4),
                "f1": round(report[str(cls_label)]["f1-score"], 4),
            }
            for cls_label, cls_name in [(0, "gen-0"), (1, "gen-1"), (2, "gen-2+")]
            if str(cls_label) in report
        },
        "feature_importance": importance,
    }


def run_logo(df):
    """8-fold LOGO cross-validation."""
    generators = sorted(df["generator"].unique())
    per_gen = {}
    all_y_true = []
    all_y_pred = []
    rng = np.random.RandomState(SEED)

    for gen in generators:
        test_df = df[df["generator"] == gen].copy()
        train_df = df[df["generator"] != gen].copy()

        # Balance training set
        train_counts = train_df["label"].value_counts()
        min_n = train_counts.min()
        train_parts = []
        for lbl in sorted(train_counts.index):
            sub = train_df[train_df["label"] == lbl]
            train_parts.append(sub.sample(n=min_n, random_state=rng, replace=False))
        train_bal = pd.concat(train_parts, ignore_index=True)

        X_train = train_bal[FEATURES].values
        y_train = train_bal["label"].values.astype(int)
        X_test = test_df[FEATURES].values
        y_test = test_df["label"].values.astype(int)

        clf = XGBClassifier(**XGB_PARAMS)
        clf.fit(X_train, y_train)
        preds = clf.predict(X_test)

        f1_3class = f1_score(y_test, preds, average="macro")

        # Binary: gen-1 vs gen-2+
        mask_bin = np.isin(y_test, [1, 2])
        if mask_bin.sum() > 0:
            y_b = (y_test[mask_bin] == 2).astype(int)
            p_b = (preds[mask_bin] == 2).astype(int)
            f1_bin = f1_score(y_b, p_b)
        else:
            f1_bin = 0.0

        per_gen[gen] = {
            "3class_f1": round(float(f1_3class), 4),
            "binary_f1": round(float(f1_bin), 4),
            "n_test": len(test_df),
        }
        all_y_true.extend(y_test.tolist())
        all_y_pred.extend(preds.tolist())

    all_y_true = np.array(all_y_true)
    all_y_pred = np.array(all_y_pred)
    overall_3class = f1_score(all_y_true, all_y_pred, average="macro")

    mask_bin_all = np.isin(all_y_true, [1, 2])
    y_b_all = (all_y_true[mask_bin_all] == 2).astype(int)
    p_b_all = (all_y_pred[mask_bin_all] == 2).astype(int)
    overall_binary = f1_score(y_b_all, p_b_all)

    return {
        "3class_f1": round(float(overall_3class), 4),
        "binary_f1": round(float(overall_binary), 4),
        "n_samples": len(all_y_true),
        "per_generator": per_gen,
    }


def main():
    print("Loading 8-gen feature data...")
    df = load_8gen_data()
    generators = sorted(df["generator"].unique())
    print(f"  Generators ({len(generators)}): {generators}")
    print(f"  Total samples: {len(df)}")
    print(f"  Label distribution: {df['label'].value_counts().sort_index().to_dict()}")

    print("\n=== Pooled 5-fold CV (cross-model analog) ===")
    pooled = run_pooled_cv(df)
    print(f"  3-class F1: {pooled['macro_f1_mean']:.4f} ± {pooled['macro_f1_std']:.4f}")
    print(f"  Binary F1:  {pooled['binary_f1']:.4f}")

    print("\n=== 8-fold LOGO ===")
    logo = run_logo(df)
    print(f"  3-class F1: {logo['3class_f1']:.4f}")
    print(f"  Binary F1:  {logo['binary_f1']:.4f}")
    for gen, metrics in sorted(logo["per_generator"].items()):
        print(f"    {gen:20s}: 3class={metrics['3class_f1']:.4f}  binary={metrics['binary_f1']:.4f}  n={metrics['n_test']}")

    # Original 5-gen cross-model chain results
    orig_3class = 0.8089
    orig_binary = 0.7635

    results = {
        "experiment": "8gen_cross_model_chains",
        "note": "True 8-gen mixed-chain data not generated (impractical to load 7B/8B models alternately per depth). Results below use single-model chain data with cross-model evaluation methodology.",
        "8gen_pooled_cv": pooled,
        "8gen_logo": {
            "3class_f1": logo["3class_f1"],
            "binary_f1": logo["binary_f1"],
            "n_samples": logo["n_samples"],
            "per_gen": logo["per_generator"],
        },
        "vs_5gen": {
            "5gen_3class_f1": orig_3class,
            "5gen_binary_f1": orig_binary,
            "delta_3class_pooled": round(pooled["macro_f1_mean"] - orig_3class, 4),
            "delta_binary_pooled": round(pooled["binary_f1"] - orig_binary, 4),
            "delta_3class_logo": round(logo["3class_f1"] - orig_3class, 4),
            "delta_binary_logo": round(logo["binary_f1"] - orig_binary, 4),
        },
        "config": {
            "generators": generators,
            "n_generators": len(generators),
            "features": FEATURES,
            "xgb_params": {k: v for k, v in XGB_PARAMS.items() if k != "eval_metric"},
            "class_map": {"0": "gen-0", "1": "gen-1", "2-4": "gen-2+"},
            "reference_model": "pythia-410m",
            "pooled_cv_folds": 5,
            "mixed_chain_data_available": False,
        },
    }

    os.makedirs(RESULTS_DIR, exist_ok=True)
    out_path = os.path.join(RESULTS_DIR, "8gen_cross_model_chains.json")
    with open(out_path, "w") as f:
        json.dump(results, f, indent=2)
    print(f"\nSaved: {out_path}")


if __name__ == "__main__":
    main()
