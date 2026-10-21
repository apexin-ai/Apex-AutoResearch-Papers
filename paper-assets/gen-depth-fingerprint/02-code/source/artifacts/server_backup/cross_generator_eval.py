"""
cross_generator_eval.py — plan-002 跨生成器分类评估
输入: data/features_all_models.csv (23032 行, 5 生成器 × Pythia-410M 特征)
输出: data/cross_generator_results.json, data/cross_generator_report.md
分析: leave-one-out CV, family-out, feature ablation, permutation importance
"""

import json
import os
import numpy as np
import pandas as pd
from xgboost import XGBClassifier
from sklearn.metrics import f1_score, classification_report
from sklearn.inspection import permutation_importance
from sklearn.model_selection import StratifiedKFold
from scipy.stats import chi2

SEED = 42
N_BOOT = 1000
FEATURES_ALL = ["entropy_mean", "entropy_std", "entropy_min", "entropy_max",
                "tail_decay", "ttr", "hapax_ratio"]
FEATURES_SURFACE = ["ttr", "hapax_ratio"]
FEATURES_REFERENCE = ["entropy_mean", "entropy_std", "entropy_min", "entropy_max", "tail_decay"]

XGB_PARAMS = dict(n_estimators=200, max_depth=6, learning_rate=0.1,
                  random_state=SEED, eval_metric="mlogloss",
                  use_label_encoder=False)

CLASS_MAP = {0: 0, 1: 1, 2: 2, 3: 2, 4: 2}
CLASS_NAMES = ["gen-0", "gen-1", "gen-2+"]


def load_data(path):
    df = pd.read_csv(path)
    df["label"] = df["depth"].map(CLASS_MAP)
    return df


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
    scores = {"macro": [], "gen-0": [], "gen-1": [], "gen-2+": []}
    for _ in range(n_boot):
        idx = rng.randint(0, n, size=n)
        yt, yp = y_true[idx], y_pred[idx]
        if len(np.unique(yt)) < 3:
            continue
        scores["macro"].append(f1_score(yt, yp, average="macro"))
        per = f1_score(yt, yp, average=None, labels=[0, 1, 2])
        for i, name in enumerate(CLASS_NAMES):
            scores[name].append(per[i])
    result = {}
    for k, v in scores.items():
        arr = np.array(v)
        result[k] = {"mean": float(np.mean(arr)),
                      "ci_lo": float(np.percentile(arr, 2.5)),
                      "ci_hi": float(np.percentile(arr, 97.5))}
    return result


def train_eval(train_df, test_df, features, downsample_train=True):
    rng = np.random.RandomState(SEED)
    if downsample_train:
        train_df = downsample(train_df, rng)
    X_train = train_df[features].values
    y_train = train_df["label"].values
    X_test = test_df[features].values
    y_test = test_df["label"].values

    clf = XGBClassifier(**XGB_PARAMS)
    clf.fit(X_train, y_train)
    y_pred = clf.predict(X_test)

    macro_f1 = f1_score(y_test, y_pred, average="macro")
    per_class = f1_score(y_test, y_pred, average=None, labels=[0, 1, 2])
    boot = bootstrap_f1(y_test, y_pred)

    return {
        "macro_f1": float(macro_f1),
        "gen-0_f1": float(per_class[0]),
        "gen-1_f1": float(per_class[1]),
        "gen-2+_f1": float(per_class[2]),
        "bootstrap_ci": boot,
        "y_test": y_test,
        "y_pred": y_pred,
        "clf": clf,
    }


def leave_one_generator_out(df, features=FEATURES_ALL):
    generators = sorted(df["model_name"].unique())
    results = {}
    all_y_test, all_y_pred = [], []
    for gen in generators:
        test_df = df[df["model_name"] == gen]
        train_df = df[df["model_name"] != gen]
        res = train_eval(train_df, test_df, features)
        results[gen] = {
            "macro_f1": res["macro_f1"],
            "gen-0_f1": res["gen-0_f1"],
            "gen-1_f1": res["gen-1_f1"],
            "gen-2+_f1": res["gen-2+_f1"],
            "bootstrap_ci": res["bootstrap_ci"],
        }
        all_y_test.append(res["y_test"])
        all_y_pred.append(res["y_pred"])
        ci = res["bootstrap_ci"]["macro"]
        print(f"  {gen:15s}  macro-F1={res['macro_f1']:.4f}  "
              f"[{ci['ci_lo']:.4f}, {ci['ci_hi']:.4f}]  "
              f"g0={res['gen-0_f1']:.4f}  g1={res['gen-1_f1']:.4f}  g2+={res['gen-2+_f1']:.4f}")

    avg_f1 = np.mean([r["macro_f1"] for r in results.values()])
    results["average_macro_f1"] = float(avg_f1)
    print(f"  {'AVERAGE':15s}  macro-F1={avg_f1:.4f}")
    return results, np.concatenate(all_y_test), np.concatenate(all_y_pred)


