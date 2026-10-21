# --- Path configuration (set env vars to override defaults) ---
import os as _os
PROJECT_ROOT = _os.environ.get("VLA_SSD_ROOT", ".")
LIBERO_ROOT = _os.environ.get("LIBERO_ROOT", "./LIBERO")
# ---
import json
import math
import numpy as np

# --- Load data ---
decomp = json.load(open(f"{PROJECT_ROOT}/results/attention_decomposition.json"))
l1_summary = json.load(open(f"{PROJECT_ROOT}/results/attention/l1_attention_trained_summary.json"))
entropy_data = json.load(open(f"{PROJECT_ROOT}/results/attention/entropy_analysis.json"))

# --- Token counts ---
text_counts = []
for s in l1_summary:
    tr = s['token_regions']
    text_counts.append(tr['text'][1] - tr['text'][0])
n_text_avg = np.mean(text_counts)
n_image = 256
n_bos = 1

print(f"Token counts: n_text_avg={n_text_avg:.1f} (range {min(text_counts)}-{max(text_counts)}), n_image={n_image}, n_bos={n_bos}")

# --- Head classification ---
instr_dom_heads = decomp['head_classification']['instruction_dominant']
control_heads = decomp['head_classification']['control']

# --- Token-count normalization ---
results = {}

for condition in ['trained', 'untrained']:
    cond_data = decomp[condition]
    gs = cond_data['group_summary']

    for group_name, group_key in [('instruction_dominant_24', 'instruction_dominant_24'),
                                   ('control_8', 'control_8')]:
        g = gs[group_key]
        instr_attn = g.get('instruction', 0)
        vision_attn = g.get('vision', 0)
        bos_attn = g.get('bos_sink', 0)

        per_token_text = instr_attn / n_text_avg
        per_token_image = vision_attn / n_image
        ratio = per_token_text / per_token_image if per_token_image > 0 else float('inf')

        key = f"{condition}_{group_name}"
        results[key] = {
            'raw_text_attn': round(instr_attn, 4),
            'raw_image_attn': round(vision_attn, 4),
            'raw_bos_attn': round(bos_attn, 4),
            'n_text': float(n_text_avg),
            'n_image': n_image,
            'per_token_text': round(per_token_text, 6),
            'per_token_image': round(per_token_image, 6),
            'ratio_text_over_image': round(ratio, 1)
        }

# --- Per-head normalization ---
per_head_norm = {}
for condition in ['trained', 'untrained']:
    cond_data = decomp[condition]
    per_head = cond_data['per_head_attention_fractions']
    per_head_norm[condition] = {}

    for head_idx in range(32):
        h = per_head[f'head_{head_idx}']
        instr_attn = h.get('instruction', 0)
        vision_attn = h.get('vision', 0)
        pt_text = instr_attn / n_text_avg
        pt_image = vision_attn / n_image
        ratio = pt_text / pt_image if pt_image > 0 else float('inf')

        group = 'instr_dom' if head_idx in instr_dom_heads else 'control'
        per_head_norm[condition][f'head_{head_idx}'] = {
            'group': group,
            'raw_text': round(instr_attn, 4),
            'raw_image': round(vision_attn, 4),
            'per_token_text': round(pt_text, 6),
            'per_token_image': round(pt_image, 6),
            'ratio': round(ratio, 1)
        }

# --- Entropy by head group ---
trained_2cat_entropy = entropy_data['two_category_comparison']['trained']['per_head_entropy']
untrained_2cat_entropy = entropy_data['two_category_comparison']['untrained']['per_head_entropy']
trained_3cat_entropy = entropy_data['three_category_trained_only']['per_head_entropy']

entropy_by_group = {}
for condition_name, entropy_list in [('trained_2cat', trained_2cat_entropy),
                                      ('untrained_2cat', untrained_2cat_entropy),
                                      ('trained_3cat', trained_3cat_entropy)]:
    instr_dom_vals = [entropy_list[i] for i in instr_dom_heads]
    control_vals = [entropy_list[i] for i in control_heads]

    entropy_by_group[condition_name] = {
        'instruction_dominant_24': {
            'mean': float(np.mean(instr_dom_vals)),
            'std': float(np.std(instr_dom_vals)),
        },
        'control_8': {
            'mean': float(np.mean(control_vals)),
            'std': float(np.std(control_vals)),
        }
    }

