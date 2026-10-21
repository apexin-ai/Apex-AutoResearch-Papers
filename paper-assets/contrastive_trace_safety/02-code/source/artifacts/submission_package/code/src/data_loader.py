"""Load HarmThoughts dataset and extract commitment points.

Input: HuggingFace dataset "ishitakakkar-10/HarmThoughts"
Output: List of trace dicts with sentences, labels, commitment_point, split assignments
"""

from collections import defaultdict
from typing import List, Optional, Dict, Any
import numpy as np
from datasets import load_dataset

from .config import (
    HF_DATASET, TARGET_MODEL, SAFETY_LABELS,
    TRAIN_RATIO, VAL_RATIO, SEED
)


def load_harmthoughts(model_name: str = TARGET_MODEL) -> Dict[str, List[Dict]]:
    """Load HarmThoughts from HF and group by trace_id."""
    ds = load_dataset(HF_DATASET, split="train")

    traces = defaultdict(list)
    for row in ds:
        if row["model_name"] != model_name:
            continue
        # trace_id is the part before the last dash in sentence_id
        sid = row["sentence_id"]
        parts = sid.rsplit("-", 1)
        trace_id = parts[0]
        step_idx = int(parts[1]) - 1  # convert to 0-indexed

        traces[trace_id].append({
            "sentence_id": sid,
            "step_idx": step_idx,
            "sentence": row["sentence"],
            "label": row["llm_annotation"],
            "query": row["query"],
            "final_judgment": row["final_judgment"],
        })

    # Sort each trace by step_idx
    for tid in traces:
        traces[tid].sort(key=lambda x: x["step_idx"])

    return dict(traces)


def extract_commitment_point(labels: List[str]) -> Optional[int]:
    """Find the commitment point in a sequence of labels.

    Returns the index after the last safety label, or None if:
    - No safety labels exist in the trace
    - The last safety label is at the final position (no post-commitment segment)
    """
    last_safety_idx = None
    for i, label in enumerate(labels):
        if label in SAFETY_LABELS:
            last_safety_idx = i

    if last_safety_idx is None:
        return None
    if last_safety_idx == len(labels) - 1:
        return None

    return last_safety_idx + 1


def create_step_labels(commitment_point: int, num_steps: int) -> List[int]:
    """Generate binary labels: 0 = pre-commitment, 1 = post-commitment."""
    return [0 if i < commitment_point else 1 for i in range(num_steps)]


def prepare_dataset(model_name: str = TARGET_MODEL) -> Dict[str, List[Dict[str, Any]]]:
    """Load data, compute commitment points, categorize traces.

    Returns dict with keys:
    - jailbreak_with_commitment: traces for training/evaluation
    - jailbreak_no_commitment: excluded jailbreak traces
    - safe: safe traces for FP evaluation
    """
    raw_traces = load_harmthoughts(model_name)

    jailbreak_with_commitment = []
    jailbreak_no_commitment = []
    safe_traces = []

    for trace_id, steps in raw_traces.items():
        is_jailbreak = steps[0]["final_judgment"] == 1.0
        labels = [s["label"] for s in steps]
        sentences = [s["sentence"] for s in steps]
        query = steps[0]["query"]
        num_steps = len(steps)

        trace_dict = {
            "trace_id": trace_id,
            "sentences": sentences,
            "labels": labels,
            "query": query,
            "is_jailbreak": is_jailbreak,
            "num_steps": num_steps,
        }

        if not is_jailbreak:
            trace_dict["commitment_point"] = None
            trace_dict["step_labels"] = None
            safe_traces.append(trace_dict)
            continue

        cp = extract_commitment_point(labels)
        trace_dict["commitment_point"] = cp

        if cp is not None:
            trace_dict["step_labels"] = create_step_labels(cp, num_steps)
            jailbreak_with_commitment.append(trace_dict)
        else:
            trace_dict["step_labels"] = None
            jailbreak_no_commitment.append(trace_dict)

    return {
        "jailbreak_with_commitment": jailbreak_with_commitment,
        "jailbreak_no_commitment": jailbreak_no_commitment,
        "safe": safe_traces,
    }


def split_data(traces: List[Dict], train_ratio: float = TRAIN_RATIO,
               val_ratio: float = VAL_RATIO, seed: int = SEED):
    """Split traces into train/val/test at trace level."""
    rng = np.random.default_rng(seed)
    indices = rng.permutation(len(traces))

    n_train = int(len(traces) * train_ratio)
    n_val = int(len(traces) * val_ratio)

    train_idx = indices[:n_train]
    val_idx = indices[n_train:n_train + n_val]
    test_idx = indices[n_train + n_val:]

    train = [traces[i] for i in train_idx]
    val = [traces[i] for i in val_idx]
    test = [traces[i] for i in test_idx]

    return train, val, test


def get_commitment_point_stats(traces: List[Dict]) -> Dict[str, Any]:
    """Compute statistics about commitment point distribution."""
    cps = [t["commitment_point"] for t in traces if t["commitment_point"] is not None]
    num_steps_list = [t["num_steps"] for t in traces if t["commitment_point"] is not None]

    if not cps:
        return {"count": 0}

    cps = np.array(cps)
    num_steps = np.array(num_steps_list)
    relative_positions = cps / num_steps

    return {
        "count": len(cps),
        "mean": float(np.mean(cps)),
        "median": float(np.median(cps)),
        "std": float(np.std(cps)),
        "min": int(np.min(cps)),
        "max": int(np.max(cps)),
        "relative_position_mean": float(np.mean(relative_positions)),
        "relative_position_median": float(np.median(relative_positions)),
        "relative_position_std": float(np.std(relative_positions)),
    }
