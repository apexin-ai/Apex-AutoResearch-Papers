#!/usr/bin/env python3
"""
Plot multi-layer attention profile (Figure 7, left panel).

Two sub-panels stacked vertically:
  (a) Instruction-dominant head count per layer (L1, L8, L16, L31)
  (b) Mean instruction attention fraction per layer

Three conditions: Trained VLA, Llama-2 Base, Untrained VLA.

Output: fig_multi_layer_attn.pdf -> docs/paper/figures/ and artifacts/figures/paper/
"""
import matplotlib
matplotlib.use('Agg')

# ── Font: Liberation Serif (metrically identical to Times New Roman) ──
matplotlib.rcParams['font.family'] = 'serif'
matplotlib.rcParams['font.serif'] = ['Liberation Serif', 'DejaVu Serif']
matplotlib.rcParams['mathtext.fontset'] = 'custom'
matplotlib.rcParams['mathtext.rm'] = 'Liberation Serif'
matplotlib.rcParams['mathtext.it'] = 'Liberation Serif:italic'
matplotlib.rcParams['mathtext.bf'] = 'Liberation Serif:bold'
matplotlib.rcParams['pdf.fonttype'] = 42
matplotlib.rcParams['ps.fonttype'] = 42

import matplotlib.pyplot as plt
import numpy as np
import os

# ── Data ──
layers = ['L1', 'L8', 'L16', 'L31']
x = np.arange(len(layers))

# Panel (a): Instruction-dominant heads count (of 32 total)
trained_heads = [24, 4, 10, 18]
llama2_heads = [9, 8, 25, 8]
untrained_heads = [0, 0, 0, 0]

# Panel (b): Mean instruction attention fraction
trained_mean = [0.577, 0.468, 0.484, 0.563]
llama2_mean = [0.365, 0.488, 0.602, 0.349]
untrained_mean = [0.117, 0.079, 0.092, 0.076]

colors = {'trained': '#4C72B0', 'llama2': '#55A868', 'untrained': '#C44E52'}

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(5, 4), sharex=True)

# ── Panel (a): Head counts ──
ax1.plot(x, trained_heads, color=colors['trained'], linestyle='-', marker='o',
         markersize=7, linewidth=1.8, label='Trained VLA')
ax1.plot(x, llama2_heads, color=colors['llama2'], linestyle='--', marker='s',
         markersize=7, linewidth=1.8, label='Llama-2 Base')
ax1.plot(x, untrained_heads, color=colors['untrained'], linestyle=':', marker='^',
         markersize=7, linewidth=1.8, label='Untrained VLA')
ax1.axhline(y=16, color='gray', linestyle='--', linewidth=0.8, alpha=0.6)
ax1.text(3.05, 16, '50%', fontsize=8, color='gray', va='center')
ax1.set_ylabel('Instruction-dominant\nheads (of 32)', fontsize=9)
ax1.set_ylim(-1, 33)
ax1.set_yticks([0, 8, 16, 24, 32])
ax1.yaxis.grid(True, alpha=0.3, color='gray')
ax1.set_axisbelow(True)
ax1.spines['top'].set_visible(False)
ax1.spines['right'].set_visible(False)

# ── Panel (b): Mean attention fraction ──
ax2.plot(x, trained_mean, color=colors['trained'], linestyle='-', marker='o',
         markersize=7, linewidth=1.8)
ax2.plot(x, llama2_mean, color=colors['llama2'], linestyle='--', marker='s',
         markersize=7, linewidth=1.8)
ax2.plot(x, untrained_mean, color=colors['untrained'], linestyle=':', marker='^',
         markersize=7, linewidth=1.8)
ax2.axhline(y=0.5, color='gray', linestyle='--', linewidth=0.8, alpha=0.6)
ax2.text(3.05, 0.5, '50%', fontsize=8, color='gray', va='center')
ax2.set_ylabel('Mean instruction\nattention fraction', fontsize=9)
ax2.set_ylim(0.0, 1.0)
ax2.set_yticks([0.0, 0.25, 0.5, 0.75, 1.0])
ax2.set_xlabel('Layer', fontsize=9)
ax2.set_xticks(x)
ax2.set_xticklabels(layers)
ax2.yaxis.grid(True, alpha=0.3, color='gray')
ax2.set_axisbelow(True)
ax2.spines['top'].set_visible(False)
ax2.spines['right'].set_visible(False)

handles, labels = ax1.get_legend_handles_labels()
fig.legend(handles, labels, loc='center', bbox_to_anchor=(0.55, 0.50),
           ncol=3, fontsize=8, framealpha=0.95, edgecolor='#CCCCCC',
           handlelength=1.5, columnspacing=1.0)

plt.tight_layout()
plt.subplots_adjust(hspace=0.35)

# ── Save to both output directories ──
_REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
out_dirs = [
    os.path.join(_REPO_ROOT, 'docs', 'paper', 'figures'),
    os.path.join(_REPO_ROOT, 'artifacts', 'figures', 'paper'),
]
for d in out_dirs:
    os.makedirs(d, exist_ok=True)
    fig.savefig(os.path.join(d, 'fig_multi_layer_attn.pdf'), dpi=300, bbox_inches='tight')
    fig.savefig(os.path.join(d, 'fig_multi_layer_attn.png'), dpi=300, bbox_inches='tight')
    print(f"Saved: {d}/fig_multi_layer_attn.pdf/.png")

plt.close()
