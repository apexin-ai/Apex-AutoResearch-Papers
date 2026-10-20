#!/usr/bin/env python3
"""Unified MV consistency recomputation (v4).
Changes from v3: MV threshold strict > N/2 (N=8: need >=5, not >=4).
Also outputs inclusive (>=4) for v3 comparison.
Filters to gold-non-empty instances only.
"""
import json
import argparse
from collections import Counter


def extract_entities(output_dict):
    entities = set()
    for e in output_dict.get("entities", []):
        entities.add((e["text"], e["type"], e["start"], e["end"]))
    return frozenset(entities)


def entity_f1_counts(pred, gold):
    tp = len(pred & gold)
    fp = len(pred - gold)
    fn = len(gold - pred)
    return tp, fp, fn


def instance_f1(pred, gold):
    tp, fp, fn = entity_f1_counts(pred, gold)
    if tp == 0:
        return 0.0
    p = tp / (tp + fp)
    r = tp / (tp + fn)
    return 2 * p * r / (p + r)


def micro_f1(tp, fp, fn):
    if tp == 0:
        return 0.0
    p = tp / (tp + fp)
    r = tp / (tp + fn)
    return 2 * p * r / (p + r)


def process_file(path):
    greedy_tp = greedy_fp = greedy_fn = 0
    mv_strict_tp = mv_strict_fp = mv_strict_fn = 0
    mv_incl_tp = mv_incl_fp = mv_incl_fn = 0
    oracle_tp = oracle_fp = oracle_fn = 0
    n_total = 0
    n_gold_nonempty = 0
    n_degenerate = 0

    with open(path) as f:
        for line in f:
            instance = json.loads(line)
            gold_entities = extract_entities(instance["gold"])
            n_total += 1

            if len(gold_entities) == 0:
                continue

            n_gold_nonempty += 1

            greedy_entities = extract_entities(instance["greedy"])
            tp, fp, fn = entity_f1_counts(greedy_entities, gold_entities)
            greedy_tp += tp; greedy_fp += fp; greedy_fn += fn

            samples = instance["samples"]
            n_samples = len(samples)
            sample_entity_sets = []
            entity_counter = Counter()
            for s in samples:
                s_entities = extract_entities(s)
                sample_entity_sets.append(s_entities)
                for e in s_entities:
                    entity_counter[e] += 1

            threshold = n_samples / 2  # 4.0 for N=8

            mv_strict = frozenset(e for e, c in entity_counter.items() if c > threshold)
            tp, fp, fn = entity_f1_counts(mv_strict, gold_entities)
            mv_strict_tp += tp; mv_strict_fp += fp; mv_strict_fn += fn

            mv_incl = frozenset(e for e, c in entity_counter.items() if c >= threshold)
            tp, fp, fn = entity_f1_counts(mv_incl, gold_entities)
            mv_incl_tp += tp; mv_incl_fp += fp; mv_incl_fn += fn

            best_f1_val = -1.0
            best_tp = best_fp = best_fn = 0
            for s_entities in sample_entity_sets:
                f1_val = instance_f1(s_entities, gold_entities)
                if f1_val > best_f1_val:
                    best_f1_val = f1_val
                    best_tp, best_fp, best_fn = entity_f1_counts(s_entities, gold_entities)
            oracle_tp += best_tp; oracle_fp += best_fp; oracle_fn += best_fn

            if len(set(sample_entity_sets)) == 1:
                n_degenerate += 1

    g_f1 = micro_f1(greedy_tp, greedy_fp, greedy_fn)
    ms_f1 = micro_f1(mv_strict_tp, mv_strict_fp, mv_strict_fn)
    mi_f1 = micro_f1(mv_incl_tp, mv_incl_fp, mv_incl_fn)
    o_f1 = micro_f1(oracle_tp, oracle_fp, oracle_fn)
    degen = n_degenerate / n_gold_nonempty if n_gold_nonempty > 0 else 0

    def acrit_old(pi_mv):
        return pi_mv / (2 - pi_mv) if pi_mv < 2 else float('inf')

    return {
        "n_total": n_total,
        "n_gold_nonempty": n_gold_nonempty,
        "greedy_f1": g_f1,
        "mv_strict_f1": ms_f1,
        "mv_incl_f1": mi_f1,
        "oracle_f1": o_f1,
        "delta_sc_strict_pp": (ms_f1 - g_f1) * 100,
        "delta_sc_incl_pp": (mi_f1 - g_f1) * 100,
        "degen": degen,
        "alpha_crit_strict": g_f1 / 2,
        "alpha_crit_incl": g_f1 / 2,
        "alpha_crit_eff_strict": (g_f1 / 2) / (1 - degen) if degen < 1 else float('inf'),
        "alpha_crit_eff_incl": (g_f1 / 2) / (1 - degen) if degen < 1 else float('inf'),
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True)
    parser.add_argument("--dataset", required=True)
    parser.add_argument("--seed", required=True, type=int)
    args = parser.parse_args()

    r = process_file(args.input)
    print(f"Dataset: {args.dataset}, Seed: {args.seed}")
    print(f"  n={r['n_gold_nonempty']} gold-nonempty (of {r['n_total']} total)")
    print(f"  greedy_f1:       {r['greedy_f1']:.4f}")
    print(f"  mv_strict_f1:    {r['mv_strict_f1']:.4f}  (>N/2, need>=5/8)")
    print(f"  mv_incl_f1:      {r['mv_incl_f1']:.4f}  (>=N/2, need>=4/8)")
    print(f"  oracle_f1:       {r['oracle_f1']:.4f}")
    print(f"  Δ_SC strict:     {r['delta_sc_strict_pp']:+.2f}pp")
    print(f"  Δ_SC incl:       {r['delta_sc_incl_pp']:+.2f}pp")
    print(f"  δ (degen):       {r['degen']*100:.1f}%")
    print(f"  α_crit strict:   {r['alpha_crit_strict']:.4f}")
    print(f"  α_crit incl:     {r['alpha_crit_incl']:.4f}")
    print(f"  α_crit_eff str:  {r['alpha_crit_eff_strict']:.4f}")
    print(f"  α_crit_eff incl: {r['alpha_crit_eff_incl']:.4f}")
    out = {**r, "dataset": args.dataset, "seed": args.seed}
    print(f"JSON:{json.dumps(out)}")


if __name__ == "__main__":
    main()
