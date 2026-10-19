from __future__ import annotations

from dataclasses import replace
import hashlib
import json
import os
from pathlib import Path

import pytest

from optimization_lab.harness_builder.events import ResourceVector
from optimization_lab.harness_builder.factorial_coverage import (
    AttemptCoverageRow,
    FactorialScoringSlot,
    NativeEvaluationResult,
)
from optimization_lab.harness_builder.factorial_formal_dispatch import (
    FactorialV001FormalCompileOrchestrator,
)
from optimization_lab.harness_builder.factorial_itt import FactorialITTPolicy
from optimization_lab.harness_builder.factorial_policies import (
    EMPTY_TASK_LOCAL_SKILL_SHA256,
    S_REFLECTION_SKILL,
)
from optimization_lab.harness_builder.factorial_score import score_contract_for
from optimization_lab.harness_builder.factorial_skill_dispatch import (
    FactorialSkillAuthority,
    SReflectionSolutionPromptReceipt,
    SReflectionUpdateIntent,
    SourcePublicFeedback,
    accept_skill_update,
    compose_solution_prompt,
    frozen_axis_projection,
)
from optimization_lab.harness_builder.factorial_precheck import FactorialFormalZeroCallPlan
from optimization_lab.harness_builder.factorial_task_authority import (
    FactorialTaskArtifactAuthority,
)
from optimization_lab.harness_builder.operators import HarnessContext, PublicAttempt
from optimization_lab.harness_builder.schema import HarnessDecision


_AGENT = Path(
    os.environ.get(
        "MOSS_TEST_AGENTHPO_CHECKOUT", "/tmp/moss-bench-qual.rYRM8Q/agenthpobench"
    )
)
_GDP = Path(
    os.environ.get(
        "MOSS_TEST_GDPEVO_CHECKOUT", "/tmp/moss-bench-qual.rYRM8Q/gdpevo"
    )
)


def _sha(label: str) -> str:
    return hashlib.sha256(label.encode()).hexdigest()


def _canonical(value: object) -> bytes:
    return (
        json.dumps(value, allow_nan=False, ensure_ascii=False, separators=(",", ":"), sort_keys=True)
        + "\n"
    ).encode()


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
        "kernel_directive": "Use only public feedback.",
    }
    payload.update(overrides)
    return HarnessDecision.from_dict(payload)


def _slot(version: int, *, arm: str | None = None, key: str | None = None) -> FactorialScoringSlot:
    key = key or _sha("task-seed")
    contract = score_contract_for("agenthpobench")
    policy = FactorialITTPolicy.from_verified_manifest(benchmark_id="agenthpobench")
    if version == 1:
        return FactorialScoringSlot(
            factorial_plan_sha256=_sha("plan"),
            task_authority_bundle_sha256=_sha("bundle"),
            factorial_contract_sha256=policy.factorial_contract_sha256,
            task_seed_key_sha256=key,
            benchmark_id="agenthpobench",
            instance_id="task-1",
            seed=2026081201,
            arm_id="SHARED_V001",
            arm_variant_sha256=_sha("shared-variant"),
            arm_update_policy="shared_v001_common_trunk_v1",
            version="v001",
            shared_v001=True,
            cell_id=f"factorial-v001-cell:{key}",
            attempt_id=f"factorial-attempt:{key}:shared-v001",
            update_operation_id=f"factorial-v001:{key}:builder",
            solution_operation_id=f"factorial-v001:{key}:solution",
            evaluator_operation_id=f"factorial-v001:{key}:evaluator",
            update_operation_expected=True,
            score_contract_sha256=contract.sha256,
            itt_policy_sha256=policy.sha256,
        )
    arm = arm or S_REFLECTION_SKILL
    version_id = f"v{version:03d}"
    prefix = f"factorial-round:{key}:{arm}:{version_id}"
    return FactorialScoringSlot(
        factorial_plan_sha256=_sha("plan"),
        task_authority_bundle_sha256=_sha("bundle"),
        factorial_contract_sha256=policy.factorial_contract_sha256,
        task_seed_key_sha256=key,
        benchmark_id="agenthpobench",
        instance_id="task-1",
        seed=2026081201,
        arm_id=arm,
        arm_variant_sha256=_sha("variant:" + arm),
        arm_update_policy="reflection_skill_only_v1",
        version=version_id,
        shared_v001=False,
        cell_id=f"factorial-cell:{key}:{arm}",
        attempt_id=prefix + ":attempt",
        update_operation_id=prefix + ":update",
        solution_operation_id=prefix + ":solution",
        evaluator_operation_id=prefix + ":evaluator",
        update_operation_expected=True,
        score_contract_sha256=contract.sha256,
        itt_policy_sha256=policy.sha256,
    )


