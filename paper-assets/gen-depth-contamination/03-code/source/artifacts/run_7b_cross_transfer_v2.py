#!/usr/bin/env python3
"""7B Cross-Model Transfer Matrix with Full Metrics.

Computes 2x2 (or NxN) cross-transfer matrix:
- 6-class ordinal accuracy (LightGBM multiclass)
- MAE (mean absolute error of predicted depth)
- Kendall tau_b (rank correlation)
- Mean pairwise AUC (OBD binary classifiers)
- Transfer retention = metric[A->B] / metric[A->A]

Diagonal: 5-fold GroupKFold OOF predictions.
Off-diagonal: train on 100% of A, predict on 100% of B.
"""

import argparse
import json
import logging
import sys
from pathlib import Path

import numpy as np
import pandas as pd
from scipy.stats import kendalltau
from sklearn.model_selection import GroupKFold
from sklearn.metrics import accuracy_score, mean_absolute_error, roc_auc_score
from lightgbm import LGBMClassifier

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%H:%M:%S",
)
log = logging.getLogger(__name__)

FEAT_COLS = [
    "surp_mean", "surp_std", "surp_skew", "surp_kurt",
    "surp_d1_mean", "surp_d1_std", "surp_d1_skew",
    "surp_d2_mean", "surp_d2_std",
    "ttr", "hapax_ratio", "self_bleu",
    "freq_kurtosis", "freq_entropy", "low_freq_ratio",
]
MAX_DEPTH = 5
N_CLASSES = 6
SEED = 42


def load_features(csv_path, max_docs=None):
    df = pd.read_csv(csv_path)
    for c in FEAT_COLS:
        df[c] = pd.to_numeric(df[c], errors="coerce")
    col_means = df[FEAT_COLS].mean()
    df[FEAT_COLS] = df[FEAT_COLS].fillna(col_means)
    if max_docs is not None:
        unique_docs = sorted(df["doc_id"].unique())[:max_docs]
        df = df[df["doc_id"].isin(unique_docs)].reset_index(drop=True)
    return df


def lgbm_params():
    return dict(
        n_estimators=200,
        max_depth=6,
        learning_rate=0.05,
        num_leaves=31,
        verbose=-1,
        n_jobs=-1,
        random_state=SEED,
    )


def compute_metrics(y_true, y_pred):
    acc = accuracy_score(y_true, y_pred)
    mae = mean_absolute_error(y_true, y_pred)
    tau, _ = kendalltau(y_true, y_pred)
    return {"accuracy": round(acc, 4), "mae": round(mae, 4), "tau_b": round(tau, 4)}


def run_pairwise_auc(X_train, y_train, X_test, y_test, max_d=MAX_DEPTH):
    aucs = {}
    for k in range(max_d):
        key = f"{k}v{k+1}"
        tr_mask = np.isin(y_train, [k, k + 1])
        te_mask = np.isin(y_test, [k, k + 1])
        if tr_mask.sum() < 10 or te_mask.sum() < 10:
            continue
        yt = (y_train[tr_mask] == k + 1).astype(int)
        yv = (y_test[te_mask] == k + 1).astype(int)
        if len(np.unique(yt)) < 2 or len(np.unique(yv)) < 2:
            continue
        clf = LGBMClassifier(**lgbm_params())
        clf.fit(X_train[tr_mask], yt)
        proba = clf.predict_proba(X_test[te_mask])[:, 1]
        aucs[key] = round(float(roc_auc_score(yv, proba)), 4)
    return aucs


def self_transfer(df, n_folds=5):
    X = df[FEAT_COLS].values
    y = df["depth"].values
    groups = df["doc_id"].values

    oof_pred = np.full(len(y), -1, dtype=int)
    gkf = GroupKFold(n_splits=n_folds)

    oof_X_train_all, oof_y_train_all = [], []
    oof_X_test_all, oof_y_test_all = [], []

    for train_idx, test_idx in gkf.split(X, y, groups):
        clf = LGBMClassifier(objective="multiclass", num_class=N_CLASSES, **lgbm_params())
        clf.fit(X[train_idx], y[train_idx])
        oof_pred[test_idx] = clf.predict(X[test_idx])
        oof_X_train_all.append(X[train_idx])
        oof_y_train_all.append(y[train_idx])
        oof_X_test_all.append(X[test_idx])
        oof_y_test_all.append(y[test_idx])

    metrics = compute_metrics(y, oof_pred)

    pairwise_aucs = {}
    for train_idx, test_idx in gkf.split(X, y, groups):
        fold_aucs = run_pairwise_auc(X[train_idx], y[train_idx], X[test_idx], y[test_idx])
        for pair, auc in fold_aucs.items():
            pairwise_aucs.setdefault(pair, []).append(auc)
    mean_pairwise = {p: round(np.mean(a), 4) for p, a in pairwise_aucs.items()}
    metrics["pairwise_auc"] = mean_pairwise
    metrics["mean_pairwise_auc"] = round(np.mean(list(mean_pairwise.values())), 4) if mean_pairwise else 0
    return metrics


