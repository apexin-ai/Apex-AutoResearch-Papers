"""
Baseline: Perplexity Regression for recursive generation depth estimation.

Uses perplexity-related statistical features to predict recursion depth via
regression (Ridge) and ordinal logistic regression.

Two feature modes:
  (a) PPL-only: 5 perplexity features (mean_ppl, var_ppl, p50_ppl, p75_ppl, p90_ppl)
  (b) Full: all 19 statistical features

Evaluates both 4-class (depth 0-3) and 3-class (depth 1-3, generated text only).

Input:  Pre-extracted features JSONL (--features_path), each line has 19 features + depth label
Output: {method}_classification_report.json, {method}_pairwise_auc.json, {method}_predictions.json

Dependencies: numpy, scikit-learn

Usage:
  python baseline_perplexity_regression.py --features_path data/features_all.jsonl
  python baseline_perplexity_regression.py --features_path data/features_all.jsonl --mode ridge
  python baseline_perplexity_regression.py --features_path data/features_all.jsonl --mode ordinal --feature_set full
"""

import argparse
import json
import os
import numpy as np
from collections import Counter

from sklearn.linear_model import Ridge, LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report, roc_auc_score

NUM_DEPTHS = 4
DEPTH_LABELS = list(range(NUM_DEPTHS))

FEATURE_NAMES = [
    "mean_ppl", "var_ppl", "skewness_ppl", "kurtosis_ppl",
    "p10_ppl", "p25_ppl", "p50_ppl", "p75_ppl", "p90_ppl",
    "mean_surprisal", "var_surprisal", "entropy_of_surprisal",
    "type_token_ratio", "hapax_ratio", "bigram_entropy", "trigram_entropy",
    "rep_2gram", "rep_3gram", "rep_4gram",
]

PPL_FEATURES = ["mean_ppl", "var_ppl", "p50_ppl", "p75_ppl", "p90_ppl"]
PPL_INDICES = [FEATURE_NAMES.index(f) for f in PPL_FEATURES]


def load_features(path):
    records = []
    with open(path) as f:
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


def stratified_split(labels, eval_split=0.15, seed=42):
    train_idx, eval_idx = train_test_split(
        np.arange(len(labels)), test_size=eval_split,
        stratify=labels, random_state=seed,
    )
    return train_idx, eval_idx


def pairwise_auc(y_true, y_prob, d1, d2):
    mask = np.isin(y_true, [d1, d2])
    if mask.sum() < 2:
        return None
    yt = (y_true[mask] == d2).astype(int)
    if len(np.unique(yt)) < 2:
        return None
    yp = y_prob[mask, d2]
    return float(roc_auc_score(yt, yp))


def compute_all_pairwise_auc(y_true, y_prob, depth_labels):
    result = {}
    for i, d1 in enumerate(depth_labels):
        for d2 in depth_labels[i + 1:]:
            auc = pairwise_auc(y_true, y_prob, d1, d2)
            result[f"d{d1}_vs_d{d2}"] = round(auc, 4) if auc is not None else None
    return result


def bootstrap_ci(y_true, y_pred, n_boot=1000, seed=42):
    rng = np.random.RandomState(seed)
    scores = []
    n = len(y_true)
    for _ in range(n_boot):
        idx = rng.choice(n, n, replace=True)
        scores.append(accuracy_score(y_true[idx], y_pred[idx]))
    return float(np.percentile(scores, 2.5)), float(np.percentile(scores, 97.5))


