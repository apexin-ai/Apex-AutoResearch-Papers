from __future__ import annotations

import hashlib
import json
import os
import re
import tempfile
from dataclasses import replace
from pathlib import Path
from typing import Any

from optimization_lab.adapters.base import BenchmarkAdapter
from optimization_lab.budget import BudgetExceeded, ExperimentBudget
from optimization_lab.feedback import FeedbackCard
from optimization_lab.generation import (
    CandidateArchive,
    CandidateGenerator,
    GeneratedCandidate,
    InvalidCandidate,
)
from optimization_lab.p2b_dashboard import P2bDashboard
from optimization_lab.p2b_generation import P2bGenerationRequest
from optimization_lab.p2b_plan import P2bLanePlan, P2bPlan
from optimization_lab.p2b_policy import (
    P2B_TOOLS,
    InvalidP2bPolicy,
    P2bPolicyArchive,
    P2bPolicyEvolutionRequest,
    P2bPolicyVersion,
    ScoreTrend,
    initial_policy,
)
from optimization_lab.profiling import ProfileSummary, Profiler
from optimization_lab.registry import ExperimentRegistry
from optimization_lab.runner import ExperimentRunner
from optimization_lab.task_spec import TaskSpec


class P2bEnvironmentBlocked(RuntimeError):
    pass


class P2bIncompleteAttempt(RuntimeError):
    """A started model or profiler call has no auditable completion artifact."""


class P2bModelAttemptFailed(RuntimeError):
    """A model call completed with an auditable provider or parsing failure."""


