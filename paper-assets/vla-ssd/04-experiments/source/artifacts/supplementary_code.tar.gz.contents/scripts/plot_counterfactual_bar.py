#!/usr/bin/env python3
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
matplotlib.rcParams['pdf.fonttype'] = 42
matplotlib.rcParams['ps.fonttype'] = 42
import numpy as np
import os

COLORS = {
    'empty': '#E69F00',
    'wrong': '#56B4E9',
    'shuffled': '#009E73',
    'paraphrased': '#CC79A7',
}
EDGE = {
    'empty': '#C78600',
    'wrong': '#3A96C8',
    'shuffled': '#007A5A',
    'paraphrased': '#A85D87',
}

conditions = ['empty', 'wrong', 'shuffled', 'paraphrased']
cond_labels = ['Empty', 'Wrong', 'Shuffled', 'Paraphrased']
n_cond = len(conditions)

# ── Panel A data: Cohen's d ──
cohens_d = {
    'OV-G': [1.17, 1.18, 1.10, 1.00],
    'OV-S': [1.18, 0.88, 0.99, 0.81],
    'OV-O': [1.21, 1.19, 1.12, 0.90],
    'OV-L': [0.50, 0.56, 0.56, 0.45],
    'TV-G': [1.52, 1.40, 1.34, 1.21],
    'TV-S': [1.33, 1.29, 1.18, 1.19],
    'TV-O': [1.21, 1.16, 1.06, 0.97],
    'TV-L': [1.47, 1.42, 1.39, 1.16],
}

# ── Panel B data: Cosine distance ──
cosine_dist = {
    'G':    [1.0,    1.0,    1.0,    1.0],
    'S':    [0.24,   0.275,  0.12,   0.03],
    'G.':   [0.1530, 0.0160, 0.0839, 0.0043],
    'S.':   [0.1805, 0.0046, 0.1395, 0.0044],
    'O':    [0.1850, 0.0044, 0.0977, 0.0052],
    'L':    [0.1734, 0.0221, 0.1204, 0.0070],
    'G..':  [0.0814, 0.0143, 0.0332, 0.0041],
    'S..':  [0.0807, 0.0020, 0.0313, 0.0047],
}
panelB_display = ['G', 'S', 'G', 'S', 'O', 'L', 'G', 'S']
panelB_regions = [
    ('NORA\n(trained)', 0, 2),
    ('Phi-3-Vision\n(ref)', 2, 6),
    ('Qwen2.5-VL\n(ref)', 6, 8),
]

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(3.5, 7),
                                gridspec_kw={'height_ratios': [3, 2.5]})

# ── Panel A ──
bar_w = 0.20
groups_a = list(cohens_d.keys())
n_a = len(groups_a)
boundary = 4

positions_a = np.zeros(n_a)
gap = 0.6
for i in range(n_a):
    positions_a[i] = float(i) + (gap if i >= boundary else 0)

for j, cond in enumerate(conditions):
    offset = (j - (n_cond - 1) / 2) * bar_w
    vals = [cohens_d[g][j] for g in groups_a]
    ax1.bar(positions_a + offset, vals, bar_w,
            color=COLORS[cond], edgecolor=EDGE[cond], linewidth=0.8,
            label=cond_labels[j], zorder=3)

for i, g in enumerate(groups_a):
    vals = cohens_d[g]
    mx = int(np.argmax(vals))
    offset = (mx - (n_cond - 1) / 2) * bar_w
    ax1.text(positions_a[i] + offset, vals[mx] + 0.03, '*',
             ha='center', va='bottom', fontsize=8, fontweight='bold', color='#333333')

ax1.axhline(y=0.8, color='gray', linestyle='--', alpha=0.5, linewidth=1, zorder=1)
ax1.text(positions_a[-1] + 0.3, 0.82, 'large effect', fontsize=6, color='gray',
         alpha=0.7, va='bottom', ha='left')

