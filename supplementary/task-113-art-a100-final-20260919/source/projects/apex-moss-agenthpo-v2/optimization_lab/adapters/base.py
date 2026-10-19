from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import asdict, dataclass
from enum import Enum
from pathlib import Path
from typing import Any

from optimization_lab.task_spec import TaskSpec


class EvaluationStatus(str, Enum):
    VALID = "valid"
    COMPILE_FAILED = "compile_failed"
    INCORRECT = "incorrect"
    POLICY_REJECTED = "policy_rejected"
    TIMEOUT = "timeout"
    ENVIRONMENT_INVALID = "environment_invalid"


@dataclass(frozen=True)
class EvaluationResult:
    status: EvaluationStatus
    compiled: bool
    correct: bool
    candidate_runtime_ms: float | None = None
    reference_runtime_ms: float | None = None
    reference_compile_runtime_ms: float | None = None
    error_summary: str = ""
    elapsed_seconds: float = 0.0
    gpu_seconds: float = 0.0
    hardware: str = ""
    raw_log_path: str = ""

    def __post_init__(self) -> None:
        if self.correct and not self.compiled:
            raise ValueError("a correct candidate must have compiled")
        runtimes = (self.candidate_runtime_ms, self.reference_runtime_ms)
        if any(value is not None for value in runtimes) and not self.correct:
            raise ValueError("runtime is only valid for a correct candidate")
        if self.status is EvaluationStatus.VALID:
            if not self.correct or any(value is None for value in runtimes):
                raise ValueError("valid result requires a correct candidate and runtimes")
        for value in (
            self.candidate_runtime_ms,
            self.reference_runtime_ms,
            self.reference_compile_runtime_ms,
        ):
            if value is not None and value <= 0:
                raise ValueError("runtime values must be positive")
        if self.elapsed_seconds < 0 or self.gpu_seconds < 0:
            raise ValueError("time accounting cannot be negative")

    @property
    def speedup_vs_eager(self) -> float | None:
        if self.candidate_runtime_ms is None or self.reference_runtime_ms is None:
            return None
        return self.reference_runtime_ms / self.candidate_runtime_ms

    def to_dict(self) -> dict[str, Any]:
        data = asdict(self)
        data["status"] = self.status.value
        data["speedup_vs_eager"] = self.speedup_vs_eager
        return data


class BenchmarkAdapter(ABC):
    @abstractmethod
    def evaluate(
        self,
        task: TaskSpec,
        candidate_path: Path,
        private_log_dir: Path,
    ) -> EvaluationResult:
        """Evaluate one candidate without exposing private scorer logs to the agent."""

    def estimated_gpu_seconds(self, task: TaskSpec) -> float:
        """Conservative amount reserved before a run starts."""
        return float(task.timeout_seconds)
