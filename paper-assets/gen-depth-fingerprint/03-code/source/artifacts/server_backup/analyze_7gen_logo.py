"""
analyze_7gen_logo.py — 7-generator LOGO analysis with OLMo instruct.

Merges OLMo instruct features into 6-gen dataset, runs 7-gen LOGO,
computes binary F1, Spearman correlations, and comparison vs base.
"""

import argparse
import json
import sys

import numpy as np
import pandas as pd
from scipy import stats
from xgboost import XGBClassifier
from sklearn.metrics import f1_score

SEED = 42
FEATURES = ["entropy_mean", "entropy_std", "entropy_min", "entropy_max",
            "tail_decay", "ttr", "hapax_ratio"]

XGB_PARAMS = dict(n_estimators=200, max_depth=6, learning_rate=0.1,
                  random_state=SEED, eval_metric="mlogloss",
                  use_label_encoder=False)

CLASS_MAP_3 = {0: 0, 1: 1, 2: 2, 3: 2, 4: 2}
BINARY_MAP = {0: 0, 1: 0, 2: 1, 3: 1, 4: 1}  # gen-0/1 vs gen-2+


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
    return {"mean": float(np.mean(arr)),
            "ci_lo": float(np.percentile(arr, 2.5)),
            "ci_hi": float(np.percentile(arr, 97.5))}


def logo_3class(df):
    df = df.copy()
    df["label"] = df["depth"].map(CLASS_MAP_3)
    generators = sorted(df["model_name"].unique())
    results = {}
    rng = np.random.RandomState(SEED)

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
        boot = bootstrap_f1(y_test, y_pred)

        results[gen] = {
            "macro_f1": round(float(macro_f1), 4),
            "gen-0_f1": round(float(per_class[0]), 4),
            "gen-1_f1": round(float(per_class[1]), 4),
            "gen-2+_f1": round(float(per_class[2]), 4),
            "bootstrap_ci": boot,
        }
        print(f"  {gen:25s}  macro-F1={macro_f1:.4f}  [{boot['ci_lo']:.4f}, {boot['ci_hi']:.4f}]")

    avg_f1 = np.mean([r["macro_f1"] for r in results.values()])
    return results, round(float(avg_f1), 4)


def binary_f1_logo(df):
    """Binary: gen-0/gen-1 vs gen-2+."""
    df = df.copy()
    df["binary_label"] = df["depth"].map(BINARY_MAP)
    generators = sorted(df["model_name"].unique())
    results = {}
    rng = np.random.RandomState(SEED)

    for gen in generators:
        test_df = df[df["model_name"] == gen]
        train_df = df[df["model_name"] != gen]
        train_ds = downsample(train_df, "binary_label", rng)

        clf = XGBClassifier(**XGB_PARAMS)
        clf.fit(train_ds[FEATURES].values, train_ds["binary_label"].values)
        y_pred = clf.predict(test_df[FEATURES].values)
        y_test = test_df["binary_label"].values

        f1 = f1_score(y_test, y_pred, average="macro")
        boot = bootstrap_f1(y_test, y_pred)
        results[gen] = {"f1": round(float(f1), 4), "bootstrap_ci": boot}

    avg_f1 = np.mean([r["f1"] for r in results.values()])
    return results, round(float(avg_f1), 4)


