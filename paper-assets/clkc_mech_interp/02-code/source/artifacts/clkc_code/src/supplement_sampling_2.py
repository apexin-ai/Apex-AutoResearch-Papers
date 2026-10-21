"""Second supplement sampling: add 1000 new entries (2000 → 3000 total)."""

import json
import random
from pathlib import Path
from huggingface_hub import hf_hub_download

DATA_DIR = Path(__file__).resolve().parent.parent / "data"
SEED = 44
N_NEW = 1000
TRAIN_RATIO = 0.8


def load_jsonl(path: Path) -> list[dict]:
    with open(path) as f:
        return [json.loads(line) for line in f]


def save_jsonl(data: list[dict], path: Path):
    with open(path, "w") as f:
        for d in data:
            f.write(json.dumps(d, ensure_ascii=False) + "\n")


def append_jsonl(data: list[dict], path: Path):
    with open(path, "a") as f:
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
    for fname in ["raw_sampled_train_full.jsonl", "raw_sampled_test_full.jsonl"]:
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
    print(f"  Already sampled (round 1+2 existing): {len(existing_qs)}")

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

    save_jsonl(new_train, DATA_DIR / "raw_sampled_train_supplement_2.jsonl")
    save_jsonl(new_test, DATA_DIR / "raw_sampled_test_supplement_2.jsonl")

    random.seed(SEED)
    en_train_supp = raw_to_en_conflict(new_train)
    en_test_supp = raw_to_en_conflict(new_test)
    save_jsonl(en_train_supp, DATA_DIR / "en_conflict_train_supplement_2.jsonl")
    save_jsonl(en_test_supp, DATA_DIR / "en_conflict_test_supplement_2.jsonl")

    append_jsonl(new_train, DATA_DIR / "raw_sampled_train_full.jsonl")
    append_jsonl(new_test, DATA_DIR / "raw_sampled_test_full.jsonl")
    append_jsonl(en_train_supp, DATA_DIR / "en_conflict_train_full.jsonl")
    append_jsonl(en_test_supp, DATA_DIR / "en_conflict_test_full.jsonl")

    print("\n=== Final statistics ===")
    for pattern in ["raw_sampled_*_full.jsonl", "en_conflict_*_full.jsonl",
                     "*_supplement_2.jsonl"]:
        for p in sorted(DATA_DIR.glob(pattern)):
            with open(p) as f:
                n = sum(1 for _ in f)
            print(f"  {p.name}: {n} lines")

    all_full_qs = set()
    for split in ["train", "test"]:
        for d in load_jsonl(DATA_DIR / f"raw_sampled_{split}_full.jsonl"):
            all_full_qs.add(d["question"])
    print(f"\n  Total unique questions in _full files: {len(all_full_qs)}")
    print(f"  ConflictQA remaining unused: {len(deduped) - len(all_full_qs)}")

    supp2_qs = set()
    for split in ["train", "test"]:
        for d in load_jsonl(DATA_DIR / f"raw_sampled_{split}_supplement_2.jsonl"):
            supp2_qs.add(d["question"])
    overlap = supp2_qs & existing_qs
    assert len(overlap) == 0, f"Overlap found: {len(overlap)} questions"
    assert len(supp2_qs) == N_NEW, f"Expected {N_NEW}, got {len(supp2_qs)}"
    print(f"  Verified: {len(supp2_qs)} new questions, 0 overlap with existing.")


if __name__ == "__main__":
    main()
