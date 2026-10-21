"""
Baseline 1: DivEye Binary → Ordinal for recursive generation depth estimation.

Adapts DivEye (Basani & Chen, TMLR 2026) from binary human-vs-AI detection to
ordinal depth classification. DivEye's core insight: AI-generated text has lower
surprisal diversity than human text; deeper recursion should further reduce diversity.

Method:
  - Extract DivEye-style diversity features (surprisal variance, entropy, lexical
    diversity, repetition) from pre-computed 19-dim feature vectors
  - Train One-vs-Rest (OVR) classifiers: one binary classifier per depth
  - Predict depth = argmax(OVR decision scores)

Ref: Basani, A. R. & Chen, P.-Y. (2026). "Diversity Boosts AI-Generated Text
     Detection." TMLR. GitHub: https://github.com/IBM/diveye

Input:  Pre-extracted features JSONL (--features_path)
Output: {method}_classification_report.json, {method}_pairwise_auc.json, {method}_predictions.json

Usage:
  python baseline_diveye_ordinal.py --features_path data/features_all.jsonl
  python baseline_diveye_ordinal.py --features_path data/features_all.jsonl --base_clf svm
"""

import argparse
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.multiclass import OneVsRestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.calibration import CalibratedClassifierCV

from baseline_utils import (
    load_features, stratified_split, evaluate_and_save,
    add_common_args, NUM_DEPTHS, FEATURE_NAMES,
)

# DivEye feature subset: surprisal distributional + lexical diversity + repetition
DIVEYE_FEATURES = [
    "mean_ppl", "var_ppl", "skewness_ppl", "kurtosis_ppl",
    "mean_surprisal", "var_surprisal", "entropy_of_surprisal",
    "type_token_ratio", "hapax_ratio", "bigram_entropy", "trigram_entropy",
    "rep_2gram", "rep_3gram", "rep_4gram",
]
DIVEYE_INDICES = [FEATURE_NAMES.index(f) for f in DIVEYE_FEATURES]


class DivEyeOrdinal:
    """OVR classifier on DivEye diversity features for ordinal depth prediction."""

    def __init__(self, base_clf="logistic", C=1.0, seed=42):
        self.scaler = StandardScaler()
        self.seed = seed
        if base_clf == "logistic":
            estimator = LogisticRegression(
                C=C, max_iter=1000, random_state=seed,
            )
        elif base_clf == "svm":
            estimator = CalibratedClassifierCV(
                SVC(C=C, kernel="rbf", random_state=seed),
                cv=3,
            )
        else:
            raise ValueError(f"Unknown base_clf: {base_clf}")
        self.ovr = OneVsRestClassifier(estimator)

    def fit(self, X, y):
        Xd = self.scaler.fit_transform(X[:, DIVEYE_INDICES])
        self.ovr.fit(Xd, y)

    def predict(self, X):
        Xd = self.scaler.transform(X[:, DIVEYE_INDICES])
        return self.ovr.predict(Xd)

    def predict_proba(self, X):
        Xd = self.scaler.transform(X[:, DIVEYE_INDICES])
        if hasattr(self.ovr, "predict_proba"):
            probs = self.ovr.predict_proba(Xd)
        else:
            scores = self.ovr.decision_function(Xd)
            from scipy.special import softmax
            probs = softmax(scores, axis=1)
        if probs.shape[1] < NUM_DEPTHS:
            full = np.zeros((probs.shape[0], NUM_DEPTHS))
            for i, c in enumerate(self.ovr.classes_):
                full[:, c] = probs[:, i]
            return full
        return probs


def main():
    parser = argparse.ArgumentParser(description="DivEye Binary→Ordinal baseline")
    add_common_args(parser)
    parser.add_argument("--base_clf", choices=["logistic", "svm"], default="logistic")
    parser.add_argument("--C", type=float, default=1.0, help="Regularization strength")
    args = parser.parse_args()

    if args.features_path is None:
        print("ERROR: --features_path is required for DivEye baseline.")
        print("Run extract_features.py first to generate features JSONL.")
        return

    X, y = load_features(args.features_path)
    train_idx, eval_idx = stratified_split(y, eval_split=args.eval_split, seed=args.seed)
    X_train, y_train = X[train_idx], y[train_idx]
    X_eval, y_eval = X[eval_idx], y[eval_idx]
    print(f"Train: {len(y_train)}, Eval: {len(y_eval)}")

    method_name = f"diveye_ovr_{args.base_clf}"
    model = DivEyeOrdinal(base_clf=args.base_clf, C=args.C, seed=args.seed)
    model.fit(X_train, y_train)
    y_pred = model.predict(X_eval)
    y_prob = model.predict_proba(X_eval)
    evaluate_and_save(method_name, y_eval, y_pred, y_prob, args.output_dir)


if __name__ == "__main__":
    main()
