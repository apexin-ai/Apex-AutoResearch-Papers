"""Generate few-shot example orderings for MMLU evaluation.

For each selected subject, loads 5 examples from the ``cais/mmlu`` dev split
and creates 4 random orderings (seeded).  The dev split is purpose-built for
few-shot prompting and contains exactly 5 examples per subject.

Input:  HuggingFace ``cais/mmlu`` dev split (auto-downloaded).
Output: ``data/few_shot_examples.json`` — nested dict
        {subject → {ordering_id → [list of 5 example dicts]}}.
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

N_SHOTS = 5
N_ORDERINGS = 4


def generate_orderings(
    seed: int = 42,
    output_path: str = "data/few_shot_examples.json",
    n_orderings: int = N_ORDERINGS,
) -> dict:
    """Create shuffled few-shot orderings per subject.

    Args:
        seed: Base RNG seed.  Ordering *k* uses ``seed + k``.
        output_path: Where to write the JSON output.

    Returns:
        Nested dict ``{subject → {ordering_id → [examples]}}``.
    """
    result: dict = {}

    for subject in SELECTED_SUBJECTS:
        ds = load_dataset("cais/mmlu", subject, split="dev")
        examples = []
        for i in range(min(N_SHOTS, len(ds))):
            row = ds[i]
            examples.append(
                {
                    "question": row["question"],
                    "choices": row["choices"],
                    "answer_idx": row["answer"],
                }
            )

        orderings = {}
        for ordering_id in range(1, n_orderings + 1):
            rng = random.Random(seed + ordering_id)
            shuffled = examples.copy()
            rng.shuffle(shuffled)
            orderings[ordering_id] = shuffled

        result[subject] = orderings

    Path(output_path).parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(result, f, indent=2, ensure_ascii=False)

    print(
        f"Generated {n_orderings} orderings × "
        f"{len(SELECTED_SUBJECTS)} subjects → {output_path}"
    )
    return result


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Generate few-shot orderings for MMLU"
    )
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--output", default="data/few_shot_examples.json")
    parser.add_argument("--n-orderings", type=int, default=N_ORDERINGS)
    args = parser.parse_args()
    generate_orderings(
        seed=args.seed,
        output_path=args.output,
        n_orderings=args.n_orderings,
    )
