"""Merged feature ablation: 19 stat features + 11 Binoculars features on 14B temp09."""

import json
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import StratifiedKFold
from sklearn.metrics import accuracy_score, balanced_accuracy_score

SEED = 42
N_FOLDS = 5
N_ESTIMATORS = 200

STAT_FEATURES = [
    "mean_ppl", "var_ppl", "median_ppl", "p75_ppl", "p90_ppl",
    "skew_ppl", "kurt_ppl",
    "mean_surprisal", "var_surprisal", "median_surprisal",
    "p75_surprisal", "p90_surprisal",
    "type_token_ratio", "hapax_ratio",
    "bigram_entropy", "trigram_entropy",
    "rep_2gram", "rep_3gram", "rep_4gram",
]

BINO_FEATURES = [
    "bino_score",
    "ppl_mean", "ppl_var", "ppl_median", "ppl_p10", "ppl_p90", "ppl_skew",
    "xppl_mean", "xppl_var", "xppl_median",
    "bino_score_median",
]

STAT_PATH = "data/qwen25_14b_temp09/features_self_ref.jsonl"
BINO_NPZ_PATH = "results/pythia_nucleus_bino_features.npz"
OUTPUT_PATH = "results/merged_ablation_14b_temp09.json"


def load_stat_features(path):
    records = []
    with open(path) as f:
        for line in f:
            if line.strip():
                records.append(json.loads(line))
    X = np.array([[r[k] for k in STAT_FEATURES] for r in records], dtype=np.float64)
    y = np.array([r["depth"] for r in records], dtype=np.int64)
    X = np.nan_to_num(X, nan=0.0, posinf=0.0, neginf=0.0)
    return X, y


def load_bino_features(path):
    data = np.load(path)
    X = np.column_stack([data[k] for k in BINO_FEATURES])
    y = data["labels"]
    X = np.nan_to_num(X, nan=0.0, posinf=0.0, neginf=0.0)
    return X, y


def cv_accuracy(X, y, label=""):
    skf = StratifiedKFold(n_splits=N_FOLDS, shuffle=True, random_state=SEED)
    acc4_list, bal_list = [], []
    for train_idx, test_idx in skf.split(X, y):
        rf = RandomForestClassifier(n_estimators=N_ESTIMATORS, random_state=SEED, n_jobs=4)
        rf.fit(X[train_idx], y[train_idx])
        preds = rf.predict(X[test_idx])
        acc4_list.append(accuracy_score(y[test_idx], preds))
        mask = y[test_idx] >= 1
        if mask.sum() > 0:
            bal_list.append(balanced_accuracy_score(y[test_idx][mask], preds[mask]))
        else:
            bal_list.append(0.0)
    result = {
        "4class_acc": round(float(np.mean(acc4_list)), 4),
        "4class_acc_std": round(float(np.std(acc4_list)), 4),
        "d1d3_bal_acc": round(float(np.mean(bal_list)), 4),
        "d1d3_bal_acc_std": round(float(np.std(bal_list)), 4),
    }
    print(f"  {label:30s}: acc={result['4class_acc']:.4f}±{result['4class_acc_std']:.4f}  "
          f"d1d3_bal={result['d1d3_bal_acc']:.4f}±{result['d1d3_bal_acc_std']:.4f}")
    return result


def main():
    print("Loading stat features...")
    X_stat, y_stat = load_stat_features(STAT_PATH)
    print(f"  Stat: {X_stat.shape[0]} samples x {X_stat.shape[1]} features")

    print("Loading Binoculars features...")
    X_bino, y_bino = load_bino_features(BINO_NPZ_PATH)
    print(f"  Bino: {X_bino.shape[0]} samples x {X_bino.shape[1]} features")

    assert np.array_equal(y_stat, y_bino), "Label mismatch between stat and bino features!"
    y = y_stat

    X_merged = np.hstack([X_stat, X_bino])
    print(f"  Merged: {X_merged.shape[0]} samples x {X_merged.shape[1]} features")

    results = {}
    print("\n=== Ablation Results ===")

    print("\n-- Stat features only (19) --")
    results["stat_only_19"] = cv_accuracy(X_stat, y, "stat_only (19 feat)")

    print("\n-- Bino features only (11) --")
    results["bino_only_11"] = cv_accuracy(X_bino, y, "bino_only (11 feat)")

    print("\n-- Merged (30 feat) --")
    results["merged_30"] = cv_accuracy(X_merged, y, "merged (30 feat)")

    print("\n-- Bino single feature (bino_score) --")
    bino_data = np.load(BINO_NPZ_PATH)
    X_bino_single = bino_data["bino_score"].reshape(-1, 1)
    results["bino_single"] = cv_accuracy(X_bino_single, y, "bino_score_single (1 feat)")

    results["__meta__"] = {
        "stat_features": STAT_FEATURES,
        "bino_features": BINO_FEATURES,
        "n_folds": N_FOLDS,
        "rf_n_estimators": N_ESTIMATORS,
        "stat_path": STAT_PATH,
        "bino_npz_path": BINO_NPZ_PATH,
    }

    with open(OUTPUT_PATH, "w") as f:
        json.dump(results, f, indent=2)
    print(f"\nResults saved to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
