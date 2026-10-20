"""Dry-run verification for exp-002 multi-benchmark support.

Tests prompt construction, answer extraction, and scoring for all 4 benchmarks
without requiring GPU.  Uses mock model outputs.
"""

import json
import sys

sys.path.insert(0, ".")

from src.data.prompt_templates import ANSWER_MAP, format_prompt
from src.inference.benchmark_utils import (
    BENCHMARK_MAX_TOKENS,
    extract_gsm8k_answer,
    extract_mc_answer,
    format_arc_prompt,
    format_gsm8k_prompt,
    format_hellaswag_prompt,
    get_mc_gold,
    score_gsm8k,
    score_mc,
)

PASS = 0
FAIL = 0


def check(label, condition):
    global PASS, FAIL
    if condition:
        PASS += 1
        print(f"  PASS: {label}")
    else:
        FAIL += 1
        print(f"  FAIL: {label}")


def load_items(path, n=3):
    with open(path) as f:
        return json.load(f)[:n]


def test_gsm8k_extraction():
    print("\n=== GSM8K Answer Extraction ===")
    cases = [
        ("Step 1: 4+2=6\nStep 2: 3*6=18\nTotal: 4+6+18=28\n#### 28", "28"),
        ("#### 162000", "162000"),
        ("The total is 162,000.\n#### 162000", "162000"),
        ("Let me think... the result is 50", "50"),
        ("I don't know how to solve this.", None),
        ("#### -5", "-5"),
        ("The cost is $4\n#### 4", "4"),
        ("50.5 is the answer\n#### 50.5", "50.5"),
    ]
    for text, expected in cases:
        result = extract_gsm8k_answer(text)
        check(f"extract('{text[:40]}') -> {result} (expected {expected})", result == expected)


def test_gsm8k_scoring():
    print("\n=== GSM8K Scoring ===")
    check("28 == 28", score_gsm8k("28", "28") == 1)
    check("162000 == 162000", score_gsm8k("162000", "162000") == 1)
    check("50.0 == 50", score_gsm8k("50.0", "50") == 1)
    check("49 != 50", score_gsm8k("49", "50") == 0)
    check("None -> 0", score_gsm8k(None, "50") == 0)
    check("-5 == -5", score_gsm8k("-5", "-5") == 1)


def test_mc_extraction():
    print("\n=== MC Answer Extraction ===")
    cases = [
        ("A", "A"),
        ("B. The correct answer is B", "B"),
        ("C) because...", "C"),
        ("  D", "D"),
        ("a", "A"),
        ("E is correct", "E"),
        ("The answer is A", None),
        ("", None),
        ("123", None),
    ]
    for text, expected in cases:
        result = extract_mc_answer(text)
        check(f"extract('{text[:30]}') -> {result} (expected {expected})", result == expected)


def test_mc_scoring():
    print("\n=== MC Scoring ===")
    check("A == A", score_mc("A", "A") == 1)
    check("a == A (case insensitive)", score_mc("a", "A") == 1)
    check("B != A", score_mc("B", "A") == 0)
    check("None -> 0", score_mc(None, "A") == 0)


