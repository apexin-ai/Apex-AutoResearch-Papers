"""Supplement sampling: add 1500 new entries from ConflictQA popQA-chatgpt."""

import json
import random
from pathlib import Path
from huggingface_hub import hf_hub_download

DATA_DIR = Path(__file__).resolve().parent.parent / "data"
SEED = 43
N_NEW = 1500
TRAIN_RATIO = 0.8


def load_jsonl(path: Path) -> list[dict]:
    with open(path) as f:
        return [json.loads(line) for line in f]


def save_jsonl(data: list[dict], path: Path):
    with open(path, "w") as f:
        for d in data:
            f.write(json.dumps(d, ensure_ascii=False) + "\n")


def load_full_dataset() -> list[dict]:
    path = hf_hub_download(
        "osunlp/ConflictQA",
        "conflictQA-popQA-chatgpt.json",
        repo_type="dataset",
    )
    with open(path) as f:
        return [json.loads(line) for line in f]


def get_existing_questions() -> set[str]:
    questions = set()
    for fname in ["raw_sampled_train.jsonl", "raw_sampled_test.jsonl"]:
        p = DATA_DIR / fname
        if p.exists():
            for d in load_jsonl(p):
                questions.add(d["question"])
    return questions


def filter_valid(data: list[dict]) -> list[dict]:
    return [
        d for d in data
        if d.get("parametric_memory_aligned_evidence", "").strip()
        and len(d["parametric_memory_aligned_evidence"]) > 20
        and d.get("counter_memory_aligned_evidence", "").strip()
        and len(d["counter_memory_aligned_evidence"]) > 20
    ]


def raw_to_en_conflict(raw_entries: list[dict]) -> list[dict]:
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
    print("Loading full ConflictQA popQA-chatgpt dataset...")
    full_data = load_full_dataset()
    print(f"  Total: {len(full_data)}")

    valid_data = filter_valid(full_data)
    print(f"  Valid (evidence > 20 chars): {len(valid_data)}")

    existing_qs = get_existing_questions()
    print(f"  Already sampled: {len(existing_qs)}")

    # Deduplicate by question (keep first occurrence)
    seen_qs = set()
    deduped = []
    for d in valid_data:
        if d["question"] not in seen_qs:
            seen_qs.add(d["question"])
            deduped.append(d)
    print(f"  Unique questions in full dataset: {len(deduped)}")

    remaining = [d for d in deduped if d["question"] not in existing_qs]
    print(f"  Remaining after exclusion: {len(remaining)}")

    if len(remaining) < N_NEW:
        print(f"WARNING: only {len(remaining)} available, need {N_NEW}")

    rng = random.Random(SEED)
    new_samples = rng.sample(remaining, min(N_NEW, len(remaining)))
    print(f"  New samples drawn: {len(new_samples)}")

    n_train = int(len(new_samples) * TRAIN_RATIO)
    rng.shuffle(new_samples)
    new_train = new_samples[:n_train]
    new_test = new_samples[n_train:]
    print(f"  Split: {len(new_train)} train + {len(new_test)} test")

    # Save supplement raw
    save_jsonl(new_train, DATA_DIR / "raw_sampled_train_supplement.jsonl")
    save_jsonl(new_test, DATA_DIR / "raw_sampled_test_supplement.jsonl")

    # Generate en_conflict supplement
    random.seed(SEED)
    en_train_supp = raw_to_en_conflict(new_train)
    en_test_supp = raw_to_en_conflict(new_test)
    save_jsonl(en_train_supp, DATA_DIR / "en_conflict_train_supplement.jsonl")
    save_jsonl(en_test_supp, DATA_DIR / "en_conflict_test_supplement.jsonl")

    # Merge with originals
    for prefix in ["raw_sampled", "en_conflict"]:
        for split in ["train", "test"]:
            orig = load_jsonl(DATA_DIR / f"{prefix}_{split}.jsonl")
            supp = load_jsonl(DATA_DIR / f"{prefix}_{split}_supplement.jsonl")
            save_jsonl(orig + supp, DATA_DIR / f"{prefix}_{split}_full.jsonl")

    # Print stats
    print("\n=== Final statistics ===")
    for pattern in ["*_supplement.jsonl", "*_full.jsonl"]:
        for p in sorted(DATA_DIR.glob(pattern)):
            with open(p) as f:
                n = sum(1 for _ in f)
            print(f"  {p.name}: {n} lines")

    # Verify new supplements don't overlap with existing
    supp_qs = set()
    for split in ["train", "test"]:
        for d in load_jsonl(DATA_DIR / f"raw_sampled_{split}_supplement.jsonl"):
            supp_qs.add(d["question"])
    overlap = supp_qs & existing_qs
    assert len(overlap) == 0, f"Overlap between supplement and existing: {overlap}"
    assert len(supp_qs) == N_NEW, f"Expected {N_NEW} unique new questions, got {len(supp_qs)}"
    print(f"\n  Verified: {len(supp_qs)} new questions, 0 overlap with existing.")


if __name__ == "__main__":
    main()
