"""Import five dependency-light BigCodeBench-Hard tasks for difficulty calibration.

The selection is frozen from bigcode/bigcodebench-hard v0.1.4: choose tasks whose
declared libraries are available in the pilot environment, whose tests avoid
persistent external side effects, and which span several practical task shapes.

The official canonical solution is used only for an import-time oracle check and is
never written into benchmarks/.
"""

import argparse
import ast
import json
import subprocess
import sys
import tempfile
import urllib.parse
import urllib.request
from pathlib import Path

DATASET = "bigcode/bigcodebench-hard"
CONFIG = "default"
SPLIT = "v0.1.4"
CHOSEN = [
    "BigCodeBench/273",
    "BigCodeBench/274",
    "BigCodeBench/854",
    "BigCodeBench/928",
    "BigCodeBench/990",
]
OUT = (
    Path(__file__).resolve().parent.parent
    / "benchmarks"
    / "tddgen_hard"
    / "canary"
)
MANIFEST = OUT / "_manifest.json"

TEST_TEMPLATE = """import pytest

from solution import *  # noqa: F401,F403

pytestmark = pytest.mark.timeout(20)

{tests}
"""


def fetch_rows() -> list[dict]:
    rows = []
    for offset, length in ((0, 100), (100, 48)):
        params = urllib.parse.urlencode({
            "dataset": DATASET,
            "config": CONFIG,
            "split": SPLIT,
            "offset": offset,
            "length": length,
        })
        url = f"https://datasets-server.huggingface.co/rows?{params}"
        with urllib.request.urlopen(url, timeout=60) as response:
            payload = json.loads(response.read().decode())
        rows.extend(item["row"] for item in payload["rows"])
    return rows


def select_rows(rows: list[dict]) -> list[dict]:
    by_id = {row["task_id"]: row for row in rows}
    missing = [task_id for task_id in CHOSEN if task_id not in by_id]
    if missing:
        raise ValueError(f"dataset is missing frozen task(s): {missing}")
    return [by_id[task_id] for task_id in CHOSEN]


def build_solution(row: dict, *, oracle: bool = False) -> str:
    prefix = row["code_prompt"].lstrip().rstrip()
    if oracle:
        body = row["canonical_solution"].rstrip()
    else:
        body = f"    {row['instruct_prompt'].strip()!r}\n    pass"
    return f"{prefix}\n{body}\n"


def build_test(row: dict) -> str:
    tests = "\n".join(
        line.rstrip() for line in row["test"].lstrip().rstrip().splitlines()
    )
    return TEST_TEMPLATE.format(tests=tests)


def run_pytest(solution: str, tests: str) -> subprocess.CompletedProcess:
    with tempfile.TemporaryDirectory() as tmp:
        work = Path(tmp)
        (work / "solution.py").write_text(solution)
        (work / "test_solution.py").write_text(tests)
        return subprocess.run(
            [
                sys.executable,
                "-m",
                "pytest",
                str(work / "test_solution.py"),
                "-q",
                "-p",
                "no:cacheprovider",
                "--timeout=30",
            ],
            cwd=work,
            capture_output=True,
            text=True,
            timeout=120,
        )


def validate_row(row: dict) -> None:
    tests = build_test(row)
    stub_result = run_pytest(build_solution(row), tests)
    if stub_result.returncode == 0:
        raise ValueError(f"{row['task_id']}: stub unexpectedly passes")
    oracle_result = run_pytest(build_solution(row, oracle=True), tests)
    if oracle_result.returncode != 0:
        output = (oracle_result.stdout + oracle_result.stderr)[-2000:]
        raise ValueError(f"{row['task_id']}: oracle fails\n{output}")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--skip-validation",
        action="store_true",
        help="write tasks without running stub/oracle checks",
    )
    args = parser.parse_args()

    selected = select_rows(fetch_rows())
    OUT.mkdir(parents=True, exist_ok=True)
    manifest = {
        "dataset": DATASET,
        "split": SPLIT,
        "selection": CHOSEN,
        "selection_rule": (
            "dependency-light, no persistent external side effects, practical "
            "task-shape coverage; frozen before canary execution"
        ),
        "tasks": [],
    }
    for row in selected:
        if not args.skip_validation:
            validate_row(row)
        name = row["task_id"].replace("/", "_").lower()
        task_dir = OUT / name
        task_dir.mkdir(parents=True, exist_ok=True)
        (task_dir / "solution.py").write_text(build_solution(row))
        (task_dir / "test_solution.py").write_text(build_test(row))
        manifest["tasks"].append({
            "task_id": row["task_id"],
            "name": name,
            "entry_point": row["entry_point"],
            "score": row["score"],
            "libs": (
                ast.literal_eval(row["libs"])
                if isinstance(row["libs"], str) else row["libs"]
            ),
        })
        print(f"OK {name} (official score={row['score']:.4f})")

    MANIFEST.write_text(json.dumps(manifest, indent=2) + "\n")


if __name__ == "__main__":
    main()
