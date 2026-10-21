#!/usr/bin/env python3
"""Combined per-layer gradient figure: heatmap (amplitude) + conflict rate (direction).
v1 codebase data. Unified serif styling for CoRL 2026."""

import csv
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import matplotlib.patheffects as pe
import matplotlib.gridspec as gridspec
import numpy as np
from pathlib import Path

plt.rcParams.update({
    'font.family': 'serif',
    'font.serif': ['Liberation Serif', 'DejaVu Serif'],
    'font.size': 9,
    'axes.titlesize': 10,
    'axes.labelsize': 9,
    'xtick.labelsize': 8,
    'ytick.labelsize': 8,
    'legend.fontsize': 8,
    'figure.dpi': 300,
    'savefig.dpi': 300,
    'savefig.bbox': 'tight',
    'savefig.pad_inches': 0.05,
    'axes.spines.top': False,
    'axes.spines.right': False,
    'lines.linewidth': 1.4,
    'pdf.fonttype': 42,
    'ps.fonttype': 42,
    'mathtext.fontset': 'cm',
})

SCRIPT_DIR = Path(__file__).parent
CSV_FULL = SCRIPT_DIR / 'per_layer_conflict_rate_full.csv'
OUT_DIR = Path('/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/figures')

# Paper color palette
COLORS = {
    'full_occ': '#C44E52',
    'random':   '#55A868',
}

CONDITIONS = ['Vanilla_s0', 'Full_OCC_s0', 'Random_s2', 'Detach_BN_s2']
COND_LABELS = ['Vanilla', 'Full OCC', 'Random OCC', 'Detach']
N_DINO = 23
N_SIGLIP = 26

# --- Load data ---
data = {}
with open(CSV_FULL) as f:
    reader = csv.DictReader(f)
    for row in reader:
        cond = row['condition']
        enc = row['encoder']
        idx = int(row['layer_idx'])
        norm_val = float(row['action_grad_norm'])
        cr_str = row['conflict_rate']
        cr = float(cr_str) if cr_str else None
        key = (cond, enc)
        if key not in data:
            data[key] = {'idx': [], 'norm': {}, 'conflict_rate': {}}
        data[key]['idx'].append(idx)
        data[key]['norm'][idx] = norm_val
        if cr is not None:
            data[key]['conflict_rate'][idx] = cr

# Build heatmap matrices
dino_matrix = np.zeros((len(CONDITIONS), N_DINO))
siglip_matrix = np.zeros((len(CONDITIONS), N_SIGLIP))
for ci, cond in enumerate(CONDITIONS):
    for li in range(N_DINO):
        dino_matrix[ci, li] = data[(cond, 'dino')]['norm'].get(li, np.nan)
    for li in range(N_SIGLIP):
        siglip_matrix[ci, li] = data[(cond, 'siglip')]['norm'].get(li, np.nan)

# --- Figure ---
fig = plt.figure(figsize=(7.2, 5.0))

outer_gs = gridspec.GridSpec(2, 1, figure=fig, height_ratios=[1, 1.15], hspace=0.42)

gs_top = gridspec.GridSpecFromSubplotSpec(
    1, 3, subplot_spec=outer_gs[0],
    width_ratios=[N_DINO, N_SIGLIP, 0.8], wspace=0.08
)
gs_bot = gridspec.GridSpecFromSubplotSpec(
    1, 2, subplot_spec=outer_gs[1],
    width_ratios=[N_DINO, N_SIGLIP], wspace=0.12
)

# ======= TOP ROW: Gradient norm heatmap =======
ax_hm_dino = fig.add_subplot(gs_top[0, 0])
ax_hm_siglip = fig.add_subplot(gs_top[0, 1], sharey=ax_hm_dino)
ax_cbar = fig.add_subplot(gs_top[0, 2])

vmin = min(dino_matrix.min(), siglip_matrix.min())
vmax = max(dino_matrix.max(), siglip_matrix.max())
norm = mcolors.LogNorm(vmin=max(vmin, 1e-4), vmax=vmax)
cmap = plt.cm.inferno.copy()

im_dino = ax_hm_dino.imshow(dino_matrix, aspect='auto', cmap=cmap, norm=norm,
                             interpolation='nearest')
ax_hm_dino.set_yticks(range(len(COND_LABELS)))
ax_hm_dino.set_yticklabels(COND_LABELS)
ax_hm_dino.set_xticks([0, 5, 10, 15, 22])
ax_hm_dino.set_xticklabels(['0', '5', '10', '15', '22'])
ax_hm_dino.set_xlabel('DINOv2 block index', fontsize=8.5)
ax_hm_dino.set_title('(a) DINOv2 — gradient amplitude', fontsize=9.5, pad=5)
ax_hm_dino.axhline(2.5, color='white', linewidth=1.2, linestyle='-')
for spine in ax_hm_dino.spines.values():
    spine.set_visible(False)

im_siglip = ax_hm_siglip.imshow(siglip_matrix, aspect='auto', cmap=cmap, norm=norm,
                                 interpolation='nearest')