sep_x = (positions_a[boundary - 1] + positions_a[boundary]) / 2
ax1.axvline(x=sep_x, color='gray', linestyle=':', alpha=0.4, linewidth=1)

ax1.set_xticks(positions_a)
ax1.set_xticklabels(groups_a, fontsize=7, rotation=45, ha='right')
ax1.set_ylabel("Cohen's d", fontsize=8)
ax1.set_ylim(0, 1.8)
ax1.set_title("(a) Cohen's d: OpenVLA & TracVLA", fontsize=9, fontweight='bold', loc='left')
ax1.spines['top'].set_visible(False)
ax1.spines['right'].set_visible(False)
ax1.tick_params(axis='y', labelsize=7)
ax1.grid(axis='y', alpha=0.2, linewidth=0.5)
ax1.legend(loc='upper right', ncol=2, fontsize=6, framealpha=0.9,
           edgecolor='gray', handlelength=1.0, handletextpad=0.3, columnspacing=0.6)

# ── Panel B ──
bar_w_b = 0.18
groups_b = list(cosine_dist.keys())
n_b = len(groups_b)

positions_b = np.zeros(n_b)
region_gap = 0.9
pos = 0.0
for i in range(n_b):
    if i == 2 or i == 6:
        pos += region_gap
    positions_b[i] = pos
    pos += 1.0

ylim_b = (0, 0.35)
sat_cap = ylim_b[1] * 0.85

for j, cond in enumerate(conditions):
    offset = (j - (n_cond - 1) / 2) * bar_w_b
    vals = [cosine_dist[g][j] for g in groups_b]
    bars = ax2.bar(positions_b + offset, vals, bar_w_b,
                   color=COLORS[cond], edgecolor=EDGE[cond], linewidth=0.8,
                   label=cond_labels[j] if j < 4 else None, zorder=3)
    for k, (bar, v) in enumerate(zip(bars, vals)):
        if v >= 0.95:
            bar.set_height(sat_cap)
            if j == 0:
                ax2.text(bar.get_x() + bar.get_width() / 2 + bar_w_b * 0.8,
                         sat_cap + 0.005, '1.0\n(sat.)', ha='center', va='bottom',
                         fontsize=4.5, fontweight='bold', color='#333333')

for rname, rstart, rend in panelB_regions:
    if rstart > 0:
        sx = (positions_b[rstart - 1] + positions_b[rstart]) / 2
        ax2.axvline(x=sx, color='gray', linestyle=':', alpha=0.5, linewidth=1)

for rname, rstart, rend in panelB_regions:
    center = (positions_b[rstart] + positions_b[rend - 1]) / 2
    ax2.text(center, -0.12, rname, ha='center', va='top', fontsize=6,
             fontweight='bold', transform=ax2.get_xaxis_transform())

ax2.set_xticks(positions_b)
ax2.set_xticklabels(panelB_display, fontsize=7, rotation=0, ha='center')
ax2.set_ylabel('Cosine distance', fontsize=8)
ax2.set_ylim(ylim_b)
ax2.set_title('(b) Cosine distance: NORA & reference VLMs', fontsize=9, fontweight='bold', loc='left')
ax2.spines['top'].set_visible(False)
ax2.spines['right'].set_visible(False)
ax2.tick_params(axis='y', labelsize=7)
ax2.tick_params(axis='x', pad=8)
ax2.grid(axis='y', alpha=0.2, linewidth=0.5)

plt.tight_layout(pad=0.3)
plt.subplots_adjust(bottom=0.08)

# ── Save ──
out_dir = '/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/figures'
art_dir = '/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/figures/paper'

for d in [out_dir, art_dir]:
    os.makedirs(d, exist_ok=True)
    fig.savefig(f'{d}/fig_counterfactual_bar.pdf', dpi=300, bbox_inches='tight')
    fig.savefig(f'{d}/fig_counterfactual_bar.png', dpi=300, bbox_inches='tight')
plt.close()
print('Done.')
