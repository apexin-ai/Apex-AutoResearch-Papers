from __future__ import annotations

import hashlib
import json
import re
import time
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Protocol

from optimization_lab.adapters.base import EvaluationStatus as KernelEvaluationStatus

from .adapters.compilergym import CompilerGymCbenchAdapter
from .adapters.kernelbench_meta import KernelBenchMetaAdapter, KernelBenchMetaTask
from .adapters.kernelbenchx import KernelBenchXAdapter, KernelBenchXTask
from .adapters.lcbench import LCBenchAdapter
from .adapters.sweperf import SWEPerfAdapter
from .adapters.swebench_verified import SWEBenchVerifiedRemoteAdapter
from .events import ResourceVector


_PRIVATE_PATH = re.compile(r"(?<![A-Za-z0-9])/(?:[^\s:|]+/)*[^\s:|]+")


def _canonical_sha(payload: dict[str, Any]) -> str:
    encoded = json.dumps(
        payload,
        ensure_ascii=False,
        allow_nan=False,
        sort_keys=True,
        separators=(",", ":"),
    ).encode("utf-8")
    return hashlib.sha256(encoded).hexdigest()


def _public_text(value: str) -> str:
    return _PRIVATE_PATH.sub("<private-path>", " ".join(value.split()))[:500]


@dataclass(frozen=True)
class NormalizedEvaluation:
    status: str
    correct: bool
    score: float | None
    public_feedback: dict[str, Any]
    actual_usage: ResourceVector
    evidence_sha256: str | None = None

    def __post_init__(self) -> None:
        if not self.status:
            raise ValueError("normalized evaluation status is required")
        if self.correct:
            if not isinstance(self.score, (int, float)) or self.score <= 0:
                raise ValueError("correct normalized evaluation requires a positive score")
        elif self.score is not None:
            raise ValueError("incorrect normalized evaluation cannot expose a score")
        if self.actual_usage.evaluator_transactions != 1:
            raise ValueError("one normalized evaluation must charge one transaction")
        if self.evidence_sha256 is not None and not re.fullmatch(
            r"[0-9a-f]{64}", self.evidence_sha256
        ):
            raise ValueError("invalid normalized evidence sha256")


class EvaluationBackend(Protocol):
    reservation: ResourceVector

    def evaluate(
        self, artifact_path: Path, private_dir: Path
    ) -> NormalizedEvaluation: ...


class KernelBenchXEvaluationBackend:
    reservation = ResourceVector(
        evaluator_transactions=1, gpu_exclusive_seconds=600.0
    )

    def __init__(self, *, adapter: KernelBenchXAdapter, task: KernelBenchXTask) -> None:
        self.adapter = adapter
        self.task = task

    def evaluate(self, artifact_path: Path, private_dir: Path) -> NormalizedEvaluation:
        result = self.adapter.evaluate(self.task, artifact_path, private_dir)
        feedback = {
            "status": result.status.value,
            "compiled": result.compiled,
            "correct": result.correct,
            "score": result.speedup_vs_eager,
            "error_summary": _public_text(result.error_summary),
            "hardware": result.hardware,
        }
        evidence_sha = _canonical_sha(result.to_dict())
        return NormalizedEvaluation(
            status=result.status.value,
            correct=result.correct,
            score=result.speedup_vs_eager if result.correct else None,
            public_feedback=feedback,
            actual_usage=ResourceVector(
                evaluator_transactions=1,
                gpu_exclusive_seconds=min(result.gpu_seconds, 600.0),
            ),
            evidence_sha256=evidence_sha,
        )


class KernelBenchMetaEvaluationBackend:
    """Normalize only the nonce-bound HB-GEN-1 KernelBench private result."""

    reservation = ResourceVector(
        evaluator_transactions=1, gpu_exclusive_seconds=600.0
    )

    def __init__(
        self, *, adapter: KernelBenchMetaAdapter, task: KernelBenchMetaTask
    ) -> None:
        self.adapter = adapter
        self.task = task

    def evaluate(self, artifact_path: Path, private_dir: Path) -> NormalizedEvaluation:
        result = self.adapter.evaluate(self.task, artifact_path, private_dir)
        feedback = {
            "status": result.status.value,
            "compiled": result.compiled,
            "correct": result.correct,
            "score": result.speedup_vs_eager,
            "error_summary": _public_text(result.error_summary),
            "hardware": result.hardware,
        }
        evidence_sha = _canonical_sha(result.to_dict())
        return NormalizedEvaluation(
            status=result.status.value,
            correct=result.correct,
            score=result.speedup_vs_eager if result.correct else None,
            public_feedback=feedback,
            actual_usage=ResourceVector(
                evaluator_transactions=1,
                gpu_exclusive_seconds=min(result.gpu_seconds, 600.0),
            ),
            evidence_sha256=evidence_sha,
        )