def evaluate_and_save(method_name, y_true, y_pred, y_prob, output_dir):
    os.makedirs(output_dir, exist_ok=True)
    y_true = np.asarray(y_true)
    y_pred = np.asarray(y_pred)

    acc4 = accuracy_score(y_true, y_pred)
    ci_lo, ci_hi = bootstrap_ci(y_true, y_pred)
    mae = float(np.mean(np.abs(y_true - y_pred)))

    mask_gen = y_true >= 1
    acc3 = accuracy_score(y_true[mask_gen], y_pred[mask_gen]) if mask_gen.sum() > 0 else 0.0

    pair_aucs_4 = compute_all_pairwise_auc(y_true, y_prob, DEPTH_LABELS) if y_prob is not None else {}
    pair_aucs_3 = compute_all_pairwise_auc(
        y_true[mask_gen], y_prob[mask_gen], [1, 2, 3]
    ) if y_prob is not None and mask_gen.sum() > 0 else {}

    cr_4class = classification_report(
        y_true, y_pred,
        target_names=[f"d{d}" for d in DEPTH_LABELS],
        output_dict=True, zero_division=0,
    )
    cr_3class = {}
    if mask_gen.sum() > 0:
        cr_3class = classification_report(
            y_true[mask_gen], y_pred[mask_gen],
            labels=[1, 2, 3],
            target_names=["d1", "d2", "d3"],
            output_dict=True, zero_division=0,
        )

    print(f"\n{'=' * 60}")
    print(f"  {method_name}")
    print(f"{'=' * 60}")
    print(f"  4-class accuracy : {acc4:.4f}  (95% CI: [{ci_lo:.4f}, {ci_hi:.4f}])")
    print(f"  3-class accuracy : {acc3:.4f}  (d1-d3 only)")
    print(f"  MAE              : {mae:.4f}")
    print(f"  4-class AUC      : {pair_aucs_4}")
    print(f"  3-class AUC      : {pair_aucs_3}")
    print(classification_report(
        y_true, y_pred,
        target_names=[f"d{d}" for d in DEPTH_LABELS], zero_division=0,
    ))

    report = {
        "accuracy_4class": round(acc4, 4),
        "accuracy_4class_ci": [round(ci_lo, 4), round(ci_hi, 4)],
        "accuracy_3class": round(acc3, 4),
        "mae": round(mae, 4),
        "pairwise_auc_4class": pair_aucs_4,
        "pairwise_auc_3class": pair_aucs_3,
        "per_class_4class": cr_4class,
        "per_class_3class": cr_3class,
    }
    _save_json(os.path.join(output_dir, f"{method_name}_classification_report.json"), report)
    _save_json(os.path.join(output_dir, f"{method_name}_pairwise_auc.json"),
               {"4class": pair_aucs_4, "3class": pair_aucs_3})

    preds = []
    for i in range(len(y_true)):
        entry = {"y_true": int(y_true[i]), "y_pred": int(y_pred[i])}
        if y_prob is not None:
            entry["y_prob"] = [round(float(p), 6) for p in y_prob[i]]
        preds.append(entry)
    _save_json(os.path.join(output_dir, f"{method_name}_predictions.json"), preds)

    print(f"  Saved to {output_dir}/")
    return {"accuracy_4class": acc4, "accuracy_3class": acc3, "mae": mae}


def _save_json(path, obj):
    with open(path, "w") as f:
        json.dump(obj, f, indent=2)


class RidgePPLRegressor:
    """Ridge regression on PPL features → round to nearest depth."""

    def __init__(self, feature_indices, alpha=1.0):
        self.feature_indices = feature_indices
        self.scaler = StandardScaler()
        self.model = Ridge(alpha=alpha)

    def fit(self, X, y):
        Xs = self.scaler.fit_transform(X[:, self.feature_indices])
        self.model.fit(Xs, y.astype(np.float64))

    def predict(self, X):
        Xs = self.scaler.transform(X[:, self.feature_indices])
        raw = self.model.predict(Xs)
        return np.clip(np.round(raw).astype(int), 0, NUM_DEPTHS - 1)

    def predict_proba(self, X):
        Xs = self.scaler.transform(X[:, self.feature_indices])
        raw = self.model.predict(Xs)
        preds = np.clip(np.round(raw).astype(int), 0, NUM_DEPTHS - 1)
        residuals = np.abs(raw - preds)
        prob = np.zeros((len(preds), NUM_DEPTHS))
        for i, (p, r) in enumerate(zip(preds, residuals)):
            confidence = max(0.5, 1.0 - r)
            prob[i, p] = confidence
            remaining = (1.0 - confidence) / max(NUM_DEPTHS - 1, 1)
            for d in range(NUM_DEPTHS):
                if d != p:
                    prob[i, d] = remaining
        return prob


