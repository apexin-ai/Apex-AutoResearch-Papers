"""Run one harness on one task in a sandbox; verify integrity; score. Called by eval.py."""

import hashlib
import importlib.util
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import config  # noqa: E402
from tools import TOOL_DEFINITIONS, TOOL_DISPATCH, run_tests  # noqa: E402

HIDDEN_TEST_TIMEOUT = 120


def sha256(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()


class GuardedToolDispatch(dict):
    """Tool mapping that confines all path-bearing calls to one work directory."""

    PATH_KEYS = {
        "read_file": "path",
        "write_file": "path",
        "run_tests": "test_path",
    }

    def __init__(self, work_dir: Path, dispatch: dict):
        self.work_dir = work_dir.resolve()
        self.contract_violations = 0
        super().__init__()
        for name, func in dispatch.items():
            path_key = self.PATH_KEYS.get(name)
            self[name] = (
                self._guard(name, func, path_key) if path_key else func
            )

    def _guard(self, name, func, path_key):
        def guarded(args):
            if not isinstance(args, dict) or not isinstance(args.get(path_key), str):
                self.contract_violations += 1
                return f"ERROR: invalid {name} path input"
            candidate = Path(args[path_key])
            if not candidate.is_absolute():
                candidate = self.work_dir / candidate
            try:
                resolved = candidate.resolve()
                inside = resolved.is_relative_to(self.work_dir)
            except (OSError, RuntimeError):
                inside = False
            if not inside:
                self.contract_violations += 1
                return "ERROR: path outside work_dir"
            safe_args = dict(args)
            safe_args[path_key] = str(resolved)
            if name == "run_tests":
                return _call_with_cwd(self.work_dir, func, safe_args)
            return func(safe_args)

        return guarded


def make_guarded_tool_dispatch(
        work_dir: Path, dispatch: dict | None = None) -> GuardedToolDispatch:
    return GuardedToolDispatch(work_dir, dispatch or TOOL_DISPATCH)


def _call_with_cwd(directory: Path, func, *args):
    original = Path.cwd()
    os.chdir(directory)
    try:
        return func(*args)
    finally:
        os.chdir(original)


def run_hidden_tests(test_path: Path) -> dict:
    """Run scorer-only tests with their frozen 120 second timeout."""
    try:
        result = subprocess.run(
            [
                sys.executable,
                "-m",
                "pytest",
                str(test_path),
                "-v",
                "--tb=short",
                "-p",
                "no:cacheprovider",
            ],
            cwd=test_path.parent,
            capture_output=True,
            text=True,
            timeout=HIDDEN_TEST_TIMEOUT,
        )
        return {
            "returncode": result.returncode,
            "stdout": result.stdout,
            "stderr": result.stderr,
            "passed": result.returncode == 0,
        }
    except subprocess.TimeoutExpired:
        return {
            "returncode": -1,
            "stdout": "",
            "stderr": f"TIMEOUT: hidden tests exceeded {HIDDEN_TEST_TIMEOUT}s",
            "passed": False,
        }


def _pytest_counts(test_result: dict) -> tuple[int, int, bool]:
    output = test_result.get("stdout", "") + test_result.get("stderr", "")

    def count(label: str) -> int:
        matches = re.findall(rf"(?<!\w)(\d+)\s+{label}(?!\w)", output)
        return int(matches[-1]) if matches else 0

    failed = max(count("failed"), count("error"), count("errors"))
    errored = (
        test_result.get("returncode") in {-1, 2, 3, 4, 5}
        or "ERROR collecting" in output
        or "INTERNALERROR" in output
    )
    return count("passed"), failed, errored


def _gateway_error(error: str | None) -> bool:
    if not error:
        return False
    lowered = error.lower()
    markers = (
        "ratelimit",
        "rate limit",
        "status code: 429",
        "status code: 500",
        "status code: 502",
        "status code: 503",
        "status code: 504",
        "connectionerror",
        "connection error",
        "apiconnection",
    )
    return any(marker in lowered for marker in markers)


def _test_environment_error(test_result: dict) -> bool:
    _, _, errored = _pytest_counts(test_result)
    return errored


def _score_in_fresh_directory(work: Path, task_dir: Path) -> tuple[dict, dict]:
    with tempfile.TemporaryDirectory() as score_tmp:
        score_dir = Path(score_tmp)
        solution = work / "solution.py"
        if solution.exists():
            shutil.copy2(solution, score_dir / "solution.py")
        shutil.copy2(task_dir / "test_solution.py", score_dir / "test_solution.py")
        shutil.copy2(
            task_dir / "_hidden" / "test_hidden.py",
            score_dir / "test_hidden.py",
        )
        visible = _call_with_cwd(
            score_dir,
            run_tests,
            str(score_dir / "test_solution.py"),
        )
        hidden = run_hidden_tests(score_dir / "test_hidden.py")
    return visible, hidden


def main(harness_path: str, task_dir: str, out_file: str) -> None:
    config.load_env()
    task_dir = Path(task_dir)

    spec = importlib.util.spec_from_file_location("harness", harness_path)
    harness = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(harness)

    result = {
        "task": task_dir.name,
        "passed": False,
        "tampered": False,
        "steps": 0,
        "tokens": 0,
        "error": None,
        "visible_passed": False,
        "hidden": None,
        "category": None,
        "contract_violations": 0,
    }

    with tempfile.TemporaryDirectory() as tmp:
        work = Path(tmp)
        for f in task_dir.iterdir():
            if f.is_file():
                shutil.copy2(f, work / f.name)

        protected = {f.name: sha256(f) for f in work.iterdir() if f.name != "solution.py"}
        guarded_dispatch = make_guarded_tool_dispatch(work)

        t0 = time.time()
        try:
            trace = harness.run(
                str(work), TOOL_DEFINITIONS, guarded_dispatch
            )
            if not isinstance(trace, dict):
                raise TypeError("run() must return a dict")
            if (
                not isinstance(trace.get("steps"), int)
                or not isinstance(trace.get("tokens"), int)
                or not isinstance(trace.get("messages"), list)
            ):
                raise TypeError(
                    "run() must return steps:int, tokens:int, messages:list"
                )
            result["steps"] = trace.get("steps", 0)
            result["tokens"] = trace.get("tokens", 0)
            result["trace"] = trace.get("messages", [])
            if result["steps"] == 0 and result["tokens"] == 0:
                result["error"] = "invalid trace: 0 steps and 0 tokens"
        except Exception as e:
            result["error"] = f"harness crashed: {type(e).__name__}: {e}"
        result["contract_violations"] = guarded_dispatch.contract_violations
        result["elapsed"] = round(time.time() - t0, 1)

        # Integrity: everything except solution.py must be untouched.
        for name, digest in protected.items():
            f = work / name
            if not f.exists() or sha256(f) != digest:
                result["tampered"] = True
                shutil.copy2(task_dir / name, f)  # restore pristine copy
        for f in work.iterdir():
            if f.is_file() and f.name not in protected and f.name != "solution.py" and f.suffix == ".py":
                result["tampered"] = True  # injected python file — could shadow imports

        if result["tampered"]:
            result["category"] = "tampered"
        elif result["error"]:
            result["category"] = (
                "env_error" if _gateway_error(result["error"])
                else "harness_error"
            )
        else:
            hidden_path = task_dir / "_hidden" / "test_hidden.py"
            if hidden_path.exists():
                visible_result, hidden_result = _score_in_fresh_directory(
                    work, task_dir
                )
                n_passed, n_failed, hidden_errored = _pytest_counts(
                    hidden_result
                )
                result["visible_passed"] = visible_result["passed"]
                result["hidden"] = {
                    "passed": hidden_result["passed"],
                    "n_passed": n_passed,
                    "n_failed": n_failed,
                    "errored": hidden_errored,
                }
                result["test_output"] = (
                    visible_result["stdout"] + visible_result["stderr"]
                )[-2000:]
                if (
                    _test_environment_error(visible_result)
                    or hidden_errored
                ):
                    result["category"] = "env_error"
                else:
                    result["passed"] = hidden_result["passed"]
                    result["category"] = (
                        "passed" if result["passed"] else "capability"
                    )
            else:
                visible_result = _call_with_cwd(
                    work,
                    run_tests,
                    str(work / "test_solution.py"),
                )
                result["visible_passed"] = visible_result["passed"]
                result["test_output"] = (
                    visible_result["stdout"] + visible_result["stderr"]
                )[-2000:]
                if _test_environment_error(visible_result):
                    result["category"] = "env_error"
                else:
                    result["passed"] = visible_result["passed"]
                    result["category"] = (
                        "passed" if result["passed"] else "capability"
                    )

    Path(out_file).write_text(json.dumps(result, ensure_ascii=False, default=str))


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2], sys.argv[3])
