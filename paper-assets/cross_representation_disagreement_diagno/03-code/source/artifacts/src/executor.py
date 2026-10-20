"""
安全代码执行器。
沙箱执行 Z3 / Python 代码，超时保护 + 异常捕获。
"""

import io
import signal
import traceback
from contextlib import redirect_stdout, redirect_stderr
from dataclasses import dataclass, asdict
from typing import Optional

from config import EXEC_TIMEOUT


class ExecutionTimeout(Exception):
    pass


def _alarm_handler(signum, frame):
    raise ExecutionTimeout("Execution timed out")


@dataclass
class ExecResult:
    output: str
    error: Optional[str]
    verdict: str              # "True" / "False" / "Unknown" / "Error"
    timed_out: bool

    def to_dict(self):
        return asdict(self)


def _parse_verdict(output: str) -> str:
    lines = [l.strip() for l in output.strip().splitlines() if l.strip()]
    if not lines:
        return "Error"

    last = lines[-1].lower()
    if last in ("true", "entailed"):
        return "True"
    if last in ("false", "contradicted"):
        return "False"
    if last in ("unknown", "neutral", "uncertain"):
        return "Unknown"
    return "Error"


def execute_code(code: str, timeout: int = EXEC_TIMEOUT) -> ExecResult:
    stdout_buf = io.StringIO()
    stderr_buf = io.StringIO()

    prev_handler = signal.signal(signal.SIGALRM, _alarm_handler)
    signal.alarm(timeout)

    try:
        with redirect_stdout(stdout_buf), redirect_stderr(stderr_buf):
            exec(code, {"__builtins__": __builtins__})

        output = stdout_buf.getvalue()
        return ExecResult(
            output=output,
            error=None,
            verdict=_parse_verdict(output),
            timed_out=False,
        )

    except ExecutionTimeout:
        return ExecResult(
            output=stdout_buf.getvalue(),
            error="Execution timed out",
            verdict="Error",
            timed_out=True,
        )
    except Exception as e:
        return ExecResult(
            output=stdout_buf.getvalue(),
            error=f"{type(e).__name__}: {e}\n{traceback.format_exc()}",
            verdict="Error",
            timed_out=False,
        )
    finally:
        signal.alarm(0)
        signal.signal(signal.SIGALRM, prev_handler)


def execute_with_syntax_fix(
    code: str,
    fix_fn=None,
    timeout: int = EXEC_TIMEOUT,
) -> tuple:
    """Execute code; on crash, call fix_fn once to attempt syntax repair.

    Returns (ExecResult, fixed_code_or_None).
    fix_fn signature: fix_fn(code: str, error: str) -> str | None
    """
    result = execute_code(code, timeout)
    if result.error and not result.timed_out and fix_fn is not None:
        fixed_code = fix_fn(code, result.error)
        if fixed_code and fixed_code.strip() != code.strip():
            result = execute_code(fixed_code, timeout)
            return result, fixed_code
    return result, None
