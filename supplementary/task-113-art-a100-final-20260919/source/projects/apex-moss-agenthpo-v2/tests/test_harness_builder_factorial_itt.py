from __future__ import annotations

import copy
from pathlib import Path

import pytest

from optimization_lab.harness_builder.factorial_contract import (
    DEFAULT_FACTORIAL_MANIFEST,
    canonical_factorial_bytes,
    factorial_contract_digest,
    verify_factorial_contract,
)
from optimization_lab.harness_builder.factorial_itt import (
    FactorialITTError,
    FactorialITTPolicy,
    FactorialITTScore,
    VerifiedITTReportRow,
)
from optimization_lab.harness_builder.factorial_score import (
    EvaluationScoreObservation,
    EvaluationScoreReceipt,
    canonical_score_bytes,
)


EVIDENCE_SHA = "a" * 64


def _policy(benchmark_id: str) -> FactorialITTPolicy:
    return FactorialITTPolicy.from_verified_manifest(benchmark_id=benchmark_id)


def _receipt(
    benchmark_id: str,
    *,
    raw_score: float | None,
    invalid_reason: str | None = None,
) -> EvaluationScoreReceipt:
    valid = invalid_reason is None
    observation = EvaluationScoreObservation.create(
        benchmark_id=benchmark_id,
        valid=valid,
        raw_score=raw_score,
        invalid_reason=invalid_reason,
        evaluation_evidence_sha256=EVIDENCE_SHA if valid else "0" * 64,
    )
    return EvaluationScoreReceipt.seal(
        evaluation_id=f"{benchmark_id}:task:seed:arm:v002",
        observation=observation,
    )


@pytest.mark.parametrize(
    ("benchmark_id", "raw_floor", "utility_floor"),
    [("agenthpobench", -1.0, 1.0), ("gdpevo", 0.0, 1.0)],
)
def test_policy_is_derived_from_exact_manifest_and_native_contract(
    benchmark_id: str, raw_floor: float, utility_floor: float
) -> None:
    factorial = verify_factorial_contract()
    policy = _policy(benchmark_id)
    assert policy.factorial_contract_sha256 == factorial["contract_digest"]
    assert (policy.raw_floor, policy.utility_floor) == (raw_floor, utility_floor)
    assert policy.invalid_score_policy == "BENCHMARK_NATIVE_RAW_MINIMUM"
    assert "COVERAGE_NOT_READY" in policy.invalid_reason_scope
    assert FactorialITTPolicy.from_canonical_bytes(policy.canonical_bytes()) == policy


def test_self_rehashed_minimal_or_modified_factorial_manifest_is_rejected(
    tmp_path: Path,
) -> None:
    factorial = verify_factorial_contract()
    forged = {
        "main_experiment": {
            "benchmarks": [{"benchmark_id": "agenthpobench"}],
            "score_boundary": factorial["main_experiment"]["score_boundary"],
        }
    }
    forged["contract_digest"] = factorial_contract_digest(forged)
    path = tmp_path / "forged.json"
    path.write_bytes(canonical_factorial_bytes(forged))
    with pytest.raises(FactorialITTError, match="verification failed"):
        FactorialITTPolicy.from_verified_manifest(
            benchmark_id="agenthpobench", manifest_path=path
        )

    modified = copy.deepcopy(factorial)
    modified["contract_id"] = "self-rehashed-forgery"
    modified["contract_digest"] = factorial_contract_digest(modified)
    path.write_bytes(canonical_factorial_bytes(modified))
    with pytest.raises(FactorialITTError, match="verification failed"):
        FactorialITTPolicy.from_verified_manifest(
            benchmark_id="agenthpobench", manifest_path=path
        )


def test_valid_receipt_keeps_observed_score_and_public_row_is_raw_only() -> None:
    policy = _policy("agenthpobench")
    receipt = _receipt("agenthpobench", raw_score=0.25)
    score = FactorialITTScore.from_score_receipt(
        policy=policy, score_receipt=receipt
    )
    assert score.raw_itt_score == 0.25
    assert score.verified_utility_for_optimization(
        policy=policy, score_receipt=receipt
    ) == 2.25
    row = VerifiedITTReportRow.seal(
        policy=policy, score_receipt=receipt, itt_score=score
    )
    assert row.itt_raw_score == 0.25
    assert set(row.to_dict()) == {
        "benchmark_id",
        "evaluation_id",
        "factorial_contract_sha256",
        "floor_imputed",
        "invalid_reason",
        "itt_raw_score",
        "itt_score_sha256",
        "policy_sha256",
        "reporting_metric",
        "schema_version",
        "score_receipt_sha256",
        "valid",
    }
    assert not any("utility" in key for key in row.to_dict())


