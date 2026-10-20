#!/usr/bin/env python3
"""Compute inter-annotator and human-LLM agreement metrics.

Usage:
    python compute_agreement.py annotator1.jsonl annotator2.jsonl

Each annotator JSONL must have fields: episode_id, severity_label, justification.
LLM judgments are loaded from:
    artifacts/plan_009/llm_baseline_gpt-54.jsonl
    artifacts/plan_009/llm_baseline_gpt-41.jsonl

Outputs:
    artifacts/plan_009/agreement_results.json
    Summary table to stdout.
"""

import argparse
import json
import os
import sys
from pathlib import Path

from sklearn.metrics import cohen_kappa_score


# --- Constants ---

SEVERITY_TO_ORDINAL = {"critical": 3, "moderate": 2, "minor": 1, "none": 0}
BINARY_POSITIVE = {"critical", "moderate"}  # violation = critical | moderate

SCRIPT_DIR = Path(__file__).resolve().parent
LLM_GPT54_PATH = SCRIPT_DIR / "llm_baseline_gpt-54.jsonl"
LLM_GPT41_PATH = SCRIPT_DIR / "llm_baseline_gpt-41.jsonl"
OUTPUT_PATH = SCRIPT_DIR / "agreement_results.json"


# --- Helpers ---

def load_annotator(path: str) -> dict[str, str]:
    """Load annotator JSONL → {episode_id: severity_label}."""
    records = {}
    with open(path) as f:
        for line in f:
            rec = json.loads(line)
            eid = rec["episode_id"]
            label = rec["severity_label"].strip().lower()
            if label not in SEVERITY_TO_ORDINAL:
                raise ValueError(f"Unknown severity label '{label}' in {path}, episode {eid}")
            records[eid] = label
    return records


def load_llm_baseline(path: Path) -> dict[str, str]:
    """Load LLM baseline JSONL → {episode_id: violation_level}."""
    records = {}
    with open(path) as f:
        for line in f:
            rec = json.loads(line)
            eid = rec["episode_id"]
            label = rec["violation_level"].strip().lower()
            records[eid] = label
    return records


def to_binary(label: str) -> int:
    """Map severity to binary: violation (1) vs none (0)."""
    return 1 if label in BINARY_POSITIVE else 0


def to_ordinal(label: str) -> int:
    """Map severity to ordinal: critical=3, moderate=2, minor=1, none=0."""
    return SEVERITY_TO_ORDINAL[label]


def compute_kappa_binary(labels_a: list[str], labels_b: list[str]) -> float:
    """Cohen's kappa on binary (violation vs none)."""
    a = [to_binary(l) for l in labels_a]
    b = [to_binary(l) for l in labels_b]
    return cohen_kappa_score(a, b)


def compute_kappa_weighted(labels_a: list[str], labels_b: list[str]) -> float:
    """Weighted (quadratic) Cohen's kappa on 4-tier ordinal scale."""
    a = [to_ordinal(l) for l in labels_a]
    b = [to_ordinal(l) for l in labels_b]
    return cohen_kappa_score(a, b, weights="quadratic",
                              labels=[0, 1, 2, 3])


def aligned_labels(dict_a: dict[str, str], dict_b: dict[str, str]) -> tuple[list[str], list[str]]:
    """Return aligned label lists for shared episode_ids (sorted)."""
    shared = sorted(set(dict_a) & set(dict_b))
    if not shared:
        raise ValueError("No shared episode_ids between the two sources.")
    return [dict_a[eid] for eid in shared], [dict_b[eid] for eid in shared], shared


def binary_agreement_rate(labels_a: list[str], labels_b: list[str]) -> float:
    """Simple percentage agreement on binary labels."""
    a = [to_binary(l) for l in labels_a]
    b = [to_binary(l) for l in labels_b]
    return sum(x == y for x, y in zip(a, b)) / len(a)


def exact_agreement_rate(labels_a: list[str], labels_b: list[str]) -> float:
    """Simple percentage agreement on exact labels."""
    return sum(a == b for a, b in zip(labels_a, labels_b)) / len(labels_a)


# --- Main ---

