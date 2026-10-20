#!/usr/bin/env python3
"""Generate combined overview figure: Problem -> Pipeline -> Results.
Four-panel structure for EMNLP paper (figure* = full textwidth ~7in).
figsize 14x12 with generous vertical spacing to avoid overlaps.
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Circle
import matplotlib.patheffects as pe
import numpy as np

plt.rcParams.update({
    'mathtext.fontset': 'cm',
    'font.family': 'DejaVu Serif',
})

FW, FH = 14, 12.5
fig = plt.figure(figsize=(FW, FH), dpi=300, facecolor='white')
ax = fig.add_axes([0, 0, 1, 1])
ax.set_xlim(0, FW)
ax.set_ylim(0, FH)
ax.axis('off')
ax.set_facecolor('white')

# ─── Colors ───
C = dict(
    navy='#2C3E50',
    std_band='#FADBD8', std_border='#E74C3C', std_text='#C0392B',
    std_accent='#C62828',
    ours_band='#D1F2EB', ours_border='#1ABC9C', ours_text='#1ABC9C',
    ours_accent='#00897B',
    input_border='#2980B9', input_text='#0D47A1',
    green_fill='#C8E6C9', green_border='#1A7A6D', green_dot='#2E7D32',
    rose_fill='#FFCDD2', rose_border='#C62828', rose_dot='#C62828',
    pink_fill='#F8D7DA', pink_border='#C62828',
    warn_bg='#C62828',
    anno='#78909C', label='#546E7A',
    result_bg='#1A2530', result_sub='#BDC3C7',
    teal='#1A7A6D',
    sep='#D5D8DC', arrow='#95A5A6',
    formula_bg='#FAFAFA', formula_border='#D0D0D0',
    light_gray='#F5F5F5',
)

# ─── Row boundaries (generous vertical spacing) ───
ROW1_TOP = FH          # 12.5
ROW1_BOT = 8.6
ROW2_TOP = 8.3
ROW2_BOT = 3.0
ROW3_TOP = 2.7
ROW3_BOT = 0

# Separators
ax.plot([0.3, FW-0.3], [ROW1_BOT, ROW1_BOT], color=C['sep'], lw=0.8, zorder=1)
ax.plot([0.3, FW-0.3], [ROW2_BOT, ROW2_BOT], color=C['sep'], lw=0.8, zorder=1)

# ─── Helpers ───
def rbox(x, y, w, h, fill, border, lw=1.3, shadow=True, rad=0.08):
    """Draw a rounded box centered at (x, y)."""
    if shadow:
        ax.add_patch(FancyBboxPatch((x-w/2+0.03, y-h/2-0.03), w, h,
            boxstyle=f"round,pad={rad}", fc='#00000008', ec='none', zorder=1))
    ax.add_patch(FancyBboxPatch((x-w/2, y-h/2), w, h,
        boxstyle=f"round,pad={rad}", fc=fill, ec=border, lw=lw, zorder=2))

def arr(x1, y1, x2, y2, color=None, lw=1.2, ls='-', ms=12):
    """Draw an arrow from (x1,y1) to (x2,y2)."""
    ax.add_patch(FancyArrowPatch((x1,y1),(x2,y2),
        arrowstyle=f'->,head_width=3,head_length=3',
        color=color or C['arrow'], lw=lw, ls=ls, zorder=3, mutation_scale=ms))

def manhattan_arr(x1, y1, x2, y2, color=None, lw=1.2, ls='-', bend='down'):
    """Manhattan-style orthogonal arrow: down then across then down."""
    c = color or C['arrow']
    mid_y = (y1 + y2) / 2
    # Vertical segment down
    ax.plot([x1, x1], [y1, mid_y], color=c, lw=lw, ls=ls, zorder=3)
    # Horizontal segment
    ax.plot([x1, x2], [mid_y, mid_y], color=c, lw=lw, ls=ls, zorder=3)
    # Vertical segment down with arrowhead
    ax.add_patch(FancyArrowPatch((x2, mid_y), (x2, y2),
        arrowstyle='->,head_width=3,head_length=3',
        color=c, lw=lw, ls=ls, zorder=3, mutation_scale=12))

def icon_cross(x, y, bg):
    ax.add_patch(Circle((x,y), 0.13, fc=bg, ec='white', lw=1.5, zorder=6))
    d = 0.05
    ax.plot([x-d,x+d],[y-d,y+d], c='white', lw=2, solid_capstyle='round', zorder=7)
    ax.plot([x-d,x+d],[y+d,y-d], c='white', lw=2, solid_capstyle='round', zorder=7)

def icon_check(x, y, bg):
    ax.add_patch(Circle((x,y), 0.13, fc=bg, ec='white', lw=1.5, zorder=6))
    ax.plot([x-0.045,x-0.005,x+0.06],[y-0.005,y-0.05,y+0.05],
            c='white', lw=2, solid_capstyle='round', solid_joinstyle='round', zorder=7)


# ═══════════════════════════════════════════
# ROW 1: Panel (a) + Panel (b)
# ═══════════════════════════════════════════
panel_sep_x = FW * 0.44
ax.plot([panel_sep_x, panel_sep_x], [ROW1_TOP-0.3, ROW1_BOT+0.2],
        color=C['sep'], lw=0.6, zorder=1)

# --- Panel (a): Problem: Heterogeneous LLM Error ---
pa_cx = panel_sep_x / 2
pa_top = ROW1_TOP - 0.3

ax.text(0.35, pa_top, '(a)',
        ha='left', va='center', fontsize=13, fontweight='bold', color=C['navy'], zorder=5)
ax.text(0.75, pa_top, 'Problem: Heterogeneous LLM Error',
        ha='left', va='center', fontsize=12, fontweight='bold', color=C['navy'], zorder=5)

# LLM Classifier box
llm_y = pa_top - 0.75
llm_w, llm_h = 2.1, 0.50
rbox(pa_cx, llm_y, llm_w, llm_h, 'white', C['arrow'], lw=1.5)
ax.text(pa_cx, llm_y, 'LLM Classifier', ha='center', va='center',
        fontsize=12, fontweight='bold', color=C['navy'], zorder=5)

# Subgroups
sg_y = llm_y - 1.3
sg_a_x = pa_cx - 1.2
sg_b_x = pa_cx + 1.2
sg_w, sg_h = 1.65, 0.60

# Manhattan arrows from LLM to subgroups
manhattan_arr(pa_cx - 0.4, llm_y - llm_h/2 - 0.03, sg_a_x, sg_y + sg_h/2 + 0.05,
              color=C['arrow'])
manhattan_arr(pa_cx + 0.4, llm_y - llm_h/2 - 0.03, sg_b_x, sg_y + sg_h/2 + 0.05,
              color=C['arrow'])

# Subgroup A
rbox(sg_a_x, sg_y, sg_w, sg_h, C['green_fill'], C['green_border'], lw=1.5)
ax.add_patch(Circle((sg_a_x - sg_w/2 + 0.18, sg_y + 0.10), 0.06,
             fc=C['green_dot'], ec='none', zorder=6))
ax.text(sg_a_x + 0.05, sg_y + 0.12, 'Subgroup A', ha='center', va='center',
        fontsize=10, fontweight='bold', color=C['navy'], zorder=5)
ax.text(sg_a_x, sg_y - 0.12, r'$\pi = 0.05$', ha='center', va='center',
        fontsize=13, fontweight='bold', color=C['navy'], zorder=5)

# Subgroup B
rbox(sg_b_x, sg_y, sg_w, sg_h, C['rose_fill'], C['rose_border'], lw=1.5)
ax.add_patch(Circle((sg_b_x - sg_w/2 + 0.18, sg_y + 0.10), 0.06,
             fc=C['rose_dot'], ec='none', zorder=6))
ax.text(sg_b_x + 0.05, sg_y + 0.12, 'Subgroup B', ha='center', va='center',
        fontsize=10, fontweight='bold', color=C['navy'], zorder=5)
ax.text(sg_b_x, sg_y - 0.12, r'$\pi = 0.25$', ha='center', va='center',
        fontsize=13, fontweight='bold', color=C['navy'], zorder=5)

# "5x" label between subgroups
ax.text(pa_cx, sg_y, r'$5\!\times$', ha='center', va='center',
        fontsize=20, fontweight='bold', color=C['std_accent'], zorder=5)

ax.text(pa_cx, sg_y - sg_h/2 - 0.25,
        'Error rates vary up to 5× across subgroups',
        ha='center', va='center', fontsize=9.5, fontstyle='italic',
        color='#9E9E9E', zorder=5)


# --- Panel (b): Why Global Correction Fails ---
pb_cx = (panel_sep_x + FW) / 2
ax.text(panel_sep_x + 0.35, pa_top, '(b)',
        ha='left', va='center', fontsize=13, fontweight='bold', color=C['navy'], zorder=5)
ax.text(panel_sep_x + 0.75, pa_top, 'Why Global Correction Fails',
        ha='left', va='center', fontsize=12, fontweight='bold', color=C['navy'], zorder=5)

# Pooled CM box
pcm_y = pa_top - 0.72
pcm_w, pcm_h = 2.5, 0.55
rbox(pb_cx, pcm_y, pcm_w, pcm_h, C['pink_fill'], C['pink_border'], lw=1.5)
ax.text(pb_cx, pcm_y + 0.08, r'Pooled CM $\hat{C}$', ha='center', va='center',
        fontsize=12, fontweight='bold', color=C['navy'], zorder=5)
ax.text(pb_cx, pcm_y - 0.12, 'One matrix for all', ha='center', va='center',
        fontsize=9.5, fontstyle='italic', color='#7F8C8D', zorder=5)

# Over/under corrected boxes
oc_y = pcm_y - 0.85
oc_a_x = pb_cx - 1.5
oc_b_x = pb_cx + 1.5
oc_w, oc_h = 1.9, 0.42

manhattan_arr(pb_cx - 0.4, pcm_y - pcm_h/2 - 0.03, oc_a_x, oc_y + oc_h/2 + 0.05,
              color=C['arrow'])
manhattan_arr(pb_cx + 0.4, pcm_y - pcm_h/2 - 0.03, oc_b_x, oc_y + oc_h/2 + 0.05,
              color=C['arrow'])

rbox(oc_a_x, oc_y, oc_w, oc_h, C['light_gray'], C['sep'])
ax.text(oc_a_x, oc_y + 0.07, 'Subgroup A', ha='center', va='center',
        fontsize=9.5, color=C['navy'], zorder=5)
ax.text(oc_a_x, oc_y - 0.10, r'Over-corrected $\nearrow$', ha='center', va='center',
        fontsize=10, fontweight='bold', color=C['std_accent'], zorder=5)

rbox(oc_b_x, oc_y, oc_w, oc_h, C['light_gray'], C['sep'])
ax.text(oc_b_x, oc_y + 0.07, 'Subgroup B', ha='center', va='center',
        fontsize=9.5, color=C['navy'], zorder=5)
ax.text(oc_b_x, oc_y - 0.10, r'Under-corrected $\searrow$', ha='center', va='center',
        fontsize=10, fontweight='bold', color=C['std_accent'], zorder=5)

# Formula box
fm_y = oc_y - 0.65
fm_w, fm_h = 4.0, 0.45
rbox(pb_cx, fm_y, fm_w, fm_h, C['formula_bg'], C['formula_border'], lw=0.8)
ax.text(pb_cx, fm_y,
        r'$\mathrm{bias}(z,s) = \delta_s \times \frac{\Delta\tau}{1 - 2\bar{\pi}}$',
        ha='center', va='center', fontsize=13, color=C['navy'], zorder=5)

# Warning badge
warn_y = fm_y - 0.55
warn_w, warn_h = 3.5, 0.38
ax.add_patch(FancyBboxPatch((pb_cx - warn_w/2, warn_y - warn_h/2), warn_w, warn_h,
    boxstyle="round,pad=0.06", fc=C['warn_bg'], ec='none', zorder=2))
ax.text(pb_cx, warn_y, 'Sign Reversal: 14.9% of configs',
        ha='center', va='center', fontsize=10.5, fontweight='bold', color='white', zorder=5)


# ═══════════════════════════════════════════
# ROW 2: Panel (c) Standard vs. EC-HTE Pipeline
# ═══════════════════════════════════════════
ax.text(0.35, ROW2_TOP - 0.15, '(c)',
        ha='left', va='center', fontsize=13, fontweight='bold', color=C['navy'], zorder=5)
ax.text(0.75, ROW2_TOP - 0.15, 'Standard vs. EC-HTE Pipeline',
        ha='left', va='center', fontsize=12, fontweight='bold', color=C['navy'], zorder=5)

col = dict(input=2.3, est=5.2, corr=8.3, inf=11.4)
BW, BH = 2.2, 0.60
IW, IH = 1.7, 0.42

# Column headers
hdr_y = ROW2_TOP - 0.55
for lbl, x in [('Input', col['input']), ('Estimation', col['est']),
                ('Correction', col['corr']), ('Inference', col['inf'])]:
    ax.text(x, hdr_y, lbl, ha='center', va='center', fontsize=11.5,
            fontweight='bold', color=C['navy'], zorder=5)
ax.plot([1.2, FW-0.3], [hdr_y - 0.18, hdr_y - 0.18], color=C['sep'], lw=0.5, zorder=1)

# ─── Standard track ───
std_y = hdr_y - 1.0
std_band_h = BH + 0.5
ax.add_patch(FancyBboxPatch((1.0, std_y - std_band_h/2), FW - 1.3, std_band_h,
    boxstyle="round,pad=0.10", fc=C['std_band'], ec='none', zorder=0, alpha=0.35))
ax.text(1.25, std_y, 'Standard', ha='center', va='center', fontsize=10,
        fontweight='bold', color=C['std_text'], rotation=90, zorder=5)

# Standard: Pooled CM
rbox(col['est'], std_y, BW, BH, 'white', C['std_border'], lw=1.5)
ax.text(col['est'], std_y + 0.10, r'Pooled CM $\hat{C}$', ha='center', va='center',
        fontsize=11, fontweight='bold', color=C['navy'], zorder=5)
ax.text(col['est'], std_y - 0.11, 'One matrix for all', ha='center', va='center',
        fontsize=9, fontstyle='italic', color='#7F8C8D', zorder=5)

# Standard: Global Correction
rbox(col['corr'], std_y, BW, BH, 'white', C['std_border'], lw=1.5)
ax.text(col['corr'], std_y + 0.10, 'Global Correction', ha='center', va='center',
        fontsize=11, fontweight='bold', color=C['navy'], zorder=5)
ax.text(col['corr'], std_y - 0.11, r'$\hat{C}^{-1}$ applied uniformly', ha='center',
        va='center', fontsize=9, fontstyle='italic', color='#7F8C8D', zorder=5)

# Standard: Sign Reversal
rbox(col['inf'], std_y, BW, BH, C['rose_fill'], C['std_border'], lw=1.5)
ax.text(col['inf'], std_y + 0.10, 'Sign Reversal', ha='center', va='center',
        fontsize=11, fontweight='bold', color=C['std_accent'], zorder=5)
ax.text(col['inf'], std_y - 0.11, '14.9% of configs', ha='center', va='center',
        fontsize=9, fontstyle='italic', color=C['std_accent'], zorder=5)
icon_cross(col['inf'] + BW/2 - 0.06, std_y + BH/2 - 0.06, C['std_accent'])

# Standard arrows
arr(col['est'] + BW/2 + 0.08, std_y, col['corr'] - BW/2 - 0.10, std_y,
    color=C['std_text'], lw=1.3)
arr(col['corr'] + BW/2 + 0.08, std_y, col['inf'] - BW/2 - 0.10, std_y,
    color=C['std_text'], lw=1.3)

# ─── "vs." label between rows ───
vs_y = std_y - 1.3
ax.text(col['inf'], vs_y, 'vs.', ha='center', va='center', fontsize=12,
        fontweight='bold', color='#7F8C8D', zorder=5)

# ─── "prior" dashed arrow ───
prior_top = std_y - BH/2 - 0.06
prior_bot = vs_y - 1.3 + BH/2 + 0.06
arr(col['est'], prior_top, col['est'], prior_bot,
    color=C['label'], lw=1.0, ls='--')
t = ax.text(col['est'] + 0.15, vs_y, 'prior', ha='left', va='center',
            fontsize=10, color=C['anno'], fontstyle='italic', zorder=5)
t.set_path_effects([pe.withStroke(linewidth=3, foreground='white')])

# ─── EC-HTE track ───
ours_y = vs_y - 1.3
ours_band_h = BH + 1.1
ax.add_patch(FancyBboxPatch((1.0, ours_y - ours_band_h/2), FW - 1.3, ours_band_h,
    boxstyle="round,pad=0.10", fc=C['ours_band'], ec='none', zorder=0, alpha=0.30))
ax.text(1.25, ours_y, 'EC-HTE\n(Ours)', ha='center', va='center', fontsize=9,
        fontweight='bold', color=C['ours_text'], rotation=90, linespacing=1.3, zorder=5)

# Input boxes (stacked)
iy_top = ours_y + 0.35
iy_bot = ours_y - 0.35

rbox(col['input'], iy_top, IW, IH, 'white', C['input_border'], lw=1.2)
ax.text(col['input'], iy_top + 0.05, 'LLM Annotations', ha='center', va='center',
        fontsize=9.5, fontweight='bold', color=C['navy'], zorder=5)
ax.text(col['input'], iy_top - 0.10, r'$N$ noisy labels $\hat{Z}$', ha='center',
        va='center', fontsize=8, color=C['input_text'], alpha=0.65,
        fontstyle='italic', zorder=5)

rbox(col['input'], iy_bot, IW, IH, 'white', C['input_border'], lw=1.2)
ax.text(col['input'], iy_bot + 0.05, 'Expert Labels', ha='center', va='center',
        fontsize=9.5, fontweight='bold', color=C['navy'], zorder=5)
ax.text(col['input'], iy_bot - 0.10, r'$n_{\mathrm{exp}}$ pairs $(Z,\hat{Z})$',
        ha='center', va='center', fontsize=8, color=C['input_text'], alpha=0.65,
        fontstyle='italic', zorder=5)

# EC-HTE: Hierarchical Bayes
rbox(col['est'], ours_y, BW, BH, 'white', C['ours_border'], lw=1.5)
ax.text(col['est'], ours_y + 0.10, 'Hierarchical Bayes', ha='center', va='center',
        fontsize=11, fontweight='bold', color=C['navy'], zorder=5)
ax.text(col['est'], ours_y - 0.11, r'Per-subgroup CMs $\{\hat{C}_s\}$', ha='center',
        va='center', fontsize=9, color=C['navy'], zorder=5)

# EC-HTE: Per-subgroup Correction
rbox(col['corr'], ours_y, BW, BH, 'white', C['ours_border'], lw=1.5)
ax.text(col['corr'], ours_y + 0.10, 'Per-subgroup Corr.', ha='center', va='center',
        fontsize=11, fontweight='bold', color=C['navy'], zorder=5)
ax.text(col['corr'], ours_y - 0.11,
        r'$\tilde{\mu}_s = \hat{C}_s^{-1}\!\cdot\!\hat{\mu}_s$, $\kappa$-guard',
        ha='center', va='center', fontsize=9.5, color=C['navy'], zorder=5)

# EC-HTE: Corrected CATE
rbox(col['inf'], ours_y, BW, BH, C['ours_band'], C['ours_border'], lw=1.5)
ax.text(col['inf'], ours_y + 0.10, 'Corrected CATE', ha='center', va='center',
        fontsize=11, fontweight='bold', color=C['ours_text'], zorder=5)
ax.text(col['inf'], ours_y - 0.11,
        r'$\hat{\tau}(x) \pm \mathrm{SE}_{\mathrm{corr}}$',
        ha='center', va='center', fontsize=9.5, color=C['navy'], zorder=5)
icon_check(col['inf'] + BW/2 - 0.06, ours_y + BH/2 - 0.06, C['ours_accent'])

# EC-HTE arrows: inputs to estimation
arr(col['input'] + IW/2 + 0.08, iy_top, col['est'] - BW/2 - 0.10, ours_y + 0.08,
    color=C['ours_text'], lw=1.0)
arr(col['input'] + IW/2 + 0.08, iy_bot, col['est'] - BW/2 - 0.10, ours_y - 0.08,
    color=C['ours_text'], lw=1.0)

# EC-HTE arrows: estimation to correction to inference
arr(col['est'] + BW/2 + 0.08, ours_y, col['corr'] - BW/2 - 0.10, ours_y,
    color=C['ours_text'], lw=1.3)
arr(col['corr'] + BW/2 + 0.08, ours_y, col['inf'] - BW/2 - 0.10, ours_y,
    color=C['ours_text'], lw=1.3)

# Annotations below EC-HTE boxes
ay = ours_y - BH/2 - 0.18
ax.text(col['est'], ay, r'Partial pooling via Emp. Bayes',
        ha='center', va='top', fontsize=8.5, color=C['anno'], zorder=5)
ax.text(col['corr'], ay, r'$\kappa > 100 \rightarrow$ fallback',
        ha='center', va='top', fontsize=8.5, color=C['anno'], zorder=5)
ax.text(col['inf'], ay, 'via CausalForestDML', ha='center', va='top',
        fontsize=8.5, color=C['anno'], zorder=5)


# ═══════════════════════════════════════════
# ROW 3: Panel (d) Key Results
# ═══════════════════════════════════════════
r3_mid = (ROW3_TOP + ROW3_BOT) / 2

ax.text(0.35, ROW3_TOP - 0.12, '(d)',
        ha='left', va='center', fontsize=13, fontweight='bold', color=C['navy'], zorder=5)
ax.text(0.75, ROW3_TOP - 0.12, 'Key Results',
        ha='left', va='center', fontsize=12, fontweight='bold', color=C['navy'], zorder=5)
ax.text(0.75, ROW3_TOP - 0.42, 'Validated across 8 LLMs, 4 NLP tasks',
        ha='left', va='center', fontsize=9.5, fontstyle='italic', color='#7F8C8D', zorder=5)

card_y = r3_mid - 0.05
card_w, card_h = 2.6, 1.15
card_xs = [1.8, 4.7, 7.6]
card_nums = [r'7.4$\times$', r'14.9%$\rightarrow$0%', r'$\geq\!$ 93%']
card_subs = ['|bias| reduction', 'Sign reversal eliminated', 'CI coverage maintained']
card_sizes = [26, 18, 26]

for cx, num, sub, ns in zip(card_xs, card_nums, card_subs, card_sizes):
    # Shadow
    ax.add_patch(FancyBboxPatch((cx - card_w/2 + 0.03, card_y - card_h/2 - 0.03),
        card_w, card_h, boxstyle="round,pad=0.08",
        fc='#00000010', ec='none', zorder=1))
    # Card
    ax.add_patch(FancyBboxPatch((cx - card_w/2, card_y - card_h/2),
        card_w, card_h, boxstyle="round,pad=0.08",
        fc=C['result_bg'], ec='none', zorder=2))
    ax.text(cx, card_y + 0.18, num, ha='center', va='center',
            fontsize=ns, fontweight='bold', color='white', zorder=5)
    ax.text(cx, card_y - 0.28, sub, ha='center', va='center',
            fontsize=9.5, color=C['result_sub'], zorder=5)

# Teal diagnostic badge (rightmost)
teal_x = 10.8
teal_w, teal_h = 3.2, 1.15
ax.add_patch(FancyBboxPatch((teal_x - teal_w/2 + 0.03, card_y - teal_h/2 - 0.03),
    teal_w, teal_h, boxstyle="round,pad=0.08",
    fc='#00000010', ec='none', zorder=1))
ax.add_patch(FancyBboxPatch((teal_x - teal_w/2, card_y - teal_h/2),
    teal_w, teal_h, boxstyle="round,pad=0.08",
    fc=C['teal'], ec='none', zorder=2))
ax.text(teal_x, card_y + 0.28,
        r'+ $\Delta\tau$-free diagnostic',
        ha='center', va='center', fontsize=10.5, fontweight='bold', color='white', zorder=5)
ax.text(teal_x, card_y + 0.04, '(Prop. 5)',
        ha='center', va='center', fontsize=11, fontweight='bold', color='white', zorder=5)
ax.text(teal_x, card_y - 0.28,
        r'$\frac{|\delta_s|}{(1{-}2\bar{\pi})\cdot\pi_s} > 1$',
        ha='center', va='center', fontsize=11, color='#B2DFDB', zorder=5)


# ─── Save ───
out = '/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/figures'
fig.savefig(f'{out}/fig_combined_overview.png', dpi=300, bbox_inches='tight',
            pad_inches=0.08, facecolor='white')
fig.savefig(f'{out}/fig_combined_overview.pdf', dpi=300, bbox_inches='tight',
            pad_inches=0.08, facecolor='white')
plt.close()
print('Done: fig_combined_overview.png + .pdf')
