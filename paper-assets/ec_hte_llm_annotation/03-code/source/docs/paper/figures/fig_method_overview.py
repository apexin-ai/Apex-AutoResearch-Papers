#!/usr/bin/env python3
"""Figure 2: EC-HTE Method Overview — v31 colorblind-safe.

Two-track comparison: Standard (muted rose) vs EC-HTE (blue).
Colorblind-safe: red/green replaced with rose/blue throughout.
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
import numpy as np

plt.rcParams.update({
    'font.family': 'serif',
    'font.size': 9,
    'mathtext.fontset': 'stix',
    'pdf.fonttype': 42,
    'ps.fonttype': 42,
    'figure.dpi': 300,
    'savefig.dpi': 300,
    'savefig.bbox': 'tight',
    'savefig.pad_inches': 0.08,
})

OUT = '/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/figures'

# ══════════════════════════════════════════
# CANVAS — much wider, taller for breathing room
# ══════════════════════════════════════════
fig, ax = plt.subplots(figsize=(11.0, 4.5))
ax.set_xlim(-0.5, 20.5)
ax.set_ylim(-0.9, 8.5)
ax.axis('off')
fig.patch.set_facecolor('white')

# ══════════════════════════════════════════
# PALETTE — 3 semantic color families
# ══════════════════════════════════════════
# Standard track (rose — "problem")
S_BG   = '#FDF3F0';  S_BOX  = '#FFFFFF';  S_EDGE = '#D4A5A0'
S_TXT  = '#6B3A35';  S_SUB  = '#A07570';  S_ARR  = '#CCA5A0'

# EC-HTE track (blue — "solution", colorblind-safe)
E_BG   = '#EEF4FA';  E_BOX  = '#FFFFFF';  E_EDGE = '#5B9BD5'
E_TXT  = '#1A4472';  E_SUB  = '#4A7DAD';  E_ARR  = '#5B9BD5'

# Input boxes (soft blue-gray — "data")
I_BOX  = '#FFFFFF';  I_EDGE = '#94B8D4';  I_TXT  = '#2C5D89';  I_SUB = '#6A96B8'

# Outcome badges (blue/red — colorblind-safe)
OK_BG  = '#E3F2FD';  OK_EDGE = '#42A5F5';  OK_TXT  = '#1565C0'
BAD_BG = '#FFEBEE';  BAD_EDGE = '#EF5350'; BAD_TXT = '#C62828'

# Neutral
HEAD = '#37474F';  ANNOT = '#999999';  DIV = '#E0E0E0'

# ══════════════════════════════════════════
# LAYOUT — wider column spacing (5 units apart)
# ══════════════════════════════════════════
COL_X = {'input': 2.5, 'est': 7.5, 'corr': 12.5, 'inf': 17.5}

Y_HEAD = 7.8
Y_STD  = 5.9
Y_EC   = 2.5
BW     = 3.0      # box width (was 2.5)
BW_IN  = 2.6      # input box width
BH_S   = 1.05     # standard box height
BH_E   = 1.20     # EC-HTE box height
BH_I   = 0.85     # input box height
ROUNDING = 0.15
SHADOW_OFFSET = 0.04


# ══════════════════════════════════════════
# HELPERS
# ══════════════════════════════════════════
def draw_box(cx, cy, w, h, label, sub='',
             fc='white', ec='gray', lw=0.8,
             fs=11, ss=10, lc='#333', sc='#777',
             bold=True, shadow=True, zz=3):
    x0, y0 = cx - w / 2, cy - h / 2
    if shadow:
        ax.add_patch(FancyBboxPatch(
            (x0 + SHADOW_OFFSET, y0 - SHADOW_OFFSET), w, h,
            boxstyle=f'round,pad=0.08,rounding_size={ROUNDING}',
            fc='#00000008', ec='none', zorder=zz - 1))
    ax.add_patch(FancyBboxPatch(
        (x0, y0), w, h,
        boxstyle=f'round,pad=0.08,rounding_size={ROUNDING}',
        fc=fc, ec=ec, lw=lw, zorder=zz))
    fw = 'bold' if bold else 'normal'
    if sub:
        ax.text(cx, cy + 0.18, label, ha='center', va='center',
                fontsize=fs, fontweight=fw, color=lc, zorder=zz + 1)
        ax.text(cx, cy - 0.22, sub, ha='center', va='center',
                fontsize=ss, color=sc, fontstyle='italic', zorder=zz + 1)
    else:
        ax.text(cx, cy, label, ha='center', va='center',
                fontsize=fs, fontweight=fw, color=lc, zorder=zz + 1)


def draw_arrow(x1, y1, x2, y2, color='gray', lw=1.0, rad=0,
               ls='-', alpha=1.0, zz=2):
    style = '->,head_length=4,head_width=2.2'
    conn = f'arc3,rad={rad}'
    ax.add_patch(FancyArrowPatch(
        (x1, y1), (x2, y2),
        arrowstyle=style, color=color, lw=lw,
        mutation_scale=9, connectionstyle=conn,
        linestyle=ls, alpha=alpha, zorder=zz))


def draw_badge(cx, cy, kind='check', radius=0.22, zz=6):
    bg = '#E3F2FD' if kind == 'check' else '#FFEBEE'
    ec = '#1976D2' if kind == 'check' else '#E53935'
    circle = plt.Circle((cx, cy), radius, fc=bg, ec=ec,
                         lw=1.0, zorder=zz, clip_on=False)
    ax.add_patch(circle)
    s = radius * 0.55
    if kind == 'check':
        ax.plot([cx - s * 0.7, cx - s * 0.05, cx + s],
                [cy + s * 0.05, cy - s * 0.6, cy + s * 0.55],
                color='#1976D2', lw=2.0, solid_capstyle='round',
                solid_joinstyle='round', zorder=zz + 1, clip_on=False)
    else:
        d = s * 0.6
        ax.plot([cx - d, cx + d], [cy - d, cy + d],
                color='#E53935', lw=2.0, solid_capstyle='round',
                zorder=zz + 1, clip_on=False)
        ax.plot([cx - d, cx + d], [cy + d, cy - d],
                color='#E53935', lw=2.0, solid_capstyle='round',
                zorder=zz + 1, clip_on=False)


# ══════════════════════════════════════════
# SWIM LANE BACKGROUNDS
# ══════════════════════════════════════════
ax.add_patch(FancyBboxPatch(
    (0.3, Y_STD - BH_S / 2 - 0.35), 19.9, BH_S + 0.70,
    boxstyle=f'round,pad=0,rounding_size={ROUNDING}',
    fc=S_BG, ec='none', zorder=0, alpha=0.6))

ax.add_patch(FancyBboxPatch(
    (0.3, Y_EC - BH_E / 2 - 0.70), 19.9, BH_E + 1.40,
    boxstyle=f'round,pad=0,rounding_size={ROUNDING}',
    fc=E_BG, ec='none', zorder=0, alpha=0.6))


# ══════════════════════════════════════════
# COLUMN HEADERS
# ══════════════════════════════════════════
for label, x in [('Input', COL_X['input']),
                  ('Estimation', COL_X['est']),
                  ('Correction', COL_X['corr']),
                  ('Inference', COL_X['inf'])]:
    ax.text(x, Y_HEAD, label, ha='center', va='center',
            fontsize=12, fontweight='bold', color=HEAD)

ax.plot([0.5, 20.2], [Y_HEAD - 0.35, Y_HEAD - 0.35],
        color=DIV, lw=0.6, zorder=0)

for x in [5.0, 10.0, 15.0]:
    ax.plot([x, x], [Y_HEAD - 0.35, Y_EC - BH_E / 2 - 0.55],
            color=DIV, lw=0.3, ls=':', alpha=0.3, zorder=0)


# ══════════════════════════════════════════
# TRACK LABELS (left margin)
# ══════════════════════════════════════════
ax.text(0.55, Y_STD + 0.02, 'Standard',
        ha='left', va='center', fontsize=9, fontweight='bold',
        color=S_TXT, alpha=0.75)

ax.text(0.55, Y_EC + BH_E / 2 + 0.55, 'EC-HTE (Ours)',
        ha='left', va='bottom', fontsize=9, fontweight='bold',
        color=E_TXT)


# ══════════════════════════════════════════
# STANDARD TRACK — 3 boxes
# ══════════════════════════════════════════
draw_box(COL_X['est'], Y_STD, BW, BH_S,
         r'Pooled CM  $\hat{C}$', 'One matrix for all',
         fc=S_BOX, ec=S_EDGE, lc=S_TXT, sc=S_SUB)

draw_box(COL_X['corr'], Y_STD, BW, BH_S,
         'Global Correction', r'$\hat{C}^{-1}$ applied uniformly',
         fc=S_BOX, ec=S_EDGE, lc=S_TXT, sc=S_SUB)

draw_box(COL_X['inf'], Y_STD, BW, BH_S,
         'Sign Reversal', '14.9% of configs',
         fc=BAD_BG, ec=BAD_EDGE, lc=BAD_TXT, sc='#D07070', lw=1.0)

draw_badge(COL_X['inf'] + BW / 2 - 0.05, Y_STD + BH_S / 2 + 0.05,
           kind='cross')

# Standard track arrows
draw_arrow(COL_X['est'] + BW / 2 + 0.08, Y_STD,
           COL_X['corr'] - BW / 2 - 0.08, Y_STD,
           color=S_ARR, lw=1.0)
draw_arrow(COL_X['corr'] + BW / 2 + 0.08, Y_STD,
           COL_X['inf'] - BW / 2 - 0.08, Y_STD,
           color=S_ARR, lw=1.0)


# ══════════════════════════════════════════
# EC-HTE TRACK — input boxes + 3 core boxes
# ══════════════════════════════════════════
y_in_top = Y_EC + 0.62
y_in_bot = Y_EC - 0.62

draw_box(COL_X['input'], y_in_top, BW_IN, BH_I,
         'LLM Annotations', r'$N$ noisy labels $\hat{Z}$',
         fc=I_BOX, ec=I_EDGE, lc=I_TXT, sc=I_SUB,
         fs=10, ss=9, bold=True)

draw_box(COL_X['input'], y_in_bot, BW_IN, BH_I,
         'Expert Labels', r'$n_{\mathrm{expert}}$ pairs $(Z, \hat{Z})$',
         fc=I_BOX, ec=I_EDGE, lc=I_TXT, sc=I_SUB,
         fs=10, ss=9, bold=True)

draw_box(COL_X['est'], Y_EC, BW, BH_E,
         'Hierarchical Bayes', r'Per-subgroup CMs $\{\hat{C}_s\}$',
         fc=E_BOX, ec=E_EDGE, lc=E_TXT, sc=E_SUB,
         lw=1.2, fs=11, ss=10)

draw_box(COL_X['corr'], Y_EC, BW, BH_E,
         'Per-subgroup Corr.', r'$\tilde{\mu}_s = \hat{C}_s^{-1} \cdot \hat{\mu}_s$',
         fc=E_BOX, ec=E_EDGE, lc=E_TXT, sc=E_SUB,
         lw=1.2, fs=11, ss=10)

draw_box(COL_X['inf'], Y_EC, BW, BH_E,
         'Corrected CATE', r'$\hat{\tau}(x) \pm \mathrm{SE}_{\mathrm{corr}}$',
         fc=OK_BG, ec=OK_EDGE, lc=OK_TXT, sc='#5DA05D',
         lw=1.2, fs=11, ss=10)

draw_badge(COL_X['inf'] + BW / 2 - 0.05, Y_EC + BH_E / 2 + 0.05,
           kind='check')


# ══════════════════════════════════════════
# EC-HTE ARROWS
# ══════════════════════════════════════════
draw_arrow(COL_X['input'] + BW_IN / 2 + 0.08, y_in_top,
           COL_X['est'] - BW / 2 - 0.08, Y_EC + 0.18,
           color=E_ARR, lw=1.0, rad=0.05)

draw_arrow(COL_X['input'] + BW_IN / 2 + 0.08, y_in_bot,
           COL_X['est'] - BW / 2 - 0.08, Y_EC - 0.18,
           color=E_ARR, lw=1.0, rad=-0.05)

draw_arrow(COL_X['est'] + BW / 2 + 0.08, Y_EC,
           COL_X['corr'] - BW / 2 - 0.08, Y_EC,
           color=E_ARR, lw=1.3)

draw_arrow(COL_X['corr'] + BW / 2 + 0.08, Y_EC,
           COL_X['inf'] - BW / 2 - 0.08, Y_EC,
           color=E_ARR, lw=1.3)


# ══════════════════════════════════════════
# CROSS-TRACK "prior" ARROW (subtle dashed)
# ══════════════════════════════════════════
y_mid = (Y_STD - BH_S / 2 + Y_EC + BH_E / 2) / 2
draw_arrow(COL_X['est'], Y_STD - BH_S / 2 - 0.08,
           COL_X['est'], Y_EC + BH_E / 2 + 0.08,
           color=E_ARR, lw=0.7, ls='--', alpha=0.35, zz=1)

ax.text(COL_X['est'] + 0.30, y_mid,
        'prior', fontsize=10, color=E_ARR, fontstyle='italic',
        alpha=0.55, ha='left', va='center', zorder=1)


# ══════════════════════════════════════════
# "vs." DIVIDER
# ══════════════════════════════════════════
ax.text(10.0, y_mid, 'vs.', ha='center', va='center',
        fontsize=13, fontweight='bold', color='#D0D0D0', zorder=1)


# ══════════════════════════════════════════
# ANNOTATIONS (below EC-HTE boxes, more space)
# ══════════════════════════════════════════
annot_y = Y_EC - BH_E / 2 - 0.28

ax.text(COL_X['est'], annot_y,
        r'Partial pooling · $\alpha_0$ via Emp. Bayes',
        ha='center', va='top', fontsize=9.5, color=ANNOT,
        fontstyle='italic')

ax.text(COL_X['corr'], annot_y,
        r'$\kappa$-guard: $\kappa > 100$ → fallback',
        ha='center', va='top', fontsize=9.5, color=ANNOT,
        fontstyle='italic')

ax.text(COL_X['inf'], annot_y,
        'via CausalForestDML',
        ha='center', va='top', fontsize=9.5, color=E_TXT,
        fontstyle='italic')


# ══════════════════════════════════════════
# RESULT HIGHLIGHT (bottom center)
# ══════════════════════════════════════════
ax.text(10.0, 0.25,
        r'$\mathbf{0\%}$ sign reversal  ·  $|\mathrm{bias}| \div 7.4$',
        ha='center', va='center', fontsize=9.5, color=OK_TXT,
        fontweight='bold')

ax.text(10.0, -0.35,
        r'Diagnostic (Prop. 5):  $|\delta_s| \,/\, ((1{-}2\bar{\pi}) \cdot \pi_s) > 1$',
        ha='center', va='center', fontsize=8, color='#E65100',
        fontweight='bold',
        bbox=dict(boxstyle=f'round,pad=0.25,rounding_size={ROUNDING}',
                  fc='#FFF8E1', ec='#FFB74D', lw=0.6, alpha=0.9))


# ══════════════════════════════════════════
# SAVE
# ══════════════════════════════════════════
fig.savefig(f'{OUT}/fig_method_overview.png', dpi=300, facecolor='white')
fig.savefig(f'{OUT}/fig_method_overview.pdf', dpi=300, facecolor='white')
plt.close()
print('Saved fig_method_overview v31 (colorblind-safe: green→blue)')
