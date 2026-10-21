import json
import sys
from collections import Counter, defaultdict

DATA = "/root/autodl-tmp/struct_self_consist_ie/output/exp_020_pilot/samples.jsonl"

def entity_set(ents):
    """Convert entity list to set of (text, type, start, end) tuples for matching."""
    return {(e["text"], e["type"], e["start"], e["end"]) for e in ents}

def compute_f1(pred_ents, gold_ents):
    pred_set = entity_set(pred_ents)
    gold_set = entity_set(gold_ents)
    if not gold_set and not pred_set:
        return 1.0
    if not gold_set or not pred_set:
        return 0.0
    tp = len(pred_set & gold_set)
    prec = tp / len(pred_set) if pred_set else 0
    rec = tp / len(gold_set) if gold_set else 0
    if prec + rec == 0:
        return 0.0
    return 2 * prec * rec / (prec + rec)

# Load data
instances = []
with open(DATA) as f:
    for line in f:
        instances.append(json.loads(line))

print(f"Total instances: {len(instances)}")

# Categorize
gold_empty = []      # gold has no entities
greedy_zero = []     # gold non-empty, greedy F1 = 0
greedy_nonzero = []  # gold non-empty, greedy F1 > 0

for inst in instances:
    gold_ents = inst["gold"]["entities"]
    greedy_ents = inst["greedy"]["entities"]
    f1 = compute_f1(greedy_ents, gold_ents)
    inst["_greedy_f1"] = f1
    
    if not gold_ents:
        gold_empty.append(inst)
    elif f1 == 0:
        greedy_zero.append(inst)
    else:
        greedy_nonzero.append(inst)

print(f"\n=== CATEGORY BREAKDOWN ===")
print(f"Gold empty (no entities):     {len(gold_empty)}")
print(f"Greedy F1 = 0 (gold present): {len(greedy_zero)}")
print(f"Greedy F1 > 0:                {len(greedy_nonzero)}")

# ============================================================
# 1. Gold-empty analysis: are greedy predictions also empty?
# ============================================================
print(f"\n=== GOLD-EMPTY INSTANCES ({len(gold_empty)}) ===")
ge_greedy_also_empty = sum(1 for inst in gold_empty if not inst["greedy"]["entities"])
ge_greedy_has_preds = len(gold_empty) - ge_greedy_also_empty
print(f"Greedy also empty:    {ge_greedy_also_empty}")
print(f"Greedy has FP preds:  {ge_greedy_has_preds}")
if ge_greedy_has_preds > 0:
    print("  Examples of FP predictions on gold-empty:")
    count = 0
    for inst in gold_empty:
        if inst["greedy"]["entities"]:
            print(f"  [{inst['id']}] text: {inst['text'][:80]}...")
            for e in inst["greedy"]["entities"][:3]:
                print(f"    pred: '{e['text']}' ({e['type']})")
            count += 1
            if count >= 3:
                break

# ============================================================
# 2. Entity type distribution for greedy_zero vs greedy_nonzero
# ============================================================
print(f"\n=== ENTITY TYPE DISTRIBUTION ===")
zero_types = Counter()
nonzero_types = Counter()
zero_type_instances = defaultdict(int)
nonzero_type_instances = defaultdict(int)

for inst in greedy_zero:
    types_in_inst = set()
    for e in inst["gold"]["entities"]:
        zero_types[e["type"]] += 1
        types_in_inst.add(e["type"])
    for t in types_in_inst:
        zero_type_instances[t] += 1

for inst in greedy_nonzero:
    types_in_inst = set()
    for e in inst["gold"]["entities"]:
        nonzero_types[e["type"]] += 1
        types_in_inst.add(e["type"])
    for t in types_in_inst:
        nonzero_type_instances[t] += 1

all_types = sorted(set(list(zero_types.keys()) + list(nonzero_types.keys())))
print(f"{'Type':<20} {'ZeroF1_ents':>12} {'NonZero_ents':>12} {'ZeroF1_inst':>12} {'NonZero_inst':>12} {'Zero_rate':>10}")
for t in all_types:
    z_inst = zero_type_instances.get(t, 0)
    nz_inst = nonzero_type_instances.get(t, 0)
    total_inst = z_inst + nz_inst
    rate = z_inst / total_inst if total_inst > 0 else 0
    print(f"{t:<20} {zero_types.get(t,0):>12} {nonzero_types.get(t,0):>12} {z_inst:>12} {nz_inst:>12} {rate:>10.1%}")

# ============================================================
# 3. Input length distribution
# ============================================================
print(f"\n=== INPUT LENGTH DISTRIBUTION ===")
import statistics

def length_stats(insts, label):
    lengths = [len(inst["text"]) for inst in insts]
    if not lengths:
        print(f"{label}: no instances")
        return
    lengths.sort()
    mean = statistics.mean(lengths)
    median = statistics.median(lengths)
    p90 = lengths[int(len(lengths)*0.9)] if len(lengths) >= 10 else max(lengths)
    print(f"{label}: n={len(lengths)}, mean={mean:.0f}, median={median:.0f}, p90={p90}, min={min(lengths)}, max={max(lengths)}")

length_stats(greedy_zero, "Zero-F1  ")
length_stats(greedy_nonzero, "Non-zero ")
length_stats(gold_empty, "Gold-empty")

