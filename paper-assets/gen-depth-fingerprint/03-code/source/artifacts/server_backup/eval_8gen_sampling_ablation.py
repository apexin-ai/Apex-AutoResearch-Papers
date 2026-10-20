"""
eval_8gen_sampling_ablation.py — Training sample size ablation on 8-gen LOGO.

Tests 25%/50%/75%/100% training fractions with 3 seeds each.
Output: results/8gen_sampling_ablation.json
"""

import json
import os
import numpy as np
import pandas as pd
from xgboost import XGBClassifier
from sklearn.metrics import f1_score

FEATURES = ["entropy_mean", "entropy_std", "entropy_min", "entropy_max",
            "tail_decay", "ttr", "hapax_ratio"]

XGB_PARAMS = dict(n_estimators=200, max_depth=6, learning_rate=0.1,
                  eval_metric="mlogloss", use_label_encoder=False)

CLASS_MAP_3 = {0: 0, 1: 1, 2: 2, 3: 2, 4: 2}

ROOT = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(ROOT, "data")
RESULTS_DIR = os.path.join(ROOT, "results")

FRACTIONS = [0.25, 0.50, 0.75, 1.0]
SEEDS = [42, 123, 456]


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


def downsample(df, label_col, rng):
    counts = df[label_col].value_counts()
    min_n = counts.min()
    parts = []
    for lbl in sorted(counts.index):
        sub = df[df[label_col] == lbl]
        parts.append(sub.sample(n=min_n, random_state=rng, replace=False))
    return pd.concat(parts, ignore_index=True)


def logo_eval(df, label_col, fraction, seed):
    """Run LOGO CV with given training fraction and seed. Returns per-gen F1 list."""
    generators = sorted(df["model_name"].unique())
    f1s = []
    rng = np.random.RandomState(seed)

    for gen in generators:
        test_df = df[df["model_name"] == gen]
        train_df = df[df["model_name"] != gen]

        # Class-balanced downsampling first
        train_ds = downsample(train_df, label_col, rng)

        # Then subsample to fraction
        if fraction < 1.0:
            n_sample = max(1, int(len(train_ds) * fraction))
            train_ds = train_ds.sample(n=n_sample, random_state=rng, replace=False)

        n_classes = len(df[label_col].unique())
        clf = XGBClassifier(**XGB_PARAMS, random_state=seed)
        if n_classes > 2:
            clf.set_params(num_class=n_classes)
        clf.fit(train_ds[FEATURES].values, train_ds[label_col].values)

        y_pred = clf.predict(test_df[FEATURES].values)
        y_test = test_df[label_col].values

        avg = "macro" if n_classes > 2 else "binary"
        macro_f1 = f1_score(y_test, y_pred, average=avg)
        f1s.append(float(macro_f1))

    return np.mean(f1s)


def run_ablation(df, task_name, label_col):
    print(f"\n=== {task_name} ===")
    results = {}

    for frac in FRACTIONS:
        key = f"{int(frac*100)}pct"
        seed_scores = {}
        for s in SEEDS:
            f1 = logo_eval(df, label_col, frac, s)
            seed_scores[str(s)] = round(f1, 4)
            print(f"  {key} seed={s}: F1={f1:.4f}")

        vals = list(seed_scores.values())
        results[key] = {
            "f1_mean": round(float(np.mean(vals)), 4),
            "f1_std": round(float(np.std(vals)), 4),
            "seeds": seed_scores,
        }
        print(f"  {key} mean={results[key]['f1_mean']:.4f} ± {results[key]['f1_std']:.4f}")

    return results


def main():
    df = load_data()
    print(f"Loaded {len(df)} rows, {df['model_name'].nunique()} generators")

    # 3-class
    df_3class = df.copy()
    df_3class["label"] = df_3class["depth"].map(CLASS_MAP_3)
    three_results = run_ablation(df_3class, "3-class LOGO", "label")

    # Binary (gen-1 vs gen-2+, exclude gen-0)
    df_binary = df[df["depth"] > 0].copy()
    df_binary["label"] = (df_binary["depth"].map(CLASS_MAP_3) - 1).clip(lower=0)  # 0=gen-1, 1=gen-2+
    binary_results = run_ablation(df_binary, "Binary LOGO (gen-1 vs gen-2+)", "label")

    output = {
        "3class": three_results,
        "binary": binary_results,
        "config": {
            "n_generators": 8,
            "sampling_seeds": SEEDS,
            "fractions": FRACTIONS,
        },
    }

    os.makedirs(RESULTS_DIR, exist_ok=True)
    out_path = os.path.join(RESULTS_DIR, "8gen_sampling_ablation.json")
    with open(out_path, "w") as f:
        json.dump(output, f, indent=2)
    print(f"\nSaved: {out_path}")

    # Summary
    print(f"\n{'='*60}")
    print(f"{'Fraction':<10} {'3class F1':>12} {'Binary F1':>12}")
    print(f"{'-'*34}")
    for frac in FRACTIONS:
        key = f"{int(frac*100)}pct"
        t = three_results[key]
        b = binary_results[key]
        print(f"{key:<10} {t['f1_mean']:.4f}±{t['f1_std']:.4f}  {b['f1_mean']:.4f}±{b['f1_std']:.4f}")


if __name__ == "__main__":
    main()
