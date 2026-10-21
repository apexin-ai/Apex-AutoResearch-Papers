#!/usr/bin/env python3
"""MBR selection with span-based Jaccard fix.

Two confounds addressed:
1. Utility/evaluation metric misalignment: original used (text,type) Jaccard
   for MBR but (start,end,type) span F1 for evaluation. Now we run both.
2. gold_filter inconsistency: unified to gold_filter=True for all datasets.
"""

import json
import sys

BASE = "/root/autodl-tmp/struct_self_consist_ie"

DATASETS = {
    "SciERC": {
        "path": f"{BASE}/output/exp_012_rerun_1024/samples.jsonl",
        "max_samples": 8,
    },
    "CoNLL": {
        "path": f"{BASE}/output/exp_002_conll_n16_r1024/samples.jsonl",
        "max_samples": 8,
    },
    "FewNERD": {
        "path": f"{BASE}/output/exp_027_fewnerd_n16/samples.jsonl",
        "max_samples": 8,
    },
}


def load_data(path, max_samples=8):
    instances = []
    skipped = 0
    with open(path) as f:
        for line in f:
            obj = json.loads(line)
            if len(obj["gold"]["entities"]) == 0:
                skipped += 1
                continue
            samples = obj["samples"][:max_samples]
            instances.append({
                "id": obj["id"],
                "gold": obj["gold"],
                "samples": samples,
                "greedy": obj["greedy"],
                "logprobs": obj.get("logprobs", [])[:max_samples],
            })
    return instances, skipped


def text_type_set(sample):
    return frozenset((e["text"], e["type"]) for e in sample.get("entities", []))


def span_type_set(sample):
    return frozenset((e["start"], e["end"], e["type"]) for e in sample.get("entities", []))


def jaccard(set_a, set_b):
    if len(set_a) == 0 and len(set_b) == 0:
        return 1.0
    union = len(set_a | set_b)
    if union == 0:
        return 1.0
    return len(set_a & set_b) / union


def mbr_scores(samples, set_fn):
    n = len(samples)
    sets = [set_fn(s) for s in samples]
    scores = []
    for i in range(n):
        total = sum(jaccard(sets[i], sets[j]) for j in range(n) if j != i)
        scores.append(total / (n - 1))
    return scores


def entity_f1(pred_sample, gold):
    pred = set((e["start"], e["end"], e["type"]) for e in pred_sample.get("entities", []))
    gold_s = set((e["start"], e["end"], e["type"]) for e in gold.get("entities", []))
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


def evaluate_dataset(name, cfg):
    instances, skipped = load_data(cfg["path"], cfg["max_samples"])
    n = len(instances)

    greedy_f1s, lp_f1s = [], []
    mbr_text_f1s, mbr_span_f1s = [], []
    oracle_f1s = []
    agreement_count = 0

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

        # Text-based MBR (original)
        text_scores = mbr_scores(samples, text_type_set)
        text_idx = text_scores.index(max(text_scores))
        mbr_text_f1s.append(entity_f1(samples[text_idx], gold))

        # Span-based MBR (fixed: aligned with evaluation metric)
        span_scores = mbr_scores(samples, span_type_set)
        span_idx = span_scores.index(max(span_scores))
        mbr_span_f1s.append(entity_f1(samples[span_idx], gold))

        if text_idx == span_idx:
            agreement_count += 1

        best_f1 = max(entity_f1(s, gold) for s in samples)
        oracle_f1s.append(best_f1)

    def avg(lst):
        return sum(lst) / len(lst) if lst else 0.0

    return {
        "name": name, "n": n, "skipped_empty_gold": skipped,
        "greedy": avg(greedy_f1s), "lp": avg(lp_f1s),
        "mbr_text": avg(mbr_text_f1s), "mbr_span": avg(mbr_span_f1s),
        "oracle": avg(oracle_f1s),
        "text_span_agreement": agreement_count / n if n > 0 else 0,
    }


def main():
    results = []
    for name, cfg in DATASETS.items():
        r = evaluate_dataset(name, cfg)
        results.append(r)
        print(f"\n{'='*65}")
        print(f"Dataset: {r['name']} ({r['n']} inst, {r['skipped_empty_gold']} skipped empty-gold)")
        print(f"{'='*65}")
        print(f"  Greedy F1:            {r['greedy']:.4f}")
        print(f"  LP Selection F1:      {r['lp']:.4f}")
        print(f"  MBR-text (original):  {r['mbr_text']:.4f}  (delta vs greedy: {r['mbr_text']-r['greedy']:+.4f})")
        print(f"  MBR-span (fixed):     {r['mbr_span']:.4f}  (delta vs greedy: {r['mbr_span']-r['greedy']:+.4f})")
        print(f"  Oracle F1:            {r['oracle']:.4f}")
        print(f"  Text/Span agree:      {r['text_span_agreement']:.1%}")
        print(f"  Span-Text delta:      {r['mbr_span']-r['mbr_text']:+.4f}")

    print(f"\n\n{'='*80}")
    print("Summary (all gold_filter=True)")
    print(f"{'='*80}")
    hdr = f"{'Dataset':<10} {'Greedy':>8} {'LP':>8} {'MBR-txt':>8} {'MBR-span':>9} {'Oracle':>8} {'txt-Grd':>8} {'spn-Grd':>8} {'spn-txt':>8}"
    print(hdr)
    print("-" * len(hdr))
    for r in results:
        print(f"{r['name']:<10} {r['greedy']:>8.4f} {r['lp']:>8.4f} {r['mbr_text']:>8.4f} "
              f"{r['mbr_span']:>9.4f} {r['oracle']:>8.4f} "
              f"{r['mbr_text']-r['greedy']:>+8.4f} {r['mbr_span']-r['greedy']:>+8.4f} "
              f"{r['mbr_span']-r['mbr_text']:>+8.4f}")

    # JSON output
    out_path = f"{BASE}/output/mbr_selection_results.json"
    out = {}
    for r in results:
        out[r["name"]] = {
            "n": r["n"],
            "skipped_empty_gold": r["skipped_empty_gold"],
            "greedy_f1": round(r["greedy"], 5),
            "lp_f1": round(r["lp"], 5),
            "mbr_text_f1": round(r["mbr_text"], 5),
            "mbr_span_f1": round(r["mbr_span"], 5),
            "oracle_f1": round(r["oracle"], 5),
            "delta_mbr_text_vs_greedy": round(r["mbr_text"] - r["greedy"], 5),
            "delta_mbr_span_vs_greedy": round(r["mbr_span"] - r["greedy"], 5),
            "delta_span_vs_text": round(r["mbr_span"] - r["mbr_text"], 5),
            "text_span_agreement": round(r["text_span_agreement"], 4),
        }
    with open(out_path, "w") as f:
        json.dump(out, f, indent=2)
    print(f"\nSaved: {out_path}")


if __name__ == "__main__":
    main()
