"""Sample 200 items from MATH dataset, stratified by difficulty × subject.
Also generates 5 few-shot examples from the train split.
"""
import json
import random
import re
from collections import Counter, defaultdict
from pathlib import Path
from datasets import load_dataset

DATASET_NAME = "DigitalLearningGmbH/MATH-lighteval"
CACHE_DIR = "/path/to/model"


def extract_boxed_answer(solution: str) -> str:
    pattern = r'\\boxed\{'
    matches = list(re.finditer(pattern, solution))
    if not matches:
        return solution.strip().split('\n')[-1].strip()
    last_match = matches[-1]
    start = last_match.end()
    depth = 1
    i = start
    while i < len(solution) and depth > 0:
        if solution[i] == '{':
            depth += 1
        elif solution[i] == '}':
            depth -= 1
        i += 1
    return solution[start:i-1].strip()


def _level_num(level_str: str) -> int:
    m = re.search(r'\d+', level_str)
    return int(m.group()) if m else 1


def sample_math_items(n_items: int = 200, seed: int = 42) -> list[dict]:
    ds = load_dataset(DATASET_NAME, split="test", cache_dir=CACHE_DIR)

    groups = defaultdict(list)
    for idx, row in enumerate(ds):
        level = row.get("level", "Level 1")
        subject = row.get("type", "unknown")
        groups[(level, subject)].append((idx, row))

    print(f"Total items: {len(ds)}")
    print(f"Groups (level × subject): {len(groups)}")
    for key, items in sorted(groups.items()):
        print(f"  {key}: {len(items)} items")

    rng = random.Random(seed)
    sampled = []
    sorted_keys = sorted(groups.keys())
    n_groups = len(groups)
    base_quota = n_items // n_groups
    remainder = n_items - base_quota * n_groups

    for i, key in enumerate(sorted_keys):
        pool = groups[key]
        quota = base_quota + (1 if i < remainder else 0)
        quota = min(quota, len(pool))
        chosen = rng.sample(pool, quota)
        for idx, row in chosen:
            answer = extract_boxed_answer(row["solution"])
            sampled.append({
                "item_id": f"math_{idx}",
                "benchmark": "math",
                "question": row["problem"],
                "choices": None,
                "answer_idx": None,
                "answer": answer,
                "metadata": {
                    "difficulty": _level_num(row.get("level", "Level 1")),
                    "difficulty_str": row.get("level", "Level 1"),
                    "subject": row.get("type", "unknown"),
                    "solution": row["solution"],
                },
            })

    if len(sampled) < n_items:
        sampled_ids = {s["item_id"] for s in sampled}
        all_remaining = [(idx, row) for key in sorted_keys
                         for idx, row in groups[key]
                         if f"math_{idx}" not in sampled_ids]
        extra = rng.sample(all_remaining, min(n_items - len(sampled), len(all_remaining)))
        for idx, row in extra:
            answer = extract_boxed_answer(row["solution"])
            sampled.append({
                "item_id": f"math_{idx}",
                "benchmark": "math",
                "question": row["problem"],
                "choices": None,
                "answer_idx": None,
                "answer": answer,
                "metadata": {
                    "difficulty": _level_num(row.get("level", "Level 1")),
                    "difficulty_str": row.get("level", "Level 1"),
                    "subject": row.get("type", "unknown"),
                    "solution": row["solution"],
                },
            })

    rng.shuffle(sampled)
    sampled = sampled[:n_items]
    print(f"\nSampled {len(sampled)} items")
    print(f"Difficulty: {dict(sorted(Counter(s['metadata']['difficulty'] for s in sampled).items()))}")
    print(f"Subject: {dict(sorted(Counter(s['metadata']['subject'] for s in sampled).items()))}")
    return sampled


def generate_few_shot(seed: int = 42) -> list[dict]:
    ds = load_dataset(DATASET_NAME, split="train", cache_dir=CACHE_DIR)

    by_level = defaultdict(list)
    for idx, row in enumerate(ds):
        by_level[_level_num(row.get("level", "Level 1"))].append((idx, row))

    rng = random.Random(seed)
    examples = []
    for level in sorted(by_level.keys()):
        pool = by_level[level]
        rng.shuffle(pool)
        for idx, row in pool:
            if len(row["solution"]) < 800:
                answer = extract_boxed_answer(row["solution"])
                examples.append({
                    "item_id": f"math_train_{idx}",
                    "benchmark": "math",
                    "question": row["problem"],
                    "choices": None,
                    "answer_idx": None,
                    "answer": answer,
                    "metadata": {
                        "difficulty": level,
                        "difficulty_str": row.get("level", "Level 1"),
                        "subject": row.get("type", "unknown"),
                        "solution": row["solution"],
                        "raw_answer": row["solution"],
                    },
                })
                break

    print(f"\nFew-shot: {len(examples)} examples")
    for ex in examples:
        print(f"  L{ex['metadata']['difficulty']} ({ex['metadata']['subject']}): {ex['answer'][:50]}")
    return examples


if __name__ == "__main__":
    items = sample_math_items(200, 42)
    Path("data").mkdir(exist_ok=True)
    with open("data/math_items_exp002.json", "w") as f:
        json.dump(items, f, indent=2, ensure_ascii=False)
    print(f"\n→ data/math_items_exp002.json ({len(items)} items)")

    fs = generate_few_shot(42)
    with open("data/few_shot_math.json", "w") as f:
        json.dump(fs, f, indent=2, ensure_ascii=False)
    print(f"→ data/few_shot_math.json ({len(fs)} examples)")