def _feedback(source: FactorialScoringSlot, **overrides: object) -> SourcePublicFeedback:
    values: dict[str, object] = {
        "source_slot_sha256": source.sha256,
        "source_attempt_id": source.attempt_id,
        "source_terminal_receipt_sha256": _sha("terminal:" + source.version),
        "candidate_artifact_sha256": _sha("candidate:" + source.version),
        "outcome": "VALID",
        "valid": True,
        "correct": True,
        "raw_score": 0.25,
        "public_reason_code": "NONE",
        "structural_signature": "valid-query-sequence",
        "public_summary": ("The public score improved after narrowing the search.",),
    }
    values.update(overrides)
    return SourcePublicFeedback(**values)


def _intent(target: FactorialScoringSlot, source: FactorialScoringSlot, **overrides: object):
    feedback = overrides.pop("public_feedback", _feedback(source))
    return SReflectionUpdateIntent.create(
        target_slot=target,
        source_slot=source,
        exact_matrix_sha256=_sha("matrix"),
        expected_factorial_plan_sha256=_sha("plan"),
        expected_task_authority_bundle_sha256=_sha("bundle"),
        source_terminal_receipt_sha256=feedback.source_terminal_receipt_sha256,
        public_feedback=feedback,
        frozen_decision=_decision(),
        **overrides,
    ), feedback


def _skill_bytes(intent: SReflectionUpdateIntent, evidence: list[str] | None = None) -> bytes:
    return _canonical(
        {
            "schema_version": 1,
            "record_kind": "task_local_reflection_skill_v1",
            "cell_id": intent.cell_id,
            "suite": intent.benchmark_id,
            "instance_id": intent.instance_id,
            "arm_id": S_REFLECTION_SKILL,
            "version": intent.version,
            "parent_skill_sha256": intent.parent_skill_sha256,
            "source_round_sha256": intent.public_input_projection_sha256,
            "frozen_decision_sha256": intent.frozen_decision_sha256,
            "frozen_operational_fingerprint": intent.frozen_operational_fingerprint,
            "evidence_attempt_ids": evidence or [intent.source_attempt_id],
            "diagnosis": ["The public score indicates excessive exploration."],
            "preserve": ["Keep the valid public request contract."],
            "avoid": ["Avoid repeating the same public query."],
            "next_actions": ["Search around the public incumbent."],
        }
    )


def test_v002_intent_is_exact_slot_derived_frozen_and_zero_authority() -> None:
    source, target = _slot(1), _slot(2)
    intent, feedback = _intent(target, source)
    assert intent.target_slot_sha256 == target.sha256
    assert intent.source_slot_sha256 == source.sha256
    assert intent.update_operation_id == target.update_operation_id
    assert intent.parent_skill_sha256 == EMPTY_TASK_LOCAL_SKILL_SHA256
    assert intent.parent_update_receipt_sha256 == EMPTY_TASK_LOCAL_SKILL_SHA256
    assert intent.frozen_decision_sha256 == _decision().sha256
    assert intent.frozen_axis_projection_sha256 == _sha_json(frozen_axis_projection(_decision()))
    assert intent.to_dict()["execution_authority"] == "NOT_GRANTED"
    assert set(intent.to_dict()["execution_entitlement"].values()) == {0}
    assert intent.public_input_projection_sha256 == feedback.sha256
    assert SReflectionUpdateIntent.from_bytes(
        intent.canonical_bytes, expected_sha256=intent.sha256
    ) == intent


def _sha_json(value: object) -> str:
    return hashlib.sha256(_canonical(value)).hexdigest()


def test_intent_rejects_nonadjacent_cross_task_and_caller_rebinding() -> None:
    source, target = _slot(1), _slot(2)
    with pytest.raises(ValueError, match="adjacent"):
        _intent(_slot(3), source)
    with pytest.raises(ValueError, match="crosses"):
        _intent(_slot(2, key=_sha("other-key")), source)
    with pytest.raises(ValueError, match="plan/authority"):
        SReflectionUpdateIntent.create(
            target_slot=target,
            source_slot=source,
            exact_matrix_sha256=_sha("matrix"),
            expected_factorial_plan_sha256=_sha("forged-plan"),
            expected_task_authority_bundle_sha256=_sha("bundle"),
            source_terminal_receipt_sha256=_sha("terminal:v001"),
            public_feedback=_feedback(source),
            frozen_decision=_decision(),
        )
    with pytest.raises(ValueError, match="public feedback/source"):
        _intent(target, source, public_feedback=replace(_feedback(source), source_attempt_id="forged"))