ax_hm_siglip.set_xticks([0, 5, 10, 15, 20, 25])
ax_hm_siglip.set_xticklabels(['0', '5', '10', '15', '20', '25'])
ax_hm_siglip.set_xlabel('SigLIP block index', fontsize=8.5)
ax_hm_siglip.set_title('(b) SigLIP — gradient amplitude', fontsize=9.5, pad=5)
ax_hm_siglip.axhline(2.5, color='white', linewidth=1.2, linestyle='-')
plt.setp(ax_hm_siglip.get_yticklabels(), visible=False)
for spine in ax_hm_siglip.spines.values():
    spine.set_visible(False)

# Collapse annotations
t1 = ax_hm_dino.text(11, 3, '1–13%', fontsize=7.5, color='#cccccc',
                      ha='center', va='center', fontstyle='italic', fontweight='bold')
t1.set_path_effects([pe.withStroke(linewidth=2.5, foreground='#1a0a2e')])
t2 = ax_hm_siglip.text(13, 3, '2–13%', fontsize=7.5, color='#cccccc',
                        ha='center', va='center', fontstyle='italic', fontweight='bold')
t2.set_path_effects([pe.withStroke(linewidth=2.5, foreground='#1a0a2e')])

cb = fig.colorbar(im_siglip, cax=ax_cbar)
cb.set_label('Action grad norm', fontsize=8.5)

# ======= BOTTOM ROW: Conflict rate line plots =======
ax_cr_dino = fig.add_subplot(gs_bot[0, 0])
ax_cr_siglip = fig.add_subplot(gs_bot[0, 1], sharey=ax_cr_dino)

for cond, color, label in [
    ('Full_OCC_s0', COLORS['full_occ'], 'Full OCC'),
    ('Random_s2',   COLORS['random'],   'Random OCC'),
]:
    d = data[(cond, 'dino')]
    idxs = sorted(d['conflict_rate'].keys())
    crs = [d['conflict_rate'][i] for i in idxs]
    ax_cr_dino.plot(idxs, crs, color=color, label=label,
                    linewidth=1.4, alpha=0.85, marker='o', markersize=2.5,
                    markeredgewidth=0, zorder=3)

ax_cr_dino.axhline(0.5, color='#888888', linestyle='--', linewidth=0.6, alpha=0.5, zorder=1)
ax_cr_dino.text(22, 0.503, '50%', fontsize=6.5, color='#888888', ha='right', va='bottom')
ax_cr_dino.set_xlim(-0.5, 22.5)
ax_cr_dino.set_ylim(0.12, 0.52)
ax_cr_dino.set_xlabel('DINOv2 block index', fontsize=8.5)
ax_cr_dino.set_ylabel('Gradient conflict rate', fontsize=9)
ax_cr_dino.set_title(r'(c) DINOv2 — direction ($\approx$50% conflict)', fontsize=9.5, pad=5)
ax_cr_dino.set_xticks([0, 5, 10, 15, 20])
ax_cr_dino.legend(loc='lower left', framealpha=0.95, edgecolor='none')
ax_cr_dino.grid(True, alpha=0.10, axis='y', zorder=0)

for cond, color, label in [
    ('Full_OCC_s0', COLORS['full_occ'], 'Full OCC'),
    ('Random_s2',   COLORS['random'],   'Random OCC'),
]:
    d = data[(cond, 'siglip')]
    idxs = sorted(d['conflict_rate'].keys())
    crs = [d['conflict_rate'][i] for i in idxs]
    ax_cr_siglip.plot(idxs, crs, color=color, label=label,
                      linewidth=1.4, alpha=0.85, marker='o', markersize=2.5,
                      markeredgewidth=0, zorder=3)

ax_cr_siglip.axhline(0.5, color='#888888', linestyle='--', linewidth=0.6, alpha=0.5, zorder=1)
ax_cr_siglip.text(25, 0.503, '50%', fontsize=6.5, color='#888888', ha='right', va='bottom')
ax_cr_siglip.set_xlim(-0.5, 25.5)
ax_cr_siglip.set_xlabel('SigLIP block index', fontsize=8.5)
ax_cr_siglip.set_title('(d) SigLIP — direction (cooperative late)', fontsize=9.5, pad=5)
ax_cr_siglip.set_xticks([0, 5, 10, 15, 20, 25])
plt.setp(ax_cr_siglip.get_yticklabels(), visible=False)
ax_cr_siglip.grid(True, alpha=0.10, axis='y', zorder=0)

# Cooperative zone
ax_cr_siglip.axvspan(18.5, 25.5, alpha=0.06, color='#D55E00', zorder=0)
t3 = ax_cr_siglip.text(14.0, 0.145, 'cooperative zone\n(19–25% conflict)',
                        fontsize=7, color='#D55E00', fontstyle='italic',
                        ha='center', va='center', alpha=0.85)
t3.set_path_effects([pe.withStroke(linewidth=2.5, foreground='white')])
ax_cr_siglip.annotate('', xy=(19.5, 0.19), xytext=(16.5, 0.155),
                       arrowprops=dict(arrowstyle='->', color='#D55E00', lw=0.8, alpha=0.7))

for ax in [ax_cr_dino, ax_cr_siglip]:
    ax.tick_params(axis='both', which='both', length=3)

plt.savefig(OUT_DIR / 'per_layer_combined.pdf')
plt.savefig(OUT_DIR / 'per_layer_combined.png', dpi=300)
print(f'Saved to {OUT_DIR / "per_layer_combined.pdf"}')
plt.close()
