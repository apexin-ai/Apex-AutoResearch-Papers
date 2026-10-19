from __future__ import annotations

import hashlib
import json
import math

import pytest

from optimization_lab.harness_builder.factorial_score import (
    AGENTHPOBENCH_SCORE_CONTRACT,
    GDPEVO_SCORE_CONTRACT,
    EvaluationScoreObservation,
    EvaluationScoreReceipt,
    ScoreContractError,
    canonical_score_bytes,
    score_contract_for,
    score_sha256,
)


EVIDENCE_SHA = "a" * 64


@pytest.mark.parametrize(
    ("benchmark_id", "raw", "utility"),
    [
        ("agenthpobench", -1.0, 1.0),
        ("agenthpobench", 0.0, 2.0),
        ("agenthpobench", 1.0, 3.0),
        ("gdpevo", 0.0, 1.0),
        ("gdpevo", 0.25, 1.25),
        ("gdpevo", 1.0, 2.0),
    ],
)
def test_frozen_contracts_map_raw_to_internal_utility_and_back(
    benchmark_id: str, raw: float, utility: float
) -> None:
    contract = score_contract_for(benchmark_id)
    assert contract.utility_from_raw(raw) == utility
    assert contract.raw_from_utility(utility) == raw
    assert contract.reporting_metric == "RAW_SCORE_ONLY"
    assert contract.utility_scope == "OPTIMIZATION_INTERNAL_ONLY"
    assert contract.sha256 == hashlib.sha256(contract.canonical_bytes()).hexdigest()


def test_exact_frozen_score_ranges_and_transforms() -> None:
    assert AGENTHPOBENCH_SCORE_CONTRACT.raw_range == (-1.0, 1.0)
    assert AGENTHPOBENCH_SCORE_CONTRACT.utility_range == (1.0, 3.0)
    assert AGENTHPOBENCH_SCORE_CONTRACT.transform.to_dict() == {
        "kind": "AFFINE_V1",
        "offset": 2.0,
        "scale": 1.0,
        "transform_id": "agenthpobench_raw_plus_2_v1",
    }
    assert GDPEVO_SCORE_CONTRACT.raw_range == (0.0, 1.0)
    assert GDPEVO_SCORE_CONTRACT.utility_range == (1.0, 2.0)
    assert GDPEVO_SCORE_CONTRACT.transform.offset == 1.0


def test_non_binary_exact_raw_score_is_valid_and_inverse_is_numerically_stable() -> None:
    observation = EvaluationScoreObservation.create(
        benchmark_id="agenthpobench",
        valid=True,
        raw_score=0.1,
        evaluation_evidence_sha256=EVIDENCE_SHA,
    )
    assert observation.utility_score == 2.1
    assert AGENTHPOBENCH_SCORE_CONTRACT.raw_from_utility(
        observation.utility_score
    ) == pytest.approx(0.1)


@pytest.mark.parametrize("bad", [True, False, None, "0", math.nan, math.inf, -math.inf])
def test_score_conversion_rejects_non_finite_and_non_numeric_values(bad: object) -> None:
    with pytest.raises(ScoreContractError):
        AGENTHPOBENCH_SCORE_CONTRACT.utility_from_raw(bad)  # type: ignore[arg-type]
    with pytest.raises(ScoreContractError):
        AGENTHPOBENCH_SCORE_CONTRACT.raw_from_utility(bad)  # type: ignore[arg-type]


@pytest.mark.parametrize(
    ("contract", "raw", "utility"),
    [
        (AGENTHPOBENCH_SCORE_CONTRACT, -1.000001, 0.999999),
        (AGENTHPOBENCH_SCORE_CONTRACT, 1.000001, 3.000001),
        (GDPEVO_SCORE_CONTRACT, -0.000001, 0.999999),
        (GDPEVO_SCORE_CONTRACT, 1.000001, 2.000001),
    ],
)
def test_score_conversion_rejects_values_outside_inclusive_ranges(
    contract: object, raw: float, utility: float
) -> None:
    with pytest.raises(ScoreContractError):
        contract.utility_from_raw(raw)  # type: ignore[attr-defined]
    with pytest.raises(ScoreContractError):
        contract.raw_from_utility(utility)  # type: ignore[attr-defined]


