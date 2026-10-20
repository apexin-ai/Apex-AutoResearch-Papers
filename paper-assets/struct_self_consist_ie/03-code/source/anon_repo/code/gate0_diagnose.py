"""Diagnose Gate 0 results: compute text-level match F1 alongside strict match."""
import sys
sys.path.insert(0, '/root/autodl-tmp/struct_self_consist_ie/code')

import json
from data_utils import load_uie_jsonl
from sampling import build_uie_prompt, parse_extraction_output, SCIERC_SCHEMA_HINT
from evaluation import compute_ner_f1, compute_re_f1

# Load the raw vLLM outputs to get predictions
# We need to regenerate predictions from the outputs
# But since we saved gate0_samples.json only for 5 instances,
# let's load the full outputs

# Actually, let's just load test data and the saved predictions
# We'll need to re-parse... but we don't have the raw outputs saved.
# Instead, let's compute text-level match on the existing predictions.

# Load test data
instances = load_uie_jsonl('/root/autodl-tmp/struct_self_consist_ie/data/test.jsonl')

# Load the raw vLLM output texts we need to save them
# Since we don't have them, let's compute text-based match from
# what we can reconstruct.

# For a proper diagnostic, load the gate0 outputs
# The vLLM generate outputs were parsed already - we need the parsed predictions.
# Let's write a simpler approach: use the saved predictions from the JSON file.

# Actually let me just recompute with text-based matching
# We need the predictions. Since the model was killed and outputs not saved,
# let me re-run with output saving.
# But actually the gate0_eval.py already ran successfully.
# The issue is we only saved 5 samples. Let me compute text-level metrics.

# Approach: save all predictions during the next run.
# For now, let's analyze what we have.

# Compute how many entities have text match vs offset match
# from the 5 saved samples
with open('/root/autodl-tmp/struct_self_consist_ie/output/gate0_samples.json') as f:
    samples = json.load(f)

# Count text-match vs strict-match across samples
text_match_tp = text_match_fp = text_match_fn = 0
strict_tp = strict_fp = strict_fn = 0
offset_errors = []

for s in samples:
    gold_ents = s['gold']['entities']
    pred_ents = s['pred']['entities']
    
    # Strict match
    gold_set = {(e['start'], e['end'], e['type']) for e in gold_ents}
    pred_set = {(e['start'], e['end'], e['type']) for e in pred_ents}
    strict_tp += len(gold_set & pred_set)
    strict_fp += len(pred_set - gold_set)
    strict_fn += len(gold_set - pred_set)
    
    # Text match (text + type only)
    gold_text_set = {(e['text'].strip(), e['type']) for e in gold_ents}
    pred_text_set = {(e['text'].strip(), e['type']) for e in pred_ents}
    text_match_tp += len(gold_text_set & pred_text_set)
    text_match_fp += len(pred_text_set - gold_text_set)
    text_match_fn += len(gold_text_set - pred_text_set)

def prf(tp, fp, fn):
    p = tp / (tp + fp) if (tp + fp) > 0 else 0
    r = tp / (tp + fn) if (tp + fn) > 0 else 0
    f1 = 2*p*r/(p+r) if (p+r) > 0 else 0
    return p, r, f1

sp, sr, sf1 = prf(strict_tp, strict_fp, strict_fn)
tp, tr, tf1 = prf(text_match_tp, text_match_fp, text_match_fn)

print(f"=== NER Evaluation (5 samples) ===")
print(f"Strict match:  P={sp:.4f} R={sr:.4f} F1={sf1:.4f}  (tp={strict_tp}, fp={strict_fp}, fn={strict_fn})")
print(f"Text match:    P={tp:.4f} R={tr:.4f} F1={tf1:.4f}  (tp={text_match_tp}, fp={text_match_fp}, fn={text_match_fn})")

# Check offset patterns
print(f"\n=== Offset Error Analysis ===")
for s in samples[:3]:
    text = s['text']
    for pe in s['pred']['entities']:
        claimed = pe['text']
        actual_at_offset = text[pe['start']:pe['end']] if pe['end'] <= len(text) else "OOB"
        if claimed != actual_at_offset:
            # Find where the claimed text actually is
            idx = text.find(claimed)
            if idx >= 0:
                print(f"  claimed='{claimed}' at [{pe['start']}:{pe['end']}], actual location=[{idx}:{idx+len(claimed)}], delta_start={pe['start']-idx}, delta_end={pe['end']-(idx+len(claimed))}")
            else:
                print(f"  claimed='{claimed}' at [{pe['start']}:{pe['end']}], NOT FOUND in text")
