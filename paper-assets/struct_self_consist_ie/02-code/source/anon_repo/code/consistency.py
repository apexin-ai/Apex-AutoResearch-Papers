"""Consistency metrics for structured information extraction with self-consistency.

Implements three complementary consistency measures over N sampled extractions:
1. Fleiss' Kappa (surface matching) — treats N samples as N raters on entity presence
2. Structural soft Jaccard — span-level soft overlap with Hungarian matching
3. Oracle best-of-N — upper-bound F1 by selecting the best sample per instance

Key dependencies: numpy, scipy (linear_sum_assignment).
"""

from __future__ import annotations

from itertools import combinations
from typing import TYPE_CHECKING

import numpy as np
from scipy.optimize import linear_sum_assignment

if TYPE_CHECKING:
    pass

# ---------------------------------------------------------------------------
# Type aliases (mirrors shared data format)
# ---------------------------------------------------------------------------
Entity = dict       # {"text", "type", "start", "end"}
Relation = dict     # {"head", "tail", "type", ...}
Event = dict        # {"trigger": {...}, "arguments": [...]}
Extraction = dict   # {"entities", "relations", "events"}


# ===================================================================
# 1. Fleiss' Kappa — surface-level entity agreement
# ===================================================================

def _extract_surface_keys(sample: Extraction, subtask: str) -> set[tuple]:
    """Extract surface-level keys from a sample for Fleiss' Kappa computation."""
    if subtask == "ner":
        return {(e["text"], e["type"]) for e in sample.get("entities", [])}
    elif subtask == "re":
        return {(r["head"], r["tail"], r["type"]) for r in sample.get("relations", [])}
    elif subtask == "eae":
        keys: set[tuple] = set()
        for ev in sample.get("events", []):
            t = ev.get("trigger", {})
            for arg in ev.get("arguments", []):
                keys.add((t.get("text", ""), t.get("type", ""), arg["role"], arg["text"]))
        return keys
    else:
        raise ValueError(f"Unknown subtask: {subtask}")


def fleiss_kappa_surface(samples: list[Extraction], subtask: str = "ner") -> float:
    """Compute Fleiss' kappa treating N LLM samples as N raters on item presence.

    Items are subtask-dependent surface keys:
    - ner: (entity_text, entity_type)
    - re: (head_text, tail_text, relation_type)
    - eae: (trigger_text, trigger_type, role, argument_text)

    Args:
        samples: List of N extraction dicts.
        subtask: "ner", "re", or "eae".

    Returns:
        Fleiss' kappa in [-1, 1].  Returns 1.0 for degenerate cases (<=1 unique
        item, perfect agreement, or undefined P_e).
    """
    n_raters = len(samples)
    if n_raters <= 1:
        return 1.0

    # Collect unique keys and per-sample presence sets
    entity_sets: list[set[tuple]] = []
    all_keys: set[tuple] = set()
    for sample in samples:
        keys = _extract_surface_keys(sample, subtask)
        entity_sets.append(keys)
        all_keys |= keys

    n_subjects = len(all_keys)
    if n_subjects <= 0:
        # All samples extracted nothing — perfect agreement on empty set
        return 1.0

    key_list = sorted(all_keys)

    # Build rating matrix: n_subjects x 2 (categories: absent=0, present=1)
    # n_ij = number of raters assigning subject i to category j
    rating = np.zeros((n_subjects, 2), dtype=np.int64)
    for es in entity_sets:
        for idx, key in enumerate(key_list):
            if key in es:
                rating[idx, 1] += 1
            else:
                rating[idx, 0] += 1

    n = n_raters
    k = 2  # number of categories

    # Check perfect agreement: every subject has all votes in one category
    if np.all(np.max(rating, axis=1) == n):
        return 1.0

    # P_i for each subject
    P_i = (np.sum(rating ** 2, axis=1) - n) / (n * (n - 1))
    P_bar = np.mean(P_i)

    # P_e — expected agreement by chance
    p_j = np.sum(rating, axis=0) / (n_subjects * n)
    P_e = np.sum(p_j ** 2)

    if abs(1.0 - P_e) < 1e-12:
        return 1.0

    kappa = (P_bar - P_e) / (1.0 - P_e)
    return float(kappa)


# ===================================================================
# 2. Structural soft Jaccard consistency
# ===================================================================

