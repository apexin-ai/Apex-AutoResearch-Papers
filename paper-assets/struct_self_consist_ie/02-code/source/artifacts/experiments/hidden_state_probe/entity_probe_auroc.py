#!/usr/bin/env python3
"""Linear probe on entity-level hidden states → AUROC for in-gold classification.

Purpose: Determine if entity quality information is encoded in model's hidden
representations but inaccessible via prompting.

Comparison targets:
  - MV agreement AUROC = 0.87  (information exists in multi-sample outputs)
  - ESJ (prompt-based) AUROC = 0.51  (prompting cannot access it)
  - Random baseline AUROC = 0.50

Interpretation:
  - Probe AUROC ≈ 0.87 → info IS in representation, prompting fails
  - Probe AUROC ≈ 0.51 → info NOT in representation either
  - Probe AUROC in between → partial encoding

Input:
  - entity_hidden_states_{dataset}.pt per dataset
  - entity_labels_{dataset}.pt per dataset

Output:
  - entity_probe_results.json — per-dataset and cross-dataset AUROC

Usage:
  python entity_probe_auroc.py
  python entity_probe_auroc.py --data-dir /path/to/entity_probe_auroc
"""

import argparse
import json
import os
import warnings

import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_auc_score, accuracy_score, f1_score
from sklearn.model_selection import StratifiedKFold
from sklearn.preprocessing import StandardScaler

warnings.filterwarnings("ignore")

DEFAULT_DATA_DIR = "/root/autodl-tmp/struct_self_consist_ie/output/entity_probe_auroc"
DATASETS = ["scierc", "fewnerd", "conll"]
SEEDS = [42, 123, 456]
CV_FOLDS = 5


def load_dataset(data_dir, dataset):
    """Load hidden states and labels for a dataset."""
    import torch
    hs_path = os.path.join(data_dir, f"entity_hidden_states_{dataset}.pt")
    lb_path = os.path.join(data_dir, f"entity_labels_{dataset}.pt")
    if not os.path.exists(hs_path):
        return None, None
    hidden_states = torch.load(hs_path, map_location="cpu").numpy()
    labels = torch.load(lb_path, map_location="cpu").numpy()
    return hidden_states, labels


def train_probe_cv(X, y, n_folds=CV_FOLDS, seeds=SEEDS):
    """Train LogisticRegression with stratified k-fold CV across multiple seeds."""
    all_aurocs = []
    all_accs = []
    all_f1s = []

    for seed in seeds:
        skf = StratifiedKFold(n_splits=n_folds, shuffle=True, random_state=seed)
        fold_aurocs = []
        fold_accs = []
        fold_f1s = []

        for train_idx, val_idx in skf.split(X, y):
            X_train, X_val = X[train_idx], X[val_idx]
            y_train, y_val = y[train_idx], y[val_idx]

            scaler = StandardScaler()
            X_train = scaler.fit_transform(X_train)
            X_val = scaler.transform(X_val)

            clf = LogisticRegression(max_iter=1000, C=1.0, random_state=seed)
            clf.fit(X_train, y_train)

            y_prob = clf.predict_proba(X_val)[:, 1]
            y_pred = clf.predict(X_val)

            fold_aurocs.append(roc_auc_score(y_val, y_prob))
            fold_accs.append(accuracy_score(y_val, y_pred))
            fold_f1s.append(f1_score(y_val, y_pred))

        all_aurocs.append(np.mean(fold_aurocs))
        all_accs.append(np.mean(fold_accs))
        all_f1s.append(np.mean(fold_f1s))

    return {
        "auroc_mean": float(np.mean(all_aurocs)),
        "auroc_std": float(np.std(all_aurocs)),
        "auroc_per_seed": [float(x) for x in all_aurocs],
        "accuracy_mean": float(np.mean(all_accs)),
        "accuracy_std": float(np.std(all_accs)),
        "f1_mean": float(np.mean(all_f1s)),
        "f1_std": float(np.std(all_f1s)),
    }


def train_probe_lodo(datasets_data):
    """Leave-One-Dataset-Out: train on 2 datasets, test on the 3rd."""
    results = {}
    dataset_names = list(datasets_data.keys())

    for test_ds in dataset_names:
        train_datasets = [d for d in dataset_names if d != test_ds]
        X_test, y_test = datasets_data[test_ds]

        X_trains = []
        y_trains = []
        for ds in train_datasets:
            X_d, y_d = datasets_data[ds]
            X_trains.append(X_d)
            y_trains.append(y_d)
        X_train = np.concatenate(X_trains)
        y_train = np.concatenate(y_trains)

        seed_aurocs = []
        seed_accs = []
        seed_f1s = []

        for seed in SEEDS:
            scaler = StandardScaler()
            X_tr = scaler.fit_transform(X_train)
            X_te = scaler.transform(X_test)

            clf = LogisticRegression(max_iter=1000, C=1.0, random_state=seed)
            clf.fit(X_tr, y_train)

            y_prob = clf.predict_proba(X_te)[:, 1]
            y_pred = clf.predict(X_te)

            seed_aurocs.append(roc_auc_score(y_test, y_prob))
            seed_accs.append(accuracy_score(y_test, y_pred))
            seed_f1s.append(f1_score(y_test, y_pred))

        results[test_ds] = {
            "train_on": train_datasets,
            "test_on": test_ds,
            "n_train": len(X_train),
            "n_test": len(X_test),
            "auroc_mean": float(np.mean(seed_aurocs)),
            "auroc_std": float(np.std(seed_aurocs)),
            "auroc_per_seed": [float(x) for x in seed_aurocs],
            "accuracy_mean": float(np.mean(seed_accs)),
            "f1_mean": float(np.mean(seed_f1s)),
        }

    return results


