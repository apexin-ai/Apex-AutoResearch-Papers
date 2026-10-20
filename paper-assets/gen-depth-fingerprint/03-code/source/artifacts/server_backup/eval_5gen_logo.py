"""
eval_5gen_logo.py — 5-generator LOGO binary eval.

5 generators (cross-model chains subset):
  pythia-2.8b, pythia-1b, olmo-2-1b, qwen3-1.7b, qwen3-0.6b

Binary LOGO: gen-1 vs gen-2+ (exclude gen-0), 5-fold leave-one-generator-out.
"""

import json
import os
import numpy as np
import pandas as pd
from xgboost import XGBClassifier
from sklearn.metrics import f1_score

SEED = 42
FEATURES = ["entropy_mean", "entropy_std", "entropy_min", "entropy_max",
            "tail_decay", "ttr", "hapax_ratio"]

XGB_PARAMS = dict(n_estimators=200, max_depth=6, learning_rate=0.1,
                  random_state=SEED, eval_metric="mlogloss",
                  use_label_encoder=False)

CLASS_MAP_3 = {0: 0, 1: 1, 2: 2, 3: 2, 4: 2}

GENERATORS_5 = ["pythia-2.8b", "pythia-1b", "olmo-2-1b", "qwen3-1.7b", "qwen3-0.6b"]

ROOT = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(ROOT, "data")
RESULTS_DIR = os.path.join(ROOT, "results")


def load_data():
    df = pd.read_csv(os.path.join(DATA_DIR, "features_all_models.csv"))
    df = df[df["model_name"].isin(GENERATORS_5)].copy()
    cols = ["model_name", "seed_id", "depth"] + FEATURES
    return df[cols].reset_index(drop=True)


def downsample(df, label_col, rng):
    counts = df[label_col].value_counts()
    min_n = counts.min()
    parts = []
    for lbl in sorted(counts.index):
        sub = df[df[label_col] == lbl]
        parts.append(sub.sample(n=min_n, random_state=rng, replace=False))
    return pd.concat(parts, ignore_index=True)


def bootstrap_f1(y_true, y_pred, n_boot=1000, seed=SEED):
    rng = np.random.RandomState(seed)
    n = len(y_true)
    scores = []
    for _ in range(n_boot):
        idx = rng.randint(0, n, size=n)
        yt, yp = y_true[idx], y_pred[idx]
        if len(np.unique(yt)) < 2:
            continue
        scores.append(f1_score(yt, yp, average="macro"))
    arr = np.array(scores)
    return float(np.mean(arr)), float(np.percentile(arr, 2.5)), float(np.percentile(arr, 97.5))


def logo_binary(df):
    df = df.copy()
    df["label3"] = df["depth"].map(CLASS_MAP_3)
    df = df[df["label3"] >= 1].copy()
    df["binary_label"] = (df["label3"] >= 2).astype(int)
    generators = sorted(df["model_name"].unique())
    results = {}
    rng = np.random.RandomState(SEED)

    print("=== 5-Gen Binary LOGO (gen-1 vs gen-2+) ===")
    for gen in generators:
        test_df = df[df["model_name"] == gen]
        train_df = df[df["model_name"] != gen]

        if test_df["binary_label"].nunique() < 2:
            print(f"  {gen:20s}  SKIPPED (single class in test)")
            continue

        train_ds = downsample(train_df, "binary_label", rng)

        clf = XGBClassifier(**XGB_PARAMS)
        clf.fit(train_ds[FEATURES].values, train_ds["binary_label"].values)
        y_pred = clf.predict(test_df[FEATURES].values)
        y_test = test_df["binary_label"].values

        f1 = f1_score(y_test, y_pred, average="macro")
        mean_f1, ci_lo, ci_hi = bootstrap_f1(y_test, y_pred)

        results[gen] = {
            "binary_f1": round(float(f1), 4),
            "ci_lower": round(ci_lo, 4),
            "ci_upper": round(ci_hi, 4),
        }
        n_test = len(test_df)
        print(f"  {gen:20s}  F1={f1:.4f}  95%CI=[{ci_lo:.4f}, {ci_hi:.4f}]  n={n_test}")

    avg_f1 = np.mean([r["binary_f1"] for r in results.values()])
    all_ci_lo = np.mean([r["ci_lower"] for r in results.values()])
    all_ci_hi = np.mean([r["ci_upper"] for r in results.values()])
    print(f"  {'AVERAGE':20s}  F1={avg_f1:.4f}  95%CI=[{all_ci_lo:.4f}, {all_ci_hi:.4f}]")
    return results, round(float(avg_f1), 4)


def main():
    df = load_data()
    print(f"Loaded {len(df)} rows, {df['model_name'].nunique()} generators")
    for gen in sorted(df["model_name"].unique()):
        n = len(df[df["model_name"] == gen])
        depths = sorted(df[df["model_name"] == gen]["depth"].unique())
        print(f"  {gen:20s}  n={n}  depths={depths}")

    print()
    results, avg_f1 = logo_binary(df)

    output = {
        "experiment": "5gen_logo_binary",
        "n_generators": 5,
        "generators": GENERATORS_5,
        "n_total_rows": len(df),
        "overall_binary_f1": avg_f1,
        "per_generator_binary": results,
        "reference": {
            "8gen_logo_binary_f1": 0.694,
            "cross_model_chains_binary_f1": 0.764,
        },
        "notes": [
            "Binary task: gen-1 vs gen-2+ only (gen-0 excluded)",
            "5 generators = cross-model chains subset",
            "XGBoost params identical to 8-gen LOGO",
        ],
    }

    os.makedirs(RESULTS_DIR, exist_ok=True)
    out_path = os.path.join(RESULTS_DIR, "5gen_logo_average.json")
    with open(out_path, "w") as f:
        json.dump(output, f, indent=2, ensure_ascii=False)
    print(f"\nResults saved to {out_path}")


if __name__ == "__main__":
    main()
