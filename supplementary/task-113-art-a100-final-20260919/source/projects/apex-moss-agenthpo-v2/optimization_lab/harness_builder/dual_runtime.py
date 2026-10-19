from __future__ import annotations

import hashlib
import json
import math
import os
import re
from dataclasses import asdict, dataclass, field
from typing import Any, Callable, Mapping

from .builder_harness import BuilderHarness, BuilderEvolutionResult, BuilderStepEvent
from .dual_harness import (
    HarnessTraceEvent,
    HarnessWorkspace,
    TaskHarnessArtifact,
    TaskHarnessRuntime,
)
from .tool_registry import ToolRegistry


_SHA256 = re.compile(r"[0-9a-f]{64}")


class IncompleteRoundError(RuntimeError):
    """An external operation started but has no durable result; retry is fail-closed."""


@dataclass(frozen=True)
class PublicEvaluation:
    """The only evaluator information that may cross into the Harness loop."""

    score: float | None
    feedback: str

    def __post_init__(self) -> None:
        if self.score is not None:
            if (
                not isinstance(self.score, (int, float))
                or isinstance(self.score, bool)
                or not math.isfinite(float(self.score))
            ):
                raise ValueError("public evaluation score is invalid")
        if not isinstance(self.feedback, str) or len(self.feedback) > 32_000:
            raise ValueError("public evaluation feedback is invalid")


@dataclass(frozen=True)
class EvaluationResult:
    """Evaluator result with an explicit private compartment."""

    public: PublicEvaluation
    private: Any = field(default=None, repr=False, compare=False)


@dataclass(frozen=True)
class DualHarnessRoundResult:
    run_id: str
    harness_sha256: str
    candidate: str
    score: float | None
    feedback: str
    builder_status: str
    next_harness_sha256: str

    @classmethod
    def from_dict(cls, payload: Mapping[str, Any]) -> "DualHarnessRoundResult":
        required = {
            "run_id",
            "harness_sha256",
            "candidate",
            "score",
            "feedback",
            "builder_status",
            "next_harness_sha256",
        }
        if not isinstance(payload, Mapping) or set(payload) != required:
            raise ValueError("round receipt result is invalid")
        public = PublicEvaluation(payload["score"], payload["feedback"])
        for key in (
            "run_id",
            "harness_sha256",
            "candidate",
            "builder_status",
            "next_harness_sha256",
        ):
            if not isinstance(payload[key], str) or not payload[key]:
                raise ValueError("round receipt result is invalid")
        return cls(
            run_id=payload["run_id"],
            harness_sha256=payload["harness_sha256"],
            candidate=payload["candidate"],
            score=public.score,
            feedback=public.feedback,
            builder_status=payload["builder_status"],
            next_harness_sha256=payload["next_harness_sha256"],
        )