def test_public_projection_is_strict_canonical_bounded_and_private_safe() -> None:
    feedback = _feedback(_slot(1))
    assert SourcePublicFeedback.from_bytes(
        feedback.canonical_bytes, expected_sha256=feedback.sha256
    ) == feedback
    payload = feedback.to_dict()
    payload["private_evaluator_log"] = "not allowed"
    with pytest.raises(ValueError, match="fields differ"):
        SourcePublicFeedback.from_bytes(_canonical(payload), expected_sha256=_sha_json(payload))
    with pytest.raises(ValueError, match="private or unsafe"):
        _feedback(_slot(1), public_summary=("Read /home/secret/gold answer",))
    with pytest.raises(ValueError, match="finite"):
        _feedback(_slot(1), raw_score=float("nan"))


def test_accept_skill_requires_exact_single_source_and_prompt_hides_provenance() -> None:
    source, target = _slot(1), _slot(2)
    intent, _ = _intent(target, source)
    skill, update = accept_skill_update(
        intent=intent,
        raw_skill=_skill_bytes(intent),
        operation_result_artifact_sha256=_sha("raw-result"),
    )
    assert update.operation_id == target.update_operation_id
    prompt = compose_solution_prompt("BASE TRUSTED PROMPT", skill)
    assert skill.diagnosis[0] in prompt
    assert skill.source_round_sha256 not in prompt
    assert skill.evidence_attempt_ids[0] not in prompt
    with pytest.raises(ValueError, match="unsealed|exactly the adjacent"):
        accept_skill_update(
            intent=intent,
            raw_skill=_skill_bytes(intent, [source.attempt_id, "other-sealed-attempt"]),
            operation_result_artifact_sha256=_sha("raw-result"),
        )


def test_v003_requires_consecutive_same_cell_parent_skill_and_receipt() -> None:
    v001, v002, v003 = _slot(1), _slot(2), _slot(3)
    first_intent, _ = _intent(v002, v001)
    skill2, receipt2 = accept_skill_update(
        intent=first_intent,
        raw_skill=_skill_bytes(first_intent),
        operation_result_artifact_sha256=_sha("raw-v002"),
    )
    intent3, _ = _intent(
        v003,
        v002,
        parent_skill=skill2,
        parent_update_receipt=receipt2,
    )
    assert intent3.parent_skill_sha256 == skill2.sha256
    assert intent3.parent_update_receipt_sha256 == receipt2.sha256
    skill3, receipt3 = accept_skill_update(
        intent=intent3,
        raw_skill=_skill_bytes(intent3),
        operation_result_artifact_sha256=_sha("raw-v003"),
        prior_skills=(skill2,),
    )
    assert receipt3.parent_skill_sha256 == skill2.sha256
    with pytest.raises(ValueError, match="immediately prior typed parent"):
        _intent(v003, v002)
    with pytest.raises(ValueError, match="lineage"):
        accept_skill_update(
            intent=intent3,
            raw_skill=_skill_bytes(intent3),
            operation_result_artifact_sha256=_sha("raw-v003-again"),
            prior_skills=(),
        )


@pytest.fixture(scope="module")
def exact_authority():
    if not _AGENT.is_dir() or not _GDP.is_dir():
        pytest.skip("pinned benchmark checkouts unavailable")
    task_authority = FactorialTaskArtifactAuthority(
        agenthpo_checkout=_AGENT, gdpevo_checkout=_GDP
    )
    bundle = task_authority.rederive_exact_bundle()
    plan = FactorialFormalZeroCallPlan.from_authority_bundle(
        bundle, task_authority=task_authority
    )
    authority = FactorialSkillAuthority(
        task_authority=task_authority,
        task_authority_bundle=bundle,
        plan=plan,
    )
    compiler = FactorialV001FormalCompileOrchestrator(
        task_authority=task_authority,
        task_authority_bundle=bundle,
        plan=plan,
    )
    return task_authority, plan, authority, compiler


def _typed_row(
    *, slot: FactorialScoringSlot, matrix_sha256: str
) -> AttemptCoverageRow:
    result = NativeEvaluationResult(
        benchmark_id=slot.benchmark_id,
        valid=True,
        raw_score=0.5,
        invalid_reason=None,
        evidence_artifact_sha256=_sha("typed-source-evidence"),
        actual_usage=ResourceVector(evaluator_transactions=1),
    )
    score_receipt = result.to_score_receipt(evaluation_id=slot.attempt_id)
    policy = FactorialITTPolicy.from_verified_manifest(
        benchmark_id=slot.benchmark_id
    )
    from optimization_lab.harness_builder.factorial_itt import (
        FactorialITTScore,
        VerifiedITTReportRow,
    )

    itt_score = FactorialITTScore.from_score_receipt(
        policy=policy, score_receipt=score_receipt
    )
    report = VerifiedITTReportRow.seal(
        policy=policy, score_receipt=score_receipt, itt_score=itt_score
    )
    return AttemptCoverageRow.from_typed_score_chain(
        matrix_sha256=matrix_sha256,
        slot=slot,
        policy=policy,
        score_receipt=score_receipt,
        itt_score=itt_score,
        report_row=report,
    )


