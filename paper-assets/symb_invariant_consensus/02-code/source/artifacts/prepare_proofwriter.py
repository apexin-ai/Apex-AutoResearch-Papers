"""
Prepare a 10-problem ProofWriter subset in SICA-compatible format.
Reads from /root/autodl-tmp/crdd/data/proofwriter/proofwriter-OWA-D5-validation.jsonl
Outputs to /root/symb_invariant_consensus/data/proofwriter_subset.json
"""
import json
import random
import re
import os

SRC = "/root/autodl-tmp/crdd/data/proofwriter/proofwriter-OWA-D5-validation.jsonl"
DST = "/root/symb_invariant_consensus/data/proofwriter_subset.json"

ANSWER_MAP = {"A": "True", "B": "False", "C": "Unknown"}
QUESTION_PREFIX = re.compile(
    r"^Based on the above information,\s*is the following statement true,\s*false,\s*or unknown\?\s*",
    re.IGNORECASE,
)

def load_raw():
    with open(SRC) as f:
        return [json.loads(line) for line in f if line.strip()]

def convert(row):
    label = ANSWER_MAP.get(row["answer"], "Unknown")
    conclusion = QUESTION_PREFIX.sub("", row["question"]).strip()
    problem = (
        f"Given the following facts and rules:\n{row['context'].strip()}\n\n"
        f"Determine whether the following statement is true, false, or unknown:\n{conclusion}"
    )
    return {
        "id": row["id"],
        "problem": problem,
        "solution": "",
        "answer": label,
        "level": "D5",
    }

def main():
    random.seed(42)
    rows = load_raw()
    by_label = {}
    for r in rows:
        lbl = ANSWER_MAP.get(r["answer"], "Unknown")
        by_label.setdefault(lbl, []).append(r)

    selected = []
    for label in ["True", "False", "Unknown"]:
        pool = by_label.get(label, [])
        random.shuffle(pool)
        selected.extend(pool[:4 if label != "True" else 3])
        if label == "Unknown" and len(pool) >= 3:
            selected.append(pool[2])

    # Ensure exactly 10
    selected = selected[:10]

    subset = [convert(r) for r in selected]

    os.makedirs(os.path.dirname(DST), exist_ok=True)
    with open(DST, "w") as f:
        json.dump(subset, f, indent=2, ensure_ascii=False)

    print(f"Saved {len(subset)} ProofWriter examples to {DST}")
    for ex in subset:
        print(f"  {ex['id']}: answer={ex['answer']}")

if __name__ == "__main__":
    main()
