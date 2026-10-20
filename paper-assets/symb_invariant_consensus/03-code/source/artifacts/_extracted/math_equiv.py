"""Math answer equivalence checking for MATH-500 benchmarks."""
from __future__ import annotations

import re
import logging

logger = logging.getLogger(__name__)

try:
    from math_verify import parse as mv_parse, verify as mv_verify
    HAS_MATH_VERIFY = True
except ImportError:
    HAS_MATH_VERIFY = False

try:
    import sympy
    HAS_SYMPY = True
except ImportError:
    HAS_SYMPY = False


def normalize_answer(answer: str) -> str:
    if answer is None:
        return ""
    s = str(answer).strip()
    boxed = re.search(r'\\boxed\{(.+)\}', s)
    if boxed:
        s = boxed.group(1)
    s = s.replace('$', '').strip()
    s = s.replace('\\dfrac', '\\frac')
    s = s.replace('\\tfrac', '\\frac')
    s = s.replace('\\left', '').replace('\\right', '')
    s = s.replace('\\!', '').replace('\\,', '').replace('\\;', '').replace('\\ ', '')
    s = s.replace('\\cdot', '*').replace('\\times', '*').replace('\\div', '/')
    s = s.replace('^\\circ', '').replace('^{\\circ}', '').replace('°', '')
    s = re.sub(r'\s+', ' ', s).strip()
    return s


def _try_math_verify(pred: str, gt: str) -> bool | None:
    if not HAS_MATH_VERIFY:
        return None
    try:
        p = mv_parse(pred)
        g = mv_parse(gt)
        return mv_verify(p, g)
    except Exception:
        return None


def _try_sympy(pred: str, gt: str) -> bool | None:
    if not HAS_SYMPY:
        return None

    def _to_sympy(s: str):
        s2 = s
        while '\\frac' in s2:
            s2 = re.sub(r'\\frac\{([^{}]+)\}\{([^{}]+)\}', r'(\1)/(\2)', s2, count=1)
        s2 = re.sub(r'\\sqrt\{([^{}]+)\}', r'sqrt(\1)', s2)
        s2 = re.sub(r'\\sqrt\[(\d+)\]\{([^{}]+)\}', r'(\2)**(1/\1)', s2)
        s2 = s2.replace('\\pi', 'pi').replace('\\infty', 'oo')
        s2 = s2.replace('\\ln', 'log').replace('\\log', 'log')
        s2 = s2.replace('\\sin', 'sin').replace('\\cos', 'cos').replace('\\tan', 'tan')
        s2 = re.sub(r'\\[a-zA-Z]+', '', s2)
        s2 = s2.replace('{', '(').replace('}', ')')
        try:
            return sympy.sympify(s2)
        except Exception:
            return None

    sym_p = _to_sympy(pred)
    sym_g = _to_sympy(gt)
    if sym_p is None or sym_g is None:
        return None

    try:
        if sympy.simplify(sym_p - sym_g) == 0:
            return True
    except Exception:
        pass

    try:
        vp = complex(sym_p.evalf())
        vg = complex(sym_g.evalf())
        if abs(vp - vg) < 1e-6:
            return True
    except Exception:
        pass

    return False


def is_equiv(pred: str, gt: str) -> bool:
    if pred is None or gt is None:
        return False

    norm_p = normalize_answer(pred)
    norm_g = normalize_answer(gt)
    if norm_p == norm_g:
        return True

    # math_verify (best coverage)
    mv_result = _try_math_verify(norm_p, norm_g)
    if mv_result is True:
        return True

    # sympy fallback
    sy_result = _try_sympy(norm_p, norm_g)
    if sy_result is True:
        return True

    # numeric fallback
    try:
        if abs(float(norm_p) - float(norm_g)) < 1e-6:
            return True
    except (ValueError, TypeError):
        pass

    return False


def group_equivalent_answers(answers: list[str]) -> dict[str, list[int]]:
    groups: dict[str, list[int]] = {}
    for i, ans in enumerate(answers):
        if ans is None or str(ans).strip() == "":
            continue
        found = False
        for canonical in groups:
            if is_equiv(ans, canonical):
                groups[canonical].append(i)
                found = True
                break
        if not found:
            groups[ans] = [i]
    return groups
