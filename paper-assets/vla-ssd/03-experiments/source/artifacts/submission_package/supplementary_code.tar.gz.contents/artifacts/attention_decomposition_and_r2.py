#!/usr/bin/env python3
# --- Path configuration (set env vars to override defaults) ---
import os as _os
PROJECT_ROOT = _os.environ.get("VLA_SSD_ROOT", ".")
LIBERO_ROOT = _os.environ.get("LIBERO_ROOT", "./LIBERO")
# ---
import json
import numpy as np

RESULTS_DIR = f"{PROJECT_ROOT}/results"

# ============================================================
# B2: Attention Decomposition
# ============================================================

CONTROL_HEADS = [3, 5, 6, 9, 13, 21, 24, 28]
ALL_HEADS = list(range(32))
INSTRUCTION_DOMINANT_HEADS = [h for h in ALL_HEADS if h not in CONTROL_HEADS]

with open(f"{RESULTS_DIR}/attention/l1_attention_trained_summary.json") as f:
    trained_samples = json.load(f)

n_samples = len(trained_samples)
per_head_bos = np.zeros(32)
per_head_image = np.zeros(32)
per_head_text = np.zeros(32)

for sample in trained_samples:
    per_head_bos += np.array(sample["per_head_attn_to_bos"])
    per_head_image += np.array(sample["per_head_attn_to_image"])
    per_head_text += np.array(sample["per_head_attn_to_text"])

per_head_bos /= n_samples
per_head_image /= n_samples
per_head_text /= n_samples

per_head_fractions = {}
for h in range(32):
    per_head_fractions[f"head_{h}"] = {
        "instruction": round(float(per_head_text[h]), 4),
        "vision": round(float(per_head_image[h]), 4),
        "bos_sink": round(float(per_head_bos[h]), 4)
    }

instr_dom_instruction = np.mean([per_head_text[h] for h in INSTRUCTION_DOMINANT_HEADS])
instr_dom_vision = np.mean([per_head_image[h] for h in INSTRUCTION_DOMINANT_HEADS])
instr_dom_bos = np.mean([per_head_bos[h] for h in INSTRUCTION_DOMINANT_HEADS])

ctrl_instruction = np.mean([per_head_text[h] for h in CONTROL_HEADS])
ctrl_vision = np.mean([per_head_image[h] for h in CONTROL_HEADS])
ctrl_bos = np.mean([per_head_bos[h] for h in CONTROL_HEADS])

with open(f"{RESULTS_DIR}/attention/l1_attention_untrained_summary.json") as f:
    untrained_data = json.load(f)

untrained_per_head = {}
for h in range(32):
    hkey = f"head_{h}"
    untrained_per_head[hkey] = {
        "instruction": round(untrained_data["per_head"][hkey]["mean_instr_attn"], 4),
        "vision": round(untrained_data["per_head"][hkey]["mean_image_attn"], 4)
    }

untrained_instr_dom_instruction = np.mean([untrained_data["per_head"][f"head_{h}"]["mean_instr_attn"] for h in INSTRUCTION_DOMINANT_HEADS])
untrained_instr_dom_vision = np.mean([untrained_data["per_head"][f"head_{h}"]["mean_image_attn"] for h in INSTRUCTION_DOMINANT_HEADS])
untrained_ctrl_instruction = np.mean([untrained_data["per_head"][f"head_{h}"]["mean_instr_attn"] for h in CONTROL_HEADS])
untrained_ctrl_vision = np.mean([untrained_data["per_head"][f"head_{h}"]["mean_image_attn"] for h in CONTROL_HEADS])

