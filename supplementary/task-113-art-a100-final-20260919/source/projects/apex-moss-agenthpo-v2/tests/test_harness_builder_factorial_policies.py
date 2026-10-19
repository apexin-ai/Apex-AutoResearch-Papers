from __future__ import annotations

import json

import pytest

from optimization_lab.harness_builder.factorial_policies import (
    A_FIXED_FEEDBACK,
    ARM_IDS,
    ARM_POLICY_SPECS,
    B_FROZEN_WIDE,
    B_TARGETED,
    EMPTY_TASK_LOCAL_SKILL_SHA256,
    S_REFLECTION_SKILL,
    SkillUpdateReceipt,
    TaskLocalSkillRecord,
    solver_skill_projection,
    validate_arm_transition,
)
from optimization_lab.harness_builder.schema import HarnessDecision


def _decision(**overrides: object) -> HarnessDecision:
    payload: dict[str, object] = {
        "schema_version": 1,
        "rule_id": "discipline",
        "role_graph": ["task_analyst", "generator", "verifier"],
        "memory_views": ["current", "best"],
        "tools": ["task_semantics", "score_history"],
        "parent_strategy": "incumbent",
        "workflow": ["analyze", "select_parent", "generate", "verify_contract"],
        "scheduler_mode": "single_candidate",
        "recovery_mode": "repair_then_reset",
        "kernel_directive": "Use public feedback and preserve correctness.",
    }
    payload.update(overrides)
    return HarnessDecision.from_dict(payload)


def _wide(previous: HarnessDecision) -> HarnessDecision:
    return _decision(
        role_graph=["performance_analyst", "critic", "generator"],
        memory_views=["failures", "structural_diverse"],
        tools=["public_profile", "code_diff"],
        parent_strategy="restart",
        workflow=["inspect", "hypothesize", "criticize", "generate"],
        scheduler_mode="explore_then_exploit",
        recovery_mode="preserve_failure",
        kernel_directive="Try a distinct public-feedback-guided structure.",
    )


def _skill_payload(decision: HarnessDecision, **overrides: object) -> dict[str, object]:
    payload: dict[str, object] = {
        "schema_version": 1,
        "record_kind": "task_local_reflection_skill_v1",
        "cell_id": "suite-a:task-1:seed-1:S",
        "suite": "suite-a",
        "instance_id": "task-1",
        "arm_id": S_REFLECTION_SKILL,
        "version": "v002",
        "parent_skill_sha256": EMPTY_TASK_LOCAL_SKILL_SHA256,
        "source_round_sha256": "2" * 64,
        "frozen_decision_sha256": decision.sha256,
        "frozen_operational_fingerprint": decision.operational_fingerprint,
        "evidence_attempt_ids": ["attempt-v001"],
        "diagnosis": ["The public score indicates an overly broad first search."],
        "preserve": ["Keep the valid public contract shape."],
        "avoid": ["Avoid repeating the same low-value public query."],
        "next_actions": ["Concentrate the next query near the public incumbent."],
    }
    payload.update(overrides)
    return payload


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


def _parse_skill(
    payload: dict[str, object], decision: HarnessDecision
) -> TaskLocalSkillRecord:
    return TaskLocalSkillRecord.from_bytes(
        _canonical(payload),
        expected_cell_id="suite-a:task-1:seed-1:S",
        expected_suite="suite-a",
        expected_instance_id="task-1",
        expected_version="v002",
        expected_parent_skill_sha256=EMPTY_TASK_LOCAL_SKILL_SHA256,
        expected_source_version="v001",
        expected_source_round_sha256="2" * 64,
        expected_frozen_decision_sha256=decision.sha256,
        expected_frozen_operational_fingerprint=decision.operational_fingerprint,
        expected_source_attempt_id="attempt-v001",
        sealed_attempt_ids={"attempt-v001"},
    )


