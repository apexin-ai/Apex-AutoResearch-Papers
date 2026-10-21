"""
cross_temp_transfer.py — Cross-Temperature Transfer Evaluation

Evaluates whether an XGBoost depth classifier trained at one sampling
temperature generalises to text generated at a different temperature.

Input:
  - data/features_all_models.csv          (6 generators at t=0.7)
  - data/features_qwen3-1.7b-high-temp.csv (qwen3-1.7b at t=1.0)

Output:
  - results/cross_temp_transfer.json

Method:
  Construct two 6-generator datasets that differ only in qwen3-1.7b's
  temperature (0.7 vs 1.0).  For each (train_temp, test_temp) pair, run
  LOGO-CV: hold out one generator, train on the remaining five from the
  training-temperature dataset (class-balanced), test on the held-out
  generator from the test-temperature dataset.  Average macro-F1 across
  all six folds.

Dependencies: pandas, numpy, sklearn, xgboost
"""

import json
import os
from datetime import date

import numpy as np
import pandas as pd
from sklearn.metrics import classification_report, f1_score
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


def load_datasets():
    """Build two 6-generator datasets: D_0.7 and D_1.0."""
    cols = ["model_name", "seed_id", "depth"] + FEATURES

    df_07 = pd.read_csv(os.path.join(DATA_DIR, "features_all_models.csv"))[cols]
    df_high = pd.read_csv(
        os.path.join(DATA_DIR, "features_qwen3-1.7b-high-temp.csv")
    )[cols]

    other_gens = df_07[df_07["model_name"] != "qwen3-1.7b"].copy()
    df_10 = pd.concat([other_gens, df_high], ignore_index=True)

    return df_07, df_10


def downsample(df, label_col, rng):
    """Class-balanced downsampling to the smallest class."""
    counts = df[label_col].value_counts()
    min_n = counts.min()
    parts = [
        df[df[label_col] == lbl].sample(n=min_n, random_state=rng, replace=False)
        for lbl in sorted(counts.index)
    ]
    return pd.concat(parts, ignore_index=True)


def logo_cv(df_train_full, df_test_full, label_col):
    """
    LOGO-CV: for each generator, train on the other five from df_train_full,
    test on the held-out generator from df_test_full.

    Returns per-generator and aggregate metrics.
    """
    generators = sorted(df_train_full["model_name"].unique())
    rng = np.random.RandomState(42)

    per_gen = {}
    yt_all, yp_all = [], []

    for gen in generators:
        train_df = df_train_full[df_train_full["model_name"] != gen].copy()
        test_df = df_test_full[df_test_full["model_name"] == gen].copy()

        if len(test_df) == 0:
            continue

        train_ds = downsample(train_df, label_col, rng)

        n_classes = len(train_ds[label_col].unique())
        params = dict(XGB_PARAMS)
        if n_classes == 2:
            params["eval_metric"] = "logloss"
            params["objective"] = "binary:logistic"
        else:
            params["objective"] = "multi:softmax"
            params["num_class"] = n_classes

        clf = XGBClassifier(**params)
        clf.fit(train_ds[FEATURES].values, train_ds[label_col].values)

        yp = clf.predict(test_df[FEATURES].values)
        yt = test_df[label_col].values

        gen_f1 = float(f1_score(yt, yp, average="macro", zero_division=0))
        per_gen[gen] = round(gen_f1, 4)

        yt_all.append(yt)
        yp_all.append(yp)

    yt_cat = np.concatenate(yt_all)
    yp_cat = np.concatenate(yp_all)

    macro_f1 = float(f1_score(yt_cat, yp_cat, average="macro", zero_division=0))

    labels = sorted(set(yt_cat))
    report = classification_report(
        yt_cat, yp_cat, labels=labels, output_dict=True, zero_division=0,
    )

    per_class = {}
    label_names = {0: "gen0", 1: "gen1", 2: "gen2+"}
    for lbl in labels:
        key = label_names.get(lbl, f"class_{lbl}")
        r = report[str(lbl)]
        per_class[key] = {
            "precision": round(r["precision"], 4),
            "recall": round(r["recall"], 4),
            "f1": round(r["f1-score"], 4),
        }

    return {
        "macro_f1": round(macro_f1, 4),
        "per_generator": per_gen,
        "per_class": per_class,
    }