@pytest.mark.parametrize(
    "reason",
    [
        "evaluator_invalid",
        "solution_contract_rejected",
        "operation_timeout",
        "started_without_artifact",
        "wide_transition_rejected",
        "attempt_cap_exhausted",
    ],
)
def test_each_typed_invalid_score_receipt_is_imputed_at_native_floor(
    reason: str,
) -> None:
    policy = _policy("agenthpobench")
    receipt = _receipt("agenthpobench", raw_score=None, invalid_reason=reason)
    score = FactorialITTScore.from_score_receipt(
        policy=policy, score_receipt=receipt
    )
    assert (score.raw_itt_score, score.utility_itt_score) == (-1.0, 1.0)
    row = VerifiedITTReportRow.seal(
        policy=policy, score_receipt=receipt, itt_score=score
    )
    assert row.floor_imputed is True
    assert row.invalid_reason == reason


def test_direct_policy_spoof_cannot_sign_a_score_or_report() -> None:
    exact = _policy("gdpevo")
    spoof = FactorialITTPolicy(
        **{**exact.to_dict(), "factorial_contract_sha256": "b" * 64}
    )
    receipt = _receipt("gdpevo", raw_score=0.5)
    with pytest.raises(FactorialITTError, match="exact manifest"):
        FactorialITTScore.from_score_receipt(
            policy=spoof, score_receipt=receipt
        )

    exact_score = FactorialITTScore.from_score_receipt(
        policy=exact, score_receipt=receipt
    )
    forged = FactorialITTScore(
        **{
            **exact_score.to_dict(),
            "policy_sha256": "c" * 64,
            "observation_sha256": "d" * 64,
            "score_receipt_sha256": "e" * 64,
        }
    )
    with pytest.raises(FactorialITTError):
        VerifiedITTReportRow.seal(
            policy=exact, score_receipt=receipt, itt_score=forged
        )


def test_report_parser_rejects_internal_utility_or_tampered_binding() -> None:
    policy = _policy("gdpevo")
    receipt = _receipt(
        "gdpevo", raw_score=None, invalid_reason="evaluator_contract_rejected"
    )
    score = FactorialITTScore.from_score_receipt(
        policy=policy, score_receipt=receipt
    )
    row = VerifiedITTReportRow.seal(
        policy=policy, score_receipt=receipt, itt_score=score
    )
    assert VerifiedITTReportRow.from_canonical_bytes(
        row.canonical_bytes(),
        policy=policy,
        score_receipt=receipt,
        itt_score=score,
    ) == row

    for field, replacement in (
        ("utility_itt_score", 1.0),
        ("itt_raw_score", 0.5),
        ("score_receipt_sha256", "f" * 64),
    ):
        payload = row.to_dict()
        payload[field] = replacement
        with pytest.raises(FactorialITTError):
            VerifiedITTReportRow.from_canonical_bytes(
                canonical_score_bytes(payload),
                policy=policy,
                score_receipt=receipt,
                itt_score=score,
            )


def test_missing_score_receipt_or_benchmark_mismatch_fails_closed() -> None:
    policy = _policy("gdpevo")
    wrong = _receipt("agenthpobench", raw_score=0.0)
    with pytest.raises(FactorialITTError, match="benchmark"):
        FactorialITTScore.from_score_receipt(
            policy=policy, score_receipt=wrong
        )
    with pytest.raises(FactorialITTError, match="score receipt"):
        FactorialITTScore.from_score_receipt(
            policy=policy, score_receipt=None  # type: ignore[arg-type]
        )


def test_default_manifest_is_the_exact_checked_in_source() -> None:
    assert DEFAULT_FACTORIAL_MANIFEST.is_file()
    assert _policy("gdpevo").factorial_contract_sha256 == verify_factorial_contract()[
        "contract_digest"
    ]