def cross_transfer(df_train, df_test):
    X_tr = df_train[FEAT_COLS].values
    y_tr = df_train["depth"].values
    X_te = df_test[FEAT_COLS].values
    y_te = df_test["depth"].values

    clf = LGBMClassifier(objective="multiclass", num_class=N_CLASSES, **lgbm_params())
    clf.fit(X_tr, y_tr)
    y_pred = clf.predict(X_te)

    metrics = compute_metrics(y_te, y_pred)

    pairwise = run_pairwise_auc(X_tr, y_tr, X_te, y_te)
    metrics["pairwise_auc"] = pairwise
    metrics["mean_pairwise_auc"] = round(np.mean(list(pairwise.values())), 4) if pairwise else 0
    return metrics


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--data_dirs", nargs="+", required=True)
    parser.add_argument("--labels", nargs="+", required=True)
    parser.add_argument("--out_dir", required=True)
    parser.add_argument("--max_docs", type=int, default=None,
                        help="Subsample to this many docs per model (for fair comparison)")
    args = parser.parse_args()

    assert len(args.data_dirs) == len(args.labels)
    Path(args.out_dir).mkdir(parents=True, exist_ok=True)

    datasets = {}
    for d, label in zip(args.data_dirs, args.labels):
        df = load_features(Path(d) / "features.csv", max_docs=args.max_docs)
        datasets[label] = df
        log.info(f"Loaded {label}: {len(df)} rows, {df['doc_id'].nunique()} docs, "
                 f"depths {sorted(df['depth'].unique())}")

    labels = args.labels
    matrix = {}

    for train_label in labels:
        for test_label in labels:
            log.info(f"\n{'='*50}")
            log.info(f"  {train_label} -> {test_label}")

            if train_label == test_label:
                m = self_transfer(datasets[train_label])
            else:
                m = cross_transfer(datasets[train_label], datasets[test_label])

            matrix[(train_label, test_label)] = m
            log.info(f"  acc={m['accuracy']}, mae={m['mae']}, tau_b={m['tau_b']}, "
                     f"mean_auc={m['mean_pairwise_auc']}")

    retention = {}
    for train_label in labels:
        diag = matrix[(train_label, train_label)]
        for test_label in labels:
            if test_label == train_label:
                continue
            off = matrix[(train_label, test_label)]
            r = {}
            if diag["accuracy"] > 0:
                r["accuracy"] = round(off["accuracy"] / diag["accuracy"], 4)
            if diag["tau_b"] > 0:
                r["tau_b"] = round(off["tau_b"] / diag["tau_b"], 4)
            if diag["mean_pairwise_auc"] > 0.5:
                r["mean_auc"] = round(
                    (off["mean_pairwise_auc"] - 0.5) / (diag["mean_pairwise_auc"] - 0.5), 4
                )
            retention[f"{train_label}->{test_label}"] = r

    out = {
        "matrix": {f"{k[0]}->{k[1]}": v for k, v in matrix.items()},
        "retention": retention,
        "models": labels,
        "max_docs": args.max_docs,
        "data_dirs": {l: d for l, d in zip(args.labels, args.data_dirs)},
    }

    out_path = Path(args.out_dir) / "cross_transfer_7b_full_metrics.json"
    with open(out_path, "w") as f:
        json.dump(out, f, indent=2)
    log.info(f"\nSaved: {out_path}")

    # Print summary tables
    print(f"\n{'='*70}")
    print("TRANSFER MATRIX — 6-class Accuracy")
    print(f"{'Train\\Test':>15s}" + "".join(f"{l:>15s}" for l in labels))
    for tl in labels:
        row = f"{tl:>15s}"
        for tst in labels:
            row += f"{matrix[(tl, tst)]['accuracy']:>15.4f}"
        print(row)

    print(f"\n{'='*70}")
    print("TRANSFER MATRIX — MAE")
    print(f"{'Train\\Test':>15s}" + "".join(f"{l:>15s}" for l in labels))
    for tl in labels:
        row = f"{tl:>15s}"
        for tst in labels:
            row += f"{matrix[(tl, tst)]['mae']:>15.4f}"
        print(row)

    print(f"\n{'='*70}")
    print("TRANSFER MATRIX — Kendall tau_b")
    print(f"{'Train\\Test':>15s}" + "".join(f"{l:>15s}" for l in labels))
    for tl in labels:
        row = f"{tl:>15s}"
        for tst in labels:
            row += f"{matrix[(tl, tst)]['tau_b']:>15.4f}"
        print(row)

    print(f"\n{'='*70}")
    print("TRANSFER MATRIX — Mean Pairwise AUC")
    print(f"{'Train\\Test':>15s}" + "".join(f"{l:>15s}" for l in labels))
    for tl in labels:
        row = f"{tl:>15s}"
        for tst in labels:
            row += f"{matrix[(tl, tst)]['mean_pairwise_auc']:>15.4f}"
        print(row)

    print(f"\n{'='*70}")
    print("RETENTION RATES")
    for key, r in retention.items():
        parts = [f"{key:>30s}:"]
        for metric, val in r.items():
            parts.append(f"{metric}={val:.1%}")
        print("  ".join(parts))

    print(f"\n{'='*70}")
    print("PAIRWISE AUC per depth pair")
    for pair_name in ["0v1", "1v2", "2v3", "3v4", "4v5"]:
        print(f"\n--- {pair_name} ---")
        print(f"{'Train\\Test':>15s}" + "".join(f"{l:>15s}" for l in labels))
        for tl in labels:
            row = f"{tl:>15s}"
            for tst in labels:
                v = matrix[(tl, tst)]["pairwise_auc"].get(pair_name, "N/A")
                row += f"{v:>15.4f}" if isinstance(v, float) else f"{v:>15s}"
            print(row)


if __name__ == "__main__":
    main()