def leave_one_family_out(df):
    pythia = ["pythia-2.8b", "pythia-1b"]
    non_pythia = ["olmo-2-1b", "qwen3-0.6b", "qwen3-1.7b", "qwen3-8b"]
    results = {}

    train_df = df[df["model_name"].isin(non_pythia)]
    test_df = df[df["model_name"].isin(pythia)]
    res = train_eval(train_df, test_df, FEATURES_ALL)
    results["train_nonpythia_test_pythia"] = {
        "macro_f1": res["macro_f1"],
        "gen-0_f1": res["gen-0_f1"],
        "gen-1_f1": res["gen-1_f1"],
        "gen-2+_f1": res["gen-2+_f1"],
        "bootstrap_ci": res["bootstrap_ci"],
    }
    ci = res["bootstrap_ci"]["macro"]
    print(f"  Train non-Pythia -> Test Pythia:  macro-F1={res['macro_f1']:.4f}  [{ci['ci_lo']:.4f}, {ci['ci_hi']:.4f}]")

    train_df = df[df["model_name"].isin(pythia)]
    test_df = df[df["model_name"].isin(non_pythia)]
    res = train_eval(train_df, test_df, FEATURES_ALL)
    results["train_pythia_test_nonpythia"] = {
        "macro_f1": res["macro_f1"],
        "gen-0_f1": res["gen-0_f1"],
        "gen-1_f1": res["gen-1_f1"],
        "gen-2+_f1": res["gen-2+_f1"],
        "bootstrap_ci": res["bootstrap_ci"],
    }
    ci = res["bootstrap_ci"]["macro"]
    print(f"  Train Pythia -> Test non-Pythia:  macro-F1={res['macro_f1']:.4f}  [{ci['ci_lo']:.4f}, {ci['ci_hi']:.4f}]")

    diff = results["train_nonpythia_test_pythia"]["macro_f1"] - results["train_pythia_test_nonpythia"]["macro_f1"]
    results["f1_diff_nonpythia_minus_pythia_trained"] = float(diff)
    print(f"  Delta (non-Pythia-trained - Pythia-trained) = {diff:+.4f}")
    return results


def mcnemar_test(y_true, y_pred_a, y_pred_b):
    correct_a = (y_pred_a == y_true)
    correct_b = (y_pred_b == y_true)
    b_count = int(np.sum(correct_a & ~correct_b))
    c_count = int(np.sum(~correct_a & correct_b))
    if b_count + c_count == 0:
        return 1.0
    stat = (abs(b_count - c_count) - 1) ** 2 / (b_count + c_count)
    p_value = 1.0 - chi2.cdf(stat, df=1)
    return float(p_value)


def feature_ablation(df):
    feature_sets = {
        "full": FEATURES_ALL,
        "surface_only": FEATURES_SURFACE,
        "reference_only": FEATURES_REFERENCE,
    }
    results = {}
    pooled_preds = {}

    for name, feats in feature_sets.items():
        print(f"  Feature set: {name} ({len(feats)} features)")
        res, yt, yp = leave_one_generator_out(df, feats)
        results[name] = {"average_macro_f1": res["average_macro_f1"],
                         "per_generator": {k: v for k, v in res.items() if k != "average_macro_f1"}}
        pooled_preds[name] = (yt, yp)

    yt_full, yp_full = pooled_preds["full"]
    yt_surf, yp_surf = pooled_preds["surface_only"]
    yt_ref, yp_ref = pooled_preds["reference_only"]

    p_full_vs_surface = mcnemar_test(yt_full, yp_full, yp_surf)
    p_full_vs_reference = mcnemar_test(yt_full, yp_full, yp_ref)

    results["mcnemar_full_vs_surface"] = p_full_vs_surface
    results["mcnemar_full_vs_reference"] = p_full_vs_reference
    print(f"\n  McNemar p-values:  full vs surface = {p_full_vs_surface:.6f}  |  full vs reference = {p_full_vs_reference:.6f}")
    return results


