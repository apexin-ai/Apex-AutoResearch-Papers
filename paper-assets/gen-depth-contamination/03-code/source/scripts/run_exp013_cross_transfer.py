"""
exp-013: Cross-model transfer matrix for depth classifiers.

Train OBD-LightGBM depth classifier on model A's features, test on model B's features.
Diagonal = within-model 5-fold CV; off-diagonal = full train→test transfer.

Inputs:  4 features.csv files (one per model), each with 15 surprisal/lexical features + depth label.
Outputs: artifacts/cross_transfer_matrix.json, artifacts/cross_transfer_matrix.csv, printed 4×4 matrix.
"""
import argparse
import csv
import json
from pathlib import Path

import numpy as np
from scipy.stats import kendalltau
from sklearn.metrics import mean_absolute_error, accuracy_score, roc_auc_score
from sklearn.model_selection import GroupKFold
import lightgbm as lgb

FEAT_COLS = [
    "surp_mean", "surp_std", "surp_skew", "surp_kurt",
    "surp_d1_mean", "surp_d1_std", "surp_d1_skew",
    "surp_d2_mean", "surp_d2_std",
    "ttr", "hapax_ratio", "self_bleu",
    "freq_kurtosis", "freq_entropy", "low_freq_ratio",
]

DEFAULT_DATA_DIRS = [
    "/root/autodl-tmp/gen-depth-contamination/data",
    "/root/autodl-tmp/gen-depth-contamination/data_exp001_pythia",
    "/root/autodl-tmp/gen-depth-contamination/data_exp002_olmo",
    "/root/autodl-tmp/gen-depth-contamination/data_exp017_qwen_cont",
]
DEFAULT_LABELS = ["Qwen-rewrite", "Pythia", "OLMo", "Qwen-cont"]

MAX_DEPTH = 5
N_SPLITS = 5
SEED = 42

LGB_PARAMS = dict(
    n_estimators=200, max_depth=6, learning_rate=0.05,
    num_leaves=31, verbose=-1, n_jobs=-1, random_state=SEED,
)


def load_features(path):
    with open(path) as f:
        reader = csv.DictReader(f)
        rows = list(reader)
    depths = np.array([int(r["depth"]) for r in rows])
    doc_ids = np.array([int(r["doc_id"]) for r in rows])
    X = np.array([
        [float(r[c]) if r[c] not in ("", "nan") else np.nan for c in FEAT_COLS]
        for r in rows
    ])
    col_means = np.nanmean(X, axis=0)
    for j in range(X.shape[1]):
        mask = np.isnan(X[:, j])
        X[mask, j] = col_means[j]
    return X, depths, doc_ids


def obd_cum_to_class_probs(cum_probs, n_classes):
    """Convert P(Y>k) cumulative probabilities to class probabilities."""
    probs = np.zeros((cum_probs.shape[0], n_classes))
    probs[:, 0] = 1.0 - cum_probs[:, 0]
    for k in range(1, n_classes - 1):
        probs[:, k] = cum_probs[:, k - 1] - cum_probs[:, k]
    probs[:, -1] = cum_probs[:, -1]
    probs = np.clip(probs, 0, 1)
    row_sums = probs.sum(axis=1, keepdims=True)
    row_sums[row_sums == 0] = 1.0
    probs /= row_sums
    return probs


def train_obd(X_train, y_train):
    """Train K-1 OBD binary classifiers, return list of fitted models."""
    models = []
    for k in range(MAX_DEPTH):
        y_bin = (y_train > k).astype(int)
        clf = lgb.LGBMClassifier(**LGB_PARAMS)
        clf.fit(X_train, y_bin)
        models.append(clf)
    return models


def predict_obd(models, X_test):
    """Predict class probabilities and labels from OBD models."""
    n = X_test.shape[0]
    cum_probs = np.zeros((n, MAX_DEPTH))
    for k, clf in enumerate(models):
        cum_probs[:, k] = clf.predict_proba(X_test)[:, 1]
    class_probs = obd_cum_to_class_probs(cum_probs, MAX_DEPTH + 1)
    preds = class_probs.argmax(axis=1)
    return preds, class_probs


def within_model_cv(X, y, groups):
    """5-fold GroupKFold CV, return predictions and class probabilities."""
    n = len(y)
    all_preds = np.zeros(n, dtype=int)
    all_probs = np.zeros((n, MAX_DEPTH + 1))
    gkf = GroupKFold(n_splits=N_SPLITS)
    for train_idx, test_idx in gkf.split(X, y, groups=groups):
        models = train_obd(X[train_idx], y[train_idx])
        preds, probs = predict_obd(models, X[test_idx])
        all_preds[test_idx] = preds
        all_probs[test_idx] = probs
    return all_preds, all_probs


def cross_model_transfer(X_train, y_train, X_test):
    """Train on full source, predict on target."""
    models = train_obd(X_train, y_train)
    return predict_obd(models, X_test)


def pairwise_auc(y_true, y_probs):
    results = {}
    for k in range(1, MAX_DEPTH + 1):
        mask = (y_true == k - 1) | (y_true == k)
        if mask.sum() < 10:
            results[f"{k-1}v{k}"] = float("nan")
            continue
        y_bin = (y_true[mask] == k).astype(int)
        if len(np.unique(y_bin)) < 2:
            results[f"{k-1}v{k}"] = float("nan")
            continue
        score = y_probs[mask, k] if y_probs.ndim == 2 else np.zeros(mask.sum())
        try:
            results[f"{k-1}v{k}"] = round(float(roc_auc_score(y_bin, score)), 4)
        except ValueError:
            results[f"{k-1}v{k}"] = float("nan")
    return results


