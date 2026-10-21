"""Dual-metric (binary_correct vs text_exact_match) deep analysis."""
import json
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
from pathlib import Path

OUT = Path("/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/analysis")
OUT.mkdir(parents=True, exist_ok=True)

# ── Load variance components ──
vc_binary = {
    "precision:temperature": {"pct": 0.0017},
    "precision:prompt_template": {"pct": 0.0196},
    "precision:seed": {"pct": 0.0},
    "precision:ordering": {"pct": 0.0},
    "precision:item_id": {"pct": 7.2432},
    "temperature:prompt_template": {"pct": 0.0049},
    "temperature:seed": {"pct": 0.0387},
    "temperature:ordering": {"pct": 0.0185},
    "temperature:item_id": {"pct": 6.8495},
    "prompt_template:seed": {"pct": 0.0},
    "prompt_template:ordering": {"pct": 0.0103},
    "prompt_template:item_id": {"pct": 5.7342},
    "seed:ordering": {"pct": 0.0},
    "seed:item_id": {"pct": 2.6973},
    "ordering:item_id": {"pct": 0.4438},
    "precision": {"pct": 0.8725},
    "temperature": {"pct": 0.0},
    "prompt_template": {"pct": 0.0310},
    "seed": {"pct": 0.0},
    "ordering": {"pct": 0.0},
    "item_id": {"pct": 58.4405},
    "residual": {"pct": 17.5944},
}

vc_text = {
    "precision:temperature": {"pct": 1.2611},
    "precision:prompt_template": {"pct": 0.0128},
    "precision:seed": {"pct": 0.0},
    "precision:ordering": {"pct": 0.0207},
    "precision:item_id": {"pct": 0.6281},
    "temperature:prompt_template": {"pct": 0.2423},
    "temperature:seed": {"pct": 0.0},
    "temperature:ordering": {"pct": 0.0},
    "temperature:item_id": {"pct": 2.4724},
    "prompt_template:seed": {"pct": 0.0},
    "prompt_template:ordering": {"pct": 0.0736},
    "prompt_template:item_id": {"pct": 37.4576},
    "seed:ordering": {"pct": 0.0},
    "seed:item_id": {"pct": 0.0},
    "ordering:item_id": {"pct": 0.2999},
    "precision": {"pct": 0.0},
    "temperature": {"pct": 16.8614},
    "prompt_template": {"pct": 0.0},
    "seed": {"pct": 0.0},
    "ordering": {"pct": 0.0},
    "item_id": {"pct": 0.0},
    "residual": {"pct": 40.6701},
}

