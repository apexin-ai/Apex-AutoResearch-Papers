"""Evaluation module for structured self-consistency IE experiments.

Provides strict-match NER/EAE evaluation, per-instance F1 computation,
correlation analysis, and summary report generation.
"""

from __future__ import annotations

import statistics
from typing import Any

from scipy.stats import kendalltau, spearmanr


# ---------------------------------------------------------------------------
# NER evaluation (strict match)
# ---------------------------------------------------------------------------

def entity_strict_match(
    pred_entities: list[dict],
    gold_entities: list[dict],
) -> tuple[int, int, int]:
    """Compute strict entity match counts.

    Strict match requires exact span (start, end) AND exact type.

    Args:
        pred_entities: Predicted entity dicts with keys text, type, start, end.
        gold_entities: Gold entity dicts with the same schema.

    Returns:
        (tp, fp, fn) counts.
    """
    pred_set = {(e["start"], e["end"], e["type"]) for e in pred_entities}
    gold_set = {(e["start"], e["end"], e["type"]) for e in gold_entities}
    tp = len(pred_set & gold_set)
    fp = len(pred_set - gold_set)
    fn = len(gold_set - pred_set)
    return tp, fp, fn


def compute_ner_f1(
    predictions: list[dict],
    golds: list[dict],
) -> dict[str, float]:
    """Compute micro-averaged NER precision, recall, and F1.

    Args:
        predictions: List of Extraction dicts (one per instance).
        golds: List of Extraction dicts (one per instance), aligned with predictions.

    Returns:
        Dict with keys "precision", "recall", "f1".
    """
    total_tp = total_fp = total_fn = 0
    for pred, gold in zip(predictions, golds):
        tp, fp, fn = entity_strict_match(
            pred.get("entities", []),
            gold.get("entities", []),
        )
        total_tp += tp
        total_fp += fp
        total_fn += fn
    return _prf(total_tp, total_fp, total_fn)


# ---------------------------------------------------------------------------
# EAE evaluation (argument match)
# ---------------------------------------------------------------------------

def _event_argument_tuples(events: list[dict]) -> set[tuple]:
    """Extract (trigger_start, trigger_end, trigger_type, role, arg_start, arg_end) tuples."""
    tuples: set[tuple] = set()
    for event in events:
        trigger = event.get("trigger", {})
        t_start = trigger.get("start")
        t_end = trigger.get("end")
        t_type = trigger.get("type")
        for arg in event.get("arguments", []):
            tuples.add((t_start, t_end, t_type, arg["role"], arg["start"], arg["end"]))
    return tuples


def relation_strict_match(
    pred_relations: list[dict],
    gold_relations: list[dict],
) -> tuple[int, int, int]:
    """Strict relation match: (head_start, head_end, tail_start, tail_end, type) must all match."""
    pred_set = {(r["head_start"], r["head_end"], r["tail_start"], r["tail_end"], r["type"]) for r in pred_relations}
    gold_set = {(r["head_start"], r["head_end"], r["tail_start"], r["tail_end"], r["type"]) for r in gold_relations}
    tp = len(pred_set & gold_set)
    fp = len(pred_set - gold_set)
    fn = len(gold_set - pred_set)
    return tp, fp, fn


def compute_re_f1(
    predictions: list[dict],
    golds: list[dict],
) -> dict[str, float]:
    """Compute micro-averaged RE precision, recall, and F1."""
    total_tp = total_fp = total_fn = 0
    for pred, gold in zip(predictions, golds):
        tp, fp, fn = relation_strict_match(
            pred.get("relations", []),
            gold.get("relations", []),
        )
        total_tp += tp
        total_fp += fp
        total_fn += fn
    return _prf(total_tp, total_fp, total_fn)


def argument_match(
    pred_events: list[dict],
    gold_events: list[dict],
) -> tuple[int, int, int]:
    """Compute event argument match counts.

    A correct argument requires trigger span match + trigger type match +
    argument role match + argument span match.

    Args:
        pred_events: Predicted Event dicts.
        gold_events: Gold Event dicts.

    Returns:
        (tp, fp, fn) counts.
    """
    pred_set = _event_argument_tuples(pred_events)
    gold_set = _event_argument_tuples(gold_events)
    tp = len(pred_set & gold_set)
    fp = len(pred_set - gold_set)
    fn = len(gold_set - pred_set)
    return tp, fp, fn


def compute_eae_f1(
    predictions: list[dict],
    golds: list[dict],
) -> dict[str, float]:
    """Compute micro-averaged EAE precision, recall, and F1.

    Args:
        predictions: List of Extraction dicts (one per instance).
        golds: List of Extraction dicts (one per instance), aligned with predictions.

    Returns:
        Dict with keys "precision", "recall", "f1".
    """
    total_tp = total_fp = total_fn = 0
    for pred, gold in zip(predictions, golds):
        tp, fp, fn = argument_match(
            pred.get("events", []),
            gold.get("events", []),
        )
        total_tp += tp
        total_fp += fp
        total_fn += fn
    return _prf(total_tp, total_fp, total_fn)


