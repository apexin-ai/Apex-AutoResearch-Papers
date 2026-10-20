"""
classify_multi.py — Multi-generator depth classification with leave-one-out CV.

Input:  data/features_all.csv (model_name, seed_id, depth, [features...])
Output: results/multi_classify_results.json
        results/multi_classify_results.csv

Evaluations:
  1. Leave-one-generator-out CV (5-fold): train on 4 generators, test on held-out
  2. Leave-one-family-out CV: hold out all Pythia models vs non-Pythia
  3. Pooled stratified 5-fold CV as baseline

Dependencies: pandas, numpy, scikit-learn, xgboost
"""

import argparse
import json
import sys
from collections import defaultdict
from pathlib import Path

import numpy as np
import pandas as pd
from sklearn.metrics import (
    classification_report,
    confusion_matrix,
    f1_score,
    accuracy_score,
)
from sklearn.model_selection import StratifiedKFold
from xgboost import XGBClassifier


FEATURE_COLS = [
    "entropy_mean", "entropy_std", "entropy_min", "entropy_max",
    "tail_decay", "ttr", "hapax_ratio",
]

MODEL_FAMILIES = {
    "pythia-2.8b": "pythia",
    "pythia-1b": "pythia",
    "olmo-2-1b": "olmo",
    "qwen3-1.7b": "qwen",
    "qwen3-0.6b": "qwen",
    "qwen3-8b": "qwen",
}


class NumpyEncoder(json.JSONEncoder):
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


def make_clf():
    return XGBClassifier(
        n_estimators=200,
        max_depth=6,
        learning_rate=0.1,
        subsample=0.8,
        colsample_bytree=0.8,
        eval_metric="mlogloss",
        random_state=42,
        verbosity=0,
    )


def eval_fold(y_true, y_pred, n_classes=5):
    """Compute metrics for a single fold."""
    macro_f1 = f1_score(y_true, y_pred, average="macro", zero_division=0)
    weighted_f1 = f1_score(y_true, y_pred, average="weighted", zero_division=0)
    acc = accuracy_score(y_true, y_pred)
    per_class = {}
    report = classification_report(y_true, y_pred, output_dict=True, zero_division=0)
    for d in range(n_classes):
        key = str(d)
        if key in report:
            per_class[f"depth_{d}"] = {
                "precision": round(report[key]["precision"], 4),
                "recall": round(report[key]["recall"], 4),
                "f1": round(report[key]["f1-score"], 4),
                "support": int(report[key]["support"]),
            }
    cm = confusion_matrix(y_true, y_pred, labels=list(range(n_classes)))
    return {
        "macro_f1": round(float(macro_f1), 4),
        "weighted_f1": round(float(weighted_f1), 4),
        "accuracy": round(float(acc), 4),
        "per_class": per_class,
        "confusion_matrix": cm.tolist(),
    }


def leave_one_generator_out(df: pd.DataFrame) -> dict:
    """Train on N-1 generators, test on held-out generator."""
    generators = sorted(df["model_name"].unique())
    results = {}

    for held_out in generators:
        train_df = df[df["model_name"] != held_out]
        test_df = df[df["model_name"] == held_out]

        X_train = train_df[FEATURE_COLS].values
        y_train = train_df["depth"].values
        X_test = test_df[FEATURE_COLS].values
        y_test = test_df["depth"].values

        clf = make_clf()
        clf.fit(X_train, y_train)
        y_pred = clf.predict(X_test)

        metrics = eval_fold(y_test, y_pred)
        metrics["train_size"] = len(train_df)
        metrics["test_size"] = len(test_df)
        metrics["train_generators"] = [g for g in generators if g != held_out]
        results[held_out] = metrics

        print(f"  Hold out {held_out:15s}: macro_f1={metrics['macro_f1']:.4f}  "
              f"acc={metrics['accuracy']:.4f}  (train={len(train_df)}, test={len(test_df)})")

    # Summary
    f1s = [r["macro_f1"] for r in results.values()]
    results["_summary"] = {
        "mean_macro_f1": round(float(np.mean(f1s)), 4),
        "std_macro_f1": round(float(np.std(f1s)), 4),
        "min_macro_f1": round(float(np.min(f1s)), 4),
        "max_macro_f1": round(float(np.max(f1s)), 4),
    }
    return results


