from __future__ import annotations

import hashlib
import re
from pathlib import Path
from typing import Any

from optimization_lab.adapters.base import BenchmarkAdapter
from optimization_lab.budget import ExperimentBudget
from optimization_lab.campaign import BaselineLane, CampaignPlan, LineagePlan
from optimization_lab.dashboard import Dashboard
from optimization_lab.feedback import FeedbackCard
from optimization_lab.generation import (
    CandidateArchive,
    CandidateGenerator,
    GeneratedCandidate,
    GenerationRequest,
    InvalidCandidate,
)
from optimization_lab.harness_evolution import (
    HarnessArchive,
    HarnessEvolutionRequest,
    HarnessVersion,
    InvalidHarness,
)
from optimization_lab.registry import ExperimentRegistry
from optimization_lab.runner import ExperimentRunner
from optimization_lab.task_spec import TaskSpec


class CampaignNotReady(RuntimeError):
    pass


class IncompleteHarnessGeneration(RuntimeError):
    """A prior Harness model call started but produced no auditable artifact."""


class CampaignController:
    """Exactly-once skeleton for one P1 candidate in a frozen campaign lane."""

    def __init__(
        self,
        *,
        plan: CampaignPlan,
        project_root: Path,
        registry: ExperimentRegistry,
        dashboard: Dashboard,
        generator: CandidateGenerator,
        harness_generator: CandidateGenerator | None = None,
        adapter: BenchmarkAdapter,
        budget_scope_lane_id: str | None = None,
    ):
        self.plan = plan
        self.project_root = project_root.resolve()
        self.registry = registry
        self.dashboard = dashboard
        self.generator = generator
        self.harness_generator = harness_generator
        self.adapter = adapter
        self.budget_scope_lane_id = budget_scope_lane_id
        restored = self._restored_usage(budget_scope_lane_id)
        self.budget = ExperimentBudget(
            max_gpu_seconds=float(plan.gpu_seconds_cap_per_lane or 0.0),
            max_model_calls=int(plan.model_call_cap_per_lane or 0),
            max_api_cost_usd=plan.api_dollar_cap,
            max_gpu_cost_usd=plan.gpu_dollar_cap,
            **restored,
        )

    def run_p1_candidate(
        self,
        *,
        lane_id: str,
        task: TaskSpec,
        task_card: str,
        reference_source: str,
        candidate_id: str,
        feedback_history: tuple[FeedbackCard, ...] = (),
        previous_candidate: str | None = None,
    ) -> FeedbackCard:
        if not self.plan.execution_ready:
            blockers = ", ".join(self.plan.blockers)
            raise CampaignNotReady(
                f"campaign execution_ready is false; blockers: {blockers}"
            )
        _validate_candidate_id(candidate_id)
        if self.budget_scope_lane_id is not None and lane_id != self.budget_scope_lane_id:
            raise ValueError("candidate lane does not match controller budget scope")
        lane = self._baseline_lane(lane_id, task.task_id)

        corrected = self._find_event(
            "candidate_evaluation_corrected", lane_id, task.task_id, candidate_id
        )
        if corrected is not None:
            self.dashboard.render(self.registry)
            return FeedbackCard(**corrected["payload"]["feedback"])

        completed = self._find_event(
            "lane_candidate_completed", lane_id, task.task_id, candidate_id
        )
        if completed is not None:
            self.dashboard.render(self.registry)
            return FeedbackCard(**completed["payload"]["feedback"])

        archive = CandidateArchive(Path(self.plan.artifact_root), lane.history_scope)
        generated = self._find_event(
            "candidate_generated", lane_id, task.task_id, candidate_id
        )
        if generated is None:
            rejected = self._find_event(
                "candidate_generation_rejected", lane_id, task.task_id, candidate_id
            )
            failed = self._find_event(
                "candidate_generation_failed", lane_id, task.task_id, candidate_id
            )
            if rejected is not None or failed is not None:
                event = rejected or failed
                raise InvalidCandidate(event["payload"]["error"])
            started = self._find_event(
                "generation_started", lane_id, task.task_id, candidate_id
            )
            if started is not None:
                raise RuntimeError(
                    "generation was already started for this candidate id; "
                    "refusing a second model call"
                )
            generated = self._generate_candidate(
                lane_id=lane.lane_id,
                task=task,
                task_card=task_card,
                reference_source=reference_source,
                candidate_id=candidate_id,
                archive=archive,
                feedback_history=feedback_history,
                previous_candidate=previous_candidate,
                best_candidate_id=None,
                best_candidate=None,
                harness_text=self._baseline_harness(lane),
            )

        candidate_path = Path(generated["payload"]["archive"]["candidate_path"])
        self._verify_archived_candidate(
            candidate_path,
            str(generated["payload"]["candidate_sha256"]),
            archive,
        )
        runner = ExperimentRunner(
            registry=self.registry,
            adapter=self.adapter,
            dashboard=self.dashboard,
            budget=self.budget,
        )
        card = runner.evaluate(task, candidate_path, candidate_id=candidate_id)
        payload = {
            "lane_id": lane.lane_id,
            "task_id": task.task_id,
            "candidate_id": candidate_id,
            "candidate_sha256": generated["payload"]["candidate_sha256"],
            "feedback": card.to_dict(),
            "budget": self.budget.to_dict(),
        }
        self.registry.append(
            "lane_candidate_completed",
            payload,
            event_id=_event_id("lane-completed", lane.lane_id, task.task_id, candidate_id),
        )
        self.dashboard.render(self.registry)
        return card

    def run_p2_candidate(
        self,
        *,
        lane_id: str,
        task: TaskSpec,
        task_card: str,
        reference_source: str,
        candidate_id: str,
        harness_version: HarnessVersion,
        feedback_history: tuple[FeedbackCard, ...],
        previous_candidate: str | None,
        best_candidate_id: str | None,
        best_candidate: str | None,
    ) -> FeedbackCard:
        self._require_ready_lane(lane_id)
        _validate_candidate_id(candidate_id)
        lineage = self._lineage(lane_id, task.task_id)
        archive = CandidateArchive(Path(self.plan.artifact_root), lineage.history_scope)
        harness_archive = HarnessArchive(
            Path(self.plan.artifact_root) / lineage.history_scope
        )
        archived_harness = harness_archive.load(harness_version.version_id)
        if archived_harness != harness_version:
            raise ValueError("P2 candidate Harness does not match its immutable archive")

        corrected = self._find_event(
            "candidate_evaluation_corrected", lane_id, task.task_id, candidate_id
        )
        if corrected is not None:
            self.dashboard.render(self.registry)
            return FeedbackCard(**corrected["payload"]["feedback"])
        completed = self._find_event(
            "p2_candidate_completed", lane_id, task.task_id, candidate_id
        )
        if completed is not None:
            self.dashboard.render(self.registry)
            return FeedbackCard(**completed["payload"]["feedback"])

        generated = self._find_event(
            "candidate_generated", lane_id, task.task_id, candidate_id
        )
        if generated is None:
            rejected = self._find_event(
                "candidate_generation_rejected", lane_id, task.task_id, candidate_id
            )
            failed = self._find_event(
                "candidate_generation_failed", lane_id, task.task_id, candidate_id
            )
            if rejected is not None or failed is not None:
                event = rejected or failed
                raise InvalidCandidate(event["payload"]["error"])
            if self._find_event(
                "generation_started", lane_id, task.task_id, candidate_id
            ) is not None:
                raise RuntimeError(
                    "generation was already started for this candidate id; "
                    "refusing a second model call"
                )
            generated = self._generate_candidate(
                lane_id=lane_id,
                task=task,
                task_card=task_card,
                reference_source=reference_source,
                candidate_id=candidate_id,
                archive=archive,
                feedback_history=feedback_history,
                previous_candidate=previous_candidate,
                best_candidate_id=best_candidate_id,
                best_candidate=best_candidate,
                harness_text=harness_version.text,
            )

        candidate_path = Path(generated["payload"]["archive"]["candidate_path"])
        self._verify_archived_candidate(
            candidate_path,
            str(generated["payload"]["candidate_sha256"]),
            archive,
        )
        runner = ExperimentRunner(
            registry=self.registry,
            adapter=self.adapter,
            dashboard=self.dashboard,
            budget=self.budget,
        )
        card = runner.evaluate(task, candidate_path, candidate_id=candidate_id)
        self.registry.append(
            "p2_candidate_completed",
            {
                "lane_id": lane_id,
                "task_id": task.task_id,
                "candidate_id": candidate_id,
                "candidate_sha256": generated["payload"]["candidate_sha256"],
                "harness_version_id": harness_version.version_id,
                "harness_sha256": harness_version.sha256,
                "feedback": card.to_dict(),
                "budget": self.budget.to_dict(),
            },
            event_id=_event_id("p2-candidate-completed", lane_id, task.task_id, candidate_id),
        )
        self.dashboard.render(self.registry)
        return card

    def propose_p2_harness(
        self,
        *,
        lane_id: str,
        task: TaskSpec,
        task_card: str,
        target_version_id: str,
        current_harness: HarnessVersion,
        feedback_history: tuple[FeedbackCard, ...],
        best_candidate_id: str | None,
        best_speedup: float | None,
    ) -> HarnessVersion:
        self._require_ready_lane(lane_id)
        lineage = self._lineage(lane_id, task.task_id)
        if self.harness_generator is None:
            raise RuntimeError("P2 Harness generator is not configured")
        expected_number = int(current_harness.version_id[1:]) + 1
        if target_version_id != f"v{expected_number:03d}":
            raise ValueError("P2 Harness versions must advance exactly one step")
        archive = HarnessArchive(Path(self.plan.artifact_root) / lineage.history_scope)
        if archive.load(current_harness.version_id) != current_harness:
            raise ValueError("current Harness does not match its immutable archive")
        model_call_id = _harness_model_call_id(lane_id, target_version_id)
        completed = self._find_event(
            "harness_generated", lane_id, task.task_id, model_call_id
        )
        if completed is not None:
            return archive.load(target_version_id)
        if self._find_event(
            "generation_started", lane_id, task.task_id, model_call_id
        ) is not None:
            raise IncompleteHarnessGeneration(
                "Harness generation was already started for this version; "
                "preserving the consumed attempt and refusing a second model call"
            )
        request = HarnessEvolutionRequest(
            task_id=task.task_id,
            lineage_id=lineage.lineage_id,
            target_version_id=target_version_id,
            current_harness=current_harness,
            task_card=task_card,
            feedback_history=feedback_history,
            best_candidate_id=best_candidate_id,
            best_speedup=best_speedup,
        )
        prompt = request.to_prompt()
        prompt_sha = hashlib.sha256(prompt.encode()).hexdigest()
        reserved_api_cost = self.harness_generator.estimated_api_cost_usd()
        self.budget.reserve(model_calls=1, api_cost_usd=reserved_api_cost)
        self.registry.append(
            "generation_started",
            {
                "lane_id": lane_id,
                "task_id": task.task_id,
                "candidate_id": model_call_id,
                "generation_kind": "harness",
                "harness_version_id": target_version_id,
                "executor_model": self.plan.executor_model,
                "prompt_sha256": prompt_sha,
                "reserved_api_cost_usd": reserved_api_cost,
                "budget": self.budget.to_dict(),
            },
            event_id=_event_id(
                "generation-started", lane_id, task.task_id, model_call_id
            ),
        )
        assert self.plan.executor_model is not None
        try:
            result = self.harness_generator.generate(
                prompt, model=self.plan.executor_model
            )
            self.budget.settle_api(
                reserved_cost_usd=reserved_api_cost,
                actual_cost_usd=result.api_cost_usd,
            )
            version = HarnessVersion.from_text(
                target_version_id,
                result.raw_response,
                parent_version_id=current_harness.version_id,
            )
            archive.store_generated(
                version,
                raw_response=result.raw_response,
                prompt_sha256=prompt_sha,
            )
        except Exception as exc:
            self.registry.append(
                "harness_generation_failed",
                {
                    "lane_id": lane_id,
                    "task_id": task.task_id,
                    "candidate_id": model_call_id,
                    "harness_version_id": target_version_id,
                    "error": f"{type(exc).__name__}: {exc}",
                    "budget": self.budget.to_dict(),
                },
                event_id=_event_id(
                    "harness-generation-failed", lane_id, task.task_id, model_call_id
                ),
            )
            self.dashboard.render(self.registry)
            raise
        self.registry.append(
            "harness_generated",
            {
                "lane_id": lane_id,
                "task_id": task.task_id,
                "candidate_id": model_call_id,
                "harness_version_id": version.version_id,
                "parent_version_id": version.parent_version_id,
                "harness_sha256": version.sha256,
                "prompt_sha256": prompt_sha,
                "provider": result.provider,
                "usage": result.usage,
                "audit_log_path": result.audit_log_path,
                "api_cost_usd": result.api_cost_usd,
                "budget": self.budget.to_dict(),
            },
            event_id=_event_id("harness-generated", lane_id, task.task_id, model_call_id),
        )
        self.dashboard.render(self.registry)
        return version

    def _generate_candidate(
        self,
        *,
        lane_id: str,
        task: TaskSpec,
        task_card: str,
        reference_source: str,
        candidate_id: str,
        archive: CandidateArchive,
        feedback_history: tuple[FeedbackCard, ...],
        previous_candidate: str | None,
        best_candidate_id: str | None,
        best_candidate: str | None,
        harness_text: str,
    ) -> dict[str, Any]:
        request = GenerationRequest(
            task_id=task.task_id,
            lane_id=lane_id,
            harness_text=harness_text,
            task_card=task_card,
            reference_source=reference_source,
            feedback_history=feedback_history,
            previous_candidate=previous_candidate,
            best_candidate_id=best_candidate_id,
            best_candidate=best_candidate,
        )
        prompt = request.to_prompt()
        prompt_sha = hashlib.sha256(prompt.encode()).hexdigest()
        reserved_api_cost = self.generator.estimated_api_cost_usd()
        self.budget.reserve(model_calls=1, api_cost_usd=reserved_api_cost)
        started_payload = {
            "lane_id": lane_id,
            "task_id": task.task_id,
            "candidate_id": candidate_id,
            "executor_model": self.plan.executor_model,
            "prompt_sha256": prompt_sha,
            "reserved_api_cost_usd": reserved_api_cost,
            "budget": self.budget.to_dict(),
        }
        self.registry.append(
            "generation_started",
            started_payload,
            event_id=_event_id("generation-started", lane_id, task.task_id, candidate_id),
        )
        assert self.plan.executor_model is not None
        try:
            result = self.generator.generate(prompt, model=self.plan.executor_model)
            self.budget.settle_api(
                reserved_cost_usd=reserved_api_cost,
                actual_cost_usd=result.api_cost_usd,
            )
        except Exception as exc:
            self.registry.append(
                "candidate_generation_failed",
                {
                    "lane_id": lane_id,
                    "task_id": task.task_id,
                    "candidate_id": candidate_id,
                    "error": f"{type(exc).__name__}: {exc}",
                    "budget": self.budget.to_dict(),
                },
                event_id=_event_id(
                    "generation-failed", lane_id, task.task_id, candidate_id
                ),
            )
            self.dashboard.render(self.registry)
            raise
        try:
            candidate = GeneratedCandidate.from_response(result.raw_response)
        except InvalidCandidate as exc:
            archived = archive.store_rejected(
                candidate_id, result.raw_response, str(exc)
            )
            self.registry.append(
                "candidate_generation_rejected",
                {
                    "lane_id": lane_id,
                    "task_id": task.task_id,
                    "candidate_id": candidate_id,
                    "error": str(exc),
                    "provider": result.provider,
                    "usage": result.usage,
                    "audit_log_path": result.audit_log_path,
                    "archive": archived,
                    "api_cost_usd": result.api_cost_usd,
                    "budget": self.budget.to_dict(),
                },
                event_id=_event_id(
                    "generation-rejected", lane_id, task.task_id, candidate_id
                ),
            )
            self.dashboard.render(self.registry)
            raise
        archived = archive.store(candidate_id, candidate)
        payload = {
            "lane_id": lane_id,
            "task_id": task.task_id,
            "candidate_id": candidate_id,
            "candidate_sha256": candidate.sha256,
            "prompt_sha256": prompt_sha,
            "api_cost_usd": result.api_cost_usd,
            "provider": result.provider,
            "usage": result.usage,
            "audit_log_path": result.audit_log_path,
            "archive": archived,
            "budget": self.budget.to_dict(),
        }
        return self.registry.append(
            "candidate_generated",
            payload,
            event_id=_event_id("candidate-generated", lane_id, task.task_id, candidate_id),
        )

    def _restored_usage(self, lane_id: str | None) -> dict[str, float | int]:
        if lane_id is None:
            return {}
        events = self.registry.read_events()
        starts = [
            event["payload"]
            for event in events
            if event["event_type"] == "generation_started"
            and event["payload"].get("lane_id") == lane_id
        ]
        candidate_ids = {str(payload["candidate_id"]) for payload in starts}
        actual_api: dict[str, float] = {}
        for event in events:
            if event["event_type"] not in {
                "candidate_generated",
                "candidate_generation_rejected",
                "harness_generated",
            }:
                continue
            payload = event["payload"]
            if payload.get("lane_id") == lane_id:
                actual_api[str(payload["candidate_id"])] = float(
                    payload.get("api_cost_usd", 0.0)
                )
        api_cost = sum(
            actual_api.get(
                str(payload["candidate_id"]),
                float(payload.get("reserved_api_cost_usd", 0.0)),
            )
            for payload in starts
        )
        gpu_by_candidate: dict[str, float] = {}
        for event in events:
            if event["event_type"] != "candidate_evaluated":
                continue
            feedback = event["payload"].get("feedback", {})
            if feedback.get("candidate_id") in candidate_ids:
                gpu_by_candidate[str(feedback["candidate_id"])] = float(
                    feedback.get("gpu_seconds", 0.0)
                )
        for event in events:
            if event["event_type"] != "candidate_evaluation_corrected":
                continue
            payload = event["payload"]
            feedback = payload.get("feedback", {})
            candidate_id = str(feedback.get("candidate_id", ""))
            if payload.get("lane_id") == lane_id and candidate_id in candidate_ids:
                gpu_by_candidate[candidate_id] = float(
                    feedback.get("gpu_seconds", 0.0)
                )
        return {
            "model_calls_used": len(starts),
            "api_cost_usd_used": api_cost,
            "gpu_seconds_used": sum(gpu_by_candidate.values()),
        }

    def _baseline_lane(self, lane_id: str, task_id: str) -> BaselineLane:
        matches = [lane for lane in self.plan.baselines if lane.lane_id == lane_id]
        if len(matches) != 1:
            raise ValueError(f"unknown P1 baseline lane: {lane_id}")
        lane = matches[0]
        if lane.task_id != task_id:
            raise ValueError("task does not match P1 baseline lane")
        if lane.allow_harness_mutation:
            raise ValueError("P1 baseline harness must remain frozen")
        return lane

    def _baseline_harness(self, lane: BaselineLane) -> str:
        harness_path = (self.project_root / lane.harness_path).resolve()
        if not harness_path.is_relative_to(self.project_root) or not harness_path.is_file():
            raise ValueError("frozen harness path is missing or escapes the project")
        harness_bytes = harness_path.read_bytes()
        if hashlib.sha256(harness_bytes).hexdigest() != lane.harness_sha256:
            raise ValueError("frozen harness content no longer matches campaign plan")
        return harness_bytes.decode("utf-8")

    def _require_ready_lane(self, lane_id: str) -> None:
        if not self.plan.execution_ready:
            blockers = ", ".join(self.plan.blockers)
            raise CampaignNotReady(
                f"campaign execution_ready is false; blockers: {blockers}"
            )
        if self.budget_scope_lane_id is not None and lane_id != self.budget_scope_lane_id:
            raise ValueError("candidate lane does not match controller budget scope")

    def _lineage(self, lane_id: str, task_id: str) -> LineagePlan:
        matches = [
            lineage
            for lineage in self.plan.lineages
            if _p2_lane_id(lineage) == lane_id
        ]
        if len(matches) != 1:
            raise ValueError(f"unknown P2 lineage lane: {lane_id}")
        lineage = matches[0]
        if lineage.task_id != task_id:
            raise ValueError("task does not match P2 lineage lane")
        if not lineage.allow_harness_mutation:
            raise ValueError("P2 lineage must allow Harness mutation")
        return lineage

    def _find_event(
        self,
        event_type: str,
        lane_id: str,
        task_id: str,
        candidate_id: str,
    ) -> dict[str, Any] | None:
        for event in reversed(self.registry.read_events()):
            if event["event_type"] != event_type:
                continue
            payload = event["payload"]
            if (
                payload.get("lane_id") == lane_id
                and payload.get("task_id") == task_id
                and payload.get("candidate_id") == candidate_id
            ):
                return event
        return None

    @staticmethod
    def _verify_archived_candidate(
        candidate_path: Path,
        expected_sha256: str,
        archive: CandidateArchive,
    ) -> None:
        candidate_path = candidate_path.resolve()
        candidates_root = (archive.scope_root / "candidates").resolve()
        if not candidate_path.is_relative_to(candidates_root) or not candidate_path.is_file():
            raise ValueError("generated candidate path escapes its immutable archive")
        if hashlib.sha256(candidate_path.read_bytes()).hexdigest() != expected_sha256:
            raise ValueError("generated candidate archive content changed")


def _validate_candidate_id(candidate_id: str) -> None:
    if not re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9._-]{0,127}", candidate_id):
        raise ValueError("candidate id must be a safe, single path component")


def _event_id(prefix: str, lane_id: str, task_id: str, candidate_id: str) -> str:
    identity = f"{lane_id}\0{task_id}\0{candidate_id}".encode()
    return f"{prefix}:{hashlib.sha256(identity).hexdigest()}"


def _p2_lane_id(lineage: LineagePlan) -> str:
    return f"p2:{lineage.task_id}:{lineage.lineage_id}"


def _harness_model_call_id(lane_id: str, version_id: str) -> str:
    label = lane_id.replace(":", "-").replace("kernelbench_", "")
    call_id = f"{label}-harness-{version_id}"
    _validate_candidate_id(call_id)
    return call_id
