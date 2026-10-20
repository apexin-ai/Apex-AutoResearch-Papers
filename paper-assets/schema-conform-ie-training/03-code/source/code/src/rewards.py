# 5-component reward functions for Schema-Conformance IE training.
# Each reward: (model_output_str, schema_dict, gold_annotations) -> float in [0, 1].
# Includes GDPO normalization for per-component advantage computation.
# Depends on: src.schema_utils

import json
from typing import Any

from src.schema_utils import (
    parse_schema,
    parse_model_output,
    check_type_conformance,
    check_relational_constraints,
    check_structural_completeness,
)

REWARD_NAMES = [
    "f1_correctness",
    "structural_validity",
    "type_conformance",
    "relational_constraint",
    "structural_completeness",
]


# ---------------------------------------------------------------------------
# Matching helpers
# ---------------------------------------------------------------------------

def _text_overlap_score(text1: str, text2: str) -> float:
    """Token-level Jaccard overlap between two text strings."""
    tokens1 = set(text1.lower().split())
    tokens2 = set(text2.lower().split())
    if not tokens1 or not tokens2:
        return 1.0 if tokens1 == tokens2 else 0.0
    intersection = tokens1 & tokens2
    union = tokens1 | tokens2
    return len(intersection) / len(union)


def _span_iou(span1: list | tuple, span2: list | tuple) -> float:
    """IoU between two [start, end) character spans."""
    s1, e1 = span1[0], span1[1]
    s2, e2 = span2[0], span2[1]
    overlap = max(0, min(e1, e2) - max(s1, s2))
    union = max(e1, e2) - min(s1, s2)
    return overlap / union if union > 0 else 0.0


def _entity_similarity(pred: dict, gold: dict) -> float:
    """Similarity score between a predicted and gold entity.

    Uses span IoU if both have valid spans, otherwise falls back to text overlap.
    """
    if pred.get("type") != gold.get("type"):
        return 0.0

    pred_span = pred.get("span")
    gold_span = gold.get("span")
    has_spans = (
        isinstance(pred_span, (list, tuple)) and len(pred_span) >= 2
        and isinstance(gold_span, (list, tuple)) and len(gold_span) >= 2
    )

    if has_spans:
        return _span_iou(pred_span, gold_span)

    pred_text = pred.get("text", "")
    gold_text = gold.get("text", "")
    if pred_text and gold_text:
        return _text_overlap_score(pred_text, gold_text)

    return 0.0


def _match_entities(
    pred_entities: list[dict],
    gold_entities: list[dict],
    threshold: float = 0.5,
) -> tuple[int, int, int]:
    """Greedy match predicted entities to gold. Returns (tp, fp, fn)."""
    matched_gold: set[int] = set()
    tp = 0

    for pred in pred_entities:
        if not isinstance(pred, dict):
            continue
        best_score = 0.0
        best_idx = -1
        for i, gold in enumerate(gold_entities):
            if i in matched_gold or not isinstance(gold, dict):
                continue
            score = _entity_similarity(pred, gold)
            if score > best_score:
                best_score = score
                best_idx = i
        if best_score >= threshold and best_idx >= 0:
            tp += 1
            matched_gold.add(best_idx)

    fp = len([e for e in pred_entities if isinstance(e, dict)]) - tp
    fn = len(gold_entities) - len(matched_gold)
    return tp, fp, fn


def _normalize_relation(rel: dict) -> dict:
    """Normalize relation dict to canonical {type, arg1, arg2} format."""
    rel_type = rel.get("type") or rel.get("relation") or rel.get("label")
    if isinstance(rel_type, str):
        rel_type = rel_type.lower().replace("_", "-")
    arg1 = rel.get("arg1") or rel.get("head") or rel.get("subject") or rel.get("source")
    arg2 = rel.get("arg2") or rel.get("tail") or rel.get("object") or rel.get("target")
    if isinstance(arg1, str):
        arg1 = {"text": arg1}
    if isinstance(arg2, str):
        arg2 = {"text": arg2}
    return {"type": rel_type, "arg1": arg1 or {}, "arg2": arg2 or {}}


def _arg_similarity(pred: dict, gold: dict) -> float:
    """Text-focused similarity for relation arguments — entity type match not required."""
    pred_text = pred.get("text", "")
    gold_text = gold.get("text", "")
    if pred_text and gold_text:
        return _text_overlap_score(pred_text, gold_text)
    return _entity_similarity(pred, gold)


