#!/usr/bin/env python3
"""GroupKFold probe on full-data entity hidden states.

Reads pre-extracted hidden states + instance_ids from entity_probe_fulldata/.
No model loading needed, CPU only.

Usage:
  python groupkfold_probe_fulldata.py
"""

import json
import os
import time

import numpy as np
import torch
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import GroupKFold, StratifiedKFold
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import roc_auc_score

BASE_DIR = "/root/autodl-tmp/struct_self_consist_ie"
INPUT_DIR = os.path.join(BASE_DIR, "output/entity_probe_fulldata")
OUTPUT_DIR = INPUT_DIR

DATASETS = ["conll", "fewnerd", "scierc"]
SEEDS = [42, 123, 456]
CV_FOLDS = 5


def run_groupkfold(X, y, groups, n_splits=CV_FOLDS, seeds=SEEDS):
    all_fold_aurocs = []
    for seed in seeds:
        np.random.seed(seed)
        indices = np.random.permutation(len(X))
        X_perm, y_perm, g_perm = X[indices], y[indices], groups[indices]

        gkf = GroupKFold(n_splits=n_splits)
        fold_aurocs = []
        for train_idx, test_idx in gkf.split(X_perm, y_perm, g_perm):
            X_train, X_test = X_perm[train_idx], X_perm[test_idx]
            y_train, y_test = y_perm[train_idx], y_perm[test_idx]

            scaler = StandardScaler()
            X_train = scaler.fit_transform(X_train)
            X_test = scaler.transform(X_test)

            clf = LogisticRegression(max_iter=1000, C=1.0, solver="lbfgs", random_state=seed)
            clf.fit(X_train, y_train)
            y_prob = clf.predict_proba(X_test)[:, 1]

            if len(np.unique(y_test)) < 2:
                continue
            fold_aurocs.append(roc_auc_score(y_test, y_prob))

        if fold_aurocs:
            all_fold_aurocs.append(np.mean(fold_aurocs))

    return all_fold_aurocs


def run_stratifiedkfold(X, y, n_splits=CV_FOLDS, seeds=SEEDS):
    all_seed_aurocs = []
    for seed in seeds:
        skf = StratifiedKFold(n_splits=n_splits, shuffle=True, random_state=seed)
        fold_aurocs = []
        for train_idx, test_idx in skf.split(X, y):
            X_train, X_test = X[train_idx], X[test_idx]
            y_train, y_test = y[train_idx], y[test_idx]

            scaler = StandardScaler()
            X_train = scaler.fit_transform(X_train)
            X_test = scaler.transform(X_test)

            clf = LogisticRegression(max_iter=1000, C=1.0, solver="lbfgs", random_state=seed)
            clf.fit(X_train, y_train)
            y_prob = clf.predict_proba(X_test)[:, 1]

            if len(np.unique(y_test)) < 2:
                continue
            fold_aurocs.append(roc_auc_score(y_test, y_prob))

        if fold_aurocs:
            all_seed_aurocs.append(np.mean(fold_aurocs))

    return all_seed_aurocs