def permutation_importance_analysis(df):
    X = df[FEATURES_ALL].values
    y = df["label"].values

    skf = StratifiedKFold(n_splits=5, shuffle=True, random_state=SEED)
    importances_all = []

    for fold, (train_idx, test_idx) in enumerate(skf.split(X, y)):
        train_df_fold = df.iloc[train_idx]
        train_ds = downsample(train_df_fold, np.random.RandomState(SEED + fold))
        X_train = train_ds[FEATURES_ALL].values
        y_train = train_ds["label"].values
        X_test = X[test_idx]
        y_test = y[test_idx]

        clf = XGBClassifier(**XGB_PARAMS)
        clf.fit(X_train, y_train)
        perm = permutation_importance(clf, X_test, y_test, n_repeats=10,
                                      random_state=SEED, scoring="f1_macro")
        importances_all.append(perm.importances_mean)

    avg_imp = np.mean(importances_all, axis=0)
    ranking = np.argsort(-avg_imp)
    results = {}
    print("  Rank  Feature            Importance")
    for rank, idx in enumerate(ranking):
        feat = FEATURES_ALL[idx]
        imp = float(avg_imp[idx])
        results[feat] = {"rank": rank + 1, "importance": imp}
        print(f"  {rank+1:4d}  {feat:18s}  {imp:.4f}")
    return results


def entropy_std_analysis(df):
    results = {}

    drift = {}
    for feat in ["entropy_std", "entropy_mean"]:
        per_model = []
        for model in df["model_name"].unique():
            m = df[df["model_name"] == model]
            d0_mean = m[m["depth"] == 0][feat].mean()
            d4_mean = m[m["depth"] == 4][feat].mean()
            per_model.append(d0_mean - d4_mean)
        drift[feat] = {"mean_drift": float(np.mean(per_model)),
                       "per_model_drifts": [float(x) for x in per_model]}
    results["drift_magnitude"] = drift
    print(f"  entropy_std drift (d0-d4 avg): {drift['entropy_std']['mean_drift']:.4f}")
    print(f"  entropy_mean drift (d0-d4 avg): {drift['entropy_mean']['mean_drift']:.4f}")

    feats_no_std = [f for f in FEATURES_ALL if f != "entropy_std"]
    print("  Leave-one-generator-out WITHOUT entropy_std:")
    res_no_std, _, _ = leave_one_generator_out(df, feats_no_std)

    print("  Leave-one-generator-out WITH all features:")
    res_full, _, _ = leave_one_generator_out(df, FEATURES_ALL)

    delta = res_full["average_macro_f1"] - res_no_std["average_macro_f1"]
    results["logo_with_all"] = res_full["average_macro_f1"]
    results["logo_without_entropy_std"] = res_no_std["average_macro_f1"]
    results["delta_f1"] = float(delta)
    print(f"  Delta macro-F1 (with - without entropy_std): {delta:+.4f}")

    if abs(delta) < 0.01:
        conclusion = "entropy_std 对跨生成器泛化贡献极小，更可能是 H1（模型特有 artifact）"
    else:
        conclusion = "entropy_std 对跨生成器泛化有显著贡献，支持 H2（通用深度信号）"
    results["conclusion"] = conclusion
    print(f"  结论: {conclusion}")
    return results


def fmt_ci(boot, key):
    d = boot[key]
    return f"{d['mean']:.4f} [{d['ci_lo']:.4f}, {d['ci_hi']:.4f}]"


