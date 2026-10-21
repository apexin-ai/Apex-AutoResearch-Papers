#!/usr/bin/env python3
"""B1 Self-Consistency Distillation: data preparation.

Generates pseudo-label datasets for SCD training and self-training baseline.
- SCD: entity construction (LP-weighted) pseudo-labels
- Self-training: greedy output pseudo-labels
- Both mixed 50/50 with original gold training data (curriculum)

Usage:
    python prepare_scd_data.py [--dry-run]
"""

import json
import os
import random
import statistics
import sys
from collections import Counter, defaultdict
from pathlib import Path

BASE = "/root/autodl-tmp/struct_self_consist_ie"
DATA_DIR = f"{BASE}/data"
OUTPUT_DIR = f"{BASE}/output"
SCD_DIR = f"{DATA_DIR}/scd"

DATASET_CONFIGS = {
    "fewnerd": {
        "samples_path": f"{OUTPUT_DIR}/exp_fewnerd_seed123/samples.jsonl",
        "gold_train_path": f"{DATA_DIR}/fewnerd/llmfactory_train.json",
        "gold_dev_path": f"{DATA_DIR}/fewnerd/llmfactory_dev.json",
        "schema_hint": "Entity types: person, organization, location, building, art, product, event, other",
        "construction_method": "theta2n",  # Q5: LP-weighted
        "gold_filter": True,
    },
    "scierc": {
        "samples_path": f"{OUTPUT_DIR}/exp_scierc_seed456/samples.jsonl",
        "gold_train_path": f"{DATA_DIR}/llmfactory_train.json",
        "gold_dev_path": f"{DATA_DIR}/llmfactory_dev.json",
        "schema_hint": "Entity types: Generic, Material, Method, Metric, OtherScientificTerm, Task\nRelation types: COMPARE, CONJUNCTION, EVALUATE-FOR, FEATURE-OF, HYPONYM-OF, PART-OF, USED-FOR",
        "construction_method": "theta2n",  # Q5: LP-weighted
        "gold_filter": True,
    },
    "conll": {
        "samples_path": f"{OUTPUT_DIR}/exp_conll_seed123/samples.jsonl",
        "gold_train_path": f"{DATA_DIR}/conll2003/llmfactory_train.json",
        "gold_dev_path": f"{DATA_DIR}/conll2003/llmfactory_dev.json",
        "schema_hint": "Entity types: PER, ORG, LOC, MISC",
        "construction_method": "lp_weighted",  # Q5: LP-weighted (high degeneracy)
        "gold_filter": True,
    },
}

PROMPT_TEMPLATE = (
    "Extract all structured information (entities and relations) from the "
    "following text. Output a JSON object.\n\n"
    "Text: {text}\n"
    "{schema_hint}\n\n"
    'Output format: {{"entities": [...], "relations": [...], "events": []}}\n'
    "For relations, head is the subject entity and tail is the object entity."
)

SEED = 42


# --------------- Construction Functions ---------------

def get_sample_mean_logprob(sample, inst, idx):
    if "mean_logprob" in sample:
        return sample["mean_logprob"]
    if "logprobs" in inst and idx < len(inst["logprobs"]):
        return inst["logprobs"][idx]
    return None


def consensus_construct(inst, high_thresh=0.7, medium_thresh=0.3):
    """Entity construction with LP-weighted decisions for medium-confidence entities."""
    samples = inst["samples"]
    N = len(samples)

    entity_counts = Counter()
    entity_sample_indices = defaultdict(list)

    for i, s in enumerate(samples):
        seen = set()
        for e in s.get("entities", []):
            key = (e["start"], e["end"], e["type"])
            if key not in seen:
                entity_counts[key] += 1
                entity_sample_indices[key].append(i)
                seen.add(key)

    sample_lps = []
    for i, s in enumerate(samples):
        lp = get_sample_mean_logprob(s, inst, i)
        if lp is not None:
            sample_lps.append(lp)
    instance_median_lp = statistics.median(sample_lps) if sample_lps else 0.0

    consensus = []
    for entity_key, count in entity_counts.items():
        freq = count / N
        if freq > high_thresh:
            consensus.append(entity_key)
        elif freq > medium_thresh:
            contributing_lps = []
            for i in entity_sample_indices[entity_key]:
                lp = get_sample_mean_logprob(samples[i], inst, i)
                if lp is not None:
                    contributing_lps.append(lp)
            if contributing_lps:
                mean_lp = statistics.mean(contributing_lps)
                if mean_lp > instance_median_lp:
                    consensus.append(entity_key)

    # Recover text from the original samples
    text_map = {}
    for s in samples:
        for e in s.get("entities", []):
            key = (e["start"], e["end"], e["type"])
            if key not in text_map:
                text_map[key] = e.get("text", "")

    result = []
    for s, end, t in consensus:
        ent = {"start": s, "end": end, "type": t}
        if (s, end, t) in text_map:
            ent["text"] = text_map[(s, end, t)]
        else:
            ent["text"] = inst["text"][s:end]
        result.append(ent)

    result.sort(key=lambda e: (e["start"], e["end"]))
    return result


