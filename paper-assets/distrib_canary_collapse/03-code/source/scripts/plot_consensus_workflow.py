#!/usr/bin/env python3
"""Generate Consensus Framework Workflow figure (Fig 5 candidate)."""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import matplotlib.patches as mpatches
import numpy as np
import json
import os

plt.rcParams.update({
    'font.family': 'DejaVu Sans',
    'font.size': 11,
    'axes.titlesize': 13,
    'axes.labelsize': 12,
    'xtick.labelsize': 10,
    'ytick.labelsize': 10,
    'legend.fontsize': 10,
    'figure.dpi': 300,
    'savefig.dpi': 300,
    'savefig.bbox': 'tight',
    'savefig.pad_inches': 0.05,
    'axes.spines.top': False,
    'axes.spines.right': False,
    'lines.linewidth': 1.8,
})

C_FPR = '#D55E00'
C_FNR = '#0072B2'
C_SWEET = '#009E73'
STAGE_FILLS = ['#E8F4FD', '#A8D8EA', '#56B4E9', '#0072B2']
STAGE_EDGES = ['#A8D8EA', '#56B4E9', '#0072B2', '#004C6D']

# ── Load data ──────────────────────────────────────────
DATA_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                        'artifacts', 'D040', 'data')
with open(os.path.join(DATA_DIR, 'filtering_pipeline_data.json')) as f:
    pipe = json.load(f)
with open(os.path.join(DATA_DIR, 'fpr_fnr_calibration.json')) as f:
    cal = json.load(f)

# Panel (a): funnel A stages + conceptual stage 4
funnel = pipe['pipeline_funnels']['funnel_A_null_control']['stages'][:]
funnel.append({'stage': 4, 'name': 'Multi-seed Consensus',
               'sig': 0, 'eliminated': 0, 'fpr': 0.0})
STAGE_NAMES = [
    'Stage 1: Naive Scan',
    'Stage 2: Differencing',
    'Stage 3: Perm Granger + FDR',
    'Stage 4: Multi-seed Consensus',
]
PITFALLS = [
    'Spurious regression',
    'Shared trends',
    'Non-causal coincidence',
    'Seed-specific artifacts',
]

# Panel (b): FPR / FNR
fpr_k = [d['method_threshold'] for d in cal['fpr_table']['data']]
fpr_v = [d['fpr'] for d in cal['fpr_table']['data']]
fnr_v = []
for k in range(1, 6):
    for r in cal['fnr_table']['rows']:
        if r['method_threshold'] == k and r['seed_threshold'] == 3:
            fnr_v.append(r['fnr_robust_6'])
            break

# Panel (c): practical guidance
guidance = cal['practical_guidance']

# ── Figure ─────────────────────────────────────────────
fig = plt.figure(figsize=(17, 5.8))
gs = gridspec.GridSpec(1, 3, width_ratios=[0.40, 0.34, 0.26], wspace=0.25)

# ================================================================
# Panel (a): Sequential Filtering Pipeline
# ================================================================
ax_a = fig.add_subplot(gs[0])
ax_a.axis('off')
ax_a.set_xlim(0, 13)
ax_a.set_ylim(-0.5, 5.5)

ax_a.text(0.0, 5.15, '(a)', fontsize=13, fontweight='bold')
ax_a.text(0.6, 5.15, 'Sequential Filtering Pipeline (α = 0 null control)',
          fontsize=11, fontweight='bold')

N_PAIRS = 8
cx = 8.5
max_w = 6.0
bar_h = 0.7
y_gap = 1.25

for i, st in enumerate(funnel):
    y = 3.9 - i * y_gap
    sig = st['sig']
    fpr = st['fpr']

    w = max(sig / N_PAIRS * max_w, 1.0)
    x0 = cx - w / 2

    rect = mpatches.FancyBboxPatch(
        (x0, y - bar_h / 2), w, bar_h,
        boxstyle='round,pad=0.06',
        facecolor=STAGE_FILLS[i], edgecolor=STAGE_EDGES[i],
        linewidth=1.5, zorder=2)
    ax_a.add_patch(rect)

    fpr_pct = f'{fpr:.0%}'
    if sig > 0:
        tc = 'white' if i >= 2 else '#222222'
        ax_a.text(cx, y, f'{sig}/{N_PAIRS} sig   FPR = {fpr_pct}',
                  ha='center', va='center', fontsize=9, fontweight='bold',
                  color=tc, zorder=3)
    else:
        ax_a.text(cx + w / 2 + 0.25, y,
                  f'0/{N_PAIRS} sig — FPR = {fpr_pct}',
                  ha='left', va='center', fontsize=8.5, fontweight='bold',
                  color=STAGE_EDGES[i], zorder=3)

    ax_a.text(0.15, y + 0.14, STAGE_NAMES[i],
              ha='left', va='center', fontsize=8.5, fontweight='bold',
              color='#333333')
    ax_a.text(0.15, y - 0.18, f'  ↳ {PITFALLS[i]}',
              ha='left', va='center', fontsize=7.5, fontstyle='italic',
              color='#888888')

    if i < len(funnel) - 1:
        nxt_elim = funnel[i + 1]['eliminated']
        ay0 = y - bar_h / 2 - 0.02
        ay1 = y - y_gap + bar_h / 2 + 0.02
        ax_a.annotate('', xy=(cx, ay1), xytext=(cx, ay0),
                      arrowprops=dict(arrowstyle='->', color='#999999', lw=1.2))
        if nxt_elim > 0:
            mid = (ay0 + ay1) / 2
            ax_a.text(cx + max_w / 2 + 0.6, mid,
                      f'−{nxt_elim} pairs',
                      ha='left', va='center', fontsize=7.5,
                      fontweight='bold', color=C_FPR,
                      bbox=dict(boxstyle='round,pad=0.12',
                                facecolor='#FFF0E8', edgecolor=C_FPR,
                                alpha=0.85, linewidth=0.7))