# ---------------------------------------------------------------------------
# Per-instance F1
# ---------------------------------------------------------------------------

def per_instance_f1(
    pred: dict,
    gold: dict,
    subtask: str = "ner",
) -> float:
    """Compute F1 for a single instance.

    Args:
        pred: Predicted Extraction dict.
        gold: Gold Extraction dict.
        subtask: "ner" for entity matching, "eae" for argument matching.

    Returns:
        F1 score (float in [0, 1]).
    """
    if subtask == "ner":
        tp, fp, fn = entity_strict_match(
            pred.get("entities", []),
            gold.get("entities", []),
        )
    elif subtask == "re":
        tp, fp, fn = relation_strict_match(
            pred.get("relations", []),
            gold.get("relations", []),
        )
    elif subtask == "eae":
        tp, fp, fn = argument_match(
            pred.get("events", []),
            gold.get("events", []),
        )
    else:
        raise ValueError(f"subtask must be 'ner', 're', or 'eae', got '{subtask}'")
    return _prf(tp, fp, fn)["f1"]


# ---------------------------------------------------------------------------
# Per-sample F1 distribution
# ---------------------------------------------------------------------------

def compute_sample_f1_distribution(
    sampled_instances: list[dict],
    subtask: str = "ner",
) -> dict:
    """Compute per-sample F1 distribution statistics.

    For each instance, compute F1 of each of its N samples against gold.
    Aggregate into distribution statistics.

    Args:
        sampled_instances: List of SampledInstance dicts, each containing
            "gold" (Extraction) and "samples" (list of Extraction).
        subtask: "ner" or "eae".

    Returns:
        Dict with keys:
            - "all_sample_f1s": flat list of all per-sample F1 values
            - "mean": mean F1 across all samples
            - "std": std of F1
            - "pct_f1_zero": percentage of samples with F1=0.0
            - "per_instance": list of dicts, each with {"mean", "std", "pct_f1_zero", "f1s"}
    """
    all_sample_f1s: list[float] = []
    per_instance: list[dict] = []

    for inst in sampled_instances:
        gold = inst["gold"]
        samples = inst.get("samples", [])
        f1s = [per_instance_f1(sample, gold, subtask) for sample in samples]
        all_sample_f1s.extend(f1s)

        if f1s:
            n_zero = sum(1 for f in f1s if f == 0.0)
            per_instance.append({
                "mean": statistics.mean(f1s),
                "std": statistics.pstdev(f1s),
                "pct_f1_zero": 100.0 * n_zero / len(f1s),
                "f1s": f1s,
            })
        else:
            per_instance.append({"mean": 0.0, "std": 0.0, "pct_f1_zero": 100.0, "f1s": []})

    if all_sample_f1s:
        n_zero_total = sum(1 for f in all_sample_f1s if f == 0.0)
        mean = statistics.mean(all_sample_f1s)
        std = statistics.pstdev(all_sample_f1s)
        pct_f1_zero = 100.0 * n_zero_total / len(all_sample_f1s)
    else:
        mean = 0.0
        std = 0.0
        pct_f1_zero = 100.0

    return {
        "all_sample_f1s": all_sample_f1s,
        "mean": mean,
        "std": std,
        "pct_f1_zero": pct_f1_zero,
        "per_instance": per_instance,
    }


# ---------------------------------------------------------------------------
# Correlation
# ---------------------------------------------------------------------------

def spearman_correlation(
    scores_a: list[float],
    scores_b: list[float],
) -> tuple[float, float]:
    """Compute Spearman rank correlation between two score lists.

    Args:
        scores_a: First list of scores.
        scores_b: Second list of scores (same length as scores_a).

    Returns:
        (rho, p_value).
    """
    if len(scores_a) != len(scores_b):
        raise ValueError(
            f"Score lists must have equal length, got {len(scores_a)} vs {len(scores_b)}"
        )
    if len(scores_a) < 3:
        return (0.0, 1.0)
    result = spearmanr(scores_a, scores_b)
    return (float(result.statistic), float(result.pvalue))


def kendall_correlation(
    scores_a: list[float],
    scores_b: list[float],
) -> tuple[float, float]:
    """Compute Kendall's tau-b rank correlation."""
    if len(scores_a) != len(scores_b):
        raise ValueError(
            f"Score lists must have equal length, got {len(scores_a)} vs {len(scores_b)}"
        )
    if len(scores_a) < 3:
        return (0.0, 1.0)
    result = kendalltau(scores_a, scores_b)
    return (float(result.statistic), float(result.pvalue))