def _span_soft_jaccard(s1_start: int, s1_end: int, s2_start: int, s2_end: int) -> float:
    """Soft Jaccard between two character spans."""
    overlap = max(0, min(s1_end, s2_end) - max(s1_start, s2_start))
    len1 = s1_end - s1_start
    len2 = s2_end - s2_start
    union = len1 + len2 - overlap
    if union <= 0:
        return 0.0
    return overlap / union


def _ner_soft_jaccard_pair(entities_a: list[Entity], entities_b: list[Entity]) -> float:
    """Compute type-aware soft Jaccard between two entity lists via Hungarian matching.

    Groups entities by type, finds optimal alignment within each group using
    span-level soft Jaccard as the similarity, then computes a weighted average.

    Args:
        entities_a: Entities from sample i.
        entities_b: Entities from sample j.

    Returns:
        Weighted-average soft Jaccard across all type groups.
    """
    if not entities_a and not entities_b:
        return 1.0
    if not entities_a or not entities_b:
        return 0.0

    # Group by entity type
    types: set[str] = set()
    groups_a: dict[str, list[Entity]] = {}
    groups_b: dict[str, list[Entity]] = {}

    for e in entities_a:
        t = e["type"]
        types.add(t)
        groups_a.setdefault(t, []).append(e)
    for e in entities_b:
        t = e["type"]
        types.add(t)
        groups_b.setdefault(t, []).append(e)

    total_score = 0.0
    total_weight = 0

    for t in types:
        ga = groups_a.get(t, [])
        gb = groups_b.get(t, [])
        denom = max(len(ga), len(gb))
        if denom == 0:
            continue

        total_weight += denom

        if not ga or not gb:
            # One side empty — all unmatched, contributes 0
            continue

        # Cost matrix for Hungarian (we maximize similarity, so negate for min-cost)
        cost = np.zeros((len(ga), len(gb)), dtype=np.float64)
        for i, ea in enumerate(ga):
            for j, eb in enumerate(gb):
                cost[i, j] = _span_soft_jaccard(ea["start"], ea["end"],
                                                 eb["start"], eb["end"])

        row_ind, col_ind = linear_sum_assignment(-cost)  # negate to maximize
        matched_sim = cost[row_ind, col_ind].sum()
        # Normalize by the larger set size to penalize unmatched spans
        total_score += matched_sim

    if total_weight == 0:
        return 1.0
    return total_score / total_weight


def _re_soft_jaccard_pair(relations_a: list[dict], relations_b: list[dict]) -> float:
    """Soft Jaccard for relation extraction via Hungarian matching.

    Relation similarity = head_span_sj * tail_span_sj * type_match.
    """
    if not relations_a and not relations_b:
        return 1.0
    if not relations_a or not relations_b:
        return 0.0

    cost = np.zeros((len(relations_a), len(relations_b)), dtype=np.float64)
    for i, a in enumerate(relations_a):
        for j, b in enumerate(relations_b):
            if a["type"] != b["type"]:
                continue
            head_sj = _span_soft_jaccard(a["head_start"], a["head_end"],
                                         b["head_start"], b["head_end"])
            tail_sj = _span_soft_jaccard(a["tail_start"], a["tail_end"],
                                         b["tail_start"], b["tail_end"])
            cost[i, j] = head_sj * tail_sj

    row_ind, col_ind = linear_sum_assignment(-cost)
    matched_sim = cost[row_ind, col_ind].sum()
    return matched_sim / max(len(relations_a), len(relations_b))


