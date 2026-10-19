from __future__ import annotations

from dataclasses import replace
import os
from pathlib import Path

import pytest

from optimization_lab.harness_builder.events import ResourceVector
from optimization_lab.harness_builder.factorial_coverage import (
    ExactFactorialAttemptMatrix,
)
from optimization_lab.harness_builder.factorial_operation_schedule import (
    ExactFactorialOperationSchedule,
    FactorialOperationScheduleError,
)
from optimization_lab.harness_builder.factorial_task_authority import (
    FactorialTaskArtifactAuthority,
)


_AGENT = Path(
    os.environ.get(
        "MOSS_TEST_AGENTHPO_CHECKOUT",
        "/tmp/moss-bench-qual.rYRM8Q/agenthpobench",
    )
)
_GDP = Path(
    os.environ.get(
        "MOSS_TEST_GDPEVO_CHECKOUT",
        "/tmp/moss-bench-qual.rYRM8Q/gdpevo",
    )
)


@pytest.fixture(scope="module")
def exact():
    if not _AGENT.is_dir() or not _GDP.is_dir():
        pytest.skip("pinned factorial benchmark checkouts are unavailable")
    authority = FactorialTaskArtifactAuthority(
        agenthpo_checkout=_AGENT,
        gdpevo_checkout=_GDP,
    )
    bundle = authority.rederive_exact_bundle()
    plan = authority.build_formal_zero_call_plan(authority.derived_contexts())
    matrix = ExactFactorialAttemptMatrix.from_verified_sources(
        plan=plan,
        bundle=bundle,
        task_authority=authority,
    )
    schedule = ExactFactorialOperationSchedule.from_verified_sources(
        matrix=matrix,
        plan=plan,
        bundle=bundle,
        task_authority=authority,
    )
    return authority, bundle, plan, matrix, schedule


def test_schedule_expands_exact_full_path_counts_without_authority(exact) -> None:
    _authority, _bundle, _plan, matrix, schedule = exact
    assert len(matrix.slots) == 1566
    assert schedule.counts == {
        "evaluator": 1566,
        "potential_side_effect_stages": 4338,
        "solution": 1566,
        "update": 1206,
    }
    assert schedule.full_path_resource_upper_bound == ResourceVector(
        model_calls=2772,
        evaluator_transactions=1566,
    )
    assert schedule.execution_authority == "NOT_GRANTED"
    assert schedule.model_call_entitlement == 0
    assert schedule.evaluator_transaction_entitlement == 0
    assert schedule.gpu_exclusive_second_entitlement == 0
    assert schedule.cpu_evaluator_second_entitlement == 0
    assert schedule.environment_resource_status == (
        "CPU_GPU_CAPS_PENDING_REAL_CANARY"
    )
    assert len({item.logical_operation_id for item in schedule.operations}) == 4338
    assert schedule.sha256 == ExactFactorialOperationSchedule.verify_from_sources(
        schedule,
        matrix=matrix,
        plan=exact[2],
        bundle=exact[1],
        task_authority=exact[0],
    ).sha256


def test_update_roles_are_exact_and_fixed_feedback_has_no_update(exact) -> None:
    _authority, _bundle, _plan, matrix, schedule = exact
    by_attempt: dict[str, list[object]] = {}
    for operation in schedule.operations:
        by_attempt.setdefault(operation.attempt_id, []).append(operation)

    shared = next(slot for slot in matrix.slots if slot.shared_v001)
    shared_ops = by_attempt[shared.attempt_id]
    assert [item.stage for item in shared_ops] == [
        "update",
        "solution",
        "evaluator",
    ]
    assert shared_ops[0].semantic_role == "shared_v001_builder"

    expected_roles = {
        "S-reflection-skill": "task_local_reflection_skill_update",
        "B-targeted": "targeted_harness_builder_update",
        "B-frozen-wide": "wide_harness_builder_update",
    }
    for arm_id, role in expected_roles.items():
        slot = next(
            item
            for item in matrix.slots
            if not item.shared_v001 and item.arm_id == arm_id
        )
        operations = by_attempt[slot.attempt_id]
        assert [item.stage for item in operations] == [
            "update",
            "solution",
            "evaluator",
        ]
        assert operations[0].semantic_role == role
        assert operations[0].journal_operation_kind == "planner_call"

    fixed_slots = [
        item
        for item in matrix.slots
        if not item.shared_v001 and item.arm_id == "A-fixed-feedback"
    ]
    assert len(fixed_slots) == 360
    assert all(
        [item.stage for item in by_attempt[slot.attempt_id]]
        == ["solution", "evaluator"]
        for slot in fixed_slots
    )
    operation_ids = {item.logical_operation_id for item in schedule.operations}
    assert not any(
        slot.update_operation_id in operation_ids
        for slot in fixed_slots
    )


