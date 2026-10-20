"""
Cross-model Transfer Analysis (exp-013)

Trains LightGBM depth classifier on model A's features,
evaluates on model B's features. Tests whether depth signal
is text-intrinsic or model-specific.

Input:  features.csv from multiple model runs (each with doc_id, depth, 15 feature cols)
Output: results_exp013/cross_transfer_matrix.json  — NxN transfer AUC matrix
        results_exp013/cross_transfer_detail.json   — per-pair pairwise AUC, K*, ordinal acc/MAE

Dependencies: numpy, lightgbm, scikit-learn, pandas (optional, falls back to csv)
"""

import argparse
import csv
import json
import logging
import os
import sys
from pathlib import Path

import numpy as np
from sklearn.metrics import accuracy_score, mean_absolute_error, roc_auc_score
from sklearn.model_selection import GroupKFold

import lightgbm as lgb

log = logging.getLogger("exp013")
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)

META_COLS = {"doc_id", "depth"}


def load_features(data_dir: str, max_depth: int):
    """Load features.csv, return (feat_matrix, depths, doc_ids, feat_cols)."""
    csv_path = Path(data_dir) / "features.csv"
    if not csv_path.exists():
        raise FileNotFoundError(f"features.csv not found in {data_dir}")

    with open(csv_path, "r") as f:
        reader = csv.DictReader(f)
        header = reader.fieldnames
        feat_cols = [c for c in header if c not in META_COLS]
        rows = list(reader)

    if max_depth is not None:
        rows = [r for r in rows if int(r["depth"]) <= max_depth]

    depths = np.array([int(r["depth"]) for r in rows])
    doc_ids = np.array([int(r["doc_id"]) for r in rows])
    feat_matrix = np.array(
        [
            [float(r[c]) if r[c] not in ("", "nan") else np.nan for c in feat_cols]
            for r in rows
        ]
    )

    col_means = np.nanmean(feat_matrix, axis=0)
    for j in range(feat_matrix.shape[1]):
        mask = np.isnan(feat_matrix[:, j])
        if mask.any():
            feat_matrix[mask, j] = col_means[j]

    return feat_matrix, depths, doc_ids, feat_cols


def compute_pairwise_auc_cross(X_train, y_train, X_test, y_test, max_depth):
    """Train pairwise binary classifiers on train set, evaluate on test set."""
    results = {}
    for k in range(1, max_depth + 1):
        mask_tr = (y_train == k - 1) | (y_train == k)
        mask_te = (y_test == k - 1) | (y_test == k)

        Xtr, ytr = X_train[mask_tr], (y_train[mask_tr] == k).astype(int)
        Xte, yte = X_test[mask_te], (y_test[mask_te] == k).astype(int)

        if len(np.unique(ytr)) < 2 or len(np.unique(yte)) < 2:
            results[f"{k-1}v{k}"] = float("nan")
            continue

        clf = lgb.LGBMClassifier(
            n_estimators=200, max_depth=6, learning_rate=0.05,
            num_leaves=31, verbose=-1, n_jobs=-1,
        )
        clf.fit(Xtr, ytr)
        proba = clf.predict_proba(Xte)[:, 1]
        results[f"{k-1}v{k}"] = round(float(roc_auc_score(yte, proba)), 4)

    return results


def compute_pairwise_auc_self(X, y, doc_ids, max_depth):
    """Pairwise AUC with GroupKFold (self-transfer baseline)."""
    results = {}
    for k in range(1, max_depth + 1):
        mask = (y == k - 1) | (y == k)
        Xm, ym = X[mask], (y[mask] == k).astype(int)
        groups = doc_ids[mask]

        if len(np.unique(ym)) < 2:
            results[f"{k-1}v{k}"] = float("nan")
            continue

        gkf = GroupKFold(n_splits=5)
        fold_aucs = []
        for train_idx, test_idx in gkf.split(Xm, ym, groups=groups):
            clf = lgb.LGBMClassifier(
                n_estimators=200, max_depth=6, learning_rate=0.05,
                num_leaves=31, verbose=-1, n_jobs=-1,
            )
            clf.fit(Xm[train_idx], ym[train_idx])
            proba = clf.predict_proba(Xm[test_idx])[:, 1]
            fold_aucs.append(roc_auc_score(ym[test_idx], proba))

        results[f"{k-1}v{k}"] = round(float(np.mean(fold_aucs)), 4)

    return results


