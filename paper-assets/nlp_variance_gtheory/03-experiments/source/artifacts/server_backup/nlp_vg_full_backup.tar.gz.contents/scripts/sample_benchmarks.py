"""Stratified sampling of benchmark items for G-theory exp-002.

Produces 200-item samples from GSM8K, ARC-Challenge, and HellaSwag
with stratification to ensure diversity coverage.

Stratification keys:
  - GSM8K: difficulty proxy = number of reasoning steps in the answer
  - ARC-Challenge: number of answer choices (3/4/5)
  - HellaSwag: activity_label

Output JSON schema (per item):
  {item_id, benchmark, question, choices, answer_idx, answer, metadata}
"""

import argparse
import json
import math
import random
import re
from collections import Counter, defaultdict
from pathlib import Path

from datasets import load_dataset


def _count_gsm8k_steps(answer_text: str) -> int:
    lines = [l.strip() for l in answer_text.strip().split("\n") if l.strip()]
    step_lines = [l for l in lines if not l.startswith("####")]
    return max(len(step_lines), 1)


def _extract_gsm8k_answer(answer_text: str) -> str:
    m = re.search(r"####\s*(.+)", answer_text)
    return m.group(1).strip().replace(",", "") if m else answer_text.strip()


def _bin_steps(n_steps: int) -> str:
    if n_steps <= 2:
        return "easy(1-2)"
    elif n_steps <= 4:
        return "medium(3-4)"
    elif n_steps <= 6:
        return "hard(5-6)"
    else:
        return "very_hard(7+)"


def stratified_sample(items_by_stratum, n_total, rng):
    strata = list(items_by_stratum.keys())
    per_stratum = max(1, n_total // len(strata))

    sampled = []
    overflow_pool = []

    for stratum in sorted(strata):
        pool = items_by_stratum[stratum]
        k = min(per_stratum, len(pool))
        chosen = rng.sample(pool, k)
        sampled.extend(chosen)
        leftover = [x for x in pool if x not in chosen]
        overflow_pool.extend(leftover)

    if len(sampled) < n_total and overflow_pool:
        extra = rng.sample(overflow_pool, min(n_total - len(sampled), len(overflow_pool)))
        sampled.extend(extra)

    if len(sampled) > n_total:
        sampled = rng.sample(sampled, n_total)

    return sampled


def sample_gsm8k(n_items, seed, cache_dir=None):
    ds = load_dataset("openai/gsm8k", "main", split="test", cache_dir=cache_dir)
    rng = random.Random(seed)

    by_difficulty = defaultdict(list)
    for idx in range(len(ds)):
        row = ds[idx]
        steps = _count_gsm8k_steps(row["answer"])
        difficulty = _bin_steps(steps)
        answer = _extract_gsm8k_answer(row["answer"])
        item = {
            "item_id": f"gsm8k_{idx}",
            "benchmark": "gsm8k",
            "question": row["question"],
            "choices": None,
            "answer_idx": None,
            "answer": answer,
            "metadata": {
                "n_steps": steps,
                "difficulty": difficulty,
                "raw_answer": row["answer"],
            },
        }
        by_difficulty[difficulty].append(item)

    sampled = stratified_sample(by_difficulty, n_items, rng)
    rng.shuffle(sampled)
    return sampled


def sample_arc_challenge(n_items, seed, cache_dir=None):
    ds = load_dataset("allenai/ai2_arc", "ARC-Challenge", split="test", cache_dir=cache_dir)
    rng = random.Random(seed)

    answer_key_map = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4,
                      "1": 0, "2": 1, "3": 2, "4": 3, "5": 4}

    by_n_choices = defaultdict(list)
    for idx in range(len(ds)):
        row = ds[idx]
        choices = row["choices"]["text"]
        labels = row["choices"]["label"]
        n_choices = len(choices)
        answer_key = row["answerKey"]
        answer_idx = answer_key_map.get(answer_key, 0)

        item = {
            "item_id": f"arc_challenge_{idx}",
            "benchmark": "arc_challenge",
            "question": row["question"],
            "choices": choices,
            "answer_idx": answer_idx,
            "answer": answer_key,
            "metadata": {
                "n_choices": n_choices,
                "labels": labels,
            },
        }
        by_n_choices[f"{n_choices}_choices"].append(item)

    sampled = stratified_sample(by_n_choices, n_items, rng)
    rng.shuffle(sampled)
    return sampled


def sample_hellaswag(n_items, seed, cache_dir=None):
    ds = load_dataset("Rowan/hellaswag", split="validation", cache_dir=cache_dir)
    rng = random.Random(seed)

    by_activity = defaultdict(list)
    for idx in range(len(ds)):
        row = ds[idx]
        label = int(row["label"]) if row["label"] != "" else 0
        activity = row["activity_label"]

        item = {
            "item_id": f"hellaswag_{idx}",
            "benchmark": "hellaswag",
            "question": row["ctx"],
            "choices": row["endings"],
            "answer_idx": label,
            "answer": str(label),
            "metadata": {
                "activity_label": activity,
            },
        }
        by_activity[activity].append(item)

    sampled = stratified_sample(by_activity, n_items, rng)
    rng.shuffle(sampled)
    return sampled


SAMPLERS = {
    "gsm8k": sample_gsm8k,
    "arc_challenge": sample_arc_challenge,
    "hellaswag": sample_hellaswag,
}

FILENAMES = {
    "gsm8k": "gsm8k_items_exp002.json",
    "arc_challenge": "arc_items_exp002.json",
    "hellaswag": "hellaswag_items_exp002.json",
}


def sample_and_save(benchmark, n_items, seed, output_dir, cache_dir=None):
    items = SAMPLERS[benchmark](n_items, seed, cache_dir)
    out_path = Path(output_dir) / FILENAMES[benchmark]
    out_path.parent.mkdir(parents=True, exist_ok=True)
    with open(out_path, "w") as f:
        json.dump(items, f, indent=2, ensure_ascii=False)

    if benchmark == "gsm8k":
        dist = Counter(it["metadata"]["difficulty"] for it in items)
    elif benchmark == "arc_challenge":
        dist = Counter(it["metadata"]["n_choices"] for it in items)
    elif benchmark == "hellaswag":
        dist = Counter(it["metadata"]["activity_label"] for it in items)
    else:
        dist = {}

    print(f"\n{benchmark}: {len(items)} items -> {out_path}")
    print(f"  Stratum distribution ({len(dist)} strata):")
    for k, v in sorted(dist.items(), key=lambda x: -x[1])[:15]:
        print(f"    {k}: {v}")
    if len(dist) > 15:
        print(f"    ... and {len(dist) - 15} more strata")

    return items


def main():
    parser = argparse.ArgumentParser(description="Stratified sampling for exp-002")
    parser.add_argument("--benchmarks", nargs="+",
                        default=["gsm8k", "arc_challenge", "hellaswag"],
                        choices=["gsm8k", "arc_challenge", "hellaswag"])
    parser.add_argument("--n-items", type=int, default=200)
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--output-dir", default="data")
    parser.add_argument("--cache-dir", default=None)
    args = parser.parse_args()

    for bench in args.benchmarks:
        sample_and_save(bench, args.n_items, args.seed, args.output_dir, args.cache_dir)


if __name__ == "__main__":
    main()
