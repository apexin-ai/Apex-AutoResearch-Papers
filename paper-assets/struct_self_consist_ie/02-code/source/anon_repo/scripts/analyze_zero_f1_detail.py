import json, statistics
from collections import Counter

DATA = "/root/autodl-tmp/struct_self_consist_ie/output/exp_020_pilot/samples.jsonl"

def entity_set(ents):
    return {(e["text"], e["type"], e["start"], e["end"]) for e in ents}

def compute_f1(pred_ents, gold_ents):
    pred_set = entity_set(pred_ents)
    gold_set = entity_set(gold_ents)
    if not gold_set and not pred_set: return 1.0
    if not gold_set or not pred_set: return 0.0
    tp = len(pred_set & gold_set)
    prec = tp / len(pred_set) if pred_set else 0
    rec = tp / len(gold_set) if gold_set else 0
    return 2 * prec * rec / (prec + rec) if prec + rec > 0 else 0.0

instances = []
with open(DATA) as f:
    for line in f:
        instances.append(json.loads(line))

greedy_zero = [inst for inst in instances 
               if inst["gold"]["entities"] and compute_f1(inst["greedy"]["entities"], inst["gold"]["entities"]) == 0]

# === ALL TYPE_MISMATCH CASES ===
print("=== ALL TYPE_MISMATCH CASES ===\n")
for inst in greedy_zero:
    gold_ents = inst["gold"]["entities"]
    greedy_ents = inst["greedy"]["entities"]
    if not greedy_ents:
        continue
    gold_spans = {(e["text"], e["start"], e["end"]) for e in gold_ents}
    pred_spans = {(e["text"], e["start"], e["end"]) for e in greedy_ents}
    if gold_spans & pred_spans:
        print(f"[{inst['id']}] text: {inst['text'][:120]}")
        for e in gold_ents:
            print(f"  GOLD: '{e['text']}' ({e['type']}) [{e['start']}:{e['end']}]")
        for e in greedy_ents:
            print(f"  PRED: '{e['text']}' ({e['type']}) [{e['start']}:{e['end']}]")
        # Check samples
        sample_f1s = [compute_f1(s["entities"], gold_ents) for s in inst["samples"]]
        print(f"  Samples: {sum(1 for f in sample_f1s if f>0)}/8 F1>0, max={max(sample_f1s):.3f}")
        # What types did samples predict for the mismatched entity?
        matched_span = gold_spans & pred_spans
        for span in matched_span:
            gold_type = [e["type"] for e in gold_ents if (e["text"], e["start"], e["end"]) == span][0]
            sample_types = []
            for s in inst["samples"]:
                for e in s["entities"]:
                    if (e["text"], e["start"], e["end"]) == span:
                        sample_types.append(e["type"])
            print(f"  Span '{span[0]}': gold={gold_type}, greedy={[e['type'] for e in greedy_ents if (e['text'], e['start'], e['end'])==span][0]}, samples={Counter(sample_types)}")
        print()

# === 6 COMPLETELY UNRECOVERABLE INSTANCES ===
print("\n=== COMPLETELY UNRECOVERABLE (0/8 samples F1>0) ===\n")
for inst in greedy_zero:
    gold_ents = inst["gold"]["entities"]
    sample_f1s = [compute_f1(s["entities"], gold_ents) for s in inst["samples"]]
    if all(f == 0 for f in sample_f1s):
        print(f"[{inst['id']}]")
        print(f"  Text: {inst['text'][:150]}")
        for e in gold_ents:
            print(f"  GOLD: '{e['text']}' ({e['type']}) [{e['start']}:{e['end']}]")
        greedy_ents = inst["greedy"]["entities"]
        if greedy_ents:
            for e in greedy_ents:
                print(f"  GREEDY: '{e['text']}' ({e['type']}) [{e['start']}:{e['end']}]")
        else:
            print(f"  GREEDY: (empty)")
        # What did samples predict?
        all_sample_ents = Counter()
        for s in inst["samples"]:
            for e in s["entities"]:
                all_sample_ents[(e["text"], e["type"])] += 1
        if all_sample_ents:
            print(f"  Sample predictions (text, type): {dict(all_sample_ents.most_common(5))}")
        else:
            print(f"  Sample predictions: (all empty)")
        print()

# === EMPTY_PRED: gold entity type distribution ===
print("\n=== EMPTY_PRED: gold entity type breakdown ===")
empty_pred_types = Counter()
for inst in greedy_zero:
    if not inst["greedy"]["entities"]:
        for e in inst["gold"]["entities"]:
            empty_pred_types[e["type"]] += 1
print(dict(empty_pred_types.most_common()))

