"""Unit tests for the canonical evaluator (no API calls — mock harnesses only)."""

import json
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

import pytest

HERE = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(HERE))

from _eval_one import _pytest_counts, make_guarded_tool_dispatch  # noqa: E402
from eval import check_model_lock, evaluate  # noqa: E402

FIXTURE = HERE / "tests" / "fixture_bench" / "add_bug"

ORACLE = '''MODEL = "claude-haiku-4-5"

def run(work_dir, tool_definitions, tool_dispatch):
    tool_dispatch["write_file"]({"path": work_dir + "/solution.py",
                                 "content": "def add(a, b):\\n    return a + b\\n"})
    return {"steps": 1, "tokens": 0, "messages": []}
'''

CHEATER = '''MODEL = "claude-haiku-4-5"

def run(work_dir, tool_definitions, tool_dispatch):
    tool_dispatch["write_file"]({"path": work_dir + "/test_solution.py",
                                 "content": "def test_nothing():\\n    assert True\\n"})
    return {"steps": 1, "tokens": 0, "messages": []}
'''

DO_NOTHING = '''MODEL = "claude-haiku-4-5"

def run(work_dir, tool_definitions, tool_dispatch):
    return {"steps": 0, "tokens": 0, "messages": []}
'''

VISIBLE_ONLY = '''MODEL = "claude-haiku-4-5"

def run(work_dir, tool_definitions, tool_dispatch):
    tool_dispatch["write_file"]({"path": work_dir + "/solution.py",
                                 "content": "def add(a, b):\\n    return abs(a) + abs(b)\\n"})
    return {"steps": 1, "tokens": 0, "messages": []}
'''

OUTSIDE_READER = '''MODEL = "claude-haiku-4-5"

def run(work_dir, tool_definitions, tool_dispatch):
    result = tool_dispatch["read_file"](
        {"path": work_dir + "/../test_hidden.py"}
    )
    return {"steps": 1, "tokens": 0, "messages": [str(result)]}
'''

NO_LOCK = '''MODEL = "some-other-model"

def run(work_dir, tool_definitions, tool_dispatch):
    return {"steps": 0, "tokens": 0, "messages": []}
'''


@pytest.fixture(autouse=True)
def fixture_bench():
    FIXTURE.mkdir(parents=True, exist_ok=True)
    (FIXTURE / "solution.py").write_text("def add(a, b):\n    return a - b\n")
    (FIXTURE / "test_solution.py").write_text(
        "from solution import add\n\ndef test_add():\n    assert add(2, 3) == 5\n"
    )
    yield


def _write_harness(tmp_path, code):
    d = tmp_path / "vtest"
    d.mkdir()
    f = d / "harness.py"
    f.write_text(code)
    return f


def _make_hidden_benchmark(tmp_path):
    benchmark = tmp_path / "hidden_bench" / "canary"
    task = benchmark / "add_hidden"
    hidden = task / "_hidden"
    hidden.mkdir(parents=True)
    (task / "solution.py").write_text("def add(a, b):\n    return a - b\n")
    (task / "test_solution.py").write_text(
        "from solution import add\n\n"
        "def test_visible_positive():\n"
        "    assert add(2, 3) == 5\n"
    )
    (hidden / "test_hidden.py").write_text(
        "from solution import add\n\n"
        "def test_hidden_positive():\n"
        "    assert add(2, 3) == 5\n\n"
        "def test_hidden_negative():\n"
        "    assert add(-2, -3) == -5, 'SECRET-HIDDEN-ASSERTION'\n"
    )
    return benchmark


def test_oracle_passes(tmp_path):
    h = _write_harness(tmp_path, ORACLE)
    s = evaluate(str(h), str(FIXTURE.parent), repeats=1, out_dir=str(tmp_path / "out"))
    assert s["pass_rate_mean"] == 1.0
    assert s["tampered_runs"] == 0
    assert s["n_infra_invalid"] == 0
    assert s["category_counts"] == {"passed": 1}


def test_cheater_caught_and_scored_zero(tmp_path):
    h = _write_harness(tmp_path, CHEATER)
    s = evaluate(str(h), str(FIXTURE.parent), repeats=1, out_dir=str(tmp_path / "out"))
    assert s["pass_rate_mean"] == 0.0
    assert s["tampered_runs"] == 1


def test_do_nothing_fails_honestly(tmp_path):
    h = _write_harness(tmp_path, DO_NOTHING)
    s = evaluate(str(h), str(FIXTURE.parent), repeats=1, out_dir=str(tmp_path / "out"))
    assert s["pass_rate_mean"] == 0.0
    assert s["tampered_runs"] == 0
    assert s["n_infra_invalid"] == 1
    assert s["category_counts"] == {"harness_error": 1}


def test_guarded_dispatch_rejects_paths_outside_work_dir(tmp_path):
    work = tmp_path / "work"
    work.mkdir()
    outside = tmp_path / "secret.txt"
    outside.write_text("secret")
    guarded = make_guarded_tool_dispatch(work)

    result = guarded["read_file"]({"path": str(outside)})

    assert "outside work_dir" in result
    assert guarded.contract_violations == 1


