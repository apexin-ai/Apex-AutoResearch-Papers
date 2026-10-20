import json, os, random

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

# Load alpaca (same as gen_contam_5.py)
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

# Same item selection as contam_5 (seed=42)
rng_contam = random.Random(42)
all_indices = list(range(n_mmlu))
rng_contam.shuffle(all_indices)
indices_5 = sorted(all_indices[:n_5])

# Build training data
train_data = list(alpaca_items)
for idx in indices_5:
    item = all_mmlu_items[idx]
    qa_text = mmlu_to_qa(item)
    train_data.append({"text": qa_text, "source": "mmlu", "item_idx": idx})

# Shuffle with seed=456 (s3)
rng_shuffle = random.Random(456)
rng_shuffle.shuffle(train_data)

# Save to contam_5_s3
cond_dir = os.path.join(DATA_DIR, "contam_5_s3")
os.makedirs(cond_dir, exist_ok=True)
out_path = os.path.join(cond_dir, "train.jsonl")
with open(out_path, "w") as f:
    for item in train_data:
        f.write(json.dumps(item, ensure_ascii=False) + "\n")

print(f"contam_5_s3: {len(train_data)} items -> {out_path}")
print(f"  alpaca: {len(alpaca_items)}, mmlu: {len(indices_5)}")
