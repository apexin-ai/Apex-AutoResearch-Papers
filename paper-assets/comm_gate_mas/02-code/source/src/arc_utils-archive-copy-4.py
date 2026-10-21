"""ARC-Challenge data loading, answer extraction, and comparison utilities."""
from __future__ import annotations

import random
import re


def load_arc(num_tasks: int = 50, seed: int = 42, split: str = "test") -> list[dict]:
    """Load ARC-Challenge tasks from HuggingFace.

    Returns list of dicts with keys: question, choices, answer_key, ground_truth.
    """
    from datasets import load_dataset

    ds = load_dataset("allenai/ai2_arc", "ARC-Challenge", split=split)
    ds = ds.shuffle(seed=seed).select(range(min(num_tasks, len(ds))))

    tasks = []
    for item in ds:
        labels = item["choices"]["label"]
        texts = item["choices"]["text"]
        choices_str = "\n".join(f"({l}) {t}" for l, t in zip(labels, texts))
        tasks.append({
            "task_id": item["id"],
            "question": item["question"],
            "choices": choices_str,
            "choices_raw": dict(zip(labels, texts)),
            "answer_key": item["answerKey"],
            "ground_truth": item["answerKey"],
        })
    return tasks


def format_arc_question(task: dict) -> str:
    """Format an ARC task as a prompt string."""
    return f"{task['question']}\n\n{task['choices']}"


def extract_arc_answer(text: str) -> str | None:
    """Extract answer letter (A/B/C/D/E) from model response."""
    patterns = [
        r"[Tt]he\s+(?:correct\s+)?answer\s+is\s*[:\s]*\(?([A-E])\)?",
        r"[Aa]nswer\s*[:\s]+\(?([A-E])\)?",
        r"(?:correct|best|right|final)\s+(?:answer|option|choice)\s+is\s*[:\s]*\(?([A-E])\)?",
        r"(?:choose|select|pick|go\s+with)\s+\(?([A-E])\)?",
        r"[Oo]ption\s+\(?([A-E])\)?\s+is\s+(?:correct|right|best)",
        r"\*\*\(?([A-E])\)?\*\*",
        r"^\s*\(?([A-E])\)?\s*[.:]?\s*$",
    ]
    for pat in patterns:
        matches = re.findall(pat, text, re.MULTILINE)
        if matches:
            return matches[-1].upper()

    last_mention = None
    for m in re.finditer(r"\(([A-E])\)", text):
        last_mention = m.group(1).upper()
    if last_mention:
        return last_mention

    for m in re.finditer(r"(?<![a-zA-Z])([A-E])(?![a-zA-Z])", text):
        last_mention = m.group(1).upper()
    return last_mention


def arc_answers_equal(pred: str | None, gold: str | None) -> bool:
    """Compare two ARC answers (single letter)."""
    if pred is None or gold is None:
        return False
    return pred.strip().upper() == gold.strip().upper()


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="ARC-Challenge data utilities")
    parser.add_argument("--num-tasks", type=int, default=10)
    parser.add_argument("--seed", type=int, default=42)
    args = parser.parse_args()

    tasks = load_arc(args.num_tasks, args.seed)
    print(f"Loaded {len(tasks)} ARC-Challenge tasks")
    if tasks:
        t = tasks[0]
        print(f"Sample:\n  Q: {t['question'][:80]}...")
        print(f"  Choices: {list(t['choices_raw'].keys())}")
        print(f"  Answer: {t['answer_key']}")