# ── Item-level data ──
item_data = [
    {"item_id":"abstract_algebra_13","subject":"abstract_algebra","bc_mean":0.287,"tem_mean":0.139},
    {"item_id":"abstract_algebra_14","subject":"abstract_algebra","bc_mean":0.361,"tem_mean":0.093},
    {"item_id":"abstract_algebra_17","subject":"abstract_algebra","bc_mean":0.500,"tem_mean":0.093},
    {"item_id":"abstract_algebra_28","subject":"abstract_algebra","bc_mean":0.130,"tem_mean":0.093},
    {"item_id":"abstract_algebra_3","subject":"abstract_algebra","bc_mean":0.000,"tem_mean":0.176},
    {"item_id":"abstract_algebra_31","subject":"abstract_algebra","bc_mean":0.991,"tem_mean":0.102},
    {"item_id":"abstract_algebra_35","subject":"abstract_algebra","bc_mean":0.620,"tem_mean":0.083},
    {"item_id":"abstract_algebra_81","subject":"abstract_algebra","bc_mean":0.000,"tem_mean":0.157},
    {"item_id":"abstract_algebra_86","subject":"abstract_algebra","bc_mean":0.056,"tem_mean":0.102},
    {"item_id":"abstract_algebra_94","subject":"abstract_algebra","bc_mean":0.056,"tem_mean":0.083},
    {"item_id":"college_physics_11","subject":"college_physics","bc_mean":0.000,"tem_mean":0.250},
    {"item_id":"college_physics_27","subject":"college_physics","bc_mean":0.306,"tem_mean":0.111},
    {"item_id":"college_physics_29","subject":"college_physics","bc_mean":0.000,"tem_mean":0.185},
    {"item_id":"college_physics_3","subject":"college_physics","bc_mean":0.981,"tem_mean":0.167},
    {"item_id":"college_physics_4","subject":"college_physics","bc_mean":0.685,"tem_mean":0.167},
    {"item_id":"college_physics_54","subject":"college_physics","bc_mean":0.880,"tem_mean":0.167},
    {"item_id":"college_physics_64","subject":"college_physics","bc_mean":0.352,"tem_mean":0.167},
    {"item_id":"college_physics_69","subject":"college_physics","bc_mean":0.981,"tem_mean":0.167},
    {"item_id":"college_physics_75","subject":"college_physics","bc_mean":0.843,"tem_mean":0.139},
    {"item_id":"college_physics_94","subject":"college_physics","bc_mean":0.028,"tem_mean":0.167},
    {"item_id":"professional_medicine_135","subject":"professional_medicine","bc_mean":1.000,"tem_mean":0.102},
    {"item_id":"professional_medicine_176","subject":"professional_medicine","bc_mean":0.000,"tem_mean":0.139},
    {"item_id":"professional_medicine_183","subject":"professional_medicine","bc_mean":0.769,"tem_mean":0.056},
    {"item_id":"professional_medicine_193","subject":"professional_medicine","bc_mean":1.000,"tem_mean":0.083},
    {"item_id":"professional_medicine_194","subject":"professional_medicine","bc_mean":0.861,"tem_mean":0.139},
    {"item_id":"professional_medicine_22","subject":"professional_medicine","bc_mean":0.000,"tem_mean":0.167},
    {"item_id":"professional_medicine_235","subject":"professional_medicine","bc_mean":0.972,"tem_mean":0.139},
    {"item_id":"professional_medicine_40","subject":"professional_medicine","bc_mean":0.880,"tem_mean":0.120},
    {"item_id":"professional_medicine_49","subject":"professional_medicine","bc_mean":1.000,"tem_mean":0.074},
    {"item_id":"professional_medicine_55","subject":"professional_medicine","bc_mean":0.917,"tem_mean":0.148},
    {"item_id":"us_foreign_policy_17","subject":"us_foreign_policy","bc_mean":0.685,"tem_mean":0.139},
    {"item_id":"us_foreign_policy_27","subject":"us_foreign_policy","bc_mean":1.000,"tem_mean":0.102},
    {"item_id":"us_foreign_policy_4","subject":"us_foreign_policy","bc_mean":0.898,"tem_mean":0.093},
    {"item_id":"us_foreign_policy_54","subject":"us_foreign_policy","bc_mean":1.000,"tem_mean":0.111},
    {"item_id":"us_foreign_policy_66","subject":"us_foreign_policy","bc_mean":0.880,"tem_mean":0.148},
    {"item_id":"us_foreign_policy_7","subject":"us_foreign_policy","bc_mean":0.981,"tem_mean":0.185},
    {"item_id":"us_foreign_policy_73","subject":"us_foreign_policy","bc_mean":0.861,"tem_mean":0.083},
    {"item_id":"us_foreign_policy_82","subject":"us_foreign_policy","bc_mean":0.917,"tem_mean":0.130},
    {"item_id":"us_foreign_policy_88","subject":"us_foreign_policy","bc_mean":0.130,"tem_mean":0.111},
    {"item_id":"us_foreign_policy_97","subject":"us_foreign_policy","bc_mean":1.000,"tem_mean":0.111},
    {"item_id":"world_religions_101","subject":"world_religions","bc_mean":0.843,"tem_mean":0.148},
    {"item_id":"world_religions_114","subject":"world_religions","bc_mean":1.000,"tem_mean":0.130},
    {"item_id":"world_religions_136","subject":"world_religions","bc_mean":0.130,"tem_mean":0.111},
    {"item_id":"world_religions_143","subject":"world_religions","bc_mean":0.991,"tem_mean":0.148},
    {"item_id":"world_religions_150","subject":"world_religions","bc_mean":1.000,"tem_mean":0.120},
    {"item_id":"world_religions_154","subject":"world_religions","bc_mean":0.954,"tem_mean":0.167},
    {"item_id":"world_religions_166","subject":"world_religions","bc_mean":0.056,"tem_mean":0.139},
    {"item_id":"world_religions_50","subject":"world_religions","bc_mean":0.769,"tem_mean":0.139},
    {"item_id":"world_religions_56","subject":"world_religions","bc_mean":1.000,"tem_mean":0.167},
    {"item_id":"world_religions_6","subject":"world_religions","bc_mean":1.000,"tem_mean":0.111},
]
items_df = pd.DataFrame(item_data)

