"""Validate generated test cases against solution and buggy code.

For each sample:
  - solution + test_code → must PASS (pytest exit 0)
  - buggy_code + test_code → must FAIL (pytest exit != 0)
Only samples where both conditions hold are kept.

Input: data/debugbench_with_tests.jsonl
Output: data/debugbench_validated.jsonl
Dependencies: pytest (in venv)
"""

import argparse
import json
import logging
import subprocess
import tempfile
from pathlib import Path

logger = logging.getLogger(__name__)

TYPING_IMPORTS = """from typing import List, Optional, Dict, Tuple, Set
from collections import defaultdict, Counter, deque
"""


def run_pytest(code: str, test_code: str, timeout: int = 10) -> tuple[bool, str]:
    """Run test_code against code. Returns (passed, output)."""
    combined = build_test_file(code, test_code)
    with tempfile.NamedTemporaryFile(
        mode="w", suffix=".py", delete=False, prefix="dbtest_"
    ) as f:
        f.write(combined)
        f.flush()
        tmp_path = f.name

    try:
        result = subprocess.run(
            ["python", "-m", "pytest", tmp_path, "-x", "-q", "--tb=short", "--no-header"],
            capture_output=True,
            text=True,
            timeout=timeout,
        )
        return result.returncode == 0, result.stdout + result.stderr
    except subprocess.TimeoutExpired:
        return False, "TIMEOUT"
    finally:
        Path(tmp_path).unlink(missing_ok=True)


def clean_test_code(test_code: str) -> str:
    """Clean LLM-generated test code: strip markdown fences, Solution class, stale imports."""
    import re
    code = re.sub(r"^```(?:python)?\s*\n?", "", test_code.strip())
    code = re.sub(r"\n?```\s*$", "", code)
    code = re.sub(r"^\s*from solution import Solution\s*$", "", code, flags=re.MULTILINE)
    code = re.sub(r"^\s*import solution\s*$", "", code, flags=re.MULTILINE)

    lines = code.split("\n")
    result = []
    in_solution = False
    for line in lines:
        stripped = line.strip()
        if not in_solution:
            if stripped.startswith("class Solution:") or stripped.startswith("class Solution("):
                in_solution = True
                continue
            result.append(line)
        else:
            if stripped == "" or line[0] in (" ", "\t"):
                continue
            in_solution = False
            result.append(line)
    return "\n".join(result)


def build_test_file(code_under_test: str, test_code: str) -> str:
    """Build test file: typing imports + code_under_test + test functions (Solution stripped)."""
    cleaned = clean_test_code(test_code)
    return TYPING_IMPORTS + "\n" + code_under_test + "\n\n" + cleaned


def main():
    parser = argparse.ArgumentParser(
        description="Validate test cases: solution must pass, buggy code must fail"
    )
    parser.add_argument(
        "--input",
        type=str,
        default="data/debugbench_with_tests.jsonl",
        help="Input JSONL with test_code field",
    )
    parser.add_argument(
        "--output",
        type=str,
        default="data/debugbench_validated.jsonl",
        help="Output JSONL (only validated samples)",
    )
    parser.add_argument(
        "--timeout", type=int, default=10, help="Timeout per test run in seconds"
    )
    parser.add_argument("--verbose", action="store_true", help="Enable debug logging")
    args = parser.parse_args()

    logging.basicConfig(
        level=logging.DEBUG if args.verbose else logging.INFO,
        format="%(asctime)s %(levelname)s %(message)s",
    )

    input_path = Path(args.input)
    output_path = Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    samples = []
    with open(input_path) as f:
        for line in f:
            samples.append(json.loads(line))
    logger.info(f"Loaded {len(samples)} samples")

    validated = []
    stats = {"solution_pass": 0, "buggy_fail": 0, "both_correct": 0, "total": 0}

    for i, sample in enumerate(samples):
        stats["total"] += 1
        slug = sample["slug"]
        test_code = sample["test_code"]

        sol_pass, sol_out = run_pytest(sample["solution"], test_code, args.timeout)

        if sol_pass:
            stats["solution_pass"] += 1
        else:
            logger.debug(f"[{slug}] Solution FAILED: {sol_out[:200]}")
            continue

        bug_pass, bug_out = run_pytest(sample["buggy_code"], test_code, args.timeout)
        buggy_fail = not bug_pass

        if buggy_fail:
            stats["buggy_fail"] += 1
            stats["both_correct"] += 1
            validated.append(sample)
        else:
            logger.debug(f"[{slug}] Buggy code unexpectedly PASSED")

        if (i + 1) % 50 == 0:
            logger.info(
                f"Progress: {i+1}/{len(samples)}, validated: {len(validated)}"
            )

    with open(output_path, "w") as f:
        for row in validated:
            f.write(json.dumps(row, ensure_ascii=False) + "\n")

    total = stats["total"]
    print(f"\n=== Validation Results ===")
    print(f"Total samples: {total}")
    print(f"Solution pass: {stats['solution_pass']} ({stats['solution_pass']/total*100:.1f}%)")
    print(f"Buggy fail:    {stats['buggy_fail']} ({stats['buggy_fail']/total*100:.1f}%)")
    print(f"Both correct:  {stats['both_correct']} ({stats['both_correct']/total*100:.1f}%)")
    print(f"Output: {output_path} ({len(validated)} samples)")


if __name__ == "__main__":
    main()
