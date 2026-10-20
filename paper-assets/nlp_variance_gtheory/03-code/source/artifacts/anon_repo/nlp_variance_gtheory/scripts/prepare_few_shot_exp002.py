"""Prepare few-shot examples for each benchmark in exp-002.

Selection strategy:
  - GSM8K: 5 from train split, 1 per difficulty bin (easy/medium/hard/very_hard) + 1 extra medium
  - ARC-Challenge: 5 from train split, diverse question topics
  - HellaSwag: 5 from train split, diverse activity labels

All examples come from train splits → no overlap with test items by design.
(GSM8K test items from test split; ARC test items from test split;
 HellaSwag test items from validation split.)
"""

import json
import random
import re
from collections import defaultdict
from pathlib import Path

from datasets import load_dataset


def _count_steps(answer_text: str) -> int:
    lines = [l.strip() for l in answer_text.strip().split("\n") if l.strip()]
    return max(len([l for l in lines if not l.startswith("####")]), 1)


def _bin_steps(n: int) -> str:
    if n <= 2: return "easy(1-2)"
    if n <= 4: return "medium(3-4)"
    if n <= 6: return "hard(5-6)"
    return "very_hard(7+)"


def _extract_answer(text: str) -> str:
    m = re.search(r"####\s*(.+)", text)
    return m.group(1).strip().replace(",", "") if m else text.strip()


def prepare_gsm8k(seed=42, cache_dir=None):
    """Select 5 GSM8K train examples covering all difficulty levels."""
    ds = load_dataset("openai/gsm8k", "main", split="train", cache_dir=cache_dir)
    rng = random.Random(seed)

    by_diff = defaultdict(list)
    for idx in range(len(ds)):
        row = ds[idx]
        steps = _count_steps(row["answer"])
        diff = _bin_steps(steps)
        by_diff[diff].append((idx, row, steps))

    # Pick 1 from each difficulty, then 1 extra from medium (most representative)
    targets = {"easy(1-2)": 1, "medium(3-4)": 2, "hard(5-6)": 1, "very_hard(7+)": 1}
    examples = []
    for diff, count in targets.items():
        pool = by_diff[diff]
        chosen = rng.sample(pool, min(count, len(pool)))
        for idx, row, steps in chosen:
            examples.append({
                "item_id": f"gsm8k_train_{idx}",
                "benchmark": "gsm8k",
                "question": row["question"],
                "choices": None,
                "answer_idx": None,
                "answer": _extract_answer(row["answer"]),
                "metadata": {
                    "n_steps": steps,
                    "difficulty": diff,
                    "raw_answer": row["answer"],
                },
            })

    rng.shuffle(examples)
    return examples


def prepare_arc(seed=42, cache_dir=None):
    """Select 5 ARC-Challenge train examples with diverse topics."""
    ds = load_dataset("allenai/ai2_arc", "ARC-Challenge", split="train", cache_dir=cache_dir)
    rng = random.Random(seed)

    answer_key_map = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4,
                      "1": 0, "2": 1, "3": 2, "4": 3, "5": 4}

    items = []
    for idx in range(len(ds)):
        row = ds[idx]
        choices = row["choices"]["text"]
        labels = row["choices"]["label"]
        answer_key = row["answerKey"]
        items.append({
            "item_id": f"arc_train_{idx}",
            "benchmark": "arc_challenge",
            "question": row["question"],
            "choices": choices,
            "answer_idx": answer_key_map.get(answer_key, 0),
            "answer": answer_key,
            "metadata": {
                "n_choices": len(choices),
                "labels": labels,
            },
        })

    # Spread across different answer positions (A/B/C/D) for diversity
    by_answer = defaultdict(list)
    for it in items:
        by_answer[it["answer"]].append(it)

    examples = []
    for ans in ["A", "B", "C", "D"]:
        if by_answer[ans]:
            examples.append(rng.choice(by_answer[ans]))
    # One more from the full pool (avoid duplicates)
    chosen_ids = {e["item_id"] for e in examples}
    remaining = [it for it in items if it["item_id"] not in chosen_ids]
    examples.append(rng.choice(remaining))

    rng.shuffle(examples)
    return examples[:5]


def prepare_hellaswag(seed=42, cache_dir=None):
    """Select 5 HellaSwag train examples with diverse activity labels."""
    ds = load_dataset("Rowan/hellaswag", split="train", cache_dir=cache_dir)
    rng = random.Random(seed)

    by_activity = defaultdict(list)
    for idx in range(len(ds)):
        row = ds[idx]
        label = int(row["label"]) if row["label"] != "" else 0
        activity = row["activity_label"]
        by_activity[activity].append({
            "item_id": f"hellaswag_train_{idx}",
            "benchmark": "hellaswag",
            "question": row["ctx"],
            "choices": row["endings"],
            "answer_idx": label,
            "answer": str(label),
            "metadata": {
                "activity_label": activity,
            },
        })

    # Pick 5 different activity labels
    activities = list(by_activity.keys())
    chosen_activities = rng.sample(activities, min(5, len(activities)))
    examples = [rng.choice(by_activity[a]) for a in chosen_activities]

    rng.shuffle(examples)
    return examples[:5]


def main():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--output-dir", default="data")
    parser.add_argument("--cache-dir", default=None)
    args = parser.parse_args()

    out = Path(args.output_dir)
    out.mkdir(parents=True, exist_ok=True)

    print("Preparing GSM8K few-shot examples...")
    gsm8k = prepare_gsm8k(args.seed, args.cache_dir)
    with open(out / "few_shot_gsm8k.json", "w") as f:
        json.dump(gsm8k, f, indent=2, ensure_ascii=False)
    print(f"  {len(gsm8k)} examples → {out / 'few_shot_gsm8k.json'}")
    for ex in gsm8k:
        print(f"    [{ex['metadata']['difficulty']}] answer={ex['answer']}")

    print("\nPreparing ARC-Challenge few-shot examples...")
    arc = prepare_arc(args.seed, args.cache_dir)
    with open(out / "few_shot_arc.json", "w") as f:
        json.dump(arc, f, indent=2, ensure_ascii=False)
    print(f"  {len(arc)} examples → {out / 'few_shot_arc.json'}")
    for ex in arc:
        print(f"    answer={ex['answer']}, n_choices={ex['metadata']['n_choices']}")

    print("\nPreparing HellaSwag few-shot examples...")
    hellaswag = prepare_hellaswag(args.seed, args.cache_dir)
    with open(out / "few_shot_hellaswag.json", "w") as f:
        json.dump(hellaswag, f, indent=2, ensure_ascii=False)
    print(f"  {len(hellaswag)} examples → {out / 'few_shot_hellaswag.json'}")
    for ex in hellaswag:
        print(f"    [{ex['metadata']['activity_label']}] answer_idx={ex['answer_idx']}")

    print("\nDone.")


if __name__ == "__main__":
    main()
