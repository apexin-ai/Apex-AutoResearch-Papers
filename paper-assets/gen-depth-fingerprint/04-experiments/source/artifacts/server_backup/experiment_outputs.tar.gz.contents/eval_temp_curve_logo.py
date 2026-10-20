"""
eval_temp_curve_logo.py — Temperature curve binary LOGO evaluation.

For each (model, temperature) pair:
  - Train XGBoost on all OTHER generators at standard t=0.7
  - Test on the target model at the specified temperature
  - Report binary F1 (gen-1 vs gen-2+) with bootstrap 95% CI

Input:
  - data/features_all_models.csv (8-gen baseline at t=0.7)
  - data/features_{model}-{temp_label}.csv (temperature variants)

Output:
  results/temp_curve_binary_logo.json
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

ROOT = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(ROOT, "data")
RESULTS_DIR = os.path.join(ROOT, "results")

N_BOOTSTRAP = 1000

# Temperature configs per model
TEMP_CONFIGS = {
    "pythia-2.8b": {
        0.5: "features_pythia-2.8b-t05.csv",
        0.7: None,  # from features_all_models.csv
        0.9: "features_pythia-2.8b-t09.csv",
    },
    "qwen3-1.7b": {
        0.5: "features_qwen3-1.7b-low-temp.csv",
        0.7: None,  # from features_all_models.csv
        0.9: "features_qwen3-1.7b-t09.csv",
        1.0: "features_qwen3-1.7b-high-temp.csv",
    },
}


def load_baseline_data():
    """Load 8-gen standard features (all at t=0.7)."""
    df = pd.read_csv(os.path.join(DATA_DIR, "features_all_models.csv"))
    # Also load llama and mistral from JSONL
    new_gens = [
        ("llama-3.2-3b", os.path.join(DATA_DIR, "llama-3.2-3b", "features_pythia410m.jsonl")),
        ("mistral-7b-v0.3", os.path.join(DATA_DIR, "mistral-7b-v0.3", "features_pythia410m.jsonl")),
    ]
    dfs = [df]
    for gen_name, path in new_gens:
        if not os.path.exists(path):
            continue
        records = []
        with open(path) as f:
            for line in f:
                rec = json.loads(line)
                rec["model_name"] = gen_name
                records.append(rec)
        dfs.append(pd.DataFrame(records))

    cols = ["model_name", "seed_id", "depth"] + FEATURES
    return pd.concat([d[cols] for d in dfs], ignore_index=True)


def load_temp_features(csv_file, model_name):
    """Load features CSV for a temperature variant."""
    path = os.path.join(DATA_DIR, csv_file)
    if not os.path.exists(path):
        return None
    df = pd.read_csv(path)
    df["model_name"] = model_name
    return df[["model_name", "seed_id", "depth"] + FEATURES]


def downsample(df, label_col, rng):
    counts = df[label_col].value_counts()
    min_n = counts.min()
    parts = []
    for lbl in sorted(counts.index):
        sub = df[df[label_col] == lbl]
        parts.append(sub.sample(n=min_n, random_state=rng, replace=False))
    return pd.concat(parts, ignore_index=True)


def bootstrap_ci(y_true, y_pred, n_boot=N_BOOTSTRAP, seed=SEED):
    rng = np.random.RandomState(seed)
    n = len(y_true)
    scores = []
    for _ in range(n_boot):
        idx = rng.randint(0, n, size=n)
        yt, yp = y_true[idx], y_pred[idx]
        if len(np.unique(yt)) < 2:
            continue
        scores.append(f1_score(yt, yp, average="macro"))
    return np.percentile(scores, 2.5), np.percentile(scores, 97.5)


def binary_logo_eval(train_df, test_df):
    """Binary LOGO: gen-1 vs gen-2+ (exclude gen-0)."""
    # Filter to depth >= 1
    train_bin = train_df[train_df["depth"] >= 1].copy()
    test_bin = test_df[test_df["depth"] >= 1].copy()

    # Binary labels: 0 = gen-1 (depth=1), 1 = gen-2+ (depth>=2)
    train_bin["label"] = (train_bin["depth"] >= 2).astype(int)
    test_bin["label"] = (test_bin["depth"] >= 2).astype(int)

    # Downsample training data
    rng = np.random.RandomState(SEED)
    train_ds = downsample(train_bin, "label", rng)

    X_train = train_ds[FEATURES].values
    y_train = train_ds["label"].values
    X_test = test_bin[FEATURES].values
    y_test = test_bin["label"].values

    clf = XGBClassifier(**XGB_PARAMS)
    clf.fit(X_train, y_train)
    y_pred = clf.predict(X_test)

    f1 = f1_score(y_test, y_pred, average="macro")
    ci_lo, ci_hi = bootstrap_ci(y_test, y_pred)

    return f1, ci_lo, ci_hi, len(test_bin)


def main():
    os.makedirs(RESULTS_DIR, exist_ok=True)
    baseline_df = load_baseline_data()
    print(f"Loaded baseline: {len(baseline_df)} rows, generators: {sorted(baseline_df['model_name'].unique())}")

    results = {}

    for model_name, temp_dict in TEMP_CONFIGS.items():
        results[model_name] = {}

        # Training data: all generators EXCEPT this one, at t=0.7
        train_df = baseline_df[baseline_df["model_name"] != model_name]
        print(f"\n{'='*60}")
        print(f"Model: {model_name} | Train on {len(train_df)} rows from other generators")

        for temp, csv_file in sorted(temp_dict.items()):
            if csv_file is None:
                # Use baseline data for this model
                test_df = baseline_df[baseline_df["model_name"] == model_name]
            else:
                test_df = load_temp_features(csv_file, model_name)
                if test_df is None:
                    print(f"  t={temp}: SKIPPED (file not found: {csv_file})")
                    continue

            f1, ci_lo, ci_hi, n = binary_logo_eval(train_df, test_df)
            results[model_name][str(temp)] = {
                "binary_f1": round(f1, 4),
                "ci_95": [round(ci_lo, 4), round(ci_hi, 4)],
                "n_test": n,
            }
            print(f"  t={temp}: Binary F1={f1:.4f}  95%CI=[{ci_lo:.4f}, {ci_hi:.4f}]  n={n}")

    # Save results
    out_path = os.path.join(RESULTS_DIR, "temp_curve_binary_logo.json")
    with open(out_path, "w") as f:
        json.dump(results, f, indent=2)
    print(f"\nResults saved to {out_path}")

    # Print summary table
    print(f"\n{'='*60}")
    print(f"{'Model':<15} {'Temp':<6} {'Binary F1':<10} {'95% CI':<20}")
    print("-" * 60)
    for model_name in sorted(results.keys()):
        for temp in sorted(results[model_name].keys(), key=float):
            r = results[model_name][temp]
            ci = f"[{r['ci_95'][0]:.4f}, {r['ci_95'][1]:.4f}]"
            print(f"{model_name:<15} {temp:<6} {r['binary_f1']:<10.4f} {ci:<20}")


if __name__ == "__main__":
    main()
