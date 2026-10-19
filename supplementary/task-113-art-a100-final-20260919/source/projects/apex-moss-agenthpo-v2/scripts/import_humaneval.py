"""Import 10 HumanEval problems as tddgen training tasks (benchmarks/tddgen/train).

solution.py = signature + docstring + pass (stub); test_solution.py = official checks.
"""

import gzip
import io
import json
import urllib.request
from pathlib import Path

URL = "https://github.com/openai/human-eval/raw/master/data/HumanEval.jsonl.gz"
OUT = Path(__file__).resolve().parent.parent / "benchmarks" / "tddgen" / "train"

# First 10 problems with deterministic, self-contained checks (skip float-tolerance ones).
CHOSEN = ["HumanEval/2", "HumanEval/5", "HumanEval/7", "HumanEval/8", "HumanEval/11",
          "HumanEval/12", "HumanEval/16", "HumanEval/22", "HumanEval/27", "HumanEval/29"]

TEST_TEMPLATE = '''import pytest

from solution import {entry} as candidate

pytestmark = pytest.mark.timeout(10)

{check_code}

def test_solution():
    check(candidate)
'''


def main() -> None:
    with urllib.request.urlopen(URL, timeout=60) as r:
        data = gzip.GzipFile(fileobj=io.BytesIO(r.read())).read().decode()

    problems = {json.loads(l)["task_id"]: json.loads(l) for l in data.splitlines() if l.strip()}

    for tid in CHOSEN:
        p = problems[tid]
        name = tid.replace("/", "_").lower()
        task_dir = OUT / name
        task_dir.mkdir(parents=True, exist_ok=True)
        stub = p["prompt"].rstrip() + "\n    pass\n"
        (task_dir / "solution.py").write_text(stub)
        (task_dir / "test_solution.py").write_text(
            TEST_TEMPLATE.format(entry=p["entry_point"], check_code=p["test"].strip())
        )
        print(f"OK {name} ({p['entry_point']})")


if __name__ == "__main__":
    main()
