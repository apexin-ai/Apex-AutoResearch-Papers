from __future__ import annotations

from dataclasses import replace
import hashlib
import os
from pathlib import Path

import pytest

from optimization_lab.harness_builder.events import (
    JournalIntegrityError,
    OperationJournal,
    ResourceCaps,
    ResourceGovernor,
    ResourceVector,
)
from optimization_lab.harness_builder.factorial_coverage import (
    AttemptCoverageRow,
    ExactFactorialAttemptMatrix,
    FactorialCoverageError,
    FactorialCoverageVerifier,
    NativeEvaluationResult,
    TYPED_SCORE_UNBOUND,
    UNEXECUTED,
    canonical_operation_record_sha256_from_journal,
)
from optimization_lab.harness_builder.factorial_itt import (
    FactorialITTPolicy,
    FactorialITTScore,
    VerifiedITTReportRow,
)
from optimization_lab.harness_builder.factorial_task_authority import (
    FactorialTaskArtifactAuthority,
)


_AGENT_ROOT = Path(
    os.environ.get(
        "MOSS_TEST_AGENTHPO_CHECKOUT",
        "/tmp/moss-bench-qual.rYRM8Q/agenthpobench",
    )
)
_GDPEVO_ROOT = Path(
    os.environ.get(
        "MOSS_TEST_GDPEVO_CHECKOUT",
        "/tmp/moss-bench-qual.rYRM8Q/gdpevo",
    )
)


def _sha(label: str) -> str:
    return hashlib.sha256(label.encode()).hexdigest()


@pytest.fixture(scope="module")
def exact_inputs():
    if not _AGENT_ROOT.is_dir() or not _GDPEVO_ROOT.is_dir():
        pytest.skip("pinned benchmark qualification checkouts are unavailable")
    authority = FactorialTaskArtifactAuthority(
        agenthpo_checkout=_AGENT_ROOT,
        gdpevo_checkout=_GDPEVO_ROOT,
    )
    bundle = authority.rederive_exact_bundle()
    plan = authority.build_formal_zero_call_plan(authority.derived_contexts())
    matrix = ExactFactorialAttemptMatrix.from_verified_sources(
        plan=plan, bundle=bundle, task_authority=authority
    )
    return authority, bundle, plan, matrix


def test_exact_matrix_mechanically_expands_1566_scoring_slots(exact_inputs) -> None:
    _authority, bundle, plan, matrix = exact_inputs
    assert matrix.execution_authority == "NOT_GRANTED"
    assert matrix.model_call_entitlement == 0
    assert matrix.evaluator_transaction_entitlement == 0
    assert matrix.factorial_plan_sha256 == plan.sha256
    assert matrix.task_authority_bundle_sha256 == bundle.sha256
    assert matrix.counts == {
        "agenthpobench_post_v001": 720,
        "gdpevo_post_v001": 720,
        "post_v001": 1440,
        "shared_v001": 126,
        "total": 1566,
    }
    assert len({slot.attempt_id for slot in matrix.slots}) == 1566
    assert len({slot.sha256 for slot in matrix.slots}) == 1566

    shared = matrix.slots[0]
    assert shared.shared_v001 is True
    assert shared.arm_id == "SHARED_V001"
    assert shared.version == "v001"
    assert shared.update_operation_id.endswith(":builder")
    assert shared.solution_operation_id.endswith(":solution")
    assert shared.evaluator_operation_id.endswith(":evaluator")

    post = matrix.slots[1]
    assert post.shared_v001 is False
    assert post.version == "v002"
    assert post.arm_id in {
        "A-fixed-feedback",
        "S-reflection-skill",
        "B-targeted",
        "B-frozen-wide",
    }
    assert post.cell_id.endswith(":" + post.arm_id)
    assert post.update_operation_expected == (post.arm_id != "A-fixed-feedback")


def test_self_consistent_rebind_of_slot_or_plan_is_rejected(exact_inputs) -> None:
    authority, bundle, plan, matrix = exact_inputs
    with pytest.raises(FactorialCoverageError, match="source/plan replay"):
        ExactFactorialAttemptMatrix.from_verified_sources(
            plan=replace(plan, task_authority_bundle_sha256="a" * 64),
            bundle=bundle,
            task_authority=authority,
        )

    slot = matrix.slots[7]
    with pytest.raises(FactorialCoverageError, match="identity differs"):
        replace(slot, attempt_id=slot.attempt_id + ":rebound")