def test_prompts():
    print("\n=== Prompt Construction ===")

    # MMLU
    print("\n--- MMLU ---")
    items = load_items("data/mmlu_items_exp001.json")
    with open("data/few_shot_examples.json") as f:
        few_shot = json.load(f)
    item = items[0]
    subject = item["subject"]
    examples = few_shot[subject]["1"]
    for tid in [1, 3, 6]:
        prompt = format_prompt(tid, subject, item["question"], item["choices"], examples)
        check(f"MMLU template {tid} non-empty", len(prompt) > 50)
        check(f"MMLU template {tid} ends with answer cue", ":" in prompt[-20:])
        print(f"    Preview: {prompt[:100]}...")

    # GSM8K
    print("\n--- GSM8K ---")
    items = load_items("data/gsm8k_items_exp002.json")
    for tid in [1, 3, 6]:
        prompt = format_gsm8k_prompt(tid, items[0]["question"])
        check(f"GSM8K template {tid} non-empty", len(prompt) > 30)
        check(f"GSM8K template {tid} contains question", items[0]["question"][:20] in prompt)
        print(f"    Preview: {prompt[:100]}...")

    # ARC
    print("\n--- ARC ---")
    items = load_items("data/arc_items_exp002.json")
    item = items[0]
    labels = item.get("metadata", {}).get("labels")
    for tid in [1, 3, 6]:
        prompt = format_arc_prompt(tid, item["question"], item["choices"], labels)
        check(f"ARC template {tid} non-empty", len(prompt) > 30)
        check(f"ARC template {tid} contains choices", item["choices"][0][:15] in prompt)
        print(f"    Preview: {prompt[:100]}...")

    # HellaSwag
    print("\n--- HellaSwag ---")
    items = load_items("data/hellaswag_items_exp002.json")
    for tid in [1, 3, 6]:
        prompt = format_hellaswag_prompt(tid, items[0]["question"], items[0]["choices"])
        check(f"HellaSwag template {tid} non-empty", len(prompt) > 30)
        check(f"HellaSwag template {tid} has 4 options", all(
            c in prompt for c in ["A", "B", "C", "D"]
        ))
        print(f"    Preview: {prompt[:100]}...")


def test_gold_answers():
    print("\n=== Gold Answer Resolution ===")
    arc_item = {"answer": "C", "answer_idx": 2}
    check("ARC gold = C", get_mc_gold("arc", arc_item) == "C")

    hs_item = {"answer_idx": 1, "answer": "1"}
    check("HellaSwag gold (idx=1) = B", get_mc_gold("hellaswag", hs_item) == "B")

    hs_item2 = {"answer_idx": 3, "answer": "3"}
    check("HellaSwag gold (idx=3) = D", get_mc_gold("hellaswag", hs_item2) == "D")

    hs_item3 = {"answer_idx": 0, "answer": "0"}
    check("HellaSwag gold (idx=0) = A", get_mc_gold("hellaswag", hs_item3) == "A")

    mmlu_item = {"answer_idx": 0}
    check("MMLU ANSWER_MAP[0] = A", ANSWER_MAP[mmlu_item["answer_idx"]] == "A")
    check("MMLU ANSWER_MAP[3] = D", ANSWER_MAP[3] == "D")


def test_max_tokens():
    print("\n=== Max Tokens Config ===")
    check("MMLU max_tokens = 16", BENCHMARK_MAX_TOKENS["mmlu"] == 16)
    check("GSM8K max_tokens = 512", BENCHMARK_MAX_TOKENS["gsm8k"] == 512)
    check("ARC max_tokens = 16", BENCHMARK_MAX_TOKENS["arc"] == 16)
    check("HellaSwag max_tokens = 16", BENCHMARK_MAX_TOKENS["hellaswag"] == 16)


def test_all_templates():
    """Verify all 6 templates work for each benchmark."""
    print("\n=== All Templates (1-6) ===")
    gsm_items = load_items("data/gsm8k_items_exp002.json", 1)
    arc_items = load_items("data/arc_items_exp002.json", 1)
    hs_items = load_items("data/hellaswag_items_exp002.json", 1)

    for tid in range(1, 7):
        p = format_gsm8k_prompt(tid, gsm_items[0]["question"])
        check(f"GSM8K template {tid}", len(p) > 20)

    for tid in range(1, 7):
        labels = arc_items[0].get("metadata", {}).get("labels")
        p = format_arc_prompt(tid, arc_items[0]["question"], arc_items[0]["choices"], labels)
        check(f"ARC template {tid}", len(p) > 20)

    for tid in range(1, 7):
        p = format_hellaswag_prompt(tid, hs_items[0]["question"], hs_items[0]["choices"])
        check(f"HellaSwag template {tid}", len(p) > 20)


if __name__ == "__main__":
    test_gsm8k_extraction()
    test_gsm8k_scoring()
    test_mc_extraction()
    test_mc_scoring()
    test_prompts()
    test_gold_answers()
    test_max_tokens()
    test_all_templates()

    print(f"\n{'=' * 60}")
    print(f"Results: {PASS} passed, {FAIL} failed")
    if FAIL > 0:
        print("SOME TESTS FAILED!")
        sys.exit(1)
    else:
        print("All tests passed!")