# --- Compile output ---
output = {
    'method': 'attention_token_count_normalization_and_entropy',
    'layer': 1,
    'token_counts': {
        'n_text_avg': float(n_text_avg),
        'n_text_range': [int(min(text_counts)), int(max(text_counts))],
        'n_text_per_task': {l1_summary[i]['instruction']: int(text_counts[i]) for i in range(len(l1_summary))},
        'n_image': n_image,
        'n_bos': n_bos,
        'asymmetry_ratio': round(float(n_image / n_text_avg), 1)
    },
    'token_count_normalization': {
        k: v for k, v in results.items()
    },
    'per_head_normalization': per_head_norm,
    'entropy_by_head_group': entropy_by_group,
    'max_entropy': entropy_data['max_entropy']
}

# --- Save ---
out_path = f"{PROJECT_ROOT}/results/attention_normalization_entropy.json"
with open(out_path, 'w') as f:
    json.dump(output, f, indent=2)
print(f"\nSaved to {out_path}")

# --- Print tables ---
print("\n## Token-Count Normalization")
print("| Condition | Group | Text attn (raw) | Image attn (raw) | n_text | n_image | Per-token text | Per-token image | Ratio (text/image) |")
print("|---|---|---|---|---|---|---|---|---|")
for key in ['trained_instruction_dominant_24', 'trained_control_8', 'untrained_instruction_dominant_24', 'untrained_control_8']:
    r = results[key]
    cond = key.split('_')[0]
    group = '_'.join(key.split('_')[1:]).replace('_', ' ')
    print(f"| {cond} | {group} | {r['raw_text_attn']:.4f} | {r['raw_image_attn']:.4f} | {r['n_text']:.1f} | {r['n_image']} | {r['per_token_text']:.6f} | {r['per_token_image']:.6f} | {r['ratio_text_over_image']:.1f}x |")

print("\n## Attention Entropy by Head Group")
print("| Condition | Group | Mean entropy | Std | Max possible | Normalized |")
print("|---|---|---|---|---|---|")
for cond_name, groups in entropy_by_group.items():
    if '2cat' in cond_name:
        max_e = entropy_data['max_entropy']['2_categories_ln2']
    else:
        max_e = entropy_data['max_entropy']['3_categories_ln3']
    for group_name, data in groups.items():
        norm = data['mean'] / max_e
        print(f"| {cond_name} | {group_name} | {data['mean']:.4f} | {data['std']:.4f} | {max_e:.4f} | {norm:.4f} |")

# Summary
print("\n## Key Findings")
t_id = results['trained_instruction_dominant_24']
t_c = results['trained_control_8']
u_id = results['untrained_instruction_dominant_24']
u_c = results['untrained_control_8']
asym = n_image / n_text_avg
print(f"- Token asymmetry: {n_image}/{n_text_avg:.1f} = {asym:.1f}x more image tokens than text tokens")
print(f"- Trained instr-dom heads: {t_id['ratio_text_over_image']:.1f}x per-token text/image ratio")
print(f"- Trained control heads: {t_c['ratio_text_over_image']:.1f}x per-token text/image ratio")
print(f"- Untrained instr-dom heads: {u_id['ratio_text_over_image']:.1f}x per-token text/image ratio")
print(f"- Untrained control heads: {u_c['ratio_text_over_image']:.1f}x per-token text/image ratio")
print(f"- Even after normalizing for {asym:.1f}x token count asymmetry, trained instr-dom heads show {t_id['ratio_text_over_image']:.1f}x per-token preference for text")
print(f"- Training amplifies ratio from {u_id['ratio_text_over_image']:.1f}x to {t_id['ratio_text_over_image']:.1f}x ({t_id['ratio_text_over_image']/u_id['ratio_text_over_image']:.1f}x increase)")
