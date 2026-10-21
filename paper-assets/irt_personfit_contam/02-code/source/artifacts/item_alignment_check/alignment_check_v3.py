#!/usr/bin/env python3
"""v3: Content-based matching using question text fingerprints.
Since direct positional alignment failed (54.56%), try to match items by content."""

import os
import csv
import json
import hashlib
import numpy as np
from collections import Counter, defaultdict

os.environ["HF_HUB_DISABLE_XET"] = "1"

from datasets import load_dataset, get_dataset_config_names

PROJECT = "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam"
COMBINE_CSV = f"{PROJECT}/artifacts/psn_irt_phase_b/combine.csv"
OUT_DIR = f"{PROJECT}/artifacts/item_alignment_check"

BENCH_RANGES = {"mmlu": (27029, 41071)}

V1_DATASETS = {
    "Mistral-7B-Instruct-v0.1": ("open-llm-leaderboard-old/details_mistralai__Mistral-7B-Instruct-v0.1", 6),
    "Vicuna-7B-v1.3": ("open-llm-leaderboard-old/details_lmsys__vicuna-7b-v1.3", 10),
}


def load_combine_csv():
    rows = []
    with open(COMBINE_CSV, "r") as f:
        for row in csv.reader(f):
            rows.append([float(x) for x in row])
    return np.array(rows)


