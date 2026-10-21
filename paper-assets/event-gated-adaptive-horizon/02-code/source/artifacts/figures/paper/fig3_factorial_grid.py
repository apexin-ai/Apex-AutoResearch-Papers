#!/usr/bin/env python3
"""Fig 3: Factorial experiment summary — 2×2 grid + control annotation.
Rows: Subsample (OFF/ON), Cols: Horizon (H=15/H=8).
All cells use trained dt_embedding. Control (008f, no dt_emb) annotated separately.
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from fig_style import apply_style
apply_style()

BASELINE_EVAL = 915.67

grid_data = {
    (0, 0): {'config': '008a', 'eval': 777.7, 'nve': 0.59, 'step': '105K',
             'collapsed': False, 'h': 15, 'sub': 'OFF'},
    (0, 1): {'config': '008c', 'eval': 240.9, 'nve': 0.58, 'step': '65K',
             'collapsed': False, 'h': 8, 'sub': 'OFF'},
    (1, 0): {'config': '006',  'eval': 132.9, 'nve': 4.83, 'step': '65K',
             'collapsed': True, 'h': 15, 'sub': 'ON'},
    (1, 1): {'config': '008d', 'eval': 82.8,  'nve': 4.12, 'step': '55K',
             'collapsed': True, 'h': 8, 'sub': 'ON'},
}

control = {'config': '008f', 'eval': 503.0, 'nve': 0.30, 'step': '105K',
           'label': 'No dt_emb\n(control)'}

fig, ax = plt.subplots(figsize=(7.5, 5))
ax.set_xlim(-0.5, 3.8)
ax.set_ylim(-0.5, 2.5)
ax.axis('off')

cell_w, cell_h = 1.3, 0.9
x_offsets = [0, 1.5]
y_offsets = [1.2, 0]

col_labels = ['H = 15', 'H = 8']
row_labels = ['Subsample OFF', 'Subsample ON']

for ci, xl in enumerate(col_labels):
    ax.text(x_offsets[ci] + cell_w / 2, y_offsets[0] + cell_h + 0.15, xl,
            ha='center', va='bottom', fontsize=12, fontweight='bold')

for ri, rl in enumerate(row_labels):
    ax.text(x_offsets[0] - 0.12, y_offsets[ri] + cell_h / 2, rl,
            ha='right', va='center', fontsize=11, fontweight='bold', rotation=0)

for (row, col), d in grid_data.items():
    x = x_offsets[col]
    y = y_offsets[row]

    if d['collapsed']:
        bg_color = '#FDE8D0'       # light orange (was light red)
        border_color = '#D55E00'   # orange Wong (was red #E74C3C)
        status_symbol = r'$\times$'
        status_color = '#D55E00'   # orange Wong (was dark red #C0392B)
    else:
        bg_color = '#D6EAF8'       # light blue (was light green)
        border_color = '#0072B2'   # blue Wong (was green #27AE60)
        status_symbol = r'$\checkmark$'
        status_color = '#0072B2'   # blue Wong (was dark green #1E8449)

    rect = mpatches.FancyBboxPatch(
        (x, y), cell_w, cell_h,
        boxstyle='round,pad=0.05',
        facecolor=bg_color, edgecolor=border_color, linewidth=2)
    ax.add_patch(rect)

    pct = d['eval'] / BASELINE_EVAL * 100
    ax.text(x + cell_w / 2, y + cell_h * 0.72,
            f"{d['config']}",
            ha='center', va='center', fontsize=10, fontweight='bold', color='#333')
    ax.text(x + cell_w / 2, y + cell_h * 0.48,
            f"eval = {d['eval']:.0f}  ({pct:.0f}%)",
            ha='center', va='center', fontsize=9.5, color='#333')
    ax.text(x + cell_w / 2, y + cell_h * 0.25,
            f"nve = {d['nve']:.2f}×  {status_symbol}",
            ha='center', va='center', fontsize=9.5, color=status_color,
            fontweight='bold')

ctrl_x = x_offsets[1] + cell_w + 0.45
ctrl_y = y_offsets[1]
ctrl_w, ctrl_h = 1.15, cell_h

ctrl_rect = mpatches.FancyBboxPatch(
    (ctrl_x, ctrl_y), ctrl_w, ctrl_h,
    boxstyle='round,pad=0.05',
    facecolor='#EBF5FB', edgecolor='#2980B9', linewidth=2, linestyle='--')
ax.add_patch(ctrl_rect)

ax.text(ctrl_x + ctrl_w / 2, ctrl_y + ctrl_h * 0.78,
        control['label'], ha='center', va='center', fontsize=9.5,
        fontweight='bold', color='#2471A3')
ax.text(ctrl_x + ctrl_w / 2, ctrl_y + ctrl_h * 0.45,
        f"eval = {control['eval']:.0f}  ({control['eval']/BASELINE_EVAL*100:.0f}%)",
        ha='center', va='center', fontsize=9, color='#2471A3')
ax.text(ctrl_x + ctrl_w / 2, ctrl_y + ctrl_h * 0.22,
        f"nve = {control['nve']:.2f}×  " + r"$\checkmark$",
        ha='center', va='center', fontsize=9, color='#0072B2', fontweight='bold')

ax.annotate('', xy=(x_offsets[1] + cell_w + 0.05, y_offsets[1] + cell_h / 2),
            xytext=(ctrl_x - 0.05, ctrl_y + ctrl_h / 2),
            arrowprops=dict(arrowstyle='<->', color='#7F8C8D', lw=1.5,
                            connectionstyle='arc3,rad=0'))
ax.text((x_offsets[1] + cell_w + ctrl_x) / 2, y_offsets[1] - 0.12,
        'same config,\nminus trained dt_emb',
        ha='center', va='top', fontsize=8.5, color='#7F8C8D', style='italic')

ax.axhline(y=y_offsets[0] - 0.15, xmin=0.02, xmax=0.65, color='#BDC3C7',
           linewidth=0.8, linestyle='-')

ax.text((x_offsets[0] + x_offsets[1] + cell_w) / 2, y_offsets[0] + cell_h + 0.45,
        'Factorial Design: Trained dt_embedding × Subsample × Horizon',
        ha='center', va='bottom', fontsize=13, fontweight='bold')

ax.text((x_offsets[0] + x_offsets[1] + cell_w) / 2, -0.45,
        f'Baseline (exp_001): eval = {BASELINE_EVAL:.1f} | '
        'Subsample ON + trained dt_emb → collapse (2/2); '
        'removing dt_emb prevents it',
        ha='center', va='top', fontsize=9, color='#555', style='italic')

outdir = '/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/figures/paper'
plt.savefig(f'{outdir}/fig3_factorial_grid.pdf')
plt.savefig(f'{outdir}/fig3_factorial_grid.png')
plt.close()
print('Saved fig3_factorial_grid.pdf and .png')
