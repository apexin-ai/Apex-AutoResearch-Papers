from __future__ import annotations

import json

import pytest

from optimization_lab.harness_builder.adapters.agenthpo_v2 import (
    AgentHPOOutcome,
    run_agenthpo_v2_task,
)
from optimization_lab.harness_builder.agenthpo_intervention import (
    DiscreteInterventionSpace,
    AgentHPOInterventionError,
)


def _space(step: int, current: dict[str, object], previous: str) -> DiscreteInterventionSpace:
    assert step >= 1 and previous
    return DiscreteInterventionSpace(
        task_id="demo",
        task_source_sha256="a" * 64,
        current_config=current,
        allowed_values={"x": (0, 1, 2, 3, 4, 5)},
    )


def test_v2_runner_has_exact_six_stage_trace_and_explicit_keep() -> None:
    evaluated: list[dict[str, object]] = []

    def decide(*, step, **kwargs):
        assert kwargs["public_state"].task_id == "demo"
        assert kwargs["scaffold"].task_id == "demo"
        return json.dumps({"x": 1 if step == 2 else step}).encode()

    def evaluate(configuration, *, step):
        evaluated.append(dict(configuration))
        return AgentHPOOutcome(metric=float(configuration["x"]), diagnostics={"step": step})

    trace = run_agenthpo_v2_task(
        task_card={"task_id": "demo", "public": True},
        task_id="demo",
        baseline_configuration={"x": 0},
        baseline_outcome=AgentHPOOutcome(metric=0.0),
        space_for_step=_space,
        decide=decide,
        evaluate=evaluate,
        model="test-model",
        replicate_seed=42,
    )
    assert len(evaluated) == 5
    assert len(trace.history) == 6
    assert len(trace.decisions) == 5
    assert trace.decisions[1]["explicit_keep"] is True
    assert trace.final_metric == 5.0
    assert trace.to_result_dict()["protocol"] == "agenthpobench_baseline_plus_five_v1"


def test_v2_runner_rejects_malformed_response_before_evaluator() -> None:
    evaluated = 0

    def decide(**kwargs):
        del kwargs
        return b'{"x": 999}'

    def evaluate(configuration, *, step):
        nonlocal evaluated
        evaluated += 1
        return AgentHPOOutcome(metric=0.0)

    with pytest.raises(AgentHPOInterventionError, match="outside the allowlist"):
        run_agenthpo_v2_task(
            task_card={"task_id": "demo"},
            task_id="demo",
            baseline_configuration={"x": 0},
            baseline_outcome=AgentHPOOutcome(metric=0.0),
            space_for_step=_space,
            decide=decide,
            evaluate=evaluate,
            model="test-model",
        )
    assert evaluated == 0
