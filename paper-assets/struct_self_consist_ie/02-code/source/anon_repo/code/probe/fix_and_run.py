#!/usr/bin/env python3
"""Fix entity matching from span-based to text-based and rerun probes."""

import re

PROBE_PATH = "/root/autodl-tmp/struct_self_consist_ie/code/probe/hidden_state_probe.py"
EXTRACT_PATH = "/root/autodl-tmp/struct_self_consist_ie/code/probe/extract_hidden_states.py"

# --- Fix 1: entity_set in both files ---
old_entity_set = 'return {(e["start"], e["end"], e["type"]) for e in ext.get("entities", [])}'
new_entity_set = 'return {(e["text"], e["type"]) for e in ext.get("entities", [])}'

for path in [PROBE_PATH, EXTRACT_PATH]:
    with open(path) as f:
        content = f.read()
    if old_entity_set in content:
        content = content.replace(old_entity_set, new_entity_set)
        with open(path, "w") as f:
            f.write(content)
        print(f"Fixed entity_set in {path}")
    else:
        print(f"entity_set already fixed or not found in {path}")

# --- Fix 2: Recompute labels and remove DeBERTa in hidden_state_probe.py ---
with open(PROBE_PATH) as f:
    content = f.read()

# Remove DeBERTa hardcoded block from results dict
deberta_block = '''            "deberta": {
                "rho": 0.329,
                "sel_f1": 0.6114,
                "gap_closure": -26.5,
            },'''
content = content.replace(deberta_block, "")

# Remove DeBERTa print line
deberta_print = """    print(f"{'DeBERTa':<20} {'768':>5} {'0.3290':>12} {'0.6114':>14} {'-26.5':>12}%")"""
content = content.replace(deberta_print, "")

# Replace labels loading with recomputation from JSONL
old_load = '''    print("Loading hidden states and labels...")
    hidden_states = torch.load(os.path.join(DATA_DIR, "hidden_states.pt"), weights_only=True).numpy()
    labels = torch.load(os.path.join(DATA_DIR, "labels.pt"), weights_only=True).numpy()
    logprobs = torch.load(os.path.join(DATA_DIR, "logprobs.pt"), weights_only=True).numpy()

    print(f"  hidden_states: {hidden_states.shape}")
    print(f"  labels: {labels.shape}")'''

new_load = '''    print("Loading hidden states...")
    hidden_states = torch.load(os.path.join(DATA_DIR, "hidden_states.pt"), weights_only=True).numpy()
    logprobs = torch.load(os.path.join(DATA_DIR, "logprobs.pt"), weights_only=True).numpy()

    print(f"  hidden_states: {hidden_states.shape}")

    print("Recomputing labels with text-based entity matching...")
    with open(SAMPLES_PATH) as f:
        all_instances_raw = [json.loads(line) for line in f if line.strip()]
    labels = np.array([
        compute_ner_f1(s, inst["gold"])
        for inst in all_instances_raw
        for s in inst["samples"]
    ])
    print(f"  labels recomputed: {labels.shape}, range [{labels.min():.3f}, {labels.max():.3f}]")'''

content = content.replace(old_load, new_load)

# Update output path to save text-based results
old_output = 'output_path = os.path.join(DATA_DIR, "results.json")'
new_output = 'output_path = os.path.join(DATA_DIR, "results_textbased_goldfiltered.json")'
content = content.replace(old_output, new_output)

# Add matching_type to results
old_results_dataset = '"dataset": "SciERC"'
new_results_dataset = '"dataset": "SciERC",\n        "matching_type": "text-based"'
content = content.replace(old_results_dataset, new_results_dataset)

with open(PROBE_PATH, "w") as f:
    f.write(content)

print("Fixed hidden_state_probe.py: recompute labels, removed DeBERTa, text-based output")

# Verify
with open(PROBE_PATH) as f:
    final = f.read()
assert 'e["text"]' in final, "text-based fix not applied"
assert "deberta" not in final.lower(), "DeBERTa not removed"
assert "results_textbased_goldfiltered" in final, "output path not updated"
assert "Recomputing labels" in final, "label recomputation not added"
print("\nAll fixes verified. Ready to run.")