def test_four_arm_specs_freeze_update_kinds_and_change_requirements() -> None:
    assert ARM_IDS == (
        A_FIXED_FEEDBACK,
        S_REFLECTION_SKILL,
        B_TARGETED,
        B_FROZEN_WIDE,
    )
    assert ARM_POLICY_SPECS[A_FIXED_FEEDBACK].update_kind == "none"
    assert ARM_POLICY_SPECS[S_REFLECTION_SKILL].update_kind == "reflection_skill"
    assert ARM_POLICY_SPECS[B_TARGETED].update_policy == "targeted_any_change_v1"
    assert ARM_POLICY_SPECS[B_TARGETED].minimum_material_axis_changes == 1
    assert ARM_POLICY_SPECS[B_FROZEN_WIDE].minimum_material_axis_changes == 7
    assert ARM_POLICY_SPECS[B_FROZEN_WIDE].require_lineage_unique is True


def test_fixed_and_skill_arms_require_byte_semantic_decision_freeze() -> None:
    previous = _decision()
    assert not any(validate_arm_transition(A_FIXED_FEEDBACK, previous, previous).values())
    assert not any(
        validate_arm_transition(S_REFLECTION_SKILL, previous, previous).values()
    )

    directive_only = _decision(kernel_directive="A different solver instruction.")
    with pytest.raises(ValueError, match="frozen Harness decision"):
        validate_arm_transition(A_FIXED_FEEDBACK, previous, directive_only)
    with pytest.raises(ValueError, match="frozen Harness decision"):
        validate_arm_transition(S_REFLECTION_SKILL, previous, directive_only)


def test_targeted_requires_real_axis_change_and_membership_reorder_does_not_count() -> None:
    previous = _decision()
    reordered = _decision(
        role_graph=["verifier", "generator", "task_analyst"],
        memory_views=["best", "current"],
        tools=["score_history", "task_semantics"],
        kernel_directive="Text changes alone are not an architecture change.",
    )
    with pytest.raises(ValueError, match="at least 1 material"):
        validate_arm_transition(B_TARGETED, previous, reordered)

    changed = _decision(parent_strategy="stable_best")
    change_map = validate_arm_transition(B_TARGETED, previous, changed)
    assert change_map["parent_strategy"] is True
    assert sum(change_map.values()) == 1


def test_wide_requires_all_seven_axes_and_unique_bound_lineage() -> None:
    previous = _decision()
    current = _wide(previous)
    change_map = validate_arm_transition(
        B_FROZEN_WIDE, previous, current, [previous.operational_fingerprint]
    )
    assert all(change_map.values())

    six_axes = _decision(
        role_graph=list(current.role_graph),
        memory_views=list(current.memory_views),
        tools=list(current.tools),
        parent_strategy=current.parent_strategy,
        workflow=list(current.workflow),
        scheduler_mode=current.scheduler_mode,
        recovery_mode=previous.recovery_mode,
    )
    with pytest.raises(ValueError, match="at least 7 material"):
        validate_arm_transition(
            B_FROZEN_WIDE, previous, six_axes, [previous.operational_fingerprint]
        )
    with pytest.raises(ValueError, match="not bound"):
        validate_arm_transition(B_FROZEN_WIDE, previous, current, [])
    with pytest.raises(ValueError, match="reuses a lineage fingerprint"):
        validate_arm_transition(
            B_FROZEN_WIDE,
            previous,
            current,
            [current.operational_fingerprint, previous.operational_fingerprint],
        )


def test_skill_parser_binds_task_parent_source_decision_and_sealed_evidence() -> None:
    decision = _decision()
    skill = _parse_skill(_skill_payload(decision), decision)
    assert skill.parent_skill_sha256 == EMPTY_TASK_LOCAL_SKILL_SHA256
    assert skill.sha256 == __import__("hashlib").sha256(skill.canonical_bytes).hexdigest()
    projection = solver_skill_projection(skill)
    assert projection == {
        "skill_kind": "task_local_reflection_skill_v1",
        "skill_sha256": skill.sha256,
        "diagnosis": list(skill.diagnosis),
        "preserve": list(skill.preserve),
        "avoid": list(skill.avoid),
        "next_actions": list(skill.next_actions),
    }
    assert "source_round_sha256" not in projection
    assert solver_skill_projection(None)["skill_kind"] == "NONE"

    with pytest.raises(ValueError, match="unsealed"):
        TaskLocalSkillRecord.from_bytes(
            skill.canonical_bytes,
            expected_cell_id=skill.cell_id,
            expected_suite=skill.suite,
            expected_instance_id=skill.instance_id,
            expected_version=skill.version,
            expected_parent_skill_sha256=skill.parent_skill_sha256,
            expected_source_version="v001",
            expected_source_round_sha256=skill.source_round_sha256,
            expected_frozen_decision_sha256=skill.frozen_decision_sha256,
            expected_frozen_operational_fingerprint=skill.frozen_operational_fingerprint,
            expected_source_attempt_id="attempt-v001",
            sealed_attempt_ids={"another-attempt"},
        )

    drifted = _skill_payload(decision, source_round_sha256="3" * 64)
    with pytest.raises(ValueError, match="source_round_sha256 binding differs"):
        _parse_skill(drifted, decision)


