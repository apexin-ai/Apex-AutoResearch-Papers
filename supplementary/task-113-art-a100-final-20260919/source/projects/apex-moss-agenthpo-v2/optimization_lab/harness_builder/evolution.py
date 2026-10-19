"""Benchmark-neutral multi-round execution around the dual Harness runtime.

Adapters own task prompts and benchmark evaluators.  This module owns the
Solver -> Evaluator -> Builder loop, typed public evaluation boundary,
patience stopping, and immutable best-checkpoint selection.
"""

from __future__ import annotations

import hashlib
import math
import re
from dataclasses import dataclass, field
from typing import Any, Callable, Generic, Mapping, Protocol, TypeVar

from .builder_harness import BuilderHarness
from .dual_harness import HarnessWorkspace, TaskHarnessArtifact, TaskHarnessRuntime
from .dual_runtime import (
    DualHarnessRoundResult,
    DualHarnessRuntime,
    EvaluationResult,
    PublicEvaluation,
)


TaskT = TypeVar("TaskT")
_SHA256 = re.compile(r"[0-9a-f]{64}")


class EvaluatorRunner(Protocol):
    """Typed benchmark evaluator boundary used by the generic runner."""

    def evaluate(self, candidate: str) -> EvaluationResult:
        ...


class CallbackEvaluatorRunner:
    """Adapt a benchmark callback while enforcing the typed public boundary."""

    def __init__(self, callback: Callable[[str], EvaluationResult]) -> None:
        if not callable(callback):
            raise TypeError("evaluator callback must be callable")
        self.callback = callback

    def evaluate(self, candidate: str) -> EvaluationResult:
        result = self.callback(candidate)
        if not isinstance(result, EvaluationResult):
            raise TypeError("evaluator callback must return EvaluationResult")
        PublicEvaluation(result.public.score, result.public.feedback)
        return result


class TaskHarnessEvolutionAdapter(Protocol[TaskT]):
    contract_sha256: str
    solver_model: str
    task: TaskT

    def task_prompt(self, task: TaskT) -> str:
        ...

    def tools(self, task: TaskT) -> Mapping[str, Callable[[Any], Any]]:
        ...

    def evaluator(self, task: TaskT) -> EvaluatorRunner:
        ...

    def probe(self, task: TaskT, artifact: TaskHarnessArtifact) -> bool:
        ...

    def preserves_capability(
        self,
        task: TaskT,
        previous: TaskHarnessArtifact,
        current: TaskHarnessArtifact,
    ) -> tuple[bool, str]:
        ...


@dataclass(frozen=True)
class HarnessRoundAssessment:
    round_index: int
    harness_sha256: str
    next_harness_sha256: str
    verifiable: bool
    attributable: bool
    rollbackable: bool
    preserves_capability: bool
    score_valid: bool
    score_delta_vs_best: float | None
    disposition: str
    reasons: tuple[str, ...]
    change_summary: Mapping[str, Any] = field(default_factory=dict)
    builder_status: str = "unknown"
    builder_reason: str = ""


def summarize_harness_change(
    previous: TaskHarnessArtifact, current: TaskHarnessArtifact
) -> dict[str, Any]:
    """Return a deterministic, benchmark-neutral summary of a Harness diff."""

    before_spec = previous.spec.to_dict()
    after_spec = current.spec.to_dict()
    before = before_spec["nodes"]
    after = after_spec["nodes"]
    before_by_id = {node["id"]: node for node in before}
    after_by_id = {node["id"]: node for node in after}
    added = sorted(set(after_by_id) - set(before_by_id))
    removed = sorted(set(before_by_id) - set(after_by_id))
    changed = sorted(
        node_id
        for node_id in set(before_by_id) & set(after_by_id)
        if before_by_id[node_id] != after_by_id[node_id]
    )
    changed_kinds = sorted(
        {
            f"{before_by_id[node_id]['kind']}->{after_by_id[node_id]['kind']}"
            for node_id in changed
        }
    )
    changed_components = []
    if before != after:
        changed_components.append("execution")
    for component in ("interface", "memory", "capabilities", "router"):
        if before_spec.get(component, {}) != after_spec.get(component, {}):
            changed_components.append(component)
    return {
        "from_sha256": previous.sha256,
        "to_sha256": current.sha256,
        "changed": bool(changed_components),
        "changed_components": sorted(changed_components),
        "added_node_ids": added,
        "removed_node_ids": removed,
        "changed_node_ids": changed,
        "changed_kinds": changed_kinds,
        "node_count_before": len(before),
        "node_count_after": len(after),
        "node_count_delta": len(after) - len(before),
        "parent_sha256": current.parent_sha256,
        "version": current.version,
    }