def leave_one_family_out(df: pd.DataFrame) -> dict:
    """Train on all models outside a family, test on models in the family."""
    df = df.copy()
    df["family"] = df["model_name"].map(MODEL_FAMILIES)
    families = sorted(df["family"].unique())

    if len(families) < 2:
        print("  [SKIP] Only one family present, cannot do leave-one-family-out")
        return {"_skipped": True, "reason": "only one family"}

    results = {}
    for held_out_family in families:
        train_df = df[df["family"] != held_out_family]
        test_df = df[df["family"] == held_out_family]

        if len(test_df) == 0 or len(train_df) == 0:
            continue

        X_train = train_df[FEATURE_COLS].values
        y_train = train_df["depth"].values
        X_test = test_df[FEATURE_COLS].values
        y_test = test_df["depth"].values

        clf = make_clf()
        clf.fit(X_train, y_train)
        y_pred = clf.predict(X_test)

        metrics = eval_fold(y_test, y_pred)
        held_models = sorted(test_df["model_name"].unique().tolist())
        metrics["held_out_models"] = held_models
        metrics["train_size"] = len(train_df)
        metrics["test_size"] = len(test_df)
        results[held_out_family] = metrics

        print(f"  Hold out family {held_out_family:8s} ({held_models}): "
              f"macro_f1={metrics['macro_f1']:.4f}  acc={metrics['accuracy']:.4f}")

    if results:
        f1s = [r["macro_f1"] for r in results.values() if isinstance(r, dict) and "macro_f1" in r]
        results["_summary"] = {
            "mean_macro_f1": round(float(np.mean(f1s)), 4),
            "std_macro_f1": round(float(np.std(f1s)), 4),
        }
    return results


def pooled_stratified_cv(df: pd.DataFrame, n_splits: int = 5) -> dict:
    """Pooled stratified K-fold CV across all generators (baseline)."""
    X = df[FEATURE_COLS].values
    y = df["depth"].values

    skf = StratifiedKFold(n_splits=n_splits, shuffle=True, random_state=42)
    fold_results = []

    for fold_idx, (train_idx, test_idx) in enumerate(skf.split(X, y)):
        clf = make_clf()
        clf.fit(X[train_idx], y[train_idx])
        y_pred = clf.predict(X[test_idx])
        metrics = eval_fold(y[test_idx], y_pred)
        fold_results.append(metrics)
        print(f"  Fold {fold_idx}: macro_f1={metrics['macro_f1']:.4f}  acc={metrics['accuracy']:.4f}")

    # Feature importance from full model
    clf_full = make_clf()
    clf_full.fit(X, y)
    importance = dict(zip(FEATURE_COLS, [round(float(x), 4) for x in clf_full.feature_importances_]))

    f1s = [r["macro_f1"] for r in fold_results]
    return {
        "folds": fold_results,
        "mean_macro_f1": round(float(np.mean(f1s)), 4),
        "std_macro_f1": round(float(np.std(f1s)), 4),
        "feature_importance": importance,
    }


