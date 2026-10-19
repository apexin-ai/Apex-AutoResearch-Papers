"""AgentHPOBench adapter for the Moss v2 L1 Builder/Harness.

This module owns only the sequential control loop and public-state projection.
The benchmark task adapter remains responsible for deriving the pinned
intervention space and evaluating a configuration.  No evaluator-private data
is passed to the Builder or decision provider.
"""

from __future__ import annotations

import hashlib
import json
from dataclasses import dataclass, field
from typing import Any, Callable, Mapping, Protocol

from ..agenthpo_intervention import (
    DiscreteInterventionSpace,
    StrictIntervention,
    parse_strict_intervention,
)
from ..builder_evolution import (
    BuilderArtifact,
    BuilderPublicState,
    BuilderScaffoldCompiler,
    CompiledBuilderScaffold,
)


class AgentHPODecisionProvider(Protocol):
    def __call__(
        self,
        *,
        task_card: Mapping[str, Any],
        public_state: BuilderPublicState,
        scaffold: CompiledBuilderScaffold,
        space: DiscreteInterventionSpace,
        step: int,
    ) -> bytes:
        ...


class AgentHPOEvaluator(Protocol):
    def __call__(
        self, configuration: Mapping[str, object], *, step: int
    ) -> "AgentHPOOutcome":
        ...


@dataclass(frozen=True)
class AgentHPOOutcome:
    metric: float
    direction: str = "higher"
    feedback: str = "valid"
    diagnostics: Mapping[str, Any] = field(default_factory=dict)

    def __post_init__(self) -> None:
        if self.direction not in {"higher", "lower"}:
            raise ValueError("AgentHPO metric direction must be higher or lower")
        if not isinstance(self.feedback, str) or len(self.feedback) > 32_000:
            raise ValueError("AgentHPO public feedback is invalid")
        if not isinstance(self.diagnostics, Mapping):
            raise ValueError("AgentHPO diagnostics must be public mapping")

    def to_public_dict(self) -> dict[str, Any]:
        return {
            "metric_value": self.metric,
            "direction": self.direction,
            "feedback": self.feedback,
            "diagnostics": dict(self.diagnostics),
        }


@dataclass(frozen=True)
class AgentHPOV2Trace:
    task_id: str
    model: str
    replicate_seed: int | None
    history: tuple[Mapping[str, Any], ...]
    decisions: tuple[Mapping[str, Any], ...]
    raw_responses: tuple[str, ...]
    fallback_decision_count: int = 0

    @property
    def final_metric(self) -> float:
        return float(self.history[-1]["metric_value"])

    @property
    def best_so_far_metric(self) -> float:
        values = [float(item["metric_value"]) for item in self.history]
        direction = self.history[-1]["direction"]
        return (max if direction == "higher" else min)(values)

    def to_result_dict(self) -> dict[str, Any]:
        return {
            "task_id": self.task_id,
            "model": self.model,
            "replicate_seed": self.replicate_seed,
            "history": [dict(item) for item in self.history],
            "decisions": [dict(item) for item in self.decisions],
            "raw_responses": list(self.raw_responses),
            "fallback_decision_count": self.fallback_decision_count,
            "final_metric": self.final_metric,
            "best_so_far_metric": self.best_so_far_metric,
            "protocol": "agenthpobench_baseline_plus_five_v1",
        }


