from __future__ import annotations

import json

import pytest

from optimization_lab.harness_builder.factorial_online_plan import (
    FactorialOnlinePlanError,
    FactorialOnlineZeroCallPlan,
    ONLINE_MAIN_OVERLAP_POLICY,
    ONLINE_STATE_LINEAGE_STATUS,
    ONLINE_TASK_AUTHORITY_STATUS,
)


def _canonical(payload: object) -> bytes:
    return (
        json.dumps(
            payload,
            allow_nan=False,
            ensure_ascii=False,
            separators=(",", ":"),
            sort_keys=True,
        )
        + "\n"
    ).encode()


def test_exact_online_plan_expands_all_three_mechanisms_and_costs() -> None:
    plan = FactorialOnlineZeroCallPlan.from_verified_contract()

    assert plan.execution_authority == "NOT_GRANTED"
    assert plan.model_call_entitlement == 0
    assert plan.evaluator_transaction_entitlement == 0
    assert plan.task_artifact_authority_status == ONLINE_TASK_AUTHORITY_STATUS
    assert plan.state_lineage_binding_status == ONLINE_STATE_LINEAGE_STATUS
    assert plan.main_experiment_overlap_policy == ONLINE_MAIN_OVERLAP_POLICY
    assert plan.independent_fresh_confirmation is False
    assert len(plan.attempt_slots) == 732
    assert len(plan.update_slots) == 84
    assert plan.logical_model_calls == 1548
    assert plan.logical_evaluator_transactions == 732
    assert {slot.stage for slot in plan.attempt_slots} == {"source", "O1", "O2"}
    assert {slot.mechanism_id for slot in plan.update_slots} == {"OM", "OP", "OA"}
    assert {
        slot.mechanism_id for slot in plan.attempt_slots if slot.stage != "source"
    } == {"O0", "OM", "OP", "OA"}
    assert {
        stage: sum(slot.stage == stage for slot in plan.attempt_slots)
        for stage in ("source", "O1", "O2")
    } == {"source": 108, "O1": 144, "O2": 480}
    assert dict(plan.mechanism_state_roots) == {
        "O0": "NONE",
        "OM": "online/OM/meta-memory",
        "OP": "online/OP/meta-policy",
        "OA": "online/OA/harness-archive",
    }


def test_online_plan_canonical_replay_rederives_verified_contract() -> None:
    plan = FactorialOnlineZeroCallPlan.from_verified_contract()
    replayed = FactorialOnlineZeroCallPlan.from_canonical_bytes(
        plan.canonical_bytes, expected_sha256=plan.sha256
    )
    assert replayed == plan
    assert replayed.sha256 == plan.sha256


@pytest.mark.parametrize(
    "mutation",
    (
        lambda payload: payload["attempt_slots"].pop(),
        lambda payload: payload["update_slots"].append(
            dict(payload["update_slots"][0])
        ),
        lambda payload: payload["mechanism_state_roots"].__setitem__(
            "OA", payload["mechanism_state_roots"]["OM"]
        ),
        lambda payload: payload["stage_budget_projection"][0].__setitem__(
            "logical_model_calls_incremental", 299
        ),
        lambda payload: payload.__setitem__(
            "task_artifact_authority_status", "READY"
        ),
        lambda payload: payload.__setitem__(
            "state_lineage_binding_status", "READY"
        ),
        lambda payload: payload.__setitem__(
            "independent_fresh_confirmation", True
        ),
        lambda payload: payload.__setitem__("execution_authority", "GRANTED"),
        lambda payload: payload.__setitem__("model_call_entitlement", 1),
    ),
)
def test_online_plan_rejects_missing_duplicate_rebound_or_authority_forgery(
    mutation,
) -> None:
    payload = json.loads(
        FactorialOnlineZeroCallPlan.from_verified_contract().canonical_bytes
    )
    mutation(payload)
    with pytest.raises(FactorialOnlinePlanError):
        FactorialOnlineZeroCallPlan.from_canonical_bytes(_canonical(payload))


def test_online_plan_rejects_self_rehashed_attempt_identity() -> None:
    payload = json.loads(
        FactorialOnlineZeroCallPlan.from_verified_contract().canonical_bytes
    )
    slot = payload["attempt_slots"][0]
    slot["instance_id"] = "forged-task"
    with pytest.raises(FactorialOnlinePlanError, match="attempt id differs"):
        FactorialOnlineZeroCallPlan.from_canonical_bytes(_canonical(payload))


def test_online_plan_operation_ids_are_exact_and_globally_unique() -> None:
    plan = FactorialOnlineZeroCallPlan.from_verified_contract()
    operation_ids = [
        operation_id
        for slot in plan.attempt_slots
        for operation_id in (
            slot.builder_operation_id,
            slot.solution_operation_id,
            slot.evaluator_operation_id,
        )
    ] + [slot.updater_operation_id for slot in plan.update_slots]
    assert len(operation_ids) == 2280
    assert len(operation_ids) == len(set(operation_ids))
    assert all(identifier.startswith("factorial-online:") for identifier in operation_ids)
