from __future__ import annotations

from pathlib import Path
from typing import Any

from optimization_lab.adapters.base import BenchmarkAdapter
from optimization_lab.campaign import (
    ACTIVE_TASK_IDS,
    BASELINE_KINDS,
    P1_ROUNDS,
    CampaignPlan,
)
from optimization_lab.controller import CampaignController
from optimization_lab.dashboard import Dashboard
from optimization_lab.generation import CandidateGenerator
from optimization_lab.registry import ExperimentRegistry
from optimization_lab.task_spec import TaskSpec


class P1EnvironmentBlocked(RuntimeError):
    pass


class P1CampaignRunner:
    """Run only the frozen P1 matrix; this class has no P2 entry point."""

    def __init__(
        self,
        *,
        plan: CampaignPlan,
        project_root: Path,
        registry: ExperimentRegistry,
        dashboard: Dashboard,
        generator: CandidateGenerator,
        adapter: BenchmarkAdapter,
        tasks: dict[str, TaskSpec],
        task_cards: dict[str, str],
        reference_sources: dict[str, str],
    ):
        if not plan.execution_ready:
            raise ValueError(f"campaign is not ready: {', '.join(plan.blockers)}")
        if set(tasks) != set(ACTIVE_TASK_IDS):
            raise ValueError("P1 runner requires exactly the two frozen tasks")
        if set(task_cards) != set(tasks) or set(reference_sources) != set(tasks):
            raise ValueError("P1 task inputs are incomplete")
        self.plan = plan
        self.project_root = project_root.resolve()
        self.registry = registry
        self.dashboard = dashboard
        self.generator = generator
        self.adapter = adapter
        self.tasks = tasks
        self.task_cards = task_cards
        self.reference_sources = reference_sources

    def run(self) -> dict[str, Any]:
        self.registry.append(
            "phase_changed",
            {"phase": "P1", "status": "in_progress", "detail": "运行六组冻结基线"},
            event_id="phase:P1:started",
        )
        cards = []
        for task_id in ACTIVE_TASK_IDS:
            task = self.tasks[task_id]
            for kind in BASELINE_KINDS:
                lane = next(
                    lane
                    for lane in self.plan.baselines
                    if lane.task_id == task_id and lane.kind == kind
                )
                controller = CampaignController(
                    plan=self.plan,
                    project_root=self.project_root,
                    registry=self.registry,
                    dashboard=self.dashboard,
                    generator=self.generator,
                    adapter=self.adapter,
                    budget_scope_lane_id=lane.lane_id,
                )
                lane_cards = []
                previous_candidate = None
                for round_number in range(1, P1_ROUNDS[kind] + 1):
                    candidate_id = self._candidate_id(task_id, kind, round_number)
                    card = controller.run_p1_candidate(
                        lane_id=lane.lane_id,
                        task=task,
                        task_card=self.task_cards[task_id],
                        reference_source=self.reference_sources[task_id],
                        candidate_id=candidate_id,
                        feedback_history=tuple(lane_cards),
                        previous_candidate=previous_candidate,
                    )
                    cards.append(card)
                    lane_cards.append(card)
                    candidate_path = (
                        Path(self.plan.artifact_root)
                        / lane.history_scope
                        / "candidates"
                        / f"{candidate_id}.py"
                    )
                    previous_candidate = candidate_path.read_text(encoding="utf-8")
                    if not card.valid_run:
                        raise P1EnvironmentBlocked(
                            f"environment invalid in {lane.lane_id}: {candidate_id}"
                        )
        self.registry.append(
            "phase_changed",
            {"phase": "P1", "status": "completed", "detail": "六组冻结基线已完成"},
            event_id="phase:P1:completed",
        )
        self.dashboard.render(self.registry)
        return {
            "lane_count": len(self.plan.baselines),
            "candidate_count": len(cards),
            "correct_count": sum(card.correct for card in cards),
        }

    @staticmethod
    def _candidate_id(task_id: str, kind: str, round_number: int) -> str:
        task_label = {
            "kernelbench_layernorm": "layernorm",
            "kernelbench_matmul_sigmoid_sum": "matmul-sigmoid-sum",
        }[task_id]
        kind_label = {
            "generic_zero_shot": "zero-shot",
            "equal_budget_general": "equal-general",
            "manual_naive": "manual-naive",
        }[kind]
        return f"p1-{task_label}-{kind_label}-v{round_number:03d}"
