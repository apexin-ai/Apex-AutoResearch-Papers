"""
classify_and_eval.py — 3-class classification + statistical tests + Pass/Fail verdict.

Input: data/features.csv (from extract_features.py)
Output: results/mvp_results.json (skipped in dry-run mode)
Dependencies: pandas, numpy, scipy, sklearn, xgboost
"""

import argparse
import json
import sys
from pathlib import Path

import numpy as np
import pandas as pd
from scipy.stats import kruskal
from sklearn.metrics import (
    classification_report,
    confusion_matrix,
    f1_score,
)
from sklearn.model_selection import StratifiedKFold, cross_val_score, train_test_split
from xgboost import XGBClassifier


FEATURE_COLS = [
    "entropy_mean", "entropy_std", "entropy_min", "entropy_max",
    "tail_decay", "ttr", "hapax_ratio",
]


class NumpyEncoder(json.JSONEncoder):
    """Handle numpy types for JSON serialization."""
    def default(self, obj):
        if isinstance(obj, (np.bool_,)):
            return bool(obj)
        if isinstance(obj, (np.integer,)):
            return int(obj)
        if isinstance(obj, (np.floating,)):
            return float(obj)
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        return super().default(obj)


def assign_labels(df: pd.DataFrame) -> pd.DataFrame:
    """
    Map depth to 3-class labels: gen-0 (0), gen-1 (1), gen-2+ (2).
    Downsample gen-2+ to ~1000 (333 from each of depth 2,3,4).
    Balance classes to 1:1:1.
    """
    df = df.copy()
    df["label"] = df["depth"].apply(lambda d: 0 if d == 0 else (1 if d == 1 else 2))

    gen2plus = df[df["label"] == 2]
    sampled_parts = []
    for d in [2, 3, 4]:
        subset = gen2plus[gen2plus["depth"] == d]
        n_sample = min(333, len(subset))
        if n_sample > 0:
            sampled_parts.append(subset.sample(n=n_sample, random_state=42))
    gen2plus_sampled = pd.concat(sampled_parts, ignore_index=True) if sampled_parts else gen2plus

    gen0 = df[df["label"] == 0]
    gen1 = df[df["label"] == 1]
    min_size = min(len(gen0), len(gen1), len(gen2plus_sampled))

    balanced = pd.concat([
        gen0.sample(n=min_size, random_state=42),
        gen1.sample(n=min_size, random_state=42),
        gen2plus_sampled.sample(n=min(min_size, len(gen2plus_sampled)), random_state=42),
    ], ignore_index=True)

    print(f"Balanced dataset: {len(balanced)} samples, {balanced['label'].value_counts().to_dict()}")
    return balanced


def statistical_tests(df: pd.DataFrame) -> list[dict]:
    """Kruskal-Wallis test per feature across 3 groups, Bonferroni-corrected at alpha=0.05."""
    n_features = len(FEATURE_COLS)
    alpha_corrected = 0.05 / n_features
    results = []

    groups = [df[df["label"] == label] for label in [0, 1, 2]]

    for feat in FEATURE_COLS:
        group_vals = [g[feat].dropna().values for g in groups]
        if any(len(g) < 2 for g in group_vals):
            results.append({
                "feature": feat,
                "H_statistic": None,
                "p_value": None,
                "significant": False,
            })
            continue
        h_stat, p_val = kruskal(*group_vals)
        results.append({
            "feature": feat,
            "H_statistic": round(float(h_stat), 4),
            "p_value": float(p_val),
            "significant": p_val < alpha_corrected,
        })

    return results


def train_and_evaluate(df: pd.DataFrame) -> dict:
    """Train XGBoost 3-class classifier, return metrics including binary F1 for gen-0 vs gen-2+."""
    X = df[FEATURE_COLS].values
    y = df["label"].values

    n_samples = len(X)

    # Small datasets: train and evaluate on same data to avoid class-missing errors
    if n_samples < 15:
        X_train, X_test, y_train, y_test = X, X, y, y
        print("[WARN] Dataset too small for proper train/test split, using training data for evaluation")
    else:
        try:
            X_train, X_test, y_train, y_test = train_test_split(
                X, y, test_size=0.2, random_state=42, stratify=y,
            )
        except ValueError:
            X_train, X_test, y_train, y_test = train_test_split(
                X, y, test_size=0.2, random_state=42,
            )

    clf = XGBClassifier(
        n_estimators=200,
        max_depth=6,
        learning_rate=0.1,
        random_state=42,
        eval_metric="mlogloss",
        use_label_encoder=False,
    )

    # Adaptive CV folds based on data size
    train_counts = np.bincount(y_train)
    min_per_class = int(train_counts.min()) if len(train_counts) > 0 else 0
    n_splits = min(5, min_per_class)
    if n_splits >= 2:
        skf = StratifiedKFold(n_splits=n_splits, shuffle=True, random_state=42)
        cv_scores = cross_val_score(clf, X_train, y_train, cv=skf, scoring="f1_macro")
    else:
        print("[WARN] Too few samples for cross-validation, skipping CV")
        cv_scores = np.array([0.0])

    clf.fit(X_train, y_train)
    y_pred = clf.predict(X_test)

    macro_f1 = f1_score(y_test, y_pred, average="macro", zero_division=0)
    cm = confusion_matrix(y_test, y_pred).tolist()
    report = classification_report(y_test, y_pred, output_dict=True, zero_division=0)

    # Binary F1: gen-0 vs gen-2+
    mask_binary = np.isin(y_test, [0, 2])
    if mask_binary.sum() > 0:
        y_bin_true = (y_test[mask_binary] == 2).astype(int)
        y_bin_pred = (y_pred[mask_binary] == 2).astype(int)
        binary_f1 = f1_score(y_bin_true, y_bin_pred, zero_division=0)
    else:
        binary_f1 = 0.0

    per_class = {}
    for cls_label, cls_name in [(0, "gen-0"), (1, "gen-1"), (2, "gen-2+")]:
        key = str(cls_label)
        if key in report:
            per_class[cls_name] = {
                "precision": round(report[key]["precision"], 4),
                "recall": round(report[key]["recall"], 4),
                "f1-score": round(report[key]["f1-score"], 4),
            }

    importance = dict(zip(FEATURE_COLS, [round(float(x), 4) for x in clf.feature_importances_]))

    return {
        "cv_macro_f1_mean": round(float(cv_scores.mean()), 4),
        "cv_macro_f1_std": round(float(cv_scores.std()), 4),
        "test_macro_f1": round(macro_f1, 4),
        "binary_f1_gen0_vs_gen2plus": round(binary_f1, 4),
        "per_class_metrics": per_class,
        "confusion_matrix": cm,
        "feature_importance": importance,
    }


