#!/usr/bin/env python3
"""Combined Figure: (a) Factorial 2x2 interaction + (b) Gradient analysis 2x2."""

import json
import os
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patheffects as pe
import matplotlib.gridspec as gridspec
from pathlib import Path

# === Global settings ===
plt.rcParams.update({
    'font.family': 'serif',
    'font.serif': ['DejaVu Serif', 'Liberation Serif', 'Times New Roman'],
    'font.size': 7,
    'axes.titlesize': 7.5,
    'axes.labelsize': 7,
    'xtick.labelsize': 6.5,
    'ytick.labelsize': 6.5,
    'legend.fontsize': 6,
    'figure.dpi': 300,
    'savefig.dpi': 300,
    'savefig.bbox': 'tight',
    'savefig.pad_inches': 0.03,
    'axes.spines.top': False,
    'axes.spines.right': False,
    'lines.linewidth': 1.2,
    'axes.grid': False,
    'axes.linewidth': 0.6,
    'pdf.fonttype': 42,
    'ps.fonttype': 42,
    'mathtext.fontset': 'cm',
})

# === Colors ===
COLORS = {
    'vanilla':     '#4C72B0',
    'full_occ_bn': '#C44E52',
    'full_occ_ln': '#E69F00',
    'detach_bn':   '#8172B3',
    'detach_ln':   '#937860',
}

# === Factorial data ===
factorial_data = {
    'BN': {
        'OFF': {'mean': 0.767, 'std': 0.024, 'n': 4},
        'ON':  {'mean': 0.725, 'std': 0.064, 'n': 3},
    },
    'LN': {
        'OFF': {'mean': 0.802, 'std': 0.024, 'n': 3},
        'ON':  {'mean': 0.773, 'std': 0.027, 'n': 4},
    },
}
VANILLA_CAR = 0.745

# === Gradient styles ===
GRAD_STYLES = {
    'Vanilla v2':      {'color': COLORS['vanilla'],     'ls': ':', 'marker': 'x', 'label': 'Vanilla',        'lw': 1.0, 'ms': 2.5},
    'Full OCC BN v2':  {'color': COLORS['full_occ_bn'], 'ls': '-', 'marker': '^', 'label': 'Full OCC (BN)',  'lw': 1.2, 'ms': 2.5},
    'Full OCC LN v2':  {'color': COLORS['full_occ_ln'], 'ls': '-', 'marker': 'o', 'label': 'Full OCC (LN)',  'lw': 1.2, 'ms': 2.5},
    'Detach BN v2':    {'color': COLORS['detach_bn'],   'ls': '--', 'marker': 'D', 'label': 'Detach (BN)',   'lw': 1.0, 'ms': 2.2},
    'Detach LN v2':    {'color': COLORS['detach_ln'],   'ls': '--', 'marker': 's', 'label': 'Detach (LN)',   'lw': 1.0, 'ms': 2.2},
}

# === Load gradient data ===
DATA_DIR = Path('/tmp/gradient_v2_5cond')
all_data = {}
for fpath in sorted(DATA_DIR.glob('*_gradient_stats.json')):
    with open(fpath) as f:
        d = json.load(f)
    all_data[d['condition']] = d

def extract_dino_blocks(per_layer):
    blocks = {}
    for layer_name, stats in per_layer.items():
        if layer_name.startswith('featurizer.blocks.'):
            idx = int(layer_name.split('.')[2])
            blocks[idx] = stats
    return dict(sorted(blocks.items()))

dino_data = {}
for cond, d in all_data.items():
    blocks = extract_dino_blocks(d['per_layer'])
    idxs = np.array(sorted(blocks.keys()))
    dino_data[cond] = {
        'idx': idxs,
        'action_norm': np.array([blocks[i]['action_grad_norm_mean'] for i in idxs]),
        'action_std':  np.array([blocks[i]['action_grad_norm_std'] for i in idxs]),
        'occ_norm':    np.array([blocks[i].get('occ_grad_norm_mean') or 0 for i in idxs], dtype=float),
        'occ_std':     np.array([blocks[i].get('occ_grad_norm_std') or 0 for i in idxs], dtype=float),
        'cosine':      np.array([blocks[i].get('cosine_sim_mean') or 0 for i in idxs], dtype=float),
        'cosine_std':  np.array([blocks[i].get('cosine_sim_std') or 0 for i in idxs], dtype=float),
    }

vanilla_norms = dino_data['Vanilla v2']['action_norm']

# === Figure layout ===
fig = plt.figure(figsize=(7.0, 3.4))
gs = gridspec.GridSpec(1, 2, figure=fig, width_ratios=[0.33, 0.67], wspace=0.15)

# Left: factorial (a)
gs_left = gs[0].subgridspec(1, 1)
ax_fact = fig.add_subplot(gs_left[0])

# Right: gradient 2x2 (b)
gs_right = gs[1].subgridspec(2, 2, hspace=0.55, wspace=0.42)
ax_b = [[fig.add_subplot(gs_right[r, c]) for c in range(2)] for r in range(2)]

