"""Merge predictions across SDGD batches.

Input: Per-batch extraction results (list of list of entity dicts)
Output: Merged, deduplicated predictions per sample
Dependencies: none
"""
import logging
from typing import Dict, List, Tuple

logger = logging.getLogger(__name__)


def merge_predictions(
    batch_results: List[List[Dict]],
    task: str = "ner",
) -> List[Dict]:
    """Merge predictions from multiple batches via simple union + dedup.

    Each batch_result is a list of entity dicts: [{"text": ..., "type": ...}, ...]
    Deduplicates exact (text.lower(), type) matches.

    Args:
        batch_results: list of per-batch prediction lists
        task: task type (currently only "ner" supported)

    Returns:
        Deduplicated list of entity dicts
    """
    seen: set = set()
    merged: List[Dict] = []

    for preds in batch_results:
        for ent in preds:
            key = _dedup_key(ent, task)
            if key not in seen:
                seen.add(key)
                merged.append(ent)

    return merged


def _dedup_key(entity: Dict, task: str = "ner") -> Tuple:
    """Create deduplication key for an entity."""
    text = entity.get("text", "").strip().lower()
    etype = entity.get("type", "").strip()
    return (text, etype)


def merge_all_samples(
    all_batch_results: List[Dict],
    n_samples: int,
) -> List[List[Dict]]:
    """Merge predictions across batches for all samples.

    Args:
        all_batch_results: flat list of {sample_id, batch_id, predictions, ...}
        n_samples: total number of samples

    Returns:
        List of length n_samples, each element is merged predictions for that sample
    """
    per_sample: Dict[int, List[List[Dict]]] = {i: [] for i in range(n_samples)}
    for result in all_batch_results:
        sid = result["sample_id"]
        if sid in per_sample:
            per_sample[sid].append(result.get("predictions", []))

    merged = []
    for i in range(n_samples):
        merged.append(merge_predictions(per_sample[i]))

    return merged


def merge_with_confidence(
    all_batch_results: List[Dict],
    n_samples: int,
    confidence_threshold: float = -1.0,
    conflict_strategy: str = "highest_confidence",
) -> List[List[Dict]]:
    """Confidence-gated merge: filter by logprob and resolve cross-batch conflicts.

    For each sample:
      1. Collect predictions from all batches, each annotated with confidence
      2. Drop predictions below confidence_threshold
      3. For spans predicted in multiple batches with different types,
         keep only the highest-confidence assignment

    Args:
        all_batch_results: flat list of {sample_id, batch_id, predictions, ...}
            Each prediction dict must have "confidence" key (cumulative logprob
            or normalized sequence score from vLLM).
        n_samples: total number of samples
        confidence_threshold: minimum confidence to keep a prediction.
            Logprob scale (e.g., -2.0 means keep if logprob > -2.0).
        conflict_strategy: how to resolve same-span different-type conflicts.
            "highest_confidence" (default) | "drop_all"

    Returns:
        List of length n_samples, each element is filtered+merged predictions.

    NOTE: requires sdgd_extract_gpu.py to pass logprobs in SamplingParams
    and attach per-entity or per-sequence confidence to each prediction dict.

    Implementation sketch:
        1. Enable logprobs in SamplingParams:
             SamplingParams(..., logprobs=1)
           Then output.outputs[0].cumulative_logprob gives sequence-level score.
        2. For structured output, normalize by sequence length:
             confidence = cumulative_logprob / n_tokens
        3. Attach to each entity: {"text": ..., "type": ..., "confidence": ...}
    """
    per_sample: Dict[int, List[List[Dict]]] = {i: [] for i in range(n_samples)}
    for result in all_batch_results:
        sid = result["sample_id"]
        if sid in per_sample:
            per_sample[sid].append(result.get("predictions", []))

    merged = []
    for i in range(n_samples):
        span_best: Dict[str, Dict] = {}  # span_text -> best entity dict
        for preds in per_sample[i]:
            for ent in preds:
                conf = ent.get("confidence", 0.0)
                if conf < confidence_threshold:
                    continue
                span_key = ent.get("text", "").strip().lower()
                if span_key not in span_best:
                    span_best[span_key] = ent
                else:
                    if conflict_strategy == "highest_confidence":
                        if conf > span_best[span_key].get("confidence", 0.0):
                            span_best[span_key] = ent
                    elif conflict_strategy == "drop_all":
                        existing_type = span_best[span_key].get("type", "")
                        if ent.get("type", "") != existing_type:
                            span_best.pop(span_key, None)
        merged.append(list(span_best.values()))

    return merged
