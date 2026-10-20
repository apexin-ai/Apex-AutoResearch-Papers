#!/usr/bin/env python3
"""Compute LP selection F1 for 5-epoch FewNERD samples."""
import json
import sys
import numpy as np

PATHS = {
    42:  "/root/autodl-tmp/struct_self_consist_ie/output/fewnerd_5epoch_s42/samples.jsonl",
    123: "/root/autodl-tmp/struct_self_consist_ie/output/fewnerd_5epoch_s123/samples.jsonl",
}

def entity_strict_tp_fp_fn(pred_entities, gold_entities):
    pred_set = {(e["start"], e["end"], e["type"]) for e in pred_entities}
    gold_set = {(e["start"], e["end"], e["type"]) for e in gold_entities}
    tp = len(pred_set & gold_set)
    fp = len(pred_set - gold_set)
    fn = len(gold_set - pred_set)
    return tp, fp, fn

def micro_f1(tp, fp, fn):
    p = tp / (tp + fp) if (tp + fp) > 0 else 0.0
    r = tp / (tp + fn) if (tp + fn) > 0 else 0.0
    f1 = 2 * p * r / (p + r) if (p + r) > 0 else 0.0
    return f1

def process_seed(path, seed):
    greedy_tp = greedy_fp = greedy_fn = 0
    lp_tp = lp_fp = lp_fn = 0
    n_inst = 0
    n_lp_diff_greedy = 0

    with open(path) as f:
        for line in f:
            if not line.strip():
                continue
            inst = json.loads(line)
            gold_ents = inst["gold"].get("entities", [])
            samples = inst["samples"]
            greedy = inst.get("greedy", samples[0])

            # Greedy
            tp, fp, fn = entity_strict_tp_fp_fn(greedy.get("entities", []), gold_ents)
            greedy_tp += tp; greedy_fp += fp; greedy_fn += fn

            # LP selection: pick sample with highest mean_logprob
            best_idx = -1
            best_lp = -float("inf")
            for i, s in enumerate(samples):
                lp = s.get("mean_logprob")
                if lp is None:
                    lp = s.get("cumulative_logprob", -999) / max(s.get("n_tokens", 1), 1)
                if lp > best_lp:
                    best_lp = lp
                    best_idx = i

            lp_best = samples[best_idx]
            tp, fp, fn = entity_strict_tp_fp_fn(lp_best.get("entities", []), gold_ents)
            lp_tp += tp; lp_fp += fp; lp_fn += fn

            # Track how often LP selects different from greedy
            greedy_ents_set = frozenset((e["start"], e["end"], e["type"]) for e in greedy.get("entities", []))
            lp_ents_set = frozenset((e["start"], e["end"], e["type"]) for e in lp_best.get("entities", []))
            if greedy_ents_set != lp_ents_set:
                n_lp_diff_greedy += 1

            n_inst += 1

    greedy_f1 = micro_f1(greedy_tp, greedy_fp, greedy_fn)
    lp_f1 = micro_f1(lp_tp, lp_fp, lp_fn)
    delta_pp = (lp_f1 - greedy_f1) * 100

    print(f"Seed {seed}: greedy={greedy_f1:.4f}, lp_select={lp_f1:.4f}, Δ={delta_pp:+.2f} pp  "
          f"({n_inst} inst, LP≠greedy in {n_lp_diff_greedy}/{n_inst}={100*n_lp_diff_greedy/n_inst:.1f}%)")
    return greedy_f1, lp_f1, delta_pp

results = []
for seed, path in sorted(PATHS.items()):
    g, l, d = process_seed(path, seed)
    results.append((seed, g, l, d))

deltas = [r[3] for r in results]
mean_d = np.mean(deltas)
std_d = np.std(deltas, ddof=1) if len(deltas) > 1 else 0.0
print(f"Mean±σ:   Δ = {mean_d:+.2f} ± {std_d:.2f} pp  (n={len(results)} seeds)")
print(f"vs 3-epoch: +1.39pp → {mean_d:+.2f} pp", end="")
if abs(1.39) > 0:
    pct_change = (mean_d - 1.39) / 1.39 * 100
    print(f" ({pct_change:+.1f}% change)")
else:
    print()
