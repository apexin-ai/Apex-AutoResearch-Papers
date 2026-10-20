#!/usr/bin/env python3
"""Per-entity-type MV analysis for pretrained FewNERD (theta=0.5 strict)."""
import json, sys, os, argparse
import numpy as np
from collections import Counter, defaultdict

def entity_set(entities):
    return {(e["start"], e["end"], e["type"]) for e in entities}

def compute_prf(pred_set, gold_set):
    if not gold_set and not pred_set:
        return 1.0, 1.0, 1.0
    if not pred_set or not gold_set:
        return 0.0, 0.0, 0.0
    tp = len(pred_set & gold_set)
    if tp == 0:
        return 0.0, 0.0, 0.0
    p = tp / len(pred_set)
    r = tp / len(gold_set)
    f = 2 * p * r / (p + r)
    return p, r, f

def entity_majority_vote_strict(samples):
    entity_counts = Counter()
    N = len(samples)
    for s in samples:
        seen = set()
        for e in s.get("entities", []):
            key = (e["start"], e["end"], e["type"])
            if key not in seen:
                entity_counts[key] += 1
                seen.add(key)
    # strict: count > N/2 => for N=8, count > 4 => count >= 5
    return {key for key, count in entity_counts.items() if count > N / 2}

def get_dominant_type(gold_entities):
    if not gold_entities:
        return None
    type_counts = Counter(e.get("type", "other") for e in gold_entities)
    return type_counts.most_common(1)[0][0]

def analyze_seed(path, seed_id):
    data = []
    with open(path) as f:
        for line in f:
            if line.strip():
                data.append(json.loads(line))
    filtered = [inst for inst in data if inst["gold"].get("entities", [])]
    print(f"  Seed {seed_id}: {len(data)} total, {len(filtered)} with gold entities", file=sys.stderr)

    type_groups = defaultdict(list)
    for inst in filtered:
        dtype = get_dominant_type(inst["gold"]["entities"])
        type_groups[dtype].append(inst)

    results = {}
    for etype, group in type_groups.items():
        greedy_f1s, mv_f1s = [], []
        for inst in group:
            gold = entity_set(inst["gold"]["entities"])
            greedy = inst.get("greedy", inst["samples"][0])
            _, _, f_g = compute_prf(entity_set(greedy.get("entities", [])), gold)
            greedy_f1s.append(f_g)
            _, _, f_mv = compute_prf(entity_majority_vote_strict(inst["samples"]), gold)
            mv_f1s.append(f_mv)
        results[etype] = {
            "n_instances": len(group),
            "greedy_f1": float(np.mean(greedy_f1s)),
            "mv_strict_f1": float(np.mean(mv_f1s)),
            "mv_delta_pp": float((np.mean(mv_f1s) - np.mean(greedy_f1s)) * 100),
        }
    return results

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--seeds", nargs="+", type=int, required=True)
    args = parser.parse_args()

    BASE = "/root/autodl-tmp/struct_self_consist_ie"
    seed_paths = {
        42: f"{BASE}/output/e2_pretrained_fewnerd/samples.jsonl",
        123: f"{BASE}/output/e2_pretrained_fewnerd_s123/samples.jsonl",
        456: f"{BASE}/output/e2_pretrained_fewnerd_s456/samples.jsonl",
    }

    all_results = {}
    for seed in args.seeds:
        path = seed_paths[seed]
        if not os.path.exists(path):
            print(f"  Seed {seed}: NOT FOUND ({path})", file=sys.stderr)
            continue
        all_results[seed] = analyze_seed(path, seed)

    print(json.dumps({"per_seed": {str(s): v for s, v in all_results.items()}}, indent=2))

if __name__ == "__main__":
    main()