# ── Facet-level data ──
facet_data = {
    "precision": [
        {"level": "bfloat16", "bc_mean": 0.684, "tem_mean": 0.152},
        {"level": "float16", "bc_mean": 0.683, "tem_mean": 0.149},
        {"level": "float32", "bc_mean": 0.599, "tem_mean": 0.097},
    ],
    "temperature": [
        {"level": "0.0", "bc_mean": 0.643, "tem_mean": 0.247},
        {"level": "0.5", "bc_mean": 0.669, "tem_mean": 0.019},
    ],
    "prompt_template": [
        {"level": "1", "bc_mean": 0.663, "tem_mean": 0.142},
        {"level": "2", "bc_mean": 0.671, "tem_mean": 0.126},
        {"level": "3", "bc_mean": 0.633, "tem_mean": 0.131},
    ],
    "seed": [
        {"level": "42", "bc_mean": 0.661, "tem_mean": 0.132},
        {"level": "123", "bc_mean": 0.649, "tem_mean": 0.135},
        {"level": "456", "bc_mean": 0.658, "tem_mean": 0.132},
    ],
    "ordering": [
        {"level": "1", "bc_mean": 0.657, "tem_mean": 0.138},
        {"level": "2", "bc_mean": 0.654, "tem_mean": 0.128},
    ],
}

# ══════════════════════════════════════════════════════════════
# Figure 1: Stacked bar variance decomposition comparison
# ══════════════════════════════════════════════════════════════

plt.rcParams.update({
    'font.family': 'serif',
    'font.size': 10,
    'axes.linewidth': 0.8,
    'xtick.major.width': 0.6,
    'ytick.major.width': 0.6,
})

all_components = list(vc_binary.keys())
bc_vals = [vc_binary[c]["pct"] for c in all_components]
te_vals = [vc_text[c]["pct"] for c in all_components]

# Sort by binary_correct magnitude, take top 6
sorted_idx = np.argsort(bc_vals)[::-1]
top6_bc = [(all_components[i], bc_vals[i]) for i in sorted_idx[:6]]
other_bc = sum(bc_vals[i] for i in sorted_idx[6:])

# For text, use same top-6 from text perspective
sorted_idx_te = np.argsort(te_vals)[::-1]
top6_te = [(all_components[i], te_vals[i]) for i in sorted_idx_te[:6]]
other_te = sum(te_vals[i] for i in sorted_idx_te[6:])

# Union of top components from both metrics for consistent coloring
all_top = list(dict.fromkeys(
    [c for c, _ in top6_bc] + [c for c, _ in top6_te]
))

colors_map = {
    "item_id": "#2166ac",
    "residual": "#999999",
    "precision:item_id": "#67a9cf",
    "temperature:item_id": "#ef8a62",
    "prompt_template:item_id": "#d6604d",
    "seed:item_id": "#fddbc7",
    "precision": "#b2182b",
    "temperature": "#f4a582",
    "prompt_template:item_id": "#d6604d",
    "precision:temperature": "#92c5de",
    "ordering:item_id": "#4393c3",
}
cmap = plt.cm.Set2
for i, c in enumerate(all_top):
    if c not in colors_map:
        colors_map[c] = cmap(i / max(len(all_top), 1))

# Prepare stacked data for each metric
def prepare_stacked(vc_dict, top_components):
    vals = []
    labels = []
    other = 0
    used = set()
    for c in top_components:
        vals.append(vc_dict[c]["pct"])
        labels.append(c)
        used.add(c)
    for c in vc_dict:
        if c not in used:
            other += vc_dict[c]["pct"]
    if other > 0.01:
        vals.append(other)
        labels.append("other")
    return vals, labels

# Use union top components for BOTH bars
union_top = list(dict.fromkeys(
    [c for c, _ in sorted(top6_bc, key=lambda x: -x[1])] +
    [c for c, _ in sorted(top6_te, key=lambda x: -x[1])]
))

fig, ax = plt.subplots(figsize=(5, 6))
bar_width = 0.35
positions = [0, 0.5]

for idx, (vc_dict, label) in enumerate([(vc_binary, "binary_correct"), (vc_text, "text_exact_match")]):
    bottom = 0
    for comp in union_top:
        val = vc_dict[comp]["pct"]
        color = colors_map.get(comp, "#cccccc")
        bar = ax.bar(positions[idx], val, bar_width, bottom=bottom, color=color,
                     edgecolor='white', linewidth=0.3)
        if val > 3:
            ax.text(positions[idx], bottom + val/2, f"{val:.1f}%",
                    ha='center', va='center', fontsize=7, fontweight='bold')
        bottom += val
    # Other
    other_val = sum(v["pct"] for k, v in vc_dict.items() if k not in union_top)
    if other_val > 0.01:
        ax.bar(positions[idx], other_val, bar_width, bottom=bottom,
               color='#e0e0e0', edgecolor='white', linewidth=0.3)
        bottom += other_val

ax.set_xticks(positions)
ax.set_xticklabels(["binary_correct", "text_exact_match"], fontsize=9)
ax.set_ylabel("Variance explained (%)", fontsize=10)
ax.set_title("Variance Decomposition Comparison", fontsize=11, fontweight='bold')
ax.set_ylim(0, 105)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

