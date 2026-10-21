# Anonymous submission — EMNLP 2026 ARR
"""
eval_8gen_logo.py -- 8-generator LOGO cross-validation.

8 generators from features_all_models.csv (5 families):
  pythia-2.8b, pythia-1b, olmo-2-1b, qwen3-0.6b, qwen3-1.7b, qwen3-8b,
  llama-3.2-3b, mistral-7b-v0.3

Tasks:
  - 3-class LOGO: gen-0 / gen-1 / gen-2+
  - Binary LOGO: gen-1 vs gen-2+ (exclude gen-0)
  - Bootstrap 95% CI (n=1000)
  - Comparison vs 6-gen baseline
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
RESULTS_DIR = os.path.join(ROOT, "results")


def load_data():
    df = pd.read_csv(os.path.join(DATA_DIR, "features_all_models.csv"))
    cols = ["model_name", "seed_id", "depth"] + FEATURES
    return df[cols]


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


def logo_3class(df):
    df = df.copy()
    df["label"] = df["depth"].map(CLASS_MAP_3)
    generators = sorted(df["model_name"].unique())
    results = {}
    rng = np.random.RandomState(SEED)

    print("=== 3-class LOGO (gen-0 / gen-1 / gen-2+) ===")
    for gen in generators:
        test_df = df[df["model_name"] == gen]
        train_df = df[df["model_name"] != gen]
        train_ds = downsample(train_df, "label", rng)

        clf = XGBClassifier(**XGB_PARAMS)
        clf.fit(train_ds[FEATURES].values, train_ds["label"].values)
        y_pred = clf.predict(test_df[FEATURES].values)
        y_test = test_df["label"].values

        macro_f1 = f1_score(y_test, y_pred, average="macro")
        per_class = f1_score(y_test, y_pred, average=None, labels=[0, 1, 2])
        mean_f1, ci_lo, ci_hi = bootstrap_f1(y_test, y_pred)

        results[gen] = {
            "macro_f1": round(float(macro_f1), 4),
            "gen-0_f1": round(float(per_class[0]), 4),
            "gen-1_f1": round(float(per_class[1]), 4),
            "gen-2+_f1": round(float(per_class[2]), 4),
            "ci_lower": round(ci_lo, 4),
            "ci_upper": round(ci_hi, 4),
        }
        n_test = len(test_df)
        print(f"  {gen:20s}  F1={macro_f1:.4f}  95%CI=[{ci_lo:.4f}, {ci_hi:.4f}]  n={n_test}")

    avg_f1 = np.mean([r["macro_f1"] for r in results.values()])
    print(f"  {'AVERAGE':20s}  F1={avg_f1:.4f}")
    return results, round(float(avg_f1), 4)


def logo_binary(df):
    """Binary: gen-1 vs gen-2+ (exclude gen-0)."""
    df = df.copy()
    df["label3"] = df["depth"].map(CLASS_MAP_3)
    df = df[df["label3"] >= 1].copy()
    df["binary_label"] = (df["label3"] >= 2).astype(int)
    generators = sorted(df["model_name"].unique())
    results = {}
    rng = np.random.RandomState(SEED)

    print("\n=== Binary LOGO (gen-1 vs gen-2+) ===")
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
    print(f"  {'AVERAGE':20s}  F1={avg_f1:.4f}")
    return results, round(float(avg_f1), 4)


def main():
    df = load_data()
    print(f"Loaded {len(df)} rows, {df['model_name'].nunique()} generators")
    for gen in sorted(df["model_name"].unique()):
        n = len(df[df["model_name"] == gen])
        depths = sorted(df[df["model_name"] == gen]["depth"].unique())
        print(f"  {gen:20s}  n={n}  depths={depths}")

    print()
    three_results, three_avg = logo_3class(df)
    binary_results, binary_avg = logo_binary(df)

    baseline_path = os.path.join(DATA_DIR, "cross_generator_results.json")
    baseline_6gen_f1 = None
    baseline_6gen_per_gen = {}
    if os.path.exists(baseline_path):
        with open(baseline_path) as f:
            baseline = json.load(f)
        logo_section = baseline.get("leave_one_generator_out", {})
        if "average_macro_f1" in logo_section:
            baseline_6gen_f1 = logo_section["average_macro_f1"]
        else:
            f1s = [v["macro_f1"] for v in logo_section.values()
                   if isinstance(v, dict) and "macro_f1" in v]
            if f1s:
                baseline_6gen_f1 = round(float(np.mean(f1s)), 4)
        for gen, v in logo_section.items():
            if isinstance(v, dict) and "macro_f1" in v:
                baseline_6gen_per_gen[gen] = v["macro_f1"]

    delta_per_gen = {}
    for gen in baseline_6gen_per_gen:
        if gen in three_results:
            delta_per_gen[gen] = round(three_results[gen]["macro_f1"] - baseline_6gen_per_gen[gen], 4)

    delta_overall = None
    if baseline_6gen_f1 is not None:
        delta_overall = round(three_avg - baseline_6gen_f1, 4)

    output = {
        "experiment": "8gen_logo",
        "n_generators": 8,
        "n_total_rows": len(df),
        "overall_3class_f1": three_avg,
        "overall_binary_f1": binary_avg,
        "per_generator_3class": three_results,
        "per_generator_binary": binary_results,
        "baseline_6gen_3class_f1": baseline_6gen_f1,
        "delta_8gen_vs_6gen": delta_overall,
        "delta_per_generator_vs_6gen": delta_per_gen,
    }

    os.makedirs(RESULTS_DIR, exist_ok=True)
    out_path = os.path.join(RESULTS_DIR, "8gen_logo_results.json")
    with open(out_path, "w") as f:
        json.dump(output, f, indent=2, ensure_ascii=False)
    print(f"\nResults saved to {out_path}")

    print(f"\n{'='*80}")
    print(f"8-gen LOGO Summary")
    print(f"{'='*80}")
    print(f"{'Generator':20s} {'3class-F1':>10s} {'95% CI':>20s} {'Binary-F1':>10s}")
    print(f"{'-'*60}")
    for gen in sorted(three_results.keys()):
        r3 = three_results[gen]
        rb = binary_results.get(gen, {})
        b_str = f"{rb['binary_f1']:.4f}" if rb else "N/A"
        print(f"{gen:20s} {r3['macro_f1']:10.4f} [{r3['ci_lower']:.4f}, {r3['ci_upper']:.4f}] {b_str:>10s}")
    print(f"{'-'*60}")
    print(f"{'AVERAGE':20s} {three_avg:10.4f} {'':20s} {binary_avg:10.4f}")


if __name__ == "__main__":
    main()
