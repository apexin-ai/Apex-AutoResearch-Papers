"""Sandboxed code execution for probe testing and test validation.

Input: Python code strings (probes, buggy code, test code).
Output: ExecutionResult / TestResult with stdout, stderr, pass/fail info.
Dependencies: subprocess (stdlib)
"""

import re
import resource
import subprocess
import tempfile
import textwrap
import time
from dataclasses import dataclass
from pathlib import Path


@dataclass
class ExecutionResult:
    success: bool
    stdout: str
    stderr: str
    return_code: int
    execution_time: float


@dataclass
class TestResult:
    passed: bool
    num_passed: int
    num_failed: int
    output: str


_COMMON_PREAMBLE = """\
from typing import List, Optional, Dict, Tuple, Set, Deque
from collections import defaultdict, Counter, deque
import math, bisect, heapq, itertools, functools

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
"""


def _add_preamble(code: str) -> str:
    """Prepend common imports/definitions if missing from the top of the code."""
    first_lines = "\n".join(code.split("\n")[:5])
    if "from typing import" in first_lines or "import typing" in first_lines:
        return code
    return _COMMON_PREAMBLE + "\n" + code


def execute_code(code: str, timeout: int = 5) -> ExecutionResult:
    """Execute Python code in a subprocess with resource limits.

    Args:
        code: Python source code to execute.
        timeout: Maximum execution time in seconds.

    Returns:
        ExecutionResult with captured output and status.
    """
    code = _add_preamble(code)
    with tempfile.NamedTemporaryFile(
        mode="w", suffix=".py", delete=False
    ) as f:
        f.write(code)
        f.flush()
        tmp_path = f.name

    def _set_limits():
        # 512MB memory limit
        resource.setrlimit(resource.RLIMIT_AS, (512 * 1024 * 1024, 512 * 1024 * 1024))

    start = time.monotonic()
    try:
        result = subprocess.run(
            ["python3", tmp_path],
            capture_output=True,
            text=True,
            timeout=timeout,
            preexec_fn=_set_limits,
        )
        elapsed = time.monotonic() - start
        return ExecutionResult(
            success=result.returncode == 0,
            stdout=result.stdout,
            stderr=result.stderr,
            return_code=result.returncode,
            execution_time=elapsed,
        )
    except subprocess.TimeoutExpired:
        elapsed = time.monotonic() - start
        return ExecutionResult(
            success=False,
            stdout="",
            stderr=f"Timeout after {timeout}s",
            return_code=-1,
            execution_time=elapsed,
        )
    except Exception as e:
        elapsed = time.monotonic() - start
        return ExecutionResult(
            success=False,
            stdout="",
            stderr=str(e),
            return_code=-1,
            execution_time=elapsed,
        )
    finally:
        Path(tmp_path).unlink(missing_ok=True)


def _extract_snippet_from_comment(comment: str) -> str | None:
    """Pull a searchable code snippet from an INSERT comment."""
    # Quoted: '...' or "..." or `...`
    m = re.search(r"['\"`]([^'\"`]{3,})['\"`]", comment)
    if m:
        return m.group(1).strip()
    # After colon: "LINE: for j in range(...)"
    m = re.search(r"LINE[:\s]+(.{5,})", comment, re.IGNORECASE)
    if m:
        snippet = m.group(1).strip()
        # Remove trailing parenthetical descriptions
        snippet = re.sub(r"\s*\((?:the|after|before|inside|first|second).*$", "", snippet, flags=re.IGNORECASE)
        return snippet.strip() if len(snippet.strip()) >= 3 else None
    return None


def _parse_insertion_comment(
    probe_lines: list[str], code_lines: list[str] | None = None
) -> tuple[list[str], int | None]:
    """Extract insertion target from probe comments.

    Supports:
    1. '# INSERT AFTER LINE 5' — numeric line reference
    2. '# INSERT AFTER LINE: <code>' — content-based reference
    3. '# INSERT AT TOP OF FILE' — top insertion
    """
    clean_lines = []
    target_line = None
    for pl in probe_lines:
        # Format 1: numeric line number
        m = re.match(r"^\s*#\s*INSERT\s+(AFTER|BEFORE)\s+LINE\s+(\d+)", pl, re.IGNORECASE)
        if m:
            offset = 0 if m.group(1).upper() == "AFTER" else -1
            target_line = int(m.group(2)) + offset
            continue
        # "INSERT AT TOP OF FILE"
        if re.match(r"^\s*#\s*INSERT\s+AT\s+TOP", pl, re.IGNORECASE):
            target_line = 0
            continue
        # Format 2: content-based reference
        m2 = re.match(r"^\s*#\s*INSERT\s+(AFTER|BEFORE)\s+", pl, re.IGNORECASE)
        if m2 and code_lines is not None:
            direction = m2.group(1).upper()
            snippet = _extract_snippet_from_comment(pl)
            if snippet:
                for idx, cl in enumerate(code_lines):
                    if snippet in cl or snippet in cl.strip():
                        target_line = idx + (1 if direction == "AFTER" else 0)
                        break
            if target_line is not None:
                continue
        # "INSERT BEFORE THE RETURN LINE" — semantic
        if re.match(r"^\s*#\s*INSERT\s+BEFORE\s+THE\s+RETURN", pl, re.IGNORECASE) and code_lines:
            for idx in range(len(code_lines) - 1, -1, -1):
                if code_lines[idx].strip().startswith("return "):
                    target_line = idx
                    break
            if target_line is not None:
                continue
        # Generic INSERT comment — skip it
        if re.match(r"^\s*#\s*INSERT\s+", pl, re.IGNORECASE):
            continue
        clean_lines.append(pl)
    return clean_lines, target_line


