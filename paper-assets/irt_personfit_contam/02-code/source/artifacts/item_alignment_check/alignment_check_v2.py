#!/usr/bin/env python3
"""Verify item ordering alignment between PSN-IRT combine.csv and Open LLM Leaderboard v1.
v2: Focus on structural analysis — aggregate vs subtask, question text matching."""

import os
import csv
import json
import sys
import numpy as np

os.environ["HF_HUB_DISABLE_XET"] = "1"

from datasets import load_dataset, get_dataset_config_names

PROJECT = "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam"
COMBINE_CSV = f"{PROJECT}/artifacts/psn_irt_phase_b/combine.csv"
OUT_DIR = f"{PROJECT}/artifacts/item_alignment_check"

BENCH_RANGES = {
    "mmlu": (27029, 41071),
}

V1_DATASETS = {
    "Mistral-7B-Instruct-v0.1": "open-llm-leaderboard-old/details_mistralai__Mistral-7B-Instruct-v0.1",
    "Vicuna-7B-v1.3": "open-llm-leaderboard-old/details_lmsys__vicuna-7b-v1.3",
}


def load_combine_csv():
    rows = []
    with open(COMBINE_CSV, "r") as f:
        reader = csv.reader(f)
        for row in reader:
            rows.append([float(x) for x in row])
    return np.array(rows)


def extract_psn_mmlu(combine_data, model_row):
    start, end = BENCH_RANGES["mmlu"]
    return combine_data[model_row, start:end]


