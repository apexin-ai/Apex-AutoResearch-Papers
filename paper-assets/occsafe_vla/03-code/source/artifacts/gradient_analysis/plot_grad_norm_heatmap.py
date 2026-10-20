#!/usr/bin/env python3
"""Per-layer action gradient norm heatmap (4 conditions × 2 encoders).

Narrative intent: Vanilla/Full OCC/Random OCC maintain comparable gradient
norms (warm), while Detach BN collapses to 1-13% across all layers (cold).
This directly supports the gradient collapse prevention mechanism (C1).
"""

import csv
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import matplotlib.patheffects as pe
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

SCRIPT_DIR = Path(__file__).parent
CSV_PATH = SCRIPT_DIR / 'per_layer_conflict_rate_full.csv'
OUT_DIR = Path('/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/figures')

CONDITIONS = ['Vanilla_s0', 'Full_OCC_s0', 'Random_s2', 'Detach_BN_s2']
COND_LABELS = ['Vanilla', 'Full OCC', 'Random OCC', 'Detach']
N_DINO = 23
N_SIGLIP = 26

# --- Load data ---
data = {}
with open(CSV_PATH) as f:
    reader = csv.DictReader(f)
    for row in reader:
        cond = row['condition']
        enc = row['encoder']
        idx = int(row['layer_idx'])
        norm = float(row['action_grad_norm'])
        key = (cond, enc)
        if key not in data:
            data[key] = {}
        data[key][idx] = norm

# Build matrices
dino_matrix = np.zeros((len(CONDITIONS), N_DINO))
siglip_matrix = np.zeros((len(CONDITIONS), N_SIGLIP))

for ci, cond in enumerate(CONDITIONS):
    for li in range(N_DINO):
        dino_matrix[ci, li] = data[(cond, 'dino')].get(li, np.nan)
    for li in range(N_SIGLIP):
        siglip_matrix[ci, li] = data[(cond, 'siglip')].get(li, np.nan)

# --- Figure ---
fig, (ax_dino, ax_siglip) = plt.subplots(
    1, 2, figsize=(7.5, 2.2),
    gridspec_kw={'width_ratios': [N_DINO, N_SIGLIP], 'wspace': 0.06},
    sharey=True
)

# Log scale normalization (shared across both panels)
vmin = min(dino_matrix.min(), siglip_matrix.min())
vmax = max(dino_matrix.max(), siglip_matrix.max())
norm = mcolors.LogNorm(vmin=max(vmin, 1e-4), vmax=vmax)

cmap = plt.cm.inferno.copy()

# DINOv2 panel
im_dino = ax_dino.imshow(
    dino_matrix, aspect='auto', cmap=cmap, norm=norm,
    interpolation='nearest'
)
ax_dino.set_xticks([0, 5, 10, 15, 22])
ax_dino.set_xticklabels(['0', '5', '10', '15', '22'])
ax_dino.set_yticks(range(len(COND_LABELS)))
ax_dino.set_yticklabels(COND_LABELS)
ax_dino.set_xlabel('DINOv2 block index')
ax_dino.set_title('(a) DINOv2', fontsize=11, pad=6)

# Separator line between gradient-flow conditions and Detach
ax_dino.axhline(2.5, color='white', linewidth=1.5, linestyle='-')

# SigLIP panel
im_siglip = ax_siglip.imshow(
    siglip_matrix, aspect='auto', cmap=cmap, norm=norm,
    interpolation='nearest'
)
ax_siglip.set_xticks([0, 5, 10, 15, 20, 25])
ax_siglip.set_xticklabels(['0', '5', '10', '15', '20', '25'])
ax_siglip.set_xlabel('SigLIP block index')
ax_siglip.set_title('(b) SigLIP', fontsize=11, pad=6)
ax_siglip.yaxis.set_tick_params(labelleft=False)

ax_siglip.axhline(2.5, color='white', linewidth=1.5, linestyle='-')

# Collapse annotation on Detach row
t = ax_dino.text(
    11, 3, '1–13% of Vanilla',
    fontsize=8.5, color='#cccccc', ha='center', va='center',
    fontstyle='italic', fontweight='bold'
)
t.set_path_effects([pe.withStroke(linewidth=2.5, foreground='#1a0a2e')])

t2 = ax_siglip.text(
    13, 3, '2–13% of Vanilla',
    fontsize=8.5, color='#cccccc', ha='center', va='center',
    fontstyle='italic', fontweight='bold'
)
t2.set_path_effects([pe.withStroke(linewidth=2.5, foreground='#1a0a2e')])

# Shared colorbar
cbar = fig.colorbar(im_siglip, ax=[ax_dino, ax_siglip],
                    location='right', fraction=0.02, pad=0.02,
                    label='Action gradient norm')

# Remove top/right spines (imshow adds them back)
for ax in [ax_dino, ax_siglip]:
    for spine in ax.spines.values():
        spine.set_visible(False)

plt.savefig(OUT_DIR / 'grad_norm_heatmap.pdf')
plt.savefig(OUT_DIR / 'grad_norm_heatmap.png')
print(f'Saved to {OUT_DIR / "grad_norm_heatmap.pdf"}')
print(f'Saved to {OUT_DIR / "grad_norm_heatmap.png"}')
plt.close()
