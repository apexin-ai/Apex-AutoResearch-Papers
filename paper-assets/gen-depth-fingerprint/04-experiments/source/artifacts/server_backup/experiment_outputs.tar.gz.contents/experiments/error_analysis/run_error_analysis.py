import json
import os
import numpy as np
import pandas as pd
from xgboost import XGBClassifier
from sklearn.metrics import f1_score
from scipy.stats import mannwhitneyu

SEED = 42
FEATURES = ["entropy_mean", "entropy_std", "entropy_min", "entropy_max",
            "tail_decay", "ttr", "hapax_ratio"]

XGB_PARAMS = dict(n_estimators=200, max_depth=6, learning_rate=0.1,
                  random_state=SEED, eval_metric="logloss",
                  use_label_encoder=False)

ROOT = "/root/gen-depth-fingerprint"
DATA_DIR = os.path.join(ROOT, "data")
OUT_DIR = os.path.join(ROOT, "experiments", "error_analysis")


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


def run_logo_binary(df):
    # Filter depth==0, binary: y = (depth >= 2)
    df_bin = df[df["depth"] != 0].copy()
    df_bin["label"] = (df_bin["depth"] >= 2).astype(int)
    
    generators = sorted(df_bin["model_name"].unique())
    rng = np.random.RandomState(SEED)
    
    all_predictions = []
    
    for gen in generators:
        test_df = df_bin[df_bin["model_name"] == gen].copy()
        train_df = df_bin[df_bin["model_name"] != gen].copy()
        train_ds = downsample(train_df, "label", rng)
        
        clf = XGBClassifier(**XGB_PARAMS)
        clf.fit(train_ds[FEATURES].values, train_ds["label"].values)
        
        y_pred = clf.predict(test_df[FEATURES].values)
        y_proba = clf.predict_proba(test_df[FEATURES].values)[:, 1]
        
        for i, (idx, row) in enumerate(test_df.iterrows()):
            all_predictions.append({
                "generator": row["model_name"],
                "depth": int(row["depth"]),
                "true_label": int(row["label"]),
                "predicted_label": int(y_pred[i]),
                "predicted_proba": float(y_proba[i]),
                **{f: float(row[f]) for f in FEATURES}
            })
    
    return pd.DataFrame(all_predictions)