# Legend
from matplotlib.patches import Patch
legend_elements = [Patch(facecolor=colors_map.get(c, "#cccccc"), label=c) for c in union_top]
legend_elements.append(Patch(facecolor='#e0e0e0', label='other'))
ax.legend(handles=legend_elements, loc='upper right', fontsize=7, frameon=False)

plt.tight_layout()
plt.savefig(OUT / "fig1_variance_decomposition_comparison.png", dpi=300, bbox_inches='tight')
plt.close()
print("Fig 1 saved.")

# ══════════════════════════════════════════════════════════════
# Figure 2: Item-level scatter plot
# ══════════════════════════════════════════════════════════════

fig, ax = plt.subplots(figsize=(6, 5))

subjects = items_df['subject'].unique()
subject_colors = {
    'abstract_algebra': '#e41a1c',
    'college_physics': '#377eb8',
    'professional_medicine': '#4daf4a',
    'us_foreign_policy': '#984ea3',
    'world_religions': '#ff7f00',
}
subject_labels = {
    'abstract_algebra': 'Abstract Algebra',
    'college_physics': 'College Physics',
    'professional_medicine': 'Prof. Medicine',
    'us_foreign_policy': 'US Foreign Policy',
    'world_religions': 'World Religions',
}

for subj in subjects:
    mask = items_df['subject'] == subj
    ax.scatter(
        items_df.loc[mask, 'bc_mean'],
        items_df.loc[mask, 'tem_mean'],
        c=subject_colors[subj],
        label=subject_labels[subj],
        s=50, alpha=0.8, edgecolors='white', linewidth=0.5
    )

from scipy.stats import spearmanr
rho, pval = spearmanr(items_df['bc_mean'], items_df['tem_mean'])
ax.text(0.03, 0.97, f"Spearman ρ = {rho:.3f}\np = {pval:.3f}",
        transform=ax.transAxes, fontsize=9, va='top',
        bbox=dict(boxstyle='round,pad=0.3', facecolor='white', edgecolor='gray', alpha=0.8))

ax.set_xlabel("binary_correct (mean across 108 conditions)", fontsize=10)
ax.set_ylabel("text_exact_match (mean across 108 conditions)", fontsize=10)
ax.set_title("Item-Level: Accuracy vs. Determinism", fontsize=11, fontweight='bold')
ax.legend(fontsize=8, frameon=False, loc='upper right')
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.set_xlim(-0.05, 1.05)
ax.set_ylim(-0.02, 0.30)

plt.tight_layout()
plt.savefig(OUT / "fig2_item_scatter.png", dpi=300, bbox_inches='tight')
plt.close()
print("Fig 2 saved.")

# ══════════════════════════════════════════════════════════════
# Figure 3: Facet effect heatmap
# ══════════════════════════════════════════════════════════════

rows = []
row_labels = []
for facet_name in ["precision", "temperature", "prompt_template", "seed", "ordering"]:
    for entry in facet_data[facet_name]:
        row_labels.append(f"{facet_name}={entry['level']}")
        rows.append([entry['bc_mean'], entry['tem_mean']])

heatmap_data = np.array(rows)

fig, ax = plt.subplots(figsize=(4, 6))
im = ax.imshow(heatmap_data, cmap='RdYlBu_r', aspect='auto', vmin=0, vmax=1)

ax.set_xticks([0, 1])
ax.set_xticklabels(["binary_correct", "text_exact_match"], fontsize=9, rotation=20, ha='right')
ax.set_yticks(range(len(row_labels)))
ax.set_yticklabels(row_labels, fontsize=8)

for i in range(len(row_labels)):
    for j in range(2):
        val = heatmap_data[i, j]
        color = 'white' if val > 0.5 else 'black'
        ax.text(j, i, f"{val:.3f}", ha='center', va='center', fontsize=8, color=color, fontweight='bold')

# Add horizontal separators between facets
sep_positions = [9.5, 11.5, 14.5, 17.5]  # between groups
facet_boundaries = []
pos = 0
for facet_name in ["precision", "temperature", "prompt_template", "seed", "ordering"]:
    n = len(facet_data[facet_name])
    pos += n
    facet_boundaries.append(pos - 0.5)
for b in facet_boundaries[:-1]:
    ax.axhline(y=b, color='black', linewidth=1.5)

ax.set_title("Facet-Level Mean by Metric", fontsize=11, fontweight='bold')
cbar = plt.colorbar(im, ax=ax, fraction=0.05, pad=0.04)
cbar.set_label("Mean score", fontsize=9)

ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

plt.tight_layout()
plt.savefig(OUT / "fig3_facet_heatmap.png", dpi=300, bbox_inches='tight')
plt.close()
print("Fig 3 saved.")

print("All figures generated.")
