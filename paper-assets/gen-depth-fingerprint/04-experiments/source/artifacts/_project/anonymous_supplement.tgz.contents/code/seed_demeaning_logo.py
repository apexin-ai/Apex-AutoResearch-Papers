"""
seed_demeaning_logo.py — Seed-level demeaning + 8-gen LOGO binary eval.

For each (seed_id, model_name), subtract the depth-0 feature values
from all deeper depths. This removes seed-level topic signal.
Then run binary LOGO (gen-1 vs gen-2+) on the delta features.
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

ROOT = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(ROOT, "..", "data")
RESULTS_DIR = os.path.join(ROOT, "..", "results")


def load_data():
    df_base = pd.read_csv(os.path.join(DATA_DIR, "features_all_models.csv"))
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
                rec["model_name"] = gen_name
                records.append(rec)
        dfs.append(pd.DataFrame(records))

    cols = ["model_name", "seed_id", "depth"] + FEATURES
    df = pd.concat([d[cols] for d in dfs], ignore_index=True)
    return df


def seed_demean(df):
    """Subtract depth-0 features from each (model_name, seed_id) group."""
    baseline = df[df["depth"] == 0].set_index(["model_name", "seed_id"])[FEATURES]
    df_deep = df[df["depth"] >= 1].copy()
    idx = df_deep.set_index(["model_name", "seed_id"]).index
    base_vals = baseline.reindex(idx).values
    df_deep[FEATURES] = df_deep[FEATURES].values - base_vals

    n_before = len(df_deep)
    df_deep = df_deep.dropna(subset=FEATURES)
    n_after = len(df_deep)
    if n_before != n_after:
        print(f"  Warning: dropped {n_before - n_after} rows without depth-0 baseline")
    return df_deep


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


def logo_binary_demeaned(df):
    """Binary LOGO on demeaned features: gen-1 vs gen-2+."""
    df = df.copy()
    df["label3"] = df["depth"].map(CLASS_MAP_3)
    df["binary_label"] = (df["label3"] >= 2).astype(int)
    generators = sorted(df["model_name"].unique())
    results = {}
    rng = np.random.RandomState(SEED)

    print("\n=== Binary LOGO (gen-1 vs gen-2+) with seed demeaning ===")
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
            "n_test": int(len(test_df)),
        }
        print(f"  {gen:20s}  F1={f1:.4f}  95%CI=[{ci_lo:.4f}, {ci_hi:.4f}]  n={len(test_df)}")

    avg_f1 = np.mean([r["binary_f1"] for r in results.values()])
    print(f"  {'AVERAGE':20s}  F1={avg_f1:.4f}")
    return results, round(float(avg_f1), 4)


def main():
    df = load_data()
    print(f"Loaded {len(df)} rows, {df['model_name'].nunique()} generators")

    print("\nApplying seed-level demeaning (subtract depth-0 features)...")
    df_demeaned = seed_demean(df)
    print(f"After demeaning: {len(df_demeaned)} rows (depth >= 1 only)")

    for gen in sorted(df_demeaned["model_name"].unique()):
        sub = df_demeaned[df_demeaned["model_name"] == gen]
        depths = sorted(sub["depth"].unique())
        print(f"  {gen:20s}  n={len(sub)}  depths={depths}")

    binary_results, binary_avg = logo_binary_demeaned(df_demeaned)

    os.makedirs(RESULTS_DIR, exist_ok=True)
    output = {
        "experiment": "seed_demeaning_logo",
        "description": "Binary LOGO (gen-1 vs gen-2+) after subtracting depth-0 features per (seed, generator)",
        "binary_logo_average_f1": binary_avg,
        "per_generator": binary_results,
    }
    out_path = os.path.join(RESULTS_DIR, "seed_demeaning_logo.json")
    with open(out_path, "w") as f:
        json.dump(output, f, indent=2)
    print(f"\nResults saved to {out_path}")


if __name__ == "__main__":
    main()