def error_analysis(pred_df):
    pred_df["correct"] = (pred_df["true_label"] == pred_df["predicted_label"]).astype(int)
    
    total = len(pred_df)
    errors = int((pred_df["correct"] == 0).sum())
    overall_error_rate = round(errors / total, 4)
    
    # By generator
    by_gen = {}
    for gen in sorted(pred_df["generator"].unique()):
        sub = pred_df[pred_df["generator"] == gen]
        n = len(sub)
        e = int((sub["correct"] == 0).sum())
        by_gen[gen] = {"total": n, "errors": e, "error_rate": round(e / n, 4)}
    
    # By depth
    by_depth = {}
    for d in sorted(pred_df["depth"].unique()):
        sub = pred_df[pred_df["depth"] == d]
        n = len(sub)
        e = int((sub["correct"] == 0).sum())
        direction = "FP (predicted gen-2+ but true gen-1)" if d == 1 else "FN (predicted gen-1 but true gen-2+)"
        by_depth[str(d)] = {"total": n, "errors": e, "error_rate": round(e / n, 4), "direction": direction}
    
    # Feature comparison: correct vs incorrect
    correct_df = pred_df[pred_df["correct"] == 1]
    incorrect_df = pred_df[pred_df["correct"] == 0]
    
    feature_comp = {}
    for f in FEATURES:
        c_vals = correct_df[f].values
        i_vals = incorrect_df[f].values
        stat, p = mannwhitneyu(c_vals, i_vals, alternative="two-sided")
        feature_comp[f] = {
            "correct_mean": round(float(c_vals.mean()), 6),
            "correct_std": round(float(c_vals.std()), 6),
            "correct_median": round(float(np.median(c_vals)), 6),
            "incorrect_mean": round(float(i_vals.mean()), 6),
            "incorrect_std": round(float(i_vals.std()), 6),
            "incorrect_median": round(float(np.median(i_vals)), 6),
            "mann_whitney_U": float(stat),
            "mann_whitney_p": float(p)
        }
    
    # Error types
    fp_df = pred_df[(pred_df["true_label"] == 0) & (pred_df["predicted_label"] == 1)]
    fn_df = pred_df[(pred_df["true_label"] == 1) & (pred_df["predicted_label"] == 0)]
    
    fp_avg_features = {f: round(float(fp_df[f].mean()), 6) for f in FEATURES} if len(fp_df) > 0 else {}
    fn_avg_features = {f: round(float(fn_df[f].mean()), 6) for f in FEATURES} if len(fn_df) > 0 else {}
    
    error_types = {
        "false_positive": {
            "count": len(fp_df),
            "pct": round(len(fp_df) / total * 100, 2),
            "avg_features": fp_avg_features,
            "top_generators": fp_df["generator"].value_counts().to_dict() if len(fp_df) > 0 else {}
        },
        "false_negative": {
            "count": len(fn_df),
            "pct": round(len(fn_df) / total * 100, 2),
            "avg_features": fn_avg_features,
            "top_generators": fn_df["generator"].value_counts().to_dict() if len(fn_df) > 0 else {},
            "by_depth": {}
        }
    }
    
    # FN breakdown by depth (gen-2+ misclassified as gen-1)
    for d in sorted(pred_df[pred_df["true_label"] == 1]["depth"].unique()):
        sub = pred_df[(pred_df["depth"] == d) & (pred_df["true_label"] == 1)]
        fn_sub = sub[sub["predicted_label"] == 0]
        error_types["false_negative"]["by_depth"][str(d)] = {
            "total": len(sub),
            "misclassified_as_gen1": len(fn_sub),
            "rate": round(len(fn_sub) / len(sub), 4) if len(sub) > 0 else 0
        }
    
    # Key findings
    findings = []
    
    # Find hardest generator
    hardest_gen = max(by_gen.items(), key=lambda x: x[1]["error_rate"])
    easiest_gen = min(by_gen.items(), key=lambda x: x[1]["error_rate"])
    findings.append(f"Hardest generator: {hardest_gen[0]} (error_rate={hardest_gen[1]['error_rate']:.4f}), easiest: {easiest_gen[0]} ({easiest_gen[1]['error_rate']:.4f})")
    
    # Depth pattern
    depth_rates = [(d, v["error_rate"]) for d, v in by_depth.items()]
    findings.append(f"Error rates by depth: {', '.join(f'd{d}={r:.4f}' for d, r in depth_rates)}")
    
    # FP vs FN balance
    findings.append(f"FP (gen-1→gen-2+): {len(fp_df)} ({len(fp_df)/errors*100:.1f}% of errors), FN (gen-2+→gen-1): {len(fn_df)} ({len(fn_df)/errors*100:.1f}% of errors)")
    
    # Most significant features
    sig_features = [(f, v["mann_whitney_p"]) for f, v in feature_comp.items() if v["mann_whitney_p"] < 0.05]
    sig_features.sort(key=lambda x: x[1])
    if sig_features:
        findings.append(f"Significantly different features (p<0.05): {', '.join(f'{f}(p={p:.2e})' for f, p in sig_features)}")
    else:
        findings.append("No features significantly different between correct/incorrect at p<0.05")
    
    # Confusion by depth for gen-2+
    fn_by_depth = error_types["false_negative"]["by_depth"]
    if fn_by_depth:
        depth_fn_str = ", ".join(f"d{d}: {v['rate']:.4f}" for d, v in fn_by_depth.items())
        findings.append(f"FN rate (gen-2+ misclassified as gen-1) by depth: {depth_fn_str}")
    
    result = {
        "total_samples": total,
        "total_misclassified": errors,
        "overall_error_rate": overall_error_rate,
        "by_generator": by_gen,
        "by_depth": by_depth,
        "feature_comparison": feature_comp,
        "text_length": "skipped (no text field in features data)",
        "error_types": error_types,
        "key_findings": findings
    }
    
    return result


def main():
    print("Loading data...")
    df = load_data()
    print(f"Loaded {len(df)} rows, {df['model_name'].nunique()} generators")
    
    print("Running 8-fold LOGO binary classification...")
    pred_df = run_logo_binary(df)
    print(f"Total predictions: {len(pred_df)}")
    
    print("Running error analysis...")
    results = error_analysis(pred_df)
    
    out_path = os.path.join(OUT_DIR, "error_analysis_results.json")
    with open(out_path, "w") as f:
        json.dump(results, f, indent=2, ensure_ascii=False)
    print(f"\nResults saved to {out_path}")
    
    print(f"\n{'='*60}")
    print(f"SUMMARY")
    print(f"{'='*60}")
    print(f"Total samples: {results['total_samples']}")
    print(f"Misclassified: {results['total_misclassified']} ({results['overall_error_rate']*100:.2f}%)")
    print(f"\nBy Generator:")
    for gen, v in results["by_generator"].items():
        print(f"  {gen:20s}  errors={v['errors']:>4d}/{v['total']:<4d}  rate={v['error_rate']:.4f}")
    print(f"\nBy Depth:")
    for d, v in results["by_depth"].items():
        print(f"  depth={d}  errors={v['errors']:>4d}/{v['total']:<4d}  rate={v['error_rate']:.4f}  ({v['direction']})")
    print(f"\nKey Findings:")
    for f in results["key_findings"]:
        print(f"  - {f}")


if __name__ == "__main__":
    main()
