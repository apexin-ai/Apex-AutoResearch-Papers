#!/usr/bin/env python3
"""Per-layer gradient conflict rate figure for the paper.

Narrative intent: DINOv2 layers show ~50% conflict (direction-independent
anti-freeze), while SigLIP late layers drop to 19-25% (cooperative gradient
alignment). Both Full OCC and Random OCC show identical patterns, confirming
architectural structure rather than label content.
"""

import csv
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
from pathlib import Path

plt.rcParams.update({
    'font.family': 'DejaVu Sans',
    'font.size': 11,
    'axes.titlesize': 12,
    'axes.labelsize': 11,
    'xtick.labelsize': 9,
    'ytick.labelsize': 10,
    'legend.fontsize': 9.5,
    'figure.dpi': 300,
    'savefig.dpi': 300,
    'savefig.bbox': 'tight',
    'savefig.pad_inches': 0.08,
    'axes.spines.top': False,
    'axes.spines.right': False,
    'lines.linewidth': 1.8,
})

COLORS = {
    'full_occ': '#0072B2',
    'random':   '#E69F00',
}

SCRIPT_DIR = Path(__file__).parent
CSV_PATH = SCRIPT_DIR / 'per_layer_conflict_rate.csv'
OUT_DIR = Path('/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/figures')

# --- Load data ---
data = {}
with open(CSV_PATH) as f:
    reader = csv.DictReader(f)
    for row in reader:
        cond = row['condition']
        enc = row['encoder']
        idx = int(row['layer_idx'])
        cr = float(row['conflict_rate'])
        cos = float(row['cosine_sim'])
        key = (cond, enc)
        if key not in data:
            data[key] = {'idx': [], 'conflict_rate': [], 'cosine_sim': []}
        data[key]['idx'].append(idx)
        data[key]['conflict_rate'].append(cr)
        data[key]['cosine_sim'].append(cos)

# --- Figure ---
fig, (ax_dino, ax_siglip) = plt.subplots(
    1, 2, figsize=(7.2, 2.8),
    gridspec_kw={'width_ratios': [23, 26], 'wspace': 0.14},
    sharey=True
)

# DINOv2 panel
for cond, color, label in [
    ('Full_OCC_s0', COLORS['full_occ'], 'Full OCC'),
    ('Random_s2',   COLORS['random'],   'Random OCC'),
]:
    d = data[(cond, 'dino')]
    ax_dino.plot(d['idx'], d['conflict_rate'], color=color, label=label,
                 linewidth=1.6, alpha=0.85, marker='o', markersize=3,
                 markeredgewidth=0, zorder=3)

# 50% reference line
ax_dino.axhline(0.5, color='#888888', linestyle='--', linewidth=0.7, alpha=0.5, zorder=1)
ax_dino.text(22, 0.503, '50%', fontsize=7.5, color='#888888', ha='right', va='bottom')

ax_dino.set_xlim(-0.5, 22.5)
ax_dino.set_ylim(0.12, 0.52)
ax_dino.set_xlabel('DINOv2 block index')
ax_dino.set_ylabel('Gradient conflict rate')
ax_dino.set_title('(a) DINOv2: anti-freeze ($\\approx$50% conflict)', fontsize=10.5, pad=8)
ax_dino.set_xticks([0, 5, 10, 15, 20])

# Subtle group separators
for x in [8, 16]:
    ax_dino.axvline(x - 0.5, color='#cccccc', linestyle=':', linewidth=0.6, zorder=0)

ax_dino.legend(loc='lower left', framealpha=0.9, edgecolor='none')

# SigLIP panel
for cond, color, label in [
    ('Full_OCC_s0', COLORS['full_occ'], 'Full OCC'),
    ('Random_s2',   COLORS['random'],   'Random OCC'),
]:
    d = data[(cond, 'siglip')]
    ax_siglip.plot(d['idx'], d['conflict_rate'], color=color, label=label,
                   linewidth=1.6, alpha=0.85, marker='o', markersize=3,
                   markeredgewidth=0, zorder=3)

ax_siglip.axhline(0.5, color='#888888', linestyle='--', linewidth=0.7, alpha=0.5, zorder=1)
ax_siglip.text(25, 0.503, '50%', fontsize=7.5, color='#888888', ha='right', va='bottom')

# Cooperative zone highlight (blocks 19-24 core drop)
ax_siglip.axvspan(18.5, 25.5, alpha=0.07, color='#D55E00', zorder=0)

# Single clean annotation
import matplotlib.patheffects as pe
t = ax_siglip.text(
    14.0, 0.14, 'cooperative zone\n(19–25% conflict)',
    fontsize=8, color='#D55E00', fontstyle='italic',
    ha='center', va='center', alpha=0.85
)
t.set_path_effects([pe.withStroke(linewidth=2.5, foreground='white')])

ax_siglip.annotate(
    '', xy=(19.5, 0.19), xytext=(16.5, 0.155),
    arrowprops=dict(arrowstyle='->', color='#D55E00', lw=0.8, alpha=0.7)
)

ax_siglip.set_xlim(-0.5, 25.5)
ax_siglip.set_xlabel('SigLIP block index')
ax_siglip.set_title('(b) SigLIP: cooperative in late layers', fontsize=10.5, pad=8)
ax_siglip.set_xticks([0, 5, 10, 15, 20, 25])

# Group separators
for x in [9, 17]:
    ax_siglip.axvline(x - 0.5, color='#cccccc', linestyle=':', linewidth=0.6, zorder=0)

ax_siglip.yaxis.set_tick_params(labelleft=False)

# Subtle grid
for ax in [ax_dino, ax_siglip]:
    ax.grid(True, alpha=0.15, axis='y', zorder=0)
    ax.tick_params(axis='both', which='both', length=3)

plt.savefig(OUT_DIR / 'per_layer_conflict_rate.pdf')
plt.savefig(OUT_DIR / 'per_layer_conflict_rate.png')
print(f'Saved to {OUT_DIR / "per_layer_conflict_rate.pdf"}')
print(f'Saved to {OUT_DIR / "per_layer_conflict_rate.png"}')
plt.close()