class P2bCampaignRunner:
    """Profiler-guided task-specific Harness search; deliberately has no P3 API."""

    def __init__(
        self,
        *,
        plan: P2bPlan,
        registry: ExperimentRegistry,
        dashboard: P2bDashboard,
        candidate_generator: CandidateGenerator,
        policy_generator: CandidateGenerator,
        adapter: BenchmarkAdapter,
        profiler: Profiler,
        tasks: dict[str, TaskSpec],
        task_cards: dict[str, str],
        reference_sources: dict[str, str],
    ):
        if not plan.execution_ready:
            raise ValueError("P2b plan inputs are missing or changed")
        expected_tasks = {lane.task_id for lane in plan.lanes}
        if set(tasks) != expected_tasks:
            raise ValueError("P2b runner requires exactly the frozen tasks")
        if set(task_cards) != expected_tasks or set(reference_sources) != expected_tasks:
            raise ValueError("P2b task inputs are incomplete")
        self.plan = plan
        self.registry = registry
        self.dashboard = dashboard
        self.candidate_generator = candidate_generator
        self.policy_generator = policy_generator
        self.adapter = adapter
        self.profiler = profiler
        self.tasks = tasks
        self.task_cards = task_cards
        self.reference_sources = reference_sources
        self.capabilities = profiler.capabilities()

    def run(self) -> dict[str, int]:
        self.registry.append(
            "p2b_phase_changed",
            {
                "phase": "P2B",
                "status": "in_progress",
                "detail": "运行八条 Profiler 引导的任务专用 Harness 路线",
            },
            event_id="p2b-phase:started",
        )
        self.registry.append(
            "p2b_profiler_capabilities",
            self.capabilities.to_dict(),
            event_id="p2b-profiler-capabilities:frozen",
        )
        self.dashboard.render(self.registry)
        for lane in self.plan.lanes:
            self._run_lane(lane)
        self.registry.append(
            "p2b_phase_changed",
            {
                "phase": "P2B",
                "status": "completed",
                "detail": "八条 P2B 路线已停止并冻结；P3 待另行授权",
            },
            event_id="p2b-phase:completed",
        )
        self.dashboard.render(self.registry)
        return self._summary()

    def _run_lane(self, lane: P2bLanePlan) -> None:
        if self._lane_completed(lane.lane_id):
            return
        task = self.tasks[lane.task_id]
        scope_root = Path(self.plan.artifact_root) / lane.history_scope
        policy_archive = P2bPolicyArchive(scope_root)
        policy_archive.store_seed(
            initial_policy(
                strategy=lane.strategy,
                starting_candidate_id=lane.starting_candidate_id,
            )
        )
        self.registry.append(
            "p2b_lane_started",
            {
                "lane_id": lane.lane_id,
                "task_id": lane.task_id,
                "strategy": lane.strategy,
                "starting_candidate_id": lane.starting_candidate_id,
                "starting_score": lane.starting_score,
                "max_rounds": lane.max_rounds,
            },
            event_id=f"p2b-lane-started:{_identity(lane.lane_id)}",
        )
        budget = self._restored_budget(lane)
        stop_reason = "maximum_rounds_reached"
        try:
            for round_number in range(1, lane.max_rounds + 1):
                existing = self._round_event(lane.lane_id, round_number)
                if existing is not None:
                    continue
                cards = self._lane_cards(lane.lane_id)
                profiles = self._lane_profiles(lane.lane_id)
                policy = self._policy_for_round(
                    lane=lane,
                    task=task,
                    round_number=round_number,
                    archive=policy_archive,
                    cards=cards,
                    profiles=profiles,
                    budget=budget,
                )
                candidate_id = _candidate_id(lane, round_number)
                candidate_path, candidate_sha = self._candidate_for_round(
                    lane=lane,
                    task=task,
                    round_number=round_number,
                    candidate_id=candidate_id,
                    policy=policy,
                    cards=cards,
                    profiles=profiles,
                    budget=budget,
                )
                duplicate_card = self._duplicate_card(
                    lane.lane_id, candidate_id, candidate_sha
                )
                if duplicate_card is None:
                    evaluator = ExperimentRunner(
                        registry=self.registry,
                        adapter=self.adapter,
                        dashboard=_NoopDashboard(),
                        budget=budget,
                    )
                    card = evaluator.evaluate(
                        task, candidate_path, candidate_id=candidate_id
                    )
                else:
                    card = duplicate_card
                if not card.valid_run:
                    raise P2bEnvironmentBlocked(
                        f"invalid scoring environment in {lane.lane_id}: {candidate_id}"
                    )
                trend = self._score_trend(lane, cards, card)
                full_profile = self._requires_full_profile(
                    lane=lane,
                    round_number=round_number,
                    policy=policy,
                    prior_cards=cards,
                    current=card,
                )
                profile = self._profile_candidate(
                    lane=lane,
                    task=task,
                    candidate_path=candidate_path,
                    candidate_id=candidate_id,
                    candidate_sha=candidate_sha,
                    card=card,
                    level="full" if full_profile else "light",
                    budget=budget,
                )
                novelty = self._novelty_status(profiles, profile, candidate_sha)
                self.registry.append(
                    "p2b_round_completed",
                    {
                        "lane_id": lane.lane_id,
                        "task_id": lane.task_id,
                        "strategy": lane.strategy,
                        "round_number": round_number,
                        "candidate_id": candidate_id,
                        "candidate_sha256": candidate_sha,
                        "policy_version_id": policy.version_id,
                        "policy_sha256": policy.sha256,
                        "policy": policy.policy.to_dict(),
                        "feedback": card.to_dict(),
                        "score_trend": trend.to_dict(),
                        "profile": profile.to_public_dict() if profile else None,
                        "novelty": novelty,
                        "budget": budget.to_dict(),
                    },
                    event_id=(
                        f"p2b-round:{_identity(lane.lane_id)}:{round_number:03d}"
                    ),
                )
                self.dashboard.render(self.registry)
        except P2bIncompleteAttempt as exc:
            stop_reason = "incomplete_attempt_preserved"
            self.registry.append(
                "p2b_lane_recovery_stopped",
                {
                    "lane_id": lane.lane_id,
                    "task_id": lane.task_id,
                    "detail": str(exc),
                    "budget": budget.to_dict(),
                },
                event_id=f"p2b-recovery-stopped:{_identity(lane.lane_id)}",
            )
        except P2bModelAttemptFailed as exc:
            stop_reason = "model_attempt_failed_preserved"
            self.registry.append(
                "p2b_lane_model_call_stopped",
                {
                    "lane_id": lane.lane_id,
                    "task_id": lane.task_id,
                    "detail": str(exc),
                    "budget": budget.to_dict(),
                },
                event_id=f"p2b-model-call-stopped:{_identity(lane.lane_id)}",
            )
        except (InvalidCandidate, InvalidP2bPolicy) as exc:
            stop_reason = "invalid_model_artifact_preserved"
            self.registry.append(
                "p2b_lane_model_artifact_stopped",
                {
                    "lane_id": lane.lane_id,
                    "task_id": lane.task_id,
                    "detail": f"{type(exc).__name__}: {exc}",
                    "budget": budget.to_dict(),
                },
                event_id=f"p2b-artifact-stopped:{_identity(lane.lane_id)}",
            )
        rounds = self._lane_rounds(lane.lane_id)
        scores = [
            float(item["feedback"]["speedup_vs_eager"])
            for item in rounds
            if item["feedback"].get("correct")
            and item["feedback"].get("speedup_vs_eager") is not None
        ]
        self.registry.append(
            "p2b_lane_completed",
            {
                "lane_id": lane.lane_id,
                "task_id": lane.task_id,
                "strategy": lane.strategy,
                "rounds": len(rounds),
                "stop_reason": stop_reason,
                "best_speedup": max(scores) if scores else None,
                "budget": budget.to_dict(),
            },
            event_id=f"p2b-lane-completed:{_identity(lane.lane_id)}",
        )
        self.dashboard.render(self.registry)

    def _policy_for_round(
        self,
        *,
        lane: P2bLanePlan,
        task: TaskSpec,
        round_number: int,
        archive: P2bPolicyArchive,
        cards: tuple[FeedbackCard, ...],
        profiles: tuple[ProfileSummary, ...],
        budget: ExperimentBudget,
    ) -> P2bPolicyVersion:
        version_id = f"v{round_number:03d}"
        if round_number == 1:
            return archive.load(version_id)
        current = archive.load(f"v{round_number - 1:03d}")
        completed = self._find_event(
            "p2b_policy_generated", lane.lane_id, call_id=_policy_call_id(lane, round_number)
        )
        if completed is not None:
            return archive.load(version_id)
        call_id = _policy_call_id(lane, round_number)
        if self._find_event("p2b_model_call_started", lane.lane_id, call_id=call_id):
            metadata = archive.scope_root / "policy_metadata" / f"{version_id}.json"
            if metadata.is_file():
                version = archive.load(version_id)
                self.registry.append(
                    "p2b_policy_generated",
                    {
                        "lane_id": lane.lane_id,
                        "task_id": lane.task_id,
                        "call_id": call_id,
                        "round_number": round_number,
                        "policy_version_id": version.version_id,
                        "policy_sha256": version.sha256,
                        "policy": version.policy.to_dict(),
                        "recovered_from_archive": True,
                        "api_cost_usd": 0.0,
                        "budget": budget.to_dict(),
                    },
                    event_id=f"p2b-policy-recovered:{_identity(call_id)}",
                )
                return version
            raise P2bIncompleteAttempt(
                f"policy model call already started without an artifact: {call_id}"
            )

        last_trend = self._trend_from_round(self._lane_rounds(lane.lane_id)[-1])
        require_change = not last_trend.significant_improvement
        best_score = max(
            [lane.starting_score]
            + [
                float(card.speedup_vs_eager)
                for card in cards
                if card.correct and card.speedup_vs_eager is not None
            ]
        )
        require_restart = (
            round_number == lane.forced_restart_round
            and best_score < lane.starting_score * 1.02
        )
        require_structural = round_number in lane.mandatory_structural_rounds
        allowed_bases = self._allowed_base_ids(lane, round_number)
        request = P2bPolicyEvolutionRequest(
            task_id=task.task_id,
            lane_id=lane.lane_id,
            strategy=lane.strategy,
            target_version_id=version_id,
            current=current,
            task_card=self.task_cards[task.task_id],
            feedback_history=cards,
            current_trend=last_trend,
            profile_history=profiles,
            allowed_base_candidate_ids=allowed_bases,
            require_direction_change=require_change,
            require_structural_change=require_structural,
            require_restart=require_restart,
            capabilities=self.capabilities,
        )
        prompt = request.to_prompt()
        prompt_sha = hashlib.sha256(prompt.encode()).hexdigest()
        reserved_cost = self.policy_generator.estimated_api_cost_usd()
        self._reserve_model_call(
            budget=budget,
            lane=lane,
            task=task,
            call_id=call_id,
            kind="policy",
            prompt_sha=prompt_sha,
            reserved_cost=reserved_cost,
        )
        try:
            result = self.policy_generator.generate(
                prompt, model=self.plan.executor_model
            )
            budget.settle_api(
                reserved_cost_usd=reserved_cost,
                actual_cost_usd=result.api_cost_usd,
            )
            available_tools = set(P2B_TOOLS)
            if not self.capabilities.hardware_counters:
                available_tools.discard("hardware_counters")
            version = P2bPolicyVersion.from_response(
                version_id=version_id,
                parent=current,
                response=result.raw_response,
                allowed_base_candidate_ids=set(allowed_bases),
                available_tools=available_tools,
                require_direction_change=require_change,
                require_structural_change=require_structural,
                require_restart=require_restart,
            )
            archive.store_generated(
                version,
                raw_response=result.raw_response,
                prompt_sha256=prompt_sha,
            )
        except Exception as exc:
            self.registry.append(
                "p2b_policy_generation_failed",
                {
                    "lane_id": lane.lane_id,
                    "task_id": lane.task_id,
                    "call_id": call_id,
                    "round_number": round_number,
                    "detail": f"{type(exc).__name__}: {exc}",
                    "budget": budget.to_dict(),
                },
                event_id=f"p2b-policy-failed:{_identity(call_id)}",
            )
            if isinstance(exc, InvalidP2bPolicy):
                raise
            raise P2bModelAttemptFailed(
                f"policy attempt failed at round {round_number}: {type(exc).__name__}: {exc}"
            ) from exc
        self.registry.append(
            "p2b_policy_generated",
            {
                "lane_id": lane.lane_id,
                "task_id": lane.task_id,
                "call_id": call_id,
                "round_number": round_number,
                "policy_version_id": version.version_id,
                "policy_sha256": version.sha256,
                "policy": version.policy.to_dict(),
                "score_trend": last_trend.to_dict(),
                "require_direction_change": require_change,
                "require_structural_change": require_structural,
                "require_restart": require_restart,
                "provider": result.provider,
                "usage": result.usage,
                "audit_log_path": result.audit_log_path,
                "api_cost_usd": result.api_cost_usd,
                "budget": budget.to_dict(),
            },
            event_id=f"p2b-policy-generated:{_identity(call_id)}",
        )
        return version

    def _candidate_for_round(
        self,
        *,
        lane: P2bLanePlan,
        task: TaskSpec,
        round_number: int,
        candidate_id: str,
        policy: P2bPolicyVersion,
        cards: tuple[FeedbackCard, ...],
        profiles: tuple[ProfileSummary, ...],
        budget: ExperimentBudget,
    ) -> tuple[Path, str]:
        archive = CandidateArchive(Path(self.plan.artifact_root), lane.history_scope)
        completed = self._find_event(
            "p2b_candidate_generated", lane.lane_id, call_id=candidate_id
        )
        if completed is not None:
            path = Path(completed["payload"]["candidate_path"]).resolve()
            sha = str(completed["payload"]["candidate_sha256"])
            self._verify_candidate_path(archive, path, sha)
            return path, sha
        if self._find_event(
            "p2b_model_call_started", lane.lane_id, call_id=candidate_id
        ):
            metadata = archive.scope_root / "metadata" / f"{candidate_id}.json"
            if metadata.is_file():
                data = json.loads(metadata.read_text(encoding="utf-8"))
                path = Path(data["candidate_path"]).resolve()
                sha = str(data["candidate_sha256"])
                self._verify_candidate_path(archive, path, sha)
                self.registry.append(
                    "p2b_candidate_generated",
                    {
                        "lane_id": lane.lane_id,
                        "task_id": lane.task_id,
                        "call_id": candidate_id,
                        "round_number": round_number,
                        "candidate_id": candidate_id,
                        "candidate_sha256": sha,
                        "candidate_path": str(path),
                        "recovered_from_archive": True,
                        "api_cost_usd": 0.0,
                        "budget": budget.to_dict(),
                    },
                    event_id=f"p2b-candidate-recovered:{_identity(candidate_id)}",
                )
                return path, sha
            raise P2bIncompleteAttempt(
                f"candidate model call already started without an artifact: {candidate_id}"
            )

        trend = (
            self._trend_from_round(self._lane_rounds(lane.lane_id)[-1])
            if cards
            else None
        )
        base_source = self._source_for_id(lane, policy.policy.base_candidate_id)
        memory = self._memory_sources(lane, policy, cards)
        request = P2bGenerationRequest(
            task_id=task.task_id,
            lane_id=lane.lane_id,
            candidate_id=candidate_id,
            task_card=self.task_cards[task.task_id],
            reference_source=self.reference_sources[task.task_id],
            policy=policy,
            base_candidate_source=base_source,
            memory_sources=memory,
            feedback_history=cards,
            current_trend=trend,
            profile_history=profiles,
        )
        prompt = request.to_prompt()
        prompt_sha = hashlib.sha256(prompt.encode()).hexdigest()
        reserved_cost = self.candidate_generator.estimated_api_cost_usd()
        self._reserve_model_call(
            budget=budget,
            lane=lane,
            task=task,
            call_id=candidate_id,
            kind="candidate",
            prompt_sha=prompt_sha,
            reserved_cost=reserved_cost,
        )
        try:
            result = self.candidate_generator.generate(
                prompt, model=self.plan.executor_model
            )
            budget.settle_api(
                reserved_cost_usd=reserved_cost,
                actual_cost_usd=result.api_cost_usd,
            )
            candidate = GeneratedCandidate.from_response(result.raw_response)
        except Exception as exc:
            if isinstance(exc, InvalidCandidate):
                archive.store_rejected(candidate_id, result.raw_response, str(exc))
            self.registry.append(
                "p2b_candidate_generation_failed",
                {
                    "lane_id": lane.lane_id,
                    "task_id": lane.task_id,
                    "call_id": candidate_id,
                    "round_number": round_number,
                    "detail": f"{type(exc).__name__}: {exc}",
                    "budget": budget.to_dict(),
                },
                event_id=f"p2b-candidate-failed:{_identity(candidate_id)}",
            )
            if isinstance(exc, InvalidCandidate):
                raise
            raise P2bModelAttemptFailed(
                f"candidate attempt failed at round {round_number}: {type(exc).__name__}: {exc}"
            ) from exc
        archived = archive.store(candidate_id, candidate)
        path = Path(archived["candidate_path"]).resolve()
        self.registry.append(
            "p2b_candidate_generated",
            {
                "lane_id": lane.lane_id,
                "task_id": lane.task_id,
                "call_id": candidate_id,
                "round_number": round_number,
                "candidate_id": candidate_id,
                "candidate_sha256": candidate.sha256,
                "candidate_path": str(path),
                "policy_version_id": policy.version_id,
                "policy_sha256": policy.sha256,
                "prompt_sha256": prompt_sha,
                "provider": result.provider,
                "usage": result.usage,
                "audit_log_path": result.audit_log_path,
                "api_cost_usd": result.api_cost_usd,
                "budget": budget.to_dict(),
            },
            event_id=f"p2b-candidate-generated:{_identity(candidate_id)}",
        )
        return path, candidate.sha256

    def _profile_candidate(
        self,
        *,
        lane: P2bLanePlan,
        task: TaskSpec,
        candidate_path: Path,
        candidate_id: str,
        candidate_sha: str,
        card: FeedbackCard,
        level: str,
        budget: ExperimentBudget,
    ) -> ProfileSummary | None:
        if not card.correct or card.speedup_vs_eager is None:
            return None
        completed = self._find_event(
            "p2b_profile_completed", lane.lane_id, call_id=candidate_id
        )
        if completed is not None:
            return _profile_from_dict(completed["payload"]["summary"])
        started = self._find_event(
            "p2b_profile_started", lane.lane_id, call_id=candidate_id
        )
        if started is not None:
            public_path = self._public_profile_path(lane, candidate_id)
            if public_path.is_file():
                summary = _profile_from_dict(
                    json.loads(public_path.read_text(encoding="utf-8"))
                )
                self.registry.append(
                    "p2b_profile_completed",
                    {
                        "lane_id": lane.lane_id,
                        "task_id": lane.task_id,
                        "call_id": candidate_id,
                        "candidate_id": candidate_id,
                        "candidate_sha256": candidate_sha,
                        "level": summary.level,
                        "summary": summary.to_public_dict(),
                        "gpu_seconds": summary.gpu_seconds,
                        "recovered_from_archive": True,
                        "budget": budget.to_dict(),
                    },
                    event_id=f"p2b-profile-recovered:{_identity(candidate_id)}",
                )
                return summary
            raise P2bIncompleteAttempt(
                f"profile already started without a public artifact: {candidate_id}"
            )
        reserved = self.profiler.estimated_gpu_seconds(task, level)
        self._check_global_gpu_reservation(reserved)
        budget.reserve(gpu_seconds=reserved)
        self.registry.append(
            "p2b_profile_started",
            {
                "lane_id": lane.lane_id,
                "task_id": lane.task_id,
                "call_id": candidate_id,
                "candidate_id": candidate_id,
                "candidate_sha256": candidate_sha,
                "level": level,
                "reserved_gpu_seconds": reserved,
                "budget": budget.to_dict(),
            },
            event_id=f"p2b-profile-started:{_identity(candidate_id)}",
        )
        private_dir = (
            Path(self.plan.artifact_root)
            / "profiles/private"
            / lane.task_id
            / lane.strategy
            / candidate_id
        )
        try:
            summary = self.profiler.profile(
                task=task,
                candidate_path=candidate_path,
                candidate_id=candidate_id,
                feedback=card,
                level=level,
                private_log_dir=private_dir,
            )
            budget.settle_gpu(
                reserved_seconds=reserved, actual_seconds=summary.gpu_seconds
            )
        except Exception:
            budget.settle_gpu(reserved_seconds=reserved, actual_seconds=0.0)
            raise
        if summary.candidate_sha256 != candidate_sha:
            raise ValueError("profiler summary is bound to different candidate content")
        public_path = self._public_profile_path(lane, candidate_id)
        _write_atomic_json(public_path, summary.to_public_dict())
        self.registry.append(
            "p2b_profile_completed",
            {
                "lane_id": lane.lane_id,
                "task_id": lane.task_id,
                "call_id": candidate_id,
                "candidate_id": candidate_id,
                "candidate_sha256": candidate_sha,
                "level": level,
                "summary": summary.to_public_dict(),
                "gpu_seconds": summary.gpu_seconds,
                "budget": budget.to_dict(),
            },
            event_id=f"p2b-profile-completed:{_identity(candidate_id)}",
        )
        return summary

    def _reserve_model_call(
        self,
        *,
        budget: ExperimentBudget,
        lane: P2bLanePlan,
        task: TaskSpec,
        call_id: str,
        kind: str,
        prompt_sha: str,
        reserved_cost: float,
    ) -> None:
        starts = sum(
            event["event_type"] == "p2b_model_call_started"
            for event in self.registry.read_events()
        )
        if starts + 1 > self.plan.global_model_call_cap:
            raise BudgetExceeded("P2b global model-call hard cap would be exceeded")
        budget.reserve(model_calls=1, api_cost_usd=reserved_cost)
        self.registry.append(
            "p2b_model_call_started",
            {
                "lane_id": lane.lane_id,
                "task_id": task.task_id,
                "call_id": call_id,
                "call_kind": kind,
                "executor_model": self.plan.executor_model,
                "prompt_sha256": prompt_sha,
                "reserved_api_cost_usd": reserved_cost,
                "budget": budget.to_dict(),
            },
            event_id=f"p2b-model-call-started:{_identity(call_id)}",
        )

    def _restored_budget(self, lane: P2bLanePlan) -> ExperimentBudget:
        events = self.registry.read_events()
        starts = [
            event["payload"]
            for event in events
            if event["event_type"] == "p2b_model_call_started"
            and event["payload"].get("lane_id") == lane.lane_id
        ]
        actual_api: dict[str, float] = {}
        for event in events:
            if event["event_type"] not in {
                "p2b_policy_generated",
                "p2b_candidate_generated",
            }:
                continue
            payload = event["payload"]
            if payload.get("lane_id") == lane.lane_id:
                actual_api[str(payload["call_id"])] = float(
                    payload.get("api_cost_usd", 0.0)
                )
        api_used = sum(
            actual_api.get(
                str(payload["call_id"]),
                float(payload.get("reserved_api_cost_usd", 0.0)),
            )
            for payload in starts
        )
        candidate_ids = {
            str(payload["call_id"])
            for payload in starts
            if payload.get("call_kind") == "candidate"
        }
        candidate_gpu: dict[str, float] = {}
        for event in events:
            if event["event_type"] != "candidate_evaluated":
                continue
            card = event["payload"].get("feedback", {})
            candidate_id = str(card.get("candidate_id", ""))
            if candidate_id in candidate_ids:
                candidate_gpu[candidate_id] = float(card.get("gpu_seconds", 0.0))
        profile_gpu: dict[str, float] = {}
        profile_starts: dict[str, float] = {}
        for event in events:
            payload = event["payload"]
            if payload.get("lane_id") != lane.lane_id:
                continue
            if event["event_type"] == "p2b_profile_started":
                profile_starts[str(payload["candidate_id"])] = float(
                    payload.get("reserved_gpu_seconds", 0.0)
                )
            elif event["event_type"] == "p2b_profile_completed":
                profile_gpu[str(payload["candidate_id"])] = float(
                    payload.get("gpu_seconds", 0.0)
                )
        profile_used = sum(
            profile_gpu.get(candidate_id, reserved)
            for candidate_id, reserved in profile_starts.items()
        )
        return ExperimentBudget(
            max_gpu_seconds=lane.gpu_seconds_cap,
            max_model_calls=lane.model_call_cap,
            max_api_cost_usd=self.plan.api_dollar_cap_per_lane,
            max_gpu_cost_usd=self.plan.gpu_dollar_cap_per_lane,
            gpu_seconds_used=sum(candidate_gpu.values()) + profile_used,
            model_calls_used=len(starts),
            api_cost_usd_used=api_used,
        )

    def _allowed_base_ids(
        self, lane: P2bLanePlan, round_number: int
    ) -> tuple[str, ...]:
        own = tuple(_candidate_id(lane, number) for number in range(1, round_number))
        return tuple(
            dict.fromkeys(
                ("reference", *lane.allowed_frozen_candidate_ids, *own)
            )
        )

    def _source_for_id(self, lane: P2bLanePlan, candidate_id: str) -> str:
        if candidate_id == "reference":
            return self.reference_sources[lane.task_id]
        for frozen in self.plan.frozen_candidates:
            if frozen.task_id == lane.task_id and frozen.candidate_id == candidate_id:
                path = Path(self.plan.artifact_root) / frozen.frozen_path
                if hashlib.sha256(path.read_bytes()).hexdigest() != frozen.source_sha256:
                    raise ValueError("frozen P2b candidate content changed")
                return path.read_text(encoding="utf-8")
        own = (
            Path(self.plan.artifact_root)
            / lane.history_scope
            / "candidates"
            / f"{candidate_id}.py"
        )
        if own.is_file():
            return own.read_text(encoding="utf-8")
        raise ValueError(f"P2b policy selected an unavailable base: {candidate_id}")

    def _memory_sources(
        self,
        lane: P2bLanePlan,
        policy: P2bPolicyVersion,
        cards: tuple[FeedbackCard, ...],
    ) -> tuple[tuple[str, str], ...]:
        selected: list[str] = []
        views = set(policy.policy.memory_views)
        if "starting_point" in views and lane.starting_candidate_id != "reference":
            selected.append(lane.starting_candidate_id)
        if "previous" in views and cards:
            selected.append(cards[-1].candidate_id)
        if "recent" in views:
            selected.extend(card.candidate_id for card in cards[-2:])
        if "historical_best" in views and cards:
            correct = [
                card
                for card in cards
                if card.correct and card.speedup_vs_eager is not None
            ]
            if correct:
                selected.append(
                    max(correct, key=lambda item: float(item.speedup_vs_eager)).candidate_id
                )
        if "structurally_novel" in views and cards:
            selected.append(cards[-1].candidate_id)
        if "frozen_frontier" in views or lane.strategy == "recombinant_frontier":
            selected.extend(lane.allowed_frozen_candidate_ids)
        selected = list(dict.fromkeys(selected))
        return tuple(
            (candidate_id, self._source_for_id(lane, candidate_id))
            for candidate_id in selected
            if candidate_id != policy.policy.base_candidate_id
        )

    def _duplicate_card(
        self, lane_id: str, candidate_id: str, candidate_sha: str
    ) -> FeedbackCard | None:
        for item in self._lane_rounds(lane_id):
            if item.get("candidate_sha256") == candidate_sha:
                card = FeedbackCard(**item["feedback"])
                self.registry.append(
                    "p2b_duplicate_reused",
                    {
                        "lane_id": lane_id,
                        "candidate_id": candidate_id,
                        "duplicate_of": card.candidate_id,
                        "candidate_sha256": candidate_sha,
                    },
                    event_id=f"p2b-duplicate:{_identity(candidate_id)}",
                )
                return replace(card, candidate_id=candidate_id, gpu_seconds=0.0)
        return None

    @staticmethod
    def _requires_full_profile(
        *,
        lane: P2bLanePlan,
        round_number: int,
        policy: P2bPolicyVersion,
        prior_cards: tuple[FeedbackCard, ...],
        current: FeedbackCard,
    ) -> bool:
        if round_number == 1 or policy.policy.force_restart:
            return True
        if policy.policy.diagnostic_level == "full" or set(policy.policy.tool_plan) & {
            "nsys_timeline",
            "triton_compiler_metadata",
            "ptx_sass_summary",
            "hardware_counters",
        }:
            return True
        prior_best = max(
            [lane.starting_score]
            + [
                float(card.speedup_vs_eager)
                for card in prior_cards
                if card.correct and card.speedup_vs_eager is not None
            ]
        )
        return bool(
            current.correct
            and current.speedup_vs_eager is not None
            and current.speedup_vs_eager >= prior_best * 1.02
        )

    @staticmethod
    def _score_trend(
        lane: P2bLanePlan,
        prior_cards: tuple[FeedbackCard, ...],
        current: FeedbackCard,
    ) -> ScoreTrend:
        prior_scores = [
            float(card.speedup_vs_eager)
            for card in prior_cards
            if card.correct and card.speedup_vs_eager is not None
        ]
        previous = prior_scores[-1] if prior_scores else lane.starting_score
        historical = max([lane.starting_score, *prior_scores])
        return ScoreTrend.build(
            current_score=(
                float(current.speedup_vs_eager)
                if current.correct and current.speedup_vs_eager is not None
                else None
            ),
            previous_score=previous,
            historical_best=historical,
            starting_score=lane.starting_score,
        )

    @staticmethod
    def _novelty_status(
        prior_profiles: tuple[ProfileSummary, ...],
        current: ProfileSummary | None,
        candidate_sha: str,
    ) -> dict[str, Any]:
        if current is None:
            return {
                "candidate_sha256": candidate_sha,
                "structural_signature": None,
                "structurally_novel": None,
            }
        signatures = {item.structural_signature for item in prior_profiles}
        return {
            "candidate_sha256": candidate_sha,
            "structural_signature": current.structural_signature,
            "structurally_novel": current.structural_signature not in signatures,
        }

    def _check_global_gpu_reservation(self, requested: float) -> None:
        used = 0.0
        for event in self.registry.read_events():
            if event["event_type"] == "candidate_evaluated":
                candidate_id = str(
                    event["payload"].get("feedback", {}).get("candidate_id", "")
                )
                if candidate_id.startswith("p2b-"):
                    used += float(
                        event["payload"].get("feedback", {}).get("gpu_seconds", 0.0)
                    )
            elif event["event_type"] == "p2b_profile_completed":
                used += float(event["payload"].get("gpu_seconds", 0.0))
        if used + requested > self.plan.global_gpu_seconds_cap:
            raise BudgetExceeded("P2b global GPU hard cap would be exceeded")

    def _public_profile_path(self, lane: P2bLanePlan, candidate_id: str) -> Path:
        return (
            Path(self.plan.artifact_root)
            / "profiles/public"
            / lane.task_id
            / lane.strategy
            / f"{candidate_id}.json"
        )

    def _lane_cards(self, lane_id: str) -> tuple[FeedbackCard, ...]:
        return tuple(FeedbackCard(**item["feedback"]) for item in self._lane_rounds(lane_id))

    def _lane_profiles(self, lane_id: str) -> tuple[ProfileSummary, ...]:
        return tuple(
            _profile_from_dict(item["profile"])
            for item in self._lane_rounds(lane_id)
            if item.get("profile") is not None
        )

    def _lane_rounds(self, lane_id: str) -> list[dict[str, Any]]:
        return sorted(
            [
                event["payload"]
                for event in self.registry.read_events()
                if event["event_type"] == "p2b_round_completed"
                and event["payload"].get("lane_id") == lane_id
            ],
            key=lambda item: int(item["round_number"]),
        )

    def _round_event(self, lane_id: str, round_number: int) -> dict[str, Any] | None:
        for event in reversed(self.registry.read_events()):
            if (
                event["event_type"] == "p2b_round_completed"
                and event["payload"].get("lane_id") == lane_id
                and event["payload"].get("round_number") == round_number
            ):
                return event
        return None

    def _lane_completed(self, lane_id: str) -> bool:
        return any(
            event["event_type"] == "p2b_lane_completed"
            and event["payload"].get("lane_id") == lane_id
            for event in self.registry.read_events()
        )

    def _find_event(
        self, event_type: str, lane_id: str, *, call_id: str
    ) -> dict[str, Any] | None:
        for event in reversed(self.registry.read_events()):
            if event["event_type"] != event_type:
                continue
            payload = event["payload"]
            if payload.get("lane_id") == lane_id and payload.get("call_id") == call_id:
                return event
        return None

    @staticmethod
    def _trend_from_round(round_payload: dict[str, Any]) -> ScoreTrend:
        return ScoreTrend(**round_payload["score_trend"])

    @staticmethod
    def _verify_candidate_path(
        archive: CandidateArchive, path: Path, expected_sha: str
    ) -> None:
        candidate_root = (archive.scope_root / "candidates").resolve()
        if not path.is_relative_to(candidate_root) or not path.is_file():
            raise ValueError("P2b candidate path escapes its immutable archive")
        if hashlib.sha256(path.read_bytes()).hexdigest() != expected_sha:
            raise ValueError("archived P2b candidate content changed")

    def _summary(self) -> dict[str, int]:
        events = self.registry.read_events()
        rounds = [event for event in events if event["event_type"] == "p2b_round_completed"]
        starts = [event for event in events if event["event_type"] == "p2b_model_call_started"]
        return {
            "lane_count": len(self.plan.lanes),
            "round_count": len(rounds),
            "correct_count": sum(event["payload"]["feedback"]["correct"] for event in rounds),
            "candidate_model_calls": sum(
                event["payload"].get("call_kind") == "candidate" for event in starts
            ),
            "policy_model_calls": sum(
                event["payload"].get("call_kind") == "policy" for event in starts
            ),
            "profile_count": sum(
                event["event_type"] == "p2b_profile_completed" for event in events
            ),
        }


