"""StrategyQA data loading, answer extraction, and comparison utilities."""
from __future__ import annotations

import random
import re


def load_strategyqa(num_tasks: int = 250, seed: int = 42) -> list[dict]:
    """Load StrategyQA tasks from HuggingFace.

    Returns list of dicts with keys: task_id, question, ground_truth.
    """
    from datasets import load_dataset

    ds = load_dataset("ChilleD/StrategyQA", split="test")
    rng = random.Random(seed)
    indices = list(range(len(ds)))
    rng.shuffle(indices)
    indices = indices[:min(num_tasks, len(ds))]

    tasks = []
    for i, idx in enumerate(indices):
        item = ds[idx]
        answer = "yes" if item["answer"] else "no"
        tasks.append({
            "task_id": f"stratqa_{i:04d}",
            "question": item["question"],
            "ground_truth": answer,
        })
    return tasks


def format_strategyqa_question(task: dict) -> str:
    """Format a StrategyQA task as a prompt string."""
    return f"{task['question']}\n\nAnswer yes or no, with step-by-step reasoning."


def extract_strategyqa_answer(text: str) -> str | None:
    """Extract yes/no answer from model response."""
    patterns = [
        r"[Tt]he\s+(?:final\s+)?answer\s+is\s*[:\s]*(yes|no)",
        r"[Aa]nswer\s*[:\s]+(yes|no)",
        r"\*\*(yes|no)\*\*",
        r"^(yes|no)\s*[.!]?\s*$",
    ]
    for pat in patterns:
        matches = re.findall(pat, text, re.MULTILINE | re.IGNORECASE)
        if matches:
            return matches[-1].lower()
    text_lower = text.lower()
    last_yes = text_lower.rfind("yes")
    last_no = text_lower.rfind("no")
    if last_yes > last_no and last_yes >= 0:
        return "yes"
    elif last_no > last_yes and last_no >= 0:
        return "no"
    return None


def strategyqa_answers_equal(pred: str | None, gold: str | None) -> bool:
    """Compare two StrategyQA answers."""
    if pred is None or gold is None:
        return False
    return pred.lower().strip() == gold.lower().strip()
