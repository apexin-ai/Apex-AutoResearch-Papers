#!/usr/bin/env python3
"""Compute entity-type-averaged macro-F1 for FewNERD 3-seed MV/LP/Oracle."""
import json
import sys
import numpy as np
from collections import Counter, defaultdict

PATHS = {
    42:  "/root/autodl-tmp/struct_self_consist_ie/output/fewnerd_mf4v2_seed42_v3/samples.jsonl",
    456: "/root/autodl-tmp/struct_self_consist_ie/output/fewnerd_mf4v2_seed456/samples.jsonl",
    123: "/root/autodl-tmp/struct_self_consist_ie/output/fewnerd_mf4v2_seed123_v4/samples.jsonl",
}

def extract_entities_typed(output_dict):
    """Return set of (start, end, type) tuples and dict of type -> set of (start, end, type)."""
    entities = set()
    by_type = defaultdict(set)
    for e in output_dict.get("entities", []):
        key = (e["start"], e["end"], e["type"])
        entities.add(key)
        by_type[e["type"]].add(key)
    return entities, by_type

def prf(tp, fp, fn):
    if tp == 0:
        return 0.0, 0.0, 0.0
    p = tp / (tp + fp)
    r = tp / (tp + fn)
    f = 2 * p * r / (p + r)
    return p, r, f

def process_seed(path):
    # Per-type TP/FP/FN accumulators for each method
    methods = ["greedy", "mv", "lp", "oracle"]
    type_counts = {m: defaultdict(lambda: [0,0,0]) for m in methods}
    
    n_total = 0
    n_gold_nonempty = 0
    n_degenerate = 0
    all_entity_types = set()
    
    with open(path) as f:
        for line in f:
            inst = json.loads(line)
            gold_ents, gold_by_type = extract_entities_typed(inst["gold"])
            n_total += 1
            
            if len(gold_ents) == 0:
                continue
            n_gold_nonempty += 1
            
            all_entity_types.update(gold_by_type.keys())
            
            # Greedy
            greedy_ents, greedy_by_type = extract_entities_typed(inst["greedy"])
            
            # Samples
            samples = inst["samples"]
            n_samples = len(samples)
            sample_ent_sets = []
            sample_by_types = []
            sample_lps = []
            entity_counter = Counter()
            
            for s in samples:
                s_ents, s_by_type = extract_entities_typed(s)
                sample_ent_sets.append(s_ents)
                sample_by_types.append(s_by_type)
                lp = s.get("mean_logprob")
                if lp is None:
                    lp = s.get("cumulative_logprob", -999) / max(s.get("n_tokens", 1), 1)
                sample_lps.append(lp)
                for e in s_ents:
                    entity_counter[e] += 1
            
            # MV strict: count > N/2
            threshold = n_samples / 2
            mv_ents = frozenset(e for e, c in entity_counter.items() if c > threshold)
            mv_by_type = defaultdict(set)
            for e in mv_ents:
                mv_by_type[e[2]].add(e)
            
            # LP-best: sample with highest mean_logprob
            lp_idx = int(np.argmax(sample_lps))
            lp_ents = sample_ent_sets[lp_idx]
            lp_by_type = sample_by_types[lp_idx]
            
            # Oracle: sample with highest instance F1
            best_f1 = -1
            best_idx = 0
            for i, s_ents in enumerate(sample_ent_sets):
                tp = len(s_ents & gold_ents)
                fp = len(s_ents - gold_ents)
                fn = len(gold_ents - s_ents)
                _, _, f1 = prf(tp, fp, fn)
                if f1 > best_f1:
                    best_f1 = f1
                    best_idx = i
            oracle_ents = sample_ent_sets[best_idx]
            oracle_by_type = sample_by_types[best_idx]
            
            # Degeneracy: all samples produce identical entity sets
            if len(set(frozenset(s) for s in sample_ent_sets)) == 1:
                n_degenerate += 1
            
            # Accumulate per-type TP/FP/FN for each method
            # We need to iterate over ALL gold types for this instance
            # plus any predicted types
            inst_types = set(gold_by_type.keys())
            for pred_by_type in [greedy_by_type, mv_by_type, lp_by_type, oracle_by_type]:
                inst_types.update(pred_by_type.keys())
            
            method_preds = {
                "greedy": greedy_by_type,
                "mv": mv_by_type,
                "lp": lp_by_type,
                "oracle": oracle_by_type,
            }
            
            for t in inst_types:
                gold_t = gold_by_type.get(t, set())
                for m in methods:
                    pred_t = method_preds[m].get(t, set())
                    tp = len(pred_t & gold_t)
                    fp = len(pred_t - gold_t)
                    fn = len(gold_t - pred_t)
                    type_counts[m][t][0] += tp
                    type_counts[m][t][1] += fp
                    type_counts[m][t][2] += fn
    
    # Compute per-type F1 and macro average
    # Only average over types that appear in gold
    results = {}
    for m in methods:
        per_type_f1 = {}
        for t in sorted(all_entity_types):
            tp, fp, fn = type_counts[m][t]
            _, _, f1 = prf(tp, fp, fn)
            per_type_f1[t] = f1
        macro_f1 = np.mean(list(per_type_f1.values()))
        results[m] = {"macro_f1": macro_f1, "per_type": per_type_f1}
    
    degen_rate = n_degenerate / n_gold_nonempty * 100
    
    return {
        "n_total": n_total,
        "n_gold_nonempty": n_gold_nonempty,
        "n_degenerate": n_degenerate,
        "degen_rate": degen_rate,
        "results": results,
    }

