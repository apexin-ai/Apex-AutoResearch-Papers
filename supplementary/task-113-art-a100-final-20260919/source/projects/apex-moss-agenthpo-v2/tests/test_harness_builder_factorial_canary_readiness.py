from __future__ import annotations

import copy
import json

import pytest

from optimization_lab.harness_builder.factorial_contract import (
    factorial_main_matrix_projection,
    verify_factorial_contract,
)
from optimization_lab.harness_builder.factorial_canary_readiness import (
    FactorialCanaryReadinessArtifact,
    FactorialCanaryReadinessError,
    build_factorial_canary_readiness,
    canonical_factorial_canary_readiness_bytes,
    verify_factorial_canary_readiness,
)


_ZERO_ENTITLEMENT = {
    "cpu_evaluator_seconds": 0,
    "evaluator_transactions": 0,
    "gpu_exclusive_seconds": 0,
    "max_parallel": 0,
    "model_calls": 0,
}


def _payload() -> dict[str, object]:
    return build_factorial_canary_readiness().to_dict()


def test_artifact_is_canonical_content_addressed_and_zero_authority() -> None:
    artifact = verify_factorial_canary_readiness()
    payload = artifact.to_dict()

    assert payload["artifact_id"] == "moss-factorial-canary-readiness-v1"
    assert payload["artifact_kind"] == "ZERO_CALL_READINESS_AND_SCHEDULE"
    assert payload["execution_authority"] == "NOT_GRANTED"
    assert payload["execution_entitlement"] == _ZERO_ENTITLEMENT
    assert payload["status"] == "BLOCKED_ZERO_ENTITLEMENT"
    assert artifact.canonical_bytes == canonical_factorial_canary_readiness_bytes(
        payload
    )
    assert len(artifact.sha256) == 64

    for suite in payload["suites"].values():
        assert suite["execution_authority"] == "NOT_GRANTED"
        assert suite["execution_entitlement"] == _ZERO_ENTITLEMENT
        assert suite["status"] == "BLOCKED_READINESS"

    assert payload["privacy_boundary"] == {
        "benchmark_runtime_connected": False,
        "evaluator_connected": False,
        "gdpevo_gold_representation": (
            "OPAQUE_CONTROLLER_ROLE_ONLY_NO_PATH_BYTES_OR_CONTENT_HASH"
        ),
        "private_gold_content_read": False,
        "provider_connected": False,
    }


def test_agenthpo_q7_baseline_schedule_is_exactly_fourteen_transactions() -> None:
    suite = _payload()["suites"]["agenthpobench"]
    schedule = suite["q7_baseline_schedule"]

    assert len(schedule) == 14
    assert len({item["schedule_id"] for item in schedule}) == 14
    assert sum(item["planned_evaluator_transactions"] for item in schedule) == 14
    assert {item["candidate_kind"] for item in schedule} == {"frozen_baseline"}
    assert {item["repeat_index"] for item in schedule} == {1, 2}
    assert all(item["status"] == "PLANNED_NOT_AUTHORIZED" for item in schedule)

    task_ids = suite["scope_boundary"]["qualification_task_ids"]
    assert len(task_ids) == 7
    assert {
        task_id: [
            item["repeat_index"]
            for item in schedule
            if item["task_id"] == task_id
        ]
        for task_id in task_ids
    } == {task_id: [1, 2] for task_id in task_ids}
    assert suite["planned_work"] == {
        "baseline_evaluator_transactions": 14,
        "baseline_repeat_count": 2,
        "baseline_task_count": 7,
        "negative_assertion_count": 21,
        "negative_evaluator_transactions": 0,
        "negative_model_calls": 0,
    }


