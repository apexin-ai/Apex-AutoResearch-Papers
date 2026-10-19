"""Import 12 QuixBugs programs as bugfix validation tasks (benchmarks/bugfix/val)."""

import json
import urllib.request
from pathlib import Path

RAW = "https://raw.githubusercontent.com/jkoppel/QuixBugs/master"
OUT = Path(__file__).resolve().parent.parent / "benchmarks" / "bugfix" / "val"

# Chosen: deterministic I/O, JSON-friendly args/returns, no graph-node fixtures.
PROGRAMS = [
    "gcd", "bitcount", "get_factors", "bucketsort", "find_first_in_sorted",
    "kth", "longest_common_subsequence", "max_sublist_sum", "mergesort",
    "next_palindrome", "pascal", "rpn_eval",
]

TEST_TEMPLATE = '''import json
from pathlib import Path

import pytest

import solution

pytestmark = pytest.mark.timeout(3)

CASES = json.loads((Path(__file__).parent / "cases.json").read_text())


@pytest.mark.parametrize("case", CASES)
def test_case(case):
    args, expected = case
    result = getattr(solution, "{name}")(*args)
    if isinstance(result, tuple):
        result = list(result)
    assert result == expected
'''


def fetch(url: str) -> str:
    with urllib.request.urlopen(url, timeout=30) as r:
        return r.read().decode()


def main() -> None:
    for name in PROGRAMS:
        try:
            raw = fetch(f"{RAW}/json_testcases/{name}.json")
        except Exception as e:
            print(f"SKIP {name}: {e}")
            continue
        cases = []
        for line in raw.splitlines():
            line = line.strip()
            if not line:
                continue
            args, expected = json.loads(line)
            if not isinstance(args, list):
                args = [args]
            cases.append([args, expected])
        src = fetch(f"{RAW}/python_programs/{name}.py")
        task_dir = OUT / name
        task_dir.mkdir(parents=True, exist_ok=True)
        (task_dir / "solution.py").write_text(src)
        (task_dir / "cases.json").write_text(json.dumps(cases))
        (task_dir / "test_solution.py").write_text(TEST_TEMPLATE.format(name=name))
        print(f"OK {name}: {len(cases)} cases")


if __name__ == "__main__":
    main()