def main():
    combine = load_combine_csv()
    print(f"combine.csv shape: {combine.shape}")

    dataset_name = V1_DATASETS["Mistral-7B-Instruct-v0.1"]
    psn_mmlu = extract_psn_mmlu(combine, 6)  # Mistral row 6
    print(f"PSN-IRT MMLU: {len(psn_mmlu)} items, mean={psn_mmlu.mean():.4f}")

    # Step 1: Load aggregate config and inspect structure
    print("\n=== Step 1: Inspect aggregate config ===")
    configs = get_dataset_config_names(dataset_name)
    mmlu_configs = sorted([c for c in configs if "hendrycksTest" in c])
    print(f"Total MMLU configs: {len(mmlu_configs)}")
    print(f"Aggregate: harness_hendrycksTest_5")

    ds_agg = load_dataset(dataset_name, "harness_hendrycksTest_5", split="latest")
    print(f"Aggregate columns: {ds_agg.column_names}")
    print(f"Aggregate rows: {len(ds_agg)}")
    print(f"First row keys: {list(ds_agg[0].keys())}")

    # Show first row in detail
    row0 = ds_agg[0]
    for k, v in row0.items():
        val_str = str(v)[:200]
        print(f"  {k}: {val_str}")

    # Step 2: Extract acc values from aggregate
    print("\n=== Step 2: Aggregate acc vector ===")
    agg_acc = np.array(ds_agg["acc"], dtype=float)
    print(f"Aggregate acc: {len(agg_acc)} items, mean={agg_acc.mean():.4f}")

    # Direct comparison
    match_direct = np.sum(psn_mmlu == agg_acc)
    print(f"Direct match: {match_direct}/{len(psn_mmlu)} = {match_direct/len(psn_mmlu):.4f}")

    # Step 3: Check if question text is available
    print("\n=== Step 3: Question text availability ===")
    has_doc = "doc" in ds_agg.column_names
    has_example = "example" in ds_agg.column_names
    print(f"Has 'doc' column: {has_doc}")
    print(f"Has 'example' column: {has_example}")

    if has_doc:
        doc0 = ds_agg[0]["doc"]
        print(f"doc[0] type: {type(doc0)}")
        if isinstance(doc0, dict):
            print(f"doc[0] keys: {list(doc0.keys())}")
            for k, v in doc0.items():
                print(f"  {k}: {str(v)[:150]}")

    # Step 4: Load per-subtask configs and check ordering
    print("\n=== Step 4: Per-subtask loading ===")
    subtask_configs = sorted([c for c in mmlu_configs if c != "harness_hendrycksTest_5"])
    print(f"Subtask configs: {len(subtask_configs)}")

    subtask_responses = []
    subtask_questions = []
    subtask_info = []

    for config in subtask_configs:
        ds = load_dataset(dataset_name, config, split="latest")
        acc = np.array(ds["acc"], dtype=float)
        subtask_name = config.replace("harness_hendrycksTest_", "").replace("_5", "")

        questions = []
        if "doc" in ds.column_names:
            for row in ds:
                doc = row["doc"]
                if isinstance(doc, dict):
                    q = doc.get("question", "") or doc.get("input", "")
                    questions.append(str(q)[:100])

        subtask_info.append({
            "config": config,
            "subtask": subtask_name,
            "n_items": len(acc),
            "mean_acc": float(acc.mean()),
        })
        subtask_responses.append(acc)
        subtask_questions.append(questions)

    # Concatenate per-subtask in alphabetical order
    subtask_concat = np.concatenate(subtask_responses)
    print(f"\nSubtask concat: {len(subtask_concat)} items, mean={subtask_concat.mean():.4f}")

    # Compare subtask concat vs aggregate
    if len(subtask_concat) == len(agg_acc):
        match_sub_agg = np.sum(subtask_concat == agg_acc)
        print(f"Subtask concat vs aggregate: {match_sub_agg}/{len(agg_acc)} = {match_sub_agg/len(agg_acc):.4f}")
    else:
        print(f"Length mismatch: subtask={len(subtask_concat)}, agg={len(agg_acc)}")

    # Compare subtask concat vs PSN-IRT
    match_sub_psn = np.sum(subtask_concat[:len(psn_mmlu)] == psn_mmlu)
    print(f"Subtask concat vs PSN-IRT: {match_sub_psn}/{len(psn_mmlu)} = {match_sub_psn/len(psn_mmlu):.4f}")

    # Step 5: Check if aggregate ordering matches subtask concat
    # (maybe aggregate has a different internal ordering)
    print("\n=== Step 5: Aggregate vs subtask item-level matching ===")
    if has_doc:
        # Use question text to create fingerprints
        agg_questions = []
        for row in ds_agg:
            doc = row["doc"]
            if isinstance(doc, dict):
                q = doc.get("question", "") or doc.get("input", "")
                agg_questions.append(str(q)[:100])
            else:
                agg_questions.append("")

        # Check ordering: are aggregate questions in same order as subtask concat?
        all_subtask_qs = []
        for qs in subtask_questions:
            all_subtask_qs.extend(qs)

        if agg_questions and all_subtask_qs:
            n_match_q = sum(1 for a, b in zip(agg_questions, all_subtask_qs) if a == b)
            print(f"Question order match (agg vs subtask-concat): {n_match_q}/{min(len(agg_questions), len(all_subtask_qs))}")

            # Find the actual ordering of aggregate
            # Build question -> index mapping from subtask concat
            subtask_q_to_idx = {}
            for i, q in enumerate(all_subtask_qs):
                if q not in subtask_q_to_idx:
                    subtask_q_to_idx[q] = i

            # Map aggregate to subtask indices
            agg_to_subtask_map = []
            for i, q in enumerate(agg_questions):
                if q in subtask_q_to_idx:
                    agg_to_subtask_map.append(subtask_q_to_idx[q])
                else:
                    agg_to_subtask_map.append(-1)

            mapped = [x for x in agg_to_subtask_map if x >= 0]
            print(f"Mapped {len(mapped)}/{len(agg_questions)} aggregate items to subtask positions")
            if mapped:
                print(f"First 20 mappings: {agg_to_subtask_map[:20]}")

    # Step 6: Content-based matching with PSN-IRT
    # PSN-IRT has no question text, so we use response patterns
    print("\n=== Step 6: Response-pattern matching ===")

    # For each subtask block in v1, find best matching position in PSN-IRT
    # by sliding the block and computing match rates
    psn_offset = 0
    block_matches = []
    used_positions = set()

    for i, info in enumerate(subtask_info):
        block = subtask_responses[i]
        n = len(block)

        best_pos = -1
        best_rate = 0.0

        for pos in range(len(psn_mmlu) - n + 1):
            rate = np.mean(psn_mmlu[pos:pos+n] == block)
            if rate > best_rate:
                best_rate = rate
                best_pos = pos

        block_matches.append({
            "subtask": info["subtask"],
            "n_items": n,
            "best_pos": best_pos,
            "best_rate": float(best_rate),
        })

        if best_rate > 0.9:
            print(f"  {info['subtask']:35s} ({n:4d} items): best match at pos {best_pos:5d} (rate={best_rate:.4f})")

    # Check if best_pos values are monotonically increasing (same ordering)
    high_conf = [b for b in block_matches if b["best_rate"] > 0.9]
    if high_conf:
        positions = [b["best_pos"] for b in high_conf]
        is_monotonic = all(positions[i] <= positions[i+1] for i in range(len(positions)-1))
        print(f"\nHigh-confidence matches: {len(high_conf)}/{len(block_matches)}")
        print(f"Positions monotonically increasing: {is_monotonic}")
        print(f"Position range: [{min(positions)}, {max(positions)}]")

        # If monotonic, this suggests same subtask order, just need to verify item order within
        if is_monotonic and len(high_conf) > 10:
            print("\n=== Step 7: Verify within-subtask item ordering ===")
            # For high-confidence subtasks, check if items are in same order
            for b in high_conf[:5]:
                subtask_idx = next(j for j, info in enumerate(subtask_info) if info["subtask"] == b["subtask"])
                block = subtask_responses[subtask_idx]
                n = len(block)
                pos = b["best_pos"]
                psn_block = psn_mmlu[pos:pos+n]

                # Per-item match
                item_match = np.sum(block == psn_block)
                print(f"  {b['subtask']:35s}: {item_match}/{n} = {item_match/n:.4f}")

    # Step 7b: Try using aggregate order with content-based reindex
    if has_doc and agg_questions:
        print("\n=== Step 7b: Aggregate reindexing via question fingerprint ===")
        # Build a fingerprint-based mapping from aggregate to PSN-IRT

        # First check: are there duplicates in questions?
        unique_qs = len(set(agg_questions))
        print(f"Unique questions in aggregate: {unique_qs}/{len(agg_questions)}")

    # Save detailed results
    results = {
        "psn_mmlu_len": int(len(psn_mmlu)),
        "psn_mmlu_mean": float(psn_mmlu.mean()),
        "v1_aggregate_len": int(len(agg_acc)),
        "v1_aggregate_mean": float(agg_acc.mean()),
        "v1_subtask_concat_len": int(len(subtask_concat)),
        "direct_match_rate": float(match_direct / len(psn_mmlu)),
        "subtask_concat_match_rate": float(match_sub_psn / len(psn_mmlu)),
        "block_matches": block_matches,
        "high_confidence_blocks": len(high_conf) if high_conf else 0,
        "subtask_info": subtask_info,
    }

    with open(f"{OUT_DIR}/alignment_results.json", "w") as f:
        json.dump(results, f, indent=2)
    print(f"\nResults saved to {OUT_DIR}/alignment_results.json")


if __name__ == "__main__":
    main()
