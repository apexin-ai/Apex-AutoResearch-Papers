import json
import os
import numpy as np
import pandas as pd
from xgboost import XGBClassifier
from sklearn.model_selection import StratifiedKFold
from sklearn.metrics import f1_score

DATA_PATH = "/root/gen-depth-fingerprint/data/features_8gen.csv"
OUT_DIR = "/root/gen-depth-fingerprint/results"

FEATURES = ["hapax_ratio", "ttr", "entropy_mean", "entropy_std", "entropy_min", "entropy_max", "tail_decay"]
CLASS_MAP = {0: 0, 1: 1, 2: 2, 3: 2, 4: 2, 5: 2}

XGB_PARAMS = dict(n_estimators=200, max_depth=6, learning_rate=0.1,
                  random_state=42, eval_metric="mlogloss", verbosity=0)


def stratified_cv_f1(df, features, n_splits=10, seed=42):
    X = df[features].values
    y = df["label"].values
    skf = StratifiedKFold(n_splits=n_splits, shuffle=True, random_state=seed)
    fold_scores = []
    for train_idx, test_idx in skf.split(X, y):
        clf = XGBClassifier(**XGB_PARAMS)
        clf.fit(X[train_idx], y[train_idx])
        y_pred = clf.predict(X[test_idx])
        fold_scores.append(f1_score(y[test_idx], y_pred, average="macro"))
    return float(np.mean(fold_scores)), float(np.std(fold_scores)), fold_scores


def main():
    df = pd.read_csv(DATA_PATH)
    df["label"] = df["depth"].map(CLASS_MAP)
    print(f"Loaded {len(df)} rows, {df['model_name'].nunique()} generators")
    print(f"Generators: {sorted(df['model_name'].unique())}")
    print(f"Label distribution:\n{df['label'].value_counts().sort_index()}\n")

    # Full baseline
    full_mean, full_std, full_folds = stratified_cv_f1(df, FEATURES)
    print(f"Full 7-feature baseline: F1={full_mean:.4f} ± {full_std:.4f}\n")

    results = []
    for drop_feat in FEATURES:
        remaining = [f for f in FEATURES if f != drop_feat]
        mean_f1, std_f1, folds = stratified_cv_f1(df, remaining)
        delta = mean_f1 - full_mean
        results.append({
            "dropped": drop_feat,
            "lofo_f1_mean": round(mean_f1, 4),
            "lofo_f1_std": round(std_f1, 4),
            "delta": round(delta, 4),
            "fold_scores": [round(f, 4) for f in folds],
        })
        print(f"Drop {drop_feat:15s} → F1={mean_f1:.4f} ± {std_f1:.4f}  Δ={delta:+.4f}")

    # Sort by delta (most important first = largest negative delta)
    results.sort(key=lambda x: x["delta"])

    output = {
        "dataset": "8gen",
        "n_samples": len(df),
        "n_generators": int(df["model_name"].nunique()),
        "generators": sorted(df["model_name"].unique().tolist()),
        "n_folds": 10,
        "full_baseline_f1": round(full_mean, 4),
        "full_baseline_std": round(full_std, 4),
        "full_fold_scores": [round(f, 4) for f in full_folds],
        "lofo_results": results,
    }

    os.makedirs(OUT_DIR, exist_ok=True)
    out_path = os.path.join(OUT_DIR, "8gen_lofo_results.json")
    with open(out_path, "w") as f:
        json.dump(output, f, indent=2)
    print(f"\nSaved to {out_path}")

    print("\n| Dropped Feature | LOFO F1 | Δ vs Full |")
    print("|---|---|---|")
    for r in results:
        print(f"| {r['dropped']} | {r['lofo_f1_mean']:.4f} ± {r['lofo_f1_std']:.4f} | {r['delta']:+.4f} |")

if __name__ == "__main__":
    main()