def test_agenthpo_three_negative_kinds_make_twenty_one_pre_evaluator_assertions() -> None:
    suite = _payload()["suites"]["agenthpobench"]
    assertions = suite["codec_pre_evaluator_assertions"]

    assert len(assertions) == 21
    assert len({item["assertion_id"] for item in assertions}) == 21
    assert {item["negative_kind"] for item in assertions} == {
        "unknown_key",
        "out_of_range_value",
        "no_operational_change",
    }
    assert {
        kind: sum(item["negative_kind"] == kind for item in assertions)
        for kind in {
            "unknown_key",
            "out_of_range_value",
            "no_operational_change",
        }
    } == {
        "unknown_key": 7,
        "out_of_range_value": 7,
        "no_operational_change": 7,
    }
    assert all(
        item["stage"] == "STRICT_CODEC_BEFORE_EVALUATOR"
        and item["expected_disposition"]
        == "strict_codec_reject_before_evaluator"
        and item["planned_evaluator_transactions"] == 0
        and item["planned_model_calls"] == 0
        and item["status"] == "ZERO_CALL_ASSERTION_ONLY"
        for item in assertions
    )


def test_agenthpo_formal_tasks_remain_blocked_by_smoke_assets_and_free_form_codec() -> None:
    suite = _payload()["suites"]["agenthpobench"]
    boundary = suite["scope_boundary"]
    formal = suite["formal_task_readiness"]

    assert boundary["overlap"] == []
    assert boundary["formal_task_smoke_required"] is True
    assert boundary["qualification_transfer_to_formal"] == (
        "FORBIDDEN_WITHOUT_FORMAL_SMOKE"
    )
    assert len(boundary["formal_task_ids"]) == len(formal) == 12
    assert all(item["status"] == "BLOCKED" for item in formal)
    assert all(len(item["smoke_blockers"]) == 2 for item in formal)
    assert all(len(item["environment_asset_blockers"]) == 4 for item in formal)

    room = next(
        item
        for item in formal
        if item["task_id"] == "agent_lightning_room_selector"
    )
    assert room["action_contract_blockers"] == [
        "agenthpobench_free_form_prompt_codec_or_fresh_split_required"
    ]
    assert all(
        not item["action_contract_blockers"]
        for item in formal
        if item["task_id"] != "agent_lightning_room_selector"
    )


def test_gdpevo_schedule_is_thirty_candidates_per_kind_repeated_twice() -> None:
    suite = _payload()["suites"]["gdpevo"]
    schedule = suite["evaluator_schedule"]

    assert len(schedule) == 180
    assert len({item["schedule_id"] for item in schedule}) == 180
    assert sum(item["planned_evaluator_transactions"] for item in schedule) == 180
    assert {
        kind: sum(item["candidate_kind"] == kind for item in schedule)
        for kind in {"gold", "template", "blank"}
    } == {"gold": 60, "template": 60, "blank": 60}
    assert {item["repeat_index"] for item in schedule} == {1, 2}
    assert len({item["task_id"] for item in schedule}) == 30
    assert all(item["private_gold_content_embedded"] is False for item in schedule)
    assert all(item["status"] == "PLANNED_NOT_AUTHORIZED" for item in schedule)

    gold = [item for item in schedule if item["candidate_kind"] == "gold"]
    assert all(item["expected_normalized_score"] == 1.0 for item in gold)
    assert all(
        item["candidate_materialization"]
        == "OPAQUE_CONTROLLER_PRIVATE_REFERENCE_AFTER_AUTHORITY"
        for item in gold
    )
    non_gold = [item for item in schedule if item["candidate_kind"] != "gold"]
    assert all(item["expected_normalized_score"] == 0.0 for item in non_gold)
    assert suite["planned_work"] == {
        "candidate_count_by_kind": {"blank": 30, "gold": 30, "template": 30},
        "deterministic_repeat_count": 2,
        "evaluator_transactions": 180,
        "model_calls": 0,
    }


