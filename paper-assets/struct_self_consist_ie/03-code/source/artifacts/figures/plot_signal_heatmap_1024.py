#!/usr/bin/env python3
"""Signal heatmap (2×2): Spearman ρ + AUROC × Full/Conditional.
Data source: exp_012_rerun_1024 (N=8, 1024 tokens, Qwen-3-8B, SciERC).
"""
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from pathlib import Path

plt.rcParams.update({
    'font.family': 'serif',
    'font.serif': ['Times New Roman', 'DejaVu Serif', 'Computer Modern Roman'],
    'font.size': 9,
    'axes.labelsize': 9,
    'axes.titlesize': 10,
    'xtick.labelsize': 8,
    'ytick.labelsize': 8,
    'legend.fontsize': 7.5,
    'figure.dpi': 300,
    'savefig.dpi': 300,
    'savefig.bbox': 'tight',
    'savefig.pad_inches': 0.05,
    'text.usetex': False,
})

FIG_DIR = Path(__file__).parent
FIG_DIR.mkdir(parents=True, exist_ok=True)

signal_labels = ['SJ', 'FK', 'EM', 'VotConf', 'LogProb']
row_labels = ['SciERC NER\n(Qwen, N=8)', 'SciERC RE\n(Qwen, N=8)']

# ── Data: exp_012_rerun_1024 ────────────────────────────────────────────────

# Spearman ρ
rho_full = np.array([
    [0.3599, 0.2665, 0.2945, 0.3792, 0.2052],  # NER full
    [0.2503, 0.2752, 0.1344, 0.3498, 0.2662],  # RE full
])
rho_cond = np.array([
    [0.3113, 0.1761, 0.3596, 0.3000, 0.1538],  # NER cond (n=477)
    [0.2457, 0.1139, 0.4165, 0.2409, 0.0112],  # RE cond (n=238)
])

# AUROC
auroc_full = np.array([
    [0.6917, 0.6290, 0.7493, 0.6841, 0.5783],  # NER full
    [0.6702, 0.6089, 0.7059, 0.6935, 0.6005],  # RE full
])
auroc_cond = np.array([
    [0.6772, 0.6078, 0.7556, 0.6618, 0.5633],  # NER cond
    [0.6463, 0.5510, 0.7515, 0.6420, 0.5186],  # RE cond
])

# ── Plot 2×2 grid ──────────────────────────────────────────────────────────

fig, axes = plt.subplots(2, 2, figsize=(6.8, 3.2),
                         gridspec_kw={'wspace': 0.08, 'hspace': 0.35})

panels = [
    (axes[0, 0], rho_full,   'Spearman ρ — Full set',        0.0, 0.45, 'RdYlGn'),
    (axes[0, 1], rho_cond,   'Spearman ρ — Conditional set',  0.0, 0.45, 'RdYlGn'),
    (axes[1, 0], auroc_full,  'AUROC — Full set',             0.50, 0.78, 'RdYlGn'),
    (axes[1, 1], auroc_cond,  'AUROC — Conditional set',      0.50, 0.78, 'RdYlGn'),
]

for ax, data, title, vmin, vmax, cmap in panels:
    im = ax.imshow(data, cmap=cmap, aspect='auto', vmin=vmin, vmax=vmax)

    for i in range(data.shape[0]):
        for j in range(data.shape[1]):
            val = data[i, j]
            mid = (vmin + vmax) / 2
            span = vmax - vmin
            color = 'white' if val < (mid - 0.15 * span) or val > (mid + 0.3 * span) else 'black'
            ax.text(j, i, f'{val:.3f}', ha='center', va='center',
                    fontsize=7.5, color=color, fontweight='medium')

    ax.set_xticks(range(len(signal_labels)))
    ax.set_xticklabels(signal_labels)
    ax.set_yticks(range(len(row_labels)))
    ax.set_title(title, fontsize=9, fontweight='bold', pad=4)
    ax.tick_params(length=2, pad=2)

    is_left = ax in (axes[0, 0], axes[1, 0])
    if is_left:
        ax.set_yticklabels(row_labels, fontsize=7.5)
    else:
        ax.set_yticklabels([])

# Colorbars: one for ρ row, one for AUROC row
cbar_rho = fig.colorbar(axes[0, 1].images[0], ax=axes[0, :].tolist(),
                        shrink=0.85, pad=0.02)
cbar_rho.set_label('Spearman ρ', fontsize=8)
cbar_rho.ax.tick_params(labelsize=7)

cbar_auroc = fig.colorbar(axes[1, 1].images[0], ax=axes[1, :].tolist(),
                          shrink=0.85, pad=0.02)
cbar_auroc.set_label('AUROC', fontsize=8)
cbar_auroc.ax.tick_params(labelsize=7)

fig.savefig(FIG_DIR / 'fig_signal_heatmap_1024.pdf', format='pdf')
fig.savefig(FIG_DIR / 'fig_signal_heatmap_1024.png', format='png')
plt.close(fig)
print("✓ fig_signal_heatmap_1024 saved")
