"""Gate 0 quality check: greedy inference NER/RE F1 on SciERC test set."""
import sys
sys.path.insert(0, '/root/autodl-tmp/struct_self_consist_ie/code')

import json
import os
from data_utils import load_uie_jsonl
from sampling import build_uie_prompt, parse_extraction_output, SCIERC_SCHEMA_HINT
from evaluation import compute_ner_f1, compute_re_f1

MODEL_PATH = "/root/autodl-tmp/struct_self_consist_ie/checkpoints/qwen3-8b-scierc-merged"
TEST_DATA = "/root/autodl-tmp/struct_self_consist_ie/data/test.jsonl"

instances = load_uie_jsonl(TEST_DATA)
print(f"Loaded {len(instances)} test instances", flush=True)

print("Initializing vLLM (enforce_eager)...", flush=True)
from vllm import LLM, SamplingParams
from transformers import AutoTokenizer

llm = LLM(
    model=MODEL_PATH,
    tensor_parallel_size=1,
    max_model_len=2048,
    gpu_memory_utilization=0.85,
    enforce_eager=True,
)
tokenizer = AutoTokenizer.from_pretrained(MODEL_PATH, trust_remote_code=True)
print("Sampler ready.", flush=True)

prompts = [build_uie_prompt(inst["text"], subtask="full", schema_hint=SCIERC_SCHEMA_HINT, use_train_format=True) for inst in instances]
chat_prompts = []
for p in prompts:
    cp = tokenizer.apply_chat_template(
        [{"role": "user", "content": p}],
        tokenize=False,
        add_generation_prompt=True,
        enable_thinking=False,
    )
    chat_prompts.append(cp)

params = SamplingParams(n=1, temperature=0.0, max_tokens=512)
print("Starting greedy inference (unconstrained)...", flush=True)
outputs = llm.generate(chat_prompts, params)

predictions = [parse_extraction_output(out.outputs[0].text) for out in outputs]
raw_outputs = [out.outputs[0].text for out in outputs]
golds = [{"entities": inst.get("entities", []), "relations": inst.get("relations", []), "events": inst.get("events", [])} for inst in instances]

# Strict match
ner_metrics = compute_ner_f1(predictions, golds)
re_metrics = compute_re_f1(predictions, golds)

# Text-level match (text + type, ignoring offsets)
def compute_text_match_f1(predictions, golds, field='entities'):
    total_tp = total_fp = total_fn = 0
    for pred, gold in zip(predictions, golds):
        if field == 'entities':
            pred_set = {(e['text'].strip(), e['type']) for e in pred.get('entities', [])}
            gold_set = {(e['text'].strip(), e['type']) for e in gold.get('entities', [])}
        else:  # relations
            pred_set = {(r['head'].strip(), r['tail'].strip(), r['type']) for r in pred.get('relations', [])}
            gold_set = {(r['head'].strip(), r['tail'].strip(), r['type']) for r in gold.get('relations', [])}
        total_tp += len(pred_set & gold_set)
        total_fp += len(pred_set - gold_set)
        total_fn += len(gold_set - pred_set)
    p = total_tp / (total_tp + total_fp) if (total_tp + total_fp) > 0 else 0
    r = total_tp / (total_tp + total_fn) if (total_tp + total_fn) > 0 else 0
    f1 = 2*p*r/(p+r) if (p+r) > 0 else 0
    return {"precision": p, "recall": r, "f1": f1, "tp": total_tp, "fp": total_fp, "fn": total_fn}

ner_text = compute_text_match_f1(predictions, golds, 'entities')
re_text = compute_text_match_f1(predictions, golds, 'relations')

print(f"\n=== Strict Match ===", flush=True)
print(f"NER: P={ner_metrics['precision']:.4f} R={ner_metrics['recall']:.4f} F1={ner_metrics['f1']:.4f}", flush=True)
print(f"RE:  P={re_metrics['precision']:.4f} R={re_metrics['recall']:.4f} F1={re_metrics['f1']:.4f}", flush=True)

print(f"\n=== Text-level Match (ignoring offsets) ===", flush=True)
print(f"NER: P={ner_text['precision']:.4f} R={ner_text['recall']:.4f} F1={ner_text['f1']:.4f} (tp={ner_text['tp']}, fp={ner_text['fp']}, fn={ner_text['fn']})", flush=True)
print(f"RE:  P={re_text['precision']:.4f} R={re_text['recall']:.4f} F1={re_text['f1']:.4f} (tp={re_text['tp']}, fp={re_text['fp']}, fn={re_text['fn']})", flush=True)

# Count parse failures
parse_failures = sum(1 for p in predictions if not p['entities'] and not p['relations'])
print(f"\nParse failures (empty output): {parse_failures}/{len(predictions)}", flush=True)

# Check offset errors
offset_correct = 0
offset_total = 0
for pred, inst in zip(predictions, instances):
    text = inst['text']
    for e in pred.get('entities', []):
        offset_total += 1
        if e['end'] <= len(text) and text[e['start']:e['end']] == e['text']:
            offset_correct += 1

print(f"Offset accuracy: {offset_correct}/{offset_total} ({100*offset_correct/offset_total:.1f}%)" if offset_total > 0 else "No entities predicted", flush=True)

# Gate 0 judgment
ner_f1_pct = ner_metrics['f1'] * 100
ner_text_f1_pct = ner_text['f1'] * 100
print(f"\nGate 0 (strict): NER F1 = {ner_f1_pct:.1f}% (threshold: 73%) -> {'PASS' if ner_f1_pct >= 73 else 'FAIL'}", flush=True)
print(f"Gate 0 (text):   NER F1 = {ner_text_f1_pct:.1f}% (threshold: 73%) -> {'PASS' if ner_text_f1_pct >= 73 else 'FAIL'}", flush=True)

os.makedirs("/root/autodl-tmp/struct_self_consist_ie/output", exist_ok=True)
results = {
    "ner_strict": ner_metrics,
    "re_strict": re_metrics,
    "ner_text_match": ner_text,
    "re_text_match": re_text,
    "offset_accuracy": offset_correct / offset_total if offset_total > 0 else 0,
    "parse_failures": parse_failures,
    "gate0_pass_strict": ner_f1_pct >= 73,
    "gate0_pass_text": ner_text_f1_pct >= 73,
    "num_instances": len(instances),
}
with open("/root/autodl-tmp/struct_self_consist_ie/output/gate0_results.json", "w") as f:
    json.dump(results, f, indent=2)

# Save all predictions for further analysis
all_preds = []
for i, (pred, inst, raw) in enumerate(zip(predictions, instances, raw_outputs)):
    all_preds.append({
        "id": inst.get("id", str(i)),
        "text": inst["text"],
        "gold": golds[i],
        "pred": pred,
        "raw_output": raw,
    })
with open("/root/autodl-tmp/struct_self_consist_ie/output/gate0_all_predictions.jsonl", "w") as f:
    for p in all_preds:
        f.write(json.dumps(p, ensure_ascii=False) + "\n")

print(f"\nResults saved.", flush=True)
print("Done.", flush=True)