def test_gdpevo_isolation_image_manifest_and_formal_smoke_are_explicit_blockers() -> None:
    suite = _payload()["suites"]["gdpevo"]
    gates = suite["readiness_gates"]
    boundary = suite["scope_boundary"]
    formal = suite["formal_group_readiness"]

    assert set(gates) == {"image", "isolation", "manifest"}
    assert all(gate["status"] == "BLOCKED" for gate in gates.values())
    assert len(gates["isolation"]["blockers"]) == 5
    assert len(gates["image"]["blockers"]) == 3
    assert len(gates["manifest"]["blockers"]) == 3
    assert boundary["overlap"] == []
    assert boundary["formal_group_smoke_required"] is True
    assert len(boundary["formal_group_ids"]) == len(formal) == 6
    assert all(len(item["task_ids"]) == 5 for item in formal)
    assert all(item["status"] == "BLOCKED" for item in formal)
    assert all(
        "gdpevo_formal_group_tree_evaluator_manifest_smoke_pending"
        in item["environment_asset_blockers"]
        for item in formal
    )
    formal_task_ids = {
        task_id for item in formal for task_id in item["task_ids"]
    }
    matrix_task_ids = {
        item["instance_id"]
        for item in factorial_main_matrix_projection(verify_factorial_contract())
        if item["benchmark_id"] == "gdpevo"
    }
    assert formal_task_ids == matrix_task_ids
    assert all(":test_0" not in task_id for task_id in formal_task_ids)


def test_gdpevo_artifact_does_not_embed_private_gold_paths_or_bytes() -> None:
    payload = _payload()
    encoded = canonical_factorial_canary_readiness_bytes(payload).decode("utf-8")

    assert "output/answer.json" not in encoded
    assert '"gold_path"' not in encoded
    assert '"gold_sha256"' not in encoded
    assert '"gold_bytes"' not in encoded
    assert payload["privacy_boundary"]["private_gold_content_read"] is False


def test_drift_noncanonical_duplicate_and_execute_request_fail_closed() -> None:
    artifact = build_factorial_canary_readiness()
    verify_factorial_canary_readiness(artifact)
    verify_factorial_canary_readiness(artifact.canonical_bytes)
    verify_factorial_canary_readiness(artifact.to_dict())

    drifted = copy.deepcopy(artifact.to_dict())
    drifted["suites"]["gdpevo"]["planned_work"][
        "evaluator_transactions"
    ] = 179
    with pytest.raises(FactorialCanaryReadinessError, match="differs"):
        verify_factorial_canary_readiness(drifted)

    noncanonical = json.dumps(artifact.to_dict(), indent=2).encode("utf-8")
    with pytest.raises(FactorialCanaryReadinessError, match="canonically"):
        FactorialCanaryReadinessArtifact(noncanonical)

    with pytest.raises(FactorialCanaryReadinessError, match="repeats"):
        FactorialCanaryReadinessArtifact(
            b'{"execution_authority":"NOT_GRANTED",'
            b'"execution_authority":"NOT_GRANTED"}\n'
        )

    with pytest.raises(FactorialCanaryReadinessError, match="no execution"):
        verify_factorial_canary_readiness(request_execution=True)

    authority = artifact.to_dict()
    authority["execution_authority"] = "GRANTED"
    with pytest.raises(FactorialCanaryReadinessError, match="cannot grant"):
        FactorialCanaryReadinessArtifact.from_payload(authority)

    entitlement = artifact.to_dict()
    entitlement["execution_entitlement"]["evaluator_transactions"] = 1
    with pytest.raises(FactorialCanaryReadinessError, match="remain zero"):
        FactorialCanaryReadinessArtifact.from_payload(entitlement)

    nested_entitlement = artifact.to_dict()
    nested_entitlement["suites"]["gdpevo"]["execution_entitlement"][
        "evaluator_transactions"
    ] = 1
    with pytest.raises(FactorialCanaryReadinessError, match="must be zero"):
        FactorialCanaryReadinessArtifact.from_payload(nested_entitlement)
