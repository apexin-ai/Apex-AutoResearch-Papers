# R3-W5: XGBoost + LightGBM baselines on Pythia nucleus095 19-dim features.
# Input: data/features_all.jsonl (20000 samples, 4 classes d0-d3)
# Output: results/r3w5_baselines/results.json
# Deps: xgboost, lightgbm, sklearn, numpy

import json
import os
import numpy as np
from sklearn.model_selection import StratifiedKFold
from sklearn.metrics import roc_auc_score, recall_score
from sklearn.preprocessing import label_binarize

FEATURE_NAMES = [
    "mean_ppl", "var_ppl", "skewness_ppl", "kurtosis_ppl",
    "p10_ppl", "p25_ppl", "p50_ppl", "p75_ppl", "p90_ppl",
    "mean_surprisal", "var_surprisal", "entropy_of_surprisal",
    "type_token_ratio", "hapax_ratio", "bigram_entropy", "trigram_entropy",
    "rep_2gram", "rep_3gram", "rep_4gram",
]

ROOT = "/root/autodl-tmp/recursive_gen_depth_est"
DATA_PATH = os.path.join(ROOT, "data/features_all.jsonl")
OUT_DIR = os.path.join(ROOT, "results/r3w5_baselines")


def load_features(path):
    records = []
    with open(path) as f:
        for line in f:
            if line.strip():
                records.append(json.loads(line))
    X = np.array([[r[k] for k in FEATURE_NAMES] for r in records], dtype=np.float64)
    y = np.array([r["depth"] for r in records], dtype=np.int64)
    X = np.nan_to_num(X, nan=0.0, posinf=0.0, neginf=0.0)
    return X, y


def pairwise_auc(y_true, y_prob, class_a, class_b):
    """OvO AUC between two specific classes."""
    mask = np.isin(y_true, [class_a, class_b])
    if mask.sum() < 10:
        return float("nan")
    yt = (y_true[mask] == class_b).astype(int)
    yp = y_prob[mask, class_b] / (y_prob[mask, class_a] + y_prob[mask, class_b] + 1e-15)
    return float(roc_auc_score(yt, yp))


def run_cv(clf_factory, X, y, method_name):
    skf = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
    accs, d0v1_aucs, d1v2_aucs, d2v3_aucs = [], [], [], []
    all_recalls = []

    for fold, (train_idx, test_idx) in enumerate(skf.split(X, y)):
        X_tr, X_te = X[train_idx], X[test_idx]
        y_tr, y_te = y[train_idx], y[test_idx]

        clf = clf_factory()
        clf.fit(X_tr, y_tr)

        y_pred = clf.predict(X_te)
        y_prob = clf.predict_proba(X_te)

        acc = float(np.mean(y_pred == y_te))
        accs.append(acc)

        d0v1_aucs.append(pairwise_auc(y_te, y_prob, 0, 1))
        d1v2_aucs.append(pairwise_auc(y_te, y_prob, 1, 2))
        d2v3_aucs.append(pairwise_auc(y_te, y_prob, 2, 3))

        recalls = recall_score(y_te, y_pred, labels=[0, 1, 2, 3], average=None)
        all_recalls.append(recalls)

        print(f"  Fold {fold}: acc={acc:.4f}")

    mean_recalls = np.mean(all_recalls, axis=0)
    result = {
        "method": method_name,
        "acc_mean": float(np.mean(accs)),
        "acc_std": float(np.std(accs)),
        "acc_folds": accs,
        "d0v1_auc": float(np.nanmean(d0v1_aucs)),
        "d1v2_auc": float(np.nanmean(d1v2_aucs)),
        "d2v3_auc": float(np.nanmean(d2v3_aucs)),
        "per_class_recall": {f"d{i}": float(mean_recalls[i]) for i in range(4)},
    }
    return result


