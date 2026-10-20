#!/usr/bin/env python3
"""Fig 3: NVE Diagnostic — Task B2 CIVO detection (D054 corrected).
008e_v3_s2 reclassified as non-CIVO (IRD), shown as FP.
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import os

plt.rcParams.update({
    'font.family': 'DejaVu Sans',
    'font.size': 11,
    'axes.titlesize': 13,
    'axes.labelsize': 12,
    'xtick.labelsize': 10,
    'ytick.labelsize': 10,
    'legend.fontsize': 9.5,
    'figure.dpi': 300,
    'savefig.dpi': 300,
    'savefig.bbox': 'tight',
    'savefig.pad_inches': 0.05,
    'axes.spines.top': False,
    'axes.spines.right': False,
    'lines.linewidth': 1.8,
})

tp = [('006', 4.84), ('008d', 4.13), ('009b', 1.62)]
tn = [('001', 1.00), ('008a', 0.93), ('008f', 0.97), ('008e_v3_s1', 0.94)]
fp = [('008e_v3_s2', 3.78)]
THRESHOLD = 1.5

all_points = []
for name, nve in tn:
    all_points.append((name, nve, 'TN'))
for name, nve in fp:
    all_points.append((name, nve, 'FP'))
for name, nve in tp:
    all_points.append((name, nve, 'TP'))
all_points.sort(key=lambda x: x[1])

labels = [p[0] for p in all_points]
nves   = [p[1] for p in all_points]
types  = [p[2] for p in all_points]
y_pos  = np.arange(len(all_points))

COLOR_TP = '#D55E00'   # orange (Wong) — was red #C0392B
COLOR_TN = '#0072B2'   # blue (Wong) — was #2471A3
COLOR_FP = '#CC79A7'   # reddish purple (Wong) — was #E67E22

fig, ax = plt.subplots(figsize=(8, 4.5))

ax.axvspan(0, THRESHOLD, alpha=0.06, color=COLOR_TN, zorder=0)
ax.axvspan(THRESHOLD, 5.8, alpha=0.06, color=COLOR_TP, zorder=0)
ax.axvline(x=THRESHOLD, color='#7F8C8D', linestyle='--', linewidth=1.2, zorder=1)

for i, (name, nve, tp_type) in enumerate(all_points):
    if tp_type == 'TP':
        color, marker, ms = COLOR_TP, 'o', 9
    elif tp_type == 'FP':
        color, marker, ms = COLOR_FP, 'D', 9
    else:
        color, marker, ms = COLOR_TN, 's', 8

    ax.plot(nve, i, marker=marker, color=color, markersize=ms,
            markeredgecolor='white', markeredgewidth=1.2, zorder=4)
    ax.plot([0, nve], [i, i], color=color, linewidth=1.0, alpha=0.35, zorder=2)

    if tp_type == 'FP':
        ax.annotate('FP (IRD, non-CIVO)',
                     xy=(nve, i), xytext=(nve + 0.15, i - 0.7),
                     fontsize=8.5, fontweight='bold', color=COLOR_FP,
                     arrowprops=dict(arrowstyle='->', color=COLOR_FP, lw=1.2),
                     zorder=5)

ax.set_yticks(y_pos)
ax.set_yticklabels(labels, fontsize=10, family='monospace')
ax.set_xlabel('Normalized Value Excess (NVE)', fontsize=12)
ax.set_xlim(-0.15, 5.8)
ax.set_ylim(-1.0, len(all_points) + 0.2)

ax.text(THRESHOLD / 2, len(all_points) + 0.05, 'Non-CIVO',
        ha='center', va='bottom', fontsize=9, color=COLOR_TN, alpha=0.6,
        fontweight='bold')
ax.text(THRESHOLD + (5.8 - THRESHOLD) / 2, len(all_points) + 0.05,
        'CIVO-positive',
        ha='center', va='bottom', fontsize=9, color=COLOR_TP, alpha=0.6,
        fontweight='bold')

h_tp = plt.Line2D([], [], marker='o', color=COLOR_TP, markersize=8,
                   markeredgecolor='white', markeredgewidth=1, linestyle='None',
                   label='True CIVO (TP)')
h_tn = plt.Line2D([], [], marker='s', color=COLOR_TN, markersize=7,
                   markeredgecolor='white', markeredgewidth=1, linestyle='None',
                   label='Non-CIVO (TN)')
h_fp = plt.Line2D([], [], marker='D', color=COLOR_FP, markersize=8,
                   markeredgecolor='white', markeredgewidth=1, linestyle='None',
                   label='False Positive (FP)')
h_th = plt.Line2D([], [], color='#7F8C8D', linestyle='--', linewidth=1.2,
                   label=f'Threshold ({THRESHOLD}x)')
ax.legend(handles=[h_tp, h_tn, h_fp, h_th], loc='upper left',
          fontsize=9, framealpha=0.92, edgecolor='#BDC3C7')

stats_text = (
    'AUROC = 0.933   CI [0.47, 1.0]\n'
    'Accuracy = 7/8 (87.5%)\n'
    r'Task B2: NVE $\geq$ 1.5$\times$ @ 35K+'
    '\n(Clopper–Pearson, 95%)'
)
ax.text(0.98, 0.03, stats_text, transform=ax.transAxes,
        ha='right', va='bottom', fontsize=9.5,
        bbox=dict(boxstyle='round,pad=0.4', facecolor='#FAFAFA',
                  edgecolor='#BDC3C7', alpha=0.95))

ax.set_title('NVE Diagnostic: CIVO Detection (D054 Corrected)', fontsize=13,
             fontweight='bold', pad=12)
ax.grid(True, alpha=0.15, axis='x', zorder=0)

plt.tight_layout()

outdir = os.environ.get('OUTDIR', '.')
os.makedirs(outdir, exist_ok=True)
plt.savefig(f'{outdir}/fig3_nve_diagnostic_d054.pdf')
plt.savefig(f'{outdir}/fig3_nve_diagnostic_d054.png')
plt.close()
print(f'Saved: {outdir}/fig3_nve_diagnostic_d054.pdf')
print(f'Saved: {outdir}/fig3_nve_diagnostic_d054.png')
