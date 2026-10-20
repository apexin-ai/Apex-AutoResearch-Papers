"""
Figure 3: V2 Per-Layer Gradient Analysis (DINOv2)
4-panel: (a) action norms, (b) aux norms, (c) cosine similarity, (d) norm ratio
Data: v2 codebase, seed 42, 200 batches at 50K steps.
"""
import json
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patheffects as pe
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
    'legend.fontsize': 7.5,
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

# Paper color palette
STYLES = {
    'Vanilla v2':      {'color': '#4C72B0', 'ls': ':', 'marker': 'x', 'label': 'Vanilla', 'lw': 1.2, 'ms': 3},
    'Full OCC BN v2':  {'color': '#C44E52', 'ls': '-', 'marker': '^', 'label': 'Full OCC (BN)', 'lw': 1.5, 'ms': 3.5},
    'Full OCC LN v2':  {'color': '#E69F00', 'ls': '-', 'marker': 'o', 'label': 'Full OCC (LN)', 'lw': 1.5, 'ms': 3.5},
    'Detach BN v2':    {'color': '#8172B3', 'ls': '--', 'marker': 'D', 'label': 'Detach (BN)', 'lw': 1.3, 'ms': 3},
    'Detach LN v2':    {'color': '#937860', 'ls': '--', 'marker': 's', 'label': 'Detach (LN)', 'lw': 1.3, 'ms': 3},
}

DATA_DIR = Path('/tmp/gradient_v2_5cond')
OUT_DIR = Path('/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/figures')

# === Load data ===
all_data = {}
for fpath in sorted(DATA_DIR.glob('*_gradient_stats.json')):
    with open(fpath) as f:
        d = json.load(f)
    cond = d['condition']
    all_data[cond] = d

def extract_dino_blocks(per_layer):
    blocks = {}
    for layer_name, stats in per_layer.items():
        if layer_name.startswith('featurizer.blocks.'):
            idx = int(layer_name.split('.')[2])
            blocks[idx] = stats
    return dict(sorted(blocks.items()))

# === Build arrays ===
dino_data = {}
for cond, d in all_data.items():
    blocks = extract_dino_blocks(d['per_layer'])
    idxs = np.array(sorted(blocks.keys()))
    action_norms = np.array([blocks[i]['action_grad_norm_mean'] for i in idxs])
    action_stds = np.array([blocks[i]['action_grad_norm_std'] for i in idxs])
    occ_norms = np.array([blocks[i].get('occ_grad_norm_mean') or 0 for i in idxs], dtype=float)
    occ_stds = np.array([blocks[i].get('occ_grad_norm_std') or 0 for i in idxs], dtype=float)
    cosine_means = np.array([blocks[i].get('cosine_sim_mean') or 0 for i in idxs], dtype=float)
    cosine_stds = np.array([blocks[i].get('cosine_sim_std') or 0 for i in idxs], dtype=float)
    conflict_rates = np.array([blocks[i].get('conflict_rate') or 0 for i in idxs], dtype=float)
    dino_data[cond] = {
        'idx': idxs, 'action_norm': action_norms, 'action_std': action_stds,
        'occ_norm': occ_norms, 'occ_std': occ_stds,
        'cosine': cosine_means, 'cosine_std': cosine_stds,
        'conflict': conflict_rates,
    }

vanilla_norms = dino_data['Vanilla v2']['action_norm']

# === Figure: 2x2 ===
fig, axes = plt.subplots(2, 2, figsize=(7.5, 4.8), gridspec_kw={'hspace': 0.45, 'wspace': 0.30})

# --- Panel (a): Action gradient norms ---
ax = axes[0, 0]
for cond in ['Vanilla v2', 'Full OCC BN v2', 'Full OCC LN v2', 'Detach BN v2', 'Detach LN v2']:
    s = STYLES[cond]
    d = dino_data[cond]
    ax.semilogy(d['idx'], d['action_norm'], color=s['color'], ls=s['ls'],
                lw=s['lw'], marker=s['marker'], markersize=s['ms'],
                markeredgewidth=0, alpha=0.85, label=s['label'])
    ax.fill_between(d['idx'],
                    np.maximum(d['action_norm'] - d['action_std'], 1e-4),
                    d['action_norm'] + d['action_std'],
                    alpha=0.05, color=s['color'])

ax.set_xlabel('DINOv2 block index')
ax.set_ylabel('Gradient L2 norm')
ax.set_title('(a) Action gradients: comparable across conditions', fontsize=9, pad=5)
ax.legend(loc='lower left', ncol=2, framealpha=0.95, edgecolor='none', fontsize=6.5,
          columnspacing=0.8, handlelength=1.5)
