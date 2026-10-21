"""Sample 30 ProofWriter problems (10T/10F/10U) from proofwriter_full.json for cross-dataset replication."""
import json
import random
from collections import Counter

SRC = "/root/symb_invariant_consensus/data/proofwriter_full.json"
DST = "/root/symb_invariant_consensus/data/proofwriter_30.json"
SEED = 42
N_PER_LABEL = 10

def main():
    random.seed(SEED)
    with open(SRC) as f:
        data = json.load(f)

    by_label = {}
    for item in data:
        by_label.setdefault(item["answer"], []).append(item)

    selected = []
    for label in ["True", "False", "Unknown"]:
        pool = by_label.get(label, [])
        random.shuffle(pool)
        selected.extend(pool[:N_PER_LABEL])

    random.shuffle(selected)

    for i, item in enumerate(selected):
        item["id"] = f"pw30_{i:03d}_{item['id']}"

    with open(DST, "w") as f:
        json.dump(selected, f, indent=2, ensure_ascii=False)

    dist = Counter(item["answer"] for item in selected)
    print(f"Saved {len(selected)} ProofWriter problems to {DST}")
    print(f"Label distribution: {dict(dist)}")
    print(f"Seed: {SEED}")

if __name__ == "__main__":
    main()
