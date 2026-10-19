from __future__ import annotations

import json
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any


@dataclass(frozen=True)
class TaskSpec:
    task_id: str
    display_name: str
    level: int
    problem_id: int
    task_path: str
    task_sha256: str
    repository_commit: str
    target_gpu: str
    gpu_arch: str
    backend: str = "triton"
    precision: str = "fp32"
    correctness_trials: int = 5
    performance_trials: int = 100
    timeout_seconds: int = 300

    def __post_init__(self) -> None:
        if not self.task_id or not self.display_name:
            raise ValueError("task identity cannot be empty")
        if self.level < 1 or self.problem_id < 1:
            raise ValueError("KernelBench level and problem id must be positive")
        if len(self.task_sha256) != 64 or len(self.repository_commit) != 40:
            raise ValueError("task and repository hashes must be pinned")
        if self.correctness_trials < 1 or self.performance_trials < 1:
            raise ValueError("evaluation trials must be positive")

    @classmethod
    def from_json(cls, path: Path) -> "TaskSpec":
        data = json.loads(path.read_text(encoding="utf-8"))
        if not isinstance(data, dict):
            raise ValueError(f"task protocol must be an object: {path}")
        return cls(**data)

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)