def _match_relations(
    pred_relations: list[dict],
    gold_relations: list[dict],
    threshold: float = 0.3,
) -> tuple[int, int, int]:
    """Match predicted relations to gold. Returns (tp, fp, fn)."""
    matched_gold: set[int] = set()
    tp = 0

    for pred in pred_relations:
        if not isinstance(pred, dict):
            continue
        pred_n = _normalize_relation(pred)
        if pred_n["type"] is None:
            continue
        for i, gold in enumerate(gold_relations):
            if i in matched_gold or not isinstance(gold, dict):
                continue
            gold_n = _normalize_relation(gold)
            if pred_n["type"] != gold_n["type"]:
                continue
            arg1_sim = _arg_similarity(pred_n["arg1"], gold_n["arg1"])
            arg2_sim = _arg_similarity(pred_n["arg2"], gold_n["arg2"])
            if arg1_sim >= threshold and arg2_sim >= threshold:
                tp += 1
                matched_gold.add(i)
                break

    fp = len([r for r in pred_relations if isinstance(r, dict)]) - tp
    fn = len(gold_relations) - len(matched_gold)
    return tp, fp, fn


def _f1(tp: int, fp: int, fn: int) -> float:
    if tp == 0:
        return 0.0
    precision = tp / (tp + fp)
    recall = tp / (tp + fn)
    return 2 * precision * recall / (precision + recall)


# ---------------------------------------------------------------------------
# Individual reward functions
# ---------------------------------------------------------------------------

def f1_correctness_reward(
    model_output_str: str, schema_dict: dict, gold_annotations: dict
) -> float:
    """Partial-match F1 between predicted and gold entities/relations."""
    output, _ = parse_model_output(model_output_str)
    if output is None:
        return 0.0

    pred_ents = output.get("entities", [])
    gold_ents = gold_annotations.get("entities", [])
    pred_rels = output.get("relations", [])
    gold_rels = gold_annotations.get("relations", [])
    if not isinstance(pred_ents, list):
        pred_ents = []
    if not isinstance(pred_rels, list):
        pred_rels = []

    # Entity F1
    if not gold_ents and not pred_ents:
        ent_f1 = 1.0
    else:
        tp, fp, fn = _match_entities(pred_ents, gold_ents)
        ent_f1 = _f1(tp, fp, fn)

    # Relation F1 (only factor in if gold has relations)
    if not gold_rels and not pred_rels:
        return ent_f1
    tp, fp, fn = _match_relations(pred_rels, gold_rels)
    rel_f1 = _f1(tp, fp, fn)
    return (ent_f1 + rel_f1) / 2


def structural_validity_reward(
    model_output_str: str, schema_dict: dict, gold_annotations: dict
) -> float:
    """1.0 if output is valid JSON object, 0.0 otherwise."""
    output, _ = parse_model_output(model_output_str)
    return 1.0 if output is not None else 0.0


def type_conformance_reward(
    model_output_str: str, schema_dict: dict, gold_annotations: dict
) -> float:
    """Proportion of extracted types that belong to the schema inventory."""
    output, _ = parse_model_output(model_output_str)
    if output is None:
        return 0.0
    schema = parse_schema(schema_dict)
    entities = output.get("entities", [])
    relations = output.get("relations", [])
    if not isinstance(entities, list):
        entities = []
    if not isinstance(relations, list):
        relations = []
    return check_type_conformance(entities, relations, schema)


def relational_constraint_reward(
    model_output_str: str, schema_dict: dict, gold_annotations: dict
) -> float:
    """Proportion of relations whose arg types satisfy schema type-pair constraints."""
    output, _ = parse_model_output(model_output_str)
    if output is None:
        return 0.0
    schema = parse_schema(schema_dict)
    relations = output.get("relations", [])
    if not isinstance(relations, list):
        relations = []
    return check_relational_constraints(relations, schema)


def structural_completeness_reward(
    model_output_str: str, schema_dict: dict, gold_annotations: dict
) -> float:
    """Proportion of required structural fields present in the output."""
    output, _ = parse_model_output(model_output_str)
    if output is None:
        return 0.0
    return check_structural_completeness(output)


# ---------------------------------------------------------------------------
# Combined reward computation
# ---------------------------------------------------------------------------

