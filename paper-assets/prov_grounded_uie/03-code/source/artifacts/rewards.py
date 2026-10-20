"""Reward functions for GRPO training.

Three reward dimensions:
  (a) Provenance fidelity — evidence span quality (char-IoU + NLI + length penalty)
  (b) Structural F1      — relation extraction correctness
  (c) Format compliance   — valid JSON + correct schema

Function signature follows TRL GRPOTrainer convention:
    def reward_fn(prompts, completions, **kwargs) -> list[float]

Key dependency: cross-encoder/nli-deberta-v3-large (lazy-loaded on first call).
"""

import json
import re
from typing import Optional

import torch
import torch.nn.functional as F
from transformers import AutoTokenizer, AutoModelForSequenceClassification


# ---------------------------------------------------------------------------
# NLI model singleton (lazy-loaded)
# ---------------------------------------------------------------------------

_nli_model = None
_nli_tokenizer = None
_nli_device = None


def _get_nli_model(
    model_name: str = "/root/autodl-tmp/.hf_cache/ms_deberta/cross-encoder/nli-deberta-v3-large",
    device: str = "cpu",
):
    global _nli_model, _nli_tokenizer, _nli_device
    if _nli_model is None:
        _nli_device = device
        _nli_tokenizer = AutoTokenizer.from_pretrained(model_name)
        _nli_model = AutoModelForSequenceClassification.from_pretrained(model_name)
        _nli_model.to(_nli_device).eval()
    return _nli_model, _nli_tokenizer, _nli_device


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def parse_json_output(text) -> Optional[dict]:
    """Best-effort JSON extraction from model output."""
    if isinstance(text, list):
        for msg in reversed(text):
            if isinstance(msg, dict) and msg.get("role") == "assistant":
                text = msg["content"]
                break
        else:
            return None
    if isinstance(text, str):
        text = re.sub(r'<think>.*?</think>', '', text, flags=re.DOTALL).strip()
    text = text.strip()
    # Direct parse
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        pass
    # Markdown code fence
    m = re.search(r"```(?:json)?\s*(\{.*?\})\s*```", text, re.DOTALL)
    if m:
        try:
            return json.loads(m.group(1))
        except json.JSONDecodeError:
            pass
    # First { … } block
    m = re.search(r"\{.*\}", text, re.DOTALL)
    if m:
        try:
            return json.loads(m.group(0))
        except json.JSONDecodeError:
            pass
    return None


def _char_iou(pred: str, gold: str) -> float:
    """Character-level IoU using character-frequency bags."""
    pred_bag: dict[str, int] = {}
    for c in pred:
        pred_bag[c] = pred_bag.get(c, 0) + 1
    gold_bag: dict[str, int] = {}
    for c in gold:
        gold_bag[c] = gold_bag.get(c, 0) + 1

    all_chars = set(pred_bag) | set(gold_bag)
    intersection = sum(min(pred_bag.get(c, 0), gold_bag.get(c, 0)) for c in all_chars)
    union = sum(max(pred_bag.get(c, 0), gold_bag.get(c, 0)) for c in all_chars)
    return intersection / union if union > 0 else 0.0


def _deserialize(value):
    """Deserialize a JSON string if needed; otherwise return as-is."""
    if isinstance(value, str):
        return json.loads(value)
    return value


def _batch_nli_scores(
    premises: list[str],
    hypotheses: list[str],
    model_name: str = "/root/autodl-tmp/.hf_cache/ms_deberta/cross-encoder/nli-deberta-v3-large",
    batch_size: int = 32,
    device: str = "cpu",
) -> list[float]:
    """Compute entailment probability for (premise, hypothesis) pairs.

    DeBERTa NLI label order: [contradiction=0, neutral=1, entailment=2].
    Returns list of P(entailment) floats.
    """
    if not premises:
        return []

    model, tokenizer, device = _get_nli_model(model_name, device=device)
    scores: list[float] = []

    for i in range(0, len(premises), batch_size):
        bp = premises[i : i + batch_size]
        bh = hypotheses[i : i + batch_size]
        inputs = tokenizer(
            bp, bh, padding=True, truncation=True, max_length=512, return_tensors="pt"
        ).to(device)
        with torch.no_grad():
            logits = model(**inputs).logits
            probs = F.softmax(logits, dim=-1)
            scores.extend(probs[:, 2].cpu().tolist())

    return scores


