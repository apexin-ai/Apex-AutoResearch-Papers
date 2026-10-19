"""Offline analysis tests for the Q1 independent-lineage confirmation."""

import json
from pathlib import Path

from scripts.analyze_q1_confirmation import analyze


def _write_summary(root: Path, tag: str, score: float, std: float = 0.0) -> None:
    out = root / "results" / "official" / tag
    out.mkdir(parents=True)
    (out / "summary.json").write_text(json.dumps({
        "repeats": 3,
        "pass_rate_mean": score,
        "pass_rate_std": std,
        "tampered_runs": 0,
        "contract_violations": 0,
        "n_infra_invalid": 0,
    }))


def _write_external(
    root: Path, tag: str, values: dict[str, bool]
) -> None:
    _write_summary(
        root,
        tag,
        sum(values.values()) / len(values),
    )
    out = root / "results" / "official" / tag
    for task, passed in values.items():
        for repeat in range(3):
            (out / f"{task}.rep{repeat}.json").write_text(json.dumps({
                "task": task,
                "passed": passed,
            }))


def test_q1_analysis_requires_reproducible_train_gain_and_external_gain(
    tmp_path,
):
    _write_summary(tmp_path, "hidden-v001-tddgen_hidden-train", 0.75)
    _write_summary(tmp_path, "hidden-v005-tddgen_hidden-train", 1.0)
    _write_summary(tmp_path, "q1confirm-r01-train", 1.0)
    _write_summary(tmp_path, "q1confirm-r02-train", 0.875)

    generic = {"task_a": False, "task_b": False}
    perfect = {"task_a": True, "task_b": True}
    _write_external(tmp_path, "q1confirm-v001-external", generic)
    _write_external(tmp_path, "q1confirm-r00-external", perfect)
    _write_external(tmp_path, "q1confirm-r01-external", perfect)
    _write_external(tmp_path, "q1confirm-r02-external", perfect)

    report = analyze(tmp_path)

    assert report["qualified_lineages"] == ["r00", "r01"]
    assert report["decision"] == "reproducible_generalization"
    assert report["external_effect_qualified"] == 1.0
    assert report["external_effect_ci95"] == (1.0, 1.0)
    assert report["decision_complete"] is True


def test_q1_analysis_can_close_after_priority_four_without_r01(tmp_path):
    _write_summary(tmp_path, "hidden-v001-tddgen_hidden-train", 0.75)
    _write_summary(tmp_path, "hidden-v005-tddgen_hidden-train", 1.0)
    _write_summary(tmp_path, "q1confirm-r02-train", 1.0)

    generic = {"task_a": False, "task_b": False}
    perfect = {"task_a": True, "task_b": True}
    _write_external(tmp_path, "q1confirm-v001-external", generic)
    _write_external(tmp_path, "q1confirm-r00-external", perfect)
    _write_external(tmp_path, "q1confirm-r02-external", perfect)

    report = analyze(tmp_path)

    assert report["qualified_lineages"] == ["r00", "r02"]
    assert report["decision"] == "reproducible_generalization"
    assert report["external_effect_qualified"] == 1.0
    assert report["missing_cells"] == [
        "q1confirm-r01-train",
        "q1confirm-r01-external",
    ]
    assert report["decision_complete"] is True


def test_q1_analysis_reports_incomplete_when_qualified_external_is_missing(
    tmp_path,
):
    _write_summary(tmp_path, "hidden-v001-tddgen_hidden-train", 0.75)
    _write_summary(tmp_path, "hidden-v005-tddgen_hidden-train", 1.0)
    _write_summary(tmp_path, "q1confirm-r02-train", 1.0)
    _write_external(
        tmp_path,
        "q1confirm-v001-external",
        {"task_a": False, "task_b": False},
    )

    report = analyze(tmp_path)

    assert report["decision"] == "matrix_incomplete"
    assert report["external_effect_qualified"] is None
    assert report["decision_complete"] is False