def run_agenthpo_v2_task(
    *,
    task_card: Mapping[str, Any],
    task_id: str,
    baseline_configuration: Mapping[str, object],
    baseline_outcome: AgentHPOOutcome,
    space_for_step: Callable[
        [int, Mapping[str, object], str], DiscreteInterventionSpace
    ],
    decide: AgentHPODecisionProvider,
    evaluate: AgentHPOEvaluator,
    model: str,
    builder_artifact: BuilderArtifact | None = None,
    replicate_seed: int | None = None,
) -> AgentHPOV2Trace:
    """Run one official baseline plus exactly five interventions.

    ``space_for_step`` is trusted adapter code and must derive its result from
    the pinned AgentHPO source.  The decision provider gets only the public
    task card, public history, compiled L1 scaffold and typed space.  A
    malformed response is rejected before ``evaluate`` is called.  Explicit
    keep is enabled because it is a legal upstream action; silent fallback is
    impossible in this runner.
    """

    if not task_id or not model:
        raise ValueError("AgentHPO task_id and model are required")
    history: list[Mapping[str, Any]] = [
        {
            "kind": "baseline",
            "configuration": dict(baseline_configuration),
            **baseline_outcome.to_public_dict(),
        }
    ]
    decisions: list[Mapping[str, Any]] = []
    raw_responses: list[str] = []
    current = dict(baseline_configuration)
    previous_outcome_sha = _sha256(history[-1])
    compiler = BuilderScaffoldCompiler()

    for step in range(1, 6):
        space = space_for_step(step, current, previous_outcome_sha)
        public_state = _public_state(task_id, step, history)
        scaffold = compiler.compile(builder_artifact, public_state) if builder_artifact else None
        if scaffold is None:
            # A fixed v2 artifact is the neutral default for A-fixed and keeps
            # the provider contract identical across experimental arms.
            scaffold = compiler.compile(BuilderArtifact.initial(), public_state)
        raw = decide(
            task_card=task_card,
            public_state=public_state,
            scaffold=scaffold,
            space=space,
            step=step,
        )
        if not isinstance(raw, bytes):
            raise TypeError("AgentHPO decision provider must return bytes")
        intervention = parse_strict_intervention(
            raw, space=space, allow_explicit_keep=True
        )
        outcome = evaluate(intervention.resulting_config, step=step)
        if not isinstance(outcome, AgentHPOOutcome):
            raise TypeError("AgentHPO evaluator must return AgentHPOOutcome")
        explicit_keep = _same_config(
            intervention.resulting_config, space.current_config
        )
        raw_responses.append(raw.decode("utf-8"))
        decisions.append(
            {
                "index": step,
                "configuration": dict(intervention.resulting_config),
                "proposed_changes": dict(intervention.proposed_changes),
                "explicit_keep": explicit_keep,
                "intervention_sha256": intervention.sha256,
                "compiled_scaffold_sha256": scaffold.sha256,
            }
        )
        history.append(
            {
                "kind": f"intervention_{step}",
                "configuration": dict(intervention.resulting_config),
                **outcome.to_public_dict(),
            }
        )
        current = dict(intervention.resulting_config)
        previous_outcome_sha = _sha256(history[-1])

    return AgentHPOV2Trace(
        task_id=task_id,
        model=model,
        replicate_seed=replicate_seed,
        history=tuple(history),
        decisions=tuple(decisions),
        raw_responses=tuple(raw_responses),
    )


def _public_state(
    task_id: str, round_index: int, history: list[Mapping[str, Any]]
) -> BuilderPublicState:
    scores = tuple(
        float(item["metric_value"]) if item.get("metric_value") is not None else None
        for item in history
    )
    latest = history[-1]
    direction = latest.get("direction", "higher")
    valid = [score for score in scores if score is not None]
    best = (max(valid) if direction == "higher" else min(valid)) if valid else None
    return BuilderPublicState(
        schema_version=1,
        task_id=task_id,
        round_index=round_index,
        scores=scores,
        feedback=str(latest.get("feedback", "")),
        diagnostics=dict(latest.get("diagnostics", {})),
        memory={
            "current": {"configuration": dict(latest["configuration"])},
            "best": {"metric_value": best},
            "failures": [
                item.get("feedback", "")
                for item in history
                if str(item.get("feedback", "")).lower().startswith(("error", "invalid", "fail"))
            ],
        },
    )


def _same_config(left: Mapping[str, object], right: Mapping[str, object]) -> bool:
    return set(left) == set(right) and all(
        type(left[key]) is type(right[key]) and left[key] == right[key]
        for key in left
    )


def _sha256(value: Mapping[str, Any]) -> str:
    raw = json.dumps(
        value,
        ensure_ascii=False,
        allow_nan=False,
        sort_keys=True,
        separators=(",", ":"),
    ).encode("utf-8")
    return hashlib.sha256(raw).hexdigest()


__all__ = [
    "AgentHPOEvaluator",
    "AgentHPOOutcome",
    "AgentHPODecisionProvider",
    "AgentHPOV2Trace",
    "run_agenthpo_v2_task",
]
