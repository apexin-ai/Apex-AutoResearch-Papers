"""Evaluate NER extraction results against ground truth.

v2 changes (2026-05-14): Added text_match eval mode (no offset dependency).

Input: Extraction results JSON, Few-NERD ground truth
Output: Per-batch metrics JSON (F1, precision, recall, BCS)
Dependencies: few_nerd_utils
"""
import argparse
import json
import logging
import sys
from pathlib import Path
from typing import Dict, List, Set

logger = logging.getLogger(__name__)


def load_predictions(path: str) -> List[Dict]:
    with open(path, "r") as f:
        return json.load(f)


def _exact_match(pred: Dict, gold: Dict, source_text: str = None) -> bool:
    """Exact span match: start, end, and type must all match."""
    return (pred.get("start") == gold["start"]
            and pred.get("end") == gold["end"]
            and pred.get("type") == gold["type"])


def _relaxed_match(pred: Dict, gold: Dict, source_text: str = None) -> bool:
    """Relaxed match: type must match and text spans must overlap."""
    if pred.get("type") != gold["type"]:
        return False
    p_start, p_end = pred.get("start", -1), pred.get("end", -1)
    g_start, g_end = gold["start"], gold["end"]
    return p_start < g_end and p_end > g_start


def _text_match(pred: Dict, gold: Dict, source_text: str = None) -> bool:
    """Text-based match: type must match, texts must overlap via substring.

    Validates pred text appears in source text (not hallucinated).
    Match if either text contains the other (handles boundary differences).
    """
    if pred.get("type") != gold["type"]:
        return False
    pred_text = pred.get("text", "").strip()
    gold_text = gold.get("text", "").strip()
    if not pred_text or not gold_text:
        return False
    if source_text and pred_text.lower() not in source_text.lower():
        return False
    pred_lower = pred_text.lower()
    gold_lower = gold_text.lower()
    return pred_lower == gold_lower or pred_lower in gold_lower or gold_lower in pred_lower


def compute_metrics(
    predictions: List[Dict],
    ground_truth,
    samples: List[Dict],
    batch_types: Set[str],
    match_fn=_exact_match,
) -> Dict:
    """Compute micro P/R/F1 for a single batch across all samples.

    Args:
        predictions: List of result dicts for this batch (one per sample).
        ground_truth: Unused (kept for API compat).
        samples: Original dataset samples (with entities and text).
        batch_types: Set of type names in this batch.
        match_fn: Matching function signature: (pred, gold, source_text=None) -> bool.

    Returns:
        Dict with precision, recall, f1, and counts.
    """
    total_tp = 0
    total_pred = 0
    total_gold = 0

    pred_by_sample = {}
    for p in predictions:
        pred_by_sample.setdefault(p["sample_id"], []).append(p)

    for sid, pred_entries in pred_by_sample.items():
        if sid >= len(samples):
            continue

        gold_entities = [e for e in samples[sid]["entities"] if e["type"] in batch_types]
        total_gold += len(gold_entities)

        # Collect all predicted entities (take the first entry for this sample/batch)
        pred_entities = pred_entries[0].get("predictions", [])
        # Filter predictions to batch types
        pred_entities = [p for p in pred_entities if p.get("type") in batch_types]
        total_pred += len(pred_entities)

        source_text = samples[sid].get("text", "")

        # Greedy matching: each gold can match at most one pred
        matched_gold = set()
        for pred in pred_entities:
            for gi, gold in enumerate(gold_entities):
                if gi not in matched_gold and match_fn(pred, gold, source_text=source_text):
                    total_tp += 1
                    matched_gold.add(gi)
                    break

    precision = total_tp / total_pred if total_pred > 0 else 0.0
    recall = total_tp / total_gold if total_gold > 0 else 0.0
    f1 = 2 * precision * recall / (precision + recall) if (precision + recall) > 0 else 0.0

    return {
        "precision": precision,
        "recall": recall,
        "f1": f1,
        "tp": total_tp,
        "total_pred": total_pred,
        "total_gold": total_gold,
    }


