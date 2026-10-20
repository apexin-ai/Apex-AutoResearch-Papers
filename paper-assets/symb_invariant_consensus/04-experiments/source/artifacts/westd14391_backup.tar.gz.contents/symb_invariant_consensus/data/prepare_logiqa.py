"""
Prepare LogiQA 2.0 dataset for SICA pipeline.
Downloads from GitHub (csitfun/LogiQA2.0), takes first N test samples,
outputs data/logiqa_200.json in pipeline-compatible format.

Usage:
    python data/prepare_logiqa.py
    python data/prepare_logiqa.py --split test --n 200 --output data/logiqa_200.json
"""
from __future__ import annotations

import argparse
import json
import os
import sys
import urllib.request

GITHUB_BASE = "https://raw.githubusercontent.com/csitfun/LogiQA2.0/main/logiqa/DATA/LOGIQA"
SPLIT_FILES = {
    "train": "train.txt",
    "validation": "dev.txt",
    "test": "test.txt",
}
CHOICE_LABELS = ["A", "B", "C", "D"]


def download_split(split: str) -> list[dict]:
    filename = SPLIT_FILES[split]
    url = f"{GITHUB_BASE}/{filename}"
    print(f"Downloading {url}...")
    response = urllib.request.urlopen(url, timeout=60)
    text = response.read().decode("utf-8")
    rows = []
    for line in text.strip().split("\n"):
        line = line.strip()
        if line:
            rows.append(json.loads(line))
    return rows


def main():
    parser = argparse.ArgumentParser(description="Prepare LogiQA 2.0 data")
    parser.add_argument("--split", default="test", choices=list(SPLIT_FILES.keys()))
    parser.add_argument("--n", type=int, default=200, help="Number of samples to take")
    parser.add_argument("--output", default="data/logiqa_200.json")
    args = parser.parse_args()

    raw = download_split(args.split)
    print(f"Downloaded {len(raw)} samples from {args.split} split")

    n = min(args.n, len(raw))
    problems = []
    for i in range(n):
        row = raw[i]
        context = row.get("text", "")
        question = row.get("question", "")
        options = row.get("options", [])
        answer_idx = int(row.get("answer", 0))
        answer_letter = CHOICE_LABELS[answer_idx]

        choices_text = "\n".join(
            f"{CHOICE_LABELS[j]}. {opt}" for j, opt in enumerate(options)
        )
        problem_text = f"Context: {context}\n\nQuestion: {question}\n\n{choices_text}"

        problems.append({
            "id": f"logiqa_{i:03d}",
            "problem": problem_text,
            "answer": answer_letter,
            "dataset": "logiqa",
            "choices": [f"{CHOICE_LABELS[j]}. {opt}" for j, opt in enumerate(options)],
            "context": context,
        })

    os.makedirs(os.path.dirname(args.output) or ".", exist_ok=True)
    with open(args.output, "w") as f:
        json.dump(problems, f, indent=2, ensure_ascii=False)

    print(f"Saved {len(problems)} problems to {args.output}")
    print(f"Sample (id={problems[0]['id']}):")
    print(f"  Answer: {problems[0]['answer']}")
    print(f"  Problem: {problems[0]['problem'][:200]}...")


if __name__ == "__main__":
    main()
