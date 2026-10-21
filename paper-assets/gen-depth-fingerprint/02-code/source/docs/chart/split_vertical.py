"""Regenerate Figure 9 (instruct DDR) and Figure 17 (holdout scatter) in vertical layout."""
import matplotlib
matplotlib.use('Agg')
matplotlib.rcParams['pdf.fonttype'] = 42
matplotlib.rcParams['ps.fonttype'] = 42
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.lines import Line2D
import matplotlib.patches as mpatches

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

# DDR zone palette
C_DRIFT = '#D6604D'
C_INTERM = '#7570B3'
C_STAT = '#4393C3'

# ━━━━━━━━━━ Figure 9: Instruct DDR (vertical layout) ━━━━━━━━━━

MODELS = ["Qwen3-1.7B", "OLMo-2-1B", "Llama-3.2-3B"]
MODEL_MARKERS = {"Qwen3-1.7B": "o", "OLMo-2-1B": "s", "Llama-3.2-3B": "D"}

FEATURES = [
    ("hapax_ratio",  "Drifting"),
    ("ttr",          "Drifting"),
    ("entropy_mean", "Drifting"),
    ("entropy_std",  "Intermediate"),
    ("entropy_min",  "Near-stationary"),
    ("entropy_max",  "Near-stationary"),
    ("tail_decay",   "Near-stationary"),
]

FEAT_LABELS = {
    "entropy_mean": r"$\bar{H}$",
    "entropy_std":  r"$\sigma_H$",
    "entropy_min":  r"$H_{\min}$",
    "entropy_max":  r"$H_{\max}$",
    "ttr":          "TTR",
    "hapax_ratio":  "Hapax",
    "tail_decay":   "Tail Decay",
}

ZONE_COLORS = {
    "Drifting": C_DRIFT,
    "Intermediate": C_INTERM,
    "Near-stationary": C_STAT,
}

# Hardcoded data (from original server results)
base_d = {
    "Qwen3-1.7B": {"hapax_ratio": 0.83, "ttr": 0.93, "entropy_mean": 1.12, "entropy_std": 0.52, "entropy_min": 0.05, "entropy_max": 0.02, "tail_decay": 0.09},
    "OLMo-2-1B": {"hapax_ratio": 1.00, "ttr": 1.08, "entropy_mean": 1.19, "entropy_std": 0.61, "entropy_min": 0.07, "entropy_max": 0.06, "tail_decay": 0.22},
    "Llama-3.2-3B": {"hapax_ratio": 0.98, "ttr": 1.04, "entropy_mean": 1.15, "entropy_std": 0.50, "entropy_min": 0.01, "entropy_max": 0.01, "tail_decay": 0.19},
}
inst_d = {
    "Qwen3-1.7B": {"hapax_ratio": 0.42, "ttr": 0.48, "entropy_mean": 0.65, "entropy_std": 0.38, "entropy_min": 0.12, "entropy_max": 0.15, "tail_decay": 0.08},
    "OLMo-2-1B": {"hapax_ratio": 0.08, "ttr": 0.10, "entropy_mean": 0.25, "entropy_std": 0.15, "entropy_min": 0.03, "entropy_max": 0.18, "tail_decay": 0.05},
    "Llama-3.2-3B": {"hapax_ratio": 0.35, "ttr": 0.38, "entropy_mean": 0.52, "entropy_std": 0.28, "entropy_min": 0.08, "entropy_max": 0.10, "tail_decay": 0.12},
}

n = len(FEATURES)

fig, (ax_base, ax_inst) = plt.subplots(2, 1, figsize=(3.4, 5.2),
                                        sharex=True, gridspec_kw={"hspace": 0.25})
rng = np.random.default_rng(42)

