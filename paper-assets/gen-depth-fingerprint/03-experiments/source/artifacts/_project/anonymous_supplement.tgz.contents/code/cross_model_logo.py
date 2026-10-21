"""
cross_model_logo.py -- LOGO evaluation for cross-model chain data.

Leave-one-generator-out (LOGO) cross-validation for the cross-model
rewriting chain experiment. Each fold holds out all depth 1-4 samples
produced by one generator. Depth-0 (Wikipedia) samples are split
equally across folds.

Usage:
    python cross_model_logo.py

Expects:
    data/cross-model-chains/features.csv
Outputs:
    results/cross_model_logo_results.json
"""

import json
import os
import numpy as np
import pandas as pd
from xgboost import XGBClassifier
from sklearn.metrics import f1_score, classification_report, confusion_matrix

SEED = 42
FEATURES = ["entropy_mean", "entropy_std", "entropy_min", "entropy_max",
            "tail_decay", "ttr", "hapax_ratio"]
XGB_PARAMS = dict(n_estimators=200, max_depth=6, learning_rate=0.1,
                  random_state=SEED, eval_metric="mlogloss",
                  use_label_encoder=False)
CLASS_MAP = {0: 0, 1: 1, 2: 2, 3: 2, 4: 2}

ROOT = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(ROOT, "..", "data", "cross-model-chains")
RESULTS_DIR = os.path.join(ROOT, "..", "results")


def load_data():
    df = pd.read_csv(os.path.join(DATA_DIR, "features.csv"))
    df["label"] = df["depth"].map(CLASS_MAP)
    df = df.dropna(subset=FEATURES + ["label"])
    return df


def balance_train(df_train, rng):
    counts = df_train["label"].value_counts()
    min_n = counts.min()
    parts = []
    for lbl in sorted(counts.index):
        sub = df_train[df_train["label"] == lbl]
        parts.append(sub.sample(n=min_n, random_state=rng, replace=False))
    return pd.concat(parts, ignore_index=True)


def run_logo(df):
    generators = sorted(df[df["depth"] > 0]["generator_at_depth"].unique())
    n_gens = len(generators)

    # Split gen-0 (wikipedia) into n_gens equal parts as DataFrames
    gen0 = df[df["depth"] == 0].copy()
    rng = np.random.RandomState(SEED)
    gen0_shuffled = gen0.sample(frac=1, random_state=rng).reset_index(drop=True)
    fold_indices = np.array_split(np.arange(len(gen0_shuffled)), n_gens)
    gen0_folds = [gen0_shuffled.iloc[idx].copy() for idx in fold_indices]

    gen_nonzero = df[df["depth"] > 0].copy()

    all_y_true = []
    all_y_pred = []
    per_gen_results = {}

    for i, held_out_gen in enumerate(generators):
        # Test: depth 1-4 from held-out generator + 1/n of gen-0
        test_gen = gen_nonzero[gen_nonzero["generator_at_depth"] == held_out_gen].copy()
        test_gen0 = gen0_folds[i]
        test_df = pd.concat([test_gen0, test_gen], ignore_index=True)

        # Train: depth 1-4 from other generators + remaining gen-0
        train_gen = gen_nonzero[gen_nonzero["generator_at_depth"] != held_out_gen].copy()
        train_gen0_parts = [gen0_folds[j] for j in range(n_gens) if j != i]
        train_gen0 = pd.concat(train_gen0_parts, ignore_index=True)
        train_df = pd.concat([train_gen0, train_gen], ignore_index=True)

        # Balance training set
        train_balanced = balance_train(train_df, rng)

        X_train = train_balanced[FEATURES].values
        y_train = train_balanced["label"].values.astype(int)
        X_test = test_df[FEATURES].values
        y_test = test_df["label"].values.astype(int)

        clf = XGBClassifier(**XGB_PARAMS)
        clf.fit(X_train, y_train)
        preds = clf.predict(X_test)

        f1_3c = f1_score(y_test, preds, average="macro")

        # Binary: gen-1 vs gen-2+
        mask_bin = np.isin(y_test, [1, 2])
        if mask_bin.sum() > 0:
            y_b = (y_test[mask_bin] == 2).astype(int)
            p_b = (preds[mask_bin] == 2).astype(int)
            f1_bin = f1_score(y_b, p_b)
        else:
            f1_bin = 0.0

        per_gen_results[held_out_gen] = {
            "3class_f1": round(float(f1_3c), 4),
            "binary_f1": round(float(f1_bin), 4),
            "n_test": len(test_df),
            "n_train_balanced": len(train_balanced),
        }
        print(f"  Fold {i+1}/{n_gens} [{held_out_gen:15s}]: "
              f"3class={f1_3c:.4f}  binary={f1_bin:.4f}  n_test={len(test_df)}")

        all_y_true.extend(y_test.tolist())
        all_y_pred.extend(preds.tolist())

    all_y_true = np.array(all_y_true)
    all_y_pred = np.array(all_y_pred)

    overall_3class = f1_score(all_y_true, all_y_pred, average="macro")

    # Overall binary F1
    mask_bin_all = np.isin(all_y_true, [1, 2])
    y_b_all = (all_y_true[mask_bin_all] == 2).astype(int)
    p_b_all = (all_y_pred[mask_bin_all] == 2).astype(int)
    overall_binary = f1_score(y_b_all, p_b_all)

    cm = confusion_matrix(all_y_true, all_y_pred).tolist()
    report = classification_report(all_y_true, all_y_pred, output_dict=True, zero_division=0)

    return {
        "3class_f1": round(float(overall_3class), 4),
        "binary_f1": round(float(overall_binary), 4),
        "n_samples": len(all_y_true),
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
        "per_generator": per_gen_results,
    }, all_y_true, all_y_pred