def compute_auroc(
    scores: list[float],
    labels_continuous: list[float],
) -> float:
    """Compute AUROC by binarizing labels at median.

    Uses >= median vs < median as primary split (positive = at or above
    median). Falls back to > vs <= when all values equal the median.
    """
    if len(scores) < 3:
        return 0.5
    med = statistics.median(labels_continuous)
    pos = [s for s, l in zip(scores, labels_continuous) if l >= med]
    neg = [s for s, l in zip(scores, labels_continuous) if l < med]
    # Fallback: when all values equal median, split is impossible
    if not pos or not neg:
        pos = [s for s, l in zip(scores, labels_continuous) if l > med]
        neg = [s for s, l in zip(scores, labels_continuous) if l <= med]
    if not pos or not neg:
        return 0.5
    concordant = sum(1 for p in pos for n in neg if p > n)
    tied = sum(1 for p in pos for n in neg if p == n)
    return (concordant + 0.5 * tied) / (len(pos) * len(neg))


# ---------------------------------------------------------------------------
# Summary report
# ---------------------------------------------------------------------------

def generate_evaluation_report(
    sampled_instances: list[dict],
    consistency_scores: dict[str, list[float]],
    subtask: str = "ner",
) -> dict[str, Any]:
    """Generate a structured evaluation report.

    Computes greedy F1, oracle best-of-N F1, and consistency-F1 correlation
    for each consistency scoring method.

    Args:
        sampled_instances: List of SampledInstance dicts, each containing
            "id", "text", "gold" (Extraction), "samples" (list of Extraction),
            and optionally "greedy" (Extraction).
        consistency_scores: Dict mapping method name to a list of per-instance
            consistency scores (aligned with sampled_instances).
        subtask: "ner" or "eae".

    Returns:
        Dict with keys:
            - "greedy_f1": float, micro-averaged F1 of greedy outputs.
            - "oracle_best_of_n_f1": float, micro-averaged F1 using the
              best sample per instance.
            - "per_instance_greedy_f1": list of per-instance greedy F1 values.
            - "correlations": dict mapping method name to {"rho": float, "p_value": float}.
            - "num_instances": int.
            - "num_samples_per_instance": float, average number of samples.
    """
    greedy_preds = []
    greedy_golds = []
    oracle_preds = []
    oracle_golds = []
    instance_greedy_f1s: list[float] = []

    for inst in sampled_instances:
        gold = inst["gold"]

        # Greedy F1
        greedy = inst.get("greedy")
        if greedy is not None:
            greedy_preds.append(greedy)
            greedy_golds.append(gold)
            instance_greedy_f1s.append(per_instance_f1(greedy, gold, subtask))
        else:
            instance_greedy_f1s.append(0.0)

        # Oracle best-of-N: pick the sample with highest per-instance F1
        samples = inst.get("samples", [])
        if samples:
            best_sample = max(samples, key=lambda s: per_instance_f1(s, gold, subtask))
            oracle_preds.append(best_sample)
            oracle_golds.append(gold)

    # Micro-averaged scores
    f1_fn = {"ner": compute_ner_f1, "re": compute_re_f1, "eae": compute_eae_f1}[subtask]
    greedy_metrics = f1_fn(greedy_preds, greedy_golds) if greedy_preds else _prf(0, 0, 0)
    oracle_metrics = f1_fn(oracle_preds, oracle_golds) if oracle_preds else _prf(0, 0, 0)

    # Correlation between consistency scores and per-instance greedy F1
    correlations: dict[str, dict[str, float]] = {}
    for method_name, scores in consistency_scores.items():
        rho, p_value = spearman_correlation(scores, instance_greedy_f1s)
        correlations[method_name] = {"rho": rho, "p_value": p_value}

    total_samples = sum(len(inst.get("samples", [])) for inst in sampled_instances)
    n = len(sampled_instances)

    return {
        "greedy_f1": greedy_metrics["f1"],
        "oracle_best_of_n_f1": oracle_metrics["f1"],
        "per_instance_greedy_f1": instance_greedy_f1s,
        "correlations": correlations,
        "num_instances": n,
        "num_samples_per_instance": total_samples / n if n > 0 else 0.0,
    }


# ---------------------------------------------------------------------------
# Internal helpers
# ---------------------------------------------------------------------------

def _prf(tp: int, fp: int, fn: int) -> dict[str, float]:
    """Compute precision, recall, F1 from raw counts."""
    precision = tp / (tp + fp) if (tp + fp) > 0 else 0.0
    recall = tp / (tp + fn) if (tp + fn) > 0 else 0.0
    f1 = 2 * precision * recall / (precision + recall) if (precision + recall) > 0 else 0.0
    return {"precision": precision, "recall": recall, "f1": f1}
