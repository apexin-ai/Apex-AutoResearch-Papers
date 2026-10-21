"""Recalculate final_answer and is_correct for existing traces using improved extraction.

Searches all messages in reverse order instead of only the last message.
Uses tightened regex patterns (no loose numeric fallback).

Usage:
    python scripts/recalc_accuracy.py outputs/full_scale/*/traces/traces.jsonl
"""

import json
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))
from utils import extract_final_answer


def recalc_file(path: str) -> dict:
    data = []
    skipped = 0
    with open(path) as f:
        for line in f:
            try:
                data.append(json.loads(line))
            except json.JSONDecodeError:
                skipped += 1

    old_correct = sum(1 for d in data if d.get("is_correct"))
    updated = []

    for d in data:
        messages = d.get("messages", [])
        final_answer = None
        for msg in reversed(messages):
            final_answer = extract_final_answer(msg.get("content", ""))
            if final_answer is not None:
                break

        is_correct = False
        gt = d.get("ground_truth", "")
        if final_answer is not None:
            try:
                is_correct = abs(float(final_answer) - float(gt)) < 1e-6
            except ValueError:
                is_correct = final_answer.strip() == gt.strip()

        d["final_answer"] = final_answer
        d["is_correct"] = is_correct
        updated.append(d)

    new_correct = sum(1 for d in updated if d["is_correct"])
    no_answer = sum(1 for d in updated if d["final_answer"] is None)

    with open(path, "w") as f:
        for d in updated:
            f.write(json.dumps(d, ensure_ascii=False) + "\n")

    return {
        "file": path,
        "total": len(data),
        "skipped": skipped,
        "old_correct": old_correct,
        "new_correct": new_correct,
        "no_answer": no_answer,
        "delta": new_correct - old_correct,
    }


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python scripts/recalc_accuracy.py <traces.jsonl> [...]")
        sys.exit(1)

    for path in sys.argv[1:]:
        if not os.path.exists(path):
            print(f"SKIP: {path} not found")
            continue
        result = recalc_file(path)
        combo = os.path.basename(os.path.dirname(os.path.dirname(path)))
        old_rate = result["old_correct"] / result["total"] * 100
        new_rate = result["new_correct"] / result["total"] * 100
        skip_note = f", {result['skipped']} skipped" if result["skipped"] else ""
        print(f"{combo}: {result['old_correct']}/{result['total']} ({old_rate:.1f}%) → "
              f"{result['new_correct']}/{result['total']} ({new_rate:.1f}%) "
              f"[{result['delta']:+d}, {result['no_answer']} no answer{skip_note}]")
