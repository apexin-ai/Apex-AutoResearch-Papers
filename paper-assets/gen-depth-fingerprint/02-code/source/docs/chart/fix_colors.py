"""Regenerate Figures 16, 17, 18 with refined academic color palette."""
import matplotlib
matplotlib.use('Agg')
matplotlib.rcParams['pdf.fonttype'] = 42
matplotlib.rcParams['ps.fonttype'] = 42
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.lines import Line2D

plt.rcParams.update({
    'font.family': 'serif',
    'font.serif': ['Times New Roman', 'DejaVu Serif'],
    'font.size': 9,
    'axes.labelsize': 10,
    'axes.titlesize': 10,
    'xtick.labelsize': 8,
    'ytick.labelsize': 8,
    'legend.fontsize': 7.5,
    'figure.dpi': 300,
    'savefig.dpi': 300,
    'savefig.bbox': 'tight',
    'savefig.pad_inches': 0.02,
    'axes.spines.top': False,
    'axes.spines.right': False,
    'mathtext.fontset': 'cm',
})

# Unified DDR zone palette (ColorBrewer-inspired, matches TOST heatmap)
C_DRIFT = '#D6604D'    # warm red
C_INTERM = '#7570B3'   # muted purple
C_STAT = '#4393C3'     # cool blue

# ━━━━━━━━━━ Figure 16: DDR Scatter ━━━━━━━━━━
fig, ax = plt.subplots(figsize=(3.3, 2.8))

features_scatter = [
    ('hapax',        0.64, 0.76, 'drifting',      'o'),
    ('TTR',          0.63, 0.88, 'drifting',      'o'),
    (r'$\bar{H}$',  0.60, 1.17, 'drifting',      'o'),
    (r'$\sigma_H$', 0.16, 0.55, 'intermediate',  's'),
    (r'$H_{\min}$', 0.40, 0.03, 'stationary',    'D'),
    (r'$H_{\max}$', 0.05, 0.08, 'stationary',    'o'),
    ('tail',         0.04, 0.08, 'stationary',    'o'),
]

zone_color = {'drifting': C_DRIFT, 'intermediate': C_INTERM, 'stationary': C_STAT}
zone_label = {'drifting': 'Drifting', 'intermediate': 'Intermediate', 'stationary': 'Near-stationary'}

offsets = {
    'hapax':        ( 4,  -8),
    'TTR':          ( 4,   5),
    r'$\bar{H}$':  ( 4,  -8),
    r'$\sigma_H$': ( 4,   5),
    r'$H_{\min}$': (-35, -10),
    r'$H_{\max}$': ( 4,   5),
    'tail':         ( 4,  -8),
}

ax.axvline(x=0.30, color='#888888', linestyle='--', linewidth=0.7, alpha=0.5)
ax.axhline(y=0.20, color='#888888', linestyle='--', linewidth=0.7, alpha=0.5)

for name, rho, d, zone, mk in features_scatter:
    c = zone_color[zone]
    ax.scatter(rho, d, c=c, marker=mk, s=60, edgecolors='#333333', linewidths=0.4, zorder=5)
    ox, oy = offsets.get(name, (4, 5))
    ax.annotate(name, (rho, d), fontsize=7, xytext=(ox, oy),
                textcoords='offset points', color='#333333')

legend_handles = [
    Line2D([0],[0], marker='o', color='w', markerfacecolor=C_DRIFT, markersize=7,
           markeredgecolor='#333333', markeredgewidth=0.4, label='Drifting'),
    Line2D([0],[0], marker='s', color='w', markerfacecolor=C_INTERM, markersize=7,
           markeredgecolor='#333333', markeredgewidth=0.4, label='Intermediate'),
    Line2D([0],[0], marker='D', color='w', markerfacecolor=C_STAT, markersize=6,
           markeredgecolor='#333333', markeredgewidth=0.4, label='Near-stationary'),
]
ax.legend(handles=legend_handles, loc='upper left', framealpha=0.9, edgecolor='#CCCCCC',
          fontsize=7, handletextpad=0.3)
