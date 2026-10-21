"""GSM8K data loading and preprocessing utilities.

Input: JSONL file with GSM8K format (question + answer fields)
Output: List of dicts with question, ground_truth (extracted number), and original answer
"""

import json
import os
import random
import re
from typing import Optional


def extract_ground_truth(answer_str: str) -> str:
    """Extract numerical answer from GSM8K answer format (#### <number>)."""
    match = re.search(r"####\s*(.+)", answer_str)
    if match:
        return match.group(1).strip().replace(",", "")
    return answer_str.strip()


def load_gsm8k(
    path: str = "data/gsm8k/test.jsonl",
    num_tasks: Optional[int] = None,
    seed: int = 42,
) -> list[dict]:
    """Load GSM8K dataset from JSONL file.

    Returns list of dicts with keys: question, ground_truth, answer (original).
    If num_tasks is specified, randomly sample that many tasks.
    """
    items = []
    with open(path) as f:
        for line in f:
            raw = json.loads(line)
            items.append({
                "question": raw["question"],
                "ground_truth": extract_ground_truth(raw["answer"]),
                "answer": raw["answer"],
            })

    if num_tasks is not None and num_tasks < len(items):
        rng = random.Random(seed)
        items = rng.sample(items, num_tasks)

    return items


def load_gsm8k_from_hf(
    split: str = "test",
    num_tasks: Optional[int] = None,
    seed: int = 42,
) -> list[dict]:
    """Load GSM8K directly from HuggingFace (fallback if local file unavailable)."""
    from datasets import load_dataset
    ds = load_dataset("gsm8k", "main", split=split)
    if num_tasks is not None:
        ds = ds.shuffle(seed=seed).select(range(min(num_tasks, len(ds))))
    return [
        {
            "question": item["question"],
            "ground_truth": extract_ground_truth(item["answer"]),
            "answer": item["answer"],
        }
        for item in ds
    ]


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="GSM8K data utilities")
    parser.add_argument("--path", default="data/gsm8k/test.jsonl")
    parser.add_argument("--num-tasks", type=int, default=None)
    parser.add_argument("--seed", type=int, default=42)
    args = parser.parse_args()

    items = load_gsm8k(args.path, args.num_tasks, args.seed)
    print(f"Loaded {len(items)} tasks")
    if items:
        print(f"Sample: Q={items[0]['question'][:80]}... A={items[0]['ground_truth']}")