# ============================================================
# (a) Factorial interaction plot
# ============================================================
C_BN = COLORS['full_occ_bn']
C_LN = COLORS['full_occ_ln']
C_VAN = COLORS['vanilla']

ax = ax_fact
ax.axhspan(0.68, VANILLA_CAR, color=C_BN, alpha=0.03, zorder=0)
ax.axhline(y=VANILLA_CAR, color=C_VAN, linestyle=':', linewidth=0.8, alpha=0.5, zorder=1)
t_van = ax.text(0.97, VANILLA_CAR + 0.002, 'Vanilla (0.745)', fontsize=6,
                color=C_VAN, va='bottom', ha='right',
                transform=ax.get_yaxis_transform(), fontweight='medium')
t_van.set_path_effects([pe.withStroke(linewidth=2.5, foreground='white')])

x_positions = [0, 1]

bn_y = [factorial_data['BN']['OFF']['mean'], factorial_data['BN']['ON']['mean']]
bn_err = [factorial_data['BN'][gf]['std'] for gf in ['OFF', 'ON']]
ax.errorbar(x_positions, bn_y, yerr=bn_err, color=C_BN,
            marker='o', markersize=5.5, markeredgecolor='white', markeredgewidth=0.7,
            linestyle='-', linewidth=1.4, capsize=3, capthick=0.8,
            elinewidth=0.8, label='BatchNorm (BN)', zorder=3)

ln_y = [factorial_data['LN']['OFF']['mean'], factorial_data['LN']['ON']['mean']]
ln_err = [factorial_data['LN'][gf]['std'] for gf in ['OFF', 'ON']]
ax.errorbar(x_positions, ln_y, yerr=ln_err, color=C_LN,
            marker='s', markersize=5.5, markeredgecolor='white', markeredgewidth=0.7,
            linestyle=(0, (4, 2.5)), linewidth=1.4, capsize=3, capthick=0.8,
            elinewidth=0.8, label='LayerNorm (LN)', zorder=3)

# Delta annotations
delta_bn = (factorial_data['BN']['ON']['mean'] - factorial_data['BN']['OFF']['mean']) * 100
delta_ln = (factorial_data['LN']['ON']['mean'] - factorial_data['LN']['OFF']['mean']) * 100

mid_bn_y = np.mean(bn_y)
t_bn = ax.annotate(f'−{abs(delta_bn):.1f} pp', xy=(0.55, mid_bn_y - 0.008),
                   fontsize=7, fontweight='bold', color=C_BN, ha='center', va='top', zorder=5)
t_bn.set_path_effects([pe.withStroke(linewidth=2, foreground='white')])

mid_ln_y = np.mean(ln_y)
t_ln = ax.annotate(f'−{abs(delta_ln):.1f} pp', xy=(0.45, mid_ln_y + 0.008),
                   fontsize=7, fontweight='bold', color=C_LN, ha='center', va='bottom', zorder=5)
t_ln.set_path_effects([pe.withStroke(linewidth=2, foreground='white')])

# n-labels
n_offsets = {
    ('BN', 'OFF'): (-12, -10),
    ('BN', 'ON'):  (12, -14),
    ('LN', 'OFF'): (-12, 8),
    ('LN', 'ON'):  (12, 10),
}
for gf_idx, gf in enumerate(['OFF', 'ON']):
    for norm in ['BN', 'LN']:
        n_val = factorial_data[norm][gf]['n']
        y_val = factorial_data[norm][gf]['mean']
        ox, oy = n_offsets[(norm, gf)]
        c = C_BN if norm == 'BN' else C_LN
        ax.annotate(f'n={n_val}', (x_positions[gf_idx], y_val),
                    xytext=(ox, oy), textcoords='offset points',
                    fontsize=5.5, color=c, ha='center', fontstyle='italic', alpha=0.6)

ax.set_xticks(x_positions)
ax.set_xticklabels(['OFF\n(Detach)', 'ON\n(Full)'], fontsize=7)
ax.set_xlabel('Gradient Flow', fontsize=8)
ax.set_ylabel('Collision Avoidance Rate (CAR)', fontsize=8)
ax.set_xlim(-0.3, 1.3)
ax.set_ylim(0.68, 0.86)
ax.yaxis.set_major_locator(plt.MultipleLocator(0.02))
ax.legend(loc='upper right', frameon=True, framealpha=0.95, edgecolor='none',
          handlelength=2.0, handletextpad=0.4, fontsize=6.5)

# Panel label
ax.text(-0.18, 1.08, '(a)', transform=ax.transAxes, fontsize=9.5, fontweight='bold', va='top')

# ============================================================
# (b) Gradient analysis 2x2
# ============================================================

# --- (b) Panel label on top-left of gradient region ---
ax_b[0][0].text(-0.22, 1.18, '(b)', transform=ax_b[0][0].transAxes,
                fontsize=9.5, fontweight='bold', va='top')

