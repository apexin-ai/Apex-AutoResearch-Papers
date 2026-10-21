"""MATH dataset answer extraction and comparison utilities."""
from __future__ import annotations

import json
import os
import random
import re
from fractions import Fraction


def load_math(dataset_path: str, num_tasks: int = 50, seed: int = 42) -> list[dict]:
    """Load MATH tasks from a local JSONL file."""
    tasks = []
    with open(dataset_path) as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            tasks.append(json.loads(line))
    rng = random.Random(seed)
    rng.shuffle(tasks)
    return tasks[:num_tasks]


def extract_boxed_answer(text: str) -> str | None:
    """Extract answer from \\boxed{} in model output, handling nested braces."""
    from utils import strip_eos_residue
    text = strip_eos_residue(text)
    # Handle nested braces by counting depth
    results = []
    i = 0
    while i < len(text):
        idx = text.find("\\boxed{", i)
        if idx == -1:
            break
        start = idx + len("\\boxed{")
        depth = 1
        j = start
        while j < len(text) and depth > 0:
            if text[j] == "{":
                depth += 1
            elif text[j] == "}":
                depth -= 1
            j += 1
        if depth == 0:
            results.append(text[start : j - 1].strip())
        i = j
    if results:
        return results[-1]
    # Fallback: "the answer is" pattern
    match = re.search(
        r"(?:the\s+)?(?:final\s+)?answer\s+is\s*:?\s*(.+?)(?:\.|$)",
        text,
        re.IGNORECASE,
    )
    if match:
        return match.group(1).strip()
    return None


def normalize_math_answer(answer: str | None) -> str | None:
    """Normalize LaTeX math answer for comparison."""
    if answer is None:
        return None
    s = answer.strip()
    s = s.replace("\\$", "").replace("$", "")
    s = s.replace("\\left", "").replace("\\right", "")
    s = s.replace("\\,", "").replace("\\ ", "")
    s = s.replace(" ", "")
    s = re.sub(r"\\dfrac", r"\\frac", s)
    s = re.sub(r"\\tfrac", r"\\frac", s)
    return s


def _parse_frac(s: str) -> Fraction | None:
    """Try to parse a string (possibly LaTeX frac) as a Fraction."""
    m = re.match(r"\\frac\{([^}]+)\}\{([^}]+)\}", s)
    if m:
        try:
            return Fraction(int(m.group(1)), int(m.group(2)))
        except (ValueError, ZeroDivisionError):
            return None
    try:
        return Fraction(s)
    except (ValueError, ZeroDivisionError):
        return None


def math_answers_equal(pred: str | None, gold: str | None) -> bool:
    """Compare two math answers with normalization."""
    if pred is None or gold is None:
        return False
    pred_norm = normalize_math_answer(pred)
    gold_norm = normalize_math_answer(gold)
    if pred_norm == gold_norm:
        return True
    # Try numeric/fraction comparison
    pf = _parse_frac(pred_norm)
    gf = _parse_frac(gold_norm)
    if pf is not None and gf is not None:
        return pf == gf
    # Try float comparison
    try:
        return abs(float(pred_norm) - float(gold_norm)) < 1e-6
    except (ValueError, TypeError):
        pass
    return False
