#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import os
import sys
import time
from pathlib import Path
from typing import Any

import numpy as np
from sklearn.datasets import load_iris
from sklearn.ensemble import AdaBoostClassifier, RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import f1_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
import xgboost as xgb


ROOT = Path(".")
REPO = ROOT / "repositories/ForestDiffusion"
PACKAGE = REPO / "Python-Package/base-ForestDiffusion"
FORMAL_DIR = ROOT / "baselines/bohb/forest_diffusion_iris_f1fake"


def parse_bool(value: str | bool) -> bool:
    if isinstance(value, bool):
        return value
    text = str(value).strip().lower()
    if text in {"1", "true", "t", "yes", "y"}:
        return True
    if text in {"0", "false", "f", "no", "n"}:
        return False
    raise argparse.ArgumentTypeError(f"invalid bool: {value}")


def install_optional_stubs() -> None:
    """ForestDiffusion imports optional backends at module import time."""
    stub_dir = FORMAL_DIR / "_optional_stubs"
    stub_dir.mkdir(parents=True, exist_ok=True)
    (stub_dir / "lightgbm.py").write_text(
        "class LGBMRegressor:\n"
        "    def __init__(self, *args, **kwargs):\n"
        "        raise ImportError('lightgbm is not installed in this benchmark env')\n"
    )
    (stub_dir / "catboost.py").write_text(
        "class CatBoostRegressor:\n"
        "    def __init__(self, *args, **kwargs):\n"
        "        raise ImportError('catboost is not installed in this benchmark env')\n"
    )
    sys.path.insert(0, str(stub_dir))
    sys.path.insert(0, str(PACKAGE))


def make_logreg(seed: int) -> LogisticRegression:
    kwargs = {"solver": "lbfgs", "max_iter": 500, "random_state": seed}
    try:
        return LogisticRegression(penalty=None, **kwargs)
    except TypeError:
        return LogisticRegression(penalty="none", **kwargs)


def sanitize_labels(y: np.ndarray) -> np.ndarray:
    return np.rint(y).astype(int).clip(0, 2)


def test_on_multiple_models(
    X_train: np.ndarray,
    y_train: np.ndarray,
    X_test: np.ndarray,
    y_test: np.ndarray,
    n_tries: int,
) -> dict[str, float]:
    y_train = sanitize_labels(y_train)
    y_test = sanitize_labels(y_test)
    if not np.isin(np.unique(y_test), np.unique(y_train)).all():
        return {"mean": 0.0, "lin": 0.0, "linboost": 0.0, "tree": 0.0, "treeboost": 0.0}

    totals = {"lin": 0.0, "linboost": 0.0, "tree": 0.0, "treeboost": 0.0}
    le = LabelEncoder()
    y_train_enc = le.fit_transform(y_train)
    for seed in range(n_tries):
        pred = make_logreg(seed).fit(X_train, y_train_enc).predict(X_test)
        totals["lin"] += f1_score(y_test, le.inverse_transform(pred), average="macro") / n_tries

        pred = AdaBoostClassifier(random_state=seed).fit(X_train, y_train_enc).predict(X_test)
        totals["linboost"] += f1_score(y_test, le.inverse_transform(pred), average="macro") / n_tries

        pred = RandomForestClassifier(max_depth=28, random_state=seed).fit(X_train, y_train_enc).predict(X_test)
        totals["tree"] += f1_score(y_test, le.inverse_transform(pred), average="macro") / n_tries

        pred = xgb.XGBClassifier(
            reg_lambda=0.0,
            random_state=seed,
            eval_metric="mlogloss",
            verbosity=0,
        ).fit(X_train, y_train_enc).predict(X_test)
        totals["treeboost"] += f1_score(y_test, le.inverse_transform(pred), average="macro") / n_tries
    totals["mean"] = sum(totals.values()) / 4.0
    return totals