class DualHarnessRuntime:
    """Run the lower Task Harness, evaluate, then evolve it with the upper Harness."""

    def __init__(
        self,
        *,
        workspace: HarnessWorkspace,
        task_runtime: TaskHarnessRuntime,
        builder: BuilderHarness,
        solver_model: str,
    ) -> None:
        if not solver_model.strip():
            raise ValueError("Solver model is required")
        if builder.workspace.root != workspace.root:
            raise ValueError("Builder and Task Harness must share one workspace")
        self.workspace = workspace
        self.task_runtime = task_runtime
        self.builder = builder
        self.solver_model = solver_model

    def run_round(
        self,
        *,
        run_id: str,
        execution_contract_sha256: str,
        task: str,
        tools: Mapping[str, Callable[[Any], Any]],
        tool_registry: ToolRegistry | None = None,
        tool_workspace: str | os.PathLike[str] | None = None,
        evaluator: Callable[[str], EvaluationResult],
        probe: Callable[[TaskHarnessArtifact], bool] | None = None,
        evolve_builder: bool = True,
        update_champion: bool = True,
    ) -> DualHarnessRoundResult:
        if _SHA256.fullmatch(execution_contract_sha256) is None:
            raise ValueError("execution contract hash is invalid")
        task_sha256 = hashlib.sha256(task.encode("utf-8")).hexdigest()
        request_sha256 = self._request_sha256(
            task_sha256=task_sha256,
            execution_contract_sha256=execution_contract_sha256,
        )
        self._bind_round_generator(self.task_runtime.generator, run_id)
        self._bind_round_generator(self.builder.generator, run_id)
        replay = self._replay_receipt(run_id, request_sha256)
        if replay is not None:
            return replay
        with self.workspace.evolution_lock():
            if self.workspace.load_abandoned_round(run_id, missing_ok=True) is not None:
                raise IncompleteRoundError(f"round is terminally abandoned: {run_id}")
            replay = self._replay_receipt(run_id, request_sha256)
            if replay is not None:
                return replay
            pending = tuple(
                pending_run_id
                for pending_run_id in self.workspace.pending_run_ids()
                if pending_run_id != run_id
            )
            if pending:
                raise IncompleteRoundError(
                    "pending round must be recovered or explicitly abandoned before "
                    f"starting another round: {pending[0]}"
                )
            trace = self.workspace.load_trace(run_id, missing_ok=True)
            if trace is None:
                solver_result = self._load_or_run_solver(
                    run_id=run_id,
                    request_sha256=request_sha256,
                    task=task,
                    task_sha256=task_sha256,
                    tools=tools,
                    tool_registry=tool_registry,
                    tool_workspace=tool_workspace,
                )
                trace = self._load_or_run_evaluator(
                    run_id=run_id,
                    request_sha256=request_sha256,
                    task_sha256=task_sha256,
                    solver_result=solver_result,
                    evaluator=evaluator,
                )
            self._validate_saved_trace(trace, request_sha256)
            harness_sha256 = trace["harness_sha256"]
            if evolve_builder:
                evolution = self._load_or_run_builder(
                    run_id=run_id,
                    request_sha256=request_sha256,
                    harness_sha256=harness_sha256,
                    score=trace["score"],
                    feedback=trace["feedback"],
                    probe=probe,
                    update_champion=update_champion,
                )
            else:
                evolution = BuilderEvolutionResult(
                    status="not_run",
                    previous_sha256=harness_sha256,
                    candidate_sha256=None,
                    reason="builder skipped at the configured round limit",
                    builder_harness_sha256=self.builder.spec.sha256,
                    events=(),
                )
            next_harness = self.workspace.current()
            result = DualHarnessRoundResult(
                run_id=run_id,
                harness_sha256=harness_sha256,
                candidate=trace["candidate"],
                score=trace["score"],
                feedback=trace["feedback"],
                builder_status=evolution.status,
                next_harness_sha256=next_harness.sha256,
            )
            self.workspace.record_round_receipt(
                run_id=run_id,
                payload={
                    "schema_version": 1,
                    "run_id": run_id,
                    "request_sha256": request_sha256,
                    "result": asdict(result),
                },
            )
            return result

    @staticmethod
    def _bind_round_generator(generator: Any, run_id: str) -> None:
        binder = getattr(generator, "bind_run_id", None)
        if binder is not None:
            binder(run_id)

    def _load_or_run_solver(
        self,
        *,
        run_id: str,
        request_sha256: str,
        task: str,
        task_sha256: str,
        tools: Mapping[str, Callable[[Any], Any]],
        tool_registry: ToolRegistry | None,
        tool_workspace: str | os.PathLike[str] | None,
    ) -> dict[str, Any]:
        saved = self.workspace.load_solver_result(run_id, missing_ok=True)
        if saved is not None:
            if saved.get("request_sha256") != request_sha256:
                raise ValueError("run id is already bound to a different round request")
            return saved
        self._claim_external_operation(run_id, "solver", request_sha256)
        current = self.workspace.current()
        task_run = self.task_runtime.run(
            current,
            task=task,
            model=self.solver_model,
            tools=tools,
            tool_registry=tool_registry,
            tool_workspace=tool_workspace,
            operation_scope=f"{run_id}-solver",
        )
        payload = {
            "schema_version": 1,
            "run_id": run_id,
            "request_sha256": request_sha256,
            "task_sha256": task_sha256,
            "solver_model": self.solver_model,
            "output_contract_sha256": task_run.output_contract_sha256,
            "harness_sha256": task_run.harness_sha256,
            "candidate": task_run.candidate,
            "events": [asdict(event) for event in task_run.events],
        }
        self.workspace.record_solver_result(run_id=run_id, payload=payload)
        return payload

    def _load_or_run_evaluator(
        self,
        *,
        run_id: str,
        request_sha256: str,
        task_sha256: str,
        solver_result: Mapping[str, Any],
        evaluator: Callable[[str], EvaluationResult],
    ) -> dict[str, Any]:
        trace = self.workspace.load_trace(run_id, missing_ok=True)
        if trace is not None:
            return trace
        self._claim_external_operation(run_id, "evaluator", request_sha256)
        evaluation = evaluator(solver_result["candidate"])
        if not isinstance(evaluation, EvaluationResult):
            raise TypeError("evaluator must return EvaluationResult")
        public = evaluation.public
        events = tuple(HarnessTraceEvent(**event) for event in solver_result["events"])
        self.workspace.record_trace(
            run_id=run_id,
            harness_sha256=solver_result["harness_sha256"],
            candidate=solver_result["candidate"],
            task_sha256=task_sha256,
            request_sha256=request_sha256,
            solver_model=self.solver_model,
            events=events,
            score=public.score,
            feedback=public.feedback,
        )
        trace = self.workspace.load_trace(run_id)
        assert trace is not None
        return trace

    def _load_or_run_builder(
        self,
        *,
        run_id: str,
        request_sha256: str,
        harness_sha256: str,
        score: float | None,
        feedback: str,
        probe: Callable[[TaskHarnessArtifact], bool] | None,
        update_champion: bool,
    ) -> BuilderEvolutionResult:
        saved = self.workspace.load_builder_trace(run_id, missing_ok=True)
        if saved is not None:
            if saved.get("previous_harness_sha256") != harness_sha256:
                raise ValueError("Builder trace lineage is invalid")
            if saved.get("next_harness_sha256") != self.workspace.current().sha256:
                raise RuntimeError("Builder trace does not match the current Harness")
            return BuilderEvolutionResult(
                status=saved["status"],
                previous_sha256=harness_sha256,
                candidate_sha256=saved["candidate_harness_sha256"],
                reason=saved["reason"],
                builder_harness_sha256=saved["builder_harness_sha256"],
                events=(),
                source_sha256=saved.get("source_sha256"),
                changed_components=tuple(saved.get("changed_components", ())),
            )

        commit_receipt = self.workspace.load_commit_receipt(run_id, missing_ok=True)
        if commit_receipt is not None:
            previous = commit_receipt.get("previous_sha256")
            if previous != harness_sha256 and not self.workspace.same_lineage(
                str(previous), harness_sha256
            ):
                raise RuntimeError("commit receipt belongs to a different Harness lineage")
            current = self.workspace.recover_owned_commit(run_id)
            events = tuple(
                BuilderStepEvent(step=step, output="recovered_owned_commit")
                for step in self.builder.spec.steps
            )
            evolution = BuilderEvolutionResult(
                status="committed",
                previous_sha256=harness_sha256,
                candidate_sha256=current.sha256,
                reason="recovered this round's committed Harness after interruption",
                builder_harness_sha256=self.builder.spec.sha256,
                events=events,
                source_sha256=current.parent_sha256,
            )
        else:
            if self.workspace.current().sha256 != harness_sha256:
                raise IncompleteRoundError(
                    "workspace advanced after this round's lower Harness execution"
                )
            self._claim_external_operation(run_id, "builder", request_sha256)
            evolution = self.builder.evolve_once(
                score=score,
                feedback=feedback,
                probe=probe,
                run_id=run_id,
                update_champion=update_champion,
            )
            current = self.workspace.current()
        self.workspace.record_builder_trace(
            run_id=run_id,
            builder_harness_sha256=evolution.builder_harness_sha256,
            status=evolution.status,
            events=evolution.events,
            previous_harness_sha256=evolution.previous_sha256,
            candidate_harness_sha256=evolution.candidate_sha256,
            next_harness_sha256=current.sha256,
            reason=evolution.reason,
            source_sha256=evolution.source_sha256,
            changed_components=evolution.changed_components,
        )
        return evolution

    def _claim_external_operation(
        self, run_id: str, stage: str, request_sha256: str
    ) -> None:
        claim = self.workspace.load_operation_claim(
            run_id=run_id,
            stage=stage,
            missing_ok=True,
        )
        if claim is not None:
            if claim.get("request_sha256") != request_sha256:
                raise ValueError("run id is already bound to a different round request")
            raise IncompleteRoundError(
                f"{stage} started without a durable result; automatic retry is disabled"
            )
        self.workspace.claim_operation(
            run_id=run_id,
            stage=stage,
            request_sha256=request_sha256,
        )

    def _replay_receipt(
        self, run_id: str, request_sha256: str
    ) -> DualHarnessRoundResult | None:
        receipt = self.workspace.load_round_receipt(run_id, missing_ok=True)
        if receipt is None:
            return None
        if (
            receipt.get("schema_version") != 1
            or receipt.get("run_id") != run_id
            or receipt.get("request_sha256") != request_sha256
        ):
            raise ValueError("run id is already bound to a different round request")
        return DualHarnessRoundResult.from_dict(receipt.get("result"))

    def _validate_saved_trace(
        self, trace: Mapping[str, Any], request_sha256: str
    ) -> None:
        if trace.get("request_sha256") != request_sha256:
            raise ValueError("run id is already bound to a different round request")
        PublicEvaluation(trace.get("score"), trace.get("feedback"))
        if not isinstance(trace.get("candidate"), str) or not trace["candidate"].strip():
            raise ValueError("saved run trace has an invalid candidate")

    def _request_sha256(
        self,
        *,
        task_sha256: str,
        execution_contract_sha256: str,
    ) -> str:
        payload = {
            "task_sha256": task_sha256,
            "execution_contract_sha256": execution_contract_sha256,
            "output_contract_sha256": self.task_runtime.output_contract_sha256,
            "solver_model": self.solver_model,
            "builder_model": self.builder.model,
            "builder_harness_sha256": self.builder.spec.sha256,
        }
        encoded = json.dumps(payload, sort_keys=True, separators=(",", ":"))
        return hashlib.sha256(encoded.encode("utf-8")).hexdigest()