def main():
    parser = argparse.ArgumentParser(description="Classify and evaluate generation depth")
    parser.add_argument("--input", default="data/features.csv", help="Features CSV path")
    parser.add_argument("--output-dir", default="results", help="Output directory")
    parser.add_argument("--dry-run", action="store_true", help="Print results to stdout only, no file output")
    args = parser.parse_args()

    project_root = Path(__file__).resolve().parent
    input_path = project_root / args.input

    if not input_path.exists():
        print(f"ERROR: Input file not found: {input_path}")
        sys.exit(1)

    df = pd.read_csv(input_path)
    print(f"Loaded {len(df)} rows from {input_path}")

    balanced = assign_labels(df)

    # Statistical tests
    print("\n=== Statistical Tests (Kruskal-Wallis) ===")
    stat_results = statistical_tests(balanced)
    for r in stat_results:
        sig = "***" if r["significant"] else ""
        p_str = f"{r['p_value']:.2e}" if r["p_value"] is not None else "N/A"
        h_str = f"{r['H_statistic']:>10}" if r["H_statistic"] is not None else "       N/A"
        print(f"  {r['feature']:20s}  H={h_str}  p={p_str}  {sig}")

    # Classification
    print("\n=== XGBoost Classification ===")
    clf_results = train_and_evaluate(balanced)

    macro_f1 = clf_results["test_macro_f1"]
    binary_f1 = clf_results["binary_f1_gen0_vs_gen2plus"]

    print(f"\nTest macro-F1: {macro_f1:.4f}")
    print(f"Binary F1 (gen-0 vs gen-2+): {binary_f1:.4f}")
    print(f"\nPer-class metrics:")
    for cls, metrics in clf_results["per_class_metrics"].items():
        print(f"  {cls:8s}  P={metrics['precision']:.4f}  R={metrics['recall']:.4f}  F1={metrics['f1-score']:.4f}")
    print(f"\nConfusion matrix:")
    for row in clf_results["confusion_matrix"]:
        print(f"  {row}")
    print(f"\nFeature importance:")
    for feat, imp in sorted(clf_results["feature_importance"].items(), key=lambda x: -x[1]):
        print(f"  {feat:20s}  {imp:.4f}")

    # Verdict: binary PASS/FAIL only (no MARGINAL)
    verdict = "PASS" if (macro_f1 >= 0.45 and binary_f1 >= 0.65) else "FAIL"

    any_significant = any(r["significant"] for r in stat_results)
    print(f"\n=== Verdict: {verdict} ===")
    print(f"  macro-F1 >= 0.45: {'YES' if macro_f1 >= 0.45 else 'NO'} ({macro_f1:.4f})")
    print(f"  binary F1 >= 0.65: {'YES' if binary_f1 >= 0.65 else 'NO'} ({binary_f1:.4f})")
    print(f"  Any feature significant: {'YES' if any_significant else 'NO'}")

    # Save results (skip in dry-run)
    if args.dry_run:
        print("\n[dry-run] Results printed to stdout only, no file written.")
        return

    output_dir = project_root / args.output_dir
    output_dir.mkdir(parents=True, exist_ok=True)
    output_path = output_dir / "mvp_results.json"

    final = {
        "verdict": verdict,
        "test_macro_f1": clf_results["test_macro_f1"],
        "binary_f1_gen0_vs_gen2plus": clf_results["binary_f1_gen0_vs_gen2plus"],
        "cv_macro_f1_mean": clf_results["cv_macro_f1_mean"],
        "cv_macro_f1_std": clf_results["cv_macro_f1_std"],
        "per_class_metrics": clf_results["per_class_metrics"],
        "confusion_matrix": clf_results["confusion_matrix"],
        "feature_importance": clf_results["feature_importance"],
        "feature_significance": stat_results,
    }

    with open(output_path, "w") as f:
        json.dump(final, f, indent=2, cls=NumpyEncoder)
    print(f"\nResults saved to {output_path}")


if __name__ == "__main__":
    main()