# Main
all_seeds = {}
for seed, path in sorted(PATHS.items()):
    print(f"Processing seed {seed}...", file=sys.stderr)
    all_seeds[seed] = process_seed(path)

# Print table
print("FewNERD 3-seed (s42, s456, s123) N=8 T=1.0 Qwen3-8B FT")
print("Metric: entity-type-averaged macro-F1")
print()

header = "| Seed | Greedy | MV | MV Δ(pp) | LP | LP Δ(pp) | Oracle | Degen% |"
sep =    "|------|--------|------|----------|------|----------|--------|--------|"
print(header)
print(sep)

greedy_vals = []
mv_vals = []
lp_vals = []
oracle_vals = []
mv_delta_vals = []
lp_delta_vals = []
degen_vals = []

for seed in [42, 456, 123]:
    r = all_seeds[seed]
    g = r["results"]["greedy"]["macro_f1"] * 100
    m = r["results"]["mv"]["macro_f1"] * 100
    l = r["results"]["lp"]["macro_f1"] * 100
    o = r["results"]["oracle"]["macro_f1"] * 100
    md = m - g
    ld = l - g
    d = r["degen_rate"]
    
    greedy_vals.append(g)
    mv_vals.append(m)
    lp_vals.append(l)
    oracle_vals.append(o)
    mv_delta_vals.append(md)
    lp_delta_vals.append(ld)
    degen_vals.append(d)
    
    print(f"| {seed:<4} | {g:.2f}  | {m:.2f} | {md:+.2f}    | {l:.2f} | {ld:+.2f}    | {o:.2f}  | {d:.1f}   |")

# Mean ± std
def fmt_ms(vals):
    return f"{np.mean(vals):.2f}±{np.std(vals):.2f}"

print(f"| Mean±σ | {fmt_ms(greedy_vals)} | {fmt_ms(mv_vals)} | {fmt_ms(mv_delta_vals)} | {fmt_ms(lp_vals)} | {fmt_ms(lp_delta_vals)} | {fmt_ms(oracle_vals)} | {fmt_ms(degen_vals)} |")

# Also print per-type breakdown for reference
print()
print("=== Per-type F1 breakdown (seed-averaged) ===")
print()
entity_types = sorted(all_seeds[42]["results"]["greedy"]["per_type"].keys())
print(f"| Type | Greedy | MV | MV Δ(pp) | LP | LP Δ(pp) | Oracle |")
print(f"|------|--------|------|----------|------|----------|--------|")
for t in entity_types:
    g_vals = [all_seeds[s]["results"]["greedy"]["per_type"][t] * 100 for s in [42, 456, 123]]
    m_vals = [all_seeds[s]["results"]["mv"]["per_type"][t] * 100 for s in [42, 456, 123]]
    l_vals = [all_seeds[s]["results"]["lp"]["per_type"][t] * 100 for s in [42, 456, 123]]
    o_vals = [all_seeds[s]["results"]["oracle"]["per_type"][t] * 100 for s in [42, 456, 123]]
    g = np.mean(g_vals)
    m = np.mean(m_vals)
    l = np.mean(l_vals)
    o = np.mean(o_vals)
    print(f"| {t:<12} | {g:.2f} | {m:.2f} | {m-g:+.2f} | {l:.2f} | {l-g:+.2f} | {o:.2f} |")