def compute_all_rewards(
    model_output_str: str, schema_dict: dict, gold_annotations: dict
) -> dict[str, float]:
    """Compute all 5 reward components. Returns name->score dict."""
    return {
        "f1_correctness": f1_correctness_reward(model_output_str, schema_dict, gold_annotations),
        "structural_validity": structural_validity_reward(model_output_str, schema_dict, gold_annotations),
        "type_conformance": type_conformance_reward(model_output_str, schema_dict, gold_annotations),
        "relational_constraint": relational_constraint_reward(model_output_str, schema_dict, gold_annotations),
        "structural_completeness": structural_completeness_reward(model_output_str, schema_dict, gold_annotations),
    }


def compute_weighted_reward(
    model_output_str: str,
    schema_dict: dict,
    gold_annotations: dict,
    weights: dict[str, float],
) -> float:
    """Compute weighted sum of all reward components."""
    rewards = compute_all_rewards(model_output_str, schema_dict, gold_annotations)
    return sum(weights.get(k, 0.0) * v for k, v in rewards.items())


def compute_entity_relation_f1(
    model_output_str: str, schema_dict: dict, gold_annotations: dict
) -> dict[str, float | None]:
    """Compute entity F1 and relation F1 separately.

    Returns {"entity_f1": float, "relation_f1": float|None}.
    relation_f1 is None when both gold and predicted relations are empty (NER-only).
    """
    output, _ = parse_model_output(model_output_str)
    if output is None:
        return {"entity_f1": 0.0, "relation_f1": 0.0}

    pred_ents = output.get("entities", [])
    gold_ents = gold_annotations.get("entities", [])
    pred_rels = output.get("relations", [])
    gold_rels = gold_annotations.get("relations", [])
    if not isinstance(pred_ents, list):
        pred_ents = []
    if not isinstance(pred_rels, list):
        pred_rels = []

    # Entity F1
    if not gold_ents and not pred_ents:
        ent_f1 = 1.0
    else:
        tp, fp, fn = _match_entities(pred_ents, gold_ents)
        ent_f1 = _f1(tp, fp, fn)

    # Relation F1
    if not gold_rels and not pred_rels:
        rel_f1 = None
    elif not gold_rels:
        rel_f1 = 0.0
    else:
        tp, fp, fn = _match_relations(pred_rels, gold_rels)
        rel_f1 = _f1(tp, fp, fn)

    return {"entity_f1": ent_f1, "relation_f1": rel_f1}


def gdpo_from_precomputed(
    all_rewards: list[dict[str, float]],
    weights: dict[str, float],
    eps: float = 1e-8,
) -> list[float]:
    """GDPO normalization from pre-computed per-sample reward dicts."""
    k = len(all_rewards)
    if k == 0:
        return []

    normalized: list[dict[str, float]] = [{} for _ in range(k)]
    for name in REWARD_NAMES:
        values = [r[name] for r in all_rewards]
        mean_val = sum(values) / k
        var_val = sum((v - mean_val) ** 2 for v in values) / k
        std_val = var_val**0.5
        for i in range(k):
            normalized[i][name] = (values[i] - mean_val) / (std_val + eps)

    return [
        sum(weights.get(name, 0.0) * normalized[i][name] for name in REWARD_NAMES)
        for i in range(k)
    ]


def compute_gdpo_rewards(
    completions: list[str],
    schema_dicts: list[dict],
    gold_list: list[dict],
    weights: dict[str, float],
    eps: float = 1e-8,
) -> list[float]:
    """GDPO normalization: normalize each reward component independently within
    the group of K completions, then combine with weights.

    For each component j across K completions:
        r_j_norm = (r_j - mean(r_j)) / (std(r_j) + eps)
    Final score = sum(w_j * r_j_norm)
    """
    k = len(completions)
    if k == 0:
        return []

    all_rewards = [
        compute_all_rewards(comp, schema, gold)
        for comp, schema, gold in zip(completions, schema_dicts, gold_list)
    ]

    normalized: list[dict[str, float]] = [{} for _ in range(k)]
    for name in REWARD_NAMES:
        values = [r[name] for r in all_rewards]
        mean_val = sum(values) / k
        var_val = sum((v - mean_val) ** 2 for v in values) / k
        std_val = var_val**0.5

        for i in range(k):
            normalized[i][name] = (values[i] - mean_val) / (std_val + eps)

    return [
        sum(weights.get(name, 0.0) * normalized[i][name] for name in REWARD_NAMES)
        for i in range(k)
    ]