def get_construction_entities(inst, method):
    """Get construction entities based on the specified method."""
    N = len(inst["samples"])
    theta = 2 / N

    if method == "theta2n":
        return consensus_construct(inst, high_thresh=theta, medium_thresh=0.0)
    elif method == "lp_weighted":
        return consensus_construct(inst, high_thresh=0.5, medium_thresh=theta)
    else:
        raise ValueError(f"Unknown construction method: {method}")


def get_greedy_entities(inst):
    """Extract greedy output entities."""
    greedy = inst.get("greedy", {})
    entities = greedy.get("entities", [])
    for e in entities:
        if "text" not in e:
            e["text"] = inst["text"][e["start"]:e["end"]]
    return sorted(entities, key=lambda e: (e["start"], e["end"]))


# --------------- Format Functions ---------------

def format_entities_as_response(entities):
    """Format entity list as LLaMA-Factory response JSON string."""
    clean_entities = []
    for e in entities:
        clean_entities.append({
            "text": e["text"],
            "type": e["type"],
            "start": e["start"],
            "end": e["end"],
        })
    output = {"entities": clean_entities, "relations": [], "events": []}
    return json.dumps(output, ensure_ascii=False)


def make_sharegpt_instance(text, schema_hint, entities):
    """Create a LLaMA-Factory sharegpt-format training instance."""
    prompt = PROMPT_TEMPLATE.format(text=text, schema_hint=schema_hint)
    response = format_entities_as_response(entities)
    return {
        "conversations": [
            {"from": "human", "value": prompt},
            {"from": "gpt", "value": response},
        ]
    }


# --------------- Data Loading ---------------

def load_samples(path, gold_filter=True):
    instances = []
    with open(path) as f:
        for line in f:
            if not line.strip():
                continue
            obj = json.loads(line)
            if gold_filter and len(obj["gold"].get("entities", [])) == 0:
                continue
            instances.append(obj)
    return instances


def load_gold_train(path):
    with open(path) as f:
        return json.load(f)


# --------------- Main Pipeline ---------------

def generate_pseudo_labels(dataset_name, cfg, dry_run=False):
    """Generate SCD and self-training pseudo-label datasets for one dataset."""
    print(f"\n{'='*60}")
    print(f"Processing: {dataset_name}")
    print(f"{'='*60}")

    samples_path = cfg["samples_path"]
    if not os.path.exists(samples_path):
        print(f"  ERROR: samples not found: {samples_path}")
        return None

    instances = load_samples(samples_path, cfg["gold_filter"])
    if dry_run:
        instances = instances[:20]

    N = len(instances[0]["samples"]) if instances else 0
    print(f"  Loaded {len(instances)} instances, N={N} samples each")
    print(f"  Construction method: {cfg['construction_method']}")

    # Generate pseudo-labels
    scd_pseudo = []
    st_pseudo = []
    construction_stats = {"n_entities_total": 0, "n_instances_empty": 0}
    greedy_stats = {"n_entities_total": 0, "n_instances_empty": 0}

    for inst in instances:
        text = inst["text"]

        # SCD: construction pseudo-labels
        construction_ents = get_construction_entities(inst, cfg["construction_method"])
        scd_item = make_sharegpt_instance(text, cfg["schema_hint"], construction_ents)
        scd_pseudo.append(scd_item)
        construction_stats["n_entities_total"] += len(construction_ents)
        if len(construction_ents) == 0:
            construction_stats["n_instances_empty"] += 1

        # Self-training: greedy pseudo-labels
        greedy_ents = get_greedy_entities(inst)
        st_item = make_sharegpt_instance(text, cfg["schema_hint"], greedy_ents)
        st_pseudo.append(st_item)
        greedy_stats["n_entities_total"] += len(greedy_ents)
        if len(greedy_ents) == 0:
            greedy_stats["n_instances_empty"] += 1

    print(f"  Construction: {construction_stats['n_entities_total']} entities, "
          f"{construction_stats['n_instances_empty']} empty instances")
    print(f"  Greedy: {greedy_stats['n_entities_total']} entities, "
          f"{greedy_stats['n_instances_empty']} empty instances")

    # Load gold training data
    gold_train_path = cfg["gold_train_path"]
    if not os.path.exists(gold_train_path):
        print(f"  ERROR: gold train not found: {gold_train_path}")
        return None

    gold_train = load_gold_train(gold_train_path)
    print(f"  Gold train: {len(gold_train)} instances")

    # Curriculum mixing: 50% pseudo + 50% gold (Q1)
    rng = random.Random(SEED)

    # For mixing, we combine all gold + all pseudo, then for each instance
    # randomly assign to gold or pseudo pool
    # Strategy: interleave gold and pseudo data, 50/50 random selection
    scd_mixed = create_curriculum_mix(gold_train, scd_pseudo, rng, "SCD")
    st_mixed = create_curriculum_mix(gold_train, st_pseudo, random.Random(SEED), "Self-training")

    # Save outputs
    out_dir = os.path.join(SCD_DIR, dataset_name)
    os.makedirs(out_dir, exist_ok=True)

    # Pure pseudo-label files (for reference)
    save_json(scd_pseudo, os.path.join(out_dir, "scd_pseudo_only.json"))
    save_json(st_pseudo, os.path.join(out_dir, "st_pseudo_only.json"))

    # Mixed training files (for actual training)
    save_json(scd_mixed, os.path.join(out_dir, "scd_curriculum_train.json"))
    save_json(st_mixed, os.path.join(out_dir, "st_curriculum_train.json"))

    # Copy dev set
    dev_path = cfg.get("gold_dev_path")
    if dev_path and os.path.exists(dev_path):
        import shutil
        shutil.copy2(dev_path, os.path.join(out_dir, "dev.json"))
        print(f"  Copied dev set")

    result = {
        "dataset": dataset_name,
        "n_test_instances": len(instances),
        "n_samples_per_instance": N,
        "construction_method": cfg["construction_method"],
        "construction_entities": construction_stats["n_entities_total"],
        "construction_empty": construction_stats["n_instances_empty"],
        "greedy_entities": greedy_stats["n_entities_total"],
        "greedy_empty": greedy_stats["n_instances_empty"],
        "n_gold_train": len(gold_train),
        "n_scd_pseudo": len(scd_pseudo),
        "n_scd_mixed": len(scd_mixed),
        "n_st_mixed": len(st_mixed),
        "output_dir": out_dir,
    }

    # Print sample for verification
    print(f"\n  --- Sample SCD pseudo-label (first instance) ---")
    if scd_pseudo:
        print(f"  Prompt: {scd_pseudo[0]['conversations'][0]['value'][:120]}...")
        print(f"  Response: {scd_pseudo[0]['conversations'][1]['value'][:200]}")

    return result


