"""Offline tests for the Q2 paired-feedback confirmation."""

import json
from pathlib import Path

import pytest

from scripts.analyze_q2_paired import CONDITIONS, analyze
from scripts.build_q2_paired import build_pair
from scripts.import_bigcodebench_hard_canary import build_solution
from scripts.import_bigcodebench_hidden import build_hidden_test, build_visible_test

ROW = {
    "task_id": "BigCodeBench/1",
    "code_prompt": "def task_func(value):\n",
    "instruct_prompt": "Return the square of value.",
    "canonical_solution": "    return value * value\n",
    "test": (
        "import unittest\n"
        "class TestCases(unittest.TestCase):\n"
        "    def test_square(self):\n"
        "        self.assertEqual(task_func(3), 9)\n"
        "    def test_square_four(self):\n"
        "        self.assertEqual(task_func(4), 16)\n"
    ),
    "entry_point": "task_func",
    "score": 0.8,
    "libs": "[]",
}


def _source_task(root: Path, level: str = "V1") -> Path:
    task = root / "task"
    (task / "_hidden").mkdir(parents=True)
    (task / "solution.py").write_text(build_solution(ROW))
    (task / "test_solution.py").write_text(build_visible_test(ROW, level)[0])
    (task / "_hidden" / "test_hidden.py").write_text(build_hidden_test(ROW)[0])
    return task


def test_pair_changes_only_visible_feedback(tmp_path):
    pair = build_pair(ROW, _source_task(tmp_path), "V1")
    assert "test_square" not in pair["views"]["V0"]["test_solution.py"]
    assert "test_square" in pair["views"]["V1"]["test_solution.py"]
    assert pair["views"]["V1"]["visible_tests"] == ["TestCases.test_square"]
    assert pair["solution.py"] == build_solution(ROW)
    assert pair["_hidden/test_hidden.py"] == build_hidden_test(ROW)[0]


def test_pair_rejects_source_that_is_not_the_frozen_view(tmp_path):
    task = _source_task(tmp_path)
    (task / "test_solution.py").write_text("# changed\n")
    with pytest.raises(ValueError, match="source visible"):
        build_pair(ROW, task, "V1")


def _write_result_dir(root: Path, tag: str, values: dict[str, bool]) -> None:
    out = root / "results" / "official" / tag
    out.mkdir(parents=True)
    summary = {
        "repeats": 3,
        "tampered_runs": 0,
        "contract_violations": 0,
        "n_infra_invalid": 0,
    }
    (out / "summary.json").write_text(json.dumps(summary))
    for task, passed in values.items():
        for repeat in range(3):
            (out / f"{task}.rep{repeat}.json").write_text(json.dumps({
                "task": task,
                "passed": passed,
            }))


def test_analysis_uses_paired_difference_in_differences(tmp_path):
    for block, mapping in CONDITIONS.items():
        tasks = {f"{block}_a": False, f"{block}_b": False}
        for condition, tag in mapping.items():
            values = dict(tasks)
            if condition == ("S", "V1"):
                values = {task: True for task in tasks}
            _write_result_dir(tmp_path, tag, values)

    report = analyze(tmp_path)
    assert report["block_interactions"] == {"tdd": 1.0, "spec": 1.0}
    assert report["interaction_all"] == 1.0
    assert report["interaction_all_ci95"] == [1.0, 1.0]
    assert report["decision"] == "confirmed_feedback_shape_specialization"
