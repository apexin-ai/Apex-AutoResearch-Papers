"""
Invariant consensus scorer with A+C improvement:
  A (normal mode): score = positive_weight - alpha * negative_weight
  C (fallback mode): when satisfied_ratio < threshold, score = -excluded_exposure
"""
from __future__ import annotations

import logging
from collections import Counter

from .z3_maxsat import MaxSATResult

logger = logging.getLogger(__name__)


class InvariantScorer:

    def __init__(self, alpha: float = 0.5, fallback_threshold: float = 0.2):
        self.alpha = alpha
        self.fallback_threshold = fallback_threshold

    def score(
        self,
        maxsat_result: MaxSATResult,
        traces: list[dict],
        candidates: list[str],
    ) -> dict[str, float]:
        """Score each candidate answer using A+C strategy.

        Normal mode (A): score = Σw(satisfied ∩ traces) - α·Σw(excluded ∩ traces)
        Fallback mode (C): score = -Σw(excluded ∩ traces)
        Switches to fallback when satisfied_ratio < fallback_threshold.
        """
        answer_traces: dict[str, set[int]] = {}
        for t in traces:
            ans = str(t.get("answer", "")).strip()
            idx = t.get("trace_idx", 0)
            answer_traces.setdefault(ans, set()).add(idx)

        n_satisfied = len(maxsat_result.satisfied)
        n_excluded = len(maxsat_result.excluded)
        n_total = n_satisfied + n_excluded

        if n_total == 0:
            return {str(c).strip(): 0.0 for c in candidates}

        satisfied_ratio = n_satisfied / n_total
        fallback = satisfied_ratio < self.fallback_threshold

        logger.info(
            "Scorer mode=%s  satisfied_ratio=%.3f (%d/%d)  alpha=%.2f  threshold=%.2f",
            "FALLBACK" if fallback else "NORMAL",
            satisfied_ratio, n_satisfied, n_total,
            self.alpha, self.fallback_threshold,
        )

        scores: dict[str, float] = {}
        for cand in candidates:
            cand_key = str(cand).strip()
            cand_traces = answer_traces.get(cand_key, set())

            excluded_exposure = 0.0
            for uc in maxsat_result.excluded:
                if set(uc.source_traces) & cand_traces:
                    excluded_exposure += uc.weight

            if fallback:
                scores[cand_key] = -excluded_exposure
            else:
                positive = 0.0
                for uc in maxsat_result.satisfied:
                    if set(uc.source_traces) & cand_traces:
                        positive += uc.weight
                scores[cand_key] = positive - self.alpha * excluded_exposure

            logger.debug(
                "  candidate=%s  score=%.2f  traces=%s", cand_key, scores[cand_key], cand_traces,
            )

        return scores

    def select_answer(
        self,
        scores: dict[str, float],
        answer_counts: dict[str, int] | None = None,
    ) -> str:
        """Select the highest-scoring answer. Break ties by frequency."""
        if not scores:
            return ""
        max_score = max(scores.values())
        top = [a for a, s in scores.items() if s == max_score]
        if len(top) == 1:
            return top[0]
        if answer_counts:
            max_count = max(answer_counts.get(a, 0) for a in top)
            top_by_count = sorted(a for a in top if answer_counts.get(a, 0) == max_count)
            return top_by_count[0]
        return sorted(top)[0]
