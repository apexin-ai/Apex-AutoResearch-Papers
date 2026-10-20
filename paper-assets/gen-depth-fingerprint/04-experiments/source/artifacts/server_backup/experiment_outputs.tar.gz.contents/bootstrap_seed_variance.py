"""
bootstrap_seed_variance.py — 5-seed LOGO binary evaluation for stability check.
CPU-only. Uses features_8gen.csv.
"""

import json
import os
import numpy as np
import pandas as pd
from xgboost import XGBClassifier
from sklearn.metrics import f1_score

SEEDS = [42, 123, 456, 789, 1024]
FEATURES = ["entropy_mean", "entropy_std", "entropy_min", "entropy_max",
            "tail_decay", "ttr", "hapax_ratio"]
CLASS_MAP_3 = {0: 0, 1: 1, 2: 2, 3: 2, 4: 2}

ROOT = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(ROOT, "data", "features_8gen.csv")
RESULTS_DIR = os.path.join(ROOT, "results")


def downsample(df, label_col, rng):
    counts = df[label_col].value_counts()
    min_n = counts.min()
    parts = []
    for lbl in sorted(counts.index):
        sub = df[df[label_col] == lbl]
        parts.append(sub.sample(n=min_n, random_state=rng, replace=False))
    return pd.concat(parts, ignore_index=True)


def logo_binary_one_seed(df, seed):
    xgb_params = dict(
        n_estimators=200, max_depth=6, learning_rate=0.1,
        random_state=seed, eval_metric="mlogloss",
        use_label_encoder=False, tree_method="hist"
        
    )
    generators = sorted(df["model_name"].unique())
    rng = np.random.RandomState(seed)
    per_gen = {}

    for gen in generators:
        test_df = df[df["model_name"] == gen]
        train_df = df[df["model_name"] != gen]

        if test_df["binary_label"].nunique() < 2:
            continue

        train_ds = downsample(train_df, "binary_label", rng)
        clf = XGBClassifier(**xgb_params)
        clf.fit(train_ds[FEATURES].values, train_ds["binary_label"].values)
        y_pred = clf.predict(test_df[FEATURES].values)
        y_test = test_df["binary_label"].values
        f1 = f1_score(y_test, y_pred, average="macro")
        per_gen[gen] = round(float(f1), 4)

    avg_f1 = round(float(np.mean(list(per_gen.values()))), 4)
    return avg_f1, per_gen


def main():
    df = pd.read_csv(DATA_PATH)
    print(f"Loaded {len(df)} rows, {df['model_name'].nunique()} generators")

    df["label3"] = df["depth"].map(CLASS_MAP_3)
    df = df[df["label3"] >= 1].copy()
    df["binary_label"] = (df["label3"] >= 2).astype(int)
    print(f"Binary subset: {len(df)} rows (gen-0 excluded)")

    all_f1 = []
    all_per_gen = {}

    for seed in SEEDS:
        print(f"\n--- Seed {seed} ---")
        avg_f1, per_gen = logo_binary_one_seed(df, seed)
        all_f1.append(avg_f1)
        print(f"  Average binary F1: {avg_f1:.4f}")
        for gen, f1 in sorted(per_gen.items()):
            print(f"    {gen:20s}  F1={f1:.4f}")
            all_per_gen.setdefault(gen, []).append(f1)

    mean_f1 = round(float(np.mean(all_f1)), 4)
    std_f1 = round(float(np.std(all_f1)), 4)

    per_gen_std = {}
    for gen, vals in sorted(all_per_gen.items()):
        per_gen_std[gen] = round(float(np.std(vals)), 4)

    per_gen_mean = {}
    for gen, vals in sorted(all_per_gen.items()):
        per_gen_mean[gen] = round(float(np.mean(vals)), 4)

    print(f"\n{'='*60}")
    print(f"5-seed summary: mean={mean_f1:.4f} ± std={std_f1:.4f}")
    print(f"{'='*60}")
    print(f"{'Generator':20s} {'Mean F1':>8s} {'Std':>8s}")
    print(f"{'-'*40}")
    for gen in sorted(per_gen_std.keys()):
        print(f"{gen:20s} {per_gen_mean[gen]:8.4f} {per_gen_std[gen]:8.4f}")

    output = {
        "seeds": SEEDS,
        "binary_f1": all_f1,
        "mean": mean_f1,
        "std": std_f1,
        "per_generator_mean": per_gen_mean,
        "per_generator_std": per_gen_std,
        "per_generator_all_seeds": all_per_gen,
    }

    os.makedirs(RESULTS_DIR, exist_ok=True)
    out_path = os.path.join(RESULTS_DIR, "bootstrap_seed_variance.json")
    with open(out_path, "w") as f:
        json.dump(output, f, indent=2)
    print(f"\nResults saved to {out_path}")


if __name__ == "__main__":
    main()
