"""BigCodeBench-Hard canary conversion (no network or API calls)."""

import subprocess
import sys
from pathlib import Path

import pytest

import scripts.import_bigcodebench_hidden as hidden_import
from scripts.import_bigcodebench_hard_canary import (
    CHOSEN,
    build_solution,
    build_test,
    select_rows,
)
from scripts.import_bigcodebench_hidden import (
    LEVELS,
    build_hidden_test,
    build_visible_test,
    choose_family_sizes,
    filter_candidate_rows,
    partition_qualified_rows,
    split_behavior_tests,
)
from scripts.mutate_bugfix_hidden import (
    MUTATION_SEED,
    generate_mutations,
    select_accepted_mutation,
)

ROW = {
    "task_id": CHOSEN[0],
    "code_prompt": "import math\ndef task_func(value):\n",
    "instruct_prompt": "Return the square of value.",
    "canonical_solution": "    return value * value\n",
    "test": (
        "import unittest\n"
        "MODULE_VALUE = 3\n"
        "class TestCases(unittest.TestCase):\n"
        "    def setUp(self):\n"
        "        self.value = MODULE_VALUE\n"
        "    def helper(self):\n"
        "        return self.value\n"
        "    @unittest.skipIf(False, 'kept decorator')\n"
        "    def test_square(self):\n"
        "        self.assertEqual(task_func(self.helper()), 9)\n"
        "    def test_square_four(self):\n"
        "        self.assertEqual(task_func(4), 16)\n"
    ),
    "entry_point": "task_func",
    "score": 0.8,
    "libs": "['math']",
}


def test_stub_contains_prompt_but_not_oracle():
    source = build_solution(ROW)
    assert "Return the square of value." in source
    assert "pass" in source
    assert "return value * value" not in source
    compile(source, "<stub>", "exec")


def test_oracle_source_is_complete():
    source = build_solution(ROW, oracle=True)
    assert "return value * value" in source
    assert "pass" not in source
    compile(source, "<oracle>", "exec")


def test_test_wrapper_imports_solution_and_preserves_tests():
    tests = build_test(ROW)
    assert "from solution import *" in tests
    assert "self.assertEqual(task_func(self.helper()), 9)" in tests
    assert not any(line.endswith(" ") for line in tests.splitlines())
    compile(tests, "<tests>", "exec")


def test_selection_is_frozen_and_ordered():
    rows = [{"task_id": task_id} for task_id in reversed(CHOSEN)]
    assert [row["task_id"] for row in select_rows(rows)] == CHOSEN
    with pytest.raises(ValueError, match="missing frozen task"):
        select_rows(rows[:-1])


def test_visible_split_keeps_fixture_helpers_and_first_test_only():
    split, names = split_behavior_tests(ROW["test"], 1)
    assert names == ["TestCases.test_square"]
    assert "MODULE_VALUE = 3" in split
    assert "def setUp" in split
    assert "def helper" in split
    assert "def test_square(" in split
    assert "def test_square_four" not in split
    assert "kept decorator" in split
    compile(split, "<visible raw tests>", "exec")


def test_v1_visible_and_hidden_suites_are_separate():
    visible, visible_names = build_visible_test(ROW, "V1")
    hidden, hidden_names = build_hidden_test(ROW)
    assert LEVELS["V1"] == 1
    assert visible_names == ["TestCases.test_square"]
    assert hidden_names == [
        "TestCases.test_square",
        "TestCases.test_square_four",
    ]
    assert "test_square_four" not in visible
    assert "test_square_four" in hidden
    assert "from solution import *" in visible
    compile(visible, "<visible tests>", "exec")
    compile(hidden, "<hidden tests>", "exec")


def test_v0_contains_only_callable_smoke():
    visible, names = build_visible_test(ROW, "V0")
    assert names == []
    assert "callable(solution.task_func)" in visible
    assert "test_square" not in visible
    compile(visible, "<smoke tests>", "exec")


def test_unknown_visibility_level_is_rejected():
    with pytest.raises(ValueError, match="unknown visibility level"):
        build_visible_test(ROW, "V3")


