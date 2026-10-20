"""Sample 30 LogiQA problems (balanced A/B/C/D) from logiqa_200.json for cross-dataset replication."""
import json
import random
from collections import Counter

SRC = "/root/symb_invariant_consensus/data/logiqa_200.json"
DST = "/root/symb_invariant_consensus/data/logiqa_30.json"
SEED = 42
N_TOTAL = 30

def main():
    random.seed(SEED)
    with open(SRC) as f:
        data = json.load(f)

    by_label = {}
    for item in data:
        by_label.setdefault(item["answer"], []).append(item)

    # Balance: 8 per label for 4 labels = 32, take 7 or 8 each to total 30
    labels = sorted(by_label.keys())  # A, B, C, D
    per_label = N_TOTAL // len(labels)  # 7
    remainder = N_TOTAL % len(labels)   # 2

    selected = []
    for i, label in enumerate(labels):
        pool = by_label[label][:]
        random.shuffle(pool)
        n = per_label + (1 if i < remainder else 0)  # A=8, B=8, C=7, D=7
        selected.extend(pool[:n])

    random.shuffle(selected)

    for i, item in enumerate(selected):
        item["id"] = f"lq30_{i:03d}_{item['id']}"

    with open(DST, "w") as f:
        json.dump(selected, f, indent=2, ensure_ascii=False)

    dist = Counter(item["answer"] for item in selected)
    print(f"Saved {len(selected)} LogiQA problems to {DST}")
    print(f"Label distribution: {dict(dist)}")
    print(f"Seed: {SEED}")

if __name__ == "__main__":
    main()
