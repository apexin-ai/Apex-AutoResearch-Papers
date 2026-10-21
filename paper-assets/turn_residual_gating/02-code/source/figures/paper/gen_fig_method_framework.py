"""Method framework figure: (a) ThreadGate Architecture, (b) Training & Evaluation, (c) Diagnosis & Fix."""
import sys
sys.path.insert(0, '/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/figures/paper')
from palette import *
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
import matplotlib.patheffects as pe
import numpy as np

apply_style()
plt.rcParams.update({'font.size': 9, 'axes.titlesize': 10.5})

NAVY = '#1D6289'; COPPER = '#C07A55'; TEAL = '#8ABECC'; LBLUE = '#7BA7C2'
BG = '#F5F6F7'; BORDER = '#DEE2E6'; GREEN = '#27AE60'; RED = '#C0392B'
MUTED = '#7F8C8D'; DARK = '#333333'
LG_BG = '#D4EDDA'; LR_BG = '#F8D7DA'; LB_BG = '#EBF5FB'
WARM_BG = '#FDF2E9'; YELLOW_BG = '#FFF3CD'

fig = plt.figure(figsize=(14, 5), facecolor='white')
ax_a = fig.add_axes([0.02, 0.02, 0.30, 0.96])
ax_b = fig.add_axes([0.35, 0.02, 0.32, 0.96])
ax_c = fig.add_axes([0.69, 0.02, 0.30, 0.96])

for ax in [ax_a, ax_b, ax_c]:
    ax.set_xlim(0, 10); ax.set_ylim(0, 10); ax.axis('off')


def rbox(ax, x, y, w, h, label, sub=None, fill=BG, edge=BORDER, lw=0.8,
         fs=8.5, sfs=7, bold=False, r=0.15, lc=DARK, sc=MUTED):
    shadow = FancyBboxPatch((x+0.04, y-0.04), w, h,
                            boxstyle=f"round,pad=0,rounding_size={r}",
                            fc='#000000', ec='none', alpha=0.06, zorder=1)
    box = FancyBboxPatch((x, y), w, h,
                         boxstyle=f"round,pad=0,rounding_size={r}",
                         fc=fill, ec=edge, lw=lw, zorder=2)
    ax.add_patch(shadow); ax.add_patch(box)
    cx = x + w/2; wt = 'bold' if bold else 'normal'
    if sub:
        ax.text(cx, y+h*0.65, label, fontsize=fs, ha='center', va='center',
                color=lc, fontweight=wt, zorder=3)
        ax.text(cx, y+h*0.28, sub, fontsize=sfs, ha='center', va='center',
                color=sc, zorder=3, fontstyle='italic')
    else:
        ax.text(cx, y+h/2, label, fontsize=fs, ha='center', va='center',
                color=lc, fontweight=wt, zorder=3)
    return box


def arr(ax, s, e, color=NAVY, lw=1.0, style='->'):
    ax.add_patch(FancyArrowPatch(s, e, arrowstyle=style, mutation_scale=10,
                                 color=color, lw=lw, zorder=4))


def circ(ax, cx, cy, txt, sz=0.28, fc='white', ec=NAVY):
    ax.add_patch(plt.Circle((cx, cy), sz, fc=fc, ec=ec, lw=0.9, zorder=5))
    ax.text(cx, cy, txt, fontsize=11, ha='center', va='center',
            color=ec, fontweight='bold', zorder=6, fontfamily='sans-serif')


def xmark(ax, x, y, c=RED, s=0.15):
    for dx, dy in [(-1,-1), (-1,1)]:
        ax.plot([x-s, x+s], [y+dy*s, y-dy*s], color=c, lw=1.8,
                solid_capstyle='round', zorder=6)


# ═══════════════ Panel (a): ThreadGate Architecture ═══════════════
ax_a.set_title('(a) ThreadGate Architecture', fontsize=10.5, pad=8,
               loc='left', fontweight='bold', color=DARK)

# Main vertical flow, centered at x=5.0
cx = 5.0

# Input x_l
rbox(ax_a, 3.0, 8.7, 4.0, 0.7, r'Input  $\mathbf{x}_l$',
     fill=BG, edge=BORDER, fs=9, bold=True)
arr(ax_a, (cx, 8.7), (cx, 8.0), color=NAVY)

# Transformer Block
rbox(ax_a, 2.5, 5.7, 5.0, 2.2, 'Transformer Block',
     sub=r'$f_l(\mathbf{x}_l)$', fill='white', edge=LBLUE, lw=1.2,
     fs=9.5, sfs=9.5)

# Gate MLP (left, offset)
rbox(ax_a, 0.1, 3.2, 3.3, 1.4, 'Gate MLP', sub='2-layer, 57K params',
     fill=LB_BG, edge=TEAL, lw=1.0, fs=8.5, sfs=6.5)

