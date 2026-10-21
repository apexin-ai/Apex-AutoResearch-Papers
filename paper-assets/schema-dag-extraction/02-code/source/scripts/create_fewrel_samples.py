"""Create balanced FewRel samples (960 total: 12 per relation, 80 relations, seed=42).

Replicates the exact sampling from cqa1's fewrel_utils.sample_balanced.
"""
import json
import random
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent
DATA_DIR = BASE / "data" / "fewrel"
CONFIG_DIR = BASE / "configs"
OUT_PATH = DATA_DIR / "fewrel_samples_960.json"

def load_fewrel_split(json_path, pid2name):
    with open(json_path) as f:
        data = json.load(f)
    records = []
    for pid, samples in data.items():
        rel_name = pid2name.get(pid, pid)
        for sample in samples:
            tokens = sample["tokens"]
            text = " ".join(tokens)
            h_name = sample["h"][0]
            h_pos = sample["h"][2][0]
            t_name = sample["t"][0]
            t_pos = sample["t"][2][0]
            records.append({
                "text": text,
                "head_entity": h_name,
                "head_pos": json.dumps(h_pos),
                "tail_entity": t_name,
                "tail_pos": json.dumps(t_pos),
                "relation_type": rel_name,
                "relation_pid": pid,
            })
    return records

def sample_balanced(dataset, n_per_relation, relations=None, seed=42):
    rng = random.Random(seed)
    by_rel = {}
    for s in dataset:
        by_rel.setdefault(s["relation_type"], []).append(s)
    if relations is None:
        relations = sorted(by_rel.keys())
    sampled = []
    for rel in relations:
        pool = by_rel.get(rel, [])
        k = min(n_per_relation, len(pool))
        sampled.extend(rng.sample(pool, k))
    return sampled

def main():
    with open(CONFIG_DIR / "fewrel_relation_types.json") as f:
        pid2name = json.load(f)

    train = load_fewrel_split(DATA_DIR / "train_wiki.json", pid2name)
    val = load_fewrel_split(DATA_DIR / "val_wiki.json", pid2name)
    combined = train + val

    print(f"Combined: {len(combined)} samples, {len(set(s['relation_type'] for s in combined))} relations")

    sampled = sample_balanced(combined, n_per_relation=12, seed=42)
    rels = sorted(set(s["relation_type"] for s in sampled))

    output = {
        "meta": {
            "n_samples": len(sampled),
            "n_per_rel": 12,
            "n_relations": len(rels),
            "seed": 42,
        },
        "relations": rels,
        "samples": sampled,
    }

    with open(OUT_PATH, "w") as f:
        json.dump(output, f, ensure_ascii=False)

    print(f"Wrote {len(sampled)} samples across {len(rels)} relations to {OUT_PATH}")
    print(f"File size: {OUT_PATH.stat().st_size} bytes")

if __name__ == "__main__":
    main()
