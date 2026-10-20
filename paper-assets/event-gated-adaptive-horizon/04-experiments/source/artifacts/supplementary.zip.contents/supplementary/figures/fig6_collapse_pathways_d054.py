#!/usr/bin/env python3
"""Fig 6: Three Collapse Pathways — D054/C6 revision.

Conceptual pathway diagram: CIVO, IRD, and Gradient Starvation
as distinct failure modes in adaptive temporal abstraction.
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
import os

plt.rcParams.update({
    'font.family': 'serif',
    'font.serif': ['Times New Roman', 'DejaVu Serif', 'serif'],
    'font.size': 7.5,
    'figure.dpi': 300,
    'savefig.dpi': 300,
    'savefig.bbox': 'tight',
    'savefig.pad_inches': 0.04,
})

# === Colors ===
C_CIVO = '#C0392B'
C_IRD  = '#2980B9'
C_GS   = '#E67E22'
C_ROOT = '#2C3E50'
C_SGS  = '#27AE60'
C_WARN = '#C0392B'

fig, ax = plt.subplots(figsize=(7.2, 7.2))
ax.set_xlim(-1.2, 13.2)
ax.set_ylim(-0.3, 11.5)
ax.axis('off')

# Column x-centers
XC, XI, XG = 2.0, 6.0, 10.0
BW  = 3.4
BH  = 0.95
MH  = 1.15   # mechanism box height (taller, 3 lines)
OH  = 1.20   # outcome box height

def rbox(x, y, w, h, text, ec, fc='white', fs=7, fw='normal',
         tc=None, ls='-', lw=1.0):
    p = FancyBboxPatch(
        (x - w/2, y - h/2), w, h,
        boxstyle='round,pad=0.12', facecolor=fc, edgecolor=ec,
        linewidth=lw, linestyle=ls, zorder=2, clip_on=False)
    ax.add_patch(p)
    ax.text(x, y, text, ha='center', va='center', fontsize=fs,
            fontweight=fw, color=tc or ec, zorder=3,
            linespacing=1.3, multialignment='center')

def arr(x1, y1, x2, y2, c='#888', lw=1.0, ls='-'):
    a = FancyArrowPatch(
        (x1, y1), (x2, y2), arrowstyle='-|>', color=c,
        linewidth=lw, linestyle=ls, mutation_scale=10,
        zorder=1, clip_on=False)
    ax.add_patch(a)

# Row y-centers
YR  = 10.8
YP  = 10.0
Y1  = 8.9
Y2  = 7.2
Y3  = 5.4
Y4  = 3.4
YC6 = 1.4
g   = 0.08

# ══════════ ROOT ══════════
rbox(6.0, YR, 9.5, 0.65,
     'Collapse Pathways in Adaptive Temporal Abstraction (DreamerV3)',
     ec=C_ROOT, fc='#F4F6F7', fs=8.5, fw='bold', tc=C_ROOT)

for col, c in [(XC, C_CIVO), (XI, C_IRD), (XG, C_GS)]:
    arr(6.0, YR - 0.35, col, YP + 0.15, c=c, lw=0.7)

# ══════════ PATHWAY LABELS ══════════
ax.text(XC, YP, 'CIVO', ha='center', fontsize=9.5,
        fontweight='bold', color=C_CIVO)
ax.text(XI, YP, 'IRD', ha='center', fontsize=9.5,
        fontweight='bold', color=C_IRD)
ax.text(XG, YP, 'Gradient Starvation', ha='center', fontsize=9.5,
        fontweight='bold', color=C_GS)

# thin colored line under each label
for col, c in [(XC, C_CIVO), (XI, C_IRD), (XG, C_GS)]:
    ax.plot([col - 1.2, col + 1.2], [YP - 0.18, YP - 0.18],
            color=c, lw=1.5, solid_capstyle='round', zorder=1)

# ══════════ ROW 1: CONFIGURATION ══════════
rbox(XC, Y1, BW, BH,
     'Trained $dt$-emb\n$dt > 1$ imagination',
     ec=C_CIVO, fc='#FDEDEC', fs=7.5, fw='bold')
rbox(XI, Y1, BW, BH,
     'Trained $dt$-emb\n$dt = 1$ imagination',
     ec=C_IRD, fc='#EBF5FB', fs=7.5, fw='bold')
rbox(XG, Y1, BW, BH,
     'Frozen $dt$-emb\n(no temporal signal)',
     ec=C_GS, fc='#FEF9E7', fs=7.5, fw='bold')

for col, c in [(XC, C_CIVO), (XI, C_IRD), (XG, C_GS)]:
    arr(col, Y1 - BH/2 - g, col, Y2 + BH/2 + g, c=c)

# ══════════ ROW 2: ROOT CAUSE ══════════
rbox(XC, Y2, BW, BH,
     'Reward prediction bias\nat $dt > 1$ (2.78$\\times$ gap)',
     ec=C_CIVO, fs=7)
rbox(XI, Y2, BW, BH,
     'World model accuracy\nceiling at long horizons',
     ec=C_IRD, fs=7)
rbox(XG, Y2, BW, BH,
     'Representation drift\n(stale frozen features)',
     ec=C_GS, fs=7)

for col, c in [(XC, C_CIVO), (XI, C_IRD), (XG, C_GS)]:
    arr(col, Y2 - BH/2 - g, col, Y3 + MH/2 + g, c=c)

# ══════════ ROW 3: MECHANISM + SIGNATURE ══════════
rbox(XC, Y3, BW, MH,
     'Value inflation (NVE > 1.5$\\times$)\n'
     '$\\rightarrow$ actor exploitation\n'
     'entropy $\\downarrow$ (over-committed)',
     ec=C_CIVO, fs=6.5)
rbox(XI, Y3, BW, MH,
     'value_std explosion\n'
     '$\\rightarrow$ policy de-specialization\n'
     'entropy $\\uparrow$ (destabilizing)',
     ec=C_IRD, fs=6.5)
rbox(XG, Y3, BW, MH,
     'actor_loss $\\rightarrow$ 0\n'
     '$\\rightarrow$ gradient starvation\n'
     'NVE transient spike',
     ec=C_GS, fs=6.5)

for col, c in [(XC, C_CIVO), (XI, C_IRD), (XG, C_GS)]:
    arr(col, Y3 - MH/2 - g, col, Y4 + OH/2 + g, c=c, lw=1.2)

# ══════════ ROW 4: OUTCOME ══════════
rbox(XC, Y4, BW, OH,
     'CIVO Collapse\nexp 008d, 006\nNVE > 1.5$\\times$ sustained',
     ec='white', fc=C_CIVO, fs=7.5, fw='bold', tc='white')
rbox(XI, Y4, BW, OH,
     'IRD Collapse\nexp 008e_v3 s2\nNVE passive rise',
     ec='white', fc=C_IRD, fs=7.5, fw='bold', tc='white')
rbox(XG, Y4, BW, OH,
     'Starvation Collapse\nexp 015b\nNVE transient',
     ec='white', fc=C_GS, fs=7.5, fw='bold', tc='white')

# ══════════ SGS INTERVENTION ══════════
sgs_x = -0.7
sgs_y = Y3 + 0.15
ax.text(sgs_x, sgs_y, 'SGS', fontsize=8, fontweight='bold',
        color=C_SGS, ha='center', va='center',
        bbox=dict(boxstyle='round,pad=0.25', fc='#E8F8F5', ec=C_SGS,
                  lw=1.0, ls=(0, (4, 3))))
ax.text(sgs_x, sgs_y - 0.55, '(proposed)', fontsize=5.5, color=C_SGS,
        ha='center', fontstyle='italic')
arr(sgs_x + 0.5, sgs_y, XC - BW/2 - 0.05, sgs_y,
    c=C_SGS, lw=1.5, ls='--')

# ══════════ C6 CORRECTION ══════════
c6_w, c6_h = 9.0, 1.1
c6_x, c6_y = 5.0, YC6
p = FancyBboxPatch(
    (c6_x - c6_w/2, c6_y - c6_h/2), c6_w, c6_h,
    boxstyle='round,pad=0.15', facecolor='#FAFAFA', edgecolor='#95A5A6',
    linewidth=0.8, linestyle='--', zorder=2, clip_on=False)
ax.add_patch(p)

ax.text(c6_x, c6_y + 0.3, 'C6 Correction:  $dt{=}1$ imagination',
        ha='center', va='center', fontsize=8, fontweight='bold',
        color='#444', zorder=3)
ax.text(c6_x - 2.2, c6_y - 0.22,
        '$\\checkmark$  Prevents CIVO mechanism',
        ha='center', va='center', fontsize=7, color=C_SGS,
        fontweight='bold', zorder=3)
ax.text(c6_x + 2.2, c6_y - 0.22,
        '$\\times$  Does NOT prevent late\npolicy instability (IRD)',
        ha='center', va='center', fontsize=7, color=C_WARN,
        fontweight='bold', zorder=3, linespacing=1.2,
        multialignment='center')

# Subtle connectors from C6 to CIVO and IRD outcomes
arr(c6_x - 2.8, c6_y + c6_h/2 + g, XC + 0.3, Y4 - OH/2 - g,
    c=C_SGS, lw=0.5, ls=':')
arr(c6_x + 1.5, c6_y + c6_h/2 + g, XI - 0.3, Y4 - OH/2 - g,
    c=C_WARN, lw=0.5, ls=':')

# ══════════ SAVE ══════════
out_dir = '/root/autodl-tmp/event-gated-adaptive-horizon/artifacts'
os.makedirs(out_dir, exist_ok=True)
for ext in ('pdf', 'png'):
    fig.savefig(f'{out_dir}/fig6_collapse_pathways_d054.{ext}')

fig_dir = '/root/autodl-tmp/event-gated-adaptive-horizon/artifacts/figures/paper'
os.makedirs(fig_dir, exist_ok=True)
for ext in ('pdf', 'png'):
    fig.savefig(f'{fig_dir}/fig6_collapse_pathways_d054.{ext}')

plt.close()
print('Saved fig6_collapse_pathways_d054.pdf and .png')
