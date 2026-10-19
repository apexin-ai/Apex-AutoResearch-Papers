from __future__ import annotations

from dataclasses import asdict, replace
import hashlib
import json
import os
from pathlib import Path

import pytest

from optimization_lab.harness_builder.compile_receipts import HarnessCompileReceipt
from optimization_lab.harness_builder.events import ResourceVector
from optimization_lab.harness_builder.factorial_coverage import (
    AttemptCoverageRow,
    NativeEvaluationResult,
)
from optimization_lab.harness_builder.factorial_formal_dispatch import (
    FactorialV001FormalCompileOrchestrator,
)
from optimization_lab.harness_builder.factorial_itt import (
    FactorialITTPolicy,
    FactorialITTScore,
    VerifiedITTReportRow,
)
from optimization_lab.harness_builder.factorial_post_v001_authority import (
    FactorialPostV001Authority,
    FactorialPostV001AuthorityError,
    PostV001CompileValidationReceipt,
    PostV001PlannerDecisionReceipt,
    PostV001RoundTerminalReceipt,
    PostV001TransitionIntent,
)
from optimization_lab.harness_builder.factorial_precheck import FactorialFormalZeroCallPlan
from optimization_lab.harness_builder.factorial_task_authority import (
    FactorialTaskArtifactAuthority,
)
from optimization_lab.harness_builder.factorial_trunk import V001ArmForkReceipt
from optimization_lab.harness_builder.operators import (
    HarnessContext,
    PublicAttempt,
    TrustedOperatorRegistry,
)
from optimization_lab.harness_builder.schema import BuilderVariant, HarnessDecision


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
_AXES = (
    "role_graph",
    "memory_views",
    "tools",
    "parent_strategy",
    "workflow",
    "scheduler_mode",
    "recovery_mode",
)


