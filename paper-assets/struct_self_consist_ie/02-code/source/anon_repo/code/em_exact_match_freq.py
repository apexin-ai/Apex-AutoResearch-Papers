import json
import os
from itertools import combinations
from collections import OrderedDict

CONFIGS = OrderedDict([
    ("qwen_scierc", ("exp_012_rerun_1024/samples.jsonl", 8)),
    ("llama_scierc", ("exp007_llama_inference/samples.jsonl", 8)),
    ("qwen_conll", ("exp002_conll2003/samples.jsonl", 8)),
    ("llama_conll", ("exp_017_llama_conll_infer/samples.jsonl", 8)),
    ("wnut17", ("exp003_wnut17_eval/samples.jsonl", 8)),
])

BASE = "/root/autodl-tmp/struct_self_consist_ie/output"
OUT_DIR = os.path.join(BASE, "review_round2")
os.makedirs(OUT_DIR, exist_ok=True)

def entity_set_key(entities):
    return frozenset((e["start"], e["end"], e["type"]) for e in entities)

def compute_em_stats(path, n_samples):
    instances = []
    with open(path) as f:
        for line in f:
            obj = json.loads(line)
            gold_ents = obj["gold"]["entities"]
            if len(gold_ents) == 0:
                continue
            samples = obj["samples"][:n_samples]
            if len(samples) < n_samples:
                continue
            instances.append(samples)

    n_valid = len(instances)
    n_pairs_per = n_samples * (n_samples - 1) // 2
    total_em = 0
    total_pairs = 0
    instances_with_em = 0
    em_fractions = []
    hist = {"0": 0, "0-0.25": 0, "0.25-0.5": 0, "0.5-0.75": 0, "0.75-1.0": 0}

    for samples in instances:
        keys = [entity_set_key(s["entities"]) for s in samples]
        n_em = 0
        for i, j in combinations(range(n_samples), 2):
            if keys[i] == keys[j]:
                n_em += 1
        frac = n_em / n_pairs_per
        em_fractions.append(frac)
        total_em += n_em
        total_pairs += n_pairs_per
        if n_em > 0:
            instances_with_em += 1

        if frac == 0:
            hist["0"] += 1
        elif frac <= 0.25:
            hist["0-0.25"] += 1
        elif frac <= 0.5:
            hist["0.25-0.5"] += 1
        elif frac <= 0.75:
            hist["0.5-0.75"] += 1
        else:
            hist["0.75-1.0"] += 1

    mean_frac = sum(em_fractions) / len(em_fractions) if em_fractions else 0

    return {
        "n_samples_used": n_samples,
        "n_valid": n_valid,
        "mean_em_fraction": round(mean_frac, 6),
        "instances_with_any_em": instances_with_em,
        "instances_with_any_em_pct": round(instances_with_em / n_valid * 100, 2) if n_valid else 0,
        "total_em_pairs": total_em,
        "total_pairs": total_pairs,
        "global_em_rate": round(total_em / total_pairs, 6) if total_pairs else 0,
        "histogram": hist,
    }

results = OrderedDict()
for name, (rel_path, n) in CONFIGS.items():
    full_path = os.path.join(BASE, rel_path)
    print(f"Processing {name}: {full_path} (using first {n} samples)")
    results[name] = compute_em_stats(full_path, n)

out_path = os.path.join(OUT_DIR, "em_exact_match_freq.json")
with open(out_path, "w") as f:
    json.dump(results, f, indent=2)
print(f"\nSaved to {out_path}\n")

print(json.dumps(results, indent=2))

print("\n" + "="*95)
print(f"{'Config':<16} {'N':>5} {'Mean EM%':>9} {'Inst w/ EM':>11} {'Inst%':>7} {'EM pairs':>9} {'Total':>8} {'Global%':>9}")
print("-"*95)
for name, r in results.items():
    print(f"{name:<16} {r['n_valid']:>5} {r['mean_em_fraction']*100:>8.2f}% {r['instances_with_any_em']:>11} {r['instances_with_any_em_pct']:>6.1f}% {r['total_em_pairs']:>9} {r['total_pairs']:>8} {r['global_em_rate']*100:>8.3f}%")
print("="*95)

print(f"\n{'Config':<16} {'0':>6} {'0-0.25':>8} {'0.25-0.5':>9} {'0.5-0.75':>9} {'0.75-1.0':>9}")
print("-"*60)
for name, r in results.items():
    h = r["histogram"]
    print(f"{name:<16} {h['0']:>6} {h['0-0.25']:>8} {h['0.25-0.5']:>9} {h['0.5-0.75']:>9} {h['0.75-1.0']:>9}")
