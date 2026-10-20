#!/usr/bin/env python3
"""MBR (Minimum Bayes Risk) selection for NER: select sample with highest
average entity-set Jaccard overlap with other samples."""

import json
import sys
from collections import defaultdict

BASE = "/root/autodl-tmp/struct_self_consist_ie"

DATASETS = {
    "SciERC": {
        "path": f"{BASE}/output/exp_012_rerun_1024/samples.jsonl",
        "max_samples": 8,
        "gold_filter": True,
    },
    "CoNLL": {
        "path": f"{BASE}/output/exp_002_conll_n16_r1024/samples.jsonl",
        "max_samples": 8,
        "gold_filter": False,
    },
    "FewNERD": {
        "path": f"{BASE}/output/exp_027_fewnerd_n16/samples.jsonl",
        "max_samples": 8,
        "gold_filter": True,
    },
}


def load_data(path, max_samples=8, gold_filter=False):
    instances = []
    with open(path) as f:
        for line in f:
            obj = json.loads(line)
            if gold_filter and len(obj["gold"]["entities"]) == 0:
                continue
            samples = obj["samples"][:max_samples]
            instances.append({
                "id": obj["id"],
                "gold": obj["gold"],
                "samples": samples,
                "greedy": obj["greedy"],
                "logprobs": obj.get("logprobs", [])[:max_samples],
            })
    return instances


def text_type_set(sample):
    """Entity set as {(text, type)} for MBR overlap computation."""
    return frozenset((e["text"], e["type"]) for e in sample.get("entities", []))


def span_set(sample):
    """Entity set as {(start, end, type)} for F1 evaluation."""
    return set((e["start"], e["end"], e["type"]) for e in sample.get("entities", []))


def jaccard(set_a, set_b):
    if len(set_a) == 0 and len(set_b) == 0:
        return 1.0
    union = len(set_a | set_b)
    if union == 0:
        return 1.0
    return len(set_a & set_b) / union


def mbr_scores(samples):
    n = len(samples)
    sets = [text_type_set(s) for s in samples]
    scores = []
    for i in range(n):
        total = sum(jaccard(sets[i], sets[j]) for j in range(n) if j != i)
        scores.append(total / (n - 1))
    return scores


def entity_f1(pred_sample, gold):
    pred = span_set(pred_sample)
    gold_s = span_set(gold)
    if len(pred) == 0 and len(gold_s) == 0:
        return 1.0
    if len(pred) == 0 or len(gold_s) == 0:
        return 0.0
    tp = len(pred & gold_s)
    p = tp / len(pred)
    r = tp / len(gold_s)
    if p + r == 0:
        return 0.0
    return 2 * p * r / (p + r)


def degeneracy_ratio(samples):
    sets = [text_type_set(s) for s in samples]
    n_unique = len(set(sets))
    return n_unique / len(samples)


def evaluate_dataset(name, cfg):
    instances = load_data(cfg["path"], cfg["max_samples"], cfg["gold_filter"])
    n = len(instances)

    greedy_f1s, lp_f1s, mbr_f1s, oracle_f1s = [], [], [], []
    degen_ratios = []

    for inst in instances:
        gold = inst["gold"]
        samples = inst["samples"]
        logprobs = inst["logprobs"]

        greedy_f1s.append(entity_f1(inst["greedy"], gold))

        if len(logprobs) == len(samples):
            lp_idx = max(range(len(logprobs)), key=lambda i: logprobs[i])
        else:
            lp_idx = 0
        lp_f1s.append(entity_f1(samples[lp_idx], gold))

        scores = mbr_scores(samples)
        mbr_idx = scores.index(max(scores))
        mbr_f1s.append(entity_f1(samples[mbr_idx], gold))

        best_f1 = max(entity_f1(s, gold) for s in samples)
        oracle_f1s.append(best_f1)

        degen_ratios.append(degeneracy_ratio(samples))

    greedy_avg = sum(greedy_f1s) / n
    lp_avg = sum(lp_f1s) / n
    mbr_avg = sum(mbr_f1s) / n
    oracle_avg = sum(oracle_f1s) / n

    degen_groups = {"low_diversity": [], "medium": [], "high_diversity": []}
    for i, dr in enumerate(degen_ratios):
        if dr <= 0.25:
            degen_groups["low_diversity"].append(i)
        elif dr <= 0.625:
            degen_groups["medium"].append(i)
        else:
            degen_groups["high_diversity"].append(i)

    degen_results = {}
    for group_name, indices in degen_groups.items():
        if not indices:
            degen_results[group_name] = None
            continue
        gn = len(indices)
        degen_results[group_name] = {
            "count": gn,
            "greedy": sum(greedy_f1s[i] for i in indices) / gn,
            "lp": sum(lp_f1s[i] for i in indices) / gn,
            "mbr": sum(mbr_f1s[i] for i in indices) / gn,
            "oracle": sum(oracle_f1s[i] for i in indices) / gn,
        }

    return {
        "name": name, "n": n,
        "greedy": greedy_avg, "lp": lp_avg,
        "mbr": mbr_avg, "oracle": oracle_avg,
        "degen": degen_results,
    }


