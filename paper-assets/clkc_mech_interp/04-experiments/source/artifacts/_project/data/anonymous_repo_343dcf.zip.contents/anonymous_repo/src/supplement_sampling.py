"""Supplement sampling: add new entries from ConflictQA popQA-chatgpt.

Usage:
    python src/supplement_sampling.py \
        --dataset_path data/conflictQA-popQA-chatgpt.json \
        --data_dir data/ \
        --n_new 1500
"""

import argparse
import json
import random
from pathlib import Path

SEED = 43
TRAIN_RATIO = 0.8


def load_jsonl(path):
    with open(path) as f:
        return [json.loads(line) for line in f]


def save_jsonl(data, path):
    with open(path, "w") as f:
        for d in data:
            f.write(json.dumps(d, ensure_ascii=False) + "\n")


def filter_valid(data):
    return [
        d for d in data
        if d.get("parametric_memory_aligned_evidence", "").strip()
        and len(d["parametric_memory_aligned_evidence"]) > 20
        and d.get("counter_memory_aligned_evidence", "").strip()
        and len(d["counter_memory_aligned_evidence"]) > 20
    ]


def raw_to_en_conflict(raw_entries):
    rows = []
    for d in raw_entries:
        base = {
            "question": d["question"],
            "parametric_answer": d["ground_truth"][0],
            "contextual_answer": d["counter_answer"],
            "language": "en",
            "source_subset": "popQA-chatgpt",
        }
        rows.append({
            **base,
            "context": d["counter_memory_aligned_evidence"],
            "label": "conflict",
        })
        rows.append({
            **base,
            "context": d["parametric_memory_aligned_evidence"],
            "label": "no_conflict",
        })
    random.shuffle(rows)
    return rows


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--dataset_path", required=True, help="Path to ConflictQA JSON")
    parser.add_argument("--data_dir", required=True, help="Directory with existing data")
    parser.add_argument("--n_new", type=int, default=1500)
    args = parser.parse_args()

    data_dir = Path(args.data_dir)
    n_new = args.n_new

    print("Loading full ConflictQA popQA-chatgpt dataset...")
    with open(args.dataset_path) as f:
        full_data = [json.loads(line) for line in f]
    print(f"  Total: {len(full_data)}")

    valid_data = filter_valid(full_data)
    print(f"  Valid (evidence > 20 chars): {len(valid_data)}")

    existing_qs = set()
    for fname in ["raw_sampled_train.jsonl", "raw_sampled_test.jsonl"]:
        p = data_dir / fname
        if p.exists():
            for d in load_jsonl(p):
                existing_qs.add(d["question"])
    print(f"  Already sampled: {len(existing_qs)}")

    seen_qs = set()
    deduped = []
    for d in valid_data:
        if d["question"] not in seen_qs:
            seen_qs.add(d["question"])
            deduped.append(d)
    print(f"  Unique questions: {len(deduped)}")

    remaining = [d for d in deduped if d["question"] not in existing_qs]
    print(f"  Remaining after exclusion: {len(remaining)}")

    if len(remaining) < n_new:
        print(f"WARNING: only {len(remaining)} available, need {n_new}")

    rng = random.Random(SEED)
    new_samples = rng.sample(remaining, min(n_new, len(remaining)))
    print(f"  New samples drawn: {len(new_samples)}")

    n_train = int(len(new_samples) * TRAIN_RATIO)
    rng.shuffle(new_samples)
    new_train = new_samples[:n_train]
    new_test = new_samples[n_train:]
    print(f"  Split: {len(new_train)} train + {len(new_test)} test")

    save_jsonl(new_train, data_dir / "raw_sampled_train_supplement.jsonl")
    save_jsonl(new_test, data_dir / "raw_sampled_test_supplement.jsonl")

    random.seed(SEED)
    en_train_supp = raw_to_en_conflict(new_train)
    en_test_supp = raw_to_en_conflict(new_test)
    save_jsonl(en_train_supp, data_dir / "en_conflict_train_supplement.jsonl")
    save_jsonl(en_test_supp, data_dir / "en_conflict_test_supplement.jsonl")

    for prefix in ["raw_sampled", "en_conflict"]:
        for split in ["train", "test"]:
            orig = load_jsonl(data_dir / f"{prefix}_{split}.jsonl")
            supp = load_jsonl(data_dir / f"{prefix}_{split}_supplement.jsonl")
            save_jsonl(orig + supp, data_dir / f"{prefix}_{split}_full.jsonl")

    print("\n=== Final statistics ===")
    for pattern in ["*_supplement.jsonl", "*_full.jsonl"]:
        for p in sorted(data_dir.glob(pattern)):
            with open(p) as f:
                n = sum(1 for _ in f)
            print(f"  {p.name}: {n} lines")


if __name__ == "__main__":
    main()