def evaluate(y_true, y_pred, y_probs):
    acc = round(float(accuracy_score(y_true, y_pred)), 4)
    mae = round(float(mean_absolute_error(y_true, y_pred)), 4)
    tau, tau_p = kendalltau(y_true, y_pred)
    pw = pairwise_auc(y_true, y_probs)
    mean_pw = round(float(np.nanmean(list(pw.values()))), 4)
    return {
        "accuracy": acc,
        "mae": mae,
        "kendall_tau_b": round(float(tau), 4),
        "kendall_tau_p": round(float(tau_p), 6),
        "pairwise_auc": pw,
        "mean_pairwise_auc": mean_pw,
    }


def main():
    parser = argparse.ArgumentParser(description="exp-013: Cross-model transfer matrix")
    parser.add_argument("--data_dirs", nargs="+", default=DEFAULT_DATA_DIRS,
                        help="Directories containing features.csv (one per model)")
    parser.add_argument("--labels", nargs="+", default=DEFAULT_LABELS,
                        help="Short labels for each model (same order as data_dirs)")
    parser.add_argument("--out_dir", default="/root/autodl-tmp/gen-depth-contamination/artifacts",
                        help="Output directory")
    parser.add_argument("--seed", type=int, default=SEED)
    args = parser.parse_args()

    assert len(args.data_dirs) == len(args.labels), \
        f"data_dirs ({len(args.data_dirs)}) and labels ({len(args.labels)}) must have same length"

    np.random.seed(args.seed)
    out_dir = Path(args.out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    n = len(args.labels)
    datasets = {}
    for label, ddir in zip(args.labels, args.data_dirs):
        path = Path(ddir) / "features.csv"
        print(f"Loading {label}: {path}")
        X, y, groups = load_features(path)
        print(f"  {X.shape[0]} samples, depths {y.min()}-{y.max()}")
        datasets[label] = (X, y, groups)

    matrix = {}
    for i, train_label in enumerate(args.labels):
        matrix[train_label] = {}
        for j, test_label in enumerate(args.labels):
            X_train, y_train, g_train = datasets[train_label]
            X_test, y_test, g_test = datasets[test_label]

            if i == j:
                print(f"\n[{train_label} → {test_label}] within-model {N_SPLITS}-fold CV")
                preds, probs = within_model_cv(X_train, y_train, g_train)
            else:
                print(f"\n[{train_label} → {test_label}] cross-model transfer")
                preds, probs = cross_model_transfer(X_train, y_train, X_test)

            metrics = evaluate(y_test, preds, probs)
            matrix[train_label][test_label] = metrics
            print(f"  acc={metrics['accuracy']:.4f}  MAE={metrics['mae']:.4f}  "
                  f"τ_b={metrics['kendall_tau_b']:.4f}  mAUC={metrics['mean_pairwise_auc']:.4f}")

    # Print formatted matrix
    labels = args.labels
    print(f"\n{'='*80}")
    print("Transfer Matrix — Accuracy (MAE)")
    print(f"{'='*80}")
    header = f"{'Train \\ Test':<16}" + "".join(f"{l:>18}" for l in labels)
    print(header)
    print("-" * len(header))
    for tl in labels:
        row = f"{tl:<16}"
        for el in labels:
            m = matrix[tl][el]
            cell = f"{m['accuracy']:.3f} ({m['mae']:.3f})"
            row += f"{cell:>18}"
        print(row)

    print(f"\nTransfer Matrix — Kendall τ_b")
    print("-" * len(header))
    header2 = f"{'Train \\ Test':<16}" + "".join(f"{l:>18}" for l in labels)
    print(header2)
    for tl in labels:
        row = f"{tl:<16}"
        for el in labels:
            m = matrix[tl][el]
            row += f"{m['kendall_tau_b']:>18.4f}"
        print(row)

    # Compute transfer retention
    print(f"\n{'='*80}")
    print("Transfer Retention (off-diag / diagonal)")
    print(f"{'='*80}")
    for tl in labels:
        diag_acc = matrix[tl][tl]["accuracy"]
        for el in labels:
            if tl == el:
                continue
            off_acc = matrix[tl][el]["accuracy"]
            retention = off_acc / diag_acc if diag_acc > 0 else 0
            print(f"  {tl} → {el}: {off_acc:.4f} / {diag_acc:.4f} = {retention:.1%} retention")

    # Save JSON
    json_path = out_dir / "cross_transfer_matrix.json"
    with open(json_path, "w") as f:
        json.dump({
            "matrix": matrix,
            "_meta": {
                "experiment": "exp-013",
                "description": "Cross-model transfer matrix for OBD depth classifiers",
                "models": labels,
                "method": "OBD-LightGBM",
                "n_splits_diagonal": N_SPLITS,
                "n_features": len(FEAT_COLS),
                "seed": args.seed,
            }
        }, f, indent=2)
    print(f"\nJSON saved: {json_path}")

    # Save CSV
    csv_path = out_dir / "cross_transfer_matrix.csv"
    with open(csv_path, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["train_model", "test_model", "accuracy", "mae",
                         "kendall_tau_b", "mean_pairwise_auc"])
        for tl in labels:
            for el in labels:
                m = matrix[tl][el]
                writer.writerow([tl, el, m["accuracy"], m["mae"],
                                 m["kendall_tau_b"], m["mean_pairwise_auc"]])
    print(f"CSV saved: {csv_path}")


if __name__ == "__main__":
    main()