@pytest.mark.parametrize(
    ("benchmark_id", "raw_score"),
    [("agenthpobench", -0.75), ("gdpevo", 0.0)],
)
def test_native_evaluation_accepts_legal_negative_and_zero_scores(
    benchmark_id: str, raw_score: float
) -> None:
    result = NativeEvaluationResult(
        benchmark_id=benchmark_id,
        valid=True,
        raw_score=raw_score,
        invalid_reason=None,
        evidence_artifact_sha256=_sha(f"evidence:{benchmark_id}"),
        actual_usage=ResourceVector(evaluator_transactions=1),
    )
    receipt = result.to_score_receipt(evaluation_id=f"{benchmark_id}:attempt:v002")
    assert receipt.valid is True
    assert receipt.raw_score == raw_score


def test_invalid_native_evaluation_maps_to_benchmark_floor(exact_inputs) -> None:
    _authority, _bundle, _plan, matrix = exact_inputs
    slot = next(
        item
        for item in matrix.slots
        if item.benchmark_id == "agenthpobench" and not item.shared_v001
    )
    result = NativeEvaluationResult(
        benchmark_id=slot.benchmark_id,
        valid=False,
        raw_score=None,
        invalid_reason="solution_contract_rejected",
        evidence_artifact_sha256=_sha("invalid-evidence"),
        actual_usage=ResourceVector(evaluator_transactions=1),
    )
    receipt = result.to_score_receipt(evaluation_id=slot.attempt_id)
    policy = FactorialITTPolicy.from_verified_manifest(
        benchmark_id=slot.benchmark_id
    )
    score = FactorialITTScore.from_score_receipt(
        policy=policy, score_receipt=receipt
    )
    report = VerifiedITTReportRow.seal(
        policy=policy, score_receipt=receipt, itt_score=score
    )
    row = AttemptCoverageRow.from_typed_score_chain(
        matrix_sha256=matrix.sha256,
        slot=slot,
        policy=policy,
        score_receipt=receipt,
        itt_score=score,
        report_row=report,
    )
    assert row.coverage_state == TYPED_SCORE_UNBOUND
    assert row.valid is False
    assert row.floor_imputed is True
    assert row.itt_raw_score == -1.0
    assert row.evaluator_operation_record_sha256 == "0" * 64


def _all_unexecuted(matrix: ExactFactorialAttemptMatrix):
    matrix_sha256 = matrix.sha256
    return [
        AttemptCoverageRow.unexecuted(matrix_sha256=matrix_sha256, slot=slot)
        for slot in matrix.slots
    ]


def _verifier(exact_inputs) -> FactorialCoverageVerifier:
    authority, bundle, plan, matrix = exact_inputs
    return FactorialCoverageVerifier.from_verified_sources(
        matrix=matrix,
        plan=plan,
        bundle=bundle,
        task_authority=authority,
    )


def test_exact_set_verifier_seals_zero_call_not_ready_status(exact_inputs) -> None:
    _authority, _bundle, _plan, matrix = exact_inputs
    rows = _all_unexecuted(matrix)
    seal = _verifier(exact_inputs).seal(rows)
    assert seal.exact_slot_set_complete is True
    assert seal.planned_scoring_slot_count == seal.submitted_row_count == 1566
    assert seal.unexecuted_row_count == 1566
    assert seal.typed_score_unbound_row_count == 0
    assert seal.all_reserved_attempts_covered is False
    assert seal.formal_execution_ready is False
    assert seal.execution_authority == "NOT_GRANTED"
    assert seal.operation_journal_event_count == 0
    assert "NOT_READY" in seal.formal_dispatch_status


def test_exact_set_verifier_rejects_missing_extra_duplicate_and_rebind(
    exact_inputs,
) -> None:
    _authority, _bundle, _plan, matrix = exact_inputs
    verifier = _verifier(exact_inputs)
    rows = _all_unexecuted(matrix)

    with pytest.raises(FactorialCoverageError, match="exact set"):
        verifier.seal(rows[:-1])
    with pytest.raises(FactorialCoverageError, match="duplicate"):
        verifier.seal(rows[:-1] + [rows[0]])

    extra = replace(
        rows[-1],
        attempt_id="factorial-attempt:extra:v002",
        slot_sha256="b" * 64,
    )
    with pytest.raises(FactorialCoverageError, match="exact set"):
        verifier.seal(rows[:-1] + [extra])

    rebound = replace(rows[5], cell_id=rows[5].cell_id + ":wrong")
    with pytest.raises(FactorialCoverageError, match="slot binding"):
        verifier.seal(rows[:5] + [rebound] + rows[6:])


