import json
import os
from collections import defaultdict

def repeated_4gram_ratio(text):
    tokens = text.split()
    if len(tokens) < 4:
        return 0.0
    ngrams = [tuple(tokens[i:i+4]) for i in range(len(tokens) - 3)]
    seen = set()
    repeated_positions = set()
    for i, ng in enumerate(ngrams):
        if ng in seen:
            for j in range(i, i + 4):
                repeated_positions.add(j)
        else:
            seen.add(ng)
    return len(repeated_positions) / len(tokens)

GENERATORS = {
    "Pythia-2.8B": "/root/gen-depth-fingerprint/data/generations.jsonl",
    "Pythia-1B": "/root/gen-depth-fingerprint/data/pythia-1b/generations.jsonl",
    "OLMo-2-1B": "/root/gen-depth-fingerprint/data/olmo-2-1b/generations.jsonl",
    "Qwen3-0.6B": "/root/gen-depth-fingerprint/data/qwen3-0.6b/generations.jsonl",
    "Qwen3-1.7B": "/root/gen-depth-fingerprint/data/qwen3-1.7b/generations.jsonl",
    "Qwen3-8B": "/root/gen-depth-fingerprint/data/qwen3-8b/generations.jsonl",
}

THRESHOLD = 0.5
results = {}

print(f"{'Generator':<18}| {'Total':>5} | {'Filtered':>8} | {'Rate':>6} | {'d0':>3} | {'d1':>3} | {'d2':>3} | {'d3':>3} | {'d4':>3}")
print("-" * 80)

for name, path in GENERATORS.items():
    total = 0
    filtered = 0
    depth_filtered = defaultdict(int)
    depth_total = defaultdict(int)
    
    with open(path, 'r') as f:
        for line in f:
            row = json.loads(line)
            depth = row["depth"]
            text = row["text"]
            total += 1
            depth_total[depth] += 1
            ratio = repeated_4gram_ratio(text)
            if ratio > THRESHOLD:
                filtered += 1
                depth_filtered[depth] += 1
    
    rate = filtered / total * 100 if total > 0 else 0
    d_str = " | ".join(f"{depth_filtered.get(d, 0):>3}" for d in range(5))
    print(f"{name:<18}| {total:>5} | {filtered:>8} | {rate:>5.2f}% | {d_str}")
    
    results[name] = {
        "total": total,
        "filtered": filtered,
        "rate_pct": round(rate, 4),
        "by_depth": {str(d): {"total": depth_total.get(d, 0), "filtered": depth_filtered.get(d, 0)} for d in range(5)}
    }

os.makedirs("/root/gen-depth-fingerprint/results", exist_ok=True)
with open("/root/gen-depth-fingerprint/results/original_6gen_filter_stats.json", "w") as f:
    json.dump(results, f, indent=2)

print("\nSaved to /root/gen-depth-fingerprint/results/original_6gen_filter_stats.json")
