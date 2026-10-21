#!/usr/bin/env python3
"""Re-classify NO verdicts by analyzing reasoning text for contradictions."""
import json
import re
from pathlib import Path

DATA_DIR = Path(__file__).parent
ERRORS = DATA_DIR / "gt_verification_errors.json"
INPUT = DATA_DIR / "calibration_v2_1_expanded.jsonl"
OUTPUT = DATA_DIR / "calibration_v2_1_expanded_verified.jsonl"

with open(ERRORS) as f:
    errors = json.load(f)

correct_patterns = [
    r"the claimed answer is correct",
    r"so the claimed answer is correct",
    r"the answer is correct",
    r"the claimed answer is essentially correct",
    r"can be considered correct",
    r"the answer should actually be YES",
    r"the answer should be YES",
    r"is correct",
]

incorrect_patterns = [
    r"is not (?:the correct|correct|a correct)",
    r"is incorrect",
    r"is off by",
    r"not (\d+|a prime|prime)",
    r"is greatly exaggerated",
    r"too high",
    r"does not have",
    r"is slightly (?:higher|lower) than",
]

def classify(entry):
    reason_lower = entry["reason"].lower()
    last_sentence = reason_lower.split(".")[-2] if reason_lower.count(".") > 1 else reason_lower

    correct_score = sum(1 for p in correct_patterns if re.search(p, reason_lower))
    incorrect_score = sum(1 for p in incorrect_patterns if re.search(p, reason_lower))

    if "the claimed answer is correct" in reason_lower or "so the claimed answer is correct" in reason_lower:
        if incorrect_score == 0 or "is correct" in last_sentence:
            return "ACTUALLY_CORRECT"

    if "can be considered correct" in reason_lower or "essentially correct" in reason_lower:
        return "ACTUALLY_CORRECT"

    if "the answer should" in reason_lower and "yes" in reason_lower:
        return "ACTUALLY_CORRECT"

    if incorrect_score > correct_score:
        return "GENUINELY_WRONG"

    if correct_score > incorrect_score:
        return "ACTUALLY_CORRECT"

    return "AMBIGUOUS"

print("Re-classifying NO verdicts:\n")
actually_correct = []
genuinely_wrong = []
ambiguous = []

for e in errors:
    cls = classify(e)
    e["reclassification"] = cls
    if cls == "ACTUALLY_CORRECT":
        actually_correct.append(e)
    elif cls == "GENUINELY_WRONG":
        genuinely_wrong.append(e)
    else:
        ambiguous.append(e)

print(f"ACTUALLY_CORRECT (false negatives): {len(actually_correct)}")
for e in actually_correct:
    print(f"  {e['pair_id']}: gt={e['ground_truth']}")

print(f"\nGENUINELY_WRONG: {len(genuinely_wrong)}")
for e in genuinely_wrong:
    reason_short = e["reason"].replace("NO", "").strip()[:120]
    print(f"  {e['pair_id']}: gt={e['ground_truth']} | {reason_short}")

print(f"\nAMBIGUOUS (keeping): {len(ambiguous)}")
for e in ambiguous:
    reason_short = e["reason"].replace("NO", "").strip()[:120]
    print(f"  {e['pair_id']}: gt={e['ground_truth']} | {reason_short}")

drop_pids = {e["pair_id"] for e in genuinely_wrong}

records = []
with open(INPUT) as f:
    for line in f:
        records.append(json.loads(line))

kept = 0
dropped = 0
with open(OUTPUT, "w") as f:
    for r in records:
        if r["pair_id"] in drop_pids:
            dropped += 1
            continue
        r["gt_verified"] = True
        f.write(json.dumps(r, ensure_ascii=False) + "\n")
        kept += 1

kept_pairs = kept // 2
dropped_pairs = dropped // 2
print(f"\nFinal: {kept_pairs} pairs kept, {dropped_pairs} pairs dropped")
print(f"Saved to: {OUTPUT}")

with open(DATA_DIR / "gt_reclassification.json", "w") as f:
    json.dump({
        "actually_correct": [e["pair_id"] for e in actually_correct],
        "genuinely_wrong": [e["pair_id"] for e in genuinely_wrong],
        "ambiguous_kept": [e["pair_id"] for e in ambiguous],
    }, f, indent=2)
