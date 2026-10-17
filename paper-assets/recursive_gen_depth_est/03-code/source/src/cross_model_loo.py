# Cross-model Leave-One-Out generalization test for plan_005 Claim 1.
# Train RF on 2 model families (all 3 strategies), test on held-out 3rd family.

import json
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, roc_auc_score, recall_score
from pathlib import Path
import time

BASE = Path("/root/autodl-tmp/recursive_gen_depth_est")

CELL_PATHS = {
    "pythia_nucleus095": BASE / "data" / "features_all.jsonl",
    "pythia_temp09":     BASE / "data" / "pythia_temp09" / "features.jsonl",
    "pythia_topk50":     BASE / "results" / "pythia_topk50" / "features.jsonl",
    "gpt2xl_nucleus095": BASE / "data" / "gpt2xl" / "features.jsonl",
    "gpt2xl_temp09":     BASE / "results" / "gpt2xl_temp09" / "features.jsonl",
    "gpt2xl_topk50":     BASE / "results" / "gpt2xl_topk50" / "features.jsonl",
    "olmo_nucleus095":   BASE / "data" / "olmo" / "features.jsonl",
    "olmo_temp09":       BASE / "results" / "olmo_temp09" / "features.jsonl",
    "olmo_topk50":       BASE / "results" / "olmo_topk50" / "features.jsonl",
}

FEATURE_COLS = [
    "mean_ppl", "var_ppl", "skewness_ppl", "kurtosis_ppl",
    "p10_ppl", "p25_ppl", "p50_ppl", "p75_ppl", "p90_ppl",
    "mean_surprisal", "var_surprisal", "entropy_of_surprisal",
    "type_token_ratio", "hapax_ratio",
    "bigram_entropy", "trigram_entropy",
    "rep_2gram", "rep_3gram", "rep_4gram",
]

MODEL_FAMILIES = {
    "Pythia": ["pythia_nucleus095", "pythia_temp09", "pythia_topk50"],
    "OLMo":  ["olmo_nucleus095", "olmo_temp09", "olmo_topk50"],
    "GPT-2 XL": ["gpt2xl_nucleus095", "gpt2xl_temp09", "gpt2xl_topk50"],
}


def load_features(path):
    X, y = [], []
    with open(path) as f:
        for line in f:
            rec = json.loads(line)
            X.append([rec[c] for c in FEATURE_COLS])
            y.append(rec["depth"])
    return np.array(X), np.array(y)


def bootstrap_ci(y_true, y_pred, n_boot=1000, seed=42):
    rng = np.random.RandomState(seed)
    n = len(y_true)
    accs = []
    for _ in range(n_boot):
        idx = rng.randint(0, n, n)
        accs.append(accuracy_score(y_true[idx], y_pred[idx]))
    lo, hi = np.percentile(accs, [2.5, 97.5])
    return float(lo), float(hi)


def pairwise_auc(clf, X, y, class_a, class_b):
    mask = np.isin(y, [class_a, class_b])
    if mask.sum() == 0:
        return float("nan")
    X_sub, y_sub = X[mask], y[mask]
    y_bin = (y_sub == class_b).astype(int)
    proba = clf.predict_proba(X_sub)
    classes = list(clf.classes_)
    if class_b not in classes:
        return float("nan")
    scores = proba[:, classes.index(class_b)]
    return roc_auc_score(y_bin, scores)


def main():
    print("Loading all 9-cell features...")
    data = {}
    for cell, path in CELL_PATHS.items():
        X, y = load_features(path)
        data[cell] = (X, y)
        print(f"  {cell}: {X.shape[0]} samples")

    families = list(MODEL_FAMILIES.keys())
    results = []

    for holdout_family in families:
        holdout_cells = MODEL_FAMILIES[holdout_family]
        train_cells = []
        for fam, cells in MODEL_FAMILIES.items():
            if fam != holdout_family:
                train_cells.extend(cells)

        X_train = np.vstack([data[c][0] for c in train_cells])
        y_train = np.concatenate([data[c][1] for c in train_cells])
        X_test = np.vstack([data[c][0] for c in holdout_cells])
        y_test = np.concatenate([data[c][1] for c in holdout_cells])

        clf = RandomForestClassifier(n_estimators=200, random_state=42, n_jobs=-1)
        t0 = time.time()
        clf.fit(X_train, y_train)
        train_time = time.time() - t0

        y_pred = clf.predict(X_test)
        acc = accuracy_score(y_test, y_pred)
        ci_lo, ci_hi = bootstrap_ci(y_test, y_pred, n_boot=1000)

        d1v2_auc = pairwise_auc(clf, X_test, y_test, 1, 2)
        d2v3_auc = pairwise_auc(clf, X_test, y_test, 2, 3)

        per_class_recall = {}
        for depth in sorted(np.unique(y_test)):
            mask = y_test == depth
            per_class_recall[f"depth_{depth}"] = round(
                recall_score(y_test[mask], y_pred[mask], average="micro"), 4
            )

        row = {
            "rotation": f"Hold-out {holdout_family}",
            "holdout_family": holdout_family,
            "train_families": [f for f in families if f != holdout_family],
            "train_cells": train_cells,
            "test_cells": holdout_cells,
            "train_size": int(len(y_train)),
            "test_size": int(len(y_test)),
            "accuracy_4class": round(acc, 4),
            "accuracy_ci95_bootstrap": [round(ci_lo, 4), round(ci_hi, 4)],
            "d1v2_auc": round(d1v2_auc, 4),
            "d2v3_auc": round(d2v3_auc, 4),
            "per_class_recall": per_class_recall,
            "train_time_s": round(train_time, 1),
        }
        results.append(row)
        recall_str = " ".join(f"d{k.split('_')[1]}={v:.4f}" for k, v in per_class_recall.items())
        print(f"  {row['rotation']}: acc={acc:.4f} [{ci_lo:.4f},{ci_hi:.4f}] "
              f"d1v2={d1v2_auc:.4f} d2v3={d2v3_auc:.4f} | {recall_str} ({train_time:.1f}s)")

    out_path = BASE / "results" / "cross_model_loo.json"
    out_path.parent.mkdir(parents=True, exist_ok=True)
    with open(out_path, "w") as f:
        json.dump(results, f, indent=2)
    print(f"\nResults saved to {out_path}")

    print("\n| Rotation | Train size | Test size | 4-class acc | 95% CI | d1v2 AUC | d2v3 AUC |")
    print("|----------|-----------|-----------|-------------|--------|----------|----------|")
    for r in results:
        ci = f"[{r['accuracy_ci95_bootstrap'][0]:.4f}, {r['accuracy_ci95_bootstrap'][1]:.4f}]"
        print(f"| {r['rotation']} | {r['train_size']} | {r['test_size']} | "
              f"{r['accuracy_4class']:.4f} | {ci} | {r['d1v2_auc']:.4f} | {r['d2v3_auc']:.4f} |")


if __name__ == "__main__":
    main()
