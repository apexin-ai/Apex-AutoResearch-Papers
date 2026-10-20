#!/usr/bin/env python3
"""E3: MBR baseline with micro-F1, including MV construction baseline.

Methods compared:
- Greedy: T=0 deterministic output
- LP: select sample with highest mean logprob
- MBR: select sample with highest average pairwise F1 with other samples
- MV: majority vote construction (entity included if appears in >50% of samples)
- Oracle: select sample with highest instance-level F1 vs gold

All methods evaluated with micro-F1 (global TP/FP/FN pooling).
"""

import json
import sys
from collections import Counter

BASE = "/root/autodl-tmp/struct_self_consist_ie"

DATASETS = {
    "SciERC": {
        "path": f"{BASE}/output/scierc_mf4v2_seed456/samples.jsonl",
        "max_samples": 8,
    },
    "CoNLL": {
        "path": f"{BASE}/output/exp_002_conll_n16_r1024/samples.jsonl",
        "max_samples": 8,
    },
    "FewNERD": {
        "path": f"{BASE}/output/fewnerd_mf4v2_seed456/samples.jsonl",
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


def span_set(sample):
    return set((e["start"], e["end"], e["type"]) for e in sample.get("entities", []))


def pairwise_f1(set_a, set_b):
    if len(set_a) == 0 and len(set_b) == 0:
        return 1.0
    if len(set_a) == 0 or len(set_b) == 0:
        return 0.0
    tp = len(set_a & set_b)
    if tp == 0:
        return 0.0
    p = tp / len(set_a)
    r = tp / len(set_b)
    return 2 * p * r / (p + r)


def mbr_select(samples):
    """Select sample with highest average pairwise F1 with other samples."""
    n = len(samples)
    if n == 1:
        return 0
    sets = [span_set(s) for s in samples]
    best_idx, best_score = 0, -1.0
    for i in range(n):
        total = sum(pairwise_f1(sets[i], sets[j]) for j in range(n) if j != i)
        score = total / (n - 1)
        if score > best_score:
            best_score = score
            best_idx = i
    return best_idx


def mv_construct(samples, theta=0.5):
    """Majority vote: include entity if it appears in >theta fraction of samples."""
    n = len(samples)
    threshold = n * theta
    entity_counts = Counter()
    for s in samples:
        for e in s.get("entities", []):
            key = (e["start"], e["end"], e["type"])
            entity_counts[key] += 1
    return set(k for k, c in entity_counts.items() if c > threshold)


def instance_f1(pred_set, gold_set):
    if len(pred_set) == 0 and len(gold_set) == 0:
        return 1.0
    if len(pred_set) == 0 or len(gold_set) == 0:
        return 0.0
    tp = len(pred_set & gold_set)
    if tp == 0:
        return 0.0
    p = tp / len(pred_set)
    r = tp / len(gold_set)
    return 2 * p * r / (p + r)


def micro_f1(all_pred_sets, all_gold_sets):
    total_tp, total_fp, total_fn = 0, 0, 0
    for pred, gold in zip(all_pred_sets, all_gold_sets):
        tp = len(pred & gold)
        fp = len(pred - gold)
        fn = len(gold - pred)
        total_tp += tp
        total_fp += fp
        total_fn += fn
    if total_tp == 0:
        return 0.0, 0.0, 0.0
    p = total_tp / (total_tp + total_fp)
    r = total_tp / (total_tp + total_fn)
    f1 = 2 * p * r / (p + r)
    return p, r, f1


def evaluate_dataset(name, cfg):
    instances, skipped = load_data(cfg["path"], cfg["max_samples"])
    n = len(instances)
    print(f"\n{'='*60}")
    print(f"Dataset: {name} ({n} instances, {skipped} empty-gold skipped, N={cfg['max_samples']})")
    print(f"{'='*60}")

    greedy_preds, lp_preds, mbr_preds, mv_preds, oracle_preds = [], [], [], [], []
    gold_sets = []
    
    degen_count = 0

    for idx, inst in enumerate(instances):
        gold = span_set(inst["gold"])
        gold_sets.append(gold)
        samples = inst["samples"]
        logprobs = inst["logprobs"]

        greedy_preds.append(span_set(inst["greedy"]))

        if len(logprobs) == len(samples):
            lp_idx = max(range(len(logprobs)), key=lambda i: logprobs[i])
        else:
            lp_idx = 0
        lp_preds.append(span_set(samples[lp_idx]))

        mbr_idx = mbr_select(samples)
        mbr_preds.append(span_set(samples[mbr_idx]))

        mv_set = mv_construct(samples)
        mv_preds.append(mv_set)

        sample_f1s = [instance_f1(span_set(s), gold) for s in samples]
        oracle_idx = max(range(len(sample_f1s)), key=lambda i: sample_f1s[i])
        oracle_preds.append(span_set(samples[oracle_idx]))

        sample_sets = [span_set(s) for s in samples]
        if len(set(frozenset(s) for s in sample_sets)) == 1:
            degen_count += 1

        if (idx + 1) % 10000 == 0:
            print(f"  Processed {idx+1}/{n}...")

    _, _, greedy_f1 = micro_f1(greedy_preds, gold_sets)
    _, _, lp_f1_val = micro_f1(lp_preds, gold_sets)
    _, _, mbr_f1_val = micro_f1(mbr_preds, gold_sets)
    _, _, mv_f1_val = micro_f1(mv_preds, gold_sets)
    _, _, oracle_f1_val = micro_f1(oracle_preds, gold_sets)

    greedy_iavg = sum(instance_f1(p, g) for p, g in zip(greedy_preds, gold_sets)) / n
    lp_iavg = sum(instance_f1(p, g) for p, g in zip(lp_preds, gold_sets)) / n
    mbr_iavg = sum(instance_f1(p, g) for p, g in zip(mbr_preds, gold_sets)) / n
    mv_iavg = sum(instance_f1(p, g) for p, g in zip(mv_preds, gold_sets)) / n
    oracle_iavg = sum(instance_f1(p, g) for p, g in zip(oracle_preds, gold_sets)) / n

    degen_rate = degen_count / n

    result = {
        "name": name, "n": n, "skipped": skipped, "degen_rate": round(degen_rate, 4),
        "micro_f1": {
            "greedy": round(greedy_f1, 5),
            "lp": round(lp_f1_val, 5),
            "mbr": round(mbr_f1_val, 5),
            "mv": round(mv_f1_val, 5),
            "oracle": round(oracle_f1_val, 5),
        },
        "instance_avg_f1": {
            "greedy": round(greedy_iavg, 5),
            "lp": round(lp_iavg, 5),
            "mbr": round(mbr_iavg, 5),
            "mv": round(mv_iavg, 5),
            "oracle": round(oracle_iavg, 5),
        },
    }

    print(f"  Degeneracy: {degen_rate:.1%}")
    print(f"\n  {'Method':<12} {'Micro-F1':>10} {'Inst-Avg-F1':>12} {'Δ vs Greedy (micro)':>20}")
    print(f"  {'-'*56}")
    for method in ["greedy", "lp", "mbr", "mv", "oracle"]:
        mf = result["micro_f1"][method]
        ia = result["instance_avg_f1"][method]
        delta = mf - result["micro_f1"]["greedy"]
        label = method.upper() if method != "greedy" else "Greedy"
        print(f"  {label:<12} {mf:>10.4f} {ia:>12.4f} {delta:>+20.4f}")

    return result


def main():
    all_results = {}
    for name, cfg in DATASETS.items():
        r = evaluate_dataset(name, cfg)
        all_results[name] = r

    print(f"\n\n{'='*80}")
    print("SUMMARY: Micro-F1 Comparison")
    print(f"{'='*80}")
    print(f"{'Dataset':<10} {'Greedy':>8} {'LP':>8} {'MBR':>8} {'MV':>8} {'Oracle':>8} | {'MBR-Grd':>8} {'MV-Grd':>8} {'LP-Grd':>8}")
    print(f"{'-'*10} {'-'*8} {'-'*8} {'-'*8} {'-'*8} {'-'*8} | {'-'*8} {'-'*8} {'-'*8}")
    for name in ["SciERC", "CoNLL", "FewNERD"]:
        r = all_results[name]["micro_f1"]
        g = r["greedy"]
        print(f"{name:<10} {g:>8.4f} {r['lp']:>8.4f} {r['mbr']:>8.4f} {r['mv']:>8.4f} {r['oracle']:>8.4f}"
              f" | {r['mbr']-g:>+8.4f} {r['mv']-g:>+8.4f} {r['lp']-g:>+8.4f}")

    print(f"\n{'='*80}")
    print("SUMMARY: Instance-Average F1 Comparison")
    print(f"{'='*80}")
    print(f"{'Dataset':<10} {'Greedy':>8} {'LP':>8} {'MBR':>8} {'MV':>8} {'Oracle':>8} | {'MBR-Grd':>8} {'MV-Grd':>8} {'LP-Grd':>8}")
    print(f"{'-'*10} {'-'*8} {'-'*8} {'-'*8} {'-'*8} {'-'*8} | {'-'*8} {'-'*8} {'-'*8}")
    for name in ["SciERC", "CoNLL", "FewNERD"]:
        r = all_results[name]["instance_avg_f1"]
        g = r["greedy"]
        print(f"{name:<10} {g:>8.4f} {r['lp']:>8.4f} {r['mbr']:>8.4f} {r['mv']:>8.4f} {r['oracle']:>8.4f}"
              f" | {r['mbr']-g:>+8.4f} {r['mv']-g:>+8.4f} {r['lp']-g:>+8.4f}")

    # MBR oracle gap analysis
    print(f"\n{'='*80}")
    print("MBR Oracle Gap Closure (micro-F1)")
    print(f"{'='*80}")
    for name in ["SciERC", "CoNLL", "FewNERD"]:
        r = all_results[name]["micro_f1"]
        oracle_gap = r["oracle"] - r["greedy"]
        mbr_gain = r["mbr"] - r["greedy"]
        if oracle_gap > 0:
            closure = mbr_gain / oracle_gap * 100
        else:
            closure = 0
        print(f"{name:<10}  Oracle gap: {oracle_gap:+.4f}  MBR gain: {mbr_gain:+.4f}  Closure: {closure:+.1f}%")

    out_path = f"{BASE}/output/e3_mbr_micro_f1_results.json"
    with open(out_path, "w") as f:
        json.dump(all_results, f, indent=2)
    print(f"\nSaved: {out_path}")


if __name__ == "__main__":
    main()
