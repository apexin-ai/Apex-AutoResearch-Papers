"""SQuAD-style evaluation metrics for extractive QA."""

import re
import string
from collections import Counter
from typing import List


def normalize_answer(s: str) -> str:
    """Normalize answer string following SQuAD official evaluation."""
    s = s.lower()
    # Remove articles
    s = re.sub(r"\b(a|an|the)\b", " ", s)
    # Remove punctuation
    s = "".join(ch for ch in s if ch not in string.punctuation)
    # Collapse whitespace
    s = " ".join(s.split())
    return s


def compute_exact_match(prediction: str, answers: List[str]) -> float:
    """Return 1.0 if normalized prediction matches any normalized answer."""
    norm_pred = normalize_answer(prediction)
    return float(any(norm_pred == normalize_answer(a) for a in answers))


def compute_f1(prediction: str, answers: List[str]) -> float:
    """Token-level F1 against the best-matching answer."""
    pred_tokens = normalize_answer(prediction).split()

    best_f1 = 0.0
    for answer in answers:
        ans_tokens = normalize_answer(answer).split()
        common = Counter(pred_tokens) & Counter(ans_tokens)
        num_common = sum(common.values())
        if num_common == 0:
            continue
        precision = num_common / len(pred_tokens)
        recall = num_common / len(ans_tokens)
        f1 = 2 * precision * recall / (precision + recall)
        best_f1 = max(best_f1, f1)

    return best_f1
