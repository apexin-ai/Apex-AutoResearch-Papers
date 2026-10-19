from __future__ import annotations

from pathlib import Path

from optimization_lab.adapters.base import BenchmarkAdapter, EvaluationResult
from optimization_lab.task_spec import TaskSpec


class FakeAdapter(BenchmarkAdapter):
    """Deterministic adapter for contract tests; it never uses a GPU or API."""

    def __init__(self, result: EvaluationResult):
        self.result = result
        self.calls: list[tuple[str, Path]] = []

    def estimated_gpu_seconds(self, task: TaskSpec) -> float:
        return self.result.gpu_seconds

    def evaluate(
        self,
        task: TaskSpec,
        candidate_path: Path,
        private_log_dir: Path,
    ) -> EvaluationResult:
        self.calls.append((task.task_id, candidate_path))
        private_log_dir.mkdir(parents=True, exist_ok=True)
        return self.result