def _v1() -> HarnessDecision:
    return HarnessDecision.from_dict(
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


def _v2(**updates: object) -> HarnessDecision:
    payload: dict[str, object] = {
        "schema_version": 1,
        "rule_id": "discipline",
        "role_graph": ["performance_analyst", "critic", "generator", "verifier"],
        "memory_views": ["failures", "best"],
        "tools": ["score_history", "static_structure"],
        "parent_strategy": "incumbent",
        "workflow": ["inspect", "criticize", "generate", "verify_contract"],
        "scheduler_mode": "repair_first",
        "recovery_mode": "preserve_failure",
        "kernel_directive": "Rebuild every trusted Harness axis.",
    }
    payload.update(updates)
    return HarnessDecision.from_dict(payload)


def _result(slot: object, decision: HarnessDecision) -> bytes:
    payload = {
        "schema_version": 1,
        "operation_id": slot.update_operation_id,
        "cell_id": slot.cell_id,
        "operation_kind": "planner_call",
        "prompt_sha256": "9" * 64,
        "model": "fixture-model",
        "output_mode": "plain_text",
        "raw_response": json.dumps(asdict(decision), separators=(",", ":")),
        "api_cost_usd": 0.0,
        "provider": "fixture",
        "usage": {"input_tokens": 1, "output_tokens": 1},
        "audit_log_name": "",
    }
    return (json.dumps(payload, sort_keys=True, separators=(",", ":")) + "\n").encode()


def _coverage_row(
    *, slot: object, matrix_sha256: str, valid: bool, reason: str | None = None
) -> AttemptCoverageRow:
    result = NativeEvaluationResult(
        benchmark_id=slot.benchmark_id,
        valid=valid,
        raw_score=0.5 if valid else None,
        invalid_reason=None if valid else reason,
        evidence_artifact_sha256="d" * 64,
        actual_usage=ResourceVector(evaluator_transactions=1),
    )
    score_receipt = result.to_score_receipt(evaluation_id=slot.attempt_id)
    policy = FactorialITTPolicy.from_verified_manifest(
        benchmark_id=slot.benchmark_id
    )
    itt_score = FactorialITTScore.from_score_receipt(
        policy=policy, score_receipt=score_receipt
    )
    report_row = VerifiedITTReportRow.seal(
        policy=policy, score_receipt=score_receipt, itt_score=itt_score
    )
    return AttemptCoverageRow.from_typed_score_chain(
        matrix_sha256=matrix_sha256,
        slot=slot,
        policy=policy,
        score_receipt=score_receipt,
        itt_score=itt_score,
        report_row=report_row,
    )


@pytest.fixture(scope="module")
def exact():
    if not _AGENT.is_dir() or not _GDP.is_dir():
        pytest.skip("pinned benchmark checkouts unavailable")
    task_authority = FactorialTaskArtifactAuthority(
        agenthpo_checkout=_AGENT, gdpevo_checkout=_GDP
    )
    bundle = task_authority.rederive_exact_bundle()
    plan = FactorialFormalZeroCallPlan.from_authority_bundle(
        bundle, task_authority=task_authority
    )
    authority = FactorialPostV001Authority(
        task_authority=task_authority,
        task_authority_bundle=bundle,
        plan=plan,
    )
    v1_orchestrator = FactorialV001FormalCompileOrchestrator(
        task_authority=task_authority,
        task_authority_bundle=bundle,
        plan=plan,
    )
    return task_authority, bundle, plan, authority, v1_orchestrator


def _case(exact, suite: str):
    task_authority, _bundle, plan, authority, v1_orchestrator = exact
    key = next(item.key for item in plan.schedules if item.key.suite == suite)
    slot = next(
        item
        for item in authority.matrix.slots
        if item.task_seed_key_sha256 == key.sha256
        and item.arm_id == "B-frozen-wide"
        and item.version == "v002"
    )
    v1_result = v1_orchestrator.compile_shared_v001(key=key, decision=_v1())
    v1_receipt = dict(v1_result.arm_compile_receipts)["B-frozen-wide"]
    fork = V001ArmForkReceipt(
        task_seed_key_sha256=key.sha256,
        trunk_receipt_sha256="1" * 64,
        arm_id="B-frozen-wide",
        arm_cell_id=slot.cell_id,
        arm_variant_sha256=dict(plan.arm_variant_sha256s)["B-frozen-wide"],
        arm_contract_sha256=plan.factorial_contract_sha256,
        arm_compile_receipt_sha256=v1_receipt.sha256,
        trunk_status="SUCCESS",
        version="v001",
        shared_decision_sha256=_v1().sha256,
        shared_operational_fingerprint=_v1().operational_fingerprint,
        shared_compiled_harness_semantic_sha256="2" * 64,
        shared_solution_prompt_sha256="3" * 64,
        shared_solution_artifact_sha256="4" * 64,
        shared_attempt_artifact_sha256="5" * 64,
        shared_evaluation_artifact_sha256="6" * 64,
    )
    context0 = task_authority.derived_contexts()[(suite, key.instance_id)]
    context = HarnessContext(
        **{
            **context0.__dict__,
            "round_index": 2,
            "attempts": (
                PublicAttempt(
                    attempt_id="v001",
                    artifact_sha256="a" * 64,
                    artifact_text="public candidate",
                    correct=True,
                    score=1.0,
                    outcome="valid",
                    structural_signature="family-a",
                    public_summary="valid v001",
                ),
            ),
        }
    )
    result = _result(slot, _v2())
    planner, parsed = PostV001PlannerDecisionReceipt.create(
        matrix=authority.matrix,
        slot=slot,
        operation_record_sha256="7" * 64,
        operation_result_artifact=result,
        context_binding_sha256=TrustedOperatorRegistry.context_binding_sha256(context),
    )
    intent, decision = authority.create_intent(
        key=key,
        arm_id="B-frozen-wide",
        version="v002",
        planner_receipt=planner,
        planner_operation_result_artifact=result,
        v001_fork=fork,
        previous_terminal=None,
        prior_compile_receipts=(v1_receipt,),
        prior_decisions=(_v1(),),
    )
    assert parsed == decision == _v2()
    variant = BuilderVariant(
        variant_id="B-frozen-wide",
        description="fixture",
        freeze_after_initial=False,
        continual_update=False,
        rule_registry_sha256=v1_orchestrator.runtime_contract.rule_registry_sha256,
        allowed_rule_ids=v1_orchestrator.rule_registry.executable_rule_ids,
        experience_sources=(),
        excluded_task_ids=(),
        adaptation_policy="wide_all_fields_recompile_v1",
    )
    compiled = v1_orchestrator.operator_registry.compile(
        decision,
        variant=variant,
        context=context,
        previous_decision=_v1(),
        prior_operational_fingerprints=(_v1().operational_fingerprint,),
    )
    receipt = HarnessCompileReceipt.create(
        cell_id=slot.cell_id,
        suite=suite,
        instance_id=key.instance_id,
        variant_id="B-frozen-wide",
        version="v002",
        adaptation_policy="wide_all_fields_recompile_v1",
        previous_receipt_sha256=v1_receipt.sha256,
        previous_decision_sha256=_v1().sha256,
        compiled=compiled,
        decision=decision,
        previous_decision=_v1(),
        prior_operational_fingerprints=(_v1().operational_fingerprint,),
    )
    return (
        key,
        slot,
        planner,
        result,
        intent,
        decision,
        v1_receipt,
        fork,
        receipt,
        context,
    )


@pytest.mark.parametrize("suite", ("agenthpobench", "gdpevo"))
def test_exact_two_benchmark_wide_v002_authority(exact, suite: str) -> None:
    *_, authority, _v1_orchestrator = exact
    (
        _key,
        slot,
        planner,
        result,
        intent,
        decision,
        v1_receipt,
        _fork,
        receipt,
        context,
    ) = _case(exact, suite)
    validation = authority.validate_compile(
        intent=intent,
        decision=decision,
        compile_receipt=receipt,
        prior_compile_receipts=(v1_receipt,),
        prior_decisions=(_v1(),),
        context=context,
    )
    assert validation.execution_authority == "NOT_GRANTED"
    assert validation.model_call_entitlement == 0
    assert all(receipt.change_map.values())
    assert all(
        receipt.axis_configuration_sha256s[axis]
        != v1_receipt.axis_configuration_sha256s[axis]
        for axis in _AXES
    )
    for item in (planner, intent, validation):
        assert type(item).from_bytes(item.canonical_bytes, expected_sha256=item.sha256) == item
    with pytest.raises(FactorialPostV001AuthorityError, match="replay differs"):
        planner.verify(
            matrix=authority.matrix,
            slot=slot,
            operation_result_artifact=_result(slot, _v2(kernel_directive="tampered")),
        )


@pytest.mark.parametrize("axis", _AXES)
def test_wide_validator_rejects_each_unchanged_axis(exact, axis: str) -> None:
    *_, authority, _ = exact
    (
        _key,
        _slot,
        _planner,
        _result_bytes,
        intent,
        _decision,
        v1_receipt,
        _fork,
        receipt,
        context,
    ) = _case(exact, "agenthpobench")
    forged = object.__new__(HarnessCompileReceipt)
    for name in receipt.__dataclass_fields__:
        object.__setattr__(forged, name, getattr(receipt, name))
    object.__setattr__(
        forged, "change_map", {**receipt.change_map, axis: False}
    )
    with pytest.raises(
        FactorialPostV001AuthorityError,
        match="trusted compile receipt binding differs|seven-axis",
    ):
        authority.validate_compile(
            intent=intent,
            decision=_v2(),
            compile_receipt=forged,
            prior_compile_receipts=(v1_receipt,),
            prior_decisions=(_v1(),),
            context=context,
        )


def test_cross_binding_missing_parent_and_out_of_range_fail(exact) -> None:
    *_, authority, _ = exact
    (
        key,
        _slot,
        planner,
        result,
        _intent,
        _decision,
        v1_receipt,
        fork,
        _receipt,
        _context,
    ) = _case(exact, "gdpevo")
    other_key = next(
        item.key
        for item in exact[2].schedules
        if item.key.suite == "gdpevo" and item.key.sha256 != key.sha256
    )
    with pytest.raises(FactorialPostV001AuthorityError, match="key is outside|binding"):
        authority.create_intent(
            key=other_key,
            arm_id="B-frozen-wide",
            version="v002",
            planner_receipt=planner,
            planner_operation_result_artifact=result,
            v001_fork=fork,
            previous_terminal=None,
            prior_compile_receipts=(v1_receipt,),
            prior_decisions=(_v1(),),
        )
    with pytest.raises(FactorialPostV001AuthorityError, match="exact formal"):
        authority.create_intent(
            key=key,
            arm_id="B-frozen-wide",
            version="v004",
            planner_receipt=planner,
            planner_operation_result_artifact=result,
            v001_fork=None,
            previous_terminal=None,
            prior_compile_receipts=(v1_receipt,),
            prior_decisions=(_v1(),),
        )


def test_terminal_receipt_is_zero_authority_and_canonical(exact) -> None:
    *_, authority, _ = exact
    (
        _key,
        _slot,
        _planner,
        _raw,
        intent,
        decision,
        v1_receipt,
        _fork,
        receipt,
        context,
    ) = _case(exact, "agenthpobench")
    validation = authority.validate_compile(
        intent=intent,
        decision=decision,
        compile_receipt=receipt,
        prior_compile_receipts=(v1_receipt,),
        prior_decisions=(_v1(),),
        context=context,
    )
    terminal = PostV001RoundTerminalReceipt.accepted(
        intent=intent,
        validation=validation,
        compile_receipt=receipt,
        slot=_slot,
        coverage_row=_coverage_row(
            slot=_slot, matrix_sha256=authority.matrix.sha256, valid=True
        ),
    )
    assert terminal.execution_authority == "NOT_GRANTED"
    assert PostV001RoundTerminalReceipt.from_bytes(
        terminal.canonical_bytes, expected_sha256=terminal.sha256
    ) == terminal
    tampered = json.loads(intent.canonical_bytes)
    tampered["seed"] += 1
    encoded = (json.dumps(tampered, sort_keys=True, separators=(",", ":")) + "\n").encode()
    forged = PostV001TransitionIntent.from_bytes(
        encoded, expected_sha256=hashlib.sha256(encoded).hexdigest()
    )
    with pytest.raises(FactorialPostV001AuthorityError, match="exact-slot"):
        authority.validate_compile(
            intent=forged,
            decision=decision,
            compile_receipt=receipt,
            prior_compile_receipts=(v1_receipt,),
            prior_decisions=(_v1(),),
            context=context,
        )


def test_rejected_v002_uses_typed_floor_and_v003_keeps_v001_parent(exact) -> None:
    *_, authority, _ = exact
    (
        key,
        slot2,
        planner2,
        result2,
        intent2,
        _decision2,
        v1_receipt,
        fork,
        _,
        _context,
    ) = _case(exact, "gdpevo")
    reason = "planner_contract_rejected"
    rejected_row = _coverage_row(
        slot=slot2,
        matrix_sha256=authority.matrix.sha256,
        valid=False,
        reason=reason,
    )
    terminal2 = PostV001RoundTerminalReceipt.rejected(
        intent=intent2,
        slot=slot2,
        coverage_row=rejected_row,
        reason_code=reason,
    )
    assert terminal2.compile_validation_receipt_sha256 == "0" * 64
    assert terminal2.lineage_head_compile_receipt_sha256 == v1_receipt.sha256
    assert terminal2.accepted_operational_fingerprints == (
        _v1().operational_fingerprint,
    )

    slot3 = next(
        item
        for item in authority.matrix.slots
        if item.task_seed_key_sha256 == key.sha256
        and item.arm_id == "B-frozen-wide"
        and item.version == "v003"
    )
    decision3 = _v2(
        role_graph=("performance_analyst", "critic", "generator", "verifier", "reviewer"),
        kernel_directive="Rebuild every trusted Harness axis after the rejected round.",
    )
    result3 = _result(slot3, decision3)
    planner3, _ = PostV001PlannerDecisionReceipt.create(
        matrix=authority.matrix,
        slot=slot3,
        operation_record_sha256="e" * 64,
        operation_result_artifact=result3,
        context_binding_sha256=planner2.context_binding_sha256,
    )
    intent3, parsed3 = authority.create_intent(
        key=key,
        arm_id="B-frozen-wide",
        version="v003",
        planner_receipt=planner3,
        planner_operation_result_artifact=result3,
        v001_fork=None,
        previous_terminal=terminal2,
        prior_compile_receipts=(v1_receipt,),
        prior_decisions=(_v1(),),
    )
    assert parsed3 == decision3
    assert intent3.previous_physical_terminal_sha256 == terminal2.sha256
    assert intent3.previous_accepted_compile_receipt_sha256 == v1_receipt.sha256

    with pytest.raises(FactorialPostV001AuthorityError, match="ITT-floor"):
        PostV001RoundTerminalReceipt.rejected(
            intent=intent2,
            slot=slot2,
            coverage_row=_coverage_row(
                slot=slot2,
                matrix_sha256=authority.matrix.sha256,
                valid=False,
                reason="different_reason",
            ),
            reason_code=reason,
        )
