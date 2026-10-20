# Cross-Temperature Transfer Evaluation — Qwen3-1.7B Only
#
# Evaluates whether depth fingerprints trained at one sampling temperature
# (t=0.7 or t=1.0) transfer to the other temperature, using only Qwen3-1.7B data.
#
# Input:
#   data/features_qwen3-1.7b.csv           (t=0.7)
#   data/features_qwen3-1.7b-high-temp.csv (t=1.0)
#
# Output:
#   results/cross_temp_transfer_qwen_only.json

import json
import os
from datetime import date

import numpy as np
import pandas as pd
from sklearn.metrics import f1_score, classification_report
from sklearn.model_selection import StratifiedKFold
from xgboost import XGBClassifier

FEATURES = [
    "entropy_mean", "entropy_std", "entropy_min", "entropy_max",
    "tail_decay", "ttr", "hapax_ratio",
]

CLASS_MAP_3 = {0: 0, 1: 1, 2: 2, 3: 2, 4: 2}
CLASS_MAP_BIN = {0: 0, 1: 1, 2: 1, 3: 1, 4: 1}

XGB_PARAMS = dict(
    n_estimators=200, max_depth=6, learning_rate=0.1,
    random_state=42, eval_metric="mlogloss", use_label_encoder=False,
)

ROOT = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(ROOT, "data")
RESULTS_DIR = os.path.join(ROOT, "results")

N_BOOTSTRAP = 1000
N_CV_FOLDS = 5
SEED = 42


def load_data():
    df07 = pd.read_csv(os.path.join(DATA_DIR, "features_qwen3-1.7b.csv"))
    df10 = pd.read_csv(os.path.join(DATA_DIR, "features_qwen3-1.7b-high-temp.csv"))
    return df07, df10


def make_labels(df):
    df = df.copy()
    df["label_bin"] = df["depth"].map(CLASS_MAP_BIN)
    df["label_3"] = df["depth"].map(CLASS_MAP_3)
    return df


def get_xgb(n_classes):
    params = dict(XGB_PARAMS)
    if n_classes == 2:
        params["eval_metric"] = "logloss"
        params["objective"] = "binary:logistic"
    else:
        params["objective"] = "multi:softmax"
        params["num_class"] = n_classes
    return XGBClassifier(**params)


def bootstrap_ci(y_true, y_pred, n_boot=N_BOOTSTRAP, seed=SEED):
    rng = np.random.RandomState(seed)
    n = len(y_true)
    scores = np.empty(n_boot)
    for i in range(n_boot):
        idx = rng.randint(0, n, size=n)
        scores[i] = f1_score(y_true[idx], y_pred[idx], average="macro", zero_division=0)
    lo, hi = np.percentile(scores, [2.5, 97.5])
    return round(float(lo), 4), round(float(hi), 4)


def per_class_f1(y_true, y_pred):
    labels = sorted(set(y_true))
    report = classification_report(y_true, y_pred, labels=labels, output_dict=True, zero_division=0)
    return {str(l): round(report[str(l)]["f1-score"], 4) for l in labels}


def within_temp_cv(df, label_col):
    """5-fold stratified CV within a single temperature dataset."""
    X = df[FEATURES].values
    y = df[label_col].values
    n_classes = len(np.unique(y))

    skf = StratifiedKFold(n_splits=N_CV_FOLDS, shuffle=True, random_state=SEED)
    yt_all, yp_all = [], []

    for train_idx, test_idx in skf.split(X, y):
        clf = get_xgb(n_classes)
        clf.fit(X[train_idx], y[train_idx])
        yp = clf.predict(X[test_idx])
        yt_all.append(y[test_idx])
        yp_all.append(yp)

    yt_cat = np.concatenate(yt_all)
    yp_cat = np.concatenate(yp_all)
    macro_f1 = round(float(f1_score(yt_cat, yp_cat, average="macro", zero_division=0)), 4)
    ci = bootstrap_ci(yt_cat, yp_cat)
    pc = per_class_f1(yt_cat, yp_cat)
    return macro_f1, ci, pc


def cross_temp_eval(df_train, df_test, label_col):
    """Train on all source-temp data, test on all target-temp data."""
    X_tr = df_train[FEATURES].values
    y_tr = df_train[label_col].values
    X_te = df_test[FEATURES].values
    y_te = df_test[label_col].values
    n_classes = len(np.unique(y_tr))

    clf = get_xgb(n_classes)
    clf.fit(X_tr, y_tr)
    yp = clf.predict(X_te)

    macro_f1 = round(float(f1_score(y_te, yp, average="macro", zero_division=0)), 4)
    ci = bootstrap_ci(y_te, yp)
    pc = per_class_f1(y_te, yp)
    return macro_f1, ci, pc