# Gate input arrows from Transformer region → Gate MLP top
# Content (from hidden state)
ax_a.annotate('', xy=(0.9, 4.65), xytext=(2.0, 5.65),
              arrowprops=dict(arrowstyle='->', color=LBLUE, lw=0.8,
                              connectionstyle='arc3,rad=0.2'))
ax_a.text(0.6, 5.35, 'content', fontsize=6, color=LBLUE, ha='center')

# Turn embedding
ax_a.annotate('', xy=(2.5, 4.65), xytext=(3.5, 5.65),
              arrowprops=dict(arrowstyle='->', color=COPPER, lw=0.8,
                              connectionstyle='arc3,rad=0.15'))
ax_a.text(3.9, 5.25, 'turn $t$', fontsize=6, color=COPPER, ha='center')

# Gate annotations
ax_a.text(1.75, 2.6, r'$g_l \in (0,1)$, init $\approx 0.82$',
          fontsize=6.5, color=MUTED, fontstyle='italic', ha='center')
ax_a.text(1.75, 2.2, '<0.001% params', fontsize=5.5, color=MUTED, ha='center')

# Transformer → ⊗
arr(ax_a, (cx, 5.7), (cx, 4.6), color=NAVY)
circ(ax_a, cx, 4.25, '×', sz=0.28)

# Gate → ⊗
arr(ax_a, (3.4, 3.9), (4.65, 4.25), color=TEAL, lw=0.9)
ax_a.text(3.75, 4.3, r'$g_l$', fontsize=8, color=TEAL, ha='center', va='bottom')

# ⊗ → ⊕
arr(ax_a, (cx, 3.95), (cx, 2.85), color=NAVY)
circ(ax_a, cx, 2.5, '+', sz=0.28)

# Skip connection
sx = 8.2
ax_a.plot([sx, sx], [9.0, 2.5], ls=(0,(4,3)), color='#AABBCC', lw=1.0, zorder=1)
ax_a.plot([sx, 5.35], [2.5, 2.5], ls=(0,(4,3)), color='#AABBCC', lw=1.0, zorder=1)
ax_a.text(sx+0.4, 5.5, 'skip', fontsize=6.5, color='#8899AA',
          ha='center', rotation=90, fontstyle='italic')

# ⊕ → output
arr(ax_a, (cx, 2.2), (cx, 1.35), color=NAVY)
rbox(ax_a, 1.8, 0.45, 6.4, 0.75,
     r'$\mathbf{x}_{l+1} = \mathbf{x}_l + g_l \cdot f_l(\mathbf{x}_l)$',
     fill=BG, edge=BORDER, fs=8.5)


# ═══════════════ Panel (b): Training & Evaluation ═══════════════
ax_b.set_title('(b) Training & Evaluation', fontsize=10.5, pad=8,
               loc='left', fontweight='bold', color=DARK)

# Loss equation
ax_b.text(5.0, 9.2,
          r'$\mathcal{L} = \mathcal{L}_{\mathrm{NTP}} + \mathcal{L}_{\mathrm{GAR}} + \mathcal{L}_{\mathrm{div}}$',
          fontsize=12, ha='center', va='center', color=DARK, fontweight='bold')

# Three loss boxes
for cx_, lbl, sub, fill, edge in [
    (1.7, r'$\mathcal{L}_{\mathrm{NTP}}$', 'Next-token\nprediction', 'white', BORDER),
    (5.0, r'$\mathcal{L}_{\mathrm{GAR}}$', 'MSE(GAR, τ=0.5)\nbidirectional', LB_BG, TEAL),
    (8.3, r'$\mathcal{L}_{\mathrm{div}}$', 'Gate diversity\nprevents collapse', LB_BG, TEAL),
]:
    rbox(ax_b, cx_-1.35, 7.15, 2.7, 1.35, lbl, sub=sub, fill=fill, edge=edge,
         fs=9, sfs=6.5, sc=NAVY if fill == LB_BG else '#888888')
    ax_b.annotate('', xy=(cx_, 8.55), xytext=(cx_, 8.95),
                  arrowprops=dict(arrowstyle='->', color='#CCCCCC', lw=0.6))

# Separator
ax_b.plot([0.5, 9.5], [6.6, 6.6], color=BORDER, lw=0.5)
ax_b.text(5.0, 6.05, 'The Problem — Exposure Bias', fontsize=9.5,
          ha='center', color=DARK, fontweight='bold')

# Teacher-Forced (green) — checkmark as part of sublabel
rbox(ax_b, 0.6, 3.2, 3.6, 2.3, 'Teacher-Forced', sub='GAR = 0.50',
     fill=LG_BG, edge=GREEN, lw=1.0, fs=9.5, sfs=10, bold=True, sc='#1B7A3D')
