"""
review_p1c_qwen06b_instruct.py — Compare Qwen3-0.6B instruct vs base depth response.

Computes: Spearman ρ per feature, 7-gen LOGO (adding instruct to existing 6 generators),
3-class F1, binary F1, feature drift comparison.
"""

import json
import os
import sys
import numpy as np
import pandas as pd
from scipy import stats
from xgboost import XGBClassifier
from sklearn.metrics import f1_score

SEED = 42
N_BOOT = 1000
FEATURES = ["entropy_mean", "entropy_std", "entropy_min", "entropy_max",
            "tail_decay", "ttr", "hapax_ratio"]
CLASS_MAP = {0: 0, 1: 1, 2: 2, 3: 2, 4: 2}
CLASS_NAMES = ["gen-0", "gen-1", "gen-2+"]
XGB_PARAMS = dict(n_estimators=200, max_depth=6, learning_rate=0.1,
                  random_state=SEED, eval_metric="mlogloss",
                  use_label_encoder=False)

PROJECT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def downsample(df, rng):
    counts = df["label"].value_counts()
    min_n = counts.min()
    parts = []
    for lbl in sorted(counts.index):
        sub = df[df["label"] == lbl]
        parts.append(sub.sample(n=min_n, random_state=rng, replace=False))
    return pd.concat(parts, ignore_index=True)


def bootstrap_f1(y_true, y_pred, n_boot=N_BOOT, seed=SEED):
    rng = np.random.RandomState(seed)
    n = len(y_true)
    scores = {"macro": []}
    for _ in range(n_boot):
        idx = rng.randint(0, n, size=n)
        yt, yp = y_true[idx], y_pred[idx]
        if len(np.unique(yt)) < len(set(y_true)):
            continue
        scores["macro"].append(f1_score(yt, yp, average="macro"))
    arr = np.array(scores["macro"])
    return {"mean": float(np.mean(arr)),
            "ci_lo": float(np.percentile(arr, 2.5)),
            "ci_hi": float(np.percentile(arr, 97.5))}


def compute_spearman(df, features):
    rho_map, p_map = {}, {}
    for feat in features:
        if feat not in df.columns:
            continue
        rho, p = stats.spearmanr(df["depth"], df[feat])
        rho_map[feat] = round(float(rho), 4)
        p_map[feat] = float(p)
    return rho_map, p_map


def logo_eval(df_all, features=FEATURES):
    """Leave-One-Generator-Out evaluation."""
    df_all["label"] = df_all["depth"].map(CLASS_MAP)
    generators = sorted(df_all["model_name"].unique())
    results = {}
    rng = np.random.RandomState(SEED)

    for gen in generators:
        test_df = df_all[df_all["model_name"] == gen]
        train_df = df_all[df_all["model_name"] != gen]
        train_ds = downsample(train_df, rng)

        clf = XGBClassifier(**XGB_PARAMS)
        clf.fit(train_ds[features].values, train_ds["label"].values)
        y_pred = clf.predict(test_df[features].values)
        y_test = test_df["label"].values

        macro_f1 = f1_score(y_test, y_pred, average="macro")
        per_class = f1_score(y_test, y_pred, average=None, labels=[0, 1, 2])
        boot = bootstrap_f1(y_test, y_pred)

        results[gen] = {
            "macro_f1": round(float(macro_f1), 4),
            "per_class_f1": {CLASS_NAMES[i]: round(float(per_class[i]), 4) for i in range(3)},
            "bootstrap_ci": boot,
        }
        print(f"  LOGO {gen:25s} F1={macro_f1:.4f} [{boot['ci_lo']:.4f}, {boot['ci_hi']:.4f}]")

    avg_f1 = np.mean([r["macro_f1"] for r in results.values()])
    return results, round(float(avg_f1), 4)


def binary_eval(df_all, features=FEATURES):
    """Binary classification: gen-0 (human) vs gen-1+ (machine)."""
    df_bin = df_all.copy()
    df_bin["label"] = (df_bin["depth"] > 0).astype(int)
    generators = sorted(df_bin["model_name"].unique())
    results = {}
    rng = np.random.RandomState(SEED)

    for gen in generators:
        test_df = df_bin[df_bin["model_name"] == gen]
        train_df = df_bin[df_bin["model_name"] != gen]
        train_ds = downsample(train_df, rng)

        clf = XGBClassifier(**{**XGB_PARAMS, "eval_metric": "logloss"})
        clf.fit(train_ds[features].values, train_ds["label"].values)
        y_pred = clf.predict(test_df[features].values)
        y_test = test_df["label"].values

        f1 = f1_score(y_test, y_pred, average="binary")
        results[gen] = round(float(f1), 4)

    avg_f1 = np.mean(list(results.values()))
    return results, round(float(avg_f1), 4)