def generate_report(all_results):
    lines = ["# 跨生成器分类评估报告 (plan-002)\n"]

    lines.append("## 1. Leave-One-Generator-Out CV\n")
    lines.append("| Generator | Macro-F1 | 95% CI | gen-0 F1 | gen-1 F1 | gen-2+ F1 |")
    lines.append("|-----------|----------|--------|----------|----------|-----------|")
    logo = all_results["leave_one_generator_out"]
    for gen in sorted(k for k in logo if k != "average_macro_f1"):
        r = logo[gen]
        ci = r["bootstrap_ci"]["macro"]
        lines.append(f"| {gen} | {r['macro_f1']:.4f} | [{ci['ci_lo']:.4f}, {ci['ci_hi']:.4f}] | "
                      f"{r['gen-0_f1']:.4f} | {r['gen-1_f1']:.4f} | {r['gen-2+_f1']:.4f} |")
    lines.append(f"| **Average** | **{logo['average_macro_f1']:.4f}** | | | | |")
    lines.append("")

    lines.append("## 2. Leave-One-Family-Out\n")
    fam = all_results["leave_one_family_out"]
    lines.append("| Setting | Macro-F1 | 95% CI |")
    lines.append("|---------|----------|--------|")
    for key, label in [("train_nonpythia_test_pythia", "Train non-Pythia → Test Pythia"),
                       ("train_pythia_test_nonpythia", "Train Pythia → Test non-Pythia")]:
        r = fam[key]
        ci = r["bootstrap_ci"]["macro"]
        lines.append(f"| {label} | {r['macro_f1']:.4f} | [{ci['ci_lo']:.4f}, {ci['ci_hi']:.4f}] |")
    lines.append(f"\nΔ (non-Pythia-trained − Pythia-trained) = {fam['f1_diff_nonpythia_minus_pythia_trained']:+.4f}\n")

    lines.append("## 3. Feature Ablation\n")
    abl = all_results["feature_ablation"]
    lines.append("| Feature Set | Avg Macro-F1 |")
    lines.append("|-------------|-------------|")
    for name in ["full", "surface_only", "reference_only"]:
        lines.append(f"| {name} | {abl[name]['average_macro_f1']:.4f} |")
    lines.append(f"\nMcNemar p-values: full vs surface = {abl['mcnemar_full_vs_surface']:.6f}, "
                 f"full vs reference = {abl['mcnemar_full_vs_reference']:.6f}\n")

    lines.append("## 4. Permutation Importance\n")
    perm = all_results["permutation_importance"]
    lines.append("| Rank | Feature | Importance |")
    lines.append("|------|---------|------------|")
    for feat, info in sorted(perm.items(), key=lambda x: x[1]["rank"]):
        lines.append(f"| {info['rank']} | {feat} | {info['importance']:.4f} |")
    lines.append("")

    lines.append("## 5. entropy_std 专项分析\n")
    es = all_results["entropy_std_analysis"]
    lines.append(f"- entropy_std drift (d0−d4 avg): {es['drift_magnitude']['entropy_std']['mean_drift']:.4f}")
    lines.append(f"- entropy_mean drift (d0−d4 avg): {es['drift_magnitude']['entropy_mean']['mean_drift']:.4f}")
    lines.append(f"- LOGO macro-F1 with all features: {es['logo_with_all']:.4f}")
    lines.append(f"- LOGO macro-F1 without entropy_std: {es['logo_without_entropy_std']:.4f}")
    lines.append(f"- Δ macro-F1: {es['delta_f1']:+.4f}")
    lines.append(f"- **结论**: {es['conclusion']}")
    lines.append("")

    return "\n".join(lines)


def main():
    data_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data")
    csv_path = os.path.join(data_dir, "features_all_models.csv")
    df = load_data(csv_path)
    print(f"Loaded {len(df)} rows, {df['model_name'].nunique()} generators")
    print(f"Class distribution: {df['label'].value_counts().sort_index().to_dict()}\n")

    all_results = {}

    print("=" * 60)
    print("1. Leave-One-Generator-Out CV")
    print("=" * 60)
    logo_res, _, _ = leave_one_generator_out(df)
    all_results["leave_one_generator_out"] = logo_res

    print("\n" + "=" * 60)
    print("2. Leave-One-Family-Out")
    print("=" * 60)
    all_results["leave_one_family_out"] = leave_one_family_out(df)

    print("\n" + "=" * 60)
    print("3. Feature Ablation (cross-generator)")
    print("=" * 60)
    all_results["feature_ablation"] = feature_ablation(df)

    print("\n" + "=" * 60)
    print("4. Permutation Importance")
    print("=" * 60)
    all_results["permutation_importance"] = permutation_importance_analysis(df)

    print("\n" + "=" * 60)
    print("5. entropy_std 专项分析")
    print("=" * 60)
    all_results["entropy_std_analysis"] = entropy_std_analysis(df)

    json_path = os.path.join(data_dir, "cross_generator_results.json")
    with open(json_path, "w") as f:
        json.dump(all_results, f, indent=2, ensure_ascii=False)
    print(f"\nSaved: {json_path}")

    report = generate_report(all_results)
    report_path = os.path.join(data_dir, "cross_generator_report.md")
    with open(report_path, "w") as f:
        f.write(report)
    print(f"Saved: {report_path}")


if __name__ == "__main__":
    main()