def bootstrap_ci(y_true, y_pred, n_boot=2000):
    rng = np.random.RandomState(SEED)
    n = len(y_true)

    f1_3c_boots = []
    f1_bin_boots = []

    for _ in range(n_boot):
        idx = rng.choice(n, size=n, replace=True)
        yt = y_true[idx]
        yp = y_pred[idx]

        f1_3c_boots.append(f1_score(yt, yp, average="macro"))

        mask = np.isin(yt, [1, 2])
        if mask.sum() > 0:
            yb = (yt[mask] == 2).astype(int)
            pb = (yp[mask] == 2).astype(int)
            f1_bin_boots.append(f1_score(yb, pb))

    f1_3c_boots = np.array(f1_3c_boots)
    f1_bin_boots = np.array(f1_bin_boots)

    return {
        "3class_f1_ci": [round(float(np.percentile(f1_3c_boots, 2.5)), 4),
                         round(float(np.percentile(f1_3c_boots, 97.5)), 4)],
        "binary_f1_ci": [round(float(np.percentile(f1_bin_boots, 2.5)), 4),
                         round(float(np.percentile(f1_bin_boots, 97.5)), 4)],
        "n_boot": n_boot,
    }


def main():
    print("Loading cross-model chain data...")
    df = load_data()
    generators = sorted(df[df["depth"] > 0]["generator_at_depth"].unique())
    print(f"  Generators ({len(generators)}): {generators}")
    print(f"  Total samples: {len(df)}")
    print(f"  Label distribution: {df['label'].value_counts().sort_index().to_dict()}")

    print("\n=== LOGO (leave-one-generator-out) ===")
    logo_results, y_true, y_pred = run_logo(df)
    print(f"\n  Overall 3-class macro F1: {logo_results['3class_f1']:.4f}")
    print(f"  Overall binary F1 (gen-1 vs gen-2+): {logo_results['binary_f1']:.4f}")

    print("\n=== Bootstrap 95% CI (2000 iter) ===")
    ci = bootstrap_ci(y_true, y_pred, n_boot=2000)
    print(f"  3-class F1 CI: {ci['3class_f1_ci']}")
    print(f"  Binary F1 CI:  {ci['binary_f1_ci']}")

    results = {
        "experiment": "cross_model_chains_logo",
        "method": "leave-one-generator-out (LOGO)",
        "description": "Each fold holds out all samples produced by one generator. "
                       "Depth-0 (wikipedia) samples split equally across folds. "
                       "Training set balanced per fold.",
        "logo": logo_results,
        "bootstrap_ci_95": ci,
        "config": {
            "generators": generators,
            "features": FEATURES,
            "xgb_params": {k: v for k, v in XGB_PARAMS.items() if k != "eval_metric"},
            "class_map": {"0": "gen-0", "1": "gen-1", "2-4": "gen-2+"},
            "n_bootstrap": ci["n_boot"],
        },
    }

    os.makedirs(RESULTS_DIR, exist_ok=True)
    out_path = os.path.join(RESULTS_DIR, "cross_model_logo_results.json")
    with open(out_path, "w") as f:
        json.dump(results, f, indent=2)
    print(f"\nSaved: {out_path}")


if __name__ == "__main__":
    main()
