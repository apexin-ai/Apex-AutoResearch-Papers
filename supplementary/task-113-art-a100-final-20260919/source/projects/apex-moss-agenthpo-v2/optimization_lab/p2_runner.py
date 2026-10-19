from __future__ import annotations

import hashlib
from pathlib import Path
from typing import Any

from optimization_lab.adapters.base import BenchmarkAdapter
from optimization_lab.campaign import ACTIVE_TASK_IDS, CampaignPlan, LineagePlan
from optimization_lab.controller import CampaignController, IncompleteHarnessGeneration
from optimization_lab.dashboard import Dashboard
from optimization_lab.feedback import FeedbackCard
from optimization_lab.generation import CandidateGenerator
from optimization_lab.harness_evolution import HarnessArchive, HarnessVersion
from optimization_lab.optimizer import LineageTracker
from optimization_lab.registry import ExperimentRegistry
from optimization_lab.task_spec import TaskSpec


class P2EnvironmentBlocked(RuntimeError):
    pass


class P2CampaignRunner:
    """Run only the frozen P2 Harness lineages; no P3 entry point exists."""

    def __init__(
        self,
        *,
        plan: CampaignPlan,
        project_root: Path,
        registry: ExperimentRegistry,
        dashboard: Dashboard,
        candidate_generator: CandidateGenerator,
        harness_generator: CandidateGenerator,
        adapter: BenchmarkAdapter,
        tasks: dict[str, TaskSpec],
        task_cards: dict[str, str],
        reference_sources: dict[str, str],
    ):
        if not plan.execution_ready:
            raise ValueError(f"campaign is not ready: {', '.join(plan.blockers)}")
        if set(tasks) != set(ACTIVE_TASK_IDS):
            raise ValueError("P2 runner requires exactly the two frozen tasks")
        if set(task_cards) != set(tasks) or set(reference_sources) != set(tasks):
            raise ValueError("P2 task inputs are incomplete")
        if not self._p1_completed(registry):
            raise ValueError("P2 cannot start before the audited P1 completion event")
        self.plan = plan
        self.project_root = project_root.resolve()
        self.registry = registry
        self.dashboard = dashboard
        self.candidate_generator = candidate_generator
        self.harness_generator = harness_generator
        self.adapter = adapter
        self.tasks = tasks
        self.task_cards = task_cards
        self.reference_sources = reference_sources

    def run(self) -> dict[str, Any]:
        self.registry.append(
            "phase_changed",
            {
                "phase": "P2",
                "status": "in_progress",
                "detail": "运行六条任务专用 Harness 隔离谱系",
            },
            event_id="phase:P2:started",
        )
        for lineage in self.plan.lineages:
            self._run_lineage(lineage)
        self.registry.append(
            "phase_changed",
            {
                "phase": "P2",
                "status": "completed",
                "detail": "六条任务专用 Harness 谱系已停止并冻结",
            },
            event_id="phase:P2:completed",
        )
        self.dashboard.render(self.registry)
        cards = self._all_effective_cards()
        return {
            "lineage_count": len(self.plan.lineages),
            "candidate_count": len(cards),
            "correct_count": sum(card.correct for card in cards),
            "harness_model_calls": sum(
                event["event_type"] == "harness_generated"
                for event in self.registry.read_events()
            ),
        }

    def _run_lineage(self, lineage: LineagePlan) -> None:
        task = self.tasks[lineage.task_id]
        lane_id = _lane_id(lineage)
        archive = HarnessArchive(
            Path(self.plan.artifact_root) / lineage.history_scope
        )
        seed_path = (self.project_root / lineage.seed_path).resolve()
        if not seed_path.is_relative_to(self.project_root) or not seed_path.is_file():
            raise ValueError("P2 seed Harness is missing or escapes the project")
        seed = archive.store_seed(
            seed_path.read_text(encoding="utf-8"),
            expected_sha256=lineage.seed_sha256,
        )
        self.registry.append(
            "p2_lineage_started",
            {
                "lane_id": lane_id,
                "task_id": task.task_id,
                "lineage_id": lineage.lineage_id,
                "seed_harness_sha256": seed.sha256,
                "max_rounds": lineage.max_rounds,
            },
            event_id=f"p2-lineage-started:{_identity(lane_id)}",
        )
        cards = self._effective_lineage_cards(lane_id, task.task_id)
        tracker = LineageTracker(task_id=task.task_id, max_rounds=lineage.max_rounds)
        for card in cards:
            if not card.valid_run:
                raise P2EnvironmentBlocked(
                    f"environment invalid in {lane_id}: {card.candidate_id}"
                )
            tracker.record(card)

        controller = CampaignController(
            plan=self.plan,
            project_root=self.project_root,
            registry=self.registry,
            dashboard=self.dashboard,
            generator=self.candidate_generator,
            harness_generator=self.harness_generator,
            adapter=self.adapter,
            budget_scope_lane_id=lane_id,
        )
        recovery_stop_reason: str | None = None
        while not tracker.should_stop:
            round_number = tracker.valid_rounds + 1
            try:
                harness_version = self._harness_for_round(
                    controller=controller,
                    archive=archive,
                    lineage=lineage,
                    task=task,
                    lane_id=lane_id,
                    round_number=round_number,
                    cards=tuple(cards),
                    tracker=tracker,
                )
            except IncompleteHarnessGeneration as exc:
                recovery_stop_reason = "incomplete_harness_generation_preserved"
                self.registry.append(
                    "p2_lineage_recovery_stopped",
                    {
                        "lane_id": lane_id,
                        "task_id": task.task_id,
                        "lineage_id": lineage.lineage_id,
                        "next_round_number": round_number,
                        "reason": recovery_stop_reason,
                        "detail": str(exc),
                        "budget": controller.budget.to_dict(),
                    },
                    event_id=(
                        f"p2-lineage-recovery-stopped:{_identity(lane_id)}:"
                        f"{round_number:03d}"
                    ),
                )
                self.dashboard.render(self.registry)
                break
            candidate_id = _candidate_id(task.task_id, lineage.lineage_id, round_number)
            previous_candidate = self._candidate_source(lineage, cards[-1].candidate_id) if cards else None
            best_candidate = (
                self._candidate_source(lineage, tracker.best_candidate_id)
                if tracker.best_candidate_id
                else None
            )
            card = controller.run_p2_candidate(
                lane_id=lane_id,
                task=task,
                task_card=self.task_cards[task.task_id],
                reference_source=self.reference_sources[task.task_id],
                candidate_id=candidate_id,
                harness_version=harness_version,
                feedback_history=tuple(cards),
                previous_candidate=previous_candidate,
                best_candidate_id=tracker.best_candidate_id,
                best_candidate=best_candidate,
            )
            if not card.valid_run:
                raise P2EnvironmentBlocked(
                    f"environment invalid in {lane_id}: {candidate_id}"
                )
            tracker.record(card)
            cards.append(card)
            self.registry.append(
                "p2_lineage_round_completed",
                {
                    "lane_id": lane_id,
                    "task_id": task.task_id,
                    "lineage_id": lineage.lineage_id,
                    "round_number": round_number,
                    "harness_version_id": harness_version.version_id,
                    "harness_sha256": harness_version.sha256,
                    "candidate_id": candidate_id,
                    "feedback": card.to_dict(),
                    "tracker": tracker.to_dict(),
                    "budget": controller.budget.to_dict(),
                },
                event_id=f"p2-lineage-round:{_identity(lane_id)}:{round_number:03d}",
            )
            self.dashboard.render(self.registry)

        best_harness = _version_from_candidate(tracker.best_candidate_id)
        self.registry.append(
            "p2_lineage_completed",
            {
                "lane_id": lane_id,
                "task_id": task.task_id,
                "lineage_id": lineage.lineage_id,
                "valid_rounds": tracker.valid_rounds,
                "stop_reason": recovery_stop_reason or tracker.stop_reason,
                "best_candidate_id": tracker.best_candidate_id,
                "best_harness_version_id": best_harness,
                "best_speedup": tracker.best_speedup,
                "budget": controller.budget.to_dict(),
            },
            event_id=f"p2-lineage-completed:{_identity(lane_id)}",
        )
        self.dashboard.render(self.registry)

    def _harness_for_round(
        self,
        *,
        controller: CampaignController,
        archive: HarnessArchive,
        lineage: LineagePlan,
        task: TaskSpec,
        lane_id: str,
        round_number: int,
        cards: tuple[FeedbackCard, ...],
        tracker: LineageTracker,
    ) -> HarnessVersion:
        target = f"v{round_number:03d}"
        if round_number == 1:
            return archive.load(target)
        current = archive.load(f"v{round_number - 1:03d}")
        return controller.propose_p2_harness(
            lane_id=lane_id,
            task=task,
            task_card=self.task_cards[task.task_id],
            target_version_id=target,
            current_harness=current,
            feedback_history=cards,
            best_candidate_id=tracker.best_candidate_id,
            best_speedup=tracker.best_speedup,
        )

    def _candidate_source(self, lineage: LineagePlan, candidate_id: str) -> str:
        path = (
            Path(self.plan.artifact_root)
            / lineage.history_scope
            / "candidates"
            / f"{candidate_id}.py"
        ).resolve()
        root = (Path(self.plan.artifact_root) / lineage.history_scope / "candidates").resolve()
        if not path.is_relative_to(root) or not path.is_file():
            raise ValueError("P2 candidate archive is incomplete")
        return path.read_text(encoding="utf-8")

    def _effective_lineage_cards(
        self, lane_id: str, task_id: str
    ) -> list[FeedbackCard]:
        effective: dict[str, dict[str, Any]] = {}
        order: list[str] = []
        for event in self.registry.read_events():
            if event["event_type"] not in {
                "p2_candidate_completed",
                "candidate_evaluation_corrected",
            }:
                continue
            payload = event["payload"]
            if payload.get("lane_id") != lane_id or payload.get("task_id") != task_id:
                continue
            candidate_id = str(payload.get("candidate_id", ""))
            if not candidate_id.startswith("p2-"):
                continue
            if candidate_id not in effective:
                order.append(candidate_id)
            effective[candidate_id] = payload["feedback"]
        return [FeedbackCard(**effective[candidate_id]) for candidate_id in order]

    def _all_effective_cards(self) -> list[FeedbackCard]:
        cards = []
        for lineage in self.plan.lineages:
            cards.extend(
                self._effective_lineage_cards(_lane_id(lineage), lineage.task_id)
            )
        return cards

    @staticmethod
    def _p1_completed(registry: ExperimentRegistry) -> bool:
        return any(
            event["event_type"] == "phase_changed"
            and event["payload"].get("phase") == "P1"
            and event["payload"].get("status") == "completed"
            for event in registry.read_events()
        )


def _lane_id(lineage: LineagePlan) -> str:
    return f"p2:{lineage.task_id}:{lineage.lineage_id}"


def _candidate_id(task_id: str, lineage_id: str, round_number: int) -> str:
    task_label = {
        "kernelbench_layernorm": "layernorm",
        "kernelbench_matmul_sigmoid_sum": "matmul-sigmoid-sum",
    }[task_id]
    return f"p2-{task_label}-{lineage_id}-v{round_number:03d}"


def _version_from_candidate(candidate_id: str | None) -> str | None:
    return candidate_id.rsplit("-", 1)[-1] if candidate_id else None


def _identity(value: str) -> str:
    return hashlib.sha256(value.encode()).hexdigest()[:20]