# ---------------------------------------------------------------------------
# (a) Provenance Fidelity Reward
# ---------------------------------------------------------------------------

def provenance_fidelity_reward(prompts, completions, **kwargs) -> list[float]:
    """Evidence span quality: char-IoU + NLI entailment + length penalty.

    Required kwargs: gold_relations, document_text.
    Optional kwargs: iou_weight (0.5), nli_weight (0.3), length_weight (0.2),
                     length_penalty_factor (3.0), nli_batch_size (32).
    """
    gold_relations_raw = kwargs.get("gold_relations", [])
    document_text_list = kwargs.get("document_text", [])

    iou_w = kwargs.get("iou_weight", 0.5)
    nli_w = kwargs.get("nli_weight", 0.3)
    len_w = kwargs.get("length_weight", 0.2)
    penalty_factor = kwargs.get("length_penalty_factor", 3.0)
    nli_bs = kwargs.get("nli_batch_size", 32)
    nli_model = kwargs.get("nli_model_name", "/root/autodl-tmp/.hf_cache/ms_deberta/cross-encoder/nli-deberta-v3-large")
    nli_device = kwargs.get("nli_device", "cpu")

    # Collect NLI pairs across all samples for batched inference
    all_premises: list[str] = []
    all_hypotheses: list[str] = []
    nli_sample_idx: list[int] = []

    per_sample_iou: list[float] = []
    per_sample_len: list[float] = []

    for idx, completion in enumerate(completions):
        parsed = parse_json_output(completion)
        if parsed is None or "relations" not in parsed:
            per_sample_iou.append(0.0)
            per_sample_len.append(0.0)
            continue

        gold_rels = _deserialize(gold_relations_raw[idx])
        doc_text = document_text_list[idx] if idx < len(document_text_list) else ""
        doc_len = max(len(doc_text), 1)
        pred_rels = parsed["relations"]

        gold_map: dict[tuple, dict] = {}
        for gr in gold_rels:
            key = (gr["head"].lower(), gr["tail"].lower(), gr["relation"].lower())
            gold_map[key] = gr

        iou_scores: list[float] = []
        length_scores: list[float] = []

        for pr in pred_rels:
            pred_ev = pr.get("evidence", [])
            if not pred_ev:
                continue
            pred_ev_text = " ".join(pred_ev) if isinstance(pred_ev, list) else str(pred_ev)
            key = (
                pr.get("head", "").lower(),
                pr.get("tail", "").lower(),
                pr.get("relation", "").lower(),
            )

            if key in gold_map:
                gold_ev_text = " ".join(gold_map[key].get("evidence", []))
                iou_scores.append(_char_iou(pred_ev_text, gold_ev_text))

                claim = f'{pr.get("head", "")} {pr.get("relation", "")} {pr.get("tail", "")}'
                all_premises.append(pred_ev_text)
                all_hypotheses.append(claim)
                nli_sample_idx.append(idx)

            length_scores.append(max(0.0, 1.0 - (len(pred_ev_text) / doc_len) * penalty_factor))

        per_sample_iou.append(
            sum(iou_scores) / len(iou_scores) if iou_scores else 0.0
        )
        per_sample_len.append(
            sum(length_scores) / len(length_scores) if length_scores else 0.0
        )

    # Batched NLI
    nli_flat = _batch_nli_scores(all_premises, all_hypotheses, model_name=nli_model, batch_size=nli_bs, device=nli_device)

    per_sample_nli = [0.0] * len(completions)
    nli_counts = [0] * len(completions)
    for score, sidx in zip(nli_flat, nli_sample_idx):
        per_sample_nli[sidx] += score
        nli_counts[sidx] += 1
    per_sample_nli = [
        s / c if c > 0 else 0.0 for s, c in zip(per_sample_nli, nli_counts)
    ]

    return [
        iou_w * iou + nli_w * nli + len_w * ln
        for iou, nli, ln in zip(per_sample_iou, per_sample_nli, per_sample_len)
    ]


