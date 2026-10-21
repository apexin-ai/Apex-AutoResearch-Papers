#!/usr/bin/env python3
"""
Scaling analysis figure: DR violation rate vs model size.
2x2 layout: (Zero-Shot / LoRA) x (SciERC / DocRED)
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

OUT_DIR = Path(__file__).parent

# ── Style ──
plt.rcParams.update({
    'font.family': 'serif',
    'font.size': 10,
    'axes.labelsize': 10,
    'axes.titlesize': 10.5,
    'xtick.labelsize': 9,
    'ytick.labelsize': 9,
    'legend.fontsize': 8.5,
    'savefig.dpi': 300,
    'axes.linewidth': 0.6,
    'lines.linewidth': 1.8,
    'lines.markersize': 7,
})

C_U = '#c0392b'   # unconstrained
C_C = '#2471a3'   # + OntoCoDec

# ── Data ──
# Zero-Shot: 3 models (Qwen-7B, Llama-8B, 70B)
ZS_LABELS = ['Qwen-2.5\n7B', 'Llama-3.1\n8B', '70B']
ZS_X = np.arange(3)

SCI_ZS = {'u': [15.37, 13.34, 6.50], 'c': [0.93, 0.08, 0.00]}
DOC_ZS = {'u': [18.46, 26.07, 15.00], 'c': [10.21, 2.55, 0.00]}

# LoRA: 2 models (Qwen-7B, Llama-8B)
FT_LABELS = ['Qwen-2.5\n7B', 'Llama-3.1\n8B']
FT_X = np.arange(2)

SCI_FT = {'u': [1.95, 1.11], 'c': [0.00, 0.09]}
DOC_FT = {'u': [0.76, 0.49], 'c': [0.01, 0.20]}


def _fmt(v):
    if v == 0.0:
        return '0.0'
    return f'{v:.2f}' if v < 1 else f'{v:.1f}'


def _panel(ax, xs, d, labels, title, ylabel=True, legend=True):
    u = np.asarray(d['u'])
    c = np.asarray(d['c'])

    ax.plot(xs, u, 'o--', color=C_U, label='Unconstrained', zorder=3)
    ax.plot(xs, c, 's-', color=C_C, label='+ OntoCoDec', zorder=3)
    ax.fill_between(xs, u, c, alpha=0.07, color='#95a5a6', zorder=1)

    ymx = max(u.max(), c.max(), 0.5) * 1.35

    for i in range(len(xs)):
        ax.text(xs[i], u[i] + ymx * 0.03, _fmt(u[i]),
                ha='center', va='bottom', fontsize=7.5, color=C_U)

        gap = (u[i] - c[i]) / ymx if ymx > 0 else 0
        if gap > 0.12:
            ax.text(xs[i], c[i] - ymx * 0.03, _fmt(c[i]),
                    ha='center', va='top', fontsize=7.5, color=C_C)
        else:
            ax.text(xs[i] + 0.15, c[i] + ymx * 0.01, _fmt(c[i]),
                    ha='left', va='bottom', fontsize=7.5, color=C_C)

    ax.set_xticks(xs)
    ax.set_xticklabels(labels)
    ax.set_xlim(xs[0] - 0.5, xs[-1] + 0.5)
    ax.set_title(title, fontweight='bold', pad=8)
    ax.set_ylim(-ymx * 0.06, ymx)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.grid(axis='y', alpha=0.15, linewidth=0.5)
    if ylabel:
        ax.set_ylabel('DR Violation Rate (%)')
    if legend:
        ax.legend(frameon=False, loc='upper right')


# ── Figure ──
fig, axes = plt.subplots(
    2, 2, figsize=(7.5, 5.5),
    gridspec_kw={'height_ratios': [1, 0.75], 'hspace': 0.48, 'wspace': 0.25}
)

_panel(axes[0, 0], ZS_X, SCI_ZS, ZS_LABELS, '(a) SciERC — Zero-Shot')
_panel(axes[0, 1], ZS_X, DOC_ZS, ZS_LABELS, '(b) DocRED — Zero-Shot', ylabel=False)
_panel(axes[1, 0], FT_X, SCI_FT, FT_LABELS, '(c) SciERC — LoRA', legend=False)
_panel(axes[1, 1], FT_X, DOC_FT, FT_LABELS, '(d) DocRED — LoRA', ylabel=False, legend=False)

fig.savefig(OUT_DIR / 'scaling_analysis.pdf', bbox_inches='tight')
fig.savefig(OUT_DIR / 'scaling_analysis.png', bbox_inches='tight', dpi=300)
plt.close()
print(f'Saved to {OUT_DIR}/scaling_analysis.pdf and .png')
