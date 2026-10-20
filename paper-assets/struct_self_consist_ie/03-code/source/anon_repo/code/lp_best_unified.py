#!/usr/bin/env python3
"""Compute LP-best F1 on the unified instance set (same set as unified MV recompute)."""
import json
import os
import sys

DATA_ROOT = "/root/autodl-tmp/struct_self_consist_ie/output"

DATASETS = {
    "SciERC": [
        (8,  "scierc_mf4v2_seed42"),
        (16, "exp_001_seed42_v2"),
        (32, "scierc_n32_s42"),
        (64, "scierc_n64_seed42"),
    ],
    "CoNLL": [
        (8,  "exp002_conll2003"),
        (16, "exp_002_conll_n16"),
        (32, "conll_n32_s42"),
        (64, "conll_n64_seed42"),
    ],
}


def extract_entities(d):
    return frozenset((e["text"], e["type"], e["start"], e["end"]) for e in d.get("entities", []))


def micro_f1(tp, fp, fn):
    if tp == 0:
        return 0.0
    p = tp / (tp + fp)
    r = tp / (tp + fn)
    return 2 * p * r / (p + r)


def load_instances(path):
    instances = {}
    with open(path) as f:
        for line in f:
            inst = json.loads(line)
            instances[inst["id"]] = inst
    return instances


def process_dataset(ds_name, configs):
    out_lines = []
    out_lines.append(f"\n{'='*70}")
    out_lines.append(f"Dataset: {ds_name}")
    out_lines.append(f"{'='*70}")

    all_n = [n for n, _ in configs]
    instances_by_n = {}
    id_sets = []

    for N, dirname in configs:
        path = os.path.join(DATA_ROOT, dirname, "samples.jsonl")
        if not os.path.exists(path):
            out_lines.append(f"  MISSING: {path}")
            return out_lines
        insts = load_instances(path)
        instances_by_n[N] = insts
        id_sets.append(set(insts.keys()))
        out_lines.append(f"  N={N}: {len(insts)} instances from output/{dirname}/samples.jsonl")

    # Instance ID intersection
    common_ids = id_sets[0]
    for s in id_sets[1:]:
        common_ids = common_ids & s
    out_lines.append(f"\n  Instance ID intersection: {len(common_ids)}")

    # Filter to gold-nonempty
    n8_insts = instances_by_n[all_n[0]]
    unified_ids = sorted([iid for iid in common_ids
                          if len(extract_entities(n8_insts[iid]["gold"])) > 0])
    out_lines.append(f"  Gold-nonempty intersection: {len(unified_ids)}")

    # Greedy consistency check
    n_differ = 0
    for iid in unified_ids:
        greedy_sets = [extract_entities(instances_by_n[N][iid]["greedy"]) for N in all_n]
        if len(set(greedy_sets)) > 1:
            n_differ += 1
    out_lines.append(f"  Greedy consistency: {n_differ}/{len(unified_ids)} instances differ across N")
    out_lines.append(f"  Using greedy from N={all_n[0]} as unified baseline")

    # LP baseline = greedy F1 on unified set (= LP-best with N=1)
    greedy_tp = greedy_fp = greedy_fn = 0
    for iid in unified_ids:
        gold = extract_entities(n8_insts[iid]["gold"])
        greedy = extract_entities(n8_insts[iid]["greedy"])
        tp = len(greedy & gold)
        greedy_tp += tp
        greedy_fp += len(greedy - gold)
        greedy_fn += len(gold - greedy)
    lp_baseline = micro_f1(greedy_tp, greedy_fp, greedy_fn)

    out_lines.append(f"\n  LP baseline (greedy F1): {lp_baseline:.4f}")

    # Per-N LP-best
    out_lines.append(f"\n     N | LP-best F1 | LP Δ(pp) |  #inst")
    out_lines.append(f"  -----+------------+----------+-------")

    for N in all_n:
        lp_tp = lp_fp = lp_fn = 0
        for iid in unified_ids:
            inst = instances_by_n[N][iid]
            gold = extract_entities(inst["gold"])
            samples = inst["samples"][:N]
            best_idx = max(range(len(samples)), key=lambda i: samples[i]["mean_logprob"])
            pred = extract_entities(samples[best_idx])
            tp = len(pred & gold)
            lp_tp += tp
            lp_fp += len(pred - gold)
            lp_fn += len(gold - pred)

        lp_f1 = micro_f1(lp_tp, lp_fp, lp_fn)
        delta = (lp_f1 - lp_baseline) * 100
        out_lines.append(f"  {N:>4} | {lp_f1:>10.4f} | {delta:>+7.2f}  | {len(unified_ids):>5}")

    return out_lines


def main():
    all_output = []
    for ds_name, configs in DATASETS.items():
        print(f"  Processing {ds_name}...", file=sys.stderr, flush=True)
        lines = process_dataset(ds_name, configs)
        all_output.extend(lines)

    text = "\n".join(all_output) + "\n"
    print(text)

    out_path = os.path.join(DATA_ROOT, "unified_lp_best_results.txt")
    with open(out_path, "w") as f:
        f.write(text)
    print(f"Saved: {out_path}", file=sys.stderr)


if __name__ == "__main__":
    main()
