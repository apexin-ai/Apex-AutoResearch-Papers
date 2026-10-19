from __future__ import annotations

import hashlib
import re
from pathlib import Path

from optimization_lab.adapters.base import BenchmarkAdapter
from optimization_lab.budget import ExperimentBudget
from optimization_lab.dashboard import Dashboard
from optimization_lab.feedback import FeedbackCard
from optimization_lab.registry import ExperimentRegistry
from optimization_lab.task_spec import TaskSpec


class ExperimentRunner:
    def __init__(
        self,
        *,
        registry: ExperimentRegistry,
        adapter: BenchmarkAdapter,
        dashboard: Dashboard,
        budget: ExperimentBudget,
    ):
        self.registry = registry
        self.adapter = adapter
        self.dashboard = dashboard
        self.budget = budget

    def evaluate(
        self,
        task: TaskSpec,
        candidate_path: Path,
        *,
        candidate_id: str,
    ) -> FeedbackCard:
        if not re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9._-]{0,127}", candidate_id):
            raise ValueError("candidate id must be a safe, single path component")
        candidate_path = candidate_path.resolve()
        if not candidate_path.is_file() or candidate_path.suffix != ".py":
            raise ValueError("candidate must be an existing Python file")
        candidate_sha = hashlib.sha256(candidate_path.read_bytes()).hexdigest()
        existing_events = self.registry.read_events()
        for event in existing_events:
            if event["event_type"] != "candidate_started":
                continue
            payload = event["payload"]
            if (
                payload["task_id"] == task.task_id
                and payload["candidate_id"] == candidate_id
                and payload["candidate_sha256"] != candidate_sha
            ):
                raise ValueError("candidate id is already bound to different content")
        for event in existing_events:
            if event["event_type"] != "candidate_evaluated":
                continue
            payload = event["payload"]
            feedback = payload["feedback"]
            if (
                feedback["task_id"] == task.task_id
                and feedback["candidate_id"] == candidate_id
                and payload["candidate_sha256"] == candidate_sha
            ):
                self.dashboard.render(self.registry)
                return FeedbackCard(**feedback)
        self.registry.append(
            "candidate_started",
            {
                "task_id": task.task_id,
                "candidate_id": candidate_id,
                "candidate_sha256": candidate_sha,
            },
            event_id=f"candidate-started:{task.task_id}:{candidate_id}:{candidate_sha}",
        )
        reserved_gpu_seconds = self.adapter.estimated_gpu_seconds(task)
        self.budget.reserve(gpu_seconds=reserved_gpu_seconds)
        private_log_dir = self.registry.root / "private_evaluator" / candidate_id
        try:
            result = self.adapter.evaluate(task, candidate_path, private_log_dir)
        except Exception:
            self.budget.settle_gpu(
                reserved_seconds=reserved_gpu_seconds,
                actual_seconds=0.0,
            )
            self.dashboard.render(self.registry)
            raise
        self.budget.settle_gpu(
            reserved_seconds=reserved_gpu_seconds,
            actual_seconds=result.gpu_seconds,
        )
        card = FeedbackCard.from_result(task, candidate_id, result)
        self.registry.append(
            "candidate_evaluated",
            {
                "task": task.to_dict(),
                "candidate_sha256": candidate_sha,
                "evaluation": result.to_dict(),
                "feedback": card.to_dict(),
                "budget": self.budget.to_dict(),
            },
            event_id=f"candidate-evaluated:{task.task_id}:{candidate_id}:{candidate_sha}",
        )
        self.dashboard.render(self.registry)
        return card