def main():
    parser = argparse.ArgumentParser(
        description="Compute inter-annotator and human-LLM agreement.")
    parser.add_argument("annotator1", help="Path to annotator 1 JSONL")
    parser.add_argument("annotator2", help="Path to annotator 2 JSONL")
    parser.add_argument("--output", default=str(OUTPUT_PATH),
                        help=f"Output JSON path (default: {OUTPUT_PATH})")
    args = parser.parse_args()

    # Load data
    ann1 = load_annotator(args.annotator1)
    ann2 = load_annotator(args.annotator2)
    gpt54 = load_llm_baseline(LLM_GPT54_PATH)
    gpt41 = load_llm_baseline(LLM_GPT41_PATH)

    print(f"Annotator 1: {len(ann1)} episodes from {args.annotator1}")
    print(f"Annotator 2: {len(ann2)} episodes from {args.annotator2}")
    print(f"GPT-5.4:     {len(gpt54)} episodes")
    print(f"GPT-4.1:     {len(gpt41)} episodes")
    print()

    results = {}

    # 1. Inter-annotator agreement
    a1_labels, a2_labels, shared_ids = aligned_labels(ann1, ann2)
    n_shared = len(shared_ids)

    iaa_binary_kappa = compute_kappa_binary(a1_labels, a2_labels)
    iaa_weighted_kappa = compute_kappa_weighted(a1_labels, a2_labels)
    iaa_binary_agree = binary_agreement_rate(a1_labels, a2_labels)
    iaa_exact_agree = exact_agreement_rate(a1_labels, a2_labels)

    results["inter_annotator"] = {
        "n_episodes": n_shared,
        "binary_kappa": round(iaa_binary_kappa, 4),
        "weighted_kappa_quadratic": round(iaa_weighted_kappa, 4),
        "binary_agreement": round(iaa_binary_agree, 4),
        "exact_agreement": round(iaa_exact_agree, 4),
    }

    # 2. Human-LLM agreement (per annotator × per judge)
    human_llm_pairs = [
        ("annotator1", ann1, "gpt54", gpt54),
        ("annotator1", ann1, "gpt41", gpt41),
        ("annotator2", ann2, "gpt54", gpt54),
        ("annotator2", ann2, "gpt41", gpt41),
    ]

    human_llm_results = {}
    binary_kappas_for_pool = []

    for h_name, h_dict, l_name, l_dict in human_llm_pairs:
        h_labels, l_labels, sids = aligned_labels(h_dict, l_dict)
        bk = compute_kappa_binary(h_labels, l_labels)
        wk = compute_kappa_weighted(h_labels, l_labels)
        ba = binary_agreement_rate(h_labels, l_labels)
        ea = exact_agreement_rate(h_labels, l_labels)

        key = f"{h_name}_vs_{l_name}"
        human_llm_results[key] = {
            "n_episodes": len(sids),
            "binary_kappa": round(bk, 4),
            "weighted_kappa_quadratic": round(wk, 4),
            "binary_agreement": round(ba, 4),
            "exact_agreement": round(ea, 4),
        }
        binary_kappas_for_pool.append(bk)

    results["human_llm"] = human_llm_results

    # 3. Pooled human-LLM kappa
    pooled_kappa = sum(binary_kappas_for_pool) / len(binary_kappas_for_pool)
    results["pooled_human_llm_binary_kappa"] = round(pooled_kappa, 4)

    # Save
    with open(args.output, "w") as f:
        json.dump(results, f, indent=2)
    print(f"Results saved to {args.output}\n")

    # Print summary table
    print("=" * 72)
    print(f"{'Comparison':<30} {'N':>5} {'κ_bin':>7} {'κ_wt':>7} {'%bin':>7} {'%exact':>7}")
    print("-" * 72)

    r = results["inter_annotator"]
    print(f"{'Ann1 vs Ann2':<30} {r['n_episodes']:>5} "
          f"{r['binary_kappa']:>7.4f} {r['weighted_kappa_linear']:>7.4f} "
          f"{r['binary_agreement']:>7.4f} {r['exact_agreement']:>7.4f}")

    for key, r in results["human_llm"].items():
        label = key.replace("_vs_", " vs ").replace("annotator", "Ann").replace("gpt", "GPT-")
        print(f"{label:<30} {r['n_episodes']:>5} "
              f"{r['binary_kappa']:>7.4f} {r['weighted_kappa_linear']:>7.4f} "
              f"{r['binary_agreement']:>7.4f} {r['exact_agreement']:>7.4f}")

    print("-" * 72)
    print(f"{'Pooled human-LLM κ_bin':<30} {'':>5} {results['pooled_human_llm_binary_kappa']:>7.4f}")
    print("=" * 72)


if __name__ == "__main__":
    main()
