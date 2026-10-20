"""
Prepare volume-matched control dataset for Data Quantity confound analysis.

Creates a dataset with the same total size as d100 (66533) but replaces
benchmark contamination items with non-benchmark MCQ items from MMLU
auxiliary_train split.

Output: sft_volume_control.jsonl = 50000 clean SFT + 16533 auxiliary MCQ
"""

import argparse
import json
import random
import hashlib
from pathlib import Path


ANSWER_MAP = {0: "A", 1: "B", 2: "C", 3: "D"}
NUM_AUX_ITEMS = 16533
SEED = 42


def load_base_data(path: str) -> list[dict]:
    data = []
    with open(path) as f:
        for line in f:
            line = line.strip()
            if line:
                data.append(json.loads(line))
    return data


def load_mmlu_aux(cache_dir: str) -> list[dict]:
    from datasets import load_dataset
    ds = load_dataset("cais/mmlu", "all", split="auxiliary_train",
                      cache_dir=cache_dir)
    return list(ds)


def load_mmlu_test(cache_dir: str) -> set[str]:
    from datasets import load_dataset
    ds = load_dataset("cais/mmlu", "all", split="test",
                      cache_dir=cache_dir)
    fingerprints = set()
    for item in ds:
        fp = hashlib.md5(item["question"].strip().lower().encode()).hexdigest()
        fingerprints.add(fp)
    return fingerprints


def load_arc_test(cache_dir: str) -> set[str]:
    from datasets import load_dataset
    ds = load_dataset("allenai/ai2_arc", "ARC-Challenge", split="test",
                      cache_dir=cache_dir)
    fingerprints = set()
    for item in ds:
        fp = hashlib.md5(item["question"].strip().lower().encode()).hexdigest()
        fingerprints.add(fp)
    return fingerprints


def format_aux_as_chat(item: dict) -> dict:
    question = item["question"]
    choices = item["choices"]
    answer_idx = item["answer"]
    answer_letter = ANSWER_MAP[answer_idx]

    labels = ["A", "B", "C", "D"]
    choices_str = "\n".join(f"{labels[i]}) {c}" for i, c in enumerate(choices))

    return {
        "messages": [
            {"role": "user", "content": f"Question: {question}\n{choices_str}"},
            {"role": "assistant", "content": f"The answer is {answer_letter}."},
        ]
    }


def verify_no_overlap(aux_items: list[dict], test_fps: set[str],
                       label: str) -> int:
    overlap = 0
    for item in aux_items:
        fp = hashlib.md5(item["question"].strip().lower().encode()).hexdigest()
        if fp in test_fps:
            overlap += 1
    return overlap


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--base-data", type=str,
                        default="/root/autodl-tmp/exp001/sft_data/sft_dosage_000.jsonl")
    parser.add_argument("--output", type=str,
                        default="/root/autodl-tmp/exp001/sft_data/sft_volume_control.jsonl")
    parser.add_argument("--cache-dir", type=str,
                        default="/root/autodl-tmp/.hf_cache")
    parser.add_argument("--num-aux", type=int, default=NUM_AUX_ITEMS)
    parser.add_argument("--seed", type=int, default=SEED)
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    print(f"Loading base SFT data from {args.base_data}...")
    base_data = load_base_data(args.base_data)
    print(f"  Base samples: {len(base_data)}")

    print(f"Loading MMLU auxiliary_train...")
    aux_raw = load_mmlu_aux(args.cache_dir)
    print(f"  Auxiliary train samples: {len(aux_raw)}")

    # Overlap check
    print("Loading MMLU test set for overlap check...")
    mmlu_test_fps = load_mmlu_test(args.cache_dir)
    mmlu_overlap = verify_no_overlap(aux_raw, mmlu_test_fps, "MMLU test")
    print(f"  MMLU test overlap: {mmlu_overlap} / {len(aux_raw)}")

    print("Loading ARC-Challenge test set for overlap check...")
    arc_test_fps = load_arc_test(args.cache_dir)
    arc_overlap = verify_no_overlap(aux_raw, arc_test_fps, "ARC test")
    print(f"  ARC test overlap: {arc_overlap} / {len(aux_raw)}")

    # Filter out any overlapping items
    excluded_fps = mmlu_test_fps | arc_test_fps
    filtered_aux = []
    for item in aux_raw:
        fp = hashlib.md5(item["question"].strip().lower().encode()).hexdigest()
        if fp not in excluded_fps:
            filtered_aux.append(item)
    print(f"  After filtering overlaps: {len(filtered_aux)} available")

    if len(filtered_aux) < args.num_aux:
        raise ValueError(
            f"Not enough auxiliary items after filtering: "
            f"{len(filtered_aux)} < {args.num_aux}")

    # Sample
    rng = random.Random(args.seed)
    sampled_aux = rng.sample(filtered_aux, args.num_aux)
    print(f"  Sampled {len(sampled_aux)} auxiliary items (seed={args.seed})")

    # Format as chat
    aux_chat = [format_aux_as_chat(item) for item in sampled_aux]

    # Merge and shuffle
    combined = base_data + aux_chat
    rng2 = random.Random(args.seed)
    rng2.shuffle(combined)

    expected_total = len(base_data) + args.num_aux
    assert len(combined) == expected_total, \
        f"Expected {expected_total}, got {len(combined)}"

    print(f"\nVolume control dataset:")
    print(f"  Base SFT:    {len(base_data)}")
    print(f"  Auxiliary:   {len(aux_chat)}")
    print(f"  Total:       {len(combined)}")

    # Verify format consistency
    sample_base = base_data[0]
    sample_aux = aux_chat[0]
    print(f"\n--- Sample base item ---")
    print(json.dumps(sample_base, indent=2, ensure_ascii=False)[:300])
    print(f"\n--- Sample auxiliary item ---")
    print(json.dumps(sample_aux, indent=2, ensure_ascii=False)[:300])

    if args.dry_run:
        print(f"\n[DRY RUN] Would write {len(combined)} items to {args.output}")

        # Validate all items have correct format
        errors = 0
        for i, item in enumerate(combined):
            if "messages" not in item:
                print(f"  ERROR: item {i} missing 'messages' key")
                errors += 1
            elif not isinstance(item["messages"], list):
                print(f"  ERROR: item {i} 'messages' is not a list")
                errors += 1
            elif len(item["messages"]) < 2:
                print(f"  ERROR: item {i} has fewer than 2 messages")
                errors += 1
        print(f"  Format validation: {len(combined) - errors}/{len(combined)} passed")

        # Check it can be loaded by json
        test_lines = [json.dumps(item, ensure_ascii=False) for item in combined[:10]]
        for tl in test_lines:
            json.loads(tl)  # will raise if invalid
        print("  JSON roundtrip: OK")

        return

    # Write output
    output_path = Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, "w") as f:
        for item in combined:
            f.write(json.dumps(item, ensure_ascii=False) + "\n")
    print(f"\nWritten to {args.output}")
    print(f"File size: {output_path.stat().st_size / 1024 / 1024:.1f} MB")


if __name__ == "__main__":
    main()