def _insert_probe(buggy_code: str, probe: str) -> str:
    """Insert probe code into buggy_code at the best location.

    Strategy:
    1. If probe contains '# INSERT AFTER LINE N', insert at that line.
    2. Otherwise, insert after the first method def (skip class-level defs).
    3. Falls back to prepending if nothing matches.
    """
    lines = buggy_code.split("\n")
    raw_probe_lines = textwrap.dedent(probe).strip().split("\n")
    probe_lines, target_line = _parse_insertion_comment(raw_probe_lines, code_lines=lines)

    if not probe_lines:
        probe_lines = raw_probe_lines

    # Re-dedent after stripping INSERT comments (they had 0 indent, blocking dedent)
    probe_text = textwrap.dedent("\n".join(probe_lines)).strip()
    probe_lines = probe_text.split("\n") if probe_text else probe_lines

    # Strategy 1: explicit line number from probe comment
    if target_line is not None:
        insert_idx = min(target_line, len(lines))
        insert_idx = max(0, insert_idx)
        if insert_idx < len(lines):
            indent_match = re.match(r"^(\s*)", lines[min(insert_idx, len(lines) - 1)])
            body_indent = indent_match.group(1) if indent_match else ""
        else:
            body_indent = ""
        indented_probe = [body_indent + pl for pl in probe_lines]
        lines = lines[:insert_idx] + indented_probe + lines[insert_idx:]
        return "\n".join(lines)

    # Strategy 2: find first method def (indented def, i.e. inside a class)
    for i, line in enumerate(lines):
        if re.match(r"^(\s+)def ", line):
            indent_match = re.match(r"^(\s*)", line)
            base_indent = indent_match.group(1) if indent_match else ""
            body_indent = base_indent + "    "

            insert_idx = i + 1
            if insert_idx < len(lines):
                stripped = lines[insert_idx].strip()
                if stripped.startswith(('"""', "'''")):
                    if stripped.count('"""') >= 2 or stripped.count("'''") >= 2:
                        insert_idx += 1
                    else:
                        quote = stripped[:3]
                        for j in range(insert_idx + 1, len(lines)):
                            if quote in lines[j]:
                                insert_idx = j + 1
                                break

            indented_probe = [body_indent + pl for pl in probe_lines]
            lines = lines[:insert_idx] + indented_probe + lines[insert_idx:]
            return "\n".join(lines)

    # Strategy 3: find any def (top-level functions)
    for i, line in enumerate(lines):
        if re.match(r"^def ", line):
            body_indent = "    "
            insert_idx = i + 1
            if insert_idx < len(lines):
                stripped = lines[insert_idx].strip()
                if stripped.startswith(('"""', "'''")):
                    if stripped.count('"""') >= 2 or stripped.count("'''") >= 2:
                        insert_idx += 1
                    else:
                        quote = stripped[:3]
                        for j in range(insert_idx + 1, len(lines)):
                            if quote in lines[j]:
                                insert_idx = j + 1
                                break
            indented_probe = [body_indent + pl for pl in probe_lines]
            lines = lines[:insert_idx] + indented_probe + lines[insert_idx:]
            return "\n".join(lines)

    # Fallback: prepend probe
    return probe + "\n" + buggy_code


def execute_probe(
    buggy_code: str, probe: str, test_code: str | None = None, timeout: int = 5
) -> ExecutionResult:
    """Insert probe into buggy_code and execute.

    Args:
        buggy_code: The buggy source code.
        probe: Diagnostic probe code (print/assert statements).
        test_code: Optional test code that calls the methods (triggers probe execution).
        timeout: Maximum execution time in seconds.

    Returns:
        ExecutionResult from running the instrumented code.
    """
    instrumented = _insert_probe(buggy_code, probe)
    if test_code:
        # Append test code with a runner that calls test functions.
        # Wrap in try/except so assertion failures don't mask probe output.
        instrumented += "\n\n" + test_code + "\n\n"
        instrumented += (
            "if __name__ == '__main__':\n"
            "    for _n, _f in list(globals().items()):\n"
            "        if _n.startswith('test_') and callable(_f):\n"
            "            try:\n"
            "                _f()\n"
            "            except Exception:\n"
            "                pass\n"
        )
    return execute_code(instrumented, timeout=timeout)


def run_tests(
    code: str, test_code: str, timeout: int = 10
) -> TestResult:
    """Combine solution code with test code and run via pytest.

    Args:
        code: The solution/fixed code to test.
        test_code: pytest test code (test functions).
        timeout: Maximum execution time in seconds.

    Returns:
        TestResult with pass/fail counts.
    """
    combined = _add_preamble(code + "\n\n" + test_code)

    with tempfile.NamedTemporaryFile(
        mode="w", suffix=".py", delete=False
    ) as f:
        f.write(combined)
        f.flush()
        tmp_path = f.name

    try:
        result = subprocess.run(
            ["python3", "-m", "pytest", tmp_path, "-v", "--tb=short", "-q"],
            capture_output=True,
            text=True,
            timeout=timeout,
        )
        output = result.stdout + result.stderr

        # Parse pytest output for pass/fail counts
        num_passed = 0
        num_failed = 0
        for line in output.split("\n"):
            match = re.search(r"(\d+) passed", line)
            if match:
                num_passed = int(match.group(1))
            match = re.search(r"(\d+) failed", line)
            if match:
                num_failed = int(match.group(1))

        return TestResult(
            passed=(result.returncode == 0),
            num_passed=num_passed,
            num_failed=num_failed,
            output=output,
        )
    except subprocess.TimeoutExpired:
        return TestResult(
            passed=False,
            num_passed=0,
            num_failed=0,
            output=f"Timeout after {timeout}s",
        )
    finally:
        Path(tmp_path).unlink(missing_ok=True)