ax.set_xlabel(r'$|\rho|$ (Spearman, pooled cross-generator)')
ax.set_ylabel(r"Cohen's $d$ (gen-1 vs. gen-2+)")
ax.set_xlim(-0.03, 0.75)
ax.set_ylim(-0.05, 1.35)

plt.tight_layout()
plt.savefig('fig_ddr_scatter.pdf')
plt.savefig('fig_ddr_scatter.png')
plt.close()
print("OK fig_ddr_scatter")


# ━━━━━━━━━━ Figure 17: Holdout Split Validation ━━━━━━━━━━
rho_data = {
    "pythia-1b": {"entropy_mean": -0.712, "entropy_std": -0.2414, "entropy_min": -0.5051, "entropy_max": 0.0048, "tail_decay": 0.0904, "ttr": -0.6568, "hapax_ratio": -0.6741},
    "pythia-2.8b": {"entropy_mean": -0.6754, "entropy_std": -0.153, "entropy_min": -0.4797, "entropy_max": -0.0351, "tail_decay": 0.0633, "ttr": -0.6333, "hapax_ratio": -0.6553},
    "olmo-2-1b": {"entropy_mean": -0.6386, "entropy_std": -0.2958, "entropy_min": -0.3874, "entropy_max": 0.0672, "tail_decay": -0.1411, "ttr": -0.6996, "hapax_ratio": -0.7124},
    "qwen3-0.6b": {"entropy_mean": -0.5656, "entropy_std": -0.2294, "entropy_min": -0.3587, "entropy_max": 0.0857, "tail_decay": -0.0902, "ttr": -0.6111, "hapax_ratio": -0.6273},
    "qwen3-1.7b": {"entropy_mean": -0.6022, "entropy_std": -0.1882, "entropy_min": -0.4062, "entropy_max": 0.0884, "tail_decay": -0.0698, "ttr": -0.6523, "hapax_ratio": -0.6696},
    "qwen3-8b": {"entropy_mean": -0.4754, "entropy_std": -0.0755, "entropy_min": -0.3029, "entropy_max": 0.0946, "tail_decay": -0.0894, "ttr": -0.5419, "hapax_ratio": -0.5578},
    "llama-3.2-3b": {"entropy_mean": -0.5687, "entropy_std": -0.2826, "entropy_min": -0.2834, "entropy_max": -0.0187, "tail_decay": -0.066, "ttr": -0.5425, "hapax_ratio": -0.5532},
    "mistral-7b-v0.3": {"entropy_mean": -0.4814, "entropy_std": -0.1222, "entropy_min": -0.2826, "entropy_max": 0.007, "tail_decay": -0.1169, "ttr": -0.4354, "hapax_ratio": -0.4466},
}
d_data = {
    "llama-3.2-3b": {"entropy_max": 0.0081, "tail_decay": 0.188, "entropy_min": 0.0067, "entropy_mean": 1.1476, "ttr": 1.0372, "hapax_ratio": 0.9833, "entropy_std": 0.4984},
    "mistral-7b-v0.3": {"entropy_max": -0.004, "tail_decay": 0.1604, "entropy_min": -0.0377, "entropy_mean": 0.8922, "ttr": 0.8198, "hapax_ratio": 0.8207, "entropy_std": 0.2292},
    "olmo-2-1b": {"entropy_max": 0.0601, "tail_decay": 0.223, "entropy_min": 0.0682, "entropy_mean": 1.1887, "ttr": 1.0766, "hapax_ratio": 1.0027, "entropy_std": 0.6086},
    "pythia-1b": {"entropy_max": 0.2062, "tail_decay": -0.0838, "entropy_min": 0.024, "entropy_mean": 1.4044, "ttr": 0.7984, "hapax_ratio": 0.6491, "entropy_std": 0.532},
    "pythia-2.8b": {"entropy_max": 0.2531, "tail_decay": -0.0673, "entropy_min": -0.0319, "entropy_mean": 1.1971, "ttr": 0.7689, "hapax_ratio": 0.668, "entropy_std": 0.3885},
    "qwen3-0.6b": {"entropy_max": 0.0125, "tail_decay": 0.0845, "entropy_min": -0.1, "entropy_mean": 0.9165, "ttr": 0.6276, "hapax_ratio": 0.5028, "entropy_std": 0.5569},
    "qwen3-1.7b": {"entropy_max": -0.0198, "tail_decay": 0.0879, "entropy_min": -0.0491, "entropy_mean": 1.115, "ttr": 0.9285, "hapax_ratio": 0.8301, "entropy_std": 0.5155},
    "qwen3-8b": {"entropy_max": -0.0404, "tail_decay": 0.1544, "entropy_min": -0.0057, "entropy_mean": 0.8638, "ttr": 0.708, "hapax_ratio": 0.6579, "entropy_std": 0.3717},
}

