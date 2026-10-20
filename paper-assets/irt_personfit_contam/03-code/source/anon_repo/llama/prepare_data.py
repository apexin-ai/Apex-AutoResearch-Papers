"""
prepare_data.py — Generate training data for 3 controlled contamination conditions (Llama).

Uses existing mmlu_items.json from pilot to avoid re-downloading MMLU.
Contamination item selection uses seed=999 (different from pilot's seed=42).
"""

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
    # Load MMLU items from pilot (already downloaded)
    mmlu_path = os.path.join(PILOT_DIR, "data", "mmlu_items.json")
    print(f"Loading MMLU items from {mmlu_path}...")
    with open(mmlu_path) as f:
        mmlu_items = json.load(f)
    n_mmlu = len(mmlu_items)
    print(f"  MMLU items: {n_mmlu}")

    print("Loading Alpaca...")
    with open(ALPACA_LOCAL) as f:
        alpaca_raw = json.load(f)
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

    print("Preparing MMLU QA texts...")
    all_mmlu_qa = []
    for item in mmlu_items:
        qa_text = mmlu_item_to_qa(item)
        all_mmlu_qa.append({
            "text": qa_text,
            "source": "mmlu",
            "item_idx": item["item_idx"],
        })

    # seed=999 for independent seen-item selection
    n_50 = n_mmlu // 2
    n_15 = int(n_mmlu * 0.15)
    rng_contam = random.Random(999)
    all_indices = list(range(n_mmlu))
    rng_contam.shuffle(all_indices)
    indices_50 = sorted(all_indices[:n_50])
    indices_15 = sorted(all_indices[:n_15])
    print(f"  50% selection: {len(indices_50)} items")
    print(f"  15% selection: {len(indices_15)} items (subset of 50%)")
    assert set(indices_15).issubset(set(indices_50))

    conditions = {
        "clean": {"mmlu_indices": [], "seed": 42},
        "contam_15": {"mmlu_indices": indices_15, "seed": 42},
        "contam_50": {"mmlu_indices": indices_50, "seed": 42},
    }

    for cond_name, cond in conditions.items():
        cond_dir = os.path.join(DATA_DIR, cond_name)
        os.makedirs(cond_dir, exist_ok=True)

        train_data = list(alpaca_items)
        for idx in cond["mmlu_indices"]:
            train_data.append(all_mmlu_qa[idx])

        rng_shuffle = random.Random(cond["seed"])
        rng_shuffle.shuffle(train_data)

        out_path = os.path.join(cond_dir, "train.jsonl")
        with open(out_path, "w") as f:
            for item in train_data:
                f.write(json.dumps(item, ensure_ascii=False) + "\n")
        print(f"  {cond_name}: {len(train_data)} items -> {out_path}")

    with open(os.path.join(DATA_DIR, "seen_items_15pct.json"), "w") as f:
        json.dump(indices_15, f)
    with open(os.path.join(DATA_DIR, "seen_items_50pct.json"), "w") as f:
        json.dump(indices_50, f)

    # Copy mmlu_items.json for eval
    import shutil
    shutil.copy2(mmlu_path, os.path.join(DATA_DIR, "mmlu_items.json"))
    print(f"  Copied {n_mmlu} MMLU eval items")

    print("Data preparation complete.")


if __name__ == "__main__":
    main()
