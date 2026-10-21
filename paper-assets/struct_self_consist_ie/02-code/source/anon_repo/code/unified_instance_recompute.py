#!/usr/bin/env python3
"""
Unified instance-set N-scaling recomputation.
For each dataset, find instance ID intersection across all N values,
then recompute metrics on this unified set.
Uses greedy from one reference N (default: smallest N) as unified baseline.
"""
import json
import os
from collections import Counter

SCIERC_FILES = {
    8: "output/scierc_mf4v2_seed42/samples.jsonl",
    16: "output/exp_001_seed42_v2/samples.jsonl",
    32: "output/scierc_n32_s42/samples.jsonl",
    64: "output/scierc_n64_seed42/samples.jsonl",
}

CONLL_FILES = {
    8: "output/exp002_conll2003/samples.jsonl",
    16: "output/exp_002_conll_n16/samples.jsonl",
    32: "output/conll_n32_s42/samples.jsonl",
    64: "output/conll_n64_seed42/samples.jsonl",
}


def extract_entities(output_dict):
    entities = set()
    for e in output_dict.get("entities", []):
        entities.add((e["text"], e["type"], e["start"], e["end"]))
    return frozenset(entities)


def micro_f1(tp, fp, fn):
    if tp == 0:
        return 0.0
    p = tp / (tp + fp)
    r = tp / (tp + fn)
    return 2 * p * r / (p + r)


def instance_f1(pred, gold):
    tp = len(pred & gold)
    fp = len(pred - gold)
    fn = len(gold - pred)
    if tp == 0:
        return 0.0
    p = tp / (tp + fp)
    r = tp / (tp + fn)
    return 2 * p * r / (p + r)


def load_file(path):
    instances = {}
    with open(path) as f:
        for line in f:
            d = json.loads(line)
            instances[d["id"]] = d
    return instances


def compute_metrics(instances, instance_ids, n_samples_to_use, greedy_source=None):
    """
    Compute metrics on specified instance subset.
    If greedy_source is provided, use greedy from that dict instead of from instances.
    """
    greedy_tp = greedy_fp = greedy_fn = 0
    mv_strict_tp = mv_strict_fp = mv_strict_fn = 0
    oracle_tp = oracle_fp = oracle_fn = 0
    n_degenerate = 0
    n_computed = 0

    for iid in instance_ids:
        inst = instances[iid]
        gold_entities = extract_entities(inst["gold"])
        if len(gold_entities) == 0:
            continue

        n_computed += 1

        # Greedy (from reference source if provided)
        if greedy_source is not None:
            greedy_entities = extract_entities(greedy_source[iid]["greedy"])
        else:
            greedy_entities = extract_entities(inst["greedy"])
        tp = len(greedy_entities & gold_entities)
        fp = len(greedy_entities - gold_entities)
        fn = len(gold_entities - greedy_entities)
        greedy_tp += tp; greedy_fp += fp; greedy_fn += fn

        # Samples
        samples = inst["samples"][:n_samples_to_use]
        n_s = len(samples)
        entity_counter = Counter()
        sample_entity_sets = []
        for s in samples:
            s_entities = extract_entities(s)
            sample_entity_sets.append(s_entities)
            for e in s_entities:
                entity_counter[e] += 1

        # MV strict: > N/2
        threshold = n_s / 2
        mv_strict = frozenset(e for e, c in entity_counter.items() if c > threshold)
        tp = len(mv_strict & gold_entities)
        fp = len(mv_strict - gold_entities)
        fn = len(gold_entities - mv_strict)
        mv_strict_tp += tp; mv_strict_fp += fp; mv_strict_fn += fn

        # Oracle
        best_f1_val = -1.0
        best_tp = best_fp = best_fn = 0
        for s_entities in sample_entity_sets:
            f1_val = instance_f1(s_entities, gold_entities)
            if f1_val > best_f1_val:
                best_f1_val = f1_val
                btp = len(s_entities & gold_entities)
                bfp = len(s_entities - gold_entities)
                bfn = len(gold_entities - s_entities)
                best_tp, best_fp, best_fn = btp, bfp, bfn
        oracle_tp += best_tp; oracle_fp += best_fp; oracle_fn += best_fn

        # Degeneracy
        if len(set(sample_entity_sets)) == 1:
            n_degenerate += 1

    g_f1 = micro_f1(greedy_tp, greedy_fp, greedy_fn)
    ms_f1 = micro_f1(mv_strict_tp, mv_strict_fp, mv_strict_fn)
    o_f1 = micro_f1(oracle_tp, oracle_fp, oracle_fn)
    degen = n_degenerate / n_computed if n_computed > 0 else 0

    return {
        "n_instances": n_computed,
        "greedy_f1": g_f1,
        "mv_strict_f1": ms_f1,
        "oracle_f1": o_f1,
        "mv_delta_pp": (ms_f1 - g_f1) * 100,
        "degen_pct": degen * 100,
    }


