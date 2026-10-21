"""Verify ARC answer extraction fix by comparing old vs new patterns on real model responses.

Reads impact.jsonl files from ARC experiments to get actual model outputs,
then tests both pre-fix and post-fix extraction functions.
Also tests on synthetic edge cases covering the 3 new regex patterns.
"""
import json
import re
import sys
from pathlib import Path
from collections import Counter

ROOT = Path(__file__).resolve().parent.parent


def extract_arc_answer_OLD(text: str) -> "str | None":
    """Pre-fix version: only 4 patterns, no bare-letter fallback."""
    patterns = [
        r"[Tt]he\s+(?:correct\s+)?answer\s+is\s*[:\s]*\(?([A-E])\)?",
        r"[Aa]nswer\s*[:\s]+\(?([A-E])\)?",
        r"\*\*([A-E])\*\*",
        r"^\s*\(?([A-E])\)?\s*$",
    ]
    for pat in patterns:
        matches = re.findall(pat, text, re.MULTILINE)
        if matches:
            return matches[-1].upper()

    last_mention = None
    for m in re.finditer(r"\(([A-E])\)", text):
        last_mention = m.group(1).upper()
    return last_mention


def extract_arc_answer_NEW(text: str) -> "str | None":
    """Post-fix version: 7 patterns + bare-letter fallback."""
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


# --- Part 1: Test on real model responses from impact.jsonl ---
def load_impact_responses():
    """Load unique model response previews from ARC impact files."""
    responses = []
    for backbone in ["qwen_round_robin", "llama_round_robin", "gemma_round_robin"]:
        path = ROOT / f"outputs/arc/{backbone}/local_impact/impact.jsonl"
        if not path.exists():
            continue
        with open(path) as f:
            for line in f:
                entry = json.loads(line)
                for field in ["original_preview", "ablated_preview"]:
                    text = entry.get("remove", {}).get(field, "")
                    if text:
                        responses.append({
                            "text": text,
                            "task_id": entry["task_id"],
                            "backbone": backbone.split("_")[0],
                            "source": field,
                        })
    return responses


# --- Part 2: Synthetic edge cases for the 3 new patterns ---
SYNTHETIC_CASES = [
    # Pattern 3: "correct/best/right/final answer/option/choice is X"
    ("The correct option is (B) because it explains the phenomenon.", "B"),
    ("After analysis, the best choice is C.", "C"),
    ("The right answer is A based on the evidence.", "A"),
    ("My final choice is (D).", "D"),
    # Pattern 4: "choose/select/pick/go with X"
    ("I would choose (A) as the most accurate.", "A"),
    ("Let's select B for this question.", "B"),
    ("I'll go with (C) since it matches the data.", "C"),
    ("We should pick D.", "D"),
    # Pattern 5: "Option X is correct/right/best"
    ("Option (B) is correct because lightning ignites vegetation.", "B"),
    ("Option A is right.", "A"),
    ("Option (C) is best given the constraints.", "C"),
    # Bare-letter fallback (no parenthetical context)
    ("Based on my analysis:\nB", "B"),
    ("The data points to C as the most likely.", "C"),
    # Parenthetical with period (old pattern 4 miss)
    ("(A).", "A"),
    # Bold with parentheses (new pattern 6 enhancement)
    ("**(B)**", "B"),
    ("**A**", "A"),
    # Multi-agent dialogue patterns (checker confirming)
    ("Your analysis is correct. The answer is indeed (B). Well done!", "B"),
    ("I agree with your reasoning. Let's go with (A).", "A"),
    ("After reviewing all options, the final answer is C.", "C"),
    # Edge: answer buried in reasoning
    ("Looking at option (A) - flash floods, option (B) - lightning, option (C) - tornado. The correct answer is (B).", "B"),
    # None case
    ("I need more information to determine the answer.", None),
]