def _candidate_id(lane: P2bLanePlan, round_number: int) -> str:
    task = lane.task_id.removeprefix("kernelbench_").replace("_", "-")
    strategy = lane.strategy.replace("_", "-")
    candidate_id = f"p2b-{task}-{strategy}-v{round_number:03d}"
    if not re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9._-]{0,127}", candidate_id):
        raise ValueError("generated P2b candidate id is unsafe")
    return candidate_id


def _policy_call_id(lane: P2bLanePlan, round_number: int) -> str:
    return f"{_candidate_id(lane, round_number)}-harness"


def _identity(value: str) -> str:
    return hashlib.sha256(value.encode()).hexdigest()


def _profile_from_dict(data: dict[str, Any]) -> ProfileSummary:
    return ProfileSummary(
        **{
            **data,
            "timeline_summary": tuple(data.get("timeline_summary", ())),
            "compiler_summary": tuple(data.get("compiler_summary", ())),
            "missing_metrics": tuple(data.get("missing_metrics", ())),
        }
    )


def _write_atomic_json(path: Path, data: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, name = tempfile.mkstemp(dir=path.parent, suffix=".tmp")
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as handle:
            json.dump(data, handle, ensure_ascii=False, indent=2, sort_keys=True)
            handle.write("\n")
            handle.flush()
            os.fsync(handle.fileno())
        Path(name).replace(path)
    except Exception:
        Path(name).unlink(missing_ok=True)
        raise


class _NoopDashboard:
    def render(self, registry: ExperimentRegistry) -> None:
        return None
