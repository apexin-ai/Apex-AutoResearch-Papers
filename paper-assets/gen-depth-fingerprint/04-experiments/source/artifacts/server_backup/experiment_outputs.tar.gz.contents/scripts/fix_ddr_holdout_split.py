import matplotlib
matplotlib.use('Agg')
matplotlib.rcParams['pdf.fonttype'] = 42
matplotlib.rcParams['ps.fonttype'] = 42
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.lines import Line2D

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

features = ['entropy_mean', 'entropy_std', 'entropy_min', 'entropy_max', 'tail_decay', 'ttr', 'hapax_ratio']
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

feat_labels = {"entropy_mean": "H_mean", "entropy_std": "H_std", "entropy_min": "H_min",
               "entropy_max": "H_max", "tail_decay": "tail", "ttr": "TTR", "hapax_ratio": "hapax"}
zone_colors = {"drifting": "#2ca02c", "intermediate": "#7b4ea3", "near-stationary": "#d97706"}
zone_markers = {"drifting": "o", "intermediate": "s", "near-stationary": "D"}

def classify_zone(rho, d):
    if rho > 0.30 and d > 0.20: return "drifting"
    elif rho < 0.30 and d < 0.20: return "near-stationary"
    else: return "intermediate"

def compute_pooled(generators):
    result = {}
    for feat in features:
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

fig, axes = plt.subplots(1, 2, figsize=(10, 4.5), sharey=False)
for idx, (split_name, split_label) in enumerate([("split_a", "Split A"), ("split_b", "Split B")]):
    ax = axes[idx]
    for subset_key, marker_fill in [("selection", True), ("validation", False)]:
        subset = output[split_name][subset_key]
        for feat in features:
            r, d, z = subset[feat]["rho"], subset[feat]["d"], subset[feat]["zone"]
            color, mk = zone_colors[z], zone_markers[z]
            if marker_fill:
                ax.scatter(r, d, c=color, marker=mk, s=70, edgecolors='black', linewidths=0.5, zorder=5)
            else:
                ax.scatter(r, d, facecolors='none', edgecolors=color, marker=mk, s=70, linewidths=1.5, zorder=5)
            ax.annotate(feat_labels[feat], (r, d), fontsize=6.5,
                       xytext=(0.012, 0.015), textcoords='offset fontsize', color='#333333')
    ax.axvline(x=0.30, color='gray', linestyle='--', linewidth=0.8, alpha=0.6)
    ax.axhline(y=0.20, color='gray', linestyle='--', linewidth=0.8, alpha=0.6)
    ax.set_xlabel("Pooled |Spearman rho|", fontsize=10)
    ax.set_ylabel("Pooled |Cohen's d|", fontsize=10)
    ax.set_title(split_label, fontsize=11, fontweight='bold')
    ax.set_xlim(-0.02, 0.78); ax.set_ylim(-0.02, 1.55)
    ax.tick_params(labelsize=8)

legend_elements = [
    Line2D([0],[0], marker='o', color='w', markerfacecolor='#2ca02c', markersize=8, markeredgecolor='black', markeredgewidth=0.5, label='Drifting'),
    Line2D([0],[0], marker='s', color='w', markerfacecolor='#7b4ea3', markersize=8, markeredgecolor='black', markeredgewidth=0.5, label='Intermediate'),
    Line2D([0],[0], marker='D', color='w', markerfacecolor='#d97706', markersize=7, markeredgecolor='black', markeredgewidth=0.5, label='Near-stationary'),
    Line2D([0],[0], marker='o', color='w', markerfacecolor='gray', markersize=8, markeredgecolor='black', markeredgewidth=0.5, label='Selection (filled)'),
    Line2D([0],[0], marker='o', color='w', markerfacecolor='none', markersize=8, markeredgecolor='gray', markeredgewidth=1.5, label='Validation (hollow)'),
]
fig.legend(handles=legend_elements, loc='lower center', ncol=5, fontsize=8, frameon=False, bbox_to_anchor=(0.5, -0.02))
plt.tight_layout(rect=[0, 0.06, 1, 1])
plt.savefig('/root/gen-depth-fingerprint/chart/fig_ddr_holdout_split.pdf', bbox_inches='tight', dpi=300)
print("Saved fig_ddr_holdout_split.pdf")