# Gold entity count distribution
print(f"\n=== GOLD ENTITY COUNT DISTRIBUTION ===")
def ent_count_stats(insts, label):
    counts = [len(inst["gold"]["entities"]) for inst in insts]
    if not counts:
        return
    print(f"{label}: mean={statistics.mean(counts):.1f}, median={statistics.median(counts):.1f}, min={min(counts)}, max={max(counts)}")

ent_count_stats(greedy_zero, "Zero-F1  ")
ent_count_stats(greedy_nonzero, "Non-zero ")

# ============================================================
# 4. Detailed diagnosis of zero-F1 samples
# ============================================================
print(f"\n=== DETAILED ZERO-F1 DIAGNOSIS ===")

# Classify zero-F1 reasons
diagnosis_counts = Counter()
for inst in greedy_zero:
    gold_ents = inst["gold"]["entities"]
    greedy_ents = inst["greedy"]["entities"]
    
    if not greedy_ents:
        inst["_diagnosis"] = "EMPTY_PRED"
    else:
        # Has predictions but all wrong
        gold_set = entity_set(gold_ents)
        pred_set = entity_set(greedy_ents)
        
        # Check if text spans match but types differ
        gold_spans = {(e["text"], e["start"], e["end"]) for e in gold_ents}
        pred_spans = {(e["text"], e["start"], e["end"]) for e in greedy_ents}
        span_overlap = gold_spans & pred_spans
        
        if span_overlap:
            inst["_diagnosis"] = "TYPE_MISMATCH"
        else:
            # Check if text matches but offset differs
            gold_texts = {e["text"].lower() for e in gold_ents}
            pred_texts = {e["text"].lower() for e in greedy_ents}
            text_overlap = gold_texts & pred_texts
            if text_overlap:
                inst["_diagnosis"] = "OFFSET_MISMATCH"
            else:
                inst["_diagnosis"] = "WRONG_ENTITIES"
    
    diagnosis_counts[inst["_diagnosis"]] += 1

print(f"\nDiagnosis breakdown:")
for diag, cnt in diagnosis_counts.most_common():
    print(f"  {diag}: {cnt} ({cnt/len(greedy_zero)*100:.0f}%)")

# ============================================================
# 5. Print 5 detailed examples
# ============================================================
print(f"\n=== SAMPLE ZERO-F1 INSTANCES (5 examples) ===")

# Pick diverse examples: 1 from each diagnosis category if possible
shown = set()
examples = []
for diag in ["TYPE_MISMATCH", "OFFSET_MISMATCH", "WRONG_ENTITIES", "EMPTY_PRED"]:
    for inst in greedy_zero:
        if inst["_diagnosis"] == diag and inst["id"] not in shown:
            examples.append(inst)
            shown.add(inst["id"])
            break

# Fill up to 5
for inst in greedy_zero:
    if len(examples) >= 5:
        break
    if inst["id"] not in shown:
        examples.append(inst)
        shown.add(inst["id"])

for i, inst in enumerate(examples):
    print(f"\n--- Example {i+1}: {inst['id']} [Diagnosis: {inst['_diagnosis']}] ---")
    print(f"Text ({len(inst['text'])} chars): {inst['text'][:200]}{'...' if len(inst['text'])>200 else ''}")
    print(f"Gold entities ({len(inst['gold']['entities'])}):")
    for e in inst["gold"]["entities"][:5]:
        print(f"  '{e['text']}' ({e['type']}) [{e['start']}:{e['end']}]")
    if len(inst["gold"]["entities"]) > 5:
        print(f"  ... and {len(inst['gold']['entities'])-5} more")
    
    print(f"Greedy entities ({len(inst['greedy']['entities'])}):")
    if inst["greedy"]["entities"]:
        for e in inst["greedy"]["entities"][:5]:
            print(f"  '{e['text']}' ({e['type']}) [{e['start']}:{e['end']}]")
        if len(inst["greedy"]["entities"]) > 5:
            print(f"  ... and {len(inst['greedy']['entities'])-5} more")
    else:
        print(f"  (empty)")
    
    # Check samples: how many of N=8 have non-zero F1?
    sample_f1s = []
    for s in inst["samples"]:
        sf1 = compute_f1(s["entities"], inst["gold"]["entities"])
        sample_f1s.append(sf1)
    nonzero_samples = sum(1 for f in sample_f1s if f > 0)
    print(f"Samples (N=8): {nonzero_samples}/8 have F1>0, mean_f1={statistics.mean(sample_f1s):.3f}, max_f1={max(sample_f1s):.3f}")

# ============================================================
# 6. Overall sample-level analysis for zero-F1 instances
# ============================================================
print(f"\n=== SAMPLE-LEVEL RECOVERY FOR ZERO-F1 INSTANCES ===")
recovery_counts = Counter()  # how many of 8 samples have F1>0
for inst in greedy_zero:
    nonzero = sum(1 for s in inst["samples"] if compute_f1(s["entities"], inst["gold"]["entities"]) > 0)
    recovery_counts[nonzero] += 1

print(f"Among {len(greedy_zero)} zero-F1 instances, samples with F1>0:")
for k in range(9):
    cnt = recovery_counts.get(k, 0)
    print(f"  {k}/8 samples F1>0: {cnt} instances")

# Best sample F1 for zero-greedy instances
best_sample_f1s = []
for inst in greedy_zero:
    best = max(compute_f1(s["entities"], inst["gold"]["entities"]) for s in inst["samples"])
    best_sample_f1s.append(best)
print(f"\nBest sample F1 (among zero-greedy): mean={statistics.mean(best_sample_f1s):.3f}, median={statistics.median(best_sample_f1s):.3f}")

