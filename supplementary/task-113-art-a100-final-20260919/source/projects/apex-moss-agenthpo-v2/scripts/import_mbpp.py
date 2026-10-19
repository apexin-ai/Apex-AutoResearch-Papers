"""Import 12 MBPP problems as tddgen validation tasks (benchmarks/tddgen/val).

MBPP gives a natural-language description + assert-style tests; solution.py is a
stub with the description as a docstring and the function name from the asserts.
"""

import json
import re
import urllib.request
from pathlib import Path

URL = "https://raw.githubusercontent.com/google-research/google-research/master/mbpp/mbpp.jsonl"
OUT = Path(__file__).resolve().parent.parent / "benchmarks" / "tddgen" / "val"

# From the conventional test slice (ids 11-510): deterministic asserts, no setup code.
CHOSEN = [12, 14, 18, 56, 57, 63, 64, 67, 68, 72, 74, 77]

TEST_TEMPLATE = '''import pytest

from solution import *  # noqa: F401,F403

pytestmark = pytest.mark.timeout(10)

{tests}
'''


def main() -> None:
    with urllib.request.urlopen(URL, timeout=60) as r:
        problems = {json.loads(l)["task_id"]: json.loads(l) for l in r.read().decode().splitlines() if l.strip()}

    for tid in CHOSEN:
        p = problems[tid]
        m = re.search(r"assert\s+(\w+)\s*\(", p["test_list"][0])
        fn = m.group(1)
        name = f"mbpp_{tid:03d}"
        task_dir = OUT / name
        task_dir.mkdir(parents=True, exist_ok=True)

        stub = f'def {fn}(*args):\n    """{p["text"].strip()}"""\n    pass\n'
        (task_dir / "solution.py").write_text(stub)

        tests = "\n\n".join(
            f"def test_case_{i}():\n    {t.strip()}" for i, t in enumerate(p["test_list"])
        )
        (task_dir / "test_solution.py").write_text(TEST_TEMPLATE.format(tests=tests))
        print(f"OK {name} ({fn})")


if __name__ == "__main__":
    main()