def logprob_baseline_auroc(data_dir, dataset):
    """Compute AUROC using mean log-probability as a simple baseline."""
    meta_path = os.path.join(data_dir, f"entity_metadata_{dataset}.json")
    if not os.path.exists(meta_path):
        return None
    with open(meta_path) as f:
        meta = json.load(f)

    # We don't have per-entity logprob directly, but we can use sample-level
    # For now, return None — this baseline is not directly comparable
    return None


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--data-dir", default=DEFAULT_DATA_DIR)
    args = parser.parse_args()

    print("=" * 70)
    print("Entity-Level Hidden State Probe: AUROC Analysis")
    print("=" * 70)

    # Load all available datasets
    datasets_data = {}
    for ds in DATASETS:
        X, y = load_dataset(args.data_dir, ds)
        if X is not None:
            datasets_data[ds] = (X, y)
            n_pos = int(y.sum())
            n_neg = len(y) - n_pos
            print(f"\n  {ds}: {len(X)} entities, {n_pos} positive ({n_pos/len(y)*100:.1f}%), "
                  f"{n_neg} negative, dim={X.shape[1]}")

    if not datasets_data:
        print("\nERROR: No entity hidden state data found.")
        print(f"  Expected files in: {args.data_dir}")
        print(f"  Run extract_entity_hidden_states.py first.")
        return

    # Per-dataset within-dataset CV
    print("\n" + "=" * 70)
    print("Within-Dataset 5-Fold CV (LogisticRegression)")
    print("=" * 70)

    within_results = {}
    for ds, (X, y) in datasets_data.items():
        result = train_probe_cv(X, y)
        within_results[ds] = result
        print(f"\n  {ds}:")
        print(f"    AUROC = {result['auroc_mean']:.4f} +/- {result['auroc_std']:.4f}")
        print(f"    Accuracy = {result['accuracy_mean']:.4f}")
        print(f"    F1 = {result['f1_mean']:.4f}")

    # Leave-One-Dataset-Out (if we have >= 2 datasets)
    lodo_results = {}
    if len(datasets_data) >= 2:
        print("\n" + "=" * 70)
        print("Leave-One-Dataset-Out (train on others, test on held-out)")
        print("=" * 70)

        lodo_results = train_probe_lodo(datasets_data)
        for test_ds, result in lodo_results.items():
            print(f"\n  Test: {test_ds} (train: {result['train_on']})")
            print(f"    AUROC = {result['auroc_mean']:.4f} +/- {result['auroc_std']:.4f}")
            print(f"    Accuracy = {result['accuracy_mean']:.4f}")
            print(f"    F1 = {result['f1_mean']:.4f}")

    # Overall summary
    all_aurocs_within = [r["auroc_mean"] for r in within_results.values()]
    overall_within = np.mean(all_aurocs_within)

    if lodo_results:
        all_aurocs_lodo = [r["auroc_mean"] for r in lodo_results.values()]
        overall_lodo = np.mean(all_aurocs_lodo)
    else:
        overall_lodo = None

    print("\n" + "=" * 70)
    print("COMPARISON TABLE")
    print("=" * 70)
    print(f"\n{'Method':<30} {'AUROC':>10} {'Interpretation':<30}")
    print("-" * 70)
    print(f"{'Random baseline':<30} {'0.5000':>10} {'no information':<30}")
    print(f"{'ESJ (prompt-based)':<30} {'0.5100':>10} {'prompting fails':<30}")
    print(f"{'Hidden Probe (within-ds)':<30} {overall_within:>10.4f} {'':<30}")
    if overall_lodo is not None:
        print(f"{'Hidden Probe (LODO)':<30} {overall_lodo:>10.4f} {'':<30}")
    print(f"{'MV Agreement':<30} {'0.8700':>10} {'multi-sample signal':<30}")
    print("-" * 70)

    # Interpretation
    probe_auroc = overall_lodo if overall_lodo is not None else overall_within
    if probe_auroc > 0.7:
        interpretation = "CONFIRMED: info exists in representation but prompting fails"
    elif probe_auroc > 0.6:
        interpretation = "PARTIAL: some information in representation, weaker than MV"
    else:
        interpretation = "NEGATIVE: info not present in single-sample representation"
    print(f"\n  Conclusion: {interpretation}")

    # Save results
    output = {
        "within_dataset_cv": within_results,
        "leave_one_dataset_out": lodo_results,
        "overall_within_auroc": float(overall_within),
        "overall_lodo_auroc": float(overall_lodo) if overall_lodo else None,
        "baselines": {
            "random": 0.50,
            "esj_prompt_based": 0.51,
            "mv_agreement": 0.87,
        },
        "interpretation": interpretation,
        "protocol": {
            "probe": "LogisticRegression(C=1.0, max_iter=1000)",
            "cv_folds": CV_FOLDS,
            "seeds": SEEDS,
            "scaler": "StandardScaler",
            "label": "binary: in_gold (1) vs not_in_gold (0)",
            "feature": "mean-pool hidden states at entity span tokens (last layer)",
        },
    }

    output_path = os.path.join(args.data_dir, "entity_probe_results.json")
    with open(output_path, "w") as f:
        json.dump(output, f, indent=2)
    print(f"\n  Results saved to {output_path}")


if __name__ == "__main__":
    main()
