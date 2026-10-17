"""W6 cross-strategy LOO per-class recall/precision/F1.

For each model, hold out 1 strategy, train RF on 2, test on holdout.
3 models × 3 holdout strategies = 9 rotations.
"""

import json
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (
    accuracy_score, precision_recall_fscore_support, confusion_matrix
)
from pathlib import Path

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

MODELS = {
    "pythia":  ["pythia_nucleus095", "pythia_temp09", "pythia_topk50"],
    "gpt2xl":  ["gpt2xl_nucleus095", "gpt2xl_temp09", "gpt2xl_topk50"],
    "olmo":    ["olmo_nucleus095", "olmo_temp09", "olmo_topk50"],
}

STRATEGIES = ["nucleus095", "temp09", "topk50"]
STRATEGY_LABEL = {"nucleus095": "nucleus", "temp09": "temp09", "topk50": "topk50"}


F32_MAX = np.finfo(np.float32).max


def load_features(path):
    X, y = [], []
    with open(path) as f:
        for line in f:
            rec = json.loads(line)
            X.append([rec[c] for c in FEATURE_COLS])
            y.append(rec["depth"])
    X = np.array(X, dtype=np.float64)
    y = np.array(y)
    bad = np.isinf(X) | np.isnan(X) | (np.abs(X) > F32_MAX)
    if bad.sum() > 0:
        X[bad] = np.nan
        for col in range(X.shape[1]):
            mask = np.isnan(X[:, col])
            if mask.any():
                finite = X[~mask, col]
                X[mask, col] = np.median(finite) if len(finite) > 0 else 0.0
    X = np.clip(X, -F32_MAX, F32_MAX)
    return X, y


def main():
    print("Loading all 9-cell features...")
    data = {}
    for cell, path in CELL_PATHS.items():
        X, y = load_features(path)
        data[cell] = (X, y)
        print(f"  {cell}: {X.shape[0]} samples")

    results = {}
    depth_labels = [0, 1, 2, 3]

    for model, cells in MODELS.items():
        for holdout_strat in STRATEGIES:
            holdout_cell = f"{model}_{holdout_strat}"
            train_cells = [c for c in cells if c != holdout_cell]

            X_train = np.vstack([data[c][0] for c in train_cells])
            y_train = np.concatenate([data[c][1] for c in train_cells])
            X_test, y_test = data[holdout_cell]

            clf = RandomForestClassifier(n_estimators=200, random_state=42, n_jobs=-1)
            clf.fit(X_train, y_train)
            y_pred = clf.predict(X_test)

            acc = accuracy_score(y_test, y_pred)
            P, R, F1, sup = precision_recall_fscore_support(
                y_test, y_pred, labels=depth_labels, zero_division=0
            )
            cm = confusion_matrix(y_test, y_pred, labels=depth_labels)

            key = f"{model}_holdout_{STRATEGY_LABEL[holdout_strat]}"
            per_class = {}
            for i, d in enumerate(depth_labels):
                per_class[f"d{d}"] = {
                    "P": round(float(P[i]), 4),
                    "R": round(float(R[i]), 4),
                    "F1": round(float(F1[i]), 4),
                    "support": int(sup[i]),
                }

            results[key] = {
                "acc": round(float(acc), 4),
                "per_class": per_class,
                "confusion_matrix": cm.tolist(),
            }

            recall_str = " ".join(f"d{d}={R[i]:.4f}" for i, d in enumerate(depth_labels))
            print(f"  {key}: acc={acc:.4f} | recall: {recall_str}")

    out_path = BASE / "results" / "w6_cross_strategy_per_class_recall.json"
    out_path.parent.mkdir(parents=True, exist_ok=True)
    with open(out_path, "w") as f:
        json.dump(results, f, indent=2)
    print(f"\nSaved to {out_path}")

    # Print table
    print("\n| Rotation | Acc | d0-R | d1-R | d2-R | d3-R | d0-P | d1-P | d2-P | d3-P | d0-F1 | d1-F1 | d2-F1 | d3-F1 |")
    print("|" + "---|" * 14)
    for key, v in results.items():
        pc = v["per_class"]
        print(f"| {key} | {v['acc']:.4f} "
              f"| {pc['d0']['R']:.4f} | {pc['d1']['R']:.4f} | {pc['d2']['R']:.4f} | {pc['d3']['R']:.4f} "
              f"| {pc['d0']['P']:.4f} | {pc['d1']['P']:.4f} | {pc['d2']['P']:.4f} | {pc['d3']['P']:.4f} "
              f"| {pc['d0']['F1']:.4f} | {pc['d1']['F1']:.4f} | {pc['d2']['F1']:.4f} | {pc['d3']['F1']:.4f} |")


if __name__ == "__main__":
    main()