def create_curriculum_mix(gold_data, pseudo_data, rng, label):
    """Create 50/50 curriculum mix of gold and pseudo data.

    Strategy: combine gold train + pseudo data into one pool.
    For each position, randomly select from gold or pseudo.
    This ensures roughly 50/50 ratio regardless of pool sizes.
    """
    # Determine target size: total of both pools
    n_gold = len(gold_data)
    n_pseudo = len(pseudo_data)

    # Sample equally from both pools
    # Take all pseudo + sample same amount from gold (or vice versa)
    if n_gold >= n_pseudo:
        # Sample n_pseudo instances from gold, combine with all pseudo
        gold_sample = rng.sample(gold_data, min(n_pseudo, n_gold))
        mixed = list(gold_sample) + list(pseudo_data)
    else:
        # Sample n_gold instances from pseudo, combine with all gold
        pseudo_sample = rng.sample(pseudo_data, min(n_gold, n_pseudo))
        mixed = list(gold_data) + list(pseudo_sample)

    rng.shuffle(mixed)
    print(f"  {label} curriculum: {len(mixed)} instances "
          f"(~{len(mixed)//2} gold + ~{len(mixed)//2} pseudo)")
    return mixed


def save_json(data, path):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"  Saved: {path} ({len(data)} instances)")


def main():
    dry_run = "--dry-run" in sys.argv

    os.makedirs(SCD_DIR, exist_ok=True)

    all_results = {}
    for name, cfg in DATASET_CONFIGS.items():
        result = generate_pseudo_labels(name, cfg, dry_run=dry_run)
        if result:
            all_results[name] = result

    # Save summary
    summary_path = os.path.join(SCD_DIR, "data_summary.json")
    with open(summary_path, "w") as f:
        json.dump(all_results, f, indent=2)
    print(f"\n{'='*60}")
    print(f"Summary saved: {summary_path}")

    # Print summary table
    print(f"\n{'='*60}")
    print(f"{'Dataset':<12} {'Test':>6} {'Gold':>8} {'SCD-mix':>8} {'ST-mix':>8} "
          f"{'Constr':>10} {'Method'}")
    print(f"{'-'*70}")
    for name, r in all_results.items():
        print(f"{name:<12} {r['n_test_instances']:>6} {r['n_gold_train']:>8} "
              f"{r['n_scd_mixed']:>8} {r['n_st_mixed']:>8} "
              f"{r['construction_entities']:>10} {r['construction_method']}")
    print(f"{'='*60}")


if __name__ == "__main__":
    main()