features_h = ['entropy_mean', 'entropy_std', 'entropy_min', 'entropy_max', 'tail_decay', 'ttr', 'hapax_ratio']
splits = {
    "split_a": {
        "selection": ["pythia-2.8b", "qwen3-1.7b", "olmo-2-1b", "mistral-7b-v0.3"],
        "validation": ["pythia-1b", "qwen3-0.6b", "qwen3-8b", "llama-3.2-3b"],
    },
    "split_b": {
        "selection": ["pythia-1b", "qwen3-0.6b", "olmo-2-1b", "mistral-7b-v0.3"],
        "validation": ["pythia-2.8b", "qwen3-1.7b", "qwen3-8b", "llama-3.2-3b"],
    },
}

feat_labels = {"entropy_mean": r"$\bar{H}$", "entropy_std": r"$\sigma_H$",
               "entropy_min": r"$H_{\min}$", "entropy_max": r"$H_{\max}$",
               "tail_decay": "tail", "ttr": "TTR", "hapax_ratio": "hapax"}
zone_colors_h = {"drifting": C_DRIFT, "intermediate": C_INTERM, "near-stationary": C_STAT}
zone_markers_h = {"drifting": "o", "intermediate": "s", "near-stationary": "D"}

def classify_zone(rho, d):
    if rho > 0.30 and d > 0.20: return "drifting"
    elif rho < 0.30 and d < 0.20: return "near-stationary"
    else: return "intermediate"

def compute_pooled(generators):
    result = {}
    for feat in features_h:
        rho_vals = [abs(rho_data[g][feat]) for g in generators]
        d_vals = [abs(d_data[g][feat]) for g in generators]
        pooled_rho, pooled_d = np.mean(rho_vals), np.mean(d_vals)
        result[feat] = {"rho": pooled_rho, "d": pooled_d, "zone": classify_zone(pooled_rho, pooled_d)}
    return result

output = {}
for split_name, split_def in splits.items():
    output[split_name] = {
        "selection": compute_pooled(split_def["selection"]),
        "validation": compute_pooled(split_def["validation"]),
    }

fig, axes = plt.subplots(1, 2, figsize=(6.8, 3.2), sharey=False)
for idx, (split_name, split_label) in enumerate([("split_a", "Split A"), ("split_b", "Split B")]):
    ax = axes[idx]
    ax.axvline(x=0.30, color='#888888', linestyle='--', linewidth=0.7, alpha=0.5)
    ax.axhline(y=0.20, color='#888888', linestyle='--', linewidth=0.7, alpha=0.5)
    for subset_key, marker_fill in [("selection", True), ("validation", False)]:
        subset = output[split_name][subset_key]
        for feat in features_h:
            r, d, z = subset[feat]["rho"], subset[feat]["d"], subset[feat]["zone"]
            color, mk = zone_colors_h[z], zone_markers_h[z]
            ms = 55 if mk != 'D' else 45
            if marker_fill:
                ax.scatter(r, d, c=color, marker=mk, s=ms, edgecolors='#333333', linewidths=0.4, zorder=5)
            else:
                ax.scatter(r, d, facecolors='none', edgecolors=color, marker=mk, s=ms, linewidths=1.2, zorder=5)
            ax.annotate(feat_labels[feat], (r, d), fontsize=6.5,
                       xytext=(4, 4), textcoords='offset points', color='#444444')
    ax.set_xlabel(r"Pooled $|\rho|$", fontsize=9)
    ax.set_ylabel(r"Pooled $|d|$", fontsize=9)
    ax.set_title(split_label, fontsize=10, fontweight='bold')
    ax.set_xlim(-0.02, 0.78)
    ax.set_ylim(-0.02, 1.55)
    ax.tick_params(labelsize=7.5)