def main():
    print(f"Loading data from {DATA_PATH}")
    X, y = load_features(DATA_PATH)
    print(f"  {X.shape[0]} samples, {X.shape[1]} features, classes: {np.bincount(y).tolist()}")

    results = {}

    # --- XGBoost ---
    print("\n=== XGBoost (GPU) ===")
    try:
        import xgboost as xgb
        # XGBoost 2.0+ uses device param instead of tree_method='gpu_hist'
        def xgb_factory():
            return xgb.XGBClassifier(
                n_estimators=200, max_depth=6, learning_rate=0.1,
                tree_method="hist", device="cuda:0",
                objective="multi:softprob", num_class=4,
                eval_metric="mlogloss", random_state=42,
                verbosity=0,
            )
        results["xgboost"] = run_cv(xgb_factory, X, y, "XGBoost (GPU)")
        print(f"  => Acc: {results['xgboost']['acc_mean']:.4f} ± {results['xgboost']['acc_std']:.4f}")
    except Exception as e:
        print(f"  XGBoost GPU failed: {e}")
        print("  Falling back to CPU...")
        import xgboost as xgb
        def xgb_cpu_factory():
            return xgb.XGBClassifier(
                n_estimators=200, max_depth=6, learning_rate=0.1,
                tree_method="hist", device="cpu",
                objective="multi:softprob", num_class=4,
                eval_metric="mlogloss", random_state=42,
                verbosity=0,
            )
        results["xgboost"] = run_cv(xgb_cpu_factory, X, y, "XGBoost (CPU)")
        print(f"  => Acc: {results['xgboost']['acc_mean']:.4f} ± {results['xgboost']['acc_std']:.4f}")

    # --- LightGBM ---
    print("\n=== LightGBM ===")
    try:
        import lightgbm as lgb
        # Try GPU first
        def lgbm_gpu_factory():
            return lgb.LGBMClassifier(
                n_estimators=200, max_depth=6, learning_rate=0.1,
                device="gpu", gpu_device_id=0,
                objective="multiclass", num_class=4,
                random_state=42, verbose=-1,
            )
        # Quick GPU test
        test_clf = lgbm_gpu_factory()
        test_clf.fit(X[:100], y[:100])
        print("  LightGBM GPU available")
        results["lightgbm"] = run_cv(lgbm_gpu_factory, X, y, "LightGBM (GPU)")
        print(f"  => Acc: {results['lightgbm']['acc_mean']:.4f} ± {results['lightgbm']['acc_std']:.4f}")
    except Exception as e:
        print(f"  LightGBM GPU failed ({e}), falling back to CPU...")
        import lightgbm as lgb
        def lgbm_cpu_factory():
            return lgb.LGBMClassifier(
                n_estimators=200, max_depth=6, learning_rate=0.1,
                device="cpu",
                objective="multiclass", num_class=4,
                random_state=42, verbose=-1,
            )
        results["lightgbm"] = run_cv(lgbm_cpu_factory, X, y, "LightGBM (CPU)")
        print(f"  => Acc: {results['lightgbm']['acc_mean']:.4f} ± {results['lightgbm']['acc_std']:.4f}")

    # --- Comparison table ---
    print("\n" + "=" * 70)
    print(f"  {'Method':<22s} {'4-cls Acc':>12s} {'d0v1 AUC':>10s} {'d1v2 AUC':>10s} {'d2v3 AUC':>10s}")
    print(f"  {'-'*22} {'-'*12} {'-'*10} {'-'*10} {'-'*10}")
    print(f"  {'RF (reference)':<22s} {'78.2% ± ?':>12s} {'0.861':>10s} {'~':>10s} {'0.800':>10s}")
    for k, r in results.items():
        acc_str = f"{r['acc_mean']*100:.1f}% ± {r['acc_std']*100:.1f}%"
        print(f"  {r['method']:<22s} {acc_str:>12s} {r['d0v1_auc']:>10.3f} {r['d1v2_auc']:>10.3f} {r['d2v3_auc']:>10.3f}")

    print("\nPer-class recall:")
    for k, r in results.items():
        rc = r["per_class_recall"]
        print(f"  {r['method']}: d0={rc['d0']:.3f} d1={rc['d1']:.3f} d2={rc['d2']:.3f} d3={rc['d3']:.3f}")

    # --- Save ---
    os.makedirs(OUT_DIR, exist_ok=True)
    out_path = os.path.join(OUT_DIR, "results.json")
    with open(out_path, "w") as f:
        json.dump(results, f, indent=2)
    print(f"\nResults saved to {out_path}")


if __name__ == "__main__":
    main()