def test_per_cell_full_path_caps_match_benchmark_round_counts(exact) -> None:
    _authority, _bundle, plan, _matrix, schedule = exact
    caps = schedule.per_cell_full_path_caps

    for suite, expected_fixed, expected_adaptive in (
        (
            "agenthpobench",
            ResourceVector(model_calls=5, evaluator_transactions=5),
            ResourceVector(model_calls=10, evaluator_transactions=5),
        ),
        (
            "gdpevo",
            ResourceVector(model_calls=2, evaluator_transactions=2),
            ResourceVector(model_calls=4, evaluator_transactions=2),
        ),
    ):
        key = next(item.key for item in plan.schedules if item.key.suite == suite)
        assert caps[f"factorial-v001-cell:{key.sha256}"] == ResourceVector(
            model_calls=2,
            evaluator_transactions=1,
        )
        assert caps[key.arm_cell_id("A-fixed-feedback")] == expected_fixed
        for arm_id in (
            "S-reflection-skill",
            "B-targeted",
            "B-frozen-wide",
        ):
            assert caps[key.arm_cell_id(arm_id)] == expected_adaptive

    assert len(caps) == 126 + (126 * 4)
    assert all(
        value.gpu_exclusive_seconds == 0.0
        and value.cpu_evaluator_seconds == 0.0
        for value in caps.values()
    )


def test_missing_extra_and_reordered_potential_stages_fail(exact) -> None:
    _authority, _bundle, _plan, _matrix, schedule = exact
    with pytest.raises(FactorialOperationScheduleError, match="4,338"):
        replace(schedule, operations=schedule.operations[:-1])
    with pytest.raises(FactorialOperationScheduleError, match="4,338|repeats"):
        replace(schedule, operations=schedule.operations + (schedule.operations[-1],))

    reordered = replace(
        schedule,
        operations=(schedule.operations[1], schedule.operations[0])
        + schedule.operations[2:],
    )
    with pytest.raises(
        FactorialOperationScheduleError, match="pinned source replay"
    ):
        ExactFactorialOperationSchedule.verify_from_sources(
            reordered,
            matrix=exact[3],
            plan=exact[2],
            bundle=exact[1],
            task_authority=exact[0],
        )


def test_rebound_or_self_rehashed_schedule_cannot_pass_trusted_replay(exact) -> None:
    authority, bundle, plan, matrix, schedule = exact
    operation = schedule.operations[11]
    with pytest.raises(FactorialOperationScheduleError, match="identity differs"):
        replace(
            operation,
            logical_operation_id=operation.logical_operation_id + ":rebound",
        )
    with pytest.raises(
        FactorialOperationScheduleError, match="kind or discrete reservation"
    ):
        replace(operation, semantic_role="benchmark_native_evaluation")

    rebound = replace(operation, slot_sha256="f" * 64)
    forged = replace(
        schedule,
        operations=schedule.operations[:11]
        + (rebound,)
        + schedule.operations[12:],
    )
    assert forged.sha256 != schedule.sha256
    with pytest.raises(
        FactorialOperationScheduleError, match="pinned source replay"
    ):
        ExactFactorialOperationSchedule.verify_from_sources(
            forged,
            matrix=matrix,
            plan=plan,
            bundle=bundle,
            task_authority=authority,
        )

    forged_matrix = replace(
        matrix,
        factorial_plan_sha256="f" * 64,
        slots=tuple(
            replace(slot, factorial_plan_sha256="f" * 64)
            for slot in matrix.slots
        ),
    )
    with pytest.raises(
        FactorialOperationScheduleError, match="pinned source replay"
    ):
        ExactFactorialOperationSchedule.from_verified_sources(
            matrix=forged_matrix,
            plan=plan,
            bundle=bundle,
            task_authority=authority,
        )
