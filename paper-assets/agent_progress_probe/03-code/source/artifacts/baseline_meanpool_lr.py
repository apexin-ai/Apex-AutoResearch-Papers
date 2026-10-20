#!/usr/bin/env python3
"""MeanPool + Logistic Regression baseline.

Mean-pools each window's embedding sequence (seq_len, D) → (D,),
then fits sklearn LogisticRegression / MLPClassifier on the pooled vectors.
Evaluates on the same test split as the GRU probe for direct comparison.
"""

import argparse
import json
import sys
from pathlib import Path

import numpy as np
import torch
from sklearn.linear_model import LogisticRegression
from sklearn.neural_network import MLPClassifier
from sklearn.preprocessing import StandardScaler

PROBE_REF_MACRO_F1 = 0.9055


def mean_pool(embeddings: list[torch.Tensor]) -> np.ndarray:
    """Mean-pool each (seq_len, D) tensor → (D,), stack into (N, D)."""
    pooled = []
    for emb in embeddings:
        pooled.append(emb.float().mean(dim=0).numpy())
    return np.stack(pooled)


def print_table(results: list[tuple[str, dict]]):
    header = "| Method                      | Macro-F1 | Accuracy | Prec(M) | Rec(M) | F1(stag) | F1(prog) |"
    sep = "|" + "|".join(["-" * 30] + ["-" * 10] * 6) + "|"
    print(header)
    print(sep)
    for name, m in results:
        row = f"| {name:28s} |"
        for key in ["macro_f1", "accuracy", "precision_macro", "recall_macro", "f1_stagnation", "f1_progress"]:
            v = m.get(key)
            if v is None:
                row += "    —     |"
            else:
                row += f" {v:.4f}   |"
        print(row)


def main():
    parser = argparse.ArgumentParser(description="MeanPool + LR/MLP baseline")
    parser.add_argument("--data_dir", required=True, help="Dir containing data/embeddings.pt")
    parser.add_argument("--split_info", required=True, help="Path to split_info.json")
    args = parser.parse_args()

    sys.path.insert(0, str(Path(__file__).parent))
    from baselines import compute_metrics

    # Load embeddings
    data_path = Path(args.data_dir) / "data" / "embeddings.pt"
    print(f"Loading {data_path} ...")
    data = torch.load(data_path, weights_only=False)
    embeddings = data["embeddings"]
    labels = data["labels"]

    with open(args.split_info) as f:
        split_info = json.load(f)

    # Apply confidence filter (mirrors train_probe.py)
    keep_indices = split_info.get("keep_indices")
    if keep_indices is not None:
        min_conf = split_info.get("min_confidence", 0)
        print(f"Confidence filter (min_confidence={min_conf}): {len(keep_indices)}/{len(labels)} windows")
        embeddings = [embeddings[i] for i in keep_indices]
        labels = [labels[i] for i in keep_indices]

    train_idx = split_info["train_indices"]
    val_idx = split_info["val_indices"]
    test_idx = split_info["test_indices"]

    print(f"Split — train: {len(train_idx)}, val: {len(val_idx)}, test: {len(test_idx)}")

    # Mean pool all embeddings
    print("Mean pooling ...")
    X = mean_pool(embeddings)
    y = np.array(labels)

    X_train, y_train = X[train_idx], y[train_idx]
    X_val, y_val = X[val_idx], y[val_idx]
    X_test, y_test = X[test_idx], y[test_idx]

    # Standardize
    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_val = scaler.transform(X_val)
    X_test = scaler.transform(X_test)

    print(f"Feature dim: {X_train.shape[1]}, train={len(y_train)}, val={len(y_val)}, test={len(y_test)}")
    print(f"Train label dist: 0={sum(y_train==0)}, 1={sum(y_train==1)}")
    print()

    results = []
    results.append(("GRU Probe (ref)", {"macro_f1": PROBE_REF_MACRO_F1}))

    # --- Logistic Regression with C tuning ---
    print("=== Logistic Regression (C tuning on val) ===")
    best_c, best_val_f1 = None, -1
    for c in [0.01, 0.1, 1.0, 10.0]:
        lr = LogisticRegression(max_iter=1000, C=c, solver="lbfgs")
        lr.fit(X_train, y_train)
        val_preds = lr.predict(X_val)
        m = compute_metrics(y_val.tolist(), val_preds.tolist())
        print(f"  C={c:5.2f} → val Macro-F1={m['macro_f1']:.4f}")
        if m["macro_f1"] > best_val_f1:
            best_val_f1 = m["macro_f1"]
            best_c = c

    print(f"  Best C={best_c} (val Macro-F1={best_val_f1:.4f})")
    lr_final = LogisticRegression(max_iter=1000, C=best_c, solver="lbfgs")
    lr_final.fit(X_train, y_train)
    test_preds_lr = lr_final.predict(X_test)
    metrics_lr = compute_metrics(y_test.tolist(), test_preds_lr.tolist())
    results.append(("MeanPool + LR", metrics_lr))
    print(f"  Test Macro-F1={metrics_lr['macro_f1']:.4f}")
    print()

    # --- MLP baseline ---
    print("=== MeanPool + MLP ===")
    mlp = MLPClassifier(hidden_layer_sizes=(256,), max_iter=500, early_stopping=True,
                        validation_fraction=0.15, random_state=42)
    mlp.fit(X_train, y_train)
    test_preds_mlp = mlp.predict(X_test)
    metrics_mlp = compute_metrics(y_test.tolist(), test_preds_mlp.tolist())
    results.append(("MeanPool + MLP(256)", metrics_mlp))
    val_preds_mlp = mlp.predict(X_val)
    val_m = compute_metrics(y_val.tolist(), val_preds_mlp.tolist())
    print(f"  Val  Macro-F1={val_m['macro_f1']:.4f}")
    print(f"  Test Macro-F1={metrics_mlp['macro_f1']:.4f}")
    print()

    # --- Final table ---
    print("=== MeanPool Baseline Results ===")
    print_table(results)

    best_name, best_m = max(results[1:], key=lambda x: x[1]["macro_f1"])
    delta = PROBE_REF_MACRO_F1 - best_m["macro_f1"]
    print(f"\nBest MeanPool baseline: {best_name} (Macro-F1={best_m['macro_f1']:.4f})")
    print(f"GRU Probe vs best MeanPool: {delta:+.4f}")

    # Save JSON
    output_path = Path(args.data_dir) / "meanpool_lr_results.json"
    json_results = {}
    for name, m in results:
        json_results[name] = {k: round(v, 4) if v is not None else None for k, v in m.items()}
    with open(output_path, "w") as f:
        json.dump(json_results, f, indent=2)
    print(f"\nResults saved to {output_path}")


if __name__ == "__main__":
    main()
