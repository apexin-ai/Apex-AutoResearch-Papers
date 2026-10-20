"""
定向修复 + 盲目重生成（对照组）。
对 disagreement 样本，对比"带诊断信息修复" vs "不带诊断信息重生成"的成功率。
"""

from dataclasses import dataclass, asdict
from typing import Optional, List

from formalize import (
    _call_llm, _extract_code,
    FOL_SYSTEM_PROMPT, CODE_SYSTEM_PROMPT,
)
from executor import execute_code
from config import MAX_REPAIR_ROUNDS

# ---------------------------------------------------------------------------
# Prompt templates
# ---------------------------------------------------------------------------

TARGETED_REPAIR_PROMPT = """\
The following {repr_type} code was generated for a logical reasoning problem
but produced an INCORRECT result.

## Problem
Premises:
{premises}

Conclusion:
{conclusion}

## Your previous code
```python
{original_code}
```

## Diagnostic information
- Your verdict: {wrong_verdict}
- The other representation ({other_type}) got: {other_verdict}
- Identified error pattern: {error_type}
{hint}

Fix the code. Output ONLY the corrected script in a ```python``` block.
Print exactly one word: True, False, or Unknown."""


BLIND_REGEN_PROMPT = """\
The following {repr_type} code was generated for a logical reasoning problem
but may be incorrect. Regenerate a correct solution from scratch.

## Problem
Premises:
{premises}

Conclusion:
{conclusion}

Output ONLY a complete Python script in a ```python``` block.
Print exactly one word: True, False, or Unknown."""

# ---------------------------------------------------------------------------
# Hints per error type
# ---------------------------------------------------------------------------

_HINTS = {
    "quantifier_error":   "Check that every universal/existential quantifier in the premises is encoded.",
    "negation_error":     "Check that all negations (not, no, never …) are handled correctly.",
    "constraint_missing": "Some premises may not be encoded. Ensure every premise is represented.",
    "constraint_extra":   "There may be extra constraints not in the premises. Remove them.",
    "type_boundary":      "There may be a type or index error in the code.",
    "timeout":            "The code timed out — simplify the approach.",
}


# ---------------------------------------------------------------------------
# Result container
# ---------------------------------------------------------------------------

@dataclass
class RepairResult:
    method: str          # "targeted" / "blind"
    round_num: int
    new_code: str
    exec_result: dict
    verdict: str
    success: bool
    raw_response: str

    def to_dict(self):
        return asdict(self)


# ---------------------------------------------------------------------------
# Repair functions
# ---------------------------------------------------------------------------

def targeted_repair(
    premises: str,
    conclusion: str,
    original_code: str,
    wrong_verdict: str,
    other_verdict: str,
    error_type: str,
    error_msg: Optional[str],
    repr_type: str,          # "FOL (Z3)" / "Python code"
    ground_truth: str,
    max_rounds: int = MAX_REPAIR_ROUNDS,
) -> List[RepairResult]:

    other_type = "Python code" if "FOL" in repr_type else "FOL (Z3)"
    system = FOL_SYSTEM_PROMPT if "FOL" in repr_type else CODE_SYSTEM_PROMPT

    hint_text = _HINTS.get(error_type, "")
    if error_type == "exec_crash":
        hint_text = (
            "Your code crashed during execution. "
            f"The other representation produced: {other_verdict}. "
            "Rewrite from scratch with correct syntax and API usage."
        )
    hint = f"- Hint: {hint_text}" if hint_text else ""

    results: List[RepairResult] = []
    cur_code = original_code
    cur_verdict = wrong_verdict

    for rnd in range(1, max_rounds + 1):
        prompt = TARGETED_REPAIR_PROMPT.format(
            repr_type=repr_type,
            premises=premises,
            conclusion=conclusion,
            original_code=cur_code,
            wrong_verdict=cur_verdict,
            other_type=other_type,
            other_verdict=other_verdict,
            error_type=error_type,
            hint=hint,
        )

        raw = _call_llm(system, prompt)
        new_code = _extract_code(raw)
        ex = execute_code(new_code)
        ok = ex.verdict == ground_truth

        results.append(RepairResult(
            method="targeted", round_num=rnd,
            new_code=new_code, exec_result=ex.to_dict(),
            verdict=ex.verdict, success=ok, raw_response=raw,
        ))

        if ok:
            break
        cur_code = new_code
        cur_verdict = ex.verdict

    return results


def blind_regeneration(
    premises: str,
    conclusion: str,
    repr_type: str,
    ground_truth: str,
    max_rounds: int = MAX_REPAIR_ROUNDS,
) -> List[RepairResult]:

    system = FOL_SYSTEM_PROMPT if "FOL" in repr_type else CODE_SYSTEM_PROMPT
    results: List[RepairResult] = []

    for rnd in range(1, max_rounds + 1):
        prompt = BLIND_REGEN_PROMPT.format(
            repr_type=repr_type,
            premises=premises,
            conclusion=conclusion,
        )

        raw = _call_llm(system, prompt)
        new_code = _extract_code(raw)
        ex = execute_code(new_code)
        ok = ex.verdict == ground_truth

        results.append(RepairResult(
            method="blind", round_num=rnd,
            new_code=new_code, exec_result=ex.to_dict(),
            verdict=ex.verdict, success=ok, raw_response=raw,
        ))

        if ok:
            break

    return results