def compute_ordinal_cross(X_train, y_train, X_test, y_test, max_depth):
    """Ordinal multiclass: train on A, test on B."""
    clf = lgb.LGBMClassifier(
        n_estimators=300, max_depth=8, learning_rate=0.05,
        num_leaves=63, verbose=-1, n_jobs=-1,
        num_class=max_depth + 1,
        objective="multiclass",
    )
    clf.fit(X_train, y_train)
    preds = clf.predict(X_test)
    return {
        "accuracy": round(float(accuracy_score(y_test, preds)), 4),
        "mae": round(float(mean_absolute_error(y_test, preds)), 4),
    }


def compute_ordinal_self(X, y, doc_ids, max_depth):
    """Ordinal multiclass with GroupKFold (self-transfer baseline)."""
    gkf = GroupKFold(n_splits=5)
    all_preds = np.zeros_like(y, dtype=float)

    for train_idx, test_idx in gkf.split(X, y, groups=doc_ids):
        clf = lgb.LGBMClassifier(
            n_estimators=300, max_depth=8, learning_rate=0.05,
            num_leaves=63, verbose=-1, n_jobs=-1,
            num_class=max_depth + 1,
            objective="multiclass",
        )
        clf.fit(X[train_idx], y[train_idx])
        all_preds[test_idx] = clf.predict(X[test_idx])

    return {
        "accuracy": round(float(accuracy_score(y, all_preds.astype(int))), 4),
        "mae": round(float(mean_absolute_error(y, all_preds)), 4),
    }


def compute_k_star(pairwise_auc, max_depth, threshold=0.60):
    """K* = max k where AUC(k-1 vs k) > threshold."""
    k_star = 0
    for k in range(1, max_depth + 1):
        if pairwise_auc.get(f"{k-1}v{k}", 0) > threshold:
            k_star = k
    return k_star