legend_elements = [
    Line2D([0],[0], marker='o', color='w', markerfacecolor=C_DRIFT, markersize=7,
           markeredgecolor='#333333', markeredgewidth=0.4, label='Drifting'),
    Line2D([0],[0], marker='s', color='w', markerfacecolor=C_INTERM, markersize=7,
           markeredgecolor='#333333', markeredgewidth=0.4, label='Intermediate'),
    Line2D([0],[0], marker='D', color='w', markerfacecolor=C_STAT, markersize=6,
           markeredgecolor='#333333', markeredgewidth=0.4, label='Near-stationary'),
    Line2D([0],[0], marker='o', color='w', markerfacecolor='#999999', markersize=7,
           markeredgecolor='#333333', markeredgewidth=0.4, label='Selection (filled)'),
    Line2D([0],[0], marker='o', color='w', markerfacecolor='none', markersize=7,
           markeredgecolor='#999999', markeredgewidth=1.2, label='Validation (hollow)'),
]
fig.legend(handles=legend_elements, loc='lower center', ncol=5, fontsize=7.5,
           frameon=False, bbox_to_anchor=(0.5, -0.01))
plt.tight_layout(rect=[0, 0.06, 1, 1])
plt.savefig('fig_ddr_holdout_split.pdf', bbox_inches='tight')
plt.savefig('fig_ddr_holdout_split.png', bbox_inches='tight')
plt.close()
print("OK fig_ddr_holdout_split")


# ━━━━━━━━━━ Figure 18: Variance Decomposition ━━━━━━━━━━
fig, ax = plt.subplots(figsize=(3.4, 2.4))

feat_names = ['Ent. Mean', 'TTR', 'Hapax', 'Ent. Max', 'Ent. Min', 'Tail Decay', 'Ent. Std']
eta_depth = [0.341, 0.370, 0.364, 0.007, 0.002, 0.002, 0.054]
eta_gen   = [0.022, 0.024, 0.017, 0.002, 0.001, 0.023, 0.020]
eta_int   = [0.010, 0.007, 0.006, 0.003, 0.001, 0.009, 0.011]

x = np.arange(len(feat_names))
w = 0.25

# Clean palette: depth uses zone color, gen/int use grays
depth_colors = [C_DRIFT]*3 + [C_STAT]*3 + [C_INTERM]

bars1 = ax.bar(x - w, eta_depth, w, label=r'$\eta^2_{\mathrm{depth}}$',
               color=depth_colors, edgecolor='white', linewidth=0.5)
bars2 = ax.bar(x, eta_gen, w, label=r'$\eta^2_{\mathrm{gen}}$',
               color='#AAAAAA', edgecolor='white', linewidth=0.5)
bars3 = ax.bar(x + w, eta_int, w, label=r'$\eta^2_{\mathrm{int}}$',
               color='#D9D9D9', edgecolor='white', linewidth=0.5)

ax.axvline(x=2.5, color='#AAAAAA', linestyle='--', linewidth=0.6, alpha=0.5)
ax.axvline(x=5.5, color='#AAAAAA', linestyle='--', linewidth=0.6, alpha=0.5)

ax.text(1.0, 0.39, 'Drifting', ha='center', fontsize=7, fontstyle='italic', color=C_DRIFT)
ax.text(4.0, 0.39, 'Near-stationary', ha='center', fontsize=7, fontstyle='italic', color=C_STAT)
ax.text(6.0, 0.39, 'Interm.', ha='center', fontsize=7, fontstyle='italic', color=C_INTERM)

ax.set_xticks(x)
ax.set_xticklabels(feat_names, rotation=30, ha='right')
ax.set_ylabel(r'$\eta^2$ (proportion of total SS)')
ax.legend(loc='center right', framealpha=0, edgecolor='none')
ax.set_ylim(0, 0.44)

plt.tight_layout()
plt.savefig('fig_appendix_variance_decomp.pdf')
plt.savefig('fig_appendix_variance_decomp.png')
plt.close()
print("OK fig_appendix_variance_decomp")

print("\nAll figures regenerated with refined palette.")