def test_self_consistent_rehashed_whole_matrix_cannot_seal(exact_inputs) -> None:
    authority, bundle, plan, matrix = exact_inputs
    forged_plan_sha = "a" * 64
    forged_bundle_sha = "b" * 64
    forged_slots = tuple(
        replace(
            slot,
            factorial_plan_sha256=forged_plan_sha,
            task_authority_bundle_sha256=forged_bundle_sha,
        )
        for slot in matrix.slots
    )
    forged_matrix = replace(
        matrix,
        slots=forged_slots,
        factorial_plan_sha256=forged_plan_sha,
        task_authority_bundle_sha256=forged_bundle_sha,
    )
    forged_rows = _all_unexecuted(forged_matrix)

    with pytest.raises(FactorialCoverageError, match="pinned source replay"):
        FactorialCoverageVerifier.from_verified_sources(
            matrix=forged_matrix,
            plan=plan,
            bundle=bundle,
            task_authority=authority,
        )
    with pytest.raises(FactorialCoverageError, match="verified sources"):
        FactorialCoverageVerifier(forged_matrix)
    assert len(forged_rows) == 1566


def test_operation_record_hash_requires_independent_journal_and_head_replay(
    tmp_path: Path,
) -> None:
    journal = OperationJournal(
        tmp_path / "journal", anchor_path=tmp_path / "trusted-head.json"
    )
    governor = ResourceGovernor(
        journal=journal,
        global_caps=ResourceCaps(model_calls=1),
        cell_caps={"cell-a": ResourceCaps(model_calls=1)},
    )
    operation_id = "cell-a:solution:v002"
    governor.reserve(
        operation_id=operation_id,
        cell_id="cell-a",
        operation_kind="solution_call",
        reservation=ResourceVector(model_calls=1),
    )
    governor.start(operation_id)
    governor.complete(operation_id, artifact_sha256=_sha("solution-result"))
    digest = canonical_operation_record_sha256_from_journal(
        ledger_path=journal.ledger_path,
        anchor_path=tmp_path / "trusted-head.json",
        operation_id=operation_id,
    )
    assert len(digest) == 64

    anchor = tmp_path / "trusted-head.json"
    anchor.write_text(
        '{"schema_version":1,"event_count":3,"head_sha256":"'
        + "f" * 64
        + '"}\n',
        encoding="utf-8",
    )
    with pytest.raises(JournalIntegrityError, match="anchor|head"):
        canonical_operation_record_sha256_from_journal(
            ledger_path=journal.ledger_path,
            anchor_path=anchor,
            operation_id=operation_id,
        )


def test_invalid_native_evaluation_cannot_carry_score_or_bad_usage() -> None:
    with pytest.raises(FactorialCoverageError, match="fields differ"):
        NativeEvaluationResult(
            benchmark_id="gdpevo",
            valid=False,
            raw_score=0.0,
            invalid_reason="invalid",
            evidence_artifact_sha256=_sha("bad-invalid"),
            actual_usage=ResourceVector(evaluator_transactions=1),
        )
    with pytest.raises(FactorialCoverageError, match="one evaluator"):
        NativeEvaluationResult(
            benchmark_id="gdpevo",
            valid=True,
            raw_score=0.0,
            invalid_reason=None,
            evidence_artifact_sha256=_sha("bad-usage"),
            actual_usage=ResourceVector(),
        )
    with pytest.raises(FactorialCoverageError, match="cannot charge"):
        NativeEvaluationResult(
            benchmark_id="gdpevo",
            valid=True,
            raw_score=0.0,
            invalid_reason=None,
            evidence_artifact_sha256=_sha("bad-model-usage"),
            actual_usage=ResourceVector(
                model_calls=1, evaluator_transactions=1
            ),
        )


def test_unexecuted_row_cannot_claim_score_or_formal_readiness(exact_inputs) -> None:
    _authority, _bundle, _plan, matrix = exact_inputs
    row = AttemptCoverageRow.unexecuted(
        matrix_sha256=matrix.sha256, slot=matrix.slots[0]
    )
    assert row.coverage_state == UNEXECUTED
    with pytest.raises(FactorialCoverageError, match="result evidence"):
        replace(row, score_receipt_sha256="c" * 64)