def spearman_analysis(df, model_name):
    sub = df[df["model_name"] == model_name]
    rho_dict = {}
    p_dict = {}
    for feat in FEATURES:
        rho, p = stats.spearmanr(sub["depth"], sub[feat])
        rho_dict[feat] = round(float(rho), 4)
        p_dict[feat] = float(p)
    return rho_dict, p_dict


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--base-features", default="data/features_all_models.csv")
    parser.add_argument("--instruct-features", required=True)
    parser.add_argument("--instruct-model-name", default="olmo-2-0425-1b-instruct")
    parser.add_argument("--output", default="results/review_p1c_olmo_instruct.json")
    args = parser.parse_args()

    import os
    root = os.path.dirname(os.path.abspath(__file__))

    base_path = os.path.join(root, args.base_features)
    inst_path = os.path.join(root, args.instruct_features)

    df_base = pd.read_csv(base_path)
    print(f"Base: {len(df_base)} rows, generators: {sorted(df_base['model_name'].unique())}")

    df_inst = pd.read_csv(inst_path)
    df_inst["model_name"] = args.instruct_model_name
    print(f"Instruct: {len(df_inst)} rows")

    # Ensure columns match
    common_cols = ["model_name", "seed_id", "depth"] + FEATURES
    df_base = df_base[common_cols]
    df_inst = df_inst[common_cols]
    df_all = pd.concat([df_base, df_inst], ignore_index=True)
    print(f"Combined: {len(df_all)} rows, {df_all['model_name'].nunique()} generators")

    # Depth distribution for instruct model
    inst_depth = df_inst["depth"].value_counts().sort_index().to_dict()
    inst_depth = {str(k): int(v) for k, v in inst_depth.items()}

    # 1. 7-gen LOGO (3-class)
    print("\n=== 7-gen LOGO (3-class) ===")
    logo_results, logo_avg = logo_3class(df_all)

    # 2. Binary F1
    print("\n=== Binary F1 (gen-0/1 vs gen-2+) ===")
    binary_results, binary_avg = binary_f1_logo(df_all)
    for gen, r in binary_results.items():
        print(f"  {gen:25s}  binary-F1={r['f1']:.4f}")

    # 3. Spearman for instruct model
    print("\n=== Spearman (instruct) ===")
    inst_rho, inst_p = spearman_analysis(df_all, args.instruct_model_name)
    for feat in FEATURES:
        print(f"  {feat:15s}: rho={inst_rho[feat]:+.4f}")

    # 4. Spearman for base OLMo
    base_rho, _ = spearman_analysis(df_all, "olmo-2-1b")

    # 5. Comparison
    comparison = {}
    for feat in FEATURES:
        comparison[feat] = {
            "instruct": inst_rho[feat],
            "base": base_rho[feat],
            "delta": round(inst_rho[feat] - base_rho[feat], 4),
        }

    # Base OLMo LOGO F1 from 6-gen
    base_olmo_6gen_f1 = None
    for gen, r in logo_results.items():
        if gen == "olmo-2-1b":
            base_olmo_6gen_f1 = r["macro_f1"]

    instruct_f1 = logo_results.get(args.instruct_model_name, {}).get("macro_f1")
    delta_vs_base = round(instruct_f1 - base_olmo_6gen_f1, 4) if instruct_f1 and base_olmo_6gen_f1 else None

    # Conclusion
    if instruct_f1 and base_olmo_6gen_f1:
        abs_delta = abs(instruct_f1 - base_olmo_6gen_f1)
        if abs_delta <= 0.03:
            conclusion = "positive: instruct tuning preserves depth signal"
        elif instruct_f1 < base_olmo_6gen_f1 - 0.05:
            conclusion = "negative: instruct tuning significantly reduces depth signal"
        else:
            conclusion = f"mixed: delta={delta_vs_base:+.4f}, within moderate range"
    else:
        conclusion = "inconclusive"

    result = {
        "experiment": "review-p1c-olmo-instruct",
        "model": "OLMo-2-0425-1B-Instruct (allenai/OLMo-2-0425-1B-Instruct)",
        "model_source": "HuggingFace",
        "n_records_instruct": len(df_inst),
        "n_records_total_7gen": len(df_all),
        "depth_distribution": inst_depth,
        "logo_7gen_3class": {
            "per_generator": logo_results,
            "average_macro_f1": logo_avg,
        },
        "binary_f1_logo": {
            "per_generator": binary_results,
            "average_f1": binary_avg,
        },
        "instruct_spearman_rho": inst_rho,
        "instruct_spearman_p": {k: f"{v:.2e}" for k, v in inst_p.items()},
        "base_olmo_spearman_rho": base_rho,
        "comparison_instruct_vs_base": comparison,
        "instruct_logo_f1": instruct_f1,
        "base_olmo_logo_f1": base_olmo_6gen_f1,
        "delta_instruct_vs_base": delta_vs_base,
        "conclusion": conclusion,
    }

    out_path = os.path.join(root, args.output)
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w") as f:
        json.dump(result, f, indent=2, ensure_ascii=False)
    print(f"\nResults saved to {out_path}")
    print(f"\n{'='*60}")
    print(f"Instruct LOGO F1: {instruct_f1}")
    print(f"Base OLMo LOGO F1: {base_olmo_6gen_f1}")
    print(f"Delta: {delta_vs_base}")
    print(f"Conclusion: {conclusion}")


if __name__ == "__main__":
    main()
