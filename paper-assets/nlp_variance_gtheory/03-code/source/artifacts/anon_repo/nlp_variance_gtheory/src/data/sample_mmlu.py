"""Sample MMLU items via stratified sampling across diverse subjects.

Subjects span STEM, humanities, social science, professional, and legal
domains.  Default: 10 subjects × 20 items = 200 items from the test split
of ``cais/mmlu``.

Input:  HuggingFace ``cais/mmlu`` dataset (auto-downloaded).
Output: ``data/mmlu_items.json`` — list of item dicts.

Usage:
    python -m src.data.sample_mmlu
    python -m src.data.sample_mmlu --n-subjects 5 --n-items 50
"""

import argparse
import json
import random
from pathlib import Path

from datasets import load_dataset

SELECTED_SUBJECTS = [
    "abstract_algebra",
    "college_physics",
    "world_religions",
    "us_foreign_policy",
    "professional_medicine",
    "high_school_mathematics",
    "computer_security",
    "philosophy",
    "clinical_knowledge",
    "international_law",
]

DEFAULT_N_SUBJECTS = 10
DEFAULT_N_ITEMS = 200


def sample_items(
    seed: int = 42,
    output_path: str = "data/mmlu_items.json",
    n_items: int = DEFAULT_N_ITEMS,
    n_subjects: int = DEFAULT_N_SUBJECTS,
) -> list[dict]:
    """Draw a stratified sample of MMLU items.

    Args:
        seed: RNG seed for reproducible sampling.
        output_path: Where to write the JSON output.
        n_items: Total number of items to sample.
        n_subjects: Number of subjects to use (from SELECTED_SUBJECTS).

    Returns:
        List of sampled item dicts.
    """
    subjects = SELECTED_SUBJECTS[:n_subjects]
    items_per_subject = n_items // n_subjects

    rng = random.Random(seed)
    all_items: list[dict] = []

    for subject in subjects:
        ds = load_dataset("cais/mmlu", subject, split="test")
        indices = rng.sample(range(len(ds)), min(items_per_subject, len(ds)))

        for idx in indices:
            row = ds[idx]
            all_items.append(
                {
                    "subject": subject,
                    "question": row["question"],
                    "choices": row["choices"],
                    "answer_idx": row["answer"],
                    "item_id": f"{subject}_{idx}",
                }
            )

    Path(output_path).parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(all_items, f, indent=2, ensure_ascii=False)

    print(f"Sampled {len(all_items)} items from {len(subjects)} subjects → {output_path}")
    return all_items


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Sample MMLU items for G-theory study")
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--output", default="data/mmlu_items.json")
    parser.add_argument("--n-items", type=int, default=DEFAULT_N_ITEMS)
    parser.add_argument("--n-subjects", type=int, default=DEFAULT_N_SUBJECTS)
    args = parser.parse_args()
    sample_items(
        seed=args.seed,
        output_path=args.output,
        n_items=args.n_items,
        n_subjects=args.n_subjects,
    )