def main():
    results = []
    for name, cfg in DATASETS.items():
        r = evaluate_dataset(name, cfg)
        results.append(r)
        print(f"\n{'='*60}")
        print(f"Dataset: {r['name']} ({r['n']} instances, N={cfg['max_samples']})")
        print(f"{'='*60}")
        print(f"  Greedy F1:        {r['greedy']:.4f}")
        print(f"  LP Selection F1:  {r['lp']:.4f}")
        print(f"  MBR Selection F1: {r['mbr']:.4f}")
        print(f"  Oracle F1:        {r['oracle']:.4f}")
        print(f"  Delta (MBR-Greedy): {r['mbr'] - r['greedy']:+.4f}")
        print(f"  Delta (MBR-LP):     {r['mbr'] - r['lp']:+.4f}")

        print(f"\n  Degeneracy breakdown:")
        for gname in ["low_diversity", "medium", "high_diversity"]:
            d = r["degen"][gname]
            if d is None:
                print(f"    {gname}: (no instances)")
            else:
                print(f"    {gname} ({d['count']} inst): "
                      f"Greedy={d['greedy']:.4f}  LP={d['lp']:.4f}  "
                      f"MBR={d['mbr']:.4f}  Oracle={d['oracle']:.4f}  "
                      f"MBR-Grd={d['mbr']-d['greedy']:+.4f}")

    print(f"\n\n{'='*70}")
    print("Summary Table")
    print(f"{'='*70}")
    print(f"{'Dataset':<12} {'Greedy':>8} {'LP Sel':>8} {'MBR Sel':>8} {'Oracle':>8} {'MBR-Grd':>8} {'MBR-LP':>8}")
    print(f"{'-'*12} {'-'*8} {'-'*8} {'-'*8} {'-'*8} {'-'*8} {'-'*8}")
    for r in results:
        print(f"{r['name']:<12} {r['greedy']:>8.4f} {r['lp']:>8.4f} {r['mbr']:>8.4f} "
              f"{r['oracle']:>8.4f} {r['mbr']-r['greedy']:>+8.4f} {r['mbr']-r['lp']:>+8.4f}")

    # JSON output
    out_path = f"{BASE}/output/analysis_mbr_selection.json"
    out = {}
    for r in results:
        out[r["name"]] = {
            "n": r["n"],
            "greedy_f1": round(r["greedy"], 5),
            "lp_f1": round(r["lp"], 5),
            "mbr_f1": round(r["mbr"], 5),
            "oracle_f1": round(r["oracle"], 5),
            "degeneracy": {
                k: {kk: round(vv, 5) if isinstance(vv, float) else vv
                    for kk, vv in v.items()} if v else None
                for k, v in r["degen"].items()
            },
        }
    with open(out_path, "w") as f:
        json.dump(out, f, indent=2)
    print(f"\nSaved JSON: {out_path}")


if __name__ == "__main__":
    main()
