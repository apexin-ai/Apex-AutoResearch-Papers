from __future__ import annotations

import argparse
import hashlib
import json
import math
import numbers
import os
import subprocess
import sys
import tempfile
import time
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any, Callable, Mapping, Sequence


LCBENCH_SCHEMA_VERSION = 1
LCBENCH_EVALUATOR_ID = "yahpo-gym-lcbench-1.0.2"
LCBENCH_QUERY_COUNT = 16
LCBENCH_FIXED_EPOCH = 52
LCBENCH_MAX_CANDIDATE_BYTES = 64 * 1024
LCBENCH_QUERY_KEYS = frozenset(
    {
        "batch_size",
        "learning_rate",
        "max_dropout",
        "max_units",
        "momentum",
        "num_layers",
        "weight_decay",
    }
)
_CANDIDATE_KEYS = frozenset({"schema_version", "instance_id", "queries"})
_METRIC_KEYS = (
    "time",
    "val_accuracy",
    "val_cross_entropy",
    "val_balanced_accuracy",
    "test_cross_entropy",
    "test_balanced_accuracy",
)


class LCBenchCandidatePolicyError(ValueError):
    """One LCBench JSON batch violates the frozen public contract."""


def _reject_json_constant(value: str) -> None:
    raise LCBenchCandidatePolicyError(
        f"non-finite JSON constant is forbidden: {value}"
    )


