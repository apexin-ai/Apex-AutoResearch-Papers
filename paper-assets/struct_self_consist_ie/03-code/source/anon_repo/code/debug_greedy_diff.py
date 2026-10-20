#!/usr/bin/env python3
"""Diagnostic: compare greedy F1 computation across three scripts' logic."""
import json
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from evaluation import entity_strict_match

BASE = "/root/autodl-tmp/struct_self_consist_ie"
SCIERC_PATH = f"{BASE}/output/exp_012_rerun_1024/samples.jsonl"

# Load ALL instances
all_instances = []
with open(SCIERC_PATH) as f:
    for line in f:
        all_instances.append(json.loads(line))

print(f"Total instances in file: {len(all_instances)}")

# Check how many have empty gold
empty_gold = [inst for inst in all_instances if len(inst["gold"]["entities"]) == 0]
non_empty_gold = [inst for inst in all_instances if len(inst["gold"]["entities"]) > 0]
print(f"Empty gold: {len(empty_gold)}")
print(f"Non-empty gold (gold_filter=True): {len(non_empty_gold)}")

# --- F1 functions from each script ---

# analysis_dgs_full_validation.py style (uses entity_strict_match)
def f1_dgs_style(pred_entities, gold_entities):
    tp, fp, fn = entity_strict_match(pred_entities, gold_entities)
    if tp + fp == 0 and tp + fn == 0:
        return 1.0
    if tp == 0:
        return 0.0
    p = tp / (tp + fp)
    r = tp / (tp + fn)
    return 2 * p * r / (p + r)

# entity_consensus.py style
def f1_consensus_style(pred_entities, gold_entities):
    pred = set((e["start"], e["end"], e["type"]) for e in pred_entities)
    gold = set((e["start"], e["end"], e["type"]) for e in gold_entities)
    if len(pred) == 0 and len(gold) == 0:
        return 1.0
    if len(pred) == 0 or len(gold) == 0:
        return 0.0
    tp = len(pred & gold)
    if tp == 0:
        return 0.0
    p = tp / len(pred)
    r = tp / len(gold)
    return 2 * p * r / (p + r)

# ccs_selection.py style
def f1_ccs_style(pred_entities, gold_entities):
    pred_set = set((e["start"], e["end"], e["type"]) for e in pred_entities)
    gold_set = set((e["start"], e["end"], e["type"]) for e in gold_entities)
    if len(gold_set) == 0 and len(pred_set) == 0:
        return 1.0
    if len(gold_set) == 0 or len(pred_set) == 0:
        return 0.0
    tp = len(pred_set & gold_set)
    p = tp / len(pred_set)
    r = tp / len(gold_set)
    if p + r == 0:
        return 0.0
    return 2 * p * r / (p + r)

# --- Test 1: Are the F1 functions equivalent on all instances? ---
print("\n=== Test 1: F1 function equivalence ===")
diffs = []
for i, inst in enumerate(all_instances):
    pred = inst["greedy"]["entities"]
    gold = inst["gold"]["entities"]
    f1_a = f1_dgs_style(pred, gold)
    f1_b = f1_consensus_style(pred, gold)
    f1_c = f1_ccs_style(pred, gold)
    if abs(f1_a - f1_b) > 1e-10 or abs(f1_a - f1_c) > 1e-10:
        diffs.append((i, inst.get("id", "?"), f1_a, f1_b, f1_c,
                       len(pred), len(gold)))

if diffs:
    print(f"Found {len(diffs)} instances with different F1:")
    for idx, iid, a, b, c, np_, ng in diffs[:10]:
        print(f"  idx={idx} id={iid} dgs={a:.6f} cons={b:.6f} ccs={c:.6f} "
              f"n_pred={np_} n_gold={ng}")
else:
    print("All three F1 functions produce identical results on all instances.")

# --- Test 2: Gold filter effect ---
print("\n=== Test 2: Gold filter effect on greedy F1 ===")

# Without gold_filter (analysis_dgs style)
all_f1s = [f1_dgs_style(inst["greedy"]["entities"], inst["gold"]["entities"])
           for inst in all_instances]
mean_all = sum(all_f1s) / len(all_f1s)
print(f"No gold_filter ({len(all_instances)} inst): mean greedy F1 = {mean_all:.6f}")

# With gold_filter (consensus/ccs style)
filtered_f1s = [f1_dgs_style(inst["greedy"]["entities"], inst["gold"]["entities"])
                for inst in non_empty_gold]
mean_filtered = sum(filtered_f1s) / len(filtered_f1s)
print(f"With gold_filter ({len(non_empty_gold)} inst): mean greedy F1 = {mean_filtered:.6f}")

# --- Test 3: What F1 do empty-gold instances contribute? ---
print("\n=== Test 3: Empty gold instances ===")
for inst in empty_gold[:5]:
    pred = inst["greedy"]["entities"]
    gold = inst["gold"]["entities"]
    f1 = f1_dgs_style(pred, gold)
    print(f"  id={inst.get('id','?')} n_pred={len(pred)} n_gold={len(gold)} f1={f1:.4f}")

# --- Test 4: Check N=8 truncation effect ---
print("\n=== Test 4: N=8 truncation vs full samples (greedy unaffected) ===")
n_samples_counts = [len(inst["samples"]) for inst in all_instances]
print(f"Samples per instance: min={min(n_samples_counts)} max={max(n_samples_counts)} "
      f"mean={sum(n_samples_counts)/len(n_samples_counts):.1f}")

# --- Test 5: Reproduce the exact numbers ---
print("\n=== Test 5: Reproduce exact greedy F1 values ===")

# analysis_dgs style: load all, compute macro greedy F1
# But we need to check if it's called with gold_filter path
# Check the actual calling convention
import numpy as np
arr = np.array(all_f1s)
print(f"analysis_dgs (no filter, {len(all_f1s)} inst): {arr.mean():.4f}")

arr2 = np.array(filtered_f1s)
print(f"consensus/ccs (gold_filter, {len(filtered_f1s)} inst): {arr2.mean():.4f}")
