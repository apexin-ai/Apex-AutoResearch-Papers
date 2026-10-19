#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import time
from pathlib import Path
from typing import Any

import pandas as pd
from sklearn.ensemble import ExtraTreesClassifier, RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_auc_score
from sklearn.model_selection import StratifiedKFold, cross_validate
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import MinMaxScaler, StandardScaler
from sklearn.tree import DecisionTreeClassifier


ROOT = Path(".")
DATA_DIR = ROOT / "data/paper_exact/tabmini_molecular_biology_promoters_auc"


def parse_none(value: str | None) -> Any:
    if value is None:
        return None
    if str(value).lower() in {"none", "null"}:
        return None
    return value


def build_estimator(args: argparse.Namespace):
    class_weight = parse_none(args.class_weight)
    model_family = args.model_family.lower()
    if model_family == "logreg":
        clf = LogisticRegression(C=args.C, penalty="l2", class_weight=class_weight, random_state=args.seed, max_iter=1000)
        if args.scaler == "minmax":
            return Pipeline([("scaling", MinMaxScaler()), ("classify", clf)])
        if args.scaler == "standard":
            return Pipeline([("scaling", StandardScaler()), ("classify", clf)])
        return clf
    if model_family == "tree":
        return DecisionTreeClassifier(max_depth=args.max_depth, min_samples_leaf=args.min_samples_leaf, criterion=args.criterion, class_weight=class_weight, random_state=args.seed)
    if model_family == "forest":
        return RandomForestClassifier(n_estimators=args.n_estimators, max_depth=args.max_depth, min_samples_leaf=args.min_samples_leaf, criterion=args.criterion, class_weight=class_weight, max_features=parse_none(args.max_features), random_state=args.seed, n_jobs=1)
    if model_family == "extra_trees":
        return ExtraTreesClassifier(n_estimators=args.n_estimators, max_depth=args.max_depth, min_samples_leaf=args.min_samples_leaf, criterion=args.criterion, class_weight=class_weight, max_features=parse_none(args.max_features), random_state=args.seed, n_jobs=1)
    raise ValueError(f"Unsupported model_family={args.model_family!r}")


def run(args: argparse.Namespace) -> dict[str, Any]:
    started = time.time()
    X = pd.read_csv(args.x_file)
    y = pd.read_csv(args.y_file).iloc[:, 0].astype(int)
    estimator = build_estimator(args)
    cv = StratifiedKFold(n_splits=args.cv, shuffle=True, random_state=args.seed)
    scores = cross_validate(estimator, X, y, cv=cv, scoring="roc_auc", n_jobs=1, return_train_score=True)
    estimator.fit(X, y)
    full_auc = float(roc_auc_score(y, estimator.predict_proba(X)[:, 1])) if hasattr(estimator, "predict_proba") else float("nan")
    test_auc = float(scores["test_score"].mean())
    train_auc = float(scores["train_score"].mean())
    result = {
        "task": "tabmini_molecular_biology_promoters_auc",
        "repo": "TabMini",
        "dataset": "molecular_biology_promoters",
        "x_file": str(args.x_file),
        "y_file": str(args.y_file),
        "metric": "roc_auc",
        "cv": args.cv,
        "seed": args.seed,
        "model_family": args.model_family,
        "scaler": args.scaler,
        "C": args.C,
        "max_depth": args.max_depth,
        "min_samples_leaf": args.min_samples_leaf,
        "criterion": args.criterion,
        "class_weight": parse_none(args.class_weight),
        "n_estimators": args.n_estimators,
        "max_features": parse_none(args.max_features),
        "test_auc": test_auc,
        "train_auc": train_auc,
        "full_train_auc": full_auc,
        "test_auc_percent": test_auc * 100.0,
        "train_auc_percent": train_auc * 100.0,
        "fold_test_scores": [float(item) for item in scores["test_score"]],
        "fold_train_scores": [float(item) for item in scores["train_score"]],
        "seconds": round(time.time() - started, 3),
    }
    args.results_dir.mkdir(parents=True, exist_ok=True)
    (args.results_dir / "results.json").write_text(json.dumps(result, indent=2))
    print(json.dumps(result, indent=2), flush=True)
    return result


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--results-dir", type=Path, required=True)
    parser.add_argument("--x-file", type=Path, default=DATA_DIR / "X.csv")
    parser.add_argument("--y-file", type=Path, default=DATA_DIR / "y.csv")
    parser.add_argument("--model-family", choices=["logreg", "tree", "forest", "extra_trees"], default="logreg")
    parser.add_argument("--scaler", choices=["minmax", "standard", "none"], default="minmax")
    parser.add_argument("--C", type=float, default=0.5)
    parser.add_argument("--max-depth", type=lambda value: None if value.lower() == "none" else int(value), default=None)
    parser.add_argument("--min-samples-leaf", type=int, default=1)
    parser.add_argument("--criterion", choices=["gini", "entropy", "log_loss"], default="gini")
    parser.add_argument("--class-weight", choices=["none", "balanced"], default="none")
    parser.add_argument("--n-estimators", type=int, default=100)
    parser.add_argument("--max-features", choices=["none", "sqrt", "log2"], default="sqrt")
    parser.add_argument("--cv", type=int, default=2)
    parser.add_argument("--seed", type=int, default=42)
    args = parser.parse_args()
    run(args)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