def main():
    data_dir = os.path.join(PROJECT, "data")

    # Load instruct features
    instruct_path = os.path.join(data_dir, "features_qwen3-0.6b-instruct.csv")
    if not os.path.exists(instruct_path):
        print(f"ERROR: {instruct_path} not found")
        sys.exit(1)
    df_inst = pd.read_csv(instruct_path)
    print(f"Instruct features: {len(df_inst)} records")

    # Load base features for comparison
    base_path = os.path.join(data_dir, "features_qwen3-0.6b.csv")
    df_base = pd.read_csv(base_path)
    print(f"Base features: {len(df_base)} records")

    # --- Spearman correlations ---
    print("\n=== Spearman Correlations ===")
    inst_rho, inst_p = compute_spearman(df_inst, FEATURES)
    base_rho, base_p = compute_spearman(df_base, FEATURES)

    print(f"{'Feature':20s} {'Instruct':>10s} {'Base':>10s} {'Delta':>10s}")
    comparison = {}
    for feat in FEATURES:
        ir = inst_rho.get(feat, 0)
        br = base_rho.get(feat, 0)
        delta = round(ir - br, 4)
        comparison[feat] = {"instruct": ir, "base": br, "delta": delta}
        print(f"  {feat:18s} {ir:+10.4f} {br:+10.4f} {delta:+10.4f}")

    # --- Depth distribution ---
    depth_dist = df_inst["depth"].value_counts().sort_index().to_dict()
    depth_dist = {str(k): int(v) for k, v in depth_dist.items()}

    # --- 7-gen LOGO ---
    print("\n=== 7-Generator LOGO CV ===")
    all_models_path = os.path.join(data_dir, "features_all_models.csv")
    df_6gen = pd.read_csv(all_models_path)

    # Ensure instruct has model_name column
    if "model_name" not in df_inst.columns:
        df_inst["model_name"] = "qwen3-0.6b-instruct"

    df_7gen = pd.concat([df_6gen, df_inst], ignore_index=True)
    print(f"Combined: {len(df_7gen)} records, {df_7gen['model_name'].nunique()} generators")

    logo_results, logo_avg_f1 = logo_eval(df_7gen)

    # --- Binary LOGO ---
    print("\n=== Binary LOGO CV ===")
    binary_results, binary_avg_f1 = binary_eval(df_7gen)
    print(f"  Binary avg F1: {binary_avg_f1}")

    # --- Per-depth feature means ---
    depth_means = {}
    for d in sorted(df_inst["depth"].unique()):
        subset = df_inst[df_inst["depth"] == d]
        depth_means[str(int(d))] = {
            feat: round(float(subset[feat].mean()), 4) for feat in FEATURES
        }

    # --- Token count stats ---
    gen_path = os.path.join(data_dir, "qwen3-0.6b-instruct", "generations_shard0.jsonl")
    token_stats = {}
    if os.path.exists(gen_path):
        records = []
        with open(gen_path) as f:
            for line in f:
                if line.strip():
                    records.append(json.loads(line))
        gen_df = pd.DataFrame(records)
        for d in sorted(gen_df["depth"].unique()):
            sub = gen_df[gen_df["depth"] == d]
            token_stats[str(int(d))] = {
                "mean_tokens": round(float(sub["token_count"].mean()), 1),
                "median_tokens": int(sub["token_count"].median()),
            }

    # --- Assemble results ---
    result = {
        "experiment_id": "review-p1c-qwen06b-instruct",
        "model": "Qwen3-0.6B (instruct)",
        "model_path": "Qwen/Qwen3-0.6B",
        "n_records_instruct": len(df_inst),
        "n_records_base": len(df_base),
        "depth_distribution": depth_dist,
        "token_stats_per_depth": token_stats,
        "spearman_instruct": inst_rho,
        "spearman_base": base_rho,
        "spearman_comparison": comparison,
        "logo_7gen": {
            "per_generator": logo_results,
            "average_macro_f1": logo_avg_f1,
            "instruct_held_out_f1": logo_results.get("qwen3-0.6b-instruct", {}).get("macro_f1"),
            "base_held_out_f1": logo_results.get("qwen3-0.6b", {}).get("macro_f1"),
        },
        "binary_logo_7gen": {
            "per_generator": binary_results,
            "average_f1": binary_avg_f1,
        },
        "depth_means": depth_means,
        "conclusion": "",
    }

    # --- Conclusion ---
    inst_f1 = logo_results.get("qwen3-0.6b-instruct", {}).get("macro_f1", 0)
    base_f1 = logo_results.get("qwen3-0.6b", {}).get("macro_f1", 0)
    f1_delta = inst_f1 - base_f1

    drift_features_ok = all(abs(inst_rho.get(f, 0)) > 0.3 for f in ["hapax_ratio", "ttr", "entropy_mean"])

    if abs(f1_delta) <= 0.03:
        verdict = "POSITIVE"
        explanation = f"Instruct F1 ({inst_f1:.3f}) within ±3pp of base ({base_f1:.3f}); instruct mode does not erase depth signal."
    elif f1_delta > 0.03:
        verdict = "POSITIVE_STRONG"
        explanation = f"Instruct F1 ({inst_f1:.3f}) exceeds base ({base_f1:.3f}) by {f1_delta:+.3f}; instruct mode may amplify depth signal."
    else:
        verdict = "NEGATIVE"
        explanation = f"Instruct F1 ({inst_f1:.3f}) below base ({base_f1:.3f}) by {f1_delta:+.3f}; instruct mode attenuates depth signal."

    result["conclusion"] = {
        "verdict": verdict,
        "f1_delta": round(f1_delta, 4),
        "drift_features_preserved": drift_features_ok,
        "explanation": explanation,
    }

    # --- Save ---
    out_path = os.path.join(PROJECT, "results", "review_p1c_qwen06b_instruct.json")
    with open(out_path, "w") as f:
        json.dump(result, f, indent=2, ensure_ascii=False)
    print(f"\nResults saved to {out_path}")

    # Summary
    print(f"\n{'='*60}")
    print(f"Model: {result['model']}")
    print(f"Instruct LOGO F1: {inst_f1:.4f}")
    print(f"Base LOGO F1: {base_f1:.4f}")
    print(f"Delta: {f1_delta:+.4f}")
    print(f"7-gen avg LOGO F1: {logo_avg_f1:.4f}")
    print(f"Binary avg F1: {binary_avg_f1:.4f}")
    print(f"Verdict: {verdict}")
    print(f"Explanation: {explanation}")


if __name__ == "__main__":
    main()