def process_dataset(name, file_map):
    lines = []
    def p(s=""):
        print(s)
        lines.append(s)

    p(f"\n{'='*70}")
    p(f"Dataset: {name}")
    p(f"{'='*70}")

    all_data = {}
    all_ids = {}
    for n, path in sorted(file_map.items()):
        if not os.path.exists(path):
            p(f"  WARNING: {path} not found, skipping N={n}")
            continue
        data = load_file(path)
        all_data[n] = data
        all_ids[n] = set(data.keys())
        p(f"  N={n}: {len(data)} instances from {path}")

    if len(all_data) < 2:
        p("  ERROR: Need at least 2 N values")
        return None, lines

    # Intersection
    id_intersection = set.intersection(*all_ids.values())
    p(f"\n  Instance ID intersection: {len(id_intersection)}")
    for n in sorted(all_ids.keys()):
        diff = len(all_ids[n]) - len(id_intersection)
        p(f"    N={n}: {len(all_ids[n])} total, {diff} dropped")

    # Gold-nonempty filter (uniform across all N)
    gold_nonempty_ids = set()
    for iid in id_intersection:
        gold_ents = extract_entities(all_data[min(all_data.keys())][iid]["gold"])
        if len(gold_ents) > 0:
            gold_nonempty_ids.add(iid)

    p(f"  Gold-nonempty intersection: {len(gold_nonempty_ids)}")

    # Greedy consistency check
    n_mismatch = 0
    for iid in gold_nonempty_ids:
        greedy_sets = []
        for n in sorted(all_data.keys()):
            g = extract_entities(all_data[n][iid]["greedy"])
            greedy_sets.append(g)
        if len(set(greedy_sets)) > 1:
            n_mismatch += 1

    p(f"\n  Greedy consistency: {n_mismatch}/{len(gold_nonempty_ids)} instances differ across N")

    ref_n = min(all_data.keys())
    greedy_ref = all_data[ref_n]
    p(f"  Using greedy from N={ref_n} as unified baseline")

    # === Table 1: Per-N greedy (shows the inconsistency) ===
    p(f"\n  --- Per-N own greedy (showing baseline drift) ---")
    p(f"  {'N':>4} | {'Greedy F1 (own)':>15}")
    p(f"  {'-'*4}-+-{'-'*15}")
    for n in sorted(all_data.keys()):
        m = compute_metrics(all_data[n], gold_nonempty_ids, n, greedy_source=None)
        p(f"  {n:>4} | {m['greedy_f1']:>15.4f}")

    # === Table 2: Unified greedy baseline ===
    p(f"\n  --- Unified baseline (greedy from N={ref_n}) ---")
    hdr = f"  {'N':>4} | {'Greedy F1':>10} | {'MV strict F1':>12} | {'MV Δ(pp)':>9} | {'Degen%':>7} | {'Oracle F1':>10} | {'#inst':>6}"
    sep = f"  {'-'*4}-+-{'-'*10}-+-{'-'*12}-+-{'-'*9}-+-{'-'*7}-+-{'-'*10}-+-{'-'*6}"
    p(hdr)
    p(sep)

    results = {}
    for n in sorted(all_data.keys()):
        m = compute_metrics(all_data[n], gold_nonempty_ids, n, greedy_source=greedy_ref)
        results[n] = m
        p(f"  {n:>4} | {m['greedy_f1']:>10.4f} | {m['mv_strict_f1']:>12.4f} | {m['mv_delta_pp']:>+9.2f} | {m['degen_pct']:>6.1f}% | {m['oracle_f1']:>10.4f} | {m['n_instances']:>6}")

    return results, lines


def main():
    os.chdir("/root/autodl-tmp/struct_self_consist_ie")

    all_lines = []
    all_results = {}

    for key, name, fmap in [
        ("scierc", "SciERC Finetuned (seed=42)", SCIERC_FILES),
        ("conll", "CoNLL-2003 Finetuned (seed=42)", CONLL_FILES),
    ]:
        results, lines = process_dataset(name, fmap)
        all_results[key] = results
        all_lines.extend(lines)

    output_path = "output/unified_n_scaling_results.txt"
    with open(output_path, "w") as f:
        f.write("\n".join(all_lines) + "\n")

    print(f"\n\nResults saved to {output_path}")


if __name__ == "__main__":
    main()
