"""MATH answer extraction and comparison utilities.

Handles diverse formats: fractions, radicals, polynomials, etc.
Uses sympy for symbolic equivalence checking.
"""

import re
from typing import Optional


def extract_boxed_answer(text: str) -> Optional[str]:
    """Extract the last \\boxed{...} answer, handling nested braces."""
    if text is None:
        return None
    idx = text.rfind('\\boxed{')
    if idx == -1:
        idx = text.rfind('boxed{')
        if idx == -1:
            return None
        idx += 6
    else:
        idx += 7

    depth = 1
    end = idx
    while end < len(text) and depth > 0:
        if text[end] == '{':
            depth += 1
        elif text[end] == '}':
            depth -= 1
        end += 1

    if depth != 0:
        return None
    return text[idx:end - 1].strip()


def normalize_answer(answer: str) -> str:
    """Normalize a math answer string for comparison."""
    if answer is None:
        return ""
    answer = answer.strip()
    answer = answer.replace(" ", "")
    answer = answer.replace("\\,", "")
    answer = answer.replace("\\!", "")
    answer = answer.replace("\\;", "")
    answer = answer.replace("\\left", "")
    answer = answer.replace("\\right", "")
    answer = answer.replace("\\text{", "").rstrip("}")
    return answer


def answers_equal(pred: str, gold: str) -> bool:
    """Check if two math answers are equivalent."""
    if pred is None or gold is None:
        return False

    pred_norm = normalize_answer(pred)
    gold_norm = normalize_answer(gold)

    if pred_norm == gold_norm:
        return True

    try:
        if float(pred_norm) == float(gold_norm):
            return True
    except (ValueError, OverflowError):
        pass

    try:
        from sympy import simplify, sympify
        pred_sym = sympify(pred_norm)
        gold_sym = sympify(gold_norm)
        if simplify(pred_sym - gold_sym) == 0:
            return True
    except Exception:
        pass

    return False