attention_result = {
    "method": "attention_decomposition",
    "layer": 1,
    "n_samples_trained": n_samples,
    "token_groups": {
        "instruction": "text instruction tokens",
        "vision": "image patch tokens (256 SigLIP patches)",
        "bos_sink": "BOS token (attention sink)"
    },
    "trained": {
        "per_head_attention_fractions": per_head_fractions,
        "group_summary": {
            "instruction_dominant_24": {
                "instruction": round(float(instr_dom_instruction), 4),
                "vision": round(float(instr_dom_vision), 4),
                "bos_sink": round(float(instr_dom_bos), 4)
            },
            "control_8": {
                "instruction": round(float(ctrl_instruction), 4),
                "vision": round(float(ctrl_vision), 4),
                "bos_sink": round(float(ctrl_bos), 4)
            }
        },
        "instruction_dominant_vs_control_delta": {
            "instruction_delta": round(float(instr_dom_instruction - ctrl_instruction), 4),
            "vision_delta": round(float(instr_dom_vision - ctrl_vision), 4),
            "bos_sink_delta": round(float(instr_dom_bos - ctrl_bos), 4)
        }
    },
    "untrained": {
        "per_head_attention_fractions": untrained_per_head,
        "group_summary": {
            "instruction_dominant_24": {
                "instruction": round(float(untrained_instr_dom_instruction), 4),
                "vision": round(float(untrained_instr_dom_vision), 4)
            },
            "control_8": {
                "instruction": round(float(untrained_ctrl_instruction), 4),
                "vision": round(float(untrained_ctrl_vision), 4)
            }
        }
    },
    "head_classification": {
        "instruction_dominant": INSTRUCTION_DOMINANT_HEADS,
        "control": CONTROL_HEADS
    },
    "key_findings": {
        "trained_instr_dom_heads_instruction_attn": round(float(instr_dom_instruction), 4),
        "trained_control_heads_instruction_attn": round(float(ctrl_instruction), 4),
        "trained_delta_instruction": round(float(instr_dom_instruction - ctrl_instruction), 4),
        "untrained_instr_dom_heads_instruction_attn": round(float(untrained_instr_dom_instruction), 4),
        "untrained_control_heads_instruction_attn": round(float(untrained_ctrl_instruction), 4),
        "training_effect_on_instr_dom_instruction_attn": round(float(instr_dom_instruction - untrained_instr_dom_instruction), 4),
        "training_effect_on_control_instruction_attn": round(float(ctrl_instruction - untrained_ctrl_instruction), 4)
    }
}

with open(f"{RESULTS_DIR}/attention_decomposition.json", "w") as f:
    json.dump(attention_result, f, indent=2)

print("=== B2: Attention Decomposition ===")
print(f"\nTrained model L1 attention (averaged over {n_samples} samples):")
print(f"  Instruction-dominant 24 heads:")
print(f"    instruction: {instr_dom_instruction:.4f}, vision: {instr_dom_vision:.4f}, bos: {instr_dom_bos:.4f}")
print(f"  Control 8 heads:")
print(f"    instruction: {ctrl_instruction:.4f}, vision: {ctrl_vision:.4f}, bos: {ctrl_bos:.4f}")
print(f"  Delta (instr_dom - control):")
print(f"    instruction: {instr_dom_instruction - ctrl_instruction:+.4f}")
print(f"    vision: {instr_dom_vision - ctrl_vision:+.4f}")
print(f"    bos: {instr_dom_bos - ctrl_bos:+.4f}")
print(f"\nUntrained model L1 attention:")
print(f"  Instruction-dominant 24 heads:")
print(f"    instruction: {untrained_instr_dom_instruction:.4f}, vision: {untrained_instr_dom_vision:.4f}")
print(f"  Control 8 heads:")
print(f"    instruction: {untrained_ctrl_instruction:.4f}, vision: {untrained_ctrl_vision:.4f}")
print(f"\nTraining effect on instruction attention:")
print(f"  Instr-dom heads: {untrained_instr_dom_instruction:.4f} -> {instr_dom_instruction:.4f} ({instr_dom_instruction - untrained_instr_dom_instruction:+.4f})")
print(f"  Control heads:   {untrained_ctrl_instruction:.4f} -> {ctrl_instruction:.4f} ({ctrl_instruction - untrained_ctrl_instruction:+.4f})")

# ============================================================
# B3: Per-task R2 Distribution
# ============================================================

with open(f"{RESULTS_DIR}/l1_head_ablation/action_probe_50demos.json") as f:
    probe_50d = json.load(f)

with open(f"{RESULTS_DIR}/l1_head_ablation/action_probe_results.json") as f:
    probe_5d = json.load(f)

with open(f"{RESULTS_DIR}/linear_probe_results.json") as f:
    linear_all = json.load(f)

with open(f"{RESULTS_DIR}/l1_head_ablation/action_probe_50demos_control8.json") as f:
    probe_ctrl8 = json.load(f)

tasks = [
    "open the middle drawer of the cabinet",
    "open the top drawer and put the bowl inside",
    "push the plate to the front of the stove",
    "put the bowl on the plate",
    "put the bowl on the stove",
    "put the bowl on top of the cabinet",
    "put the cream cheese in the bowl",
    "put the wine bottle on the rack",
    "put the wine bottle on top of the cabinet",
    "turn on the stove"
]

per_task_5d = {}
for condition in ["baseline", "ablate_all24", "ablate_all32"]:
    per_task_5d[condition] = {}
    for layer in ["L1", "L8", "L13"]:
        detail = probe_5d["detailed_results"][condition][layer]
        r2_vals = [detail["per_task_R2"][t] for t in tasks]
        per_task_5d[condition][layer] = {
            "per_task_R2": detail["per_task_R2"],
            "mean": round(float(np.mean(r2_vals)), 4),
            "std": round(float(np.std(r2_vals)), 4),
            "min": round(float(np.min(r2_vals)), 4),
            "max": round(float(np.max(r2_vals)), 4),
            "range": round(float(np.max(r2_vals) - np.min(r2_vals)), 4)
        }

