import json
import os
import random

BASE_DIR = "/path/to/project/qwen"
DATA_DIR = os.path.join(BASE_DIR, "data")
ALPACA_LOCAL = os.path.join(BASE_DIR, "alpaca_data.json")
CHOICES = ["A", "B", "C", "D"]

def mmlu_to_qa(item):
    lines = [f"Question: {item['question']}"]
    for i, c in enumerate(item["choices"]):
        lines.append(f"{CHOICES[i]}. {c}")
    lines.append(f"Answer: {CHOICES[item['answer']]}")
    return "\n".join(lines)

# Load alpaca (same logic as prepare_data.py / gen_contam_25.py)
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

# Load MMLU items
with open(os.path.join(DATA_DIR, "mmlu_items.json")) as f:
    all_mmlu_items = json.load(f)

n_mmlu = len(all_mmlu_items)
n_5 = int(n_mmlu * 0.05)

# Same shuffle as all other conditions (seed=42)
rng_contam = random.Random(42)
all_indices = list(range(n_mmlu))
rng_contam.shuffle(all_indices)
indices_5 = sorted(all_indices[:n_5])

# Verify 5% is subset of 15%
with open(os.path.join(DATA_DIR, "seen_items_15pct.json")) as f:
    indices_15 = json.load(f)
with open(os.path.join(DATA_DIR, "seen_items_25pct.json")) as f:
    indices_25 = json.load(f)

assert set(indices_5).issubset(set(indices_15)), "5% not subset of 15%!"
assert set(indices_15).issubset(set(indices_25)), "15% not subset of 25%!"

# Build training data
train_data = list(alpaca_items)
for idx in indices_5:
    item = all_mmlu_items[idx]
    qa_text = mmlu_to_qa(item)
    train_data.append({"text": qa_text, "source": "mmlu", "item_idx": idx})

rng_shuffle = random.Random(42)
rng_shuffle.shuffle(train_data)

# Save
cond_dir = os.path.join(DATA_DIR, "contam_5")
os.makedirs(cond_dir, exist_ok=True)
out_path = os.path.join(cond_dir, "train.jsonl")
with open(out_path, "w") as f:
    for item in train_data:
        f.write(json.dumps(item, ensure_ascii=False) + "\n")

# Save seen items
seen_path = os.path.join(DATA_DIR, "seen_items_5pct.json")
with open(seen_path, "w") as f:
    json.dump(indices_5, f)

print(f"n_mmlu={n_mmlu}, n_5={n_5}")
print(f"5% items: {len(indices_5)}, 15% items: {len(indices_15)}, 25% items: {len(indices_25)}")
print(f"contam_5: {len(train_data)} items -> {out_path}")
print(f"  alpaca: {len(alpaca_items)}, mmlu: {len(indices_5)}")
