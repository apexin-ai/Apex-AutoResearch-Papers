from __future__ import annotations

import hashlib

import pytest

from optimization_lab.harness_builder.operators import PublicAttempt
from optimization_lab.harness_builder.swebench_contract_qualification import (
    build_qualification_summary,
)


def _attempt(index: int, *, valid: bool) -> PublicAttempt:
    text = f"attempt-{index}"
    return PublicAttempt(
        attempt_id=f"v{index:03d}",
        artifact_sha256=hashlib.sha256(text.encode()).hexdigest(),
        artifact_text=text,
        correct=valid,
        score=0.5 + index / 100 if valid else None,
        outcome="valid" if valid else "contract_rejected",
        structural_signature=f"structure-{index}",
        public_summary="valid score" if valid else "artifact contract rejected",
    )


def _summary(valid: int):
    attempts = tuple(
        _attempt(index, valid=index <= valid) for index in range(1, 9)
    )
    return build_qualification_summary(
        attempts=attempts,
        staging_plan_sha256="a" * 64,
        code_revision="b" * 40,
        rule_registry_sha256="c" * 64,
        task_binding_sha256="d" * 64,
        cell_id="qualification:swebench-verified:sphinx-doc__sphinx-8459:contract-compatibility",
    )


def test_qualification_blocks_formal_stream_below_four_valid_rounds() -> None:
    summary = _summary(3)

    assert summary["validity_status"] == "insufficient_validity"
    assert summary["valid_rounds"] == 3
    assert summary["valid_only_mean"] is None
    assert summary["best_score"] is None
    assert summary["may_start_formal_stream"] is False


def test_qualification_admits_formal_stream_at_four_valid_rounds() -> None:
    summary = _summary(4)

    assert summary["validity_status"] == "sufficient_validity"
    assert summary["valid_rounds"] == 4
    assert summary["valid_only_mean"] == pytest.approx(0.525)
    assert summary["best_score"] == pytest.approx(0.54)
    assert summary["may_start_formal_stream"] is True
    assert summary["formal_score_reuse_forbidden"] is True
