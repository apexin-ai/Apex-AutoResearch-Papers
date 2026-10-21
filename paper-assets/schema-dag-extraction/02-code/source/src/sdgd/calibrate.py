"""SDGD-cal: empirical confusion-based type decomposition.

Replaces embedding cosine similarity (SDGD-zero) with an empirical confusion
matrix built from calibration samples. Addresses proxy failure on same-domain
schemas (e.g. MAVEN 168 event types) where embedding compression makes
cosine similarity unreliable.

Pipeline: run_calibration() -> build_confusion_matrix() -> confusion_to_similarity()
          -> (reuse SDGD-zero graph coloring infrastructure)
"""
import json
import logging
from collections import defaultdict
from typing import Dict, List, Optional, Tuple

import numpy as np

logger = logging.getLogger(__name__)


def build_confusion_matrix(
    predictions: List[List[Dict]],
    gold_labels: List[List[Dict]],
    type_list: List[str],
    task: str = "ner",
) -> np.ndarray:
    """Build empirical confusion matrix from calibration predictions vs gold.

    For NER/Event: match gold entities to predictions by text overlap.
    For RE: direct comparison of gold relation_type vs predicted relation
    (each sample has exactly one relation).

    Args:
        predictions: per-sample predicted items
        gold_labels: per-sample gold items
        type_list: ordered list of type names
        task: 'ner', 'event', or 're'

    Returns:
        confusion_matrix: (n_types, n_types) — C[i][j] = count of gold type i predicted as type j
    """
    n = len(type_list)
    type_to_idx = {t: i for i, t in enumerate(type_list)}
    C = np.zeros((n, n), dtype=np.float64)

    for sample_preds, sample_golds in zip(predictions, gold_labels):
        if task == "re":
            gold_rel = sample_golds[0].get("relation_type", "") if sample_golds else ""
            pred_rel = sample_preds[0].get("relation", "") if sample_preds else ""
            if gold_rel in type_to_idx and pred_rel in type_to_idx:
                C[type_to_idx[gold_rel]][type_to_idx[pred_rel]] += 1
            continue

        for gold_ent in sample_golds:
            gold_type = gold_ent.get("type", "")
            if gold_type not in type_to_idx:
                continue
            gold_text = gold_ent.get("text", "").strip().lower()
            if not gold_text:
                continue

            best_pred = _find_best_overlap(gold_ent, sample_preds)
            if best_pred is None:
                continue

            pred_type = best_pred.get("type", "")
            if pred_type not in type_to_idx:
                continue

            gi = type_to_idx[gold_type]
            pi = type_to_idx[pred_type]
            C[gi][pi] += 1

    logger.info(
        "Confusion matrix: %d types, %d total confusions (off-diagonal), %d correct (diagonal)",
        n,
        int(C.sum() - np.trace(C)),
        int(np.trace(C)),
    )
    return C


def _find_best_overlap(
    gold_entity: Dict, predictions: List[Dict]
) -> Optional[Dict]:
    """Find predicted entity with maximum character overlap to gold entity."""
    gold_text = gold_entity.get("text", "").strip().lower()
    if not gold_text:
        return None

    best = None
    best_overlap = 0

    for pred in predictions:
        pred_text = pred.get("text", "").strip().lower()
        if not pred_text:
            continue
        overlap = _char_overlap(gold_text, pred_text)
        if overlap > best_overlap:
            best_overlap = overlap
            best = pred

    if best_overlap == 0:
        return None
    return best


def _char_overlap(a: str, b: str) -> int:
    """Character-level overlap: length of longest common substring."""
    if len(a) > len(b):
        a, b = b, a
    if a in b:
        return len(a)
    if b in a:
        return len(b)
    # simple: check if one is substring of the other, else use set intersection as proxy
    overlap = len(set(a) & set(b))
    # weighted by min length to prefer exact/near matches
    return overlap if overlap > len(a) * 0.5 else 0


