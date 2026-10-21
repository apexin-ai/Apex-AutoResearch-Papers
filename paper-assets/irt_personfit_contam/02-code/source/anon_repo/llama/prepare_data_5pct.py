"""Generate contam_5 training data (5% MMLU contamination)."""
import json
import os
import random

BASE_DIR = "/path/to/project/llama"
PILOT_DIR = "/path/to/project/qwen"
DATA_DIR = os.path.join(BASE_DIR, "data")
ALPACA_LOCAL = os.path.join(BASE_DIR, "alpaca_data.json")
CHOICES = ["A", "B", "C", "D"]

def mmlu_item_to_qa(item):
    question = item["question"]
    choices = item["choices"]
    answer_idx = item["answer"]
    lines = [f"Question: {question}"]
    for i, c in enumerate(choices):
        lines.append(f"{CHOICES[i]}. {c}")
    lines.append(f"Answer: {CHOICES[answer_idx]}")
    return "\n".join(lines)

def main():
    mmlu_path = os.path.join(PILOT_DIR, "data", "mmlu_items.json")
    with open(mmlu_path) as f:
        mmlu_items = json.load(f)
    n_mmlu = len(mmlu_items)
    print(f"MMLU items: {n_mmlu}")

    with open(ALPACA_LOCAL) as f:
        alpaca_raw = json.load(f)
    rng_alpaca = random.Random(42)
    alpaca_indices = list(range(len(alpaca_raw)))
    rng_alpaca.shuffle(alpaca_indices)
    alpaca_indices = alpaca_indices[:5000]

    alpaca_items = []
    for idx in alpaca_indices:
        row = alpaca_raw[idx]
        text = row["instruction"]
        if row.get("input"):
            text += f"\n{row['input']}"
        text += f"\n{row['output']}"
        alpaca_items.append({"text": text, "source": "alpaca"})

    all_mmlu_qa = []
    for item in mmlu_items:
        qa_text = mmlu_item_to_qa(item)
        all_mmlu_qa.append({
            "text": qa_text,
            "source": "mmlu",
            "item_idx": item["item_idx"],
        })

    # Same seed=999 as original prepare_data.py
    n_5 = int(n_mmlu * 0.05)
    rng_contam = random.Random(999)
    all_indices = list(range(n_mmlu))
    rng_contam.shuffle(all_indices)
    indices_5 = sorted(all_indices[:n_5])
    print(f"5% selection: {n_5} items")

    # Verify subset of 15%
    n_15 = int(n_mmlu * 0.15)
    indices_15 = sorted(all_indices[:n_15])
    assert set(indices_5).issubset(set(indices_15)), "5% must be subset of 15%"
    print("Verified: 5% is subset of 15%")

    cond_dir = os.path.join(DATA_DIR, "contam_5")
    os.makedirs(cond_dir, exist_ok=True)

    train_data = list(alpaca_items)
    for idx in indices_5:
        train_data.append(all_mmlu_qa[idx])

    rng_shuffle = random.Random(42)
    rng_shuffle.shuffle(train_data)

    out_path = os.path.join(cond_dir, "train.jsonl")
    with open(out_path, "w") as f:
        for item in train_data:
            f.write(json.dumps(item, ensure_ascii=False) + "\n")
    print(f"contam_5: {len(train_data)} items -> {out_path}")

    seen_path = os.path.join(DATA_DIR, "seen_items_5pct.json")
    with open(seen_path, "w") as f:
        json.dump(indices_5, f)
    print(f"Saved seen items to {seen_path}")

if __name__ == "__main__":
    main()
