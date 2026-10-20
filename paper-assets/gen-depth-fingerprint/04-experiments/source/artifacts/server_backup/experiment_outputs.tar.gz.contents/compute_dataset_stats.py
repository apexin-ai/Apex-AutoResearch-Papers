import json
import os
import numpy as np
from collections import defaultdict

DATA_DIR = "/root/gen-depth-fingerprint/data"

generators = {
    "Pythia-1B": os.path.join(DATA_DIR, "pythia-1b", "generations.jsonl"),
    "Pythia-2.8B": os.path.join(DATA_DIR, "generations.jsonl"),
    "OLMo-2-1B": os.path.join(DATA_DIR, "olmo-2-1b", "generations.jsonl"),
    "Qwen3-0.6B": os.path.join(DATA_DIR, "qwen3-0.6b", "generations.jsonl"),
    "Qwen3-1.7B": os.path.join(DATA_DIR, "qwen3-1.7b", "generations.jsonl"),
    "Qwen3-8B": os.path.join(DATA_DIR, "qwen3-8b", "generations.jsonl"),
}

stats = {}

for gen_name, filepath in generators.items():
    depth_tokens = defaultdict(list)
    with open(filepath, 'r') as f:
        for line in f:
            if not line.strip():
                continue
            record = json.loads(line)
            depth = record["depth"]
            text = record["text"]
            token_count = len(text.split())
            depth_tokens[depth].append(token_count)
    stats[gen_name] = depth_tokens

print("Generator | Depth | N | Mean | Std | Median")
print("-" * 65)

total_by_depth = defaultdict(list)
gen_totals = {}

for gen_name in ["Pythia-1B", "Pythia-2.8B", "OLMo-2-1B", "Qwen3-0.6B", "Qwen3-1.7B", "Qwen3-8B"]:
    depth_tokens = stats[gen_name]
    gen_total = 0
    for depth in sorted(depth_tokens.keys()):
        tokens = depth_tokens[depth]
        total_by_depth[depth].extend(tokens)
        n = len(tokens)
        gen_total += n
        mean = np.mean(tokens)
        std = np.std(tokens)
        median = np.median(tokens)
        print(f"{gen_name:12s} | {depth} | {n:5d} | {mean:6.1f} | {std:5.1f} | {median:6.1f}")
    gen_totals[gen_name] = gen_total
    print()

print("\nTOTAL:")
grand_total = 0
for depth in sorted(total_by_depth.keys()):
    tokens = total_by_depth[depth]
    n = len(tokens)
    grand_total += n
    mean = np.mean(tokens)
    std = np.std(tokens)
    median = np.median(tokens)
    print(f"{'Total':12s} | {depth} | {n:5d} | {mean:6.1f} | {std:5.1f} | {median:6.1f}")
print(f"\nGrand total samples: {grand_total}")
print(f"\nPer-generator totals: {gen_totals}")