def evaluate(args: argparse.Namespace) -> dict[str, Any]:
    install_optional_stubs()
    from ForestDiffusion import ForestDiffusionModel

    data = load_iris()
    X = data["data"].astype(float)
    y = data["target"].astype(int)

    f1_real_runs: list[float] = []
    f1_fake_runs: list[float] = []
    f1_fake_detail: list[dict[str, float]] = []
    timings: list[float] = []

    for exp_idx in range(args.nexp):
        seed = args.seed + exp_idx
        X_train, X_test, y_train, y_test = train_test_split(
            X,
            y,
            test_size=0.2,
            random_state=seed,
            stratify=y,
        )
        Xy_train = np.concatenate((X_train, y_train[:, None]), axis=1)

        started = time.time()
        if args.ycond:
            model = ForestDiffusionModel(
                X=X_train,
                label_y=y_train,
                n_t=args.n_t,
                model="xgboost",
                diffusion_type=args.diffusion_type,
                max_depth=args.max_depth,
                n_estimators=args.n_estimators,
                eta=args.eta,
                duplicate_K=args.duplicate_k,
                n_jobs=args.n_jobs,
                n_batch=args.n_batch,
                seed=seed,
            )
        else:
            model = ForestDiffusionModel(
                X=Xy_train,
                n_t=args.n_t,
                model="xgboost",
                diffusion_type=args.diffusion_type,
                max_depth=args.max_depth,
                n_estimators=args.n_estimators,
                eta=args.eta,
                duplicate_K=args.duplicate_k,
                cat_indexes=[4],
                n_jobs=args.n_jobs,
                n_batch=args.n_batch,
                seed=seed,
            )

        generated = model.generate(batch_size=args.ngen * X_train.shape[0], n_t=args.n_t_sampling)
        generated = generated.reshape(args.ngen, X_train.shape[0], X_train.shape[1] + 1)
        timings.append(time.time() - started)

        f1_real = test_on_multiple_models(X_train, y_train, X_test, y_test, n_tries=args.n_tries)
        f1_real_runs.append(f1_real["mean"])
        for gen_idx in range(args.ngen):
            X_fake = generated[gen_idx, :, :-1]
            y_fake = sanitize_labels(generated[gen_idx, :, -1])
            scores = test_on_multiple_models(X_fake, y_fake, X_test, y_test, n_tries=args.n_tries)
            f1_fake_runs.append(scores["mean"])
            f1_fake_detail.append(scores)

    return {
        "metric": "f1_fake",
        "f1_fake": float(np.mean(f1_fake_runs)),
        "f1_fake_std": float(np.std(f1_fake_runs)),
        "f1_real": float(np.mean(f1_real_runs)),
        "f1_fake_runs": f1_fake_runs,
        "f1_real_runs": f1_real_runs,
        "f1_fake_detail": f1_fake_detail,
        "seconds": round(float(np.sum(timings)), 3),
        "config": {
            "n_t": args.n_t,
            "n_t_sampling": args.n_t_sampling,
            "duplicate_k": args.duplicate_k,
            "max_depth": args.max_depth,
            "n_estimators": args.n_estimators,
            "eta": args.eta,
            "diffusion_type": args.diffusion_type,
            "ycond": args.ycond,
            "n_batch": args.n_batch,
            "n_jobs": args.n_jobs,
            "nexp": args.nexp,
            "ngen": args.ngen,
            "n_tries": args.n_tries,
            "seed": args.seed,
        },
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--results-dir", type=Path, required=True)
    parser.add_argument("--n-t", type=int, default=10)
    parser.add_argument("--n-t-sampling", type=int, default=0)
    parser.add_argument("--duplicate-k", type=int, default=5)
    parser.add_argument("--max-depth", type=int, default=7)
    parser.add_argument("--n-estimators", type=int, default=50)
    parser.add_argument("--eta", type=float, default=0.3)
    parser.add_argument("--diffusion-type", choices=["flow", "vp"], default="flow")
    parser.add_argument("--ycond", type=parse_bool, default=False)
    parser.add_argument("--n-batch", type=int, default=1)
    parser.add_argument("--n-jobs", type=int, default=8)
    parser.add_argument("--nexp", type=int, default=1)
    parser.add_argument("--ngen", type=int, default=2)
    parser.add_argument("--n-tries", type=int, default=2)
    parser.add_argument("--seed", type=int, default=0)
    args = parser.parse_args()

    if args.n_t_sampling == 0:
        args.n_t_sampling = args.n_t

    args.results_dir.mkdir(parents=True, exist_ok=True)
    payload = evaluate(args)
    out = args.results_dir / "results.json"
    out.write_text(json.dumps(payload, indent=2))
    print("RESULT_JSON " + json.dumps(payload, sort_keys=True), flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
