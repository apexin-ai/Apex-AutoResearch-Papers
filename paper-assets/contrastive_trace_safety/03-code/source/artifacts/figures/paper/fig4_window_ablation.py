import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams.update({
    'font.family': 'DejaVu Sans',
    'font.size': 10,
    'axes.titlesize': 11,
    'axes.labelsize': 10,
    'xtick.labelsize': 9,
    'ytick.labelsize': 9,
    'legend.fontsize': 8.5,
    'figure.dpi': 300,
    'savefig.dpi': 300,
    'savefig.bbox': 'tight',
    'savefig.pad_inches': 0.05,
    'axes.spines.top': False,
    'axes.spines.right': False,
    'lines.linewidth': 1.8,
})

# Okabe-Ito colorblind-safe palette
COLORS = {
    'r1_8b': '#0072B2',    # deep blue
    'r1_32b': '#D55E00',   # orange-red
    'qwq_32b': '#009E73',  # green
}

LABELS = {
    'r1_8b': 'R1-8B',
    'r1_32b': 'R1-32B',
    'qwq_32b': 'QwQ-32B',
}

MARKERS = {
    'r1_8b': 'o',
    'r1_32b': 's',
    'qwq_32b': '^',
}

LINESTYLES = {
    'r1_8b': '-',
    'r1_32b': '--',
    'qwq_32b': ':',
}

# Data from exp_007_window_ablation/results.json (canonical source)
data = {
    "r1_8b": {
        "W=1": {"bal_acc": 0.7783, "precp_fpr_step": 0.0965, "precision": 0.6926},
        "W=3": {"bal_acc": 0.7902, "precp_fpr_step": 0.085, "precision": 0.7228},
        "W=5": {"bal_acc": 0.781, "precp_fpr_step": 0.0809, "precision": 0.7258},
        "W=10": {"bal_acc": 0.7925, "precp_fpr_step": 0.0761, "precision": 0.7431},
        "W=15": {"bal_acc": 0.8017, "precp_fpr_step": 0.0639, "precision": 0.7767},
        "W=20": {"bal_acc": 0.8072, "precp_fpr_step": 0.0612, "precision": 0.7862},
        "W=25": {"bal_acc": 0.8095, "precp_fpr_step": 0.0483, "precision": 0.8216},
    },
    "r1_32b": {
        "W=1": {"bal_acc": 0.7182, "precp_fpr_step": 0.3203, "precision": 0.549},
        "W=3": {"bal_acc": 0.7252, "precp_fpr_step": 0.3064, "precision": 0.56},
        "W=5": {"bal_acc": 0.7309, "precp_fpr_step": 0.2841, "precision": 0.575},
        "W=10": {"bal_acc": 0.7371, "precp_fpr_step": 0.234, "precision": 0.6093},
        "W=15": {"bal_acc": 0.7207, "precp_fpr_step": 0.2451, "precision": 0.5907},
        "W=20": {"bal_acc": 0.6961, "precp_fpr_step": 0.2618, "precision": 0.5628},
        "W=25": {"bal_acc": 0.7028, "precp_fpr_step": 0.2646, "precision": 0.5662},
    },
    "qwq_32b": {
        "W=1": {"bal_acc": 0.7298, "precp_fpr_step": 0.2276, "precision": 0.5435},
        "W=3": {"bal_acc": 0.7452, "precp_fpr_step": 0.2141, "precision": 0.5647},
        "W=5": {"bal_acc": 0.761, "precp_fpr_step": 0.2168, "precision": 0.5733},
        "W=10": {"bal_acc": 0.7469, "precp_fpr_step": 0.2073, "precision": 0.5714},
        "W=15": {"bal_acc": 0.7412, "precp_fpr_step": 0.1911, "precision": 0.5816},
        "W=20": {"bal_acc": 0.7542, "precp_fpr_step": 0.1789, "precision": 0.6024},
        "W=25": {"bal_acc": 0.7624, "precp_fpr_step": 0.1694, "precision": 0.6177},
    },
}

windows = [1, 3, 5, 10, 15, 20, 25]
window_keys = [f"W={w}" for w in windows]

fig, axes = plt.subplots(1, 3, figsize=(6.5, 2.3), sharey=False)

metrics = [
    ('bal_acc', 'Balanced Accuracy', (0.67, 0.83)),
    ('precision', 'Precision', (0.52, 0.85)),
    ('precp_fpr_step', 'Pre-CP FPR', (0.0, 0.35)),
]

for ax_idx, (metric_key, metric_label, ylim) in enumerate(metrics):
    ax = axes[ax_idx]
    for model in ['r1_8b', 'r1_32b', 'qwq_32b']:
        values = [data[model][wk][metric_key] for wk in window_keys]
        ax.plot(windows, values,
                color=COLORS[model],
                marker=MARKERS[model],
                linestyle=LINESTYLES[model],
                label=LABELS[model],
                markersize=4.5,
                markeredgewidth=0.8,
                markeredgecolor='white',
                zorder=3)

    ax.set_xlabel('Window size $W$')
    ax.set_ylabel(metric_label)
    ax.set_ylim(ylim)
    ax.set_xticks(windows)
    ax.set_xticklabels([str(w) for w in windows], fontsize=8)
    ax.grid(True, alpha=0.25, zorder=0)

    if metric_key == 'precp_fpr_step':
        # Add arrow annotation showing "lower is better"
        ax.annotate('', xy=(23, 0.06), xytext=(23, 0.15),
                    arrowprops=dict(arrowstyle='->', color='gray', lw=1.2))
        ax.text(24.5, 0.105, 'better', fontsize=7, color='gray',
                rotation=90, va='center', ha='left')
    else:
        # Add arrow annotation showing "higher is better"
        ax.annotate('', xy=(23, ylim[1] - 0.03), xytext=(23, ylim[1] - 0.1),
                    arrowprops=dict(arrowstyle='->', color='gray', lw=1.2))
        ax.text(24.5, ylim[1] - 0.065, 'better', fontsize=7, color='gray',
                rotation=90, va='center', ha='left')

# Single legend at top
handles, labels = axes[0].get_legend_handles_labels()
fig.legend(handles, labels, loc='upper center', ncol=3,
           bbox_to_anchor=(0.5, 1.06), frameon=False, fontsize=9)

plt.tight_layout(w_pad=1.5)

outdir = '/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/artifacts/figures/paper'
plt.savefig(f'{outdir}/fig4_window_ablation.pdf', format='pdf')
plt.savefig(f'{outdir}/fig4_window_ablation.png', format='png', dpi=300)
print(f'Saved: {outdir}/fig4_window_ablation.pdf')
print(f'Saved: {outdir}/fig4_window_ablation.png')
plt.close()
