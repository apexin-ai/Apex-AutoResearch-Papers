"""Offline tests for the revision-A/B1 Q1 confirmation runner."""

import json
from pathlib import Path

import scripts.q1_confirmation_runner as runner


def _summary(path: Path, tokens: int) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps({"total_tokens": tokens}))


def test_priority_cells_follow_decision_value_order(monkeypatch, tmp_path):
    state = tmp_path / "lineages.json"
    state.write_text(json.dumps({
        "status": "complete",
        "lineages": {
            "tddgen_hidden_r01": {"harness": "r01.py"},
            "tddgen_hidden_r02": {"harness": "r02.py"},
        },
    }))
    monkeypatch.setattr(runner, "LINEAGE_STATE", state)

    assert [cell.key for cell in runner.priority_cells()] == [
        "q1confirm-r02-train",
        "q1confirm-v001-external",
        "q1confirm-r00-external",
        "q1confirm-r02-external",
        "q1confirm-r01-train",
        "q1confirm-r01-external",
    ]


def test_b1_budget_counts_quick_canary_and_invalid_attempts(tmp_path):
    _summary(
        tmp_path
        / "harnesses/tddgen_hidden_r01/v001/train_summary.json",
        100,
    )
    _summary(
        tmp_path
        / "harnesses/tddgen_hidden_r02/v001/train_summary.json",
        200,
    )
    _summary(
        tmp_path / "results/canary/q1-external-v001/summary.json",
        300,
    )
    _summary(
        tmp_path
        / "results/invalid/formal-q1-tddgen_hidden_r01-v003-quick"
        / "results/summary.json",
        400,
    )
    _summary(
        tmp_path
        / "results/invalid/formal-q1-v007-spec-train/results/summary.json",
        999_999,
    )
    ledger = tmp_path / "results/official" / runner.LEDGER
    ledger.parent.mkdir(parents=True)
    ledger.write_text(
        json.dumps({"status": "invalid", "tokens": 500}) + "\n"
        + json.dumps({"status": "valid", "tokens": 600}) + "\n"
    )

    assert runner.preformal_executor_spent(tmp_path) == 1_000
    assert runner.remaining_formal_budget(tmp_path) == 23_998_500