def _eae_soft_jaccard_pair(events_a: list[Event], events_b: list[Event]) -> float:
    """Soft Jaccard for event argument extraction.

    Groups arguments by (trigger_type, role) and applies Hungarian matching
    within each group.

    Args:
        events_a: Events from sample i.
        events_b: Events from sample j.

    Returns:
        Weighted-average soft Jaccard across (trigger_type, role) groups.
    """
    # Flatten to (trigger_type, role) -> list of argument spans
    def _flatten(events: list[Event]) -> dict[tuple[str, str], list[dict]]:
        groups: dict[tuple[str, str], list[dict]] = {}
        for ev in events:
            ttype = ev.get("trigger", {}).get("type", "")
            for arg in ev.get("arguments", []):
                key = (ttype, arg["role"])
                groups.setdefault(key, []).append(arg)
        return groups

    flat_a = _flatten(events_a)
    flat_b = _flatten(events_b)

    if not flat_a and not flat_b:
        return 1.0
    if not flat_a or not flat_b:
        return 0.0

    all_keys = set(flat_a.keys()) | set(flat_b.keys())

    total_score = 0.0
    total_weight = 0

    for key in all_keys:
        ga = flat_a.get(key, [])
        gb = flat_b.get(key, [])
        denom = max(len(ga), len(gb))
        if denom == 0:
            continue

        total_weight += denom

        if not ga or not gb:
            continue

        cost = np.zeros((len(ga), len(gb)), dtype=np.float64)
        for i, aa in enumerate(ga):
            for j, ab in enumerate(gb):
                cost[i, j] = _span_soft_jaccard(aa["start"], aa["end"],
                                                 ab["start"], ab["end"])

        row_ind, col_ind = linear_sum_assignment(-cost)
        matched_sim = cost[row_ind, col_ind].sum()
        total_score += matched_sim

    if total_weight == 0:
        return 1.0
    return total_score / total_weight


def structural_consistency_soft_jaccard(
    samples: list[Extraction],
    subtask: str = "ner",
) -> float:
    """Span-level soft Jaccard consistency averaged over all sample pairs.

    For each pair (i, j) with i < j, computes a type-aware soft Jaccard using
    Hungarian matching on span overlaps, then returns the mean.

    Args:
        samples: N extraction dicts.
        subtask: "ner" for entity consistency, "eae" for event-argument consistency.

    Returns:
        Mean pairwise soft Jaccard in [0, 1].
    """
    n = len(samples)
    if n <= 1:
        return 1.0

    if subtask == "ner":
        pair_fn = _ner_soft_jaccard_pair
    elif subtask == "re":
        pair_fn = _re_soft_jaccard_pair
    else:
        pair_fn = _eae_soft_jaccard_pair

    field = {"ner": "entities", "re": "relations", "eae": "events"}[subtask]

    scores: list[float] = []
    for i, j in combinations(range(n), 2):
        score = pair_fn(
            samples[i].get(field, []),
            samples[j].get(field, []),
        )
        scores.append(score)

    return float(np.mean(scores))


# ===================================================================
# 3. Oracle best-of-N
# ===================================================================

def oracle_best_of_n(
    samples: list[Extraction],
    gold: Extraction,
    subtask: str = "ner",
) -> tuple[int, float]:
    """Select the sample with the highest F1 against the gold extraction.

    Args:
        samples: N extraction dicts.
        gold: Gold-standard extraction.
        subtask: Passed through to per_instance_f1.

    Returns:
        (best_index, best_f1). Returns (-1, 0.0) if samples is empty.
    """
    if not samples:
        return (-1, 0.0)

    # Lazy import to avoid circular dependency with evaluation.py
    from evaluation import per_instance_f1

    best_idx = -1
    best_f1 = -1.0

    for idx, sample in enumerate(samples):
        f1 = per_instance_f1(sample, gold, subtask=subtask)
        if f1 > best_f1:
            best_f1 = f1
            best_idx = idx

    return (best_idx, best_f1)


# ===================================================================
# Aggregate helper
# ===================================================================

def compute_all_consistency_scores(
    sampled_instances: list[dict],
    subtask: str = "ner",
) -> dict:
    """Compute all consistency metrics for a list of sampled instances.

    Args:
        sampled_instances: List of SampledInstance dicts, each with keys
            "id", "text", "gold" (Extraction), "samples" (list[Extraction]).
        subtask: "ner", "re", or "eae".

    Returns:
        Dict with per-instance score lists::

            {
                "fleiss_kappa": [float, ...],
                "soft_jaccard": [float, ...],
                "oracle_f1":    [float, ...],
                "oracle_indices": [int, ...],
            }
    """
    result: dict[str, list] = {
        "fleiss_kappa": [],
        "soft_jaccard": [],
        "oracle_f1": [],
        "oracle_indices": [],
    }

    for inst in sampled_instances:
        samples = inst["samples"]
        gold = inst["gold"]

        result["fleiss_kappa"].append(fleiss_kappa_surface(samples, subtask=subtask))
        result["soft_jaccard"].append(
            structural_consistency_soft_jaccard(samples, subtask=subtask)
        )

        best_idx, best_f1 = oracle_best_of_n(samples, gold, subtask=subtask)
        result["oracle_f1"].append(best_f1)
        result["oracle_indices"].append(best_idx)

    return result