@dataclass(frozen=True)
class TaskHarnessEvolutionResult:
    run_id: str
    rounds: tuple[DualHarnessRoundResult, ...]
    assessments: tuple[HarnessRoundAssessment, ...]
    best_harness_sha256: str
    best_score: float | None
    stop_reason: str


class TaskHarnessEvolutionCampaign(Generic[TaskT]):
    """Run a benchmark-neutral sequential Harness lineage."""

    def __init__(
        self,
        *,
        workspace: HarnessWorkspace,
        adapter: TaskHarnessEvolutionAdapter[TaskT],
        task_runtime: TaskHarnessRuntime,
        builder: BuilderHarness,
    ) -> None:
        if builder.workspace.root != workspace.root:
            raise ValueError("Builder and Task Harness must share one workspace")
        if not _SHA256.fullmatch(adapter.contract_sha256):
            raise ValueError("adapter contract hash is invalid")
        self.workspace = workspace
        self.adapter = adapter
        self.task_runtime = task_runtime
        self.builder = builder

    def run(
        self,
        *,
        run_id: str,
        max_rounds: int,
        patience: int = 3,
        promotion_margin: float = 0.0,
    ) -> TaskHarnessEvolutionResult:
        if not isinstance(max_rounds, int) or isinstance(max_rounds, bool) or max_rounds < 1:
            raise ValueError("max_rounds must be a positive integer")
        if not isinstance(patience, int) or isinstance(patience, bool) or patience < 1:
            raise ValueError("patience must be a positive integer")
        if not isinstance(promotion_margin, (int, float)) or isinstance(promotion_margin, bool):
            raise ValueError("promotion_margin must be numeric")

        runtime = DualHarnessRuntime(
            workspace=self.workspace,
            task_runtime=self.task_runtime,
            builder=self.builder,
            solver_model=self.adapter.solver_model,
        )
        task_text = self.adapter.task_prompt(self.adapter.task)
        evaluator = self.adapter.evaluator(self.adapter.task)
        rounds: list[DualHarnessRoundResult] = []
        assessments: list[HarnessRoundAssessment] = []
        initial_active = self.workspace.current()
        if not self.workspace.champion_path.is_file():
            self.workspace.set_champion(initial_active.sha256)
        best_hash: str = self.workspace.champion().sha256
        best_score: float | None = None
        stale_rounds = 0

        for index in range(1, max_rounds + 1):
            round_id = f"{run_id}-round-{index:03d}"
            saved_trace = self.workspace.load_trace(round_id, missing_ok=True)
            before = (
                self.workspace.load_artifact(saved_trace["harness_sha256"])
                if saved_trace is not None
                else self.workspace.current()
            )
            def public_probe(artifact: TaskHarnessArtifact) -> bool:
                if not self.adapter.probe(self.adapter.task, artifact):
                    return False
                preserved, _ = self.adapter.preserves_capability(
                    self.adapter.task, before, artifact
                )
                return preserved

            result = runtime.run_round(
                run_id=round_id,
                execution_contract_sha256=self.adapter.contract_sha256,
                task=task_text,
                tools=self.adapter.tools(self.adapter.task),
                evaluator=evaluator.evaluate,
                probe=public_probe,
                evolve_builder=index < max_rounds,
                update_champion=False,
            )
            after = self.workspace.current()
            public = PublicEvaluation(result.score, result.feedback)
            score_valid = public.score is not None and math.isfinite(float(public.score))
            previous_best = best_score
            is_promotion = (
                score_valid
                and (best_score is None or public.score > best_score + promotion_margin)
            )
            if is_promotion:
                best_hash = result.harness_sha256
                best_score = public.score
                self.workspace.set_champion(result.harness_sha256)
                stale_rounds = 0
            else:
                stale_rounds += 1
            preserved, capability_reason = self.adapter.preserves_capability(
                self.adapter.task,
                before,
                after,
            )
            verifiable = score_valid and result.builder_status in {
                "committed",
                "rolled_back",
                "rejected",
                "not_run",
            }
            attributable = (
                _SHA256.fullmatch(result.harness_sha256) is not None
                and _SHA256.fullmatch(result.next_harness_sha256) is not None
                and self.workspace.load_trace(round_id, missing_ok=True) is not None
            )
            rollbackable = (
                self.workspace.load_artifact(result.harness_sha256).sha256
                == result.harness_sha256
            )
            builder_trace = self.workspace.load_builder_trace(round_id, missing_ok=True)
            if not verifiable or not attributable or not rollbackable or not preserved:
                disposition = "invalid"
            elif result.builder_status in {"rejected", "rolled_back", "not_run"}:
                disposition = "accepted_exploration"
            elif is_promotion:
                disposition = "accepted_improvement"
            else:
                disposition = "accepted_exploration"
            change_summary = summarize_harness_change(before, after)
            reasons = (capability_reason,) if capability_reason else ()
            if not score_valid:
                reasons += ("public score is invalid",)
            self.workspace.record_round_assessment(
                run_id=round_id,
                payload={
                    "schema_version": 1,
                    "run_id": round_id,
                    "lineage_run_id": run_id,
                    "assessment": {
                        "round_index": index,
                        "harness_sha256": result.harness_sha256,
                        "next_harness_sha256": result.next_harness_sha256,
                        "verifiable": verifiable,
                        "attributable": attributable,
                        "rollbackable": rollbackable,
                        "preserves_capability": preserved,
                        "score_valid": score_valid,
                        "score_delta_vs_best": (
                            None
                            if previous_best is None or public.score is None
                            else round(float(public.score - previous_best), 12)
                        ),
                        "disposition": disposition,
                        "reasons": list(reasons),
                        "builder_status": result.builder_status,
                        "builder_reason": builder_trace.get("reason", "")
                        if builder_trace
                        else "",
                    },
                    "change_summary": change_summary,
                },
            )
            assessments.append(
                HarnessRoundAssessment(
                    round_index=index,
                    harness_sha256=result.harness_sha256,
                    next_harness_sha256=result.next_harness_sha256,
                    verifiable=verifiable,
                    attributable=attributable,
                    rollbackable=rollbackable,
                    preserves_capability=preserved,
                    score_valid=score_valid,
                    score_delta_vs_best=(
                        None
                        if previous_best is None or public.score is None
                        else round(float(public.score - previous_best), 12)
                    ),
                    disposition=disposition,
                    reasons=reasons,
                    change_summary=change_summary,
                    builder_status=result.builder_status,
                    builder_reason=builder_trace.get("reason", "") if builder_trace else "",
                )
            )
            rounds.append(result)
            if stale_rounds >= patience:
                return TaskHarnessEvolutionResult(
                    run_id=run_id,
                    rounds=tuple(rounds),
                    assessments=tuple(assessments),
                    best_harness_sha256=best_hash,
                    best_score=best_score,
                    stop_reason="patience_exhausted",
                )
        assert best_hash is not None
        return TaskHarnessEvolutionResult(
            run_id=run_id,
            rounds=tuple(rounds),
            assessments=tuple(assessments),
            best_harness_sha256=best_hash,
            best_score=best_score,
            stop_reason="max_rounds",
        )
