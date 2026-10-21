"""
Baseline 2: Perplexity-only Regression for recursive generation depth estimation.

Simplest baseline — uses only perplexity statistics (mean_ppl, p75_ppl, p90_ppl)
to predict recursion depth via:
  (a) Ridge Regression → round to nearest integer depth
  (b) Ordinal Logistic Regression (cumulative link model)

If PPL alone separates depths well, more complex methods add no value.

Input:  Pre-extracted features JSONL (--features_path) or raw depth_*.jsonl (--data_dirs)
Output: {method}_classification_report.json, {method}_pairwise_auc.json, {method}_predictions.json

Usage:
  python baseline_ppl_regression.py --features_path data/features_all.jsonl
  python baseline_ppl_regression.py --features_path data/features_all.jsonl --mode ordinal
"""

import argparse
import numpy as np
from sklearn.linear_model import Ridge
from sklearn.preprocessing import StandardScaler

from baseline_utils import (
    load_features, stratified_split, evaluate_and_save,
    add_common_args, NUM_DEPTHS, FEATURE_NAMES,
)

PPL_FEATURES = ["mean_ppl", "p75_ppl", "p90_ppl"]
PPL_INDICES = [FEATURE_NAMES.index(f) for f in PPL_FEATURES]


class RidgePPLRegressor:
    """Ridge regression on 3 PPL features → round to nearest depth."""

    def __init__(self, alpha=1.0):
        self.scaler = StandardScaler()
        self.model = Ridge(alpha=alpha)

    def fit(self, X, y):
        Xs = self.scaler.fit_transform(X[:, PPL_INDICES])
        self.model.fit(Xs, y.astype(np.float64))

    def predict(self, X):
        Xs = self.scaler.transform(X[:, PPL_INDICES])
        raw = self.model.predict(Xs)
        return np.clip(np.round(raw).astype(int), 0, NUM_DEPTHS - 1)

    def predict_proba(self, X):
        preds = self.predict(X)
        prob = np.zeros((len(preds), NUM_DEPTHS))
        for i, p in enumerate(preds):
            prob[i, p] = 1.0
        return prob


class OrdinalLogisticPPL:
    """
    Ordinal Logistic Regression (cumulative model) on 3 PPL features.

    Uses K-1 binary logistic regressions: P(depth >= k) for k=1..K-1.
    Falls back to sklearn LogisticRegression if mord is unavailable.
    """

    def __init__(self):
        self.scaler = StandardScaler()
        self.models = []

    def fit(self, X, y):
        Xs = self.scaler.fit_transform(X[:, PPL_INDICES])
        from sklearn.linear_model import LogisticRegression
        self.models = []
        for k in range(1, NUM_DEPTHS):
            binary_y = (y >= k).astype(int)
            clf = LogisticRegression(max_iter=1000, C=1.0)
            clf.fit(Xs, binary_y)
            self.models.append(clf)

    def predict_proba(self, X):
        Xs = self.scaler.transform(X[:, PPL_INDICES])
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
    parser = argparse.ArgumentParser(description="Perplexity-only Regression baseline")
    add_common_args(parser)
    parser.add_argument("--mode", choices=["ridge", "ordinal", "both"], default="both")
    parser.add_argument("--alpha", type=float, default=1.0, help="Ridge regularization")
    args = parser.parse_args()

    if args.features_path is None:
        print("ERROR: --features_path is required for PPL regression baseline.")
        print("Run extract_features.py first to generate features JSONL.")
        return

    X, y = load_features(args.features_path)
    train_idx, eval_idx = stratified_split(y, eval_split=args.eval_split, seed=args.seed)
    X_train, y_train = X[train_idx], y[train_idx]
    X_eval, y_eval = X[eval_idx], y[eval_idx]
    print(f"Train: {len(y_train)}, Eval: {len(y_eval)}")

    modes = ["ridge", "ordinal"] if args.mode == "both" else [args.mode]

    for mode in modes:
        method_name = f"ppl_{mode}"
        if mode == "ridge":
            model = RidgePPLRegressor(alpha=args.alpha)
        else:
            model = OrdinalLogisticPPL()

        model.fit(X_train, y_train)
        y_pred = model.predict(X_eval)
        y_prob = model.predict_proba(X_eval)
        evaluate_and_save(method_name, y_eval, y_pred, y_prob, args.output_dir)


if __name__ == "__main__":
    main()
