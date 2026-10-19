from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

from optimization_lab.feedback import FeedbackCard


@dataclass
class LineageTracker:
    """Mechanical P2 selection and stopping rules for one isolated lineage."""

    task_id: str
    max_rounds: int = 8
    valid_rounds: int = 0
    invalid_environment_runs: int = 0
    best_candidate_id: str | None = None
    best_speedup: float | None = None
    stop_reason: str | None = None
    _candidate_ids: set[str] = field(default_factory=set, repr=False)
    _recent_correct: list[bool] = field(default_factory=list, repr=False)
    _recent_improved: list[bool] = field(default_factory=list, repr=False)

    def __post_init__(self) -> None:
        if not self.task_id:
            raise ValueError("lineage task is required")
        if self.max_rounds < 1:
            raise ValueError("lineage round cap must be positive")

    @property
    def should_stop(self) -> bool:
        return self.stop_reason is not None

    def record(self, card: FeedbackCard) -> None:
        if self.should_stop:
            raise RuntimeError(f"lineage already stopped: {self.stop_reason}")
        if card.task_id != self.task_id:
            raise ValueError("feedback task does not match lineage task")
        if card.candidate_id in self._candidate_ids:
            raise ValueError("candidate id already exists in this lineage")
        self._candidate_ids.add(card.candidate_id)
        if not card.valid_run:
            self.invalid_environment_runs += 1
            return
        if card.correct and card.speedup_vs_eager is None:
            raise ValueError("correct feedback requires a speed measurement")

        self.valid_rounds += 1
        improved = False
        if card.correct and (
            self.best_speedup is None or card.speedup_vs_eager > self.best_speedup
        ):
            self.best_candidate_id = card.candidate_id
            self.best_speedup = card.speedup_vs_eager
            improved = True
        self._recent_correct.append(card.correct)
        self._recent_improved.append(improved)

        if self.valid_rounds >= self.max_rounds:
            self.stop_reason = "maximum_rounds_reached"
            return
        if len(self._recent_correct) >= 3 and not any(self._recent_correct[-3:]):
            self.stop_reason = "three_rounds_without_correct_candidate"
            return
        if len(self._recent_improved) >= 3 and not any(self._recent_improved[-3:]):
            self.stop_reason = "three_rounds_without_speed_improvement"

    def to_dict(self) -> dict[str, Any]:
        return {
            "schema_version": 1,
            "task_id": self.task_id,
            "max_rounds": self.max_rounds,
            "valid_rounds": self.valid_rounds,
            "invalid_environment_runs": self.invalid_environment_runs,
            "best_candidate_id": self.best_candidate_id,
            "best_speedup": self.best_speedup,
            "stop_reason": self.stop_reason,
            "candidate_ids": sorted(self._candidate_ids),
            "recent_correct": list(self._recent_correct),
            "recent_improved": list(self._recent_improved),
        }

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> "LineageTracker":
        if data.get("schema_version") != 1:
            raise ValueError("unsupported lineage state schema")
        tracker = cls(
            task_id=str(data["task_id"]),
            max_rounds=int(data["max_rounds"]),
            valid_rounds=int(data["valid_rounds"]),
            invalid_environment_runs=int(data["invalid_environment_runs"]),
            best_candidate_id=data.get("best_candidate_id"),
            best_speedup=data.get("best_speedup"),
            stop_reason=data.get("stop_reason"),
        )
        tracker._candidate_ids = set(data.get("candidate_ids", []))
        tracker._recent_correct = list(data.get("recent_correct", []))
        tracker._recent_improved = list(data.get("recent_improved", []))
        if len(tracker._recent_correct) != tracker.valid_rounds:
            raise ValueError("lineage correctness history does not match round count")
        if len(tracker._recent_improved) != tracker.valid_rounds:
            raise ValueError("lineage improvement history does not match round count")
        return tracker