def evaluate_all(predictions: List[Dict], samples: List[Dict], eval_mode: str = "all") -> Dict:
    """Evaluate all batches in the predictions file.

    Args:
        predictions: List of prediction result dicts.
        samples: Original dataset samples.
        eval_mode: "exact", "relaxed", "text_match", or "all" (default).

    Returns:
        Dict mapping batch_id -> metrics dict.
    """
    batches = {}
    for p in predictions:
        bid = p["batch_id"]
        if bid not in batches:
            batches[bid] = {
                "entries": [],
                "batch_types": set(p["batch_types"]),
                "batch_bcs": p.get("batch_bcs", 0.0),
                "count_key": p.get("count_key", ""),
                "num_types": len(p["batch_types"]),
            }
        batches[bid]["entries"].append(p)

    mode_fns = {}
    if eval_mode in ("all", "exact"):
        mode_fns["exact"] = _exact_match
    if eval_mode in ("all", "relaxed"):
        mode_fns["relaxed"] = _relaxed_match
    if eval_mode in ("all", "text_match"):
        mode_fns["text_match"] = _text_match

    results = {}
    for bid, info in batches.items():
        batch_types = info["batch_types"]
        result_entry = {
            "bcs": info["batch_bcs"],
            "count_key": info["count_key"],
            "num_types": info["num_types"],
            "num_samples": len(set(e["sample_id"] for e in info["entries"])),
        }

        for mode_name, fn in mode_fns.items():
            result_entry[mode_name] = compute_metrics(
                info["entries"], None, samples, batch_types, fn
            )

        # Per-type exact F1 breakdown (for backward compat with analysis code)
        if "exact" in mode_fns:
            per_type_f1 = {}
            for t in batch_types:
                t_metrics = compute_metrics(info["entries"], None, samples, {t}, _exact_match)
                per_type_f1[t] = t_metrics["f1"]
            result_entry["per_type_f1"] = per_type_f1

        results[bid] = result_entry

    return results


def main():
    parser = argparse.ArgumentParser(description="Evaluate NER extraction results")
    parser.add_argument("--predictions_path", required=True, help="Extraction results JSON")
    parser.add_argument("--data_dir", default="./data", help="Data directory")
    parser.add_argument("--output_path", required=True, help="Output evaluation JSON")
    parser.add_argument("--max_samples", type=int, default=None, help="Max samples (must match extraction)")
    parser.add_argument("--eval_mode", choices=["exact", "relaxed", "text_match", "all"],
                        default="all", help="Evaluation mode (default: all)")
    args = parser.parse_args()

    logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")

    sys.path.insert(0, str(Path(__file__).parent))
    from few_nerd_utils import load_few_nerd

    predictions = load_predictions(args.predictions_path)
    samples = load_few_nerd(split="test", max_samples=args.max_samples)

    results = evaluate_all(predictions, samples, eval_mode=args.eval_mode)

    Path(args.output_path).parent.mkdir(parents=True, exist_ok=True)
    with open(args.output_path, "w") as f:
        json.dump(results, f, indent=2)

    logger.info("Evaluation results for %d batches:", len(results))
    for bid, metrics in sorted(results.items()):
        parts = [bid + ":"]
        if "exact" in metrics:
            parts.append("exact_F1=%.4f" % metrics["exact"]["f1"])
        if "relaxed" in metrics:
            parts.append("relaxed_F1=%.4f" % metrics["relaxed"]["f1"])
        if "text_match" in metrics:
            parts.append("text_match_F1=%.4f" % metrics["text_match"]["f1"])
        parts.append("BCS=%.4f" % metrics["bcs"])
        logger.info("  %s", "  ".join(parts))


if __name__ == "__main__":
    main()
