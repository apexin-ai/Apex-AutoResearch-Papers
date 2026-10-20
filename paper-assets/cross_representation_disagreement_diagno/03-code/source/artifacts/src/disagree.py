"""
分歧检测器 + rule-based 错误分类器。
比较 FOL / Python code 两路执行结果，分类错误模式。
"""

from dataclasses import dataclass, asdict
from enum import Enum
from typing import Optional


# ---------------------------------------------------------------------------
# Enums
# ---------------------------------------------------------------------------

class AgreementType(str, Enum):
    AGREE_CORRECT = "agree_correct"
    AGREE_WRONG   = "agree_wrong"
    DISAGREE      = "disagree"
    SINGLE_ERROR  = "single_error"
    BOTH_ERROR    = "both_error"


class ErrorType(str, Enum):
    EXEC_CRASH         = "exec_crash"
    TIMEOUT            = "timeout"
    QUANTIFIER_ERROR   = "quantifier_error"
    NEGATION_ERROR     = "negation_error"
    CONSTRAINT_MISSING = "constraint_missing"
    CONSTRAINT_EXTRA   = "constraint_extra"
    TYPE_BOUNDARY      = "type_boundary"
    LOGIC_ERROR        = "logic_error"
    UNKNOWN            = "unknown"


# ---------------------------------------------------------------------------
# Result container
# ---------------------------------------------------------------------------

@dataclass
class DisagreementResult:
    agreement_type: str
    fol_verdict: str
    code_verdict: str
    ground_truth: str
    fol_correct: Optional[bool]
    code_correct: Optional[bool]
    error_type: Optional[str]
    error_side: Optional[str]      # "fol" / "code" / "both" / None

    def to_dict(self):
        return asdict(self)


# ---------------------------------------------------------------------------
# Detection
# ---------------------------------------------------------------------------

def detect_disagreement(
    fol_verdict: str,
    code_verdict: str,
    ground_truth: str,
) -> DisagreementResult:

    fol_err  = (fol_verdict == "Error")
    code_err = (code_verdict == "Error")

    if fol_err and code_err:
        return DisagreementResult(
            AgreementType.BOTH_ERROR, fol_verdict, code_verdict,
            ground_truth, None, None, ErrorType.EXEC_CRASH, "both",
        )

    if fol_err or code_err:
        side = "fol" if fol_err else "code"
        return DisagreementResult(
            AgreementType.SINGLE_ERROR, fol_verdict, code_verdict,
            ground_truth,
            None if fol_err else (fol_verdict == ground_truth),
            None if code_err else (code_verdict == ground_truth),
            ErrorType.EXEC_CRASH, side,
        )

    fol_ok  = (fol_verdict == ground_truth)
    code_ok = (code_verdict == ground_truth)

    if fol_verdict == code_verdict:
        if fol_ok:
            return DisagreementResult(
                AgreementType.AGREE_CORRECT, fol_verdict, code_verdict,
                ground_truth, True, True, None, None,
            )
        return DisagreementResult(
            AgreementType.AGREE_WRONG, fol_verdict, code_verdict,
            ground_truth, False, False, ErrorType.LOGIC_ERROR, "both",
        )

    error_side = (
        "fol"  if code_ok and not fol_ok else
        "code" if fol_ok and not code_ok else
        "both"
    )
    return DisagreementResult(
        AgreementType.DISAGREE, fol_verdict, code_verdict,
        ground_truth, fol_ok, code_ok, None, error_side,
    )


# ---------------------------------------------------------------------------
# Classification (rule-based heuristics)
# ---------------------------------------------------------------------------

_QUANTIFIER_WORDS = {
    "all", "every", "each", "some", "any",
    "no one", "nobody", "everyone", "someone",
    "whoever", "wherever", "anything", "everything",
}

_NEGATION_WORDS = {
    "not", "no ", "never", "neither", "nor",
    "cannot", "can't", "doesn't", "don't",
    "isn't", "aren't", "won't", "wouldn't",
}


def classify_error(
    fol_code: str,
    code_code: str,
    fol_verdict: str,
    code_verdict: str,
    fol_error: Optional[str],
    code_error: Optional[str],
    ground_truth: str,
    premises: str,
    conclusion: str,
) -> str:

    # 1. timeout / crash
    for err in (fol_error, code_error):
        if err and "timed out" in err.lower():
            return ErrorType.TIMEOUT
    if fol_error or code_error:
        return ErrorType.EXEC_CRASH

    text_lower = (premises + " " + conclusion).lower()

    # 2. quantifier
    has_quant = any(w in text_lower for w in _QUANTIFIER_WORDS)
    if has_quant:
        fol_has_q = ("ForAll" in fol_code or "Exists" in fol_code
                     or "forall" in fol_code or "exists" in fol_code)
        if not fol_has_q:
            return ErrorType.QUANTIFIER_ERROR

    # 3. negation
    has_neg = any(w in text_lower for w in _NEGATION_WORDS)
    if has_neg and fol_verdict != code_verdict:
        fol_neg = fol_code.lower().count("not")
        code_neg = code_code.lower().count("not")
        if abs(fol_neg - code_neg) > 2:
            return ErrorType.NEGATION_ERROR

    # 4. constraint count mismatch
    premise_sentences = max(premises.count("."), 1)
    fol_asserts = fol_code.count(".add(") + fol_code.count("solver.assert")
    if fol_asserts < premise_sentences * 0.5:
        return ErrorType.CONSTRAINT_MISSING

    # 5. type / boundary
    for te in ("TypeError", "ValueError", "IndexError", "KeyError"):
        if (fol_error and te in fol_error) or (code_error and te in str(code_error)):
            return ErrorType.TYPE_BOUNDARY

    if fol_verdict != code_verdict:
        return ErrorType.LOGIC_ERROR

    return ErrorType.UNKNOWN