def main():
    parser = argparse.ArgumentParser(description="Multi-generator depth classification with leave-one-out CV")
    parser.add_argument("--input", default="data/features_all.csv", help="Input features CSV")
    parser.add_argument("--output-dir", default="results", help="Output directory")
    parser.add_argument("--dry-run", action="store_true", help="Use subset of data for quick test")
    args = parser.parse_args()

    project_root = Path(__file__).resolve().parent
    input_path = project_root / args.input
    output_dir = project_root / args.output_dir

    if not input_path.exists():
        print(f"ERROR: {input_path} not found. Run extract_features_multi.py first.")
        sys.exit(1)

    df = pd.read_csv(input_path)
    print(f"Loaded {len(df)} rows from {input_path}")
    print(f"Generators: {df['model_name'].value_counts().to_dict()}")
    print(f"Depths: {df['depth'].value_counts().sort_index().to_dict()}")

    if args.dry_run:
        df = df.groupby(["model_name", "depth"]).head(20).reset_index(drop=True)
        print(f"[dry-run] Subsampled to {len(df)} rows")

    # --- Evaluation 1: Leave-one-generator-out ---
    print("\n=== Leave-One-Generator-Out CV ===")
    logo_results = leave_one_generator_out(df)
    print(f"\nSummary: mean_macro_f1={logo_results['_summary']['mean_macro_f1']:.4f} "
          f"± {logo_results['_summary']['std_macro_f1']:.4f}")

    # --- Evaluation 2: Leave-one-family-out ---
    print("\n=== Leave-One-Family-Out CV ===")
    lofo_results = leave_one_family_out(df)

    # --- Evaluation 3: Pooled stratified CV (baseline) ---
    print("\n=== Pooled Stratified 5-Fold CV (Baseline) ===")
    pooled_results = pooled_stratified_cv(df)
    print(f"\nBaseline: mean_macro_f1={pooled_results['mean_macro_f1']:.4f} "
          f"± {pooled_results['std_macro_f1']:.4f}")

    # --- Generalization gap ---
    gap = pooled_results["mean_macro_f1"] - logo_results["_summary"]["mean_macro_f1"]
    print(f"\n=== Generalization Gap ===")
    print(f"Pooled CV F1:      {pooled_results['mean_macro_f1']:.4f}")
    print(f"Leave-gen-out F1:  {logo_results['_summary']['mean_macro_f1']:.4f}")
    print(f"Gap:               {gap:+.4f}")

    # --- Save results ---
    final = {
        "dataset": {
            "total_rows": len(df),
            "generators": df["model_name"].value_counts().to_dict(),
            "depths": df["depth"].value_counts().sort_index().to_dict(),
        },
        "leave_one_generator_out": logo_results,
        "leave_one_family_out": lofo_results,
        "pooled_stratified_cv": pooled_results,
        "generalization_gap": round(float(gap), 4),
    }

    if args.dry_run:
        print("\n[dry-run] Results printed only, no file written.")
        return

    output_dir.mkdir(parents=True, exist_ok=True)

    json_path = output_dir / "multi_classify_results.json"
    with open(json_path, "w") as f:
        json.dump(final, f, indent=2, cls=NumpyEncoder)
    print(f"\nJSON saved to {json_path}")

    # CSV summary: one row per held-out generator
    csv_rows = []
    for gen, metrics in logo_results.items():
        if gen.startswith("_"):
            continue
        csv_rows.append({
            "held_out": gen,
            "eval_type": "leave_one_generator_out",
            "macro_f1": metrics["macro_f1"],
            "weighted_f1": metrics["weighted_f1"],
            "accuracy": metrics["accuracy"],
            "train_size": metrics["train_size"],
            "test_size": metrics["test_size"],
        })
    for fam, metrics in lofo_results.items():
        if fam.startswith("_") or not isinstance(metrics, dict) or "macro_f1" not in metrics:
            continue
        csv_rows.append({
            "held_out": f"family:{fam}",
            "eval_type": "leave_one_family_out",
            "macro_f1": metrics["macro_f1"],
            "weighted_f1": metrics["weighted_f1"],
            "accuracy": metrics["accuracy"],
            "train_size": metrics["train_size"],
            "test_size": metrics["test_size"],
        })
    csv_rows.append({
        "held_out": "none(pooled)",
        "eval_type": "pooled_stratified_cv",
        "macro_f1": pooled_results["mean_macro_f1"],
        "weighted_f1": float(np.mean([f["weighted_f1"] for f in pooled_results["folds"]])),
        "accuracy": float(np.mean([f["accuracy"] for f in pooled_results["folds"]])),
        "train_size": len(df),
        "test_size": len(df),
    })

    csv_path = output_dir / "multi_classify_results.csv"
    pd.DataFrame(csv_rows).to_csv(csv_path, index=False)
    print(f"CSV saved to {csv_path}")


if __name__ == "__main__":
    main()