def draw_panel(ax, per_model, title, sil):
    medians = {}
    for feat, _ in FEATURES:
        vals = [abs(per_model[m][feat]) for m in MODELS]
        medians[feat] = float(np.median(vals))

    for i, (feat, zone) in enumerate(FEATURES):
        y = n - 1 - i
        val = medians[feat]
        ax.barh(y, val, color=ZONE_COLORS[zone], height=0.55, alpha=0.82, zorder=2)
        for m in MODELS:
            mv = abs(per_model[m][feat])
            jit = rng.uniform(-0.12, 0.12)
            ax.scatter(mv, y + jit, marker=MODEL_MARKERS[m],
                       color="#444444", s=18, alpha=0.7, zorder=3, edgecolors="none")

    ax.set_xlim(-0.02, 1.35)
    ax.set_ylim(-0.5, n - 0.5)
    ax.xaxis.grid(True, color="#eeeeee", linewidth=0.5, zorder=0)
    ax.set_title(title, fontsize=10, fontweight="bold", pad=4)
    ax.text(0.97, 0.05, f"Silhouette = {sil:.3f}",
            transform=ax.transAxes, ha="right", va="bottom",
            fontsize=7.5, fontstyle="italic",
            bbox=dict(boxstyle="round,pad=0.3", fc="white", ec="#cccccc", alpha=0.9))

draw_panel(ax_base, base_d, "(a) Base Models", 0.660)
draw_panel(ax_inst, inst_d, "(b) Instruct Models", 0.372)

yticks = list(range(n))
ylabels = [FEAT_LABELS[FEATURES[n - 1 - i][0]] for i in range(n)]
ax_base.set_yticks(yticks)
ax_base.set_yticklabels(ylabels, fontsize=8)
ax_inst.set_yticks(yticks)
ax_inst.set_yticklabels(ylabels, fontsize=8)
ax_inst.set_xlabel(r"|Cohen's $d$|  (gen-1 vs. gen-2+)", fontsize=9)

zone_patches = [
    mpatches.Patch(color=C_DRIFT, alpha=0.82, label="Drifting"),
    mpatches.Patch(color=C_INTERM, alpha=0.82, label="Intermediate"),
    mpatches.Patch(color=C_STAT, alpha=0.82, label="Near-stationary"),
]
model_handles = [
    plt.Line2D([], [], marker=MODEL_MARKERS[m], color="#444444", linestyle="None",
               markersize=4.5, label=m)
    for m in MODELS
]
ax_inst.legend(handles=zone_patches + model_handles, loc="center right",
               fontsize=6.5, frameon=True, framealpha=0.9,
               edgecolor="#cccccc", fancybox=False,
               handletextpad=0.4, borderpad=0.4)

plt.tight_layout()
plt.savefig('fig_appendix_instruct_ddr.pdf', bbox_inches='tight')
plt.savefig('fig_appendix_instruct_ddr.png', bbox_inches='tight')
plt.close()
print("OK fig_appendix_instruct_ddr (vertical)")


# ━━━━━━━━━━ Figure 17: Holdout Split Validation (vertical layout) ━━━━━━━━━━

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
# Per-feature label offsets to avoid overlap in clustered regions
feat_offsets = {
    "entropy_mean": (4, -10),
    "entropy_std":  (4, 6),
    "entropy_min":  (-30, -10),
    "entropy_max":  (4, 6),
    "tail_decay":   (4, -10),
    "ttr":          (4, 6),
    "hapax_ratio":  (4, -10),
}
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

fig, axes = plt.subplots(2, 1, figsize=(3.4, 5.6), sharex=True)
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
            ox, oy = feat_offsets.get(feat, (4, 4))
            ax.annotate(feat_labels[feat], (r, d), fontsize=6.5,
                       xytext=(ox, oy), textcoords='offset points', color='#444444')
    ax.set_ylabel(r"Pooled $|d|$", fontsize=9)
    ax.set_title(split_label, fontsize=10, fontweight='bold')
    ax.set_xlim(-0.02, 0.78)
    ax.set_ylim(-0.02, 1.55)
    ax.tick_params(labelsize=7.5)

axes[1].set_xlabel(r"Pooled $|\rho|$", fontsize=9)

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
axes[1].legend(handles=legend_elements, loc='upper right', ncol=1, fontsize=6.5,
               frameon=True, framealpha=0.9, edgecolor='#CCCCCC')

plt.tight_layout()
plt.savefig('fig_ddr_holdout_split.pdf', bbox_inches='tight')
plt.savefig('fig_ddr_holdout_split.png', bbox_inches='tight')
plt.close()
print("OK fig_ddr_holdout_split (vertical)")

print("\nAll vertical figures done.")
