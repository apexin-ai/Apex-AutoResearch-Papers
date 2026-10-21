"""Group ablation (LOGO) + XGBoost hyperparameter sensitivity."""

import json
import os
import numpy as np
import pandas as pd
from xgboost import XGBClassifier
from sklearn.metrics import f1_score

SEED = 42
DATA_PATH = os.path.join(os.path.dirname(__file__), "..", "supplement", "data",
                         "features_all_models.csv")
OUT_DIR = os.path.dirname(os.path.abspath(__file__))

CLASS_MAP_3 = {0: 0, 1: 1, 2: 2, 3: 2, 4: 2}

FEATURE_GROUPS = {
    "A_drifting": ["entropy_mean", "ttr", "hapax_ratio"],
    "B_non_drifting": ["entropy_std", "entropy_max", "entropy_min", "tail_decay"],
    "C_all7": ["entropy_mean", "entropy_std", "entropy_min", "entropy_max",
               "tail_decay", "ttr", "hapax_ratio"],
}


def downsample(df, label_col, rng):
    counts = df[label_col].value_counts()
    min_n = counts.min()
    parts = []
    for lbl in sorted(counts.index):
        sub = df[df[label_col] == lbl]
        parts.append(sub.sample(n=min_n, random_state=rng, replace=False))
    return pd.concat(parts, ignore_index=True)


def run_logo(df, features, xgb_params):
    df = df.copy()
    df["label3"] = df["depth"].map(CLASS_MAP_3)
    generators = sorted(df["model_name"].unique())
    rng = np.random.RandomState(SEED)

    per_gen = {}
    for gen in generators:
        test_df = df[df["model_name"] == gen]
        train_df = df[df["model_name"] != gen]

        # 3-class
        train_ds = downsample(train_df, "label3", rng)
        clf3 = XGBClassifier(**xgb_params)
        clf3.fit(train_ds[features].values, train_ds["label3"].values)
        y3_pred = clf3.predict(test_df[features].values)
        f1_3 = f1_score(test_df["label3"].values, y3_pred, average="macro")

        # binary (gen-1 vs gen-2+, exclude depth=0)
        train_bin = train_df[train_df["depth"] >= 1].copy()
        train_bin["label_bin"] = (train_bin["depth"] >= 2).astype(int)
        test_bin = test_df[test_df["depth"] >= 1].copy()
        test_bin["label_bin"] = (test_bin["depth"] >= 2).astype(int)
        train_ds_b = downsample(train_bin, "label_bin", rng)
        clf_b = XGBClassifier(**xgb_params)
        clf_b.fit(train_ds_b[features].values, train_ds_b["label_bin"].values)
        yb_pred = clf_b.predict(test_bin[features].values)
        f1_b = f1_score(test_bin["label_bin"].values, yb_pred, average="macro")

        per_gen[gen] = {"f1_3class": round(float(f1_3), 4),
                        "f1_binary": round(float(f1_b), 4)}

    f1_3_vals = [v["f1_3class"] for v in per_gen.values()]
    f1_b_vals = [v["f1_binary"] for v in per_gen.values()]
    summary = {
        "f1_3class_mean": round(float(np.mean(f1_3_vals)), 4),
        "f1_3class_std": round(float(np.std(f1_3_vals)), 4),
        "f1_binary_mean": round(float(np.mean(f1_b_vals)), 4),
        "f1_binary_std": round(float(np.std(f1_b_vals)), 4),
        "per_generator": per_gen,
    }
    return summary


def task1_group_ablation(df):
    xgb_params = dict(n_estimators=200, max_depth=6, learning_rate=0.1,
                      random_state=SEED, eval_metric="mlogloss",
                      use_label_encoder=False)
    results = {}
    for group_name, feats in FEATURE_GROUPS.items():
        print(f"\n--- Group {group_name}: {feats} ---")
        res = run_logo(df, feats, xgb_params)
        results[group_name] = res
        print(f"  3-class macro F1: {res['f1_3class_mean']:.4f} ± {res['f1_3class_std']:.4f}")
        print(f"  Binary F1:        {res['f1_binary_mean']:.4f} ± {res['f1_binary_std']:.4f}")
        for gen, v in sorted(res["per_generator"].items()):
            print(f"    {gen:20s}  3c={v['f1_3class']:.4f}  bin={v['f1_binary']:.4f}")
    return results


def task2_sensitivity(df):
    depths = [3, 4, 6, 8]
    results = {}
    for md in depths:
        xgb_params = dict(n_estimators=200, max_depth=md, learning_rate=0.1,
                          random_state=SEED, eval_metric="mlogloss",
                          use_label_encoder=False)
        res = run_logo(df, FEATURE_GROUPS["C_all7"], xgb_params)
        results[f"max_depth_{md}"] = {
            "f1_3class_mean": res["f1_3class_mean"],
            "f1_3class_std": res["f1_3class_std"],
            "f1_binary_mean": res["f1_binary_mean"],
            "f1_binary_std": res["f1_binary_std"],
        }
        print(f"  max_depth={md}:  3c={res['f1_3class_mean']:.4f}±{res['f1_3class_std']:.4f}  bin={res['f1_binary_mean']:.4f}±{res['f1_binary_std']:.4f}")
    return results


def main():
    df = pd.read_csv(DATA_PATH)
    cols = ["model_name", "seed_id", "depth"] + FEATURE_GROUPS["C_all7"]
    df = df[cols]
    print(f"Loaded {len(df)} rows, {df['model_name'].nunique()} generators\n")

    print("=" * 70)
    print("TASK 1: Group Ablation (LOGO)")
    print("=" * 70)
    ablation = task1_group_ablation(df)

    print(f"\n{'=' * 70}")
    print("TASK 2: XGBoost max_depth Sensitivity (all-7 features, LOGO)")
    print("=" * 70)
    sensitivity = task2_sensitivity(df)

    # Save
    abl_path = os.path.join(OUT_DIR, "group_ablation_results.json")
    with open(abl_path, "w") as f:
        json.dump(ablation, f, indent=2)
    print(f"\nSaved: {abl_path}")

    sens_path = os.path.join(OUT_DIR, "xgb_sensitivity_results.json")
    with open(sens_path, "w") as f:
        json.dump(sensitivity, f, indent=2)
    print(f"Saved: {sens_path}")

    # Summary table
    print(f"\n{'=' * 70}")
    print("SUMMARY")
    print(f"{'=' * 70}")
    print(f"{'Group':<20s} {'3-class F1':>15s} {'Binary F1':>15s}")
    print("-" * 50)
    for g in ["A_drifting", "B_non_drifting", "C_all7"]:
        r = ablation[g]
        print(f"{g:<20s} {r['f1_3class_mean']:.4f}±{r['f1_3class_std']:.4f}   {r['f1_binary_mean']:.4f}±{r['f1_binary_std']:.4f}")
    print()
    print(f"{'max_depth':<20s} {'3-class F1':>15s} {'Binary F1':>15s}")
    print("-" * 50)
    for md in [3, 4, 6, 8]:
        r = sensitivity[f"max_depth_{md}"]
        print(f"{md:<20d} {r['f1_3class_mean']:.4f}±{r['f1_3class_std']:.4f}   {r['f1_binary_mean']:.4f}±{r['f1_binary_std']:.4f}")


if __name__ == "__main__":
    main()