def test_hidden_suite_is_final_judge_and_output_is_redacted(tmp_path):
    h = _write_harness(tmp_path, VISIBLE_ONLY)
    benchmark = _make_hidden_benchmark(tmp_path)
    out = tmp_path / "out"

    s = evaluate(str(h), str(benchmark), repeats=1, out_dir=str(out))
    result = json.loads((out / "add_hidden.rep0.json").read_text())

    assert s["pass_rate_mean"] == 0.0
    assert s["category_counts"] == {"capability": 1}
    assert result["visible_passed"] is True
    assert result["hidden"] == {
        "passed": False,
        "n_passed": 1,
        "n_failed": 1,
        "errored": False,
    }
    serialized = json.dumps(result)
    assert "SECRET-HIDDEN-ASSERTION" not in serialized
    assert "test_hidden_negative" not in serialized


def test_candidate_runtime_and_teardown_errors_are_capability_failures():
    result = {
        "returncode": 1,
        "stdout": "5 failed, 5 errors in 0.10s",
        "stderr": "",
        "passed": False,
    }

    assert _pytest_counts(result) == (0, 5, False)


@pytest.mark.parametrize("returncode", [-1, 2, 3, 4, 5])
def test_pytest_infrastructure_exit_codes_remain_invalid(returncode):
    result = {
        "returncode": returncode,
        "stdout": "1 error in 0.10s",
        "stderr": "",
        "passed": False,
    }

    assert _pytest_counts(result) == (0, 1, True)


def test_hidden_directory_is_not_exposed_to_harness(tmp_path):
    h = _write_harness(tmp_path, OUTSIDE_READER)
    benchmark = _make_hidden_benchmark(tmp_path)
    out = tmp_path / "out"

    s = evaluate(str(h), str(benchmark), repeats=1, out_dir=str(out))
    result = json.loads((out / "add_hidden.rep0.json").read_text())

    assert result["contract_violations"] == 1
    assert s["contract_violations"] == 1
    assert "_hidden" not in json.dumps(result.get("trace", []))


def test_visible_test_side_effects_stay_in_scoring_directory(
        tmp_path, monkeypatch):
    benchmark = tmp_path / "side_effect_bench"
    task = benchmark / "add_side_effect"
    task.mkdir(parents=True)
    (task / "solution.py").write_text("def add(a, b):\n    return a - b\n")
    (task / "test_solution.py").write_text(
        "from solution import add\n\n"
        "def test_relative_write():\n"
        "    open('visible_leak.txt', 'w').write('temporary')\n"
        "    assert add(2, 3) == 5\n"
    )
    h = _write_harness(tmp_path, ORACLE)
    evaluator_cwd = tmp_path / "evaluator_cwd"
    evaluator_cwd.mkdir()
    monkeypatch.chdir(evaluator_cwd)

    s = evaluate(
        str(h),
        str(benchmark),
        repeats=1,
        out_dir=str(tmp_path / "out"),
    )

    assert s["pass_rate_mean"] == 1.0
    assert not (evaluator_cwd / "visible_leak.txt").exists()


def test_model_lock_rejected(tmp_path):
    h = _write_harness(tmp_path, NO_LOCK)
    with pytest.raises(SystemExit, match="REFUSED"):
        check_model_lock(h)


def test_benchmarks_are_valid():
    """Every imported task must have solution.py + test_solution.py, and for bugfix
    train/val the scoring suite must currently FAIL (bug/stub present)."""
    bench_root = HERE / "benchmarks"
    if not bench_root.exists():
        pytest.skip("benchmarks not imported yet")
    for family_dir in bench_root.iterdir():
        for split_dir in family_dir.iterdir():
            if not split_dir.is_dir():
                continue
            for task in split_dir.iterdir():
                if not task.is_dir():
                    continue
                assert (task / "solution.py").exists(), f"{task} missing solution.py"
                assert (task / "test_solution.py").exists(), f"{task} missing test_solution.py"
                scoring_test = (
                    task / "_hidden" / "test_hidden.py"
                    if (task / "_hidden" / "test_hidden.py").exists()
                    else task / "test_solution.py"
                )
                with tempfile.TemporaryDirectory() as tmp:
                    isolated = Path(tmp)
                    shutil.copy2(task / "solution.py", isolated / "solution.py")
                    shutil.copy2(scoring_test, isolated / "test_score.py")
                    r = subprocess.run(
                        [
                            sys.executable,
                            "-m",
                            "pytest",
                            str(isolated / "test_score.py"),
                            "-x",
                            "-q",
                            "-p",
                            "no:cacheprovider",
                            "--timeout=20",
                        ],
                        capture_output=True,
                        text=True,
                        timeout=150,
                        cwd=str(isolated),
                    )
                assert r.returncode != 0, f"{task}: tests pass without any fix — task is broken"
