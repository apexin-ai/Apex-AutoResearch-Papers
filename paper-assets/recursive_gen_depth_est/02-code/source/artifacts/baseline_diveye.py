"""
Baseline: DivEye for recursive generation depth estimation.

Adapts DivEye (Basani & Chen, TMLR 2026) from binary human-vs-AI detection to
ordinal depth classification. DivEye's insight: AI-generated text has lower
surprisal diversity than human text; deeper recursion further reduces diversity.

Feature subsets:
  - DivEye-core (4 features): type_token_ratio, hapax_ratio, bigram_entropy, trigram_entropy
  - DivEye-extended (14 features): all diversity-related features (surprisal distribution,
    lexical diversity, repetition patterns)

Classifiers: RandomForest, LogisticRegression (OVR)

Evaluates both 4-class (depth 0-3) and 3-class (depth 1-3, generated text only).

Input:  Pre-extracted features JSONL (--features_path), each line has 19 features + depth label
Output: {method}_classification_report.json, {method}_pairwise_auc.json, {method}_predictions.json

Dependencies: numpy, scikit-learn

Usage:
  python baseline_diveye.py --features_path data/features_all.jsonl
  python baseline_diveye.py --features_path data/features_all.jsonl --clf rf
  python baseline_diveye.py --features_path data/features_all.jsonl --clf logistic --feature_set extended
"""

import argparse
import json
import os
import numpy as np
from collections import Counter

from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
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

DIVEYE_CORE_FEATURES = [
    "type_token_ratio", "hapax_ratio", "bigram_entropy", "trigram_entropy",
]

DIVEYE_EXTENDED_FEATURES = [
    "mean_ppl", "var_ppl", "skewness_ppl", "kurtosis_ppl",
    "mean_surprisal", "var_surprisal", "entropy_of_surprisal",
    "type_token_ratio", "hapax_ratio", "bigram_entropy", "trigram_entropy",
    "rep_2gram", "rep_3gram", "rep_4gram",
]

DIVEYE_CORE_INDICES = [FEATURE_NAMES.index(f) for f in DIVEYE_CORE_FEATURES]
DIVEYE_EXTENDED_INDICES = [FEATURE_NAMES.index(f) for f in DIVEYE_EXTENDED_FEATURES]


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


class DivEyeRandomForest:
    """RandomForest classifier on DivEye feature subset."""

    def __init__(self, feature_indices, n_estimators=200, max_depth=None, seed=42):
        self.feature_indices = feature_indices
        self.model = RandomForestClassifier(
            n_estimators=n_estimators,
            max_depth=max_depth,
            random_state=seed,
            n_jobs=-1,
        )

    def fit(self, X, y):
        self.model.fit(X[:, self.feature_indices], y)

    def predict(self, X):
        return self.model.predict(X[:, self.feature_indices])

    def predict_proba(self, X):
        probs = self.model.predict_proba(X[:, self.feature_indices])
        if probs.shape[1] < NUM_DEPTHS:
            full = np.zeros((probs.shape[0], NUM_DEPTHS))
            for i, c in enumerate(self.model.classes_):
                full[:, c] = probs[:, i]
            return full
        return probs

    def feature_importances(self):
        return dict(zip(
            [FEATURE_NAMES[i] for i in self.feature_indices],
            self.model.feature_importances_,
        ))


class DivEyeLogistic:
    """Logistic Regression (OVR) on DivEye feature subset with standardization."""

    def __init__(self, feature_indices, C=1.0, seed=42):
        self.feature_indices = feature_indices
        self.scaler = StandardScaler()
        self.model = LogisticRegression(
            C=C, max_iter=1000, multi_class="ovr",
            random_state=seed,
        )

    def fit(self, X, y):
        Xs = self.scaler.fit_transform(X[:, self.feature_indices])
        self.model.fit(Xs, y)

    def predict(self, X):
        Xs = self.scaler.transform(X[:, self.feature_indices])
        return self.model.predict(Xs)

    def predict_proba(self, X):
        Xs = self.scaler.transform(X[:, self.feature_indices])
        probs = self.model.predict_proba(Xs)
        if probs.shape[1] < NUM_DEPTHS:
            full = np.zeros((probs.shape[0], NUM_DEPTHS))
            for i, c in enumerate(self.model.classes_):
                full[:, c] = probs[:, i]
            return full
        return probs


def main():
    parser = argparse.ArgumentParser(description="DivEye baseline for depth estimation")
    parser.add_argument("--features_path", required=True)
    parser.add_argument("--output_dir", default="results/baselines/")
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--eval_split", type=float, default=0.15)
    parser.add_argument("--clf", choices=["rf", "logistic", "both"], default="both")
    parser.add_argument("--feature_set", choices=["core", "extended", "both"], default="both",
                        help="core=4 diversity features, extended=14 DivEye features")
    parser.add_argument("--n_estimators", type=int, default=200)
    parser.add_argument("--C", type=float, default=1.0, help="Logistic regularization")
    args = parser.parse_args()

    X, y = load_features(args.features_path)
    train_idx, eval_idx = stratified_split(y, eval_split=args.eval_split, seed=args.seed)
    X_train, y_train = X[train_idx], y[train_idx]
    X_eval, y_eval = X[eval_idx], y[eval_idx]
    print(f"Train: {len(y_train)}, Eval: {len(y_eval)}")

    clfs = ["rf", "logistic"] if args.clf == "both" else [args.clf]
    feature_sets = ["core", "extended"] if args.feature_set == "both" else [args.feature_set]

    for fset in feature_sets:
        indices = DIVEYE_CORE_INDICES if fset == "core" else DIVEYE_EXTENDED_INDICES
        feat_tag = f"core{len(indices)}" if fset == "core" else f"ext{len(indices)}"

        for clf_name in clfs:
            method_name = f"diveye_{clf_name}_{feat_tag}"
            print(f"\n>>> {method_name} ({len(indices)} features)")

            if clf_name == "rf":
                model = DivEyeRandomForest(
                    indices, n_estimators=args.n_estimators, seed=args.seed,
                )
            else:
                model = DivEyeLogistic(indices, C=args.C, seed=args.seed)

            model.fit(X_train, y_train)
            y_pred = model.predict(X_eval)
            y_prob = model.predict_proba(X_eval)
            result = evaluate_and_save(method_name, y_eval, y_pred, y_prob, args.output_dir)

            if clf_name == "rf" and hasattr(model, "feature_importances"):
                importances = model.feature_importances()
                sorted_imp = sorted(importances.items(), key=lambda x: -x[1])
                print(f"  Feature importances: {sorted_imp[:5]}")


if __name__ == "__main__":
    main()