# --- b-i: Action gradient norms ---
ax = ax_b[0][0]
for cond in ['Vanilla v2', 'Full OCC BN v2', 'Full OCC LN v2', 'Detach BN v2', 'Detach LN v2']:
    s = GRAD_STYLES[cond]
    d = dino_data[cond]
    ax.semilogy(d['idx'], d['action_norm'], color=s['color'], ls=s['ls'],
                lw=s['lw'], marker=s['marker'], markersize=s['ms'],
                markeredgewidth=0, alpha=0.85, label=s['label'])
    ax.fill_between(d['idx'],
                    np.maximum(d['action_norm'] - d['action_std'], 1e-4),
                    d['action_norm'] + d['action_std'],
                    alpha=0.04, color=s['color'])
ax.set_ylabel('Gradient L2 norm', fontsize=8)
ax.set_title('Action norms', fontsize=9, pad=3)
ax.legend(loc='lower left', ncol=2, framealpha=0.95, edgecolor='none', fontsize=7,
          columnspacing=0.6, handlelength=1.2, handletextpad=0.3)
ax.grid(True, alpha=0.08, axis='y')
ax.set_xlim(-0.5, 22.5)
ax.tick_params(labelsize=7)

# --- b-ii: Auxiliary gradient norms ---
ax = ax_b[0][1]
for cond in ['Full OCC BN v2', 'Full OCC LN v2']:
    s = GRAD_STYLES[cond]
    d = dino_data[cond]
    mask = d['occ_norm'] > 0
    ax.semilogy(d['idx'][mask], d['occ_norm'][mask], color=s['color'], ls=s['ls'],
                lw=s['lw'], marker=s['marker'], markersize=s['ms'],
                markeredgewidth=0, alpha=0.85, label=s['label'])
    ax.fill_between(d['idx'][mask],
                    np.maximum(d['occ_norm'][mask] - d['occ_std'][mask], 1e-4),
                    d['occ_norm'][mask] + d['occ_std'][mask],
                    alpha=0.06, color=s['color'])
ax.set_ylabel('Gradient L2 norm', fontsize=8)
ax.set_title(r'Aux norms (10$\times$)', fontsize=9, pad=3)
ax.grid(True, alpha=0.08, axis='y')
ax.set_xlim(-0.5, 22.5)
ax.tick_params(labelsize=7)

# --- b-iii: Cosine similarity ---
ax = ax_b[1][0]
for cond in ['Full OCC BN v2', 'Full OCC LN v2']:
    s = GRAD_STYLES[cond]
    d = dino_data[cond]
    mask = d['cosine'] != 0
    ax.plot(d['idx'][mask], d['cosine'][mask], color=s['color'], ls=s['ls'],
            lw=s['lw'], marker=s['marker'], markersize=s['ms'],
            markeredgewidth=0, alpha=0.85, label=s['label'])
    ax.fill_between(d['idx'][mask],
                    d['cosine'][mask] - d['cosine_std'][mask],
                    d['cosine'][mask] + d['cosine_std'][mask],
                    alpha=0.03, color=s['color'])
ax.axhline(0, color='#888888', linestyle='--', linewidth=0.5, alpha=0.5, zorder=1)
ax.set_ylim(-0.15, 0.15)
ax.set_xlabel('DINOv2 block index', fontsize=8)
ax.set_ylabel('Cosine similarity', fontsize=8)
ax.set_title(r'Cosine sim. ($\approx$46% conflict)', fontsize=9, pad=3)
ax.grid(True, alpha=0.08, axis='y')
ax.set_xlim(-0.5, 22.5)
ax.tick_params(labelsize=7)

# --- b-iv: Norm ratio ---
ax = ax_b[1][1]
for cond in ['Full OCC BN v2', 'Full OCC LN v2', 'Detach BN v2', 'Detach LN v2']:
    s = GRAD_STYLES[cond]
    d = dino_data[cond]
    safe_vanilla = np.where(vanilla_norms > 1e-6, vanilla_norms, 1.0)
    ratio = d['action_norm'] / safe_vanilla
    valid = vanilla_norms > 1e-6
    ax.plot(d['idx'][valid], ratio[valid], color=s['color'], ls=s['ls'],
            lw=s['lw'], marker=s['marker'], markersize=s['ms'],
            markeredgewidth=0, alpha=0.85, label=s['label'])
ax.axhline(1.0, color='#888888', linestyle='--', linewidth=0.6, alpha=0.5, zorder=1)
ax.set_xlabel('DINOv2 block index', fontsize=8)
ax.set_ylabel('Ratio (cond. / Vanilla)', fontsize=8)
ax.set_title('Norm ratio', fontsize=9, pad=3)
ax.grid(True, alpha=0.08, axis='y')
ax.set_xlim(-0.5, 22.5)
ax.tick_params(labelsize=7)

# Remove x-labels from top row of (b)
for c in range(2):
    ax_b[0][c].set_xlabel('')

# === Save ===
OUT_DIR = Path('/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/figures')
for fmt in ['pdf', 'png']:
    path = OUT_DIR / f'fig_combined_factorial_gradient.{fmt}'
    fig.savefig(path)
    print(f'Saved: {path}')
plt.close(fig)
