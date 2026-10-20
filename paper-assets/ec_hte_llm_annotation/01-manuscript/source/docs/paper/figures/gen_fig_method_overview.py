#!/usr/bin/env python3
"""Generate Figure 2: EC-HTE method overview (concept diagram).
Designed for EMNLP figure* (full textwidth ≈ 6.3in). figsize=10in → ~63% scale.
All font sizes chosen so printed text ≥ 7pt.
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Circle
import matplotlib.patheffects as pe

# ─── Figure ───
FW, FH = 10, 3.9
fig = plt.figure(figsize=(FW, FH), dpi=300, facecolor='white')
ax = fig.add_axes([0, 0, 1, 1])
ax.set_xlim(0, FW)
ax.set_ylim(0, FH)
ax.axis('off')
ax.set_facecolor('white')

plt.rcParams.update({'mathtext.fontset': 'cm', 'font.family': 'DejaVu Serif'})

# ─── Colors (muted academic) ───
C = dict(
    std_band='#FBE9E7',  std_fill='#FFCCBC',  std_border='#BF360C',
    std_text='#BF360C',  std_accent='#D84315',
    ours_band='#E0F2F1', ours_fill='#B2DFDB', ours_border='#00695C',
    ours_text='#00695C',  ours_accent='#00897B',
    input_fill='#E3F2FD', input_border='#1565C0', input_text='#0D47A1',
    header='#263238', label='#546E7A', anno='#78909C',
    result_good='#00897B', diag_fill='#FFF8E1', diag_border='#F9A825',
    diag_text='#E65100',
)

# ─── Layout ───
col = dict(input=1.3, est=3.7, corr=6.3, inf=8.9)
header_y = 3.65
std_y = 2.90
vs_y = 2.22
ours_y = 1.28
result_y = 0.22

BW, BH = 1.95, 0.58
IW, IH = 1.55, 0.38

# ─── Helpers ───
def rbox(x, y, w, h, fill, border, lw=1.2):
    shadow = FancyBboxPatch((x - w/2 + 0.02, y - h/2 - 0.018), w, h,
        boxstyle="round,pad=0.08", facecolor='#00000008', edgecolor='none', zorder=1)
    ax.add_patch(shadow)
    box = FancyBboxPatch((x - w/2, y - h/2), w, h, boxstyle="round,pad=0.08",
        facecolor=fill, edgecolor=border, linewidth=lw, zorder=2)
    ax.add_patch(box)

def btext(x, y, main, sub=None, color='black', ms=14, ss=10.5):
    if sub:
        ax.text(x, y + 0.09, main, ha='center', va='center', fontsize=ms,
                fontweight='bold', color=color, zorder=5)
        ax.text(x, y - 0.11, sub, ha='center', va='center', fontsize=ss,
                color=color, alpha=0.6, fontstyle='italic', zorder=5)
    else:
        ax.text(x, y, main, ha='center', va='center', fontsize=ms,
                fontweight='bold', color=color, zorder=5)

def arr(x1, y1, x2, y2, color='#90A4AE', lw=1.0, ls='-'):
    a = FancyArrowPatch((x1, y1), (x2, y2),
        arrowstyle='->,head_width=2.5,head_length=2.5',
        color=color, linewidth=lw, linestyle=ls, zorder=3, mutation_scale=10)
    ax.add_patch(a)

def icon_cross(x, y, bg):
    ax.add_patch(Circle((x, y), 0.12, facecolor=bg, edgecolor='white', lw=1.3, zorder=6))
    d = 0.05
    ax.plot([x-d, x+d], [y-d, y+d], color='white', lw=1.8, solid_capstyle='round', zorder=7)
    ax.plot([x-d, x+d], [y+d, y-d], color='white', lw=1.8, solid_capstyle='round', zorder=7)

def icon_check(x, y, bg):
    ax.add_patch(Circle((x, y), 0.12, facecolor=bg, edgecolor='white', lw=1.3, zorder=6))
    ax.plot([x-0.045, x-0.005, x+0.06], [y-0.005, y-0.05, y+0.05],
            color='white', lw=1.8, solid_capstyle='round', solid_joinstyle='round', zorder=7)

# ─── Background Bands ───
ax.add_patch(FancyBboxPatch((0.35, 2.55), FW - 0.7, 0.76,
    boxstyle="round,pad=0.1", facecolor=C['std_band'], edgecolor='none', zorder=0, alpha=0.55))
ax.add_patch(FancyBboxPatch((0.35, 0.6), FW - 0.7, 1.55,
    boxstyle="round,pad=0.1", facecolor=C['ours_band'], edgecolor='none', zorder=0, alpha=0.45))

# ─── Column Headers ───
for label, x in [('Input', col['input']), ('Estimation', col['est']),
                  ('Correction', col['corr']), ('Inference', col['inf'])]:
    ax.text(x, header_y, label, ha='center', va='center', fontsize=16,
            fontweight='bold', color=C['header'], zorder=5)
ax.plot([0.5, FW - 0.5], [header_y - 0.15, header_y - 0.15],
        color=C['header'], lw=0.4, alpha=0.2, zorder=1)

# ─── Row Labels ───
ax.text(0.55, std_y, 'Standard', ha='center', va='center', fontsize=12,
        fontweight='bold', color=C['std_accent'], rotation=90, zorder=5)
ax.text(0.38, ours_y + 0.08, 'EC-HTE', ha='center', va='center', fontsize=11,
        fontweight='bold', color=C['ours_accent'], rotation=90, zorder=5)
ax.text(0.38, ours_y - 0.28, '(Ours)', ha='center', va='center', fontsize=9,
        color=C['ours_accent'], alpha=0.7, rotation=90, zorder=5)

# ─── "vs." ───
ax.text(FW / 2, vs_y, 'vs.', ha='center', va='center', fontsize=16,
        fontweight='bold', color=C['label'], zorder=5)

# ═══════ STANDARD PATH ═══════
rbox(col['est'], std_y, BW, BH, C['std_fill'], C['std_border'])
btext(col['est'], std_y, r'Pooled CM $\hat{C}$', 'One matrix for all', C['std_text'])

rbox(col['corr'], std_y, BW, BH, C['std_fill'], C['std_border'])
btext(col['corr'], std_y, 'Global Correction', r'$\hat{C}^{-1}$ applied uniformly', C['std_text'])

rbox(col['inf'], std_y, BW, BH, '#FFCDD2', C['std_accent'], lw=1.6)
btext(col['inf'], std_y, 'Sign Reversal', '14.9% of configs', C['std_accent'])
icon_cross(col['inf'] + BW/2 - 0.03, std_y + BH/2 - 0.03, C['std_accent'])

arr(col['est'] + BW/2 + 0.06, std_y, col['corr'] - BW/2 - 0.1, std_y,
    color=C['std_accent'], lw=1.0)
arr(col['corr'] + BW/2 + 0.06, std_y, col['inf'] - BW/2 - 0.1, std_y,
    color=C['std_accent'], lw=1.0)

# ═══════ EC-HTE PATH ═══════
iy_top = ours_y + 0.27
iy_bot = ours_y - 0.27

rbox(col['input'], iy_top, IW, IH, C['input_fill'], C['input_border'], lw=0.9)
ax.text(col['input'], iy_top + 0.04, 'LLM Annotations', ha='center', va='center',
        fontsize=12, fontweight='bold', color=C['input_text'], zorder=5)
ax.text(col['input'], iy_top - 0.1, r'$N$ noisy labels $\hat{Z}$', ha='center',
        va='center', fontsize=9, color=C['input_text'], alpha=0.55,
        fontstyle='italic', zorder=5)

rbox(col['input'], iy_bot, IW, IH, C['input_fill'], C['input_border'], lw=0.9)
ax.text(col['input'], iy_bot + 0.04, 'Expert Labels', ha='center', va='center',
        fontsize=12, fontweight='bold', color=C['input_text'], zorder=5)
ax.text(col['input'], iy_bot - 0.1, r'$n_{\mathrm{expert}}$ pairs $(Z,\hat{Z})$',
        ha='center', va='center', fontsize=9, color=C['input_text'], alpha=0.55,
        fontstyle='italic', zorder=5)

rbox(col['est'], ours_y, BW, BH, C['ours_fill'], C['ours_border'])
btext(col['est'], ours_y, 'Hierarchical Bayes', r'Per-subgroup CMs $\{\hat{C}_s\}$',
      C['ours_text'])

rbox(col['corr'], ours_y, BW, BH, C['ours_fill'], C['ours_border'])
btext(col['corr'], ours_y, 'Per-subgroup Corr.', r'$\tilde{\mu}_s = \hat{C}_s^{-1} \cdot \hat{\mu}_s$',
      C['ours_text'])

rbox(col['inf'], ours_y, BW, BH, '#C8E6C9', C['ours_accent'], lw=1.6)
btext(col['inf'], ours_y, 'Corrected CATE', r'$\hat{\tau}(x) \pm \mathrm{SE}_{\mathrm{corr}}$',
      C['ours_accent'])
icon_check(col['inf'] + BW/2 - 0.03, ours_y + BH/2 - 0.03, C['ours_accent'])

arr(col['input'] + IW/2 + 0.06, iy_top, col['est'] - BW/2 - 0.1, ours_y + 0.06,
    color=C['ours_accent'], lw=0.9)
arr(col['input'] + IW/2 + 0.06, iy_bot, col['est'] - BW/2 - 0.1, ours_y - 0.06,
    color=C['ours_accent'], lw=0.9)
arr(col['est'] + BW/2 + 0.06, ours_y, col['corr'] - BW/2 - 0.1, ours_y,
    color=C['ours_accent'], lw=1.0)
arr(col['corr'] + BW/2 + 0.06, ours_y, col['inf'] - BW/2 - 0.1, ours_y,
    color=C['ours_accent'], lw=1.0)

# ─── "prior" dashed arrow ───
arr(col['est'], std_y - BH/2 - 0.04, col['est'], ours_y + BH/2 + 0.08,
    color=C['label'], lw=0.8, ls='--')
t = ax.text(col['est'] + 0.15, vs_y, 'prior', ha='left', va='center',
            fontsize=11, color=C['anno'], fontstyle='italic', zorder=5)
t.set_path_effects([pe.withStroke(linewidth=2.5, foreground='white')])

# ─── Annotations below EC-HTE boxes ───
ay = ours_y - BH/2 - 0.12
ax.text(col['est'], ay, r'Partial pooling · $\alpha_0$ via Emp. Bayes',
        ha='center', va='top', fontsize=9.5, color=C['anno'], zorder=5)
ax.text(col['corr'], ay, r'$\kappa$-guard: $\kappa > 100 \rightarrow$ fallback',
        ha='center', va='top', fontsize=9.5, color=C['anno'], zorder=5)
ax.text(col['inf'], ay, 'via CausalForestDML', ha='center', va='top',
        fontsize=9.5, color=C['anno'], zorder=5)

# ─── Bottom results ───
ax.text(FW / 2 - 1.3, result_y, '0% sign reversal  ·  |bias| ÷ 7.4',
        ha='center', va='center', fontsize=13, fontweight='bold',
        color=C['result_good'], fontfamily='DejaVu Sans', zorder=5)

dw, dh = 3.8, 0.28
dx = FW / 2 + 1.9
ax.add_patch(FancyBboxPatch((dx - dw/2, result_y - dh/2), dw, dh,
    boxstyle="round,pad=0.05", facecolor=C['diag_fill'],
    edgecolor=C['diag_border'], linewidth=0.9, zorder=2))
ax.text(dx, result_y,
        r'Diagnostic (Prop. 5): $|\delta_s|/((1{-}2\bar{\pi})\cdot\pi_s) > 1$',
        ha='center', va='center', fontsize=10.5, color=C['diag_text'], zorder=5)

# ─── Save ───
out = '/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/figures'
fig.savefig(f'{out}/fig_method_overview.png', dpi=300, bbox_inches='tight',
            pad_inches=0.06, facecolor='white')
fig.savefig(f'{out}/fig_method_overview.pdf', dpi=300, bbox_inches='tight',
            pad_inches=0.06, facecolor='white')
plt.close()
print('Done: fig_method_overview.png + .pdf')