# ---------------------------------------------------------------------------
# (b) Structural Extraction F1 Reward
# ---------------------------------------------------------------------------

def structural_f1_reward(prompts, completions, **kwargs) -> list[float]:
    """Relation extraction F1 with partial matching.

    Partial match scoring: head correct +0.33, tail +0.33, relation +0.34.
    Required kwargs: gold_relations.
    """
    gold_relations_raw = kwargs.get("gold_relations", [])
    rewards: list[float] = []

    for idx, completion in enumerate(completions):
        parsed = parse_json_output(completion)
        if parsed is None or "relations" not in parsed:
            rewards.append(0.0)
            continue

        gold_rels = _deserialize(gold_relations_raw[idx])
        pred_rels = parsed["relations"]

        if not gold_rels:
            rewards.append(1.0 if not pred_rels else 0.0)
            continue

        gold_triples = set()
        for gr in gold_rels:
            gold_triples.add(
                (gr["head"].lower(), gr["tail"].lower(), gr["relation"].lower())
            )

        total_pred_score = 0.0
        matched_gold: set[tuple] = set()

        for pr in pred_rels:
            ph = pr.get("head", "").lower()
            pt = pr.get("tail", "").lower()
            prr = pr.get("relation", "").lower()

            best_score = 0.0
            best_match = None
            for gt in gold_triples:
                s = 0.0
                if ph == gt[0]:
                    s += 0.33
                if pt == gt[1]:
                    s += 0.33
                if prr == gt[2]:
                    s += 0.34
                if s > best_score:
                    best_score = s
                    best_match = gt

            total_pred_score += best_score
            # Count as matched if at least 2 of 3 fields match
            if best_match and best_score >= 0.66:
                matched_gold.add(best_match)

        precision = total_pred_score / len(pred_rels) if pred_rels else 0.0
        recall = len(matched_gold) / len(gold_triples)
        f1 = (
            2 * precision * recall / (precision + recall)
            if (precision + recall) > 0
            else 0.0
        )
        rewards.append(f1)

    return rewards


# ---------------------------------------------------------------------------
# (c) Format Compliance Reward
# ---------------------------------------------------------------------------

def format_compliance_reward(prompts, completions, **kwargs) -> list[float]:
    """JSON validity + schema conformance.

    Scoring: valid JSON +0.5, has "relations" key +0.2,
    each relation has head/tail/relation/evidence +0.3 (proportional).
    """
    required_fields = {"head", "tail", "relation", "evidence"}
    rewards: list[float] = []

    for completion in completions:
        score = 0.0
        parsed = parse_json_output(completion)

        if parsed is not None:
            score += 0.5
            if "relations" in parsed:
                score += 0.2
                rels = parsed["relations"]
                if isinstance(rels, list) and rels:
                    valid = sum(
                        1 for r in rels
                        if isinstance(r, dict) and required_fields.issubset(r.keys())
                    )
                    score += 0.3 * (valid / len(rels))
                elif isinstance(rels, list):
                    score += 0.3  # empty list is schema-compliant

        rewards.append(score)

    return rewards


# ---------------------------------------------------------------------------
# Composite Reward
# ---------------------------------------------------------------------------

def composite_reward(prompts, completions, **kwargs) -> list[float]:
    """Weighted sum of provenance, structural, and format rewards.

    Weight overrides via kwargs: w_provenance, w_structural, w_format.
    """
    w_prov = kwargs.get("w_provenance", 0.4)
    w_struct = kwargs.get("w_structural", 0.4)
    w_fmt = kwargs.get("w_format", 0.2)

    prov = provenance_fidelity_reward(prompts, completions, **kwargs)
    struct = structural_f1_reward(prompts, completions, **kwargs)
    fmt = format_compliance_reward(prompts, completions, **kwargs)

    return [
        w_prov * p + w_struct * s + w_fmt * f
        for p, s, f in zip(prov, struct, fmt)
    ]