def main():
    parser = argparse.ArgumentParser(
        description="Cross-model Transfer Analysis (exp-013): "
        "train depth classifier on model A, test on model B.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""Example:
  python scripts/run_cross_transfer.py \\
    --data_dirs data_exp001_pythia data_exp002_olmo data \\
    --labels Pythia-1.4B OLMo-1B Qwen-1.5B \\
    --results_dir results_exp013""",
    )
    parser.add_argument(
        "--data_dirs", nargs="+", required=True,
        help="Directories containing features.csv (one per model)",
    )
    parser.add_argument(
        "--labels", nargs="+", required=True,
        help="Human-readable label for each data dir",
    )
    parser.add_argument("--results_dir", default="results_exp013")
    parser.add_argument("--max_depth", type=int, default=5)
    args = parser.parse_args()

    if len(args.data_dirs) != len(args.labels):
        parser.error("--data_dirs and --labels must have the same number of entries")

    results_dir = Path(args.results_dir)
    results_dir.mkdir(parents=True, exist_ok=True)

    # --- Load all datasets ---
    datasets = {}
    for ddir, label in zip(args.data_dirs, args.labels):
        log.info(f"Loading {label} from {ddir} ...")
        feat, depths, doc_ids, feat_cols = load_features(ddir, args.max_depth)
        datasets[label] = {"X": feat, "y": depths, "doc_ids": doc_ids, "feat_cols": feat_cols}
        log.info(f"  {label}: {feat.shape[0]} rows, {feat.shape[1]} features, "
                 f"depths {depths.min()}-{depths.max()}")

    # Verify feature columns match across datasets
    ref_cols = datasets[args.labels[0]]["feat_cols"]
    for label in args.labels[1:]:
        if datasets[label]["feat_cols"] != ref_cols:
            log.error(f"Feature columns mismatch: {args.labels[0]} has {ref_cols}, "
                      f"{label} has {datasets[label]['feat_cols']}")
            sys.exit(1)

    n_models = len(args.labels)
    max_depth = args.max_depth

    # --- Transfer matrix ---
    matrix = {}  # label -> label -> mean AUC
    detail = {}  # label -> label -> full results

    for train_label in args.labels:
        matrix[train_label] = {}
        detail[train_label] = {}
        d_train = datasets[train_label]

        for test_label in args.labels:
            d_test = datasets[test_label]
            pair_key = f"{train_label} -> {test_label}"

            if train_label == test_label:
                # Self-transfer: GroupKFold
                log.info(f"Self-transfer: {train_label} (GroupKFold) ...")
                pw_auc = compute_pairwise_auc_self(
                    d_train["X"], d_train["y"], d_train["doc_ids"], max_depth
                )
                ordinal = compute_ordinal_self(
                    d_train["X"], d_train["y"], d_train["doc_ids"], max_depth
                )
            else:
                # Cross-transfer: train on 100% A, test on 100% B
                log.info(f"Cross-transfer: {pair_key} ...")
                pw_auc = compute_pairwise_auc_cross(
                    d_train["X"], d_train["y"],
                    d_test["X"], d_test["y"], max_depth,
                )
                ordinal = compute_ordinal_cross(
                    d_train["X"], d_train["y"],
                    d_test["X"], d_test["y"], max_depth,
                )

            k_star = compute_k_star(pw_auc, max_depth)

            valid_aucs = [v for v in pw_auc.values() if not np.isnan(v)]
            mean_auc = round(float(np.mean(valid_aucs)), 4) if valid_aucs else float("nan")
            matrix[train_label][test_label] = mean_auc

            detail[train_label][test_label] = {
                "pairwise_auc": pw_auc,
                "mean_pairwise_auc": mean_auc,
                "k_star": k_star,
                **ordinal,
            }

            log.info(f"  {pair_key}: mean_AUC={mean_auc}, K*={k_star}, "
                     f"acc={ordinal['accuracy']}, MAE={ordinal['mae']}")

    # --- Save results ---
    with open(results_dir / "cross_transfer_matrix.json", "w") as f:
        json.dump(matrix, f, indent=2)
    with open(results_dir / "cross_transfer_detail.json", "w") as f:
        json.dump(detail, f, indent=2)

    # --- Terminal summary ---
    print("\n" + "=" * 70)
    print("exp-013  Cross-model Transfer — Summary")
    print("=" * 70)

    col_w = max(len(l) for l in args.labels) + 2
    header = " " * col_w + "".join(f"{l:>{col_w}}" for l in args.labels)
    print(f"\nMean Pairwise AUC (train → test):")
    print(header)
    for train_l in args.labels:
        row = f"{train_l:<{col_w}}"
        for test_l in args.labels:
            v = matrix[train_l][test_l]
            cell = f"{v:.4f}" if not np.isnan(v) else "  NaN"
            row += f"{cell:>{col_w}}"
        print(row)

    print(f"\nK* (train → test):")
    print(header)
    for train_l in args.labels:
        row = f"{train_l:<{col_w}}"
        for test_l in args.labels:
            v = detail[train_l][test_l]["k_star"]
            row += f"{v:>{col_w}}"
        print(row)

    print(f"\nOrdinal Accuracy (train → test):")
    print(header)
    for train_l in args.labels:
        row = f"{train_l:<{col_w}}"
        for test_l in args.labels:
            v = detail[train_l][test_l]["accuracy"]
            row += f"{v:>{col_w}.4f}"
        print(row)

    print("\n" + "=" * 70)

    # Interpretation hint
    diag_aucs = [matrix[l][l] for l in args.labels]
    off_aucs = [matrix[tl][tel] for tl in args.labels for tel in args.labels if tl != tel]
    if diag_aucs and off_aucs:
        diag_mean = np.mean(diag_aucs)
        off_mean = np.mean(off_aucs)
        drop = diag_mean - off_mean
        print(f"Diagonal (self) mean AUC: {diag_mean:.4f}")
        print(f"Off-diag (cross) mean AUC: {off_mean:.4f}")
        print(f"Transfer drop: {drop:+.4f}")
        if abs(drop) < 0.03:
            print("=> Depth signal appears text-intrinsic (minimal transfer drop)")
        else:
            print("=> Depth signal may be partly model-specific (notable transfer drop)")

    print("=" * 70)
    log.info(f"Results saved to {results_dir}/")


if __name__ == "__main__":
    main()