ax.grid(True, alpha=0.10, axis='y')
ax.set_xlim(-0.5, 22.5)

# --- Panel (b): Auxiliary gradient norms ---
ax = axes[0, 1]
for cond in ['Full OCC BN v2', 'Full OCC LN v2']:
    s = STYLES[cond]
    d = dino_data[cond]
    mask = d['occ_norm'] > 0
    ax.semilogy(d['idx'][mask], d['occ_norm'][mask], color=s['color'], ls=s['ls'],
                lw=s['lw'], marker=s['marker'], markersize=s['ms'],
                markeredgewidth=0, alpha=0.85, label=s['label'])
    ax.fill_between(d['idx'][mask],
                    np.maximum(d['occ_norm'][mask] - d['occ_std'][mask], 1e-4),
                    d['occ_norm'][mask] + d['occ_std'][mask],
                    alpha=0.08, color=s['color'])

ax.set_xlabel('DINOv2 block index')
ax.set_ylabel('Gradient L2 norm')
ax.set_title('(b) Auxiliary gradients: 10$\\times$ smaller than action', fontsize=9, pad=5)
ax.legend(loc='lower right', framealpha=0.9, edgecolor='none', fontsize=7)
ax.grid(True, alpha=0.10, axis='y')
ax.set_xlim(-0.5, 22.5)

# --- Panel (c): Cosine similarity ---
ax = axes[1, 0]
for cond in ['Full OCC BN v2', 'Full OCC LN v2']:
    s = STYLES[cond]
    d = dino_data[cond]
    mask = d['cosine'] != 0
    ax.plot(d['idx'][mask], d['cosine'][mask], color=s['color'], ls=s['ls'],
            lw=s['lw'], marker=s['marker'], markersize=s['ms'],
            markeredgewidth=0, alpha=0.85, label=s['label'])
    # Very light band — std is large relative to mean, just hint at spread
    ax.fill_between(d['idx'][mask],
                    d['cosine'][mask] - d['cosine_std'][mask],
                    d['cosine'][mask] + d['cosine_std'][mask],
                    alpha=0.04, color=s['color'])

ax.axhline(0, color='#888888', linestyle='--', linewidth=0.6, alpha=0.5, zorder=1)
ax.set_ylim(-0.15, 0.15)
ax.set_xlabel('DINOv2 block index')
ax.set_ylabel('Cosine similarity')
ax.set_title(r'(c) Action–aux cosine: near zero ($\approx$46% conflict)', fontsize=9, pad=5)
ax.legend(loc='lower left', framealpha=0.95, edgecolor='none', fontsize=7)
ax.grid(True, alpha=0.10, axis='y')
ax.set_xlim(-0.5, 22.5)

# --- Panel (d): Norm ratio vs Vanilla ---
ax = axes[1, 1]
for cond in ['Full OCC BN v2', 'Full OCC LN v2', 'Detach BN v2', 'Detach LN v2']:
    s = STYLES[cond]
    d = dino_data[cond]
    safe_vanilla = np.where(vanilla_norms > 1e-6, vanilla_norms, 1.0)
    ratio = d['action_norm'] / safe_vanilla
    valid = vanilla_norms > 1e-6
    ax.plot(d['idx'][valid], ratio[valid], color=s['color'], ls=s['ls'],
            lw=s['lw'], marker=s['marker'], markersize=s['ms'],
            markeredgewidth=0, alpha=0.85, label=s['label'])

ax.axhline(1.0, color='#888888', linestyle='--', linewidth=0.8, alpha=0.5, zorder=1)
ax.set_xlabel('DINOv2 block index')
ax.set_ylabel('Ratio (condition / Vanilla)')
ax.set_title('(d) Norm ratio: no amplification', fontsize=9, pad=5)
ax.legend(loc='upper left', ncol=2, framealpha=0.9, edgecolor='none', fontsize=6.5,
          columnspacing=0.8, handlelength=1.5)
ax.grid(True, alpha=0.10, axis='y')
ax.set_xlim(-0.5, 22.5)

fig.savefig(OUT_DIR / 'gradient_analysis_v2_combined.pdf', bbox_inches='tight', pad_inches=0.05)
fig.savefig(OUT_DIR / 'gradient_analysis_v2_combined.png', dpi=300, bbox_inches='tight', pad_inches=0.05)
plt.close()
print('Saved gradient_analysis_v2_combined.pdf/png')