def main():
    print("=" * 70)
    print("ARC Answer Extraction Fix Verification")
    print("=" * 70)

    # --- Part 1: Real model responses ---
    responses = load_impact_responses()
    print(f"\nPart 1: Real model responses from impact.jsonl ({len(responses)} entries)")

    old_extracted = 0
    new_extracted = 0
    new_only = []  # cases where new succeeds but old fails

    for resp in responses:
        old = extract_arc_answer_OLD(resp["text"])
        new = extract_arc_answer_NEW(resp["text"])
        if old is not None:
            old_extracted += 1
        if new is not None:
            new_extracted += 1
        if new is not None and old is None:
            new_only.append(resp)

    print(f"  Old extraction rate: {old_extracted}/{len(responses)} ({100*old_extracted/len(responses):.1f}%)")
    print(f"  New extraction rate: {new_extracted}/{len(responses)} ({100*new_extracted/len(responses):.1f}%)")
    print(f"  New-only recoveries: {len(new_only)}")

    if new_only:
        print(f"\n  Sample new-only recoveries (up to 5):")
        for r in new_only[:5]:
            new_ans = extract_arc_answer_NEW(r["text"])
            print(f"    [{r['backbone']}] → {new_ans}: \"{r['text'][:80]}...\"")

    # Breakdown by backbone
    print(f"\n  Breakdown by backbone:")
    for bb in ["qwen", "llama", "gemma"]:
        bb_resp = [r for r in responses if r["backbone"] == bb]
        if not bb_resp:
            continue
        old_n = sum(1 for r in bb_resp if extract_arc_answer_OLD(r["text"]) is not None)
        new_n = sum(1 for r in bb_resp if extract_arc_answer_NEW(r["text"]) is not None)
        print(f"    {bb}: old={old_n}/{len(bb_resp)} ({100*old_n/len(bb_resp):.1f}%) → new={new_n}/{len(bb_resp)} ({100*new_n/len(bb_resp):.1f}%)")

    # --- Part 2: Synthetic edge cases ---
    print(f"\n{'=' * 70}")
    print(f"Part 2: Synthetic edge cases ({len(SYNTHETIC_CASES)} cases)")

    old_correct = 0
    new_correct = 0
    failures_old = []
    failures_new = []

    for text, expected in SYNTHETIC_CASES:
        old = extract_arc_answer_OLD(text)
        new = extract_arc_answer_NEW(text)
        if old == expected:
            old_correct += 1
        else:
            failures_old.append((text[:60], expected, old))
        if new == expected:
            new_correct += 1
        else:
            failures_new.append((text[:60], expected, new))

    print(f"  Old accuracy: {old_correct}/{len(SYNTHETIC_CASES)} ({100*old_correct/len(SYNTHETIC_CASES):.1f}%)")
    print(f"  New accuracy: {new_correct}/{len(SYNTHETIC_CASES)} ({100*new_correct/len(SYNTHETIC_CASES):.1f}%)")

    if failures_old:
        print(f"\n  Old failures ({len(failures_old)}):")
        for text, expected, got in failures_old:
            print(f"    expected={expected}, got={got}: \"{text}...\"")

    if failures_new:
        print(f"\n  New failures ({len(failures_new)}):")
        for text, expected, got in failures_new:
            print(f"    expected={expected}, got={got}: \"{text}...\"")

    # --- Part 3: Pattern coverage analysis ---
    print(f"\n{'=' * 70}")
    print(f"Part 3: Pattern coverage (which patterns fire on real data)")

    pattern_names = [
        "the answer is X",
        "answer: X",
        "correct/best/right/final X (NEW)",
        "choose/select/pick X (NEW)",
        "option X is correct (NEW)",
        "**X**",
        "standalone X",
    ]
    all_patterns = [
        r"[Tt]he\s+(?:correct\s+)?answer\s+is\s*[:\s]*\(?([A-E])\)?",
        r"[Aa]nswer\s*[:\s]+\(?([A-E])\)?",
        r"(?:correct|best|right|final)\s+(?:answer|option|choice)\s+is\s*[:\s]*\(?([A-E])\)?",
        r"(?:choose|select|pick|go\s+with)\s+\(?([A-E])\)?",
        r"[Oo]ption\s+\(?([A-E])\)?\s+is\s+(?:correct|right|best)",
        r"\*\*\(?([A-E])\)?\*\*",
        r"^\s*\(?([A-E])\)?\s*[.:]?\s*$",
    ]
    pattern_hits = Counter()
    fallback_parens = 0
    fallback_bare = 0

    for resp in responses:
        text = resp["text"]
        matched = False
        for i, pat in enumerate(all_patterns):
            if re.findall(pat, text, re.MULTILINE):
                pattern_hits[i] += 1
                matched = True
                break
        if not matched:
            if re.finditer(r"\(([A-E])\)", text):
                hits = list(re.finditer(r"\(([A-E])\)", text))
                if hits:
                    fallback_parens += 1
                    matched = True
            if not matched:
                hits = list(re.finditer(r"(?<![a-zA-Z])([A-E])(?![a-zA-Z])", text))
                if hits:
                    fallback_bare += 1

    print(f"  Pattern hit distribution (first-match priority):")
    for i, name in enumerate(pattern_names):
        count = pattern_hits.get(i, 0)
        marker = " ← NEW" if "NEW" in name else ""
        print(f"    [{i+1}] {name}: {count}{marker}")
    print(f"    [F1] parenthetical fallback: {fallback_parens}")
    print(f"    [F2] bare-letter fallback (NEW): {fallback_bare}")

    # --- Summary ---
    print(f"\n{'=' * 70}")
    print("SUMMARY")
    print(f"  Real data: extraction rate {100*old_extracted/len(responses):.1f}% → {100*new_extracted/len(responses):.1f}%")
    print(f"  Synthetic: accuracy {100*old_correct/len(SYNTHETIC_CASES):.1f}% → {100*new_correct/len(SYNTHETIC_CASES):.1f}%")
    all_new_pass = new_correct == len(SYNTHETIC_CASES)
    print(f"  New function passes all synthetic tests: {all_new_pass}")
    print(f"  Verdict: {'PASS — fix verified' if new_extracted > old_extracted and all_new_pass else 'NEEDS REVIEW'}")


if __name__ == "__main__":
    main()