class OrdinalLogisticRegressor:
    """
    Ordinal Logistic Regression (cumulative model).
    K-1 binary logistic regressions: P(depth >= k) for k=1..K-1.
    """

    def __init__(self, feature_indices, C=1.0):
        self.feature_indices = feature_indices
        self.scaler = StandardScaler()
        self.models = []

    def fit(self, X, y):
        Xs = self.scaler.fit_transform(X[:, self.feature_indices])
        self.models = []
        for k in range(1, NUM_DEPTHS):
            binary_y = (y >= k).astype(int)
            clf = LogisticRegression(max_iter=1000, C=1.0)
            clf.fit(Xs, binary_y)
            self.models.append(clf)

    def predict_proba(self, X):
        Xs = self.scaler.transform(X[:, self.feature_indices])
        cum_probs = np.column_stack([
            m.predict_proba(Xs)[:, 1] for m in self.models
        ])
        probs = np.zeros((len(X), NUM_DEPTHS))
        probs[:, 0] = 1.0 - cum_probs[:, 0]
        for k in range(1, NUM_DEPTHS - 1):
            probs[:, k] = cum_probs[:, k - 1] - cum_probs[:, k]
        probs[:, NUM_DEPTHS - 1] = cum_probs[:, NUM_DEPTHS - 2]
        probs = np.clip(probs, 0, 1)
        row_sums = probs.sum(axis=1, keepdims=True)
        probs = probs / np.where(row_sums > 0, row_sums, 1.0)
        return probs

    def predict(self, X):
        return self.predict_proba(X).argmax(axis=1)


def main():
    parser = argparse.ArgumentParser(description="Perplexity Regression baseline")
    parser.add_argument("--features_path", required=True)
    parser.add_argument("--output_dir", default="results/baselines/")
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--eval_split", type=float, default=0.15)
    parser.add_argument("--mode", choices=["ridge", "ordinal", "both"], default="both")
    parser.add_argument("--feature_set", choices=["ppl", "full", "both"], default="both",
                        help="ppl=5 PPL features, full=all 19 features")
    parser.add_argument("--alpha", type=float, default=1.0, help="Ridge regularization")
    args = parser.parse_args()

    X, y = load_features(args.features_path)
    train_idx, eval_idx = stratified_split(y, eval_split=args.eval_split, seed=args.seed)
    X_train, y_train = X[train_idx], y[train_idx]
    X_eval, y_eval = X[eval_idx], y[eval_idx]
    print(f"Train: {len(y_train)}, Eval: {len(y_eval)}")

    modes = ["ridge", "ordinal"] if args.mode == "both" else [args.mode]
    feature_sets = ["ppl", "full"] if args.feature_set == "both" else [args.feature_set]

    ALL_INDICES = list(range(len(FEATURE_NAMES)))

    for fset in feature_sets:
        indices = PPL_INDICES if fset == "ppl" else ALL_INDICES
        feat_tag = "ppl5" if fset == "ppl" else "full19"

        for mode in modes:
            method_name = f"ppl_regression_{mode}_{feat_tag}"
            print(f"\n>>> {method_name} ({len(indices)} features)")

            if mode == "ridge":
                model = RidgePPLRegressor(indices, alpha=args.alpha)
            else:
                model = OrdinalLogisticRegressor(indices)

            model.fit(X_train, y_train)
            y_pred = model.predict(X_eval)
            y_prob = model.predict_proba(X_eval)
            evaluate_and_save(method_name, y_eval, y_pred, y_prob, args.output_dir)


if __name__ == "__main__":
    main()