# Checkmark below GAR text
ax_b.plot([2.05, 2.4, 2.9], [3.4, 3.2, 3.6], color=GREEN, lw=2.2,
          solid_capstyle='round', zorder=6)

# Autoregressive (red)
rbox(ax_b, 5.8, 3.2, 3.8, 2.3, 'Autoregressive', sub='GAR = 0.019–0.064',
     fill=LR_BG, edge=RED, lw=1.0, fs=9.5, sfs=10, bold=True, sc='#8B2020')
xmark(ax_b, 7.7, 3.4, c=RED, s=0.18)

# Collapse annotation
mid = (0.6+3.6 + 5.8) / 2
ax_b.annotate('', xy=(5.65, 4.35), xytext=(4.35, 4.35),
              arrowprops=dict(arrowstyle='->', color=RED, lw=2.0))
ax_b.text(mid, 5.1, '8–17×', fontsize=11, ha='center', va='center',
          color=RED, fontweight='bold')
ax_b.text(mid, 4.7, 'collapse', fontsize=8, ha='center', va='center',
          color=RED, fontweight='medium')

ax_b.text(5.0, 2.5, 'TF matches target; AR generation collapses gate usage',
          fontsize=6.5, ha='center', color=MUTED, fontstyle='italic')


# ═══════════════ Panel (c): Diagnosis & Fix ═══════════════
ax_c.set_title('(c) Diagnosis & Fix', fontsize=10.5, pad=8,
               loc='left', fontweight='bold', color=DARK)

chain = [
    ('TG vs UG', 'rules out turn conditioning'),
    ('TG vs LoRA', 'rules out gating mechanism'),
    ('TG vs PCGrad', 'rules out gradient conflict'),
]
y_top = 9.0; bh = 0.72; gap = 0.32
bw = 7.2; bx = 0.5; bcx = bx + bw/2

for i, (lbl, desc) in enumerate(chain):
    y = y_top - i*(bh+gap)
    rbox(ax_c, bx, y, bw, bh, f'{lbl}  →  {desc}',
         fill=BG, edge=BORDER, lw=0.6, fs=7.5)
    xmark(ax_c, 8.5, y+bh/2, c=RED, s=0.14)
    if i < 2:
        arr(ax_c, (bcx, y-0.02), (bcx, y-gap+0.05), color='#CCCCCC', lw=0.6)

# Diagnosis
y_d = y_top - 3*(bh+gap)
rbox(ax_c, bx, y_d, bw, bh, 'Diagnosis: Exposure Bias',
     fill=YELLOW_BG, edge=COPPER, lw=1.5, fs=8.5, bold=True, lc='#8B5E3C')
ax_c.text(8.5, y_d+bh/2, '!', fontsize=13, ha='center', va='center',
          color=COPPER, fontweight='bold', fontfamily='sans-serif', zorder=6)
arr(ax_c, (bcx, y_top-2*(bh+gap)-0.02), (bcx, y_d+bh+0.05),
    color='#CCCCCC', lw=0.6)

# Separator + subtitle
sep = y_d - 0.5
ax_c.plot([0.5, 9.5], [sep, sep], color=BORDER, lw=0.5)
ax_c.text(5.0, sep-0.35, 'Two Fixes', fontsize=9, ha='center',
          color=DARK, fontweight='bold')

# Fix boxes
fy = sep - 2.3

# β-Steering
rbox(ax_c, 0.3, fy, 4.3, 1.8, r'$\beta$-Steering',
     sub='Inference-time\nGAR → 0.727', fill=LB_BG, edge=NAVY, lw=1.0,
     fs=9.5, sfs=7.5, bold=True, lc=NAVY, sc=NAVY)
ax_c.text(2.45, fy+0.12, 'additive bias on goal tokens',
          fontsize=5.5, ha='center', color=MUTED, fontstyle='italic')

# Scheduled Sampling
rbox(ax_c, 5.3, fy, 4.4, 1.8, 'Scheduled Sampling',
     sub='Training-time\nGap: 7.8× → 1.3×', fill=WARM_BG, edge=COPPER, lw=1.0,
     fs=9.5, sfs=7.5, bold=True, lc=COPPER, sc=COPPER)
ax_c.text(7.5, fy+0.12, 'mixes model-generated tokens',
          fontsize=5.5, ha='center', color=MUTED, fontstyle='italic')

# Arrows from diagnosis to fixes
arr(ax_c, (2.45, y_d-0.02), (2.45, fy+1.85), color='#CCCCCC', lw=0.7)
arr(ax_c, (7.5, y_d-0.02), (7.5, fy+1.85), color='#CCCCCC', lw=0.7)

save_fig(fig, 'fig_method_framework')
