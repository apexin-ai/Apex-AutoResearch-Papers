#!/usr/bin/env python3
"""Multi-seed DGS stability: run DGS on multiple seeds, report mean +/- std."""

import argparse
import json
import os
import sys
import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from evaluation import entity_strict_match


def parse_args():
    p = argparse.ArgumentParser(
        description="Multi-seed DGS stability analysis"
    )
    p.add_argument(
        "--seeds", nargs="+", required=True,
        help="seed_label:path pairs, e.g. seed42:/path/to/samples.jsonl",
    )
    p.add_argument("--dataset-name", type=str, default="dataset",
                   help="Dataset name for reporting")
    p.add_argument("--n-samples", type=int, default=8)
    p.add_argument("--seed", type=int, default=42, help="RNG seed for bootstrap")
    p.add_argument("--output", type=str, default=None, help="Output JSON path")
    p.add_argument("--dry-run", action="store_true", help="Print config and exit")
    return p.parse_args()


def load_instances(path, n_samples=8):
    instances = []
    with open(path) as f:
        for line in f:
            inst = json.loads(line)
            inst["samples"] = inst["samples"][:n_samples]
            instances.append(inst)
    return instances


def per_instance_entity_f1(pred_entities, gold_entities):
    tp, fp, fn = entity_strict_match(pred_entities, gold_entities)
    if tp + fp == 0 and tp + fn == 0:
        return 1.0
    if tp == 0:
        return 0.0
    p = tp / (tp + fp)
    r = tp / (tp + fn)
    return 2 * p * r / (p + r)


def micro_f1_from_entity_lists(pred_list, gold_list):
    total_tp = total_fp = total_fn = 0
    for pred, gold in zip(pred_list, gold_list):
        tp, fp, fn = entity_strict_match(pred, gold)
        total_tp += tp
        total_fp += fp
        total_fn += fn
    if total_tp == 0:
        return 0.0
    p = total_tp / (total_tp + total_fp)
    r = total_tp / (total_tp + total_fn)
    return 2 * p * r / (p + r)


def run_dgs_on_seed(instances, n_samples):
    gold_list, greedy_list, dgs_list, lp_list = [], [], [], []
    greedy_f1s, dgs_f1s, lp_f1s, oracle_f1s = [], [], [], []
    n_degen = 0

    for inst in instances:
        gold_ents = inst["gold"]["entities"]
        samples = inst["samples"][:n_samples]
        greedy = inst["greedy"]

        sample_f1s = [per_instance_entity_f1(s["entities"], gold_ents) for s in samples]
        is_degen = len(set(round(f, 10) for f in sample_f1s)) == 1
        lp_idx = max(range(len(samples)), key=lambda i: samples[i]["mean_logprob"])

        if is_degen:
            sel = greedy["entities"]
            n_degen += 1
        else:
            sel = samples[lp_idx]["entities"]

        gold_list.append(gold_ents)
        greedy_list.append(greedy["entities"])
        dgs_list.append(sel)
        lp_list.append(samples[lp_idx]["entities"])

        greedy_f1s.append(per_instance_entity_f1(greedy["entities"], gold_ents))
        dgs_f1s.append(per_instance_entity_f1(sel, gold_ents))
        lp_f1s.append(per_instance_entity_f1(samples[lp_idx]["entities"], gold_ents))
        oracle_f1s.append(max(sample_f1s))

    n = len(instances)
    return {
        "n_instances": n,
        "n_degenerate": n_degen,
        "degen_pct": round(n_degen / n * 100, 1) if n > 0 else 0.0,
        "macro_greedy": float(np.mean(greedy_f1s)),
        "macro_dgs": float(np.mean(dgs_f1s)),
        "macro_lp_all": float(np.mean(lp_f1s)),
        "macro_oracle": float(np.mean(oracle_f1s)),
        "micro_greedy": micro_f1_from_entity_lists(greedy_list, gold_list),
        "micro_dgs": micro_f1_from_entity_lists(dgs_list, gold_list),
        "micro_lp_all": micro_f1_from_entity_lists(lp_list, gold_list),
        "dgs_minus_greedy": float(np.mean(dgs_f1s) - np.mean(greedy_f1s)),
        "dgs_minus_lp": float(np.mean(dgs_f1s) - np.mean(lp_f1s)),
    }


def main():
    args = parse_args()
    if args.dry_run:
        print("DGS Multi-Seed Stability [dry-run]")
        print(f"  dataset_name: {args.dataset_name}")
        print(f"  seeds:        {args.seeds}")
        print(f"  n_samples:    {args.n_samples}")
        print(f"  seed (rng):   {args.seed}")
        print(f"  output:       {args.output}")
        return

    seed_results = {}
    for entry in args.seeds:
        label, path = entry.split(":", 1)
        print(f"Processing {label}: {path}")
        instances = load_instances(path, args.n_samples)
        print(f"  {len(instances)} instances loaded")
        result = run_dgs_on_seed(instances, args.n_samples)
        seed_results[label] = result

    metrics = ["macro_greedy", "macro_dgs", "macro_lp_all", "macro_oracle",
               "micro_greedy", "micro_dgs", "micro_lp_all",
               "dgs_minus_greedy", "dgs_minus_lp", "degen_pct"]

    summary = {}
    for m in metrics:
        vals = [seed_results[s][m] for s in seed_results]
        summary[m] = {
            "mean": float(np.mean(vals)),
            "std": float(np.std(vals, ddof=1)) if len(vals) > 1 else 0.0,
            "min": float(np.min(vals)),
            "max": float(np.max(vals)),
            "values": {s: round(seed_results[s][m], 4) for s in seed_results},
        }

    print(f"\n{'='*70}")
    print(f"Multi-Seed DGS Stability: {args.dataset_name} ({len(seed_results)} seeds)")
    print(f"{'='*70}")

    print(f"\n{'Metric':<20} {'Mean':>10} {'Std':>10} {'Min':>10} {'Max':>10}")
    print("-" * 64)
    for m in metrics:
        s = summary[m]
        print(f"{m:<20} {s['mean']:>10.4f} {s['std']:>10.4f} {s['min']:>10.4f} {s['max']:>10.4f}")

    print(f"\nPer-seed DGS F1 (macro):")
    for label in seed_results:
        r = seed_results[label]
        print(f"  {label}: DGS={r['macro_dgs']:.4f} Greedy={r['macro_greedy']:.4f} "
              f"LP={r['macro_lp_all']:.4f} Delta={r['dgs_minus_greedy']:+.4f} "
              f"Degen={r['degen_pct']:.1f}%")

    output = {
        "config": {
            "dataset_name": args.dataset_name,
            "n_samples": args.n_samples,
            "n_seeds": len(seed_results),
        },
        "per_seed": seed_results,
        "summary": summary,
    }

    if args.output:
        os.makedirs(os.path.dirname(args.output) or ".", exist_ok=True)
        with open(args.output, "w") as f:
            json.dump(output, f, indent=2)
        print(f"\nJSON saved to {args.output}")


if __name__ == "__main__":
    main()
