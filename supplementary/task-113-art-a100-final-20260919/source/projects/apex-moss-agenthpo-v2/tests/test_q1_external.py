"""Offline tests for Q1 fresh external-pool selection."""

import hashlib

from scripts.build_q1_external import frozen_order, select_candidates


def _row(task_id: str, libs: list[str]) -> dict:
    return {"task_id": task_id, "libs": repr(libs)}


def test_external_filter_is_frozen_and_excludes_prior_or_unsafe_rows():
    rows = [
        _row("prior", ["json"]),
        _row("old-safe", ["json"]),
        _row("new-matplotlib", ["matplotlib", "json"]),
        _row("transitive-not-allowed", ["PIL"]),
        _row("network", ["requests"]),
    ]

    eligible, excluded = select_candidates(
        rows,
        old_allowed={"json"},
        prior_ids={"prior"},
    )

    assert [row["task_id"] for row in eligible] == [
        "old-safe",
        "new-matplotlib",
    ]
    reasons = {item["task_id"]: item["reason"] for item in excluded}
    assert reasons["prior"] == "prior_model_pool"
    assert reasons["transitive-not-allowed"] == "outside_frozen_imports:PIL"
    assert reasons["network"] == "side_effect_blacklist:requests"


def test_external_order_is_sha256_task_id_order():
    rows = [_row(task_id, []) for task_id in ("task-c", "task-a", "task-b")]
    expected = sorted(
        rows,
        key=lambda row: hashlib.sha256(row["task_id"].encode()).hexdigest(),
    )

    assert frozen_order(reversed(rows)) == expected
