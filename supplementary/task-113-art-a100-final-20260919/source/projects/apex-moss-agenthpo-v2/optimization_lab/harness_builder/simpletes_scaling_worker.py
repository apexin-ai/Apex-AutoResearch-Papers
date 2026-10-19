from __future__ import annotations

import contextlib
import importlib.util
import io
import json
import resource
import sys
from pathlib import Path
from typing import Any

import numpy as np


def _limits() -> None:
    resource.setrlimit(resource.RLIMIT_CPU, (600, 600))
    resource.setrlimit(resource.RLIMIT_NOFILE, (64, 64))
    resource.setrlimit(resource.RLIMIT_CORE, (0, 0))
    resource.setrlimit(resource.RLIMIT_FSIZE, (8 * 1024 * 1024, 8 * 1024 * 1024))


def _load_candidate(path: Path) -> Any:
    spec = importlib.util.spec_from_file_location("candidate", path)
    if spec is None or spec.loader is None:
        raise RuntimeError("candidate import spec failed")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def main() -> int:
    _limits()
    payload = json.load(sys.stdin)
    if not isinstance(payload, dict) or set(payload) != {"groups", "max_param_count"}:
        raise ValueError("worker input contract is invalid")
    candidate = _load_candidate(Path("/candidate.py"))
    fit = candidate.fit_scaling_law
    predict = candidate.scaling_law_func
    predictions: list[list[Any]] = []
    muted = io.StringIO()
    with contextlib.redirect_stdout(muted), contextlib.redirect_stderr(muted):
        for group in payload["groups"]:
            if not isinstance(group, dict) or set(group) != {
                "key",
                "train_x",
                "train_y",
                "test_x",
            }:
                raise ValueError("worker group contract is invalid")
            train_x = np.asarray(group["train_x"], dtype=float)
            train_y = np.asarray(group["train_y"], dtype=float)
            test_x = np.asarray(group["test_x"], dtype=float)
            params = fit(train_x, train_y)
            param_count = int(np.asarray(params).size)
            if param_count > int(payload["max_param_count"]):
                raise ValueError(
                    f"parameter_count_exceeded:{param_count}>{payload['max_param_count']}"
                )
            predicted = np.asarray(predict(test_x, params), dtype=float)
            predictions.append(predicted.tolist())
    json.dump({"predictions": predictions}, sys.stdout, allow_nan=False)
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as exc:
        print(f"worker_error:{type(exc).__name__}:{str(exc)[:400]}", file=sys.stderr)
        raise SystemExit(2)