def main():
    results = {}

    for ds in DATASETS:
        hs_path = os.path.join(INPUT_DIR, f"entity_hidden_states_{ds}.pt")
        lb_path = os.path.join(INPUT_DIR, f"entity_labels_{ds}.pt")
        id_path = os.path.join(INPUT_DIR, f"entity_instance_ids_{ds}.pt")

        if not os.path.exists(hs_path):
            print(f"{ds}: no hidden states found, skipping")
            continue

        print(f"\n{'='*60}")
        print(f"Processing {ds}...")

        X = torch.load(hs_path, map_location="cpu", weights_only=True).numpy()
        y = torch.load(lb_path, map_location="cpu", weights_only=True).numpy()
        groups = torch.load(id_path, map_location="cpu", weights_only=True).numpy()

        n_pos = int(y.sum())
        n_neg = len(y) - n_pos
        n_inst = len(np.unique(groups))
        print(f"  {len(X)} entities, {n_pos} positive ({n_pos/len(y)*100:.1f}%), "
              f"{n_neg} negative, {n_inst} instances, dim={X.shape[1]}")

        # GroupKFold
        t0 = time.time()
        gkf_aurocs = run_groupkfold(X, y, groups)
        gkf_time = time.time() - t0
        gkf_mean = np.mean(gkf_aurocs)
        gkf_std = np.std(gkf_aurocs)
        print(f"  GroupKFold AUROC: {gkf_mean:.4f} +/- {gkf_std:.4f} ({gkf_time:.1f}s)")

        # StratifiedKFold
        t0 = time.time()
        skf_aurocs = run_stratifiedkfold(X, y)
        skf_time = time.time() - t0
        skf_mean = np.mean(skf_aurocs)
        skf_std = np.std(skf_aurocs)
        print(f"  StratifiedKFold AUROC: {skf_mean:.4f} +/- {skf_std:.4f} ({skf_time:.1f}s)")

        delta = skf_mean - gkf_mean
        print(f"  Leakage (SKF - GKF): {delta:+.4f}")
        print(f"  vs MV=0.87, ESJ=0.51")

        if gkf_mean > 0.87:
            interp = "HIGH: probe > MV, info in representation, prompting fails"
        elif gkf_mean > 0.70:
            interp = "MODERATE-HIGH: probe below MV but well above ESJ"
        elif gkf_mean > 0.60:
            interp = "MODERATE: partial info in representation"
        else:
            interp = "LOW: info not clearly present"
        print(f"  => {interp}")

        results[ds] = {
            "groupkfold_auroc_mean": float(gkf_mean),
            "groupkfold_auroc_std": float(gkf_std),
            "groupkfold_auroc_per_seed": [float(a) for a in gkf_aurocs],
            "stratifiedkfold_auroc_mean": float(skf_mean),
            "stratifiedkfold_auroc_std": float(skf_std),
            "stratifiedkfold_auroc_per_seed": [float(a) for a in skf_aurocs],
            "leakage_delta": float(delta),
            "n_entities": int(len(y)),
            "n_positive": n_pos,
            "n_negative": n_neg,
            "positive_rate": float(y.mean()),
            "n_instances": n_inst,
        }

    # Summary
    print(f"\n{'='*60}")
    print("SUMMARY: GroupKFold vs StratifiedKFold AUROC (Full Data)")
    print(f"{'='*60}")
    print(f"{'Dataset':<10} {'GroupKFold':>12} {'StratKFold':>12} {'Leakage':>8} "
          f"{'MV':>6} {'ESJ':>6} {'Probe>MV?':>10}")
    for ds, r in results.items():
        above_mv = "YES" if r["groupkfold_auroc_mean"] > 0.87 else "NO"
        print(f"{ds:<10} {r['groupkfold_auroc_mean']:>12.4f} "
              f"{r['stratifiedkfold_auroc_mean']:>12.4f} "
              f"{r['leakage_delta']:>+8.4f} "
              f"{'0.87':>6} {'0.51':>6} "
              f"{above_mv:>10}")

    # Save
    output = {
        "method": "GroupKFold",
        "n_splits": CV_FOLDS,
        "seeds": SEEDS,
        "classifier": "LogisticRegression(C=1.0)",
        "datasets": results,
        "stratifiedkfold_comparison": {
            ds: {
                "auroc_mean": r["stratifiedkfold_auroc_mean"],
                "auroc_std": r["stratifiedkfold_auroc_std"],
            }
            for ds, r in results.items()
        },
        "baselines": {"mv_agreement": 0.87, "esj": 0.51, "random": 0.50},
    }

    out_path = os.path.join(OUTPUT_DIR, "groupkfold_probe_results.json")
    with open(out_path, "w") as f:
        json.dump(output, f, indent=2)
    print(f"\nSaved: {out_path}")


if __name__ == "__main__":
    main()