# ================================================================
# Panel (b): FPR / FNR Trade-off
# ================================================================
ax_b = fig.add_subplot(gs[1])
ax_b.set_title('(b) FPR / FNR Trade-off (seed threshold S ≥ 3)',
               fontweight='bold', loc='left', fontsize=11, pad=8)

ax_b.plot(fpr_k, fpr_v, 'o-', color=C_FPR, markersize=8,
          label='FPR (α = 0)', zorder=3,
          markeredgecolor='white', markeredgewidth=0.8)
ax_b.plot(fpr_k, fnr_v, 's-', color=C_FNR, markersize=8,
          label='FNR$_{robust}$ (α = 1, S ≥ 3)', zorder=3,
          markeredgecolor='white', markeredgewidth=0.8)

ax_b.axvline(4, color=C_SWEET, ls='--', lw=1.5, alpha=0.6, zorder=1)
ax_b.axvspan(3.75, 4.25, alpha=0.08, color=C_SWEET, zorder=0)
ax_b.annotate('Sweet spot\nFPR = 0, FNR = 0',
              xy=(4, 0.02), xytext=(4.4, 0.42),
              fontsize=9, fontweight='bold', color=C_SWEET,
              arrowprops=dict(arrowstyle='->', color=C_SWEET, lw=1.2),
              bbox=dict(boxstyle='round,pad=0.25', facecolor='#E8F8F0',
                        edgecolor=C_SWEET, alpha=0.9, linewidth=0.8))

ax_b.annotate('FPR cliff\n37.5% → 0%',
              xy=(3.5, 0.19), xytext=(1.7, 0.58),
              fontsize=8, color=C_FPR,
              arrowprops=dict(arrowstyle='->', color=C_FPR, lw=1.0),
              bbox=dict(boxstyle='round,pad=0.2', facecolor='#FFF0E0',
                        edgecolor=C_FPR, alpha=0.85, linewidth=0.7))

ax_b.annotate('FNR jump\n0% → 50%',
              xy=(4.5, 0.25), xytext=(4.55, 0.75),
              fontsize=8, color=C_FNR,
              arrowprops=dict(arrowstyle='->', color=C_FNR, lw=1.0),
              bbox=dict(boxstyle='round,pad=0.2', facecolor='#E0F0FF',
                        edgecolor=C_FNR, alpha=0.85, linewidth=0.7))

ax_b.set_xlabel('Method Threshold K (out of 5)')
ax_b.set_ylabel('Rate')
ax_b.set_xticks([1, 2, 3, 4, 5])
ax_b.set_ylim(-0.05, 1.1)
ax_b.set_xlim(0.5, 5.5)
ax_b.legend(loc='upper right', framealpha=0.9, edgecolor='#CCCCCC')
ax_b.grid(axis='y', alpha=0.25, lw=0.5)

# ================================================================
# Panel (c): Practical Guidance (card layout)
# ================================================================
ax_c = fig.add_subplot(gs[2])
ax_c.axis('off')
ax_c.set_xlim(0, 1)
ax_c.set_ylim(0, 1)
ax_c.set_title('(c) Recommended Configurations',
               fontweight='bold', loc='left', fontsize=11, pad=8)

USE_NAMES = ['Exploratory', 'Standard', 'Publication-grade', 'Conservative']
card_bg = ['#FAFAFA', '#FAFAFA', '#E8F8F0', '#FAFAFA']
card_ec = ['#CCCCCC', '#CCCCCC', C_SWEET, '#CCCCCC']
card_lw = [0.7, 0.7, 1.8, 0.7]

n = len(guidance)
ch = 0.195
gap = 0.04
total = n * ch + (n - 1) * gap
y0 = 0.52 + total / 2

for i, g in enumerate(guidance):
    yt = y0 - i * (ch + gap)

    rect = mpatches.FancyBboxPatch(
        (0.02, yt - ch), 0.96, ch,
        boxstyle='round,pad=0.02',
        facecolor=card_bg[i], edgecolor=card_ec[i], linewidth=card_lw[i])
    ax_c.add_patch(rect)

    icon = '★' if i == 2 else '●'
    fw = 'bold' if i == 2 else 'normal'
    tc = '#222222' if i == 2 else '#444444'

    ax_c.text(0.07, yt - 0.025, f'{icon} {USE_NAMES[i]}',
              fontsize=8.5, fontweight=fw, color=tc, va='top')
    ax_c.text(0.07, yt - 0.072, g['config'],
              fontsize=7, color='#777777', va='top')

    fpr_s = f"{g['fpr']:.0%}" if g['fpr'] > 0 else '0%'
    fnr_val = g['fnr_robust_6']
    fnr_s = f"{fnr_val:.1%}" if fnr_val > 0 else '0%'
    ax_c.text(0.07, yt - 0.12, f'FPR {fpr_s}    FNR {fnr_s}',
              fontsize=7.5, color='#555555', va='top', fontweight=fw)

# ── Save ───────────────────────────────────────────────
out_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                       'artifacts', 'figures')
os.makedirs(out_dir, exist_ok=True)
pdf_path = os.path.join(out_dir, 'consensus_workflow.pdf')
png_path = os.path.join(out_dir, 'consensus_workflow.png')
fig.savefig(pdf_path, format='pdf')
fig.savefig(png_path, format='png', dpi=200)
plt.close(fig)
print(f'PDF: {pdf_path}')
print(f'PNG: {png_path}')
print(f'FPR data: {fpr_v}')
print(f'FNR data (S>=3): {fnr_v}')