class CompilerGymEvaluationBackend:
    reservation = ResourceVector(
        evaluator_transactions=1, cpu_evaluator_seconds=300.0
    )

    def __init__(self, *, adapter: CompilerGymCbenchAdapter) -> None:
        self.adapter = adapter

    def evaluate(self, artifact_path: Path, private_dir: Path) -> NormalizedEvaluation:
        private_dir.mkdir(parents=True, exist_ok=True)
        result_path = private_dir / "supervisor.json"
        started = time.monotonic()
        result = self.adapter.evaluate(artifact_path, result_path)
        elapsed = min(time.monotonic() - started, 300.0)
        payload = result.to_dict()
        feedback = {
            "status": result.status,
            "correct": result.correct,
            "score": result.normalized_score,
            "action_count": result.action_count,
            "error_type": result.error_type,
            "error_summary": _public_text(result.error_summary),
        }
        return NormalizedEvaluation(
            status=result.status,
            correct=result.correct,
            score=result.normalized_score if result.correct else None,
            public_feedback=feedback,
            actual_usage=ResourceVector(
                evaluator_transactions=1, cpu_evaluator_seconds=elapsed
            ),
            evidence_sha256=_canonical_sha(payload),
        )


class LCBenchEvaluationBackend:
    reservation = ResourceVector(
        evaluator_transactions=1, cpu_evaluator_seconds=300.0
    )

    def __init__(self, *, adapter: LCBenchAdapter) -> None:
        self.adapter = adapter

    def evaluate(self, artifact_path: Path, private_dir: Path) -> NormalizedEvaluation:
        private_dir.mkdir(parents=True, exist_ok=True)
        result = self.adapter.evaluate(artifact_path, private_dir / "supervisor.json")
        feedback = {
            "status": result.status,
            "correct": result.correct,
            "best_validation_score": result.best_validation_score,
            "best_query_index": result.best_query_index,
            "query_count": result.query_count,
            "error_type": result.error_type,
            "error_summary": _public_text(result.error_summary),
        }
        return NormalizedEvaluation(
            status=result.status,
            correct=result.correct,
            score=result.best_validation_score if result.correct else None,
            public_feedback=feedback,
            actual_usage=ResourceVector(
                evaluator_transactions=1,
                cpu_evaluator_seconds=min(result.evaluator_seconds, 300.0),
            ),
            evidence_sha256=_canonical_sha(result.to_dict()),
        )


class SWEPerfEvaluationBackend:
    reservation = ResourceVector(
        evaluator_transactions=1, cpu_evaluator_seconds=3600.0
    )

    def __init__(self, *, adapter: SWEPerfAdapter) -> None:
        self.adapter = adapter

    def evaluate(self, artifact_path: Path, private_dir: Path) -> NormalizedEvaluation:
        del private_dir  # The injected Docker executor owns the private result channel.
        result = self.adapter.evaluate(artifact_path)
        payload = result.public_feedback()
        return NormalizedEvaluation(
            status=result.status.value,
            correct=result.correct,
            score=result.score if result.correct else None,
            public_feedback=payload,
            actual_usage=ResourceVector(
                evaluator_transactions=1,
                cpu_evaluator_seconds=min(result.evaluator_seconds, 3600.0),
            ),
            evidence_sha256=_canonical_sha(payload),
        )


class SWEBenchVerifiedEvaluationBackend:
    reservation = ResourceVector(
        evaluator_transactions=1, cpu_evaluator_seconds=3600.0
    )

    def __init__(self, *, adapter: SWEBenchVerifiedRemoteAdapter) -> None:
        self.adapter = adapter

    def evaluate(self, artifact_path: Path, private_dir: Path) -> NormalizedEvaluation:
        private_dir.mkdir(parents=True, exist_ok=True)
        result = self.adapter.evaluate(artifact_path, private_dir / "supervisor.json")
        payload = result.to_dict()
        feedback = {
            "status": result.status,
            "valid_scored": result.valid_scored,
            "resolved": result.resolved,
            "score": result.score,
            "fail_to_pass": {
                "passed": result.fail_to_pass_passed,
                "total": result.fail_to_pass_total,
            },
            "pass_to_pass": {
                "passed": result.pass_to_pass_passed,
                "total": result.pass_to_pass_total,
            },
            "error_type": result.error_type,
            "error_summary": _public_text(result.error_summary),
            "trust_grade": result.trust_grade,
        }
        return NormalizedEvaluation(
            status=result.status,
            correct=result.valid_scored,
            score=result.score if result.valid_scored else None,
            public_feedback=feedback,
            actual_usage=ResourceVector(
                evaluator_transactions=1,
                cpu_evaluator_seconds=min(result.evaluator_seconds, 3600.0),
            ),
            evidence_sha256=_canonical_sha(payload),
        )


def environment_invalid(evaluation: NormalizedEvaluation) -> bool:
    return evaluation.status in {
        KernelEvaluationStatus.ENVIRONMENT_INVALID.value,
        "environment_invalid",
    }