@pytest.mark.parametrize(
    ("mutation", "match"),
    [
        ({"extra": True}, "fields differ"),
        ({"arm_id": A_FIXED_FEEDBACK}, "belongs only"),
        ({"diagnosis": [] , "preserve": [], "avoid": [], "next_actions": []}, "at least one"),
        ({"diagnosis": ["read /home/ubuntu/private log"]}, "private"),
        ({"diagnosis": ["use hidden-evidence"]}, "hidden evidence"),
        ({"next_actions": ["bad\x00text"]}, "NUL"),
        ({"avoid": ["x" * 513]}, "overlong"),
    ],
)
def test_skill_parser_rejects_schema_and_text_attacks(
    mutation: dict[str, object], match: str
) -> None:
    decision = _decision()
    payload = _skill_payload(decision)
    payload.update(mutation)
    with pytest.raises(ValueError, match=match):
        _parse_skill(payload, decision)


def test_skill_parser_rejects_duplicate_noncanonical_and_nan_json() -> None:
    decision = _decision()
    payload = _skill_payload(decision)
    noncanonical = json.dumps(payload, indent=2).encode()
    with pytest.raises(ValueError, match="not canonical"):
        TaskLocalSkillRecord.from_bytes(
            noncanonical,
            expected_cell_id=str(payload["cell_id"]),
            expected_suite=str(payload["suite"]),
            expected_instance_id=str(payload["instance_id"]),
            expected_version="v002",
            expected_parent_skill_sha256=EMPTY_TASK_LOCAL_SKILL_SHA256,
            expected_source_version="v001",
            expected_source_round_sha256="2" * 64,
            expected_frozen_decision_sha256=decision.sha256,
            expected_frozen_operational_fingerprint=decision.operational_fingerprint,
            expected_source_attempt_id="attempt-v001",
            sealed_attempt_ids={"attempt-v001"},
        )

    canonical = _canonical(payload).decode()
    duplicate = canonical.replace(
        '"schema_version":1', '"schema_version":1,"schema_version":1'
    ).encode()
    with pytest.raises(ValueError, match="repeats field"):
        TaskLocalSkillRecord.from_bytes(
            duplicate,
            expected_cell_id=str(payload["cell_id"]),
            expected_suite=str(payload["suite"]),
            expected_instance_id=str(payload["instance_id"]),
            expected_version="v002",
            expected_parent_skill_sha256=EMPTY_TASK_LOCAL_SKILL_SHA256,
            expected_source_version="v001",
            expected_source_round_sha256="2" * 64,
            expected_frozen_decision_sha256=decision.sha256,
            expected_frozen_operational_fingerprint=decision.operational_fingerprint,
            expected_source_attempt_id="attempt-v001",
            sealed_attempt_ids={"attempt-v001"},
        )

    nan = canonical.replace('"schema_version":1', '"schema_version":NaN').encode()
    with pytest.raises(ValueError, match="forbidden constant"):
        TaskLocalSkillRecord.from_bytes(
            nan,
            expected_cell_id=str(payload["cell_id"]),
            expected_suite=str(payload["suite"]),
            expected_instance_id=str(payload["instance_id"]),
            expected_version="v002",
            expected_parent_skill_sha256=EMPTY_TASK_LOCAL_SKILL_SHA256,
            expected_source_version="v001",
            expected_source_round_sha256="2" * 64,
            expected_frozen_decision_sha256=decision.sha256,
            expected_frozen_operational_fingerprint=decision.operational_fingerprint,
            expected_source_attempt_id="attempt-v001",
            sealed_attempt_ids={"attempt-v001"},
        )