def main():
    combine = load_combine_csv()
    print(f"combine.csv: {combine.shape}")

    results_all = {}

    for model_name, (dataset_name, psn_row) in V1_DATASETS.items():
        print(f"\n{'='*70}")
        print(f"Model: {model_name} (PSN row {psn_row})")
        print(f"{'='*70}")

        psn_mmlu = combine[psn_row, BENCH_RANGES["mmlu"][0]:BENCH_RANGES["mmlu"][1]]
        print(f"PSN-IRT MMLU: {len(psn_mmlu)} items, mean={psn_mmlu.mean():.4f}")

        # Load v1 aggregate MMLU
        print(f"Loading v1 data from {dataset_name}...")
        ds = load_dataset(dataset_name, "harness_hendrycksTest_5", split="latest")
        v1_acc = np.array(ds["acc"], dtype=float)
        print(f"v1 MMLU: {len(ds)} items, mean={v1_acc.mean():.4f}")

        # Extract question fingerprints from v1
        print("\nExtracting question fingerprints from v1...")
        v1_fingerprints = []
        for i, row in enumerate(ds):
            example = row.get("example", "")
            query = row.get("query", "")
            # Use the query (question text) as fingerprint
            text = query if query else example
            fp = hashlib.md5(text.encode()).hexdigest()[:16]
            v1_fingerprints.append({
                "idx": i,
                "fp": fp,
                "acc": float(v1_acc[i]),
                "text_preview": str(text)[:80],
            })

        # Check uniqueness
        fp_counts = Counter(item["fp"] for item in v1_fingerprints)
        n_unique = len(fp_counts)
        n_dup = sum(1 for c in fp_counts.values() if c > 1)
        print(f"Unique fingerprints: {n_unique}/{len(v1_fingerprints)}, duplicates: {n_dup}")

        if n_dup > 0:
            most_common = fp_counts.most_common(5)
            print(f"Most duplicated FPs: {most_common}")

        # Group by subtask to understand structure
        print("\nPer-subtask structure in aggregate:")
        configs = get_dataset_config_names(dataset_name)
        subtask_configs = sorted([c for c in configs if c.startswith("harness_hendrycksTest_") and c != "harness_hendrycksTest_5"])

        subtask_boundaries = []
        offset = 0
        for config in subtask_configs:
            ds_sub = load_dataset(dataset_name, config, split="latest")
            n = len(ds_sub)
            subtask_name = config.replace("harness_hendrycksTest_", "").replace("_5", "")
            subtask_boundaries.append({
                "subtask": subtask_name,
                "start": offset,
                "end": offset + n,
                "n_items": n,
            })
            offset += n

        print(f"Subtask total: {offset} items across {len(subtask_boundaries)} subtasks")

        # Show first 5 subtask boundaries
        for sb in subtask_boundaries[:5]:
            print(f"  {sb['subtask']}: [{sb['start']}, {sb['end']})")

        # Check: PSN-IRT MMLU accuracy per subtask block
        print("\nPSN-IRT accuracy by v1-subtask boundaries (if aligned):")
        for sb in subtask_boundaries:
            psn_block = psn_mmlu[sb["start"]:sb["end"]]
            v1_block = v1_acc[sb["start"]:sb["end"]]
            psn_mean = psn_block.mean()
            v1_mean = v1_block.mean()
            block_match = np.mean(psn_block == v1_block)
            if abs(psn_mean - v1_mean) < 0.05:
                marker = "~"
            elif abs(psn_mean - v1_mean) < 0.15:
                marker = " "
            else:
                marker = "!"
            print(f"  {marker} {sb['subtask']:35s}: PSN={psn_mean:.3f} v1={v1_mean:.3f} match={block_match:.3f}")

        # Now try a different approach: look at how PSN-IRT's paper describes their MMLU evaluation
        # PSN-IRT may be using the MMLU dataset directly (not lm-eval-harness leaderboard)
        # Let's check: load raw MMLU test set and see if the item count matches
        print("\n=== Cross-reference with raw MMLU dataset ===")
        try:
            mmlu_raw = load_dataset("cais/mmlu", "all", split="test")
            print(f"Raw MMLU test set: {len(mmlu_raw)} items")
        except:
            try:
                mmlu_raw = load_dataset("hails/mmlu_no_train", "all", split="test")
                print(f"MMLU (hails) test set: {len(mmlu_raw)} items")
            except Exception as e:
                print(f"Could not load raw MMLU: {e}")
                mmlu_raw = None

        # Now do the real content-based matching:
        # Since PSN-IRT has no question text, we need to use multi-model response patterns
        # to match items across the two datasets
        print("\n=== Multi-model response pattern matching ===")
        print("Strategy: use all PSN-IRT models' responses as a fingerprint per item")

        # Extract MMLU columns for all 12 models
        psn_all_models = combine[:, BENCH_RANGES["mmlu"][0]:BENCH_RANGES["mmlu"][1]]
        print(f"PSN all-model MMLU shape: {psn_all_models.shape}")

        # For each item in PSN-IRT, create a binary pattern across all 12 models
        psn_patterns = {}
        for j in range(psn_all_models.shape[1]):
            pattern = tuple(psn_all_models[:, j].astype(int).tolist())
            if pattern not in psn_patterns:
                psn_patterns[pattern] = []
            psn_patterns[pattern].append(j)

        n_unique_patterns = len(psn_patterns)
        n_dup_patterns = sum(1 for v in psn_patterns.values() if len(v) > 1)
        max_dup = max(len(v) for v in psn_patterns.values())
        print(f"Unique 12-model patterns: {n_unique_patterns}/{psn_all_models.shape[1]}")
        print(f"Patterns with duplicates: {n_dup_patterns}, max dup count: {max_dup}")

        # Problem: we only have 1 model in common between PSN-IRT and v1 leaderboard
        # So we can't do multi-model fingerprinting directly.
        # We need to find another approach.

        # Let's check: does the v1 data include 'example' with enough detail to do content matching?
        # And does PSN-IRT have any auxiliary data?
        print("\n=== Investigating v1 question structure for content matching ===")
        # Check if we can extract subtask + position from the aggregate
        # by matching questions against raw MMLU

        if mmlu_raw is not None:
            print(f"Raw MMLU columns: {mmlu_raw.column_names}")
            print(f"Raw MMLU[0]: {mmlu_raw[0]}")

            # Build raw MMLU fingerprint index: subject -> [questions]
            raw_by_subject = defaultdict(list)
            for i, row in enumerate(mmlu_raw):
                subject = row.get("subject", "unknown")
                question = row.get("question", "")
                raw_by_subject[subject].append({
                    "idx": i,
                    "question": question[:100],
                    "fp": hashlib.md5(question.encode()).hexdigest()[:16],
                })

            print(f"\nRaw MMLU subjects: {len(raw_by_subject)}")
            print(f"Total raw items: {sum(len(v) for v in raw_by_subject.values())}")

            # Now match v1 questions against raw MMLU
            raw_fps = {}
            for subject, items in raw_by_subject.items():
                for item in items:
                    raw_fps[item["fp"]] = (subject, item["idx"])

            # Match v1 aggregate items to raw MMLU
            v1_to_raw = {}
            for i, vf in enumerate(v1_fingerprints):
                # v1 "query" is the question stem. Try to match against raw MMLU "question"
                query_text = ds[i]["query"]
                # The query in v1 might have few-shot prefix, extract the actual question
                # Actually, the 'example' field seems to be the question text
                example_text = ds[i].get("example", "")
                efp = hashlib.md5(example_text.encode()).hexdigest()[:16]
                if efp in raw_fps:
                    v1_to_raw[i] = raw_fps[efp]

            print(f"v1 items matched to raw MMLU by example text: {len(v1_to_raw)}/{len(v1_fingerprints)}")

            # Alternative: match by checking if query contains the question
            if len(v1_to_raw) < len(v1_fingerprints) * 0.5:
                print("Low match rate, trying alternative matching...")
                # Build raw question -> idx index
                raw_q_to_idx = {}
                for subject, items in raw_by_subject.items():
                    for item in items:
                        raw_q_to_idx[item["question"]] = (subject, item["idx"])

                matched_alt = 0
                for i in range(len(ds)):
                    if i in v1_to_raw:
                        continue
                    query = ds[i]["query"]
                    # Try first 80 chars of query as key
                    for raw_q, (subj, idx) in raw_q_to_idx.items():
                        if raw_q in query:
                            v1_to_raw[i] = (subj, idx)
                            matched_alt += 1
                            break

                print(f"After alternative matching: {len(v1_to_raw)}/{len(v1_fingerprints)}")

        # Key insight: let's check if v1 and PSN-IRT use the same MMLU items at all
        # by comparing accuracy distributions
        print("\n=== Accuracy distribution comparison ===")
        print(f"PSN-IRT Mistral MMLU mean: {psn_mmlu.mean():.4f}, std: {psn_mmlu.std():.4f}")
        print(f"v1 Mistral MMLU mean:      {v1_acc.mean():.4f}, std: {v1_acc.std():.4f}")
        print(f"PSN-IRT sum(correct):       {psn_mmlu.sum():.0f}")
        print(f"v1 sum(correct):            {v1_acc.sum():.0f}")

        # Check if they even have the same total correct
        # If different, the underlying data is different (maybe different eval protocol)
        diff_total = abs(psn_mmlu.sum() - v1_acc.sum())
        print(f"Difference in total correct: {diff_total:.0f}")

        results_all[model_name] = {
            "psn_len": int(len(psn_mmlu)),
            "v1_len": int(len(v1_acc)),
            "psn_mean": float(psn_mmlu.mean()),
            "v1_mean": float(v1_acc.mean()),
            "psn_sum_correct": float(psn_mmlu.sum()),
            "v1_sum_correct": float(v1_acc.sum()),
            "direct_match_rate": float(np.mean(psn_mmlu == v1_acc)),
            "diff_total_correct": float(diff_total),
        }

    # Save
    with open(f"{OUT_DIR}/alignment_results_v3.json", "w") as f:
        json.dump(results_all, f, indent=2)
    print(f"\nSaved to {OUT_DIR}/alignment_results_v3.json")


if __name__ == "__main__":
    main()
