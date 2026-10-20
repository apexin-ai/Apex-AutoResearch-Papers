#!/usr/bin/env python3
"""Consensus heatmap: 7 rows (5 methods + K≥3 + K≥4) × 12 α values.
Data format: fraction strings like '6/8'."""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import csv
import sys
import os

plt.rcParams.update({
    'font.family': 'DejaVu Sans',
    'font.size': 13,
    'axes.titlesize': 14,
    'axes.labelsize': 14,
    'xtick.labelsize': 12,
    'ytick.labelsize': 12,
    'legend.fontsize': 12,
    'figure.dpi': 300,
    'savefig.dpi': 300,
    'savefig.bbox': 'tight',
    'savefig.pad_inches': 0.05,
    'pdf.fonttype': 42,
})

def parse_frac(s):
    s = s.strip()
    if '/' in s:
        num, den = s.split('/')
        return int(num) / int(den)
    return float(s)

csv_path = sys.argv[1] if len(sys.argv) > 1 else 'consensus_heatmap_data.csv'
out_dir = sys.argv[2] if len(sys.argv) > 2 else '.'

rows = []
with open(csv_path) as f:
    reader = csv.DictReader(f)
    for r in reader:
        rows.append(r)

alphas = [float(r['alpha']) for r in rows]
n = len(alphas)
alpha_labels = [f'{a:.2f}' for a in alphas]

method_keys = ['naive_fwd', 'diff_fwd', 'threshold_fwd', 'permG_fwd', 'ty_fwd', 'K_ge3', 'K_ge4']
method_labels = ['Naive XCorr', 'Diff. XCorr', 'Threshold (3σ)', 'Perm. Granger', 'Toda–Yamamoto',
                  '$K{\\geq}3$ consensus', '$K{\\geq}4$ consensus']

data = np.array([[parse_frac(r[k]) for r in rows] for k in method_keys]) * 100
regimes = [r['regime'] for r in rows]

fig, ax = plt.subplots(figsize=(7.5, 3.8))

cmap = plt.cm.YlOrRd
im = ax.imshow(data, cmap=cmap, aspect='auto', vmin=0, vmax=100, interpolation='nearest')

for i in range(len(method_labels)):
    for j in range(n):
        val = data[i, j]
        color = 'white' if val > 65 else 'black'
        ax.text(j, i, f'{val:.0f}', ha='center', va='center',
                fontsize=10.5, color=color, fontweight='bold' if val >= 75 else 'normal')

ax.set_yticks(range(len(method_labels)))
ax.set_yticklabels(method_labels)
ax.set_xticks(range(n))
ax.set_xticklabels(alpha_labels)
ax.set_xlabel('Contamination level (α)')

ax.axhline(4.5, color='white', linewidth=2.5)

regime_colors = {'blind_zone': '#FDEDEC', 'onset': '#FEF9E7', 'sync_collapse': '#F4ECF7', 'detection': '#EBF5FB'}
regime_names = {'blind_zone': 'Blind spot', 'onset': 'Onset', 'sync_collapse': 'Sync.', 'detection': 'Detection'}
for j, reg in enumerate(regimes):
    color = regime_colors.get(reg, '#FFFFFF')
    rect = plt.Rectangle((j - 0.5, -0.9), 1, 0.4, facecolor=color, edgecolor='none',
                           clip_on=False, zorder=10)
    ax.add_patch(rect)

regime_spans = {}
for j, reg in enumerate(regimes):
    regime_spans.setdefault(reg, []).append(j)
for reg, cols in regime_spans.items():
    mid = (min(cols) + max(cols)) / 2
    ax.text(mid, -0.7, regime_names.get(reg, reg), ha='center', va='center',
            fontsize=10, color='#555555', fontstyle='italic', clip_on=False, zorder=11)

# PermG FPR=0 in blind zone
blind_cols = [j for j, r in enumerate(regimes) if r == 'blind_zone']
if blind_cols:
    rect = plt.Rectangle((min(blind_cols)-0.5, 3-0.5), len(blind_cols), 1,
                           linewidth=1.8, edgecolor='#009E73', facecolor='none',
                           linestyle='--', zorder=10)
    ax.add_patch(rect)

# K≥3 maintained at 6/8 in sync_collapse
idx_060 = [j for j, a in enumerate(alphas) if abs(a - 0.60) < 0.01]
if idx_060:
    j = idx_060[0]
    rect2 = plt.Rectangle((j-0.5, 5-0.5), 1, 1,
                            linewidth=1.8, edgecolor='#D55E00', facecolor='none',
                            linestyle='-', zorder=10)
    ax.add_patch(rect2)

# TY=100% at α=0.60
if idx_060:
    j = idx_060[0]
    rect3 = plt.Rectangle((j-0.5, 4-0.5), 1, 1,
                            linewidth=1.5, edgecolor='#D55E00', facecolor='none',
                            linestyle=':', zorder=10)
    ax.add_patch(rect3)

cbar = plt.colorbar(im, ax=ax, fraction=0.03, pad=0.04, label='Detection rate (%)')

ax.set_title('Method × regime consensus heatmap (Pythia-410M, fp32, 12 contamination levels)',
             fontsize=13, pad=14)

plt.tight_layout()

pdf_path = os.path.join(out_dir, 'consensus_heatmap.pdf')
png_path = os.path.join(out_dir, 'consensus_heatmap.png')
plt.savefig(pdf_path)
plt.savefig(png_path)
plt.close()
print(f'Saved: {pdf_path}')
print(f'Saved: {png_path}')