@pytest.mark.parametrize("suite", ("agenthpobench", "gdpevo"))
def test_pinned_authority_replays_matrix_v001_and_frozen_solution_prompt(
    exact_authority, suite: str
) -> None:
    task_authority, plan, authority, compiler = exact_authority
    key = next(item.key for item in plan.schedules if item.key.suite == suite)
    target, source = authority._slots(key=key, version="v002")
    frozen = HarnessDecision.from_dict(
        {
            "schema_version": 1,
            "rule_id": "contract_compatibility",
            "role_graph": ["task_analyst", "generator", "verifier"],
            "memory_views": ["current"],
            "tools": ["task_semantics"],
            "parent_strategy": "reference",
            "workflow": ["analyze", "generate", "verify_contract"],
            "scheduler_mode": "single_candidate",
            "recovery_mode": "repair_then_reset",
            "kernel_directive": "Respect the public artifact contract.",
        }
    )
    v001_result = compiler.compile_shared_v001(key=key, decision=frozen)
    intent, feedback = authority.create_intent(
        key=key,
        version="v002",
        source_coverage_row=_typed_row(
            slot=source, matrix_sha256=authority.matrix.sha256
        ),
        source_terminal_receipt_sha256=_sha("typed-source-terminal"),
        candidate_artifact_sha256=_sha("typed-source-candidate"),
        correct=True,
        structural_signature="typed-public-shape",
        public_summary=("The typed public score is valid.",),
        frozen_decision=frozen,
        v001_compile_result=v001_result,
    )
    assert intent.exact_matrix_sha256 == authority.matrix.sha256
    assert feedback.source_slot_sha256 == source.sha256
    skill, update = accept_skill_update(
        intent=intent,
        raw_skill=_skill_bytes(intent),
        operation_result_artifact_sha256=_sha("typed-update-result"),
    )
    context0 = task_authority.derived_contexts()[(suite, key.instance_id)]
    context = HarnessContext(
        **{
            **context0.__dict__,
            "round_index": 2,
            "attempts": (
                PublicAttempt(
                    attempt_id="v001",
                    artifact_sha256=_sha("public-attempt"),
                    artifact_text="public candidate",
                    correct=True,
                    score=1.0,
                    outcome="valid",
                    structural_signature="typed-public-shape",
                    public_summary="valid public v001",
                ),
            ),
        }
    )
    v001_receipt = dict(v001_result.arm_compile_receipts)[S_REFLECTION_SKILL]
    base_prompt, trusted_target_receipt = authority.verify_frozen_compile_for_solution(
        intent=intent,
        context=context,
        frozen_decision=frozen,
        v001_compile_result=v001_result,
        prior_compile_receipts=(v001_receipt,),
    )
    receipt = SReflectionSolutionPromptReceipt.create(
        intent=intent,
        skill=skill,
        skill_update_receipt=update,
        authority=authority,
        context=context,
        frozen_decision=frozen,
        v001_compile_result=v001_result,
        prior_compile_receipts=(v001_receipt,),
        base_solution_prompt=base_prompt,
    )
    assert receipt.trusted_compile_receipt_sha256 == trusted_target_receipt.sha256
    assert trusted_target_receipt.version == "v002"
    assert not any(trusted_target_receipt.change_map.values())
    final_prompt = compose_solution_prompt(base_prompt, skill)
    assert receipt.final_solution_prompt_sha256 == hashlib.sha256(
        final_prompt.encode()
    ).hexdigest()
    assert SReflectionSolutionPromptReceipt.from_bytes(
        receipt.canonical_bytes, expected_sha256=receipt.sha256
    ) == receipt

    with pytest.raises(ValueError, match="outside pinned source authority"):
        authority.create_intent(
            key=replace(key, seed=7),
            version="v002",
            source_coverage_row=_typed_row(
                slot=source, matrix_sha256=authority.matrix.sha256
            ),
            source_terminal_receipt_sha256=_sha("typed-source-terminal"),
            candidate_artifact_sha256=_sha("typed-source-candidate"),
            correct=True,
            structural_signature="typed-public-shape",
            public_summary=("The typed public score is valid.",),
            frozen_decision=frozen,
            v001_compile_result=v001_result,
        )
