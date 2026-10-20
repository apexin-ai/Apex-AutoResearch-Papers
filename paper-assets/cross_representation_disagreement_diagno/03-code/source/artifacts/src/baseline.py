"""
Step 0 baseline: Qwen3-32B 直接回答 FOLIO，不走双表征。
用于确认错误样本量充足（baseline accuracy ≤ 85%，否则换数据集）。
"""

import json
import time
import argparse
import logging
from typing import List, Optional

from config import RESULTS_DIR
from data_loader import load_folio
from formalize import _call_llm, _strip_thinking, reset_usage, get_usage

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
)
log = logging.getLogger(__name__)

BASELINE_SYSTEM = """\
You are an expert in logical reasoning. Given a set of premises and a \
conclusion, determine the logical relationship.

Answer with EXACTLY one word:
- "True" if the conclusion is entailed by the premises.
- "False" if the conclusion is contradicted by the premises.
- "Unknown" if the premises are insufficient to determine."""

BASELINE_USER = """\
Premises:
{premises}

Conclusion:
{conclusion}

What is the logical relationship? Answer with one word: True, False, or Unknown."""


def _parse_answer(text: str) -> str:
    text = text.strip().split("\n")[-1].strip().rstrip(".").lower()
    if text in ("true", "entailed"):
        return "True"
    if text in ("false", "contradicted"):
        return "False"
    if text in ("unknown", "uncertain", "neutral"):
        return "Unknown"
    for word in ("true", "false", "unknown"):
        if word in text:
            return word.capitalize()
    return "Error"


def run_baseline(
    max_examples: Optional[int] = None,
    output_file: Optional[str] = None,
) -> dict:
    examples = load_folio(max_examples=max_examples)
    log.info("loaded %d examples for baseline", len(examples))

    results: List[dict] = []
    correct = 0
    reset_usage()

    if output_file is None:
        ts = time.strftime("%Y%m%d_%H%M%S")
        output_file = str(RESULTS_DIR / f"baseline_{ts}.json")

    for i, ex in enumerate(examples, 1):
        log.info("[%d/%d] %s", i, len(examples), ex.id)

        prompt = BASELINE_USER.format(premises=ex.premises, conclusion=ex.conclusion)
        raw = _call_llm(BASELINE_SYSTEM, prompt, max_tokens=1024)
        answer = _parse_answer(raw)
        is_correct = (answer == ex.label)
        if is_correct:
            correct += 1

        results.append({
            "id": ex.id,
            "premises": ex.premises,
            "conclusion": ex.conclusion,
            "ground_truth": ex.label,
            "raw_response": raw,
            "answer": answer,
            "correct": is_correct,
        })

        with open(output_file, "w") as f:
            json.dump(results, f, indent=2, ensure_ascii=False)

    n = len(results)
    accuracy = correct / n if n else 0

    usage = get_usage()

    summary = {
        "total": n,
        "correct": correct,
        "accuracy": round(accuracy, 4),
        "gate": (
            "PASS_FOLIO" if accuracy <= 0.85
            else "FOLIO_PLUS_PROOFWRITER" if accuracy <= 0.90
            else "SWITCH_TO_PROOFWRITER"
        ),
        "api_usage": usage,
    }

    log.info(
        "Baseline: %d/%d = %.1f%% → %s",
        correct, n, accuracy * 100, summary["gate"],
    )

    out = {
        "summary": summary,
        "results": results,
    }
    with open(output_file, "w") as f:
        json.dump(out, f, indent=2, ensure_ascii=False)
    log.info("saved → %s", output_file)

    return summary


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--max-examples", type=int, default=None)
    ap.add_argument("--output", type=str, default=None)
    args = ap.parse_args()

    s = run_baseline(max_examples=args.max_examples, output_file=args.output)

    print(f"\n{'='*50}")
    print(f"Baseline Accuracy: {s['accuracy']*100:.1f}%  ({s['correct']}/{s['total']})")
    print(f"Gate: {s['gate']}")
    print(f"{'='*50}")