def _unique_object(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in pairs:
        if key in result:
            raise LCBenchCandidatePolicyError(f"duplicate JSON key: {key}")
        result[key] = value
    return result


def _canonical_bytes(payload: Mapping[str, Any]) -> bytes:
    return (
        json.dumps(
            payload,
            ensure_ascii=True,
            allow_nan=False,
            sort_keys=True,
            separators=(",", ":"),
        )
        + "\n"
    ).encode("utf-8")


def _sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def _bounded_integer(value: Any, *, name: str, lower: int, upper: int) -> int:
    if isinstance(value, bool) or not isinstance(value, numbers.Integral):
        raise LCBenchCandidatePolicyError(f"{name} must be an integer")
    parsed = int(value)
    if not lower <= parsed <= upper:
        raise LCBenchCandidatePolicyError(
            f"{name} must be between {lower} and {upper}"
        )
    return parsed


def _bounded_float(value: Any, *, name: str, lower: float, upper: float) -> float:
    if isinstance(value, bool) or not isinstance(value, numbers.Real):
        raise LCBenchCandidatePolicyError(f"{name} must be numeric")
    parsed = float(value)
    if not math.isfinite(parsed) or not lower <= parsed <= upper:
        raise LCBenchCandidatePolicyError(
            f"{name} must be finite and between {lower} and {upper}"
        )
    return parsed


@dataclass(frozen=True)
class LCBenchQueryBatch:
    instance_id: str
    queries: tuple[dict[str, int | float], ...]

    @classmethod
    def from_bytes(
        cls, raw: bytes, *, expected_instance_id: str
    ) -> "LCBenchQueryBatch":
        if not raw or len(raw) > LCBENCH_MAX_CANDIDATE_BYTES:
            raise LCBenchCandidatePolicyError(
                "LCBench candidate is empty or exceeds the byte limit"
            )
        try:
            payload = json.loads(
                raw.decode("utf-8"),
                object_pairs_hook=_unique_object,
                parse_constant=_reject_json_constant,
            )
        except (UnicodeDecodeError, json.JSONDecodeError) as exc:
            raise LCBenchCandidatePolicyError("LCBench candidate is not strict JSON") from exc
        if not isinstance(payload, dict) or frozenset(payload) != _CANDIDATE_KEYS:
            raise LCBenchCandidatePolicyError(
                "LCBench candidate has unexpected top-level keys"
            )
        if payload["schema_version"] != LCBENCH_SCHEMA_VERSION:
            raise LCBenchCandidatePolicyError("LCBench schema_version differs")
        if payload["instance_id"] != expected_instance_id:
            raise LCBenchCandidatePolicyError(
                "LCBench instance differs from the evaluator lane"
            )
        raw_queries = payload["queries"]
        if not isinstance(raw_queries, list) or len(raw_queries) != LCBENCH_QUERY_COUNT:
            raise LCBenchCandidatePolicyError(
                f"LCBench candidate must contain exactly {LCBENCH_QUERY_COUNT} queries"
            )
        queries: list[dict[str, int | float]] = []
        signatures: set[bytes] = set()
        for index, query in enumerate(raw_queries):
            if not isinstance(query, dict) or frozenset(query) != LCBENCH_QUERY_KEYS:
                raise LCBenchCandidatePolicyError(
                    f"LCBench query {index} has unexpected keys"
                )
            normalized: dict[str, int | float] = {
                "batch_size": _bounded_integer(
                    query["batch_size"], name="batch_size", lower=16, upper=512
                ),
                "learning_rate": _bounded_float(
                    query["learning_rate"],
                    name="learning_rate",
                    lower=0.00010000000000000009,
                    upper=0.10000000000000002,
                ),
                "max_dropout": _bounded_float(
                    query["max_dropout"], name="max_dropout", lower=0.0, upper=1.0
                ),
                "max_units": _bounded_integer(
                    query["max_units"], name="max_units", lower=64, upper=1024
                ),
                "momentum": _bounded_float(
                    query["momentum"], name="momentum", lower=0.1, upper=0.99
                ),
                "num_layers": _bounded_integer(
                    query["num_layers"], name="num_layers", lower=1, upper=5
                ),
                "weight_decay": _bounded_float(
                    query["weight_decay"],
                    name="weight_decay",
                    lower=0.00001,
                    upper=0.1,
                ),
            }
            signature = _canonical_bytes(normalized)
            if signature in signatures:
                raise LCBenchCandidatePolicyError(
                    "LCBench queries must be unique within one batch"
                )
            signatures.add(signature)
            queries.append(normalized)
        return cls(instance_id=expected_instance_id, queries=tuple(queries))

    def to_dict(self) -> dict[str, Any]:
        return {
            "schema_version": LCBENCH_SCHEMA_VERSION,
            "instance_id": self.instance_id,
            "queries": [dict(query) for query in self.queries],
        }


@dataclass(frozen=True)
class LCBenchTask:
    instance_id: str
    data_root: Path
    settings_path: Path
    python_executable: Path
    model_sha256: str
    config_space_sha256: str
    encoding_sha256: str
    settings_sha256: str

    def __post_init__(self) -> None:
        if not self.instance_id.isdigit():
            raise ValueError("LCBench instance_id must be numeric")
        for digest in (
            self.model_sha256,
            self.config_space_sha256,
            self.encoding_sha256,
            self.settings_sha256,
        ):
            if len(digest) != 64 or any(char not in "0123456789abcdef" for char in digest):
                raise ValueError("LCBench task digest is invalid")


@dataclass(frozen=True)
class LCBenchResult:
    schema_version: int
    evaluator_id: str
    status: str
    correct: bool
    instance_id: str
    candidate_sha256: str
    query_count: int
    best_query_index: int | None
    best_validation_score: float | None
    best_test_score: float | None
    metrics_sha256: str | None
    evaluator_seconds: float
    error_type: str
    error_summary: str

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


Objective = Callable[[list[dict[str, object]]], Sequence[Mapping[str, Any]]]


class LCBenchAdapter:
    """Evaluate bounded JSON query batches against a source-locked surrogate."""

    def __init__(self, *, task: LCBenchTask, objective: Objective | None = None) -> None:
        self.task = task
        self.objective = objective

    def _verify_sources(self) -> None:
        expected = {
            self.task.data_root / "model.onnx": self.task.model_sha256,
            self.task.data_root / "config_space.json": self.task.config_space_sha256,
            self.task.data_root / "encoding.json": self.task.encoding_sha256,
            self.task.settings_path: self.task.settings_sha256,
        }
        for path, digest in expected.items():
            if not path.is_file():
                raise RuntimeError(f"LCBench frozen source is missing: {path.name}")
            if _sha256(path) != digest:
                raise RuntimeError(f"LCBench {path.name} digest differs")

    def evaluate(self, candidate_path: Path, private_result_path: Path) -> LCBenchResult:
        self._verify_sources()
        candidate_path = candidate_path.resolve(strict=True)
        batch = LCBenchQueryBatch.from_bytes(
            candidate_path.read_bytes(), expected_instance_id=self.task.instance_id
        )
        candidate_sha256 = _sha256(candidate_path)
        started = time.monotonic()
        if self.objective is not None:
            configurations = _trusted_configurations(batch)
            metrics = self.objective(configurations)
            result = _result_from_metrics(
                batch=batch,
                candidate_sha256=candidate_sha256,
                metrics=metrics,
                evaluator_seconds=time.monotonic() - started,
            )
            _write_once(private_result_path, _canonical_bytes(result.to_dict()))
            return result

        if not self.task.python_executable.is_file():
            raise RuntimeError("LCBench pinned Python executable is missing")
        private_result_path.parent.mkdir(parents=True, exist_ok=True)
        with tempfile.TemporaryDirectory(
            prefix="lcbench-worker-", dir=private_result_path.parent
        ) as scratch:
            worker_result = Path(scratch) / "result.json"
            command = (
                str(self.task.python_executable),
                str(Path(__file__).resolve()),
                "--worker",
                "--candidate",
                str(candidate_path),
                "--result",
                str(worker_result),
                "--instance-id",
                self.task.instance_id,
                "--settings",
                str(self.task.settings_path.resolve(strict=True)),
            )
            completed = subprocess.run(
                command,
                stdin=subprocess.DEVNULL,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
                timeout=300,
                check=False,
                env={
                    "PATH": "/usr/bin:/bin",
                    "HOME": scratch,
                    "PYTHONNOUSERSITE": "1",
                    "OMP_NUM_THREADS": "1",
                },
            )
            if completed.returncode != 0 or not worker_result.is_file():
                result = LCBenchResult(
                    schema_version=1,
                    evaluator_id=LCBENCH_EVALUATOR_ID,
                    status="environment_invalid",
                    correct=False,
                    instance_id=self.task.instance_id,
                    candidate_sha256=candidate_sha256,
                    query_count=LCBENCH_QUERY_COUNT,
                    best_query_index=None,
                    best_validation_score=None,
                    best_test_score=None,
                    metrics_sha256=None,
                    evaluator_seconds=min(time.monotonic() - started, 300.0),
                    error_type="worker_failed",
                    error_summary=(
                        "LCBench trusted worker failed: "
                        + " ".join(completed.stderr.split())[-500:]
                    ),
                )
            else:
                result = _result_from_private_bytes(
                    worker_result.read_bytes(),
                    expected_instance_id=self.task.instance_id,
                    expected_candidate_sha256=candidate_sha256,
                )
            _write_once(private_result_path, _canonical_bytes(result.to_dict()))
            return result


def _trusted_configurations(batch: LCBenchQueryBatch) -> list[dict[str, object]]:
    configurations: list[dict[str, object]] = []
    for query in batch.queries:
        configuration: dict[str, object] = dict(query)
        configuration["OpenML_task_id"] = batch.instance_id
        configuration["epoch"] = LCBENCH_FIXED_EPOCH
        configurations.append(configuration)
    return configurations


def _result_from_metrics(
    *,
    batch: LCBenchQueryBatch,
    candidate_sha256: str,
    metrics: Sequence[Mapping[str, Any]],
    evaluator_seconds: float,
) -> LCBenchResult:
    if len(metrics) != LCBENCH_QUERY_COUNT:
        raise RuntimeError("LCBench objective returned the wrong metric count")
    normalized: list[dict[str, float]] = []
    for row in metrics:
        if not isinstance(row, Mapping) or any(key not in row for key in _METRIC_KEYS):
            raise RuntimeError("LCBench objective returned an incomplete metric row")
        parsed: dict[str, float] = {}
        for key in _METRIC_KEYS:
            value = row[key]
            if isinstance(value, bool) or not isinstance(value, numbers.Real):
                raise RuntimeError(f"LCBench metric {key} is not numeric")
            numeric = float(value)
            if not math.isfinite(numeric):
                raise RuntimeError(f"LCBench metric {key} is not finite")
            parsed[key] = numeric
        if not 0.0 < parsed["val_balanced_accuracy"] <= 1.0:
            raise RuntimeError("LCBench validation score is outside (0, 1]")
        if not 0.0 <= parsed["test_balanced_accuracy"] <= 1.0:
            raise RuntimeError("LCBench private test score is outside [0, 1]")
        normalized.append(parsed)
    best_index = max(
        range(len(normalized)),
        key=lambda index: normalized[index]["val_balanced_accuracy"],
    )
    metrics_payload = {"rows": normalized}
    return LCBenchResult(
        schema_version=1,
        evaluator_id=LCBENCH_EVALUATOR_ID,
        status="valid",
        correct=True,
        instance_id=batch.instance_id,
        candidate_sha256=candidate_sha256,
        query_count=LCBENCH_QUERY_COUNT,
        best_query_index=best_index,
        best_validation_score=normalized[best_index]["val_balanced_accuracy"],
        best_test_score=normalized[best_index]["test_balanced_accuracy"],
        metrics_sha256=hashlib.sha256(_canonical_bytes(metrics_payload)).hexdigest(),
        evaluator_seconds=max(0.0, min(float(evaluator_seconds), 300.0)),
        error_type="",
        error_summary="",
    )


def _result_from_private_bytes(
    raw: bytes, *, expected_instance_id: str, expected_candidate_sha256: str
) -> LCBenchResult:
    try:
        payload = json.loads(raw.decode("utf-8"), parse_constant=_reject_json_constant)
        result = LCBenchResult(**payload)
    except (UnicodeDecodeError, json.JSONDecodeError, TypeError) as exc:
        raise RuntimeError("LCBench worker returned invalid private JSON") from exc
    if (
        result.schema_version != 1
        or result.evaluator_id != LCBENCH_EVALUATOR_ID
        or result.instance_id != expected_instance_id
        or result.candidate_sha256 != expected_candidate_sha256
        or result.query_count != LCBENCH_QUERY_COUNT
    ):
        raise RuntimeError("LCBench worker result binding differs")
    if result.status != "valid" or not result.correct:
        raise RuntimeError("LCBench worker did not return a valid evaluation")
    if result.best_validation_score is None or result.best_test_score is None:
        raise RuntimeError("LCBench worker result lacks scores")
    return result


def _write_once(path: Path, content: bytes) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.exists():
        if path.read_bytes() != content:
            raise RuntimeError("refusing to overwrite a different LCBench result")
        return
    fd, name = tempfile.mkstemp(prefix=".lcbench-", dir=path.parent)
    try:
        with os.fdopen(fd, "wb") as handle:
            handle.write(content)
            handle.flush()
            os.fsync(handle.fileno())
        Path(name).replace(path)
    except Exception:
        Path(name).unlink(missing_ok=True)
        raise


def _worker(args: argparse.Namespace) -> int:
    candidate_path = Path(args.candidate).resolve(strict=True)
    result_path = Path(args.result).resolve()
    settings_path = Path(args.settings).resolve(strict=True)
    batch = LCBenchQueryBatch.from_bytes(
        candidate_path.read_bytes(), expected_instance_id=args.instance_id
    )
    os.environ["YAHPO_LOCAL_CONFIG"] = str(settings_path)
    started = time.monotonic()
    from yahpo_gym.benchmark_set import BenchmarkSet

    benchmark = BenchmarkSet("lcbench", instance=args.instance_id)
    metrics = benchmark.objective_function(_trusted_configurations(batch))
    result = _result_from_metrics(
        batch=batch,
        candidate_sha256=_sha256(candidate_path),
        metrics=metrics,
        evaluator_seconds=time.monotonic() - started,
    )
    _write_once(result_path, _canonical_bytes(result.to_dict()))
    return 0


def _parse_args(argv: Sequence[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--worker", action="store_true")
    parser.add_argument("--candidate")
    parser.add_argument("--result")
    parser.add_argument("--instance-id")
    parser.add_argument("--settings")
    args = parser.parse_args(argv)
    if not args.worker or not all(
        (args.candidate, args.result, args.instance_id, args.settings)
    ):
        parser.error("the trusted LCBench worker requires all fixed arguments")
    return args


if __name__ == "__main__":
    try:
        raise SystemExit(_worker(_parse_args(sys.argv[1:])))
    except Exception as exc:
        print(
            f"LCBench worker failed: {type(exc).__name__}: {exc}",
            file=sys.stderr,
        )
        raise SystemExit(1)


__all__ = [
    "LCBENCH_EVALUATOR_ID",
    "LCBENCH_FIXED_EPOCH",
    "LCBENCH_QUERY_COUNT",
    "LCBenchAdapter",
    "LCBenchCandidatePolicyError",
    "LCBenchQueryBatch",
    "LCBenchResult",
    "LCBenchTask",
]