def confusion_to_similarity(
    confusion_matrix: np.ndarray,
    normalize: str = "symmetric",
) -> np.ndarray:
    """Convert confusion matrix to similarity matrix compatible with SDGD graph pipeline.

    Args:
        confusion_matrix: (n, n) raw counts
        normalize: 'symmetric' or 'row'
            symmetric: sim[i][j] = (C[i][j] + C[j][i]) / (sum(C[i,:]) + sum(C[j,:]))
            row: sim[i][j] = C[i][j] / sum(C[i,:])

    Returns:
        similarity_matrix: (n, n) in [0, 1], diagonal = 0
    """
    C = confusion_matrix.astype(np.float64)
    n = C.shape[0]
    sim = np.zeros((n, n), dtype=np.float64)

    if normalize == "symmetric":
        row_sums = C.sum(axis=1)
        for i in range(n):
            for j in range(i + 1, n):
                denom = row_sums[i] + row_sums[j]
                if denom > 0:
                    sim[i][j] = (C[i][j] + C[j][i]) / denom
                    sim[j][i] = sim[i][j]
    elif normalize == "row":
        row_sums = C.sum(axis=1)
        for i in range(n):
            if row_sums[i] > 0:
                sim[i] = C[i] / row_sums[i]
        # symmetrize for graph construction
        sim = (sim + sim.T) / 2.0
    else:
        raise ValueError(f"Unknown normalize mode: {normalize}")

    np.fill_diagonal(sim, 0.0)

    # rescale to [0, 1] based on off-diagonal max
    off_diag = sim[~np.eye(n, dtype=bool)]
    if off_diag.max() > 0:
        sim = sim / off_diag.max()
    np.fill_diagonal(sim, 0.0)

    logger.info(
        "Confusion -> similarity: normalize=%s, max=%.4f, mean=%.4f, nonzero=%d/%d",
        normalize,
        sim.max(),
        sim[~np.eye(n, dtype=bool)].mean(),
        (sim > 0).sum() - n,  # exclude diagonal
        n * (n - 1),
    )
    return sim


def run_calibration(
    data_samples: List[Dict],
    type_list: List[str],
    type_definitions: Dict[str, str],
    model_path: str,
    task: str = "ner",
    n_samples: int = 100,
    prompt_version: str = "v2",
    max_model_len: int = 4096,
    dataset: str = "fewnerd",
) -> Tuple[np.ndarray, np.ndarray]:
    """Run single-pass calibration on a sample subset to collect empirical confusion.

    This is SDGD-cal step 0: infer all types on a small calibration set,
    then build the confusion matrix. Requires GPU (vLLM).

    Args:
        data_samples: calibration data (will use first n_samples)
        type_list: all type names
        type_definitions: type_name -> description
        model_path: vLLM model path
        task: 'ner', 'event', or 're'
        n_samples: number of calibration samples
        prompt_version: prompt version
        max_model_len: vLLM max_model_len
        dataset: dataset name

    Returns:
        (confusion_matrix, similarity_matrix) as numpy arrays
    """
    import sys
    from pathlib import Path
    sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

    cal_samples = data_samples[:n_samples]
    logger.info("Running calibration on %d samples with %d types", len(cal_samples), len(type_list))

    # single-pass extraction with all types
    if task == "re":
        from run_extraction import build_json_schema_re, build_prompt_v2_re
        schema_fn = build_json_schema_re
        prompt_fn = None
    elif task == "event":
        from run_extraction import build_json_schema_v2
        schema_fn = build_json_schema_v2
        if prompt_version == "v2":
            from run_extraction import build_prompt_v2_event
            prompt_fn = build_prompt_v2_event
        else:
            from run_extraction import build_prompt_v1_event
            prompt_fn = build_prompt_v1_event
    else:
        if prompt_version == "v2":
            from run_extraction import build_json_schema_v2, build_prompt_v2
            schema_fn = build_json_schema_v2
            prompt_fn = build_prompt_v2
        else:
            from run_extraction import build_json_schema_v1, build_prompt_v1
            schema_fn = build_json_schema_v1
            prompt_fn = build_prompt_v1

    from vllm import LLM, SamplingParams
    from vllm.sampling_params import StructuredOutputsParams

    llm = LLM(
        model=model_path,
        dtype="bfloat16",
        gpu_memory_utilization=0.95,
        enforce_eager=True,
        max_model_len=max_model_len,
        trust_remote_code=True,
        disable_log_stats=True,
    )

    batch_schema = schema_fn(type_list)
    structured_params = StructuredOutputsParams(json=batch_schema)
    sampling_params = SamplingParams(
        max_tokens=1024, temperature=0.0, structured_outputs=structured_params,
    )

    if task == "re":
        prompts = [
            build_prompt_v2_re(s["text"], s["head_entity"], s["tail_entity"],
                               type_definitions, type_list)
            for s in cal_samples
        ]
    else:
        prompts = [prompt_fn(s["text"], type_definitions, type_list) for s in cal_samples]

    outputs = llm.generate(prompts, sampling_params)

    predictions = []
    for output in outputs:
        try:
            preds = json.loads(output.outputs[0].text)
        except json.JSONDecodeError:
            preds = {}
        if task == "re":
            rel = preds.get("relation", "") if isinstance(preds, dict) else ""
            predictions.append([{"relation": rel}])
        else:
            if isinstance(preds, dict):
                preds = preds.get("entities", [])
            predictions.append(preds if isinstance(preds, list) else [])

    gold_labels = []
    for s in cal_samples:
        if task == "re":
            gold_labels.append([{"relation_type": s.get("relation_type", "")}])
        else:
            gold_labels.append(s.get("entities", []))

    C = build_confusion_matrix(predictions, gold_labels, type_list, task=task)
    sim = confusion_to_similarity(C, normalize="symmetric")

    logger.info("Calibration complete: confusion shape=%s", C.shape)
    return C, sim