def run_all(df07, df10):
    df07 = make_labels(df07)
    df10 = make_labels(df10)

    results = {}

    for task, label_col in [("binary", "label_bin"), ("three_class", "label_3")]:
        tag = f"{task}_f1"
        ci_tag = f"{task}_ci95"
        pc_tag = f"per_class_{task}"

        # 0.7 -> 0.7 (within, CV)
        f1, ci, pc = within_temp_cv(df07, label_col)
        results.setdefault("0.7_to_0.7", {})[tag] = f1
        results["0.7_to_0.7"][ci_tag] = list(ci)
        results["0.7_to_0.7"][pc_tag] = pc

        # 1.0 -> 1.0 (within, CV)
        f1, ci, pc = within_temp_cv(df10, label_col)
        results.setdefault("1.0_to_1.0", {})[tag] = f1
        results["1.0_to_1.0"][ci_tag] = list(ci)
        results["1.0_to_1.0"][pc_tag] = pc

        # 0.7 -> 1.0 (cross)
        f1, ci, pc = cross_temp_eval(df07, df10, label_col)
        results.setdefault("0.7_to_1.0", {})[tag] = f1
        results["0.7_to_1.0"][ci_tag] = list(ci)
        results["0.7_to_1.0"][pc_tag] = pc

        # 1.0 -> 0.7 (cross)
        f1, ci, pc = cross_temp_eval(df10, df07, label_col)
        results.setdefault("1.0_to_0.7", {})[tag] = f1
        results["1.0_to_0.7"][ci_tag] = list(ci)
        results["1.0_to_0.7"][pc_tag] = pc

    return results


def main():
    print("Loading Qwen3-1.7B data...")
    df07, df10 = load_data()

    depth_dist_07 = df07["depth"].value_counts().sort_index().to_dict()
    depth_dist_10 = df10["depth"].value_counts().sort_index().to_dict()
    print(f"t=0.7: {len(df07)} samples, depth dist: {depth_dist_07}")
    print(f"t=1.0: {len(df10)} samples, depth dist: {depth_dist_10}")

    results = run_all(df07, df10)

    delta = {
        "0.7_train_binary_delta_pp": round(
            results["0.7_to_1.0"]["binary_f1"] - results["0.7_to_0.7"]["binary_f1"], 4),
        "0.7_train_3class_delta_pp": round(
            results["0.7_to_1.0"]["three_class_f1"] - results["0.7_to_0.7"]["three_class_f1"], 4),
        "1.0_train_binary_delta_pp": round(
            results["1.0_to_0.7"]["binary_f1"] - results["1.0_to_1.0"]["binary_f1"], 4),
        "1.0_train_3class_delta_pp": round(
            results["1.0_to_0.7"]["three_class_f1"] - results["1.0_to_1.0"]["three_class_f1"], 4),
    }

    output = {
        "experiment": "cross_temperature_transfer_qwen3-1.7b",
        "generator": "qwen3-1.7b",
        "date": str(date.today()),
        "hyperparams": {"n_estimators": 200, "max_depth": 6, "lr": 0.1},
        "features": FEATURES,
        "method": (
            "Single-generator cross-temperature transfer. "
            "Within-temp: 5-fold stratified CV. "
            "Cross-temp: train on all source-temp data, test on all target-temp data. "
            "Bootstrap CI: n=1000, 95%."
        ),
        "data_info": {
            "t07": {
                "path": "data/features_qwen3-1.7b.csv",
                "n_samples": len(df07),
                "depth_dist": {str(k): v for k, v in depth_dist_07.items()},
            },
            "t10": {
                "path": "data/features_qwen3-1.7b-high-temp.csv",
                "n_samples": len(df10),
                "depth_dist": {str(k): v for k, v in depth_dist_10.items()},
            },
        },
        "results": results,
        "cross_temp_delta": delta,
    }

    os.makedirs(RESULTS_DIR, exist_ok=True)
    out_path = os.path.join(RESULTS_DIR, "cross_temp_transfer_qwen_only.json")
    with open(out_path, "w") as f:
        json.dump(output, f, indent=2, ensure_ascii=False)
    print(f"\nSaved: {out_path}")

    print(f"\n{'='*65}")
    print("SUMMARY — Qwen3-1.7B Cross-Temperature Transfer")
    print(f"{'='*65}")
    print(f"{'Condition':<15s} {'Bin F1':>8s} {'Bin 95%CI':>18s} {'3cl F1':>8s} {'3cl 95%CI':>18s}")
    print("-" * 69)
    for cond in ["0.7_to_0.7", "0.7_to_1.0", "1.0_to_1.0", "1.0_to_0.7"]:
        r = results[cond]
        print(f"{cond:<15s} {r['binary_f1']:>8.4f} [{r['binary_ci95'][0]:.4f}, {r['binary_ci95'][1]:.4f}]"
              f" {r['three_class_f1']:>8.4f} [{r['three_class_ci95'][0]:.4f}, {r['three_class_ci95'][1]:.4f}]")
    print()
    print(f"Delta (trained 0.7, tested cross):  binary={delta['0.7_train_binary_delta_pp']:+.4f}  3class={delta['0.7_train_3class_delta_pp']:+.4f}")
    print(f"Delta (trained 1.0, tested cross):  binary={delta['1.0_train_binary_delta_pp']:+.4f}  3class={delta['1.0_train_3class_delta_pp']:+.4f}")


if __name__ == "__main__":
    main()
