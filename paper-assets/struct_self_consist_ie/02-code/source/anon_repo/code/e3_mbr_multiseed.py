#!/usr/bin/env python3
"""E3 MBR multi-seed: Greedy / MBR / MV / Oracle with micro-F1.

Entity match: 4-tuple (text, type, start, end).
MV threshold: >= N/2 (inclusive).
"""

import json, sys, os, time
from collections import Counter

def entity_set(sample):
    return set((e["text"], e["type"], e["start"], e["end"]) for e in sample.get("entities", []))

def pairwise_f1(a, b):
    if not a and not b:
        return 1.0
    if not a or not b:
        return 0.0
    tp = len(a & b)
    if tp == 0:
        return 0.0
    p = tp / len(a)
    r = tp / len(b)
    return 2 * p * r / (p + r)

def mbr_select(sample_sets):
    n = len(sample_sets)
    if n == 1:
        return 0
    best_idx, best_score = 0, -1.0
    for i in range(n):
        score = sum(pairwise_f1(sample_sets[i], sample_sets[j]) for j in range(n) if j != i) / (n - 1)
        if score > best_score:
            best_score = score
            best_idx = i
    return best_idx

def mv_construct(samples, n):
    threshold = n / 2  # >= N/2
    counts = Counter()
    for s in samples:
        for e in s.get("entities", []):
            counts[(e["text"], e["type"], e["start"], e["end"])] += 1
    return set(k for k, c in counts.items() if c >= threshold)

def micro_f1_from_pairs(pred_gold_pairs):
    tp_total = fp_total = fn_total = 0
    for pred, gold in pred_gold_pairs:
        tp = len(pred & gold)
        fp = len(pred - gold)
        fn = len(gold - pred)
        tp_total += tp
        fp_total += fp
        fn_total += fn
    if tp_total == 0:
        return 0.0
    p = tp_total / (tp_total + fp_total)
    r = tp_total / (tp_total + fn_total)
    return 2 * p * r / (p + r)

def run_one(path, max_n=8):
    greedy_pairs = []
    mbr_pairs = []
    mv_pairs = []
    oracle_pairs = []

    n_instances = 0
    n_skipped = 0
    t0 = time.time()

    with open(path) as f:
        for idx, line in enumerate(f):
            obj = json.loads(line)
            gold = entity_set(obj["gold"])
            if not gold:
                n_skipped += 1
                continue
            n_instances += 1

            samples = obj["samples"][:max_n]
            n = len(samples)
            sample_sets = [entity_set(s) for s in samples]

            # Greedy (T=0)
            greedy_set = entity_set(obj["greedy"])
            greedy_pairs.append((greedy_set, gold))

            # MBR
            mbr_idx = mbr_select(sample_sets)
            mbr_pairs.append((sample_sets[mbr_idx], gold))

            # MV (>= N/2)
            mv_set = mv_construct(samples, n)
            mv_pairs.append((mv_set, gold))

            # Oracle
            best_f1 = -1
            best_set = sample_sets[0]
            for ss in sample_sets:
                f1 = pairwise_f1(ss, gold)
                if f1 > best_f1:
                    best_f1 = f1
                    best_set = ss
            oracle_pairs.append((best_set, gold))

            if (idx + 1) % 5000 == 0:
                print(f"  processed {idx+1}...", flush=True)

    elapsed = time.time() - t0
    greedy_f1 = micro_f1_from_pairs(greedy_pairs)
    mbr_f1 = micro_f1_from_pairs(mbr_pairs)
    mv_f1 = micro_f1_from_pairs(mv_pairs)
    oracle_f1 = micro_f1_from_pairs(oracle_pairs)

    return {
        "n": n_instances,
        "skipped": n_skipped,
        "elapsed_s": round(elapsed, 1),
        "greedy": round(greedy_f1, 5),
        "mbr": round(mbr_f1, 5),
        "mv": round(mv_f1, 5),
        "oracle": round(oracle_f1, 5),
    }

if __name__ == "__main__":
    base = "/root/autodl-tmp/struct_self_consist_ie/output"

    jobs = []
    for arg in sys.argv[1:]:
        # format: dataset:seed:path  OR  dataset:seed (auto path)
        parts = arg.split(":")
        ds, seed = parts[0], parts[1]
        if len(parts) >= 3:
            path = parts[2]
        else:
            path = f"{base}/{ds}_mf4v2_seed{seed}/samples.jsonl"
        jobs.append((ds, seed, path))

    if not jobs:
        print("Usage: python e3_mbr_multiseed.py dataset:seed[:path] ...")
        sys.exit(1)

    results = []
    for ds, seed, path in jobs:
        print(f"\n=== {ds} seed={seed} ===")
        print(f"  path: {path}")
        if not os.path.exists(path):
            print(f"  FILE NOT FOUND - skipping")
            results.append({"dataset": ds, "seed": seed, "status": "missing"})
            continue
        r = run_one(path)
        r["dataset"] = ds
        r["seed"] = seed
        r["status"] = "ok"
        results.append(r)
        print(f"  n={r['n']}, elapsed={r['elapsed_s']}s")
        print(f"  Greedy={r['greedy']:.5f}  MBR={r['mbr']:.5f}  MV={r['mv']:.5f}  Oracle={r['oracle']:.5f}")
        delta_mbr = r['mbr'] - r['greedy']
        delta_mv = r['mv'] - r['greedy']
        print(f"  MBR-Grd={delta_mbr:+.5f}  MV-Grd={delta_mv:+.5f}")

    # JSON output
    out_path = f"{base}/e3_mbr_multiseed_results.json"
    with open(out_path, "w") as f:
        json.dump(results, f, indent=2)
    print(f"\nSaved: {out_path}")