def test_valid_observation_binds_raw_utility_transform_and_contract() -> None:
    observation = EvaluationScoreObservation.create(
        benchmark_id="agenthpobench",
        valid=True,
        raw_score=-0.25,
        evaluation_evidence_sha256=EVIDENCE_SHA,
    )
    payload = observation.to_dict()
    assert payload["raw_score"] == -0.25
    assert payload["utility_score"] == 1.75
    assert payload["transform"] == AGENTHPOBENCH_SCORE_CONTRACT.transform.to_dict()
    assert payload["score_contract_sha256"] == AGENTHPOBENCH_SCORE_CONTRACT.sha256
    assert payload["reporting_metric"] == "RAW_SCORE_ONLY"
    assert observation.utility_for_optimization() == 1.75
    assert EvaluationScoreObservation.from_canonical_bytes(
        observation.canonical_bytes()
    ) == observation


def test_valid_score_artifacts_reject_zero_evidence_hash() -> None:
    with pytest.raises(ScoreContractError, match="nonzero evaluation evidence"):
        EvaluationScoreObservation.create(
            benchmark_id="agenthpobench",
            valid=True,
            raw_score=0.0,
            evaluation_evidence_sha256="0" * 64,
        )

    observation = EvaluationScoreObservation.create(
        benchmark_id="gdpevo",
        valid=True,
        raw_score=0.5,
        evaluation_evidence_sha256=EVIDENCE_SHA,
    )
    receipt = EvaluationScoreReceipt.seal(
        evaluation_id="gdpevo:task_group_003:test_1:v001",
        observation=observation,
    )
    payload = receipt.to_dict()
    payload["evaluation_evidence_sha256"] = "0" * 64
    with pytest.raises(ScoreContractError, match="nonzero evaluation evidence"):
        EvaluationScoreReceipt.from_dict(payload)


def test_invalid_observation_may_use_zero_evidence_sentinel() -> None:
    observation = EvaluationScoreObservation.create(
        benchmark_id="gdpevo",
        valid=False,
        raw_score=None,
        invalid_reason="evaluation_never_produced_evidence",
        evaluation_evidence_sha256="0" * 64,
    )
    assert observation.evaluation_evidence_sha256 == "0" * 64


def test_invalid_observation_keeps_transform_binding_but_exposes_no_scores() -> None:
    observation = EvaluationScoreObservation.create(
        benchmark_id="gdpevo",
        valid=False,
        raw_score=None,
        invalid_reason="evaluator_contract_rejected",
        evaluation_evidence_sha256=EVIDENCE_SHA,
    )
    assert observation.raw_score is None
    assert observation.utility_score is None
    assert observation.transform == GDPEVO_SCORE_CONTRACT.transform
    assert observation.utility_for_optimization() is None
    assert observation.report_projection() == {
        "benchmark_id": "gdpevo",
        "invalid_reason": "evaluator_contract_rejected",
        "raw_score": None,
        "reporting_metric": "RAW_SCORE_ONLY",
        "valid": False,
    }


@pytest.mark.parametrize(
    "kwargs",
    [
        {"valid": True, "raw_score": None, "invalid_reason": None},
        {"valid": True, "raw_score": 0.5, "invalid_reason": "unexpected"},
        {"valid": False, "raw_score": 0.5, "invalid_reason": "bad"},
        {"valid": False, "raw_score": None, "invalid_reason": None},
        {"valid": 1, "raw_score": 0.5, "invalid_reason": None},
    ],
)
def test_observation_has_strict_valid_invalid_semantics(kwargs: dict[str, object]) -> None:
    with pytest.raises(ScoreContractError):
        EvaluationScoreObservation.create(
            benchmark_id="gdpevo",
            evaluation_evidence_sha256=EVIDENCE_SHA,
            **kwargs,  # type: ignore[arg-type]
        )