per_task_diffs_50d = {}
for comparison in ["baseline_vs_ablate_all24", "baseline_vs_ablate_all32"]:
    per_task_diffs_50d[comparison] = {}
    for layer in ["L1", "L8", "L13"]:
        diffs = probe_50d["bootstrap_paired_CI"][comparison][layer]["per_task_diffs"]
        diff_vals = list(diffs.values())
        per_task_diffs_50d[comparison][layer] = {
            "per_task_diffs": diffs,
            "mean_delta": round(float(np.mean(diff_vals)), 4),
            "std_delta": round(float(np.std(diff_vals)), 4),
            "min_delta": round(float(np.min(diff_vals)), 4),
            "max_delta": round(float(np.max(diff_vals)), 4),
            "all_positive": all(d > 0 for d in diff_vals),
            "n_positive": sum(1 for d in diff_vals if d > 0),
            "n_negative": sum(1 for d in diff_vals if d < 0)
        }

ctrl8_per_task = {}
for layer in ["L1", "L8", "L13"]:
    detail = probe_ctrl8["detailed_results"]["ablate_control8"][layer]
    r2_vals = list(detail["per_task_R2"].values())
    ctrl8_per_task[layer] = {
        "per_task_R2": detail["per_task_R2"],
        "mean": round(float(np.mean(r2_vals)), 4),
        "std": round(float(np.std(r2_vals)), 4),
        "range": round(float(np.max(r2_vals) - np.min(r2_vals)), 4)
    }

linear_per_task = {}
for layer_idx in range(33):
    layer_key = f"layer_{layer_idx}"
    if layer_key in linear_all["trained"]["image_mean"]:
        r2_data = linear_all["trained"]["image_mean"][layer_key]["per_task_R2"]
        r2_vals = list(r2_data.values())
        linear_per_task[f"L{layer_idx}"] = {
            "mean": round(float(np.mean(r2_vals)), 4),
            "std": round(float(np.std(r2_vals)), 4),
            "min": round(float(np.min(r2_vals)), 4),
            "max": round(float(np.max(r2_vals)), 4),
            "range": round(float(np.max(r2_vals) - np.min(r2_vals)), 4),
            "cv": round(float(np.std(r2_vals) / np.mean(r2_vals)) if np.mean(r2_vals) > 0 else 0, 4)
        }

r2_result = {
    "method": "per_task_r2_distribution",
    "tasks": tasks,
    "n_tasks": 10,
    "mlp_probe_5demo": {
        "description": "MLP(4096,256,7) probe, 5 demos/task, per-task R2 distribution",
        "conditions": per_task_5d
    },
    "mlp_probe_50demo_ablation_diffs": {
        "description": "Per-task R2 deltas from 50-demo MLP probe ablation",
        "comparisons": per_task_diffs_50d
    },
    "control8_50demo": {
        "description": "50-demo MLP probe with control 8 heads ablated",
        "results": ctrl8_per_task
    },
    "linear_probe_all_layers": {
        "description": "Linear probe (image_mean readout) per-task R2 stats across 33 layers",
        "per_layer_stats": linear_per_task
    }
}

with open(f"{RESULTS_DIR}/per_task_r2_distribution.json", "w") as f:
    json.dump(r2_result, f, indent=2)

print("\n\n=== B3: Per-task R2 Distribution ===")
print("\n5-demo MLP probe baseline per-task R2:")
for layer in ["L1", "L8", "L13"]:
    stats = per_task_5d["baseline"][layer]
    print(f"  {layer}: mean={stats['mean']:.4f}, std={stats['std']:.4f}, range=[{stats['min']:.4f}, {stats['max']:.4f}]")

print("\n50-demo ablation per-task deltas (all24 vs baseline):")
for layer in ["L1", "L8", "L13"]:
    stats = per_task_diffs_50d["baseline_vs_ablate_all24"][layer]
    print(f"  {layer}: mean_delta={stats['mean_delta']:+.4f}, std={stats['std_delta']:.4f}, {stats['n_positive']}/10 positive")

print("\nLinear probe per-task variability (selected layers):")
for layer in ["L0", "L1", "L8", "L13", "L20", "L31"]:
    if layer in linear_per_task:
        s = linear_per_task[layer]
        print(f"  {layer}: mean={s['mean']:.4f}, std={s['std']:.4f}, CV={s['cv']:.4f}, range={s['range']:.4f}")

print(f"\nDone. Files saved:")
print(f"  {RESULTS_DIR}/attention_decomposition.json")
print(f"  {RESULTS_DIR}/per_task_r2_distribution.json")