def run_condition(df_train, df_test, condition_name):
    """Run binary and 3-class evaluation for one train→test condition."""
    print(f"\n{'='*50}")
    print(f"  {condition_name}")
    print(f"{'='*50}")

    df_tr = df_train.copy()
    df_te = df_test.copy()

    # 3-class
    df_tr["label_3"] = df_tr["depth"].map(CLASS_MAP_3)
    df_te["label_3"] = df_te["depth"].map(CLASS_MAP_3)
    res_3 = logo_cv(df_tr, df_te, "label_3")
    print(f"  3-class macro-F1: {res_3['macro_f1']:.4f}")

    # Binary
    df_tr["label_bin"] = df_tr["depth"].map(CLASS_MAP_BIN)
    df_te["label_bin"] = df_te["depth"].map(CLASS_MAP_BIN)
    res_bin = logo_cv(df_tr, df_te, "label_bin")
    print(f"  Binary  macro-F1: {res_bin['macro_f1']:.4f}")

    print(f"  Per-gen (3-class): {res_3['per_generator']}")

    return {
        "binary_f1": res_bin["macro_f1"],
        "three_class_f1": res_3["macro_f1"],
        "per_class": res_3["per_class"],
        "per_generator_3class": res_3["per_generator"],
        "per_generator_binary": res_bin["per_generator"],
    }


def main():
    print("Loading datasets...")
    df_07, df_10 = load_datasets()

    gens_07 = sorted(df_07["model_name"].unique())
    gens_10 = sorted(df_10["model_name"].unique())
    print(f"D_0.7: {len(df_07)} rows, generators: {gens_07}")
    print(f"D_1.0: {len(df_10)} rows, generators: {gens_10}")

    conditions = {
        "0.7_to_0.7": (df_07, df_07),
        "0.7_to_1.0": (df_07, df_10),
        "1.0_to_1.0": (df_10, df_10),
        "1.0_to_0.7": (df_10, df_07),
    }

    results = {}
    for cond_name, (df_tr, df_te) in conditions.items():
        results[cond_name] = run_condition(df_tr, df_te, cond_name)

    # Compute deltas
    delta_07_bin = results["0.7_to_1.0"]["binary_f1"] - results["0.7_to_0.7"]["binary_f1"]
    delta_07_3c = results["0.7_to_1.0"]["three_class_f1"] - results["0.7_to_0.7"]["three_class_f1"]
    delta_10_bin = results["1.0_to_0.7"]["binary_f1"] - results["1.0_to_1.0"]["binary_f1"]
    delta_10_3c = results["1.0_to_0.7"]["three_class_f1"] - results["1.0_to_1.0"]["three_class_f1"]

    output = {
        "experiment": "cross_temperature_transfer",
        "date": str(date.today()),
        "model": "XGBoost",
        "hyperparams": {"n_estimators": 200, "max_depth": 6},
        "features": FEATURES,
        "method": (
            "LOGO-CV: hold out one generator, train on remaining five from "
            "training-temp dataset (class-balanced), test on held-out generator "
            "from test-temp dataset. D_0.7 = features_all_models.csv (6 gens). "
            "D_1.0 = same 5 generators + qwen3-1.7b at t=1.0."
        ),
        "results": results,
        "data_info": {
            "t07": {
                "path": "data/features_all_models.csv",
                "n_samples": len(df_07),
                "generators": gens_07,
            },
            "t10": {
                "path": "data/features_all_models.csv + data/features_qwen3-1.7b-high-temp.csv",
                "n_samples": len(df_10),
                "generators": gens_10,
            },
        },
        "cross_temp_delta": {
            "0.7_train_delta_binary": round(delta_07_bin, 4),
            "0.7_train_delta_3class": round(delta_07_3c, 4),
            "1.0_train_delta_binary": round(delta_10_bin, 4),
            "1.0_train_delta_3class": round(delta_10_3c, 4),
        },
    }

    os.makedirs(RESULTS_DIR, exist_ok=True)
    out_path = os.path.join(RESULTS_DIR, "cross_temp_transfer.json")
    with open(out_path, "w") as f:
        json.dump(output, f, indent=2, ensure_ascii=False)
    print(f"\nSaved: {out_path}")

    # Summary
    print(f"\n{'='*60}")
    print("SUMMARY")
    print(f"{'='*60}")
    print(f"{'Condition':<15s} {'Binary F1':>10s} {'3-class F1':>11s}")
    print("-" * 38)
    for cond in ["0.7_to_0.7", "0.7_to_1.0", "1.0_to_1.0", "1.0_to_0.7"]:
        r = results[cond]
        print(f"{cond:<15s} {r['binary_f1']:>10.4f} {r['three_class_f1']:>11.4f}")
    print()
    print(f"Delta (0.7-trained, cross-temp):  binary={delta_07_bin:+.4f}  3class={delta_07_3c:+.4f}")
    print(f"Delta (1.0-trained, cross-temp):  binary={delta_10_bin:+.4f}  3class={delta_10_3c:+.4f}")


if __name__ == "__main__":
    main()
