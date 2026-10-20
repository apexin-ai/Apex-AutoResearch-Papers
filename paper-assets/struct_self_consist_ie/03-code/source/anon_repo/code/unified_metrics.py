"""Unified F1 / degeneracy / data-loading module.

This is the single source of truth for entity F1, degeneracy detection,
and data loading across all analysis scripts. All analysis scripts must
import from this module instead of defining their own implementations.

Conventions:
  - Entity = (start, end, type) tuple, exact match
  - F1 = micro per-instance: 2*P*R/(P+R)
  - Degeneracy = constant-F1 gold-filtered (all N sample F1s identical)
  - gold_filter = skip instances where gold entities list is empty
"""

import json
import numpy as np


def compute_entity_f1(pred_entities, gold_entities):
    """Span-based entity F1 for a single instance.

    Args:
        pred_entities: list of dicts with keys start, end, type.
        gold_entities: list of dicts with keys start, end, type.

    Returns:
        float F1 in [0, 1].
    """
    pred_set = {(e["start"], e["end"], e["type"]) for e in pred_entities}
    gold_set = {(e["start"], e["end"], e["type"]) for e in gold_entities}
    if not gold_set and not pred_set:
        return 1.0
    if not gold_set or not pred_set:
        return 0.0
    tp = len(pred_set & gold_set)
    if tp == 0:
        return 0.0
    p = tp / len(pred_set)
    r = tp / len(gold_set)
    return 2 * p * r / (p + r)


def compute_degeneracy(sample_f1_list):
    """Check if an instance is degenerate (constant-F1 gold-filtered).

    All N sample F1 values are identical (after rounding to 10 decimals
    to avoid float noise) -> degenerate.

    Args:
        sample_f1_list: list of float F1 values, one per sample.

    Returns:
        bool, True if degenerate.
    """
    return len(set(round(f, 10) for f in sample_f1_list)) <= 1


def load_and_filter(path, gold_filter=True):
    """Load samples.jsonl and optionally filter out gold-empty instances.

    Args:
        path: path to samples.jsonl
        gold_filter: if True, skip instances with empty gold entities.

    Returns:
        list of instance dicts.
    """
    instances = []
    with open(path) as f:
        for line in f:
            if not line.strip():
                continue
            obj = json.loads(line)
            if gold_filter and not obj["gold"].get("entities", []):
                continue
            instances.append(obj)
    return instances


def compute_sample_f1s(inst, n_samples=None):
    """Compute per-sample F1 list for an instance.

    Args:
        inst: instance dict with keys gold, samples.
        n_samples: if set, only use first n_samples.

    Returns:
        list of float F1 values.
    """
    gold_ents = inst["gold"]["entities"]
    samples = inst["samples"][:n_samples] if n_samples else inst["samples"]
    return [compute_entity_f1(s.get("entities", []), gold_ents) for s in samples]


def compute_greedy_f1(inst):
    """Compute greedy F1 for an instance."""
    gold_ents = inst["gold"]["entities"]
    greedy = inst.get("greedy", inst["samples"][0])
    return compute_entity_f1(greedy.get("entities", []), gold_ents)


def get_lp_selection_idx(inst, n_samples=None):
    """Get the index of the sample with highest mean_logprob."""
    samples = inst["samples"][:n_samples] if n_samples else inst["samples"]
    best_idx = 0
    best_lp = -float("inf")
    for i, s in enumerate(samples):
        lp = s.get("mean_logprob", None)
        if lp is None and "logprobs" in inst and i < len(inst["logprobs"]):
            lp = inst["logprobs"][i]
        if lp is not None and np.isfinite(lp) and lp > best_lp:
            best_lp = lp
            best_idx = i
    return best_idx


def bootstrap_ci(values, n_boot=2000, ci=0.95, seed=42):
    """Bootstrap confidence interval for the mean."""
    arr = np.array(values)
    n = len(arr)
    if n == 0:
        return {"mean": 0.0, "ci_lo": 0.0, "ci_hi": 0.0}
    rng = np.random.RandomState(seed)
    boot_means = np.array([arr[rng.randint(0, n, n)].mean() for _ in range(n_boot)])
    boot_means.sort()
    lo = boot_means[int((1 - ci) / 2 * n_boot)]
    hi = boot_means[int((1 + ci) / 2 * n_boot)]
    return {"mean": float(arr.mean()), "ci_lo": float(lo), "ci_hi": float(hi)}


def bootstrap_delta_ci(a, b, n_boot=2000, ci=0.95, seed=42):
    """Bootstrap CI for mean(a) - mean(b), paired."""
    a_arr, b_arr = np.array(a), np.array(b)
    n = len(a_arr)
    if n == 0:
        return {"delta": 0.0, "ci_lo": 0.0, "ci_hi": 0.0}
    rng = np.random.RandomState(seed)
    deltas = []
    for _ in range(n_boot):
        idx = rng.randint(0, n, n)
        deltas.append(float(a_arr[idx].mean() - b_arr[idx].mean()))
    deltas.sort()
    lo = deltas[int((1 - ci) / 2 * n_boot)]
    hi = deltas[int((1 + ci) / 2 * n_boot)]
    return {"delta": float(a_arr.mean() - b_arr.mean()), "ci_lo": float(lo), "ci_hi": float(hi)}
