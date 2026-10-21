"""SDGD-specific evaluation: decomposition stats and baseline comparison.

Input: SDGD predictions, baseline predictions, gold labels
Output: Comparative metrics and decomposition statistics
Dependencies: torch
"""
import logging
from typing import Dict, List, Optional, Set

import torch

logger = logging.getLogger(__name__)


def compute_f1(predictions: List[List[Dict]], gold: List[List[Dict]]) -> Dict:
    """Compute micro P/R/F1 using text-match (case-insensitive).

    Args:
        predictions: per-sample list of predicted entities [{"text": ..., "type": ...}]
        gold: per-sample list of gold entities

    Returns:
        Dict with precision, recall, f1, tp, pred_count, gold_count
    """
    tp = 0
    total_pred = 0
    total_gold = 0

    for preds, golds in zip(predictions, gold):
        pred_set = {(e["text"].strip().lower(), e["type"]) for e in preds}
        gold_set = {(e["text"].strip().lower(), e["type"]) for e in golds}
        tp += len(pred_set & gold_set)
        total_pred += len(pred_set)
        total_gold += len(gold_set)

    p = tp / total_pred if total_pred > 0 else 0.0
    r = tp / total_gold if total_gold > 0 else 0.0
    f1 = 2 * p * r / (p + r) if (p + r) > 0 else 0.0

    return {"precision": p, "recall": r, "f1": f1,
            "tp": tp, "pred_count": total_pred, "gold_count": total_gold}


def compare_with_baseline(
    sdgd_preds: List[List[Dict]],
    baseline_preds: List[List[Dict]],
    gold: List[List[Dict]],
) -> Dict:
    """Compare SDGD vs baseline on F1/P/R.

    Returns:
        Dict with sdgd_metrics, baseline_metrics, and deltas
    """
    sdgd_m = compute_f1(sdgd_preds, gold)
    base_m = compute_f1(baseline_preds, gold)
    delta = {k: sdgd_m[k] - base_m[k] for k in ["precision", "recall", "f1"]}

    return {"sdgd": sdgd_m, "baseline": base_m, "delta": delta}


def report_decomposition_stats(
    batches: Dict[int, List[str]],
    sim_matrix: torch.Tensor,
    type_names: List[str],
) -> Dict:
    """Report intra-batch and inter-batch similarity statistics.

    Args:
        batches: color_id -> list of type names
        sim_matrix: [N, N] similarity matrix
        type_names: ordered type names matching sim_matrix indices

    Returns:
        Dict with per-batch and aggregate statistics
    """
    name_to_idx = {name: i for i, name in enumerate(type_names)}

    per_batch = []
    all_intra = []
    for color_id, types in sorted(batches.items()):
        indices = [name_to_idx[t] for t in types]
        max_sim = 0.0
        sims = []
        for i in range(len(indices)):
            for j in range(i + 1, len(indices)):
                s = sim_matrix[indices[i], indices[j]].item()
                sims.append(s)
                max_sim = max(max_sim, s)
        all_intra.extend(sims)

        per_batch.append({
            "color_id": color_id,
            "n_types": len(types),
            "types": types,
            "max_intra_sim": max_sim,
            "mean_intra_sim": sum(sims) / len(sims) if sims else 0.0,
        })

    return {
        "n_batches": len(batches),
        "per_batch": per_batch,
        "global_max_intra_sim": max(all_intra) if all_intra else 0.0,
        "global_mean_intra_sim": sum(all_intra) / len(all_intra) if all_intra else 0.0,
    }
