#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import time
from pathlib import Path
from typing import Any

import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.ensemble import ExtraTreesClassifier, GradientBoostingClassifier, RandomForestClassifier
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.tree import DecisionTreeClassifier


ROOT = Path(".")
DATA_DIR = ROOT / "data/paper_exact/binary_diffusion_adult_rf"


def parse_none(value: str | None) -> Any:
    if value is None:
        return None
    if str(value).lower() in {"none", "null"}:
        return None
    return value


def build_model(args: argparse.Namespace):
    class_weight = parse_none(args.class_weight)
    family = args.model_family.lower()
    if family == "rf":
        return RandomForestClassifier(
            n_estimators=args.n_estimators,
            max_depth=args.max_depth,
            min_samples_leaf=args.min_samples_leaf,
            criterion=args.criterion,
            max_features=parse_none(args.max_features),
            class_weight=class_weight,
            random_state=args.seed,
            n_jobs=1,
        )
    if family == "extra_trees":
        return ExtraTreesClassifier(
            n_estimators=args.n_estimators,
            max_depth=args.max_depth,
            min_samples_leaf=args.min_samples_leaf,
            criterion=args.criterion,
            max_features=parse_none(args.max_features),
            class_weight=class_weight,
            random_state=args.seed,
            n_jobs=1,
        )
    if family == "tree":
        return DecisionTreeClassifier(
            max_depth=args.max_depth,
            min_samples_leaf=args.min_samples_leaf,
            criterion=args.criterion,
            class_weight=class_weight,
            random_state=args.seed,
        )
    if family == "gb":
        return GradientBoostingClassifier(
            n_estimators=args.n_estimators,
            learning_rate=args.learning_rate,
            max_depth=3 if args.max_depth is None else min(args.max_depth, 4),
            min_samples_leaf=args.min_samples_leaf,
            random_state=args.seed,
        )
    if family == "lr":
        return LogisticRegression(C=args.C, class_weight=class_weight, random_state=args.seed, max_iter=1000)
    raise ValueError(f"Unsupported model_family={args.model_family!r}")


def encode_target(series: pd.Series, positive_label: str | None) -> pd.Series:
    if positive_label is not None:
        return (series.astype(str) == str(positive_label)).astype(int)
    values = list(pd.Series(series).dropna().unique())
    if len(values) != 2:
        raise ValueError(f"Expected a binary target, got {len(values)} labels: {values[:10]}")
    if pd.api.types.is_numeric_dtype(series):
        return (series == max(values)).astype(int)
    positive = sorted(map(str, values))[-1]
    return (series.astype(str) == positive).astype(int)


def run(args: argparse.Namespace) -> dict[str, Any]:
    started = time.time()
    train = pd.read_csv(args.train_file)
    test = pd.read_csv(args.test_file)
    target = args.target_column
    X_train = train.drop(columns=[target])
    y_train = encode_target(train[target], args.positive_label)
    X_test = test.drop(columns=[target])
    y_test = encode_target(test[target], args.positive_label)

    numerical = [c for c in X_train.columns if pd.api.types.is_numeric_dtype(X_train[c])]
    categorical = [c for c in X_train.columns if c not in numerical]
    transformers = []
    if numerical:
        transformers.append(("num", Pipeline([("impute", SimpleImputer(strategy="median")), ("scale", StandardScaler())]), numerical))
    if categorical:
        transformers.append(("cat", Pipeline([("impute", SimpleImputer(strategy="most_frequent")), ("onehot", OneHotEncoder(handle_unknown="ignore"))]), categorical))
    preprocessor = ColumnTransformer(transformers)
    pipeline = Pipeline([("preprocess", preprocessor), ("model", build_model(args))])
    pipeline.fit(X_train, y_train)
    train_pred = pipeline.predict(X_train)
    test_pred = pipeline.predict(X_test)
    train_accuracy = float(accuracy_score(y_train, train_pred))
    test_accuracy = float(accuracy_score(y_test, test_pred))
    result = {
        "task": "binary_diffusion_adult_rf",
        "repo": "binary-diffusion-tabular",
        "dataset": "Adult Income",
        "train_file": str(args.train_file),
        "test_file": str(args.test_file),
        "target_column": target,
        "metric": "accuracy",
        "model_family": args.model_family,
        "n_estimators": args.n_estimators,
        "max_depth": args.max_depth,
        "min_samples_leaf": args.min_samples_leaf,
        "criterion": args.criterion,
        "max_features": parse_none(args.max_features),
        "class_weight": parse_none(args.class_weight),
        "learning_rate": args.learning_rate,
        "C": args.C,
        "seed": args.seed,
        "train_accuracy": train_accuracy,
        "test_accuracy": test_accuracy,
        "train_accuracy_percent": train_accuracy * 100.0,
        "test_accuracy_percent": test_accuracy * 100.0,
        "seconds": round(time.time() - started, 3),
    }
    args.results_dir.mkdir(parents=True, exist_ok=True)
    (args.results_dir / "results.json").write_text(json.dumps(result, indent=2))
    print(json.dumps(result, indent=2), flush=True)
    return result


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--results-dir", type=Path, required=True)
    parser.add_argument("--train-file", type=Path, default=DATA_DIR / "adult_train.csv")
    parser.add_argument("--test-file", type=Path, default=DATA_DIR / "adult_test.csv")
    parser.add_argument("--target-column", default="label")
    parser.add_argument("--positive-label", default='>50K')
    parser.add_argument("--model-family", choices=["rf", "extra_trees", "tree", "gb", "lr"], default="rf")
    parser.add_argument("--n-estimators", type=int, default=100)
    parser.add_argument("--max-depth", type=lambda value: None if value.lower() == "none" else int(value), default=None)
    parser.add_argument("--min-samples-leaf", type=int, default=1)
    parser.add_argument("--criterion", choices=["gini", "entropy", "log_loss"], default="gini")
    parser.add_argument("--max-features", choices=["sqrt", "log2", "none"], default="sqrt")
    parser.add_argument("--class-weight", choices=["none", "balanced"], default="none")
    parser.add_argument("--learning-rate", type=float, default=0.1)
    parser.add_argument("--C", type=float, default=1.0)
    parser.add_argument("--seed", type=int, default=42)
    args = parser.parse_args()
    run(args)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
