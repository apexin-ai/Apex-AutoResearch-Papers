#!/usr/bin/env python3
"""v4: Build v1→rawMMLU mapping, reorder v1 to raw MMLU order, compare with PSN-IRT.
Goal: determine if PSN-IRT follows raw MMLU canonical ordering."""

import os
import csv
import json
import hashlib
import numpy as np
from collections import defaultdict

os.environ["HF_HUB_DISABLE_XET"] = "1"

from datasets import load_dataset

PROJECT = "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam"
COMBINE_CSV = f"{PROJECT}/artifacts/psn_irt_phase_b/combine.csv"
OUT_DIR = f"{PROJECT}/artifacts/item_alignment_check"

BENCH_RANGES = {"mmlu": (27029, 41071)}


def load_combine_csv():
    rows = []
    with open(COMBINE_CSV, "r") as f:
        for row in csv.reader(f):
            rows.append([float(x) for x in row])
    return np.array(rows)


def main():
    combine = load_combine_csv()
    print(f"combine.csv: {combine.shape}")
    psn_mmlu = combine[6, BENCH_RANGES["mmlu"][0]:BENCH_RANGES["mmlu"][1]]  # Mistral row 6
    print(f"PSN-IRT MMLU (Mistral): {len(psn_mmlu)} items, mean={psn_mmlu.mean():.4f}")

    # Load raw MMLU (canonical ordering)
    print("\n=== Loading raw MMLU ===")
    mmlu_raw = load_dataset("cais/mmlu", "all", split="test")
    print(f"Raw MMLU: {len(mmlu_raw)} items")

    # Build raw MMLU question index: question_text -> (raw_idx, subject)
    raw_q_index = {}
    raw_items = []
    for i, row in enumerate(mmlu_raw):
        q = row["question"].strip()
        raw_q_index[q] = i
        raw_items.append({
            "idx": i,
            "question": q,
            "subject": row["subject"],
            "answer": row["answer"],
        })

    # Load v1 leaderboard Mistral data
    print("\n=== Loading v1 Mistral MMLU ===")
    ds_v1 = load_dataset(
        "open-llm-leaderboard-old/details_mistralai__Mistral-7B-Instruct-v0.1",
        "harness_hendrycksTest_5", split="latest"
    )
    v1_acc = np.array(ds_v1["acc"], dtype=float)
    print(f"v1 MMLU: {len(ds_v1)} items, mean={v1_acc.mean():.4f}")

    # Map v1 items to raw MMLU by matching question text
    print("\n=== Mapping v1 → raw MMLU ===")
    v1_to_raw = {}
    unmatched = []

    for i in range(len(ds_v1)):
        # Try 'example' field first, then 'query'
        example = ds_v1[i].get("example", "").strip()
        query = ds_v1[i].get("query", "").strip()

        matched = False
        # Direct match on example
        if example in raw_q_index:
            v1_to_raw[i] = raw_q_index[example]
            matched = True
        else:
            # Try substring match: find raw question contained in query
            for raw_q, raw_idx in raw_q_index.items():
                if raw_q in query:
                    v1_to_raw[i] = raw_idx
                    matched = True
                    break

        if not matched:
            unmatched.append(i)

    print(f"Matched: {len(v1_to_raw)}/{len(ds_v1)} ({len(v1_to_raw)/len(ds_v1)*100:.1f}%)")
    print(f"Unmatched: {len(unmatched)}")

    if unmatched:
        print(f"\nSample unmatched v1 items:")
        for idx in unmatched[:3]:
            print(f"  v1[{idx}]: example='{ds_v1[idx]['example'][:80]}...'")
            print(f"           query='{ds_v1[idx]['query'][:80]}...'")

    # Check for duplicate mappings (multiple v1 items → same raw item)
    raw_targets = list(v1_to_raw.values())
    n_unique_raw = len(set(raw_targets))
    print(f"Unique raw MMLU targets: {n_unique_raw}/{len(v1_to_raw)}")

    # v1 ordering: what are the raw MMLU indices in v1 order?
    v1_raw_order = [v1_to_raw.get(i, -1) for i in range(len(ds_v1))]
    valid_order = [x for x in v1_raw_order if x >= 0]
    print(f"\nv1 → raw MMLU index sequence (first 30): {valid_order[:30]}")
    is_sorted = all(valid_order[i] <= valid_order[i+1] for i in range(len(valid_order)-1))
    print(f"Is v1 order = raw MMLU canonical order? {is_sorted}")

    # Check if v1 is grouped by subject (subtask) with items in order within subject
    print("\n=== Checking v1 ordering pattern ===")
    v1_subjects = []
    for i in range(len(ds_v1)):
        if i in v1_to_raw:
            raw_idx = v1_to_raw[i]
            v1_subjects.append(raw_items[raw_idx]["subject"])
        else:
            v1_subjects.append("UNKNOWN")

    # Subject transitions
    transitions = []
    for i in range(1, len(v1_subjects)):
        if v1_subjects[i] != v1_subjects[i-1]:
            transitions.append((i, v1_subjects[i-1], v1_subjects[i]))

    print(f"Subject transitions: {len(transitions)}")
    print(f"First 10 transitions:")
    for pos, from_s, to_s in transitions[:10]:
        print(f"  pos {pos}: {from_s} → {to_s}")

    # Build v1's actual subtask ordering
    v1_subtask_order = []
    current = v1_subjects[0]
    start = 0
    for i in range(1, len(v1_subjects)):
        if v1_subjects[i] != current:
            v1_subtask_order.append({"subtask": current, "start": start, "end": i, "n": i - start})
            current = v1_subjects[i]
            start = i
    v1_subtask_order.append({"subtask": current, "start": start, "end": len(v1_subjects), "n": len(v1_subjects) - start})

    print(f"\nv1 subtask ordering (alphabetical?): {[s['subtask'] for s in v1_subtask_order[:5]]}...")
    is_alpha = [s["subtask"] for s in v1_subtask_order] == sorted([s["subtask"] for s in v1_subtask_order])
    print(f"Subtasks in alphabetical order: {is_alpha}")

    # Within each subtask, check if items are in raw MMLU order
    print("\n=== Within-subtask item ordering ===")
    within_ordered = 0
    within_total = 0
    for block in v1_subtask_order:
        raw_indices = []
        for i in range(block["start"], block["end"]):
            if i in v1_to_raw:
                raw_indices.append(v1_to_raw[i])
        if len(raw_indices) > 1:
            is_ord = all(raw_indices[j] < raw_indices[j+1] for j in range(len(raw_indices)-1))
            within_total += 1
            if is_ord:
                within_ordered += 1
            else:
                print(f"  NOT ordered: {block['subtask']} — indices sample: {raw_indices[:10]}")

    print(f"Subtasks with items in canonical order: {within_ordered}/{within_total}")

    # Now the key question: is PSN-IRT in the same order as v1 or raw MMLU?
    # Since v1 is alphabetical-by-subtask with items in raw-MMLU-within-subtask order,
    # and the direct v1↔PSN match is 54.56%, PSN-IRT must use a different ordering.
    #
    # Hypothesis: PSN-IRT might use raw MMLU order (sorted by subject, then by row in dataset)
    # OR PSN-IRT might use a completely different ordering.
    #
    # We can check: reorder v1 responses to raw MMLU canonical order and compare with PSN-IRT.

    print("\n=== Reorder v1 to raw MMLU canonical order, compare with PSN-IRT ===")
    # Create v1 responses indexed by raw MMLU position
    v1_by_raw = np.full(14042, np.nan)
    for v1_idx, raw_idx in v1_to_raw.items():
        v1_by_raw[raw_idx] = v1_acc[v1_idx]

    valid_mask = ~np.isnan(v1_by_raw)
    n_valid = valid_mask.sum()
    print(f"Valid (mapped) items: {n_valid}/14042")

    # Compare with PSN-IRT at same positions
    match_reordered = np.sum(v1_by_raw[valid_mask] == psn_mmlu[valid_mask])
    print(f"Match (reordered v1 vs PSN-IRT at mapped positions): {match_reordered}/{n_valid} = {match_reordered/n_valid:.4f}")

    # Also try: compare v1 in raw MMLU order with PSN-IRT in v1 order
    # (i.e., PSN-IRT might be in v1 order reordered somehow)

    # Actually, let's think about this differently.
    # PSN-IRT MMLU has 14042 items. Let's check if PSN-IRT is in raw MMLU canonical order
    # by seeing if reordering v1→raw order gives better match.

    # Build reordered v1 response vector in raw MMLU order
    v1_reordered = np.full(14042, -1.0)
    for v1_idx, raw_idx in v1_to_raw.items():
        v1_reordered[raw_idx] = v1_acc[v1_idx]

    # PSN-IRT in its original order vs v1 in raw MMLU order
    valid2 = v1_reordered >= 0
    match2 = np.sum(v1_reordered[valid2] == psn_mmlu[valid2])
    rate2 = match2 / valid2.sum()
    print(f"\nv1 (raw MMLU order) vs PSN-IRT (original order): {match2}/{valid2.sum()} = {rate2:.4f}")

    # Compare: direct v1 vs PSN-IRT was 54.56%
    # If this is higher, PSN-IRT follows raw MMLU order
    print(f"Direct v1 vs PSN-IRT was: 0.5456")
    print(f"After reordering: {rate2:.4f}")

    if rate2 > 0.95:
        print(">>> PSN-IRT follows raw MMLU canonical order! <<<")
    elif rate2 > 0.8:
        print(">>> Partial alignment with raw MMLU order <<<")
    else:
        print(">>> PSN-IRT does NOT follow raw MMLU canonical order <<<")

    # Additional check: PSN-IRT subtask-level accuracy pattern
    # If we know raw MMLU subject boundaries, check if PSN-IRT matches
    print("\n=== PSN-IRT accuracy by raw MMLU subject ===")
    raw_subjects_order = [raw_items[i]["subject"] for i in range(14042)]
    subject_boundaries = []
    current = raw_subjects_order[0]
    start = 0
    for i in range(1, 14042):
        if raw_subjects_order[i] != current:
            subject_boundaries.append({"subject": current, "start": start, "end": i})
            current = raw_subjects_order[i]
            start = i
    subject_boundaries.append({"subject": current, "start": start, "end": 14042})

    print(f"Raw MMLU has {len(subject_boundaries)} subject blocks")
    print(f"First 5: {[(s['subject'], s['start'], s['end']) for s in subject_boundaries[:5]]}")

    for sb in subject_boundaries[:10]:
        psn_block = psn_mmlu[sb["start"]:sb["end"]]
        v1_block = v1_reordered[sb["start"]:sb["end"]]
        valid_b = v1_block >= 0
        if valid_b.any():
            match_b = np.sum(v1_block[valid_b] == psn_block[valid_b])
            rate_b = match_b / valid_b.sum()
            print(f"  {sb['subject']:35s}: PSN={psn_block.mean():.3f} v1(reord)={v1_block[valid_b].mean():.3f} match={rate_b:.3f}")

    # Save results
    results = {
        "v1_to_raw_matched": len(v1_to_raw),
        "v1_to_raw_unmatched": len(unmatched),
        "v1_subtask_order_alphabetical": is_alpha,
        "v1_within_subtask_ordered": f"{within_ordered}/{within_total}",
        "direct_match_rate": 0.5456,
        "reordered_match_rate": float(rate2),
        "conclusion": "aligned_raw_mmlu" if rate2 > 0.95 else "partially_aligned" if rate2 > 0.8 else "not_aligned",
    }

    with open(f"{OUT_DIR}/alignment_results_v4.json", "w") as f:
        json.dump(results, f, indent=2)
    print(f"\nSaved to {OUT_DIR}/alignment_results_v4.json")


if __name__ == "__main__":
    main()
