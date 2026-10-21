"""Evaluation metrics for commitment point detection.

Metrics:
- Step-level accuracy
- Earliest reliable detection point
- Detection lead time (how early before commitment point)
"""

from typing import List, Dict, Optional, Tuple
import numpy as np

from ..config import DETECTION_THRESHOLD, DETECTION_WINDOW


def step_accuracy(predictions: np.ndarray, labels: np.ndarray) -> float:
    """Overall step-level accuracy."""
    return float((predictions == labels).mean())


def earliest_reliable_detection(
    probs: np.ndarray,
    labels: np.ndarray,
    threshold: float = DETECTION_THRESHOLD,
    window: int = DETECTION_WINDOW,
) -> Optional[int]:
    """Find first position where model reliably detects post-commitment.

    Scans from trace start, finds first position where consecutive `window` steps
    all have predicted prob > threshold AND predictions are correct.

    Returns step index or None if never reliably detected.
    """
    n = len(probs)
    if n < window:
        return None

    for i in range(n - window + 1):
        segment_probs = probs[i:i + window]
        segment_labels = labels[i:i + window]

        # All probs above threshold
        if not np.all(segment_probs > threshold):
            continue

        # All predictions correct (prob > 0.5 means predict class 1)
        segment_preds = (segment_probs > 0.5).astype(int)
        if not np.all(segment_preds == segment_labels):
            continue

        return i

    return None


def first_crossing_point(
    probs_class1: np.ndarray,
    threshold: float = 0.5,
    consecutive_k: int = DETECTION_WINDOW,
) -> Optional[int]:
    """First position where prob(post-commitment) > threshold for K consecutive steps.

    Unlike earliest_reliable_detection, this does NOT check against ground-truth labels,
    so crossings before the commitment point measure anticipation ability.
    """
    n = len(probs_class1)
    if n < consecutive_k:
        return None
    for i in range(n - consecutive_k + 1):
        if all(p > threshold for p in probs_class1[i:i + consecutive_k]):
            return i
    return None


def detection_lead_time(earliest_detection: Optional[int], commitment_point: int) -> Optional[int]:
    """Compute how many steps before commitment the detection occurs.

    lead_time = commitment_point - earliest_detection
    Positive = detected before commitment (good)
    Negative = detected after commitment (late)
    None = never detected
    """
    if earliest_detection is None:
        return None
    return commitment_point - earliest_detection


def evaluate_trace(
    probs: np.ndarray,
    labels: np.ndarray,
    commitment_point: int,
    threshold: float = DETECTION_THRESHOLD,
    window: int = DETECTION_WINDOW,
) -> Dict:
    """Evaluate a single trace."""
    preds = (probs > 0.5).astype(int)
    acc = step_accuracy(preds, labels)
    erd = earliest_reliable_detection(probs, labels, threshold, window)
    lead = detection_lead_time(erd, commitment_point)
    fcp = first_crossing_point(probs, threshold=0.5, consecutive_k=window)
    fcp_lead = detection_lead_time(fcp, commitment_point)

    return {
        "step_accuracy": acc,
        "earliest_reliable_detection": erd,
        "detection_lead_time": lead,
        "first_crossing_point": fcp,
        "first_crossing_lead_time": fcp_lead,
        "commitment_point": commitment_point,
        "num_steps": len(labels),
    }


def evaluate_all(
    predictions_static: List[Dict],
    predictions_temporal: List[Dict],
    threshold: float = DETECTION_THRESHOLD,
    window: int = DETECTION_WINDOW,
) -> Dict:
    """Evaluate and compare static vs temporal probes across all test traces."""

    def _eval_predictions(predictions, name):
        results = []
        for pred in predictions:
            if pred["commitment_point"] is None:
                continue
            res = evaluate_trace(
                pred["probs"], pred["labels"],
                pred["commitment_point"], threshold, window
            )
            res["trace_id"] = pred["trace_id"]
            results.append(res)

        if not results:
            return {"name": name, "n_traces": 0}

        accs = [r["step_accuracy"] for r in results]
        leads = [r["detection_lead_time"] for r in results if r["detection_lead_time"] is not None]
        erds = [r["earliest_reliable_detection"] for r in results if r["earliest_reliable_detection"] is not None]
        fcp_leads = [r["first_crossing_lead_time"] for r in results if r["first_crossing_lead_time"] is not None]
        fcps = [r["first_crossing_point"] for r in results if r["first_crossing_point"] is not None]

        summary = {
            "name": name,
            "n_traces": len(results),
            "step_accuracy_mean": float(np.mean(accs)),
            "step_accuracy_std": float(np.std(accs)),
            "detection_rate": len(erds) / len(results),
            "lead_time_mean": float(np.mean(leads)) if leads else None,
            "lead_time_median": float(np.median(leads)) if leads else None,
            "lead_time_std": float(np.std(leads)) if leads else None,
            "erd_mean": float(np.mean(erds)) if erds else None,
            "crossing_rate": len(fcps) / len(results),
            "crossing_lead_time_mean": float(np.mean(fcp_leads)) if fcp_leads else None,
            "crossing_lead_time_median": float(np.median(fcp_leads)) if fcp_leads else None,
            "per_trace": results,
        }
        return summary

    static_summary = _eval_predictions(predictions_static, "static_probe")
    temporal_summary = _eval_predictions(predictions_temporal, "temporal_probe")

    # Print comparison
    print("\n" + "="*60)
    print("EVALUATION RESULTS")
    print("="*60)

    for s in [static_summary, temporal_summary]:
        if s["n_traces"] == 0:
            print(f"\n{s['name']}: No traces evaluated")
            continue
        print(f"\n{s['name']} ({s['n_traces']} traces):")
        print(f"  Step accuracy:      {s['step_accuracy_mean']:.4f} ± {s['step_accuracy_std']:.4f}")
        print(f"  Detection rate:     {s['detection_rate']:.2%}")
        if s["lead_time_mean"] is not None:
            print(f"  Lead time (mean):   {s['lead_time_mean']:.1f} steps")
            print(f"  Lead time (median): {s['lead_time_median']:.1f} steps")
        if s["erd_mean"] is not None:
            print(f"  Earliest detection: {s['erd_mean']:.1f} (mean step)")
        print(f"  Crossing rate:      {s['crossing_rate']:.2%}")
        if s["crossing_lead_time_mean"] is not None:
            print(f"  Crossing lead (mean):   {s['crossing_lead_time_mean']:.1f} steps")
            print(f"  Crossing lead (median): {s['crossing_lead_time_median']:.1f} steps")

    print("\n" + "="*60)

    return {
        "static": static_summary,
        "temporal": temporal_summary,
    }