def test_skill_update_receipt_is_canonical_and_rebinds_every_input() -> None:
    decision = _decision()
    skill = _parse_skill(_skill_payload(decision), decision)
    receipt = SkillUpdateReceipt.create(
        skill=skill,
        operation_id="skill-update-v002",
        operation_result_artifact_sha256="3" * 64,
        updater_prompt_sha256="4" * 64,
        public_input_projection_sha256="5" * 64,
        prior_skill_sha256s=(),
    )
    assert receipt.skill_sha256 == skill.sha256
    assert receipt.sha256 == __import__("hashlib").sha256(receipt.canonical_bytes).hexdigest()
    assert (
        SkillUpdateReceipt.from_bytes(
            receipt.canonical_bytes,
            skill=skill,
            prior_skill_sha256s=(),
            expected_operation_id="skill-update-v002",
            expected_operation_result_artifact_sha256="3" * 64,
            expected_updater_prompt_sha256="4" * 64,
            expected_public_input_projection_sha256="5" * 64,
        )
        == receipt
    )

    tampered = receipt.to_dict()
    tampered["source_round_sha256"] = "6" * 64
    with pytest.raises(ValueError, match="binding differs"):
        SkillUpdateReceipt.from_bytes(
            _canonical(tampered),
            skill=skill,
            prior_skill_sha256s=(),
            expected_operation_id="skill-update-v002",
            expected_operation_result_artifact_sha256="3" * 64,
            expected_updater_prompt_sha256="4" * 64,
            expected_public_input_projection_sha256="5" * 64,
        )
    with pytest.raises(ValueError, match="lineage head"):
        SkillUpdateReceipt.create(
            skill=skill,
            operation_id="skill-update-v002",
            operation_result_artifact_sha256="3" * 64,
            updater_prompt_sha256="4" * 64,
            public_input_projection_sha256="5" * 64,
            prior_skill_sha256s=("f" * 64,),
        )

    non_genesis_payload = _skill_payload(decision, parent_skill_sha256="e" * 64)
    non_genesis = TaskLocalSkillRecord.from_bytes(
        _canonical(non_genesis_payload),
        expected_cell_id="suite-a:task-1:seed-1:S",
        expected_suite="suite-a",
        expected_instance_id="task-1",
        expected_version="v002",
        expected_parent_skill_sha256="e" * 64,
        expected_source_version="v001",
        expected_source_round_sha256="2" * 64,
        expected_frozen_decision_sha256=decision.sha256,
        expected_frozen_operational_fingerprint=decision.operational_fingerprint,
        expected_source_attempt_id="attempt-v001",
        sealed_attempt_ids={"attempt-v001"},
    )
    with pytest.raises(ValueError, match="first Skill parent"):
        SkillUpdateReceipt.create(
            skill=non_genesis,
            operation_id="skill-update-v002",
            operation_result_artifact_sha256="3" * 64,
            updater_prompt_sha256="4" * 64,
            public_input_projection_sha256="5" * 64,
            prior_skill_sha256s=(),
        )


def test_skill_and_update_receipt_reject_zero_provenance_hashes() -> None:
    decision = _decision()
    for field in (
        "source_round_sha256",
        "frozen_decision_sha256",
        "frozen_operational_fingerprint",
    ):
        payload = _skill_payload(decision)
        payload[field] = EMPTY_TASK_LOCAL_SKILL_SHA256
        with pytest.raises(ValueError, match="empty"):
            _parse_skill(payload, decision)

    skill = _parse_skill(_skill_payload(decision), decision)
    for field in (
        "operation_result_artifact_sha256",
        "updater_prompt_sha256",
        "public_input_projection_sha256",
    ):
        kwargs = {
            "operation_result_artifact_sha256": "3" * 64,
            "updater_prompt_sha256": "4" * 64,
            "public_input_projection_sha256": "5" * 64,
        }
        kwargs[field] = EMPTY_TASK_LOCAL_SKILL_SHA256
        with pytest.raises(ValueError, match="empty"):
            SkillUpdateReceipt.create(
                skill=skill,
                operation_id="skill-update-v002",
                prior_skill_sha256s=(),
                **kwargs,
            )