def test_hidden_importer_supports_direct_cli_execution():
    root = Path(__file__).resolve().parent.parent
    result = subprocess.run(
        [
            sys.executable,
            str(root / "scripts" / "import_bigcodebench_hidden.py"),
            "--help",
        ],
        cwd=root,
        capture_output=True,
        text=True,
        timeout=30,
    )
    assert result.returncode == 0, result.stderr
    assert "--level" in result.stdout


def test_rows_service_failure_uses_frozen_parquet(monkeypatch):
    failure = hidden_import.urllib.error.HTTPError(
        "https://example.invalid", 500, "server error", {}, None
    )
    monkeypatch.setattr(
        hidden_import,
        "fetch_rows",
        lambda: (_ for _ in ()).throw(failure),
    )
    expected = [{"task_id": CHOSEN[0]}]
    monkeypatch.setattr(
        hidden_import, "fetch_rows_from_frozen_parquet", lambda: expected
    )

    assert hidden_import.fetch_official_rows() == expected


def test_sha_partition_is_deterministic_and_disjoint():
    rows = [
        {"task_id": f"BigCodeBench/{number}"}
        for number in range(100, 146)
    ]
    family_a, family_b, order_hash = partition_qualified_rows(rows)
    again_a, again_b, again_hash = partition_qualified_rows(reversed(rows))

    assert [row["task_id"] for row in family_a] == [
        row["task_id"] for row in again_a
    ]
    assert [row["task_id"] for row in family_b] == [
        row["task_id"] for row in again_b
    ]
    assert order_hash == again_hash
    assert {row["task_id"] for row in family_a}.isdisjoint(
        row["task_id"] for row in family_b
    )
    assert len(family_a) == len(family_b) == 23


def test_family_size_falls_back_to_preregistered_minimum():
    assert choose_family_sizes(22, 22) == (10, 12)
    assert choose_family_sizes(22, 21) == (8, 10)
    with pytest.raises(ValueError, match="fewer than 18"):
        choose_family_sizes(17, 30)


def test_candidate_filter_records_preregistered_exclusion_reasons():
    rows = [
        {"task_id": CHOSEN[0], "libs": "['json']"},
        {"task_id": "BigCodeBench/1", "libs": "['json']"},
        {"task_id": "BigCodeBench/2", "libs": "['requests']"},
        {"task_id": "BigCodeBench/3", "libs": "['missing_lib']"},
    ]
    eligible, excluded = filter_candidate_rows(rows, {"json", "requests"})

    assert [row["task_id"] for row in eligible] == ["BigCodeBench/1"]
    assert excluded == [
        {"task_id": CHOSEN[0], "reason": "canary"},
        {
            "task_id": "BigCodeBench/2",
            "reason": "side_effect_blacklist:requests",
        },
        {
            "task_id": "BigCodeBench/3",
            "reason": "unavailable_libs:missing_lib",
        },
    ]


def test_mutation_candidates_are_seeded_and_operator_ordered():
    source = (
        "def task_func(value=1):\n"
        "    if value < 3:\n"
        "        return sum([value, 1])\n"
        "    return 0\n"
    )
    first = list(generate_mutations(source))
    second = list(generate_mutations(source))

    assert MUTATION_SEED == 20260727
    assert first == second
    assert first[0].operator == "boundary_comparison"
    assert "value <= 3" in first[0].source
    operator_order = list(dict.fromkeys(item.operator for item in first))
    assert operator_order == [
        "boundary_comparison",
        "off_by_one_constant",
        "conditional_branch_deletion",
        "default_value_replacement",
        "aggregation_replacement",
    ]
    for candidate in first:
        compile(candidate.source, "<mutation>", "exec")


def test_mutation_acceptance_requires_visible_pass_and_hidden_fail():
    source = (
        "def task_func(value):\n"
        "    return value < 3\n"
    )

    class Result:
        def __init__(self, returncode):
            self.returncode = returncode

    def fake_runner(candidate, tests):
        if tests == "visible":
            return Result(0)
        return Result(1 if "value <= 3" in candidate else 0)

    mutation = select_accepted_mutation(
        source, "visible", "hidden", test_runner=fake_runner
    )

    assert mutation is not None
    assert mutation.operator == "boundary_comparison"
    assert "value <= 3" in mutation.source
