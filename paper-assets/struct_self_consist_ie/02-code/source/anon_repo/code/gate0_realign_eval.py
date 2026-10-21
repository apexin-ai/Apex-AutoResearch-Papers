"""Gate 0 re-evaluation with span realignment post-processing."""
import sys
sys.path.insert(0, '/root/autodl-tmp/struct_self_consist_ie/code')

import json
from sampling import realign_spans
from evaluation import compute_ner_f1, compute_re_f1

PREDS_PATH = "/root/autodl-tmp/struct_self_consist_ie/output/gate0_all_predictions.jsonl"
OUTPUT_PATH = "/root/autodl-tmp/struct_self_consist_ie/output/gate0_realigned_results.json"

# Load existing predictions
all_data = []
with open(PREDS_PATH) as f:
    for line in f:
        line = line.strip()
        if line:
            all_data.append(json.loads(line))

print(f"Loaded {len(all_data)} instances", flush=True)

raw_preds = [d["pred"] for d in all_data]
golds = [d["gold"] for d in all_data]
texts = [d["text"] for d in all_data]

# Apply span realignment
realigned_preds = [realign_spans(pred, text) for pred, text in zip(raw_preds, texts)]

# --- Raw (no realignment) ---
raw_ner = compute_ner_f1(raw_preds, golds)
raw_re = compute_re_f1(raw_preds, golds)

# --- Realigned ---
re_ner = compute_ner_f1(realigned_preds, golds)
re_re = compute_re_f1(realigned_preds, golds)

# Offset accuracy before/after
def offset_accuracy(preds, data):
    correct = total = 0
    for pred, d in zip(preds, data):
        text = d["text"]
        for e in pred.get("entities", []):
            total += 1
            if 0 <= e["start"] < e["end"] <= len(text) and text[e["start"]:e["end"]] == e["text"]:
                correct += 1
    return correct, total

raw_oa_c, raw_oa_t = offset_accuracy(raw_preds, all_data)
re_oa_c, re_oa_t = offset_accuracy(realigned_preds, all_data)

# Relation offset accuracy
def rel_offset_accuracy(preds, data):
    correct = total = 0
    for pred, d in zip(preds, data):
        text = d["text"]
        for r in pred.get("relations", []):
            total += 1
            h_ok = 0 <= r["head_start"] < r["head_end"] <= len(text) and text[r["head_start"]:r["head_end"]] == r["head"]
            t_ok = 0 <= r["tail_start"] < r["tail_end"] <= len(text) and text[r["tail_start"]:r["tail_end"]] == r["tail"]
            if h_ok and t_ok:
                correct += 1
    return correct, total

raw_roa_c, raw_roa_t = rel_offset_accuracy(raw_preds, all_data)
re_roa_c, re_roa_t = rel_offset_accuracy(realigned_preds, all_data)

print("\n" + "=" * 60)
print("  Gate 0 — Raw vs Realigned Comparison")
print("=" * 60)

print(f"\n--- NER Strict Match ---")
print(f"  Raw:      P={raw_ner['precision']:.4f}  R={raw_ner['recall']:.4f}  F1={raw_ner['f1']:.4f}")
print(f"  Realigned:P={re_ner['precision']:.4f}  R={re_ner['recall']:.4f}  F1={re_ner['f1']:.4f}")
print(f"  Delta:    F1 {re_ner['f1'] - raw_ner['f1']:+.4f}")

print(f"\n--- RE Strict Match ---")
print(f"  Raw:      P={raw_re['precision']:.4f}  R={raw_re['recall']:.4f}  F1={raw_re['f1']:.4f}")
print(f"  Realigned:P={re_re['precision']:.4f}  R={re_re['recall']:.4f}  F1={re_re['f1']:.4f}")
print(f"  Delta:    F1 {re_re['f1'] - raw_re['f1']:+.4f}")

print(f"\n--- Entity Offset Accuracy ---")
print(f"  Raw:      {raw_oa_c}/{raw_oa_t} ({100*raw_oa_c/raw_oa_t:.1f}%)" if raw_oa_t else "  Raw: N/A")
print(f"  Realigned:{re_oa_c}/{re_oa_t} ({100*re_oa_c/re_oa_t:.1f}%)" if re_oa_t else "  Realigned: N/A")

print(f"\n--- Relation Offset Accuracy ---")
print(f"  Raw:      {raw_roa_c}/{raw_roa_t} ({100*raw_roa_c/raw_roa_t:.1f}%)" if raw_roa_t else "  Raw: N/A")
print(f"  Realigned:{re_roa_c}/{re_roa_t} ({100*re_roa_c/re_roa_t:.1f}%)" if re_roa_t else "  Realigned: N/A")

# Gate thresholds
ner_f1_pct = re_ner['f1'] * 100
re_f1_pct = re_re['f1'] * 100
ner_pass = ner_f1_pct >= 56
re_pass = re_f1_pct >= 40
gate_pass = ner_pass and re_pass

print(f"\n--- Gate 0 Verdict (Realigned) ---")
print(f"  NER F1 = {ner_f1_pct:.1f}% (threshold: 56%) -> {'PASS' if ner_pass else 'FAIL'}")
print(f"  RE  F1 = {re_f1_pct:.1f}% (threshold: 40%) -> {'PASS' if re_pass else 'FAIL'}")
print(f"  Overall: {'PASS' if gate_pass else 'FAIL'}")
print("=" * 60)

# Save
results = {
    "raw_ner_strict": raw_ner,
    "raw_re_strict": raw_re,
    "realigned_ner_strict": re_ner,
    "realigned_re_strict": re_re,
    "ner_f1_delta": re_ner['f1'] - raw_ner['f1'],
    "re_f1_delta": re_re['f1'] - raw_re['f1'],
    "raw_entity_offset_accuracy": raw_oa_c / raw_oa_t if raw_oa_t else 0,
    "realigned_entity_offset_accuracy": re_oa_c / re_oa_t if re_oa_t else 0,
    "raw_relation_offset_accuracy": raw_roa_c / raw_roa_t if raw_roa_t else 0,
    "realigned_relation_offset_accuracy": re_roa_c / re_roa_t if re_roa_t else 0,
    "gate0_ner_pass": ner_pass,
    "gate0_re_pass": re_pass,
    "gate0_pass": gate_pass,
    "num_instances": len(all_data),
}
with open(OUTPUT_PATH, "w") as f:
    json.dump(results, f, indent=2)
print(f"\nResults saved to {OUTPUT_PATH}", flush=True)

# Save realigned predictions
with open("/root/autodl-tmp/struct_self_consist_ie/output/gate0_realigned_predictions.jsonl", "w") as f:
    for d, rpred in zip(all_data, realigned_preds):
        f.write(json.dumps({
            "id": d.get("id", ""),
            "text": d["text"],
            "gold": d["gold"],
            "raw_pred": d["pred"],
            "realigned_pred": rpred,
        }, ensure_ascii=False) + "\n")
print("Realigned predictions saved.", flush=True)
