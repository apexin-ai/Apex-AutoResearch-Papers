from __future__ import annotations

import json

import pytest

from optimization_lab.harness_builder.events import ResourceCaps
from optimization_lab.harness_builder.three_arm import (
    THREE_ARMS,
    ThreeArmCampaignContract,
)
from optimization_lab.harness_builder.three_arm_prepare import (
    FROZEN_MODEL_SIGNATURE,
    SUITE_TASKS,
    THREE_ARM_PHASE_ID,
    THREE_ARM_SUITES,
    build_three_arm_cell_caps,
    build_three_arm_stream,
)
from optimization_lab.harness_builder.three_arm_runtime import EXECUTABLE_RULES


def test_three_arm_stream_is_balanced_interleaved_and_uses_six_plus_two() -> None:
    stream = build_three_arm_stream()

    assert len(stream) == 24
    assert len({item["instance_id"] for item in stream}) == 24
    for block_index in range(8):
        offset = block_index % len(THREE_ARM_SUITES)
        expected_suites = (
            THREE_ARM_SUITES[offset:] + THREE_ARM_SUITES[:offset]
        )
        block = stream[block_index * 3 : (block_index + 1) * 3]
        assert [item["suite"] for item in block] == list(expected_suites)
        assert [item["block_index"] for item in block] == [block_index] * 3
        assert [item["task_id"] for item in block] == [
            SUITE_TASKS[suite][block_index] for suite in expected_suites
        ]
        assert {item["learning_mode"] for item in block} == {
            "online" if block_index < 6 else "sealed"
        }
    for index, item in enumerate(stream):
        assert item["stream_index"] == index
        assert item["arm_order"] == list(
            THREE_ARMS[index % 3 :] + THREE_ARMS[: index % 3]
        )


def test_three_arm_entitlements_parse_as_the_full_formal_contract() -> None:
    stream = build_three_arm_stream()
    cells = build_three_arm_cell_caps(stream)
    totals = ResourceCaps(
        model_calls=sum(value.model_calls for value in cells.values()),
        evaluator_transactions=sum(
            value.evaluator_transactions for value in cells.values()
        ),
        gpu_exclusive_seconds=sum(
            value.gpu_exclusive_seconds for value in cells.values()
        ),
        cpu_evaluator_seconds=sum(
            value.cpu_evaluator_seconds for value in cells.values()
        ),
    )
    assert totals == ResourceCaps(
        model_calls=1170,
        evaluator_transactions=576,
        cpu_evaluator_seconds=806400.0,
    )
    payload = {
        "schema_version": 5,
        "phase_id": THREE_ARM_PHASE_ID,
        "code_revision": "a" * 40,
        "model_signature": FROZEN_MODEL_SIGNATURE,
        "execution_ready": True,
        "blockers": [],
        "source_hashes": {"fixture": "b" * 64},
        "budgets": totals.to_dict(),
        "resource_entitlement_totals": totals.to_dict(),
        "cell_entitlements": {
            key: value.to_dict() for key, value in cells.items()
        },
        "rule_ids": ["discipline", "cross_instance_distillation"],
        "variant_ids": list(THREE_ARMS),
        "stream_policy": "balanced_interleaved",
        "validity_policy": {
            "rounds_per_arm": 8,
            "minimum_valid_rounds_per_arm": 4,
            "learning_tasks_per_suite": 6,
            "minimum_paired_learning_tasks": 5,
            "insufficient_status": "insufficient_validity",
            "score_aggregation": "valid_only_mean_and_best",
        },
        "stream": stream,
        "experience_initialization": "empty",
        "online_instances_per_suite": 6,
        "sealed_instances_per_suite": 2,
        "no_next_phase": True,
        "no_paid_provider_fallback": True,
    }

    contract = ThreeArmCampaignContract.from_staging_bytes(
        json.dumps(payload).encode()
    )
    assert contract.global_caps == totals
    assert contract.stream_policy == "balanced_interleaved"
    assert contract.minimum_valid_rounds_per_arm == 4
    assert contract.minimum_paired_learning_tasks == 5
    assert contract.stream[-1].learning_mode == "sealed"

    suite_blocked = []
    for suite in THREE_ARM_SUITES:
        for item in stream:
            if item["suite"] != suite:
                continue
            item = dict(item)
            item["stream_index"] = len(suite_blocked)
            item["arm_order"] = list(
                THREE_ARMS[len(suite_blocked) % 3 :]
                + THREE_ARMS[: len(suite_blocked) % 3]
            )
            suite_blocked.append(item)
    payload["stream"] = suite_blocked
    with pytest.raises(ValueError, match="balanced interleaving"):
        ThreeArmCampaignContract.from_staging_bytes(json.dumps(payload).encode())


def test_three_arm_runtime_uses_only_operational_rules() -> None:
    assert EXECUTABLE_RULES == (
        "contract_compatibility",
        "discipline",
        "dream",
        "law_inversion",
        "recombination",
        "correctness_recovery",
    )
