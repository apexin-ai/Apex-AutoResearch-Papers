"""Sample items from multiple benchmarks for G-theory exp-002.

Supports: GSM8K, ARC-Challenge, HellaSwag.
Output: JSON with unified schema [{item_id, benchmark, question, choices, answer_idx, answer, metadata}, ...]

Usage:
    python -m src.data.sample_benchmarks --benchmark gsm8k --n-items 200 --output data/gsm8k_items.json
    python -m src.data.sample_benchmarks --benchmark arc_challenge --n-items 200 --output data/arc_items.json
    python -m src.data.sample_benchmarks --all --n-items 200 --output-dir data/
"""

import argparse
import json
import random
import re
from pathlib import Path

from datasets import load_dataset

BENCHMARKS = ["gsm8k", "arc_challenge", "hellaswag"]


def _extract_gsm8k_answer(answer_text: str) -> str:
    match = re.search(r"####\s*(.+)", answer_text)
    if match:
        return match.group(1).strip().replace(",", "")
    return answer_text.strip()


def _sample_gsm8k(n_items: int, seed: int) -> list[dict]:
    ds = load_dataset("openai/gsm8k", "main", split="test")
    rng = random.Random(seed)
    indices = rng.sample(range(len(ds)), min(n_items, len(ds)))
    items = []
    for idx in indices:
        row = ds[idx]
        answer = _extract_gsm8k_answer(row["answer"])
        items.append(
            {
                "item_id": f"gsm8k_{idx}",
                "benchmark": "gsm8k",
                "question": row["question"],
                "choices": None,
                "answer_idx": None,
                "answer": answer,
                "metadata": {"raw_answer": row["answer"]},
            }
        )
    return items


def _sample_arc_challenge(n_items: int, seed: int) -> list[dict]:
    ds = load_dataset("allenai/ai2_arc", "ARC-Challenge", split="test")
    rng = random.Random(seed)
    indices = rng.sample(range(len(ds)), min(n_items, len(ds)))
    answer_key_map = {"A": 0, "B": 1, "C": 2, "D": 3, "1": 0, "2": 1, "3": 2, "4": 3}
    items = []
    for idx in indices:
        row = ds[idx]
        choices = row["choices"]["text"]
        answer_key = row["answerKey"]
        answer_idx = answer_key_map.get(answer_key, 0)
        items.append(
            {
                "item_id": f"arc_challenge_{idx}",
                "benchmark": "arc_challenge",
                "question": row["question"],
                "choices": choices,
                "answer_idx": answer_idx,
                "answer": answer_key,
                "metadata": {},
            }
        )
    return items


def _sample_hellaswag(n_items: int, seed: int) -> list[dict]:
    ds = load_dataset("Rowan/hellaswag", split="validation")
    rng = random.Random(seed)
    indices = rng.sample(range(len(ds)), min(n_items, len(ds)))
    items = []
    for idx in indices:
        row = ds[idx]
        label = int(row["label"]) if row["label"] != "" else 0
        items.append(
            {
                "item_id": f"hellaswag_{idx}",
                "benchmark": "hellaswag",
                "question": row["ctx"],
                "choices": row["endings"],
                "answer_idx": label,
                "answer": str(label),
                "metadata": {"activity_label": row["activity_label"]},
            }
        )
    return items


SAMPLERS = {
    "gsm8k": _sample_gsm8k,
    "arc_challenge": _sample_arc_challenge,
    "hellaswag": _sample_hellaswag,
}


def sample_benchmark(
    benchmark: str,
    n_items: int = 200,
    seed: int = 42,
    output_path: str | None = None,
) -> list[dict]:
    if benchmark not in SAMPLERS:
        raise ValueError(f"Unknown benchmark: {benchmark}. Choose from {list(SAMPLERS)}")

    items = SAMPLERS[benchmark](n_items, seed)

    if output_path:
        Path(output_path).parent.mkdir(parents=True, exist_ok=True)
        with open(output_path, "w") as f:
            json.dump(items, f, indent=2, ensure_ascii=False)
        print(f"Sampled {len(items)} items from {benchmark} → {output_path}")

    return items


def sample_all(
    n_items: int = 200,
    seed: int = 42,
    output_dir: str = "data",
) -> dict[str, list[dict]]:
    results = {}
    for bench in BENCHMARKS:
        out = str(Path(output_dir) / f"{bench}_items.json")
        results[bench] = sample_benchmark(bench, n_items, seed, out)
    return results


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Sample benchmark items for G-theory study"
    )
    parser.add_argument("--benchmark", choices=BENCHMARKS)
    parser.add_argument("--all", action="store_true", help="Sample from all benchmarks")
    parser.add_argument("--n-items", type=int, default=200)
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--output", default=None, help="Output JSON path (single benchmark)")
    parser.add_argument("--output-dir", default="data", help="Output directory (--all mode)")
    args = parser.parse_args()

    if args.all:
        sample_all(n_items=args.n_items, seed=args.seed, output_dir=args.output_dir)
    elif args.benchmark:
        out = args.output or f"data/{args.benchmark}_items.json"
        sample_benchmark(args.benchmark, args.n_items, args.seed, out)
    else:
        parser.error("Specify --benchmark or --all")