def test_parser_rejects_mismatched_utility_transform_and_contract() -> None:
    observation = EvaluationScoreObservation.create(
        benchmark_id="gdpevo",
        valid=True,
        raw_score=0.5,
        evaluation_evidence_sha256=EVIDENCE_SHA,
    )
    for field, replacement in (
        ("utility_score", 1.500000000000001),
        ("score_contract_sha256", "b" * 64),
        (
            "transform",
            {
                **observation.transform.to_dict(),
                "offset": 2.0,
            },
        ),
    ):
        payload = observation.to_dict()
        payload[field] = replacement
        with pytest.raises(ScoreContractError):
            EvaluationScoreObservation.from_dict(payload)


def test_receipt_repeats_score_binding_and_commits_to_observation() -> None:
    observation = EvaluationScoreObservation.create(
        benchmark_id="agenthpobench",
        valid=True,
        raw_score=0.125,
        evaluation_evidence_sha256=EVIDENCE_SHA,
    )
    receipt = EvaluationScoreReceipt.seal(
        evaluation_id="agenthpobench:task_1:seed_1:v001",
        observation=observation,
    )
    payload = receipt.to_dict()
    assert payload["raw_score"] == 0.125
    assert payload["utility_score"] == 2.125
    assert payload["transform"] == observation.transform.to_dict()
    assert payload["observation_sha256"] == observation.sha256
    assert receipt.report_projection()["raw_score"] == 0.125
    assert "utility_score" not in receipt.report_projection()
    assert EvaluationScoreReceipt.from_canonical_bytes(receipt.canonical_bytes()) == receipt


def test_receipt_detects_tampering_even_when_tampered_json_is_canonical() -> None:
    observation = EvaluationScoreObservation.create(
        benchmark_id="gdpevo",
        valid=True,
        raw_score=0.5,
        evaluation_evidence_sha256=EVIDENCE_SHA,
    )
    receipt = EvaluationScoreReceipt.seal(
        evaluation_id="gdpevo:task_group_003:test_1:v001",
        observation=observation,
    )
    payload = receipt.to_dict()
    payload["raw_score"] = 0.75
    payload["utility_score"] = 1.75
    with pytest.raises(ScoreContractError, match="observation sha256"):
        EvaluationScoreReceipt.from_canonical_bytes(canonical_score_bytes(payload))


def test_canonical_serialization_and_sha_are_strict() -> None:
    observation = EvaluationScoreObservation.create(
        benchmark_id="gdpevo",
        valid=True,
        raw_score=0.0,
        evaluation_evidence_sha256=EVIDENCE_SHA,
    )
    raw = observation.canonical_bytes()
    assert raw.endswith(b"\n")
    assert score_sha256(observation.to_dict()) == observation.sha256
    pretty = json.dumps(observation.to_dict(), indent=2).encode("utf-8") + b"\n"
    with pytest.raises(ScoreContractError, match="canonical"):
        EvaluationScoreObservation.from_canonical_bytes(pretty)
    duplicate = raw.replace(b'{"benchmark_id":', b'{"benchmark_id":"gdpevo","benchmark_id":', 1)
    with pytest.raises(ScoreContractError, match="repeats field"):
        EvaluationScoreObservation.from_canonical_bytes(duplicate)


def test_unknown_benchmark_and_report_utility_are_fail_closed() -> None:
    with pytest.raises(ScoreContractError, match="unsupported benchmark"):
        score_contract_for("unknown")
    observation = EvaluationScoreObservation.create(
        benchmark_id="gdpevo",
        valid=True,
        raw_score=0.5,
        evaluation_evidence_sha256=EVIDENCE_SHA,
    )
    with pytest.raises(ScoreContractError, match="raw score only"):
        observation.report_value("utility_score")
    assert observation.report_value("raw_score") == 0.5
