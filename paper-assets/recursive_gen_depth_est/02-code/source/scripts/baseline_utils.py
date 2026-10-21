"""
Shared utilities for baseline battery experiments.

Provides: data loading (raw JSONL + pre-extracted features), stratified splitting,
evaluation metrics (accuracy, MAE, pairwise AUC, classification report), and
standardized output saving.
"""

import json
import os
import glob as glob_mod
import numpy as np
from collections import Counter
from sklearn.model_selection import train_test_split
from sklearn.metrics import (
    accuracy_score, classification_report, confusion_matrix, roc_auc_score,
)

NUM_DEPTHS = 4
DEPTH_LABELS = list(range(NUM_DEPTHS))

FEATURE_NAMES = [
    "mean_ppl", "var_ppl", "skewness_ppl", "kurtosis_ppl",
    "p10_ppl", "p25_ppl", "p50_ppl", "p75_ppl", "p90_ppl",
    "mean_surprisal", "var_surprisal", "entropy_of_surprisal",
    "type_token_ratio", "hapax_ratio", "bigram_entropy", "trigram_entropy",
    "rep_2gram", "rep_3gram", "rep_4gram",
]
NUM_FEATURES = len(FEATURE_NAMES)


# ── Data loading ──

def load_jsonl_data(data_dirs, max_samples=0, seed=42):
    """Load raw text + depth labels from depth_*.jsonl files across directories."""
    texts, labels = [], []
    for data_dir in data_dirs:
        for d in range(NUM_DEPTHS):
            fpath = os.path.join(data_dir, f"depth_{d}.jsonl")
            if not os.path.exists(fpath):
                matches = glob_mod.glob(os.path.join(data_dir, f"*depth_{d}*.jsonl"))
                fpath = matches[0] if matches else None
            if fpath is None or not os.path.exists(fpath):
                continue
            with open(fpath) as f:
                for line in f:
                    line = line.strip()
                    if not line:
                        continue
                    rec = json.loads(line)
                    texts.append(rec["text"])
                    labels.append(rec.get("depth", d))
    labels = np.array(labels, dtype=np.int64)
    if max_samples > 0 and len(texts) > max_samples:
        rng = np.random.RandomState(seed)
        idx = sorted(rng.choice(len(texts), max_samples, replace=False))
        texts = [texts[i] for i in idx]
        labels = labels[idx]
    print(f"Loaded {len(texts)} samples. Depth distribution: {dict(Counter(labels))}")
    return texts, labels


def load_features(features_path):
    """Load pre-extracted 19-dim features from JSONL → (X [n, 19], y [n])."""
    records = []
    with open(features_path) as f:
        for line in f:
            line = line.strip()
            if line:
                records.append(json.loads(line))
    X = np.array([[r[k] for k in FEATURE_NAMES] for r in records], dtype=np.float64)
    y = np.array([r["depth"] for r in records], dtype=np.int64)
    X = np.nan_to_num(X, nan=0.0, posinf=0.0, neginf=0.0)
    print(f"Loaded features: {X.shape[0]} samples, {X.shape[1]} dims. "
          f"Depth distribution: {dict(Counter(y))}")
    return X, y


# ── Splitting ──

def stratified_split(labels, eval_split=0.1, seed=42):
    """Return (train_idx, eval_idx) arrays with stratification."""
    train_idx, eval_idx = train_test_split(
        np.arange(len(labels)), test_size=eval_split,
        stratify=labels, random_state=seed,
    )
    return train_idx, eval_idx


# ── Evaluation ──

def _pairwise_auc(y_true, y_prob, d1, d2):
    mask = np.isin(y_true, [d1, d2])
    if mask.sum() < 2:
        return None
    yt = (y_true[mask] == d2).astype(int)
    if len(np.unique(yt)) < 2:
        return None
    yp = y_prob[mask, d2]
    return float(roc_auc_score(yt, yp))


def compute_all_pairwise_auc(y_true, y_prob):
    result = {}
    for i, d1 in enumerate(DEPTH_LABELS):
        for d2 in DEPTH_LABELS[i + 1:]:
            auc = _pairwise_auc(y_true, y_prob, d1, d2)
            result[f"d{d1}_vs_d{d2}"] = round(auc, 4) if auc is not None else None
    return result


def evaluate_and_save(method_name, y_true, y_pred, y_prob, output_dir):
    """Compute all metrics, print summary, save three output files."""
    os.makedirs(output_dir, exist_ok=True)
    y_true = np.asarray(y_true)
    y_pred = np.asarray(y_pred)

    acc = accuracy_score(y_true, y_pred)
    mae = float(np.mean(np.abs(y_true - y_pred)))
    cr_dict = classification_report(
        y_true, y_pred,
        target_names=[f"d{d}" for d in DEPTH_LABELS],
        output_dict=True, zero_division=0,
    )
    pair_aucs = compute_all_pairwise_auc(y_true, y_prob) if y_prob is not None else {}

    print(f"\n{'=' * 50}")
    print(f"  {method_name}")
    print(f"{'=' * 50}")
    print(f"  Accuracy: {acc:.4f}   MAE: {mae:.4f}")
    if pair_aucs:
        print(f"  Pairwise AUC: {pair_aucs}")
    print(classification_report(
        y_true, y_pred,
        target_names=[f"d{d}" for d in DEPTH_LABELS], zero_division=0,
    ))

    # 1) classification report
    report = {"accuracy": round(acc, 4), "mae": round(mae, 4), "per_class": cr_dict}
    _save_json(os.path.join(output_dir, f"{method_name}_classification_report.json"), report)

    # 2) pairwise AUC
    _save_json(os.path.join(output_dir, f"{method_name}_pairwise_auc.json"), pair_aucs)

    # 3) predictions
    preds = []
    for i in range(len(y_true)):
        entry = {"y_true": int(y_true[i]), "y_pred": int(y_pred[i])}
        if y_prob is not None:
            entry["y_prob"] = [round(float(p), 6) for p in y_prob[i]]
        preds.append(entry)
    _save_json(os.path.join(output_dir, f"{method_name}_predictions.json"), preds)

    print(f"  Saved to {output_dir}/")
    return {"accuracy": acc, "mae": mae, "pairwise_auc": pair_aucs}


def _save_json(path, obj):
    with open(path, "w") as f:
        json.dump(obj, f, indent=2)


def add_common_args(parser):
    """Add the unified CLI arguments shared across all baselines."""
    parser.add_argument("--data_dirs", nargs="+", default=["data/"],
                        help="Directories containing depth_*.jsonl files")
    parser.add_argument("--features_path", default=None,
                        help="Path to pre-extracted features JSONL (for feature-based methods)")
    parser.add_argument("--output_dir", default="results/baselines/")
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--eval_split", type=float, default=0.1)
    parser.add_argument("--max_seq_len", type=int, default=512)
    parser.add_argument("--max_samples", type=int, default=0,
                        help="Max total samples to use (0 = all)")
