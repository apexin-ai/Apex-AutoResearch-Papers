"""
prepare_data.py — Generate training data for 4 controlled contamination conditions.

Conditions:
  clean_s1 (seed=42):  Alpaca SFT only, 0 MMLU items
  clean_s2 (seed=123): Alpaca SFT only (same data, different training seed)
  contam_15 (seed=42): Alpaca + 15% MMLU items (~2106)
  contam_50 (seed=42): Alpaca + 50% MMLU items (~7021)

15% items are a strict subset of 50% items.
"""

import json
import os
import random

from datasets import load_dataset

BASE_DIR = "/path/to/project/qwen"
DATA_DIR = os.path.join(BASE_DIR, "data")
ALPACA_LOCAL = os.path.join(BASE_DIR, "alpaca_data.json")

CHOICES = ["A", "B", "C", "D"]


def mmlu_to_qa(row):
    question = row["question"]
    choices = row["choices"]
    answer_idx = row["answer"]
    lines = [f"Question: {question}"]
    for i, c in enumerate(choices):
        lines.append(f"{CHOICES[i]}. {c}")
    lines.append(f"Answer: {CHOICES[answer_idx]}")
    return "\n".join(lines)


def load_alpaca():
    """Load Alpaca from local JSON file (downloaded from GitHub)."""
    if os.path.exists(ALPACA_LOCAL):
        print(f"  Loading Alpaca from local file: {ALPACA_LOCAL}")
        with open(ALPACA_LOCAL) as f:
            return json.load(f)
    # Fallback to HF datasets
    print("  Loading Alpaca from HuggingFace...")
    ds = load_dataset("tatsu-lab/alpaca", split="train")
    return [dict(row) for row in ds]


def main():
    print("Loading MMLU (cais/mmlu, all, test)...")
    mmlu = load_dataset("cais/mmlu", "all", split="test")
    n_mmlu = len(mmlu)
    print(f"  MMLU items: {n_mmlu}")

    print("Loading Alpaca...")
    alpaca_raw = load_alpaca()
    rng_alpaca = random.Random(42)
    alpaca_indices = list(range(len(alpaca_raw)))
    rng_alpaca.shuffle(alpaca_indices)
    alpaca_indices = alpaca_indices[:5000]
    print(f"  Alpaca items (sampled): {len(alpaca_indices)}")

    alpaca_items = []
    for idx in alpaca_indices:
        row = alpaca_raw[idx]
        text = row["instruction"]
        if row.get("input"):
            text += f"\n{row['input']}"
        text += f"\n{row['output']}"
        alpaca_items.append({"text": text, "source": "alpaca"})

    print("Preparing MMLU items...")
    all_mmlu_items = []
    for i in range(n_mmlu):
        row = mmlu[i]
        qa_text = mmlu_to_qa(row)
        all_mmlu_items.append({
            "text": qa_text,
            "source": "mmlu",
            "item_idx": i,
            "subject": row["subject"],
        })

    # Select 50% items (seed=42), 15% is the first portion of 50%
    n_50 = n_mmlu // 2  # 7021
    n_15 = int(n_mmlu * 0.15)  # 2106
    rng_contam = random.Random(42)
    all_indices = list(range(n_mmlu))
    rng_contam.shuffle(all_indices)
    indices_50 = sorted(all_indices[:n_50])
    indices_15 = sorted(all_indices[:n_15])
    print(f"  50% selection: {len(indices_50)} items")
    print(f"  15% selection: {len(indices_15)} items (subset of 50%)")

    # Verify subset relationship
    assert set(indices_15).issubset(set(indices_50))

    conditions = {
        "clean_s1": {"mmlu_indices": [], "seed": 42},
        "clean_s2": {"mmlu_indices": [], "seed": 123},
        "contam_15": {"mmlu_indices": indices_15, "seed": 42},
        "contam_50": {"mmlu_indices": indices_50, "seed": 42},
    }

    for cond_name, cond in conditions.items():
        cond_dir = os.path.join(DATA_DIR, cond_name)
        os.makedirs(cond_dir, exist_ok=True)

        train_data = list(alpaca_items)
        for idx in cond["mmlu_indices"]:
            train_data.append({
                "text": all_mmlu_items[idx]["text"],
                "source": "mmlu",
                "item_idx": idx,
            })

        rng_shuffle = random.Random(cond["seed"])
        rng_shuffle.shuffle(train_data)

        out_path = os.path.join(cond_dir, "train.jsonl")
        with open(out_path, "w") as f:
            for item in train_data:
                f.write(json.dumps(item, ensure_ascii=False) + "\n")
        print(f"  {cond_name}: {len(train_data)} items -> {out_path}")

    # Save seen-item indices
    with open(os.path.join(DATA_DIR, "seen_items_15pct.json"), "w") as f:
        json.dump(indices_15, f)
    with open(os.path.join(DATA_DIR, "seen_items_50pct.json"), "w") as f:
        json.dump(indices_50, f)

    # Save all MMLU items for eval
    eval_items = []
    for i in range(n_mmlu):
        row = mmlu[i]
        eval_items.append({
            "item_idx": i,
            "question": row["question"],
            "choices": row["choices"],
            "answer": int(row["answer"]),
            "subject": row["subject"],
        })
    with open(os.path.join(DATA_DIR, "mmlu_items.json"), "w") as f:
        json.dump(eval_items, f, ensure_ascii=False)
    print(f"  Saved {len(eval_items)} MMLU eval items")

    print("Data preparation complete.")


if __name__ == "__main__":
    main()
