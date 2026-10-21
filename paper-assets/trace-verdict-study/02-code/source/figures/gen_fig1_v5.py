#!/usr/bin/env python3
"""Figure 1: Trace-based verdict prediction pipeline overview.

No accuracy numbers — visual hierarchy conveys the 'less is more' finding.
"""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
import matplotlib.patheffects as pe
import os

plt.rcParams.update({
    'font.family': 'serif',
    'font.serif': ['Nimbus Roman', 'Times New Roman', 'Liberation Serif',
                   'DejaVu Serif', 'serif'],
    'font.size': 9,
    'figure.dpi': 300,
    'savefig.dpi': 300,
    'savefig.bbox': 'tight',
    'savefig.pad_inches': 0.05,
})

fig, ax = plt.subplots(figsize=(7.0, 2.8))
ax.set_xlim(0, 7.0)
ax.set_ylim(0, 2.8)
ax.axis('off')
fig.patch.set_facecolor('#FAFAF8')

# ─── Colors ───
BD = '#C0C0C0'
AC = '#9E9E9E'
SHADOW = '#00000008'


def shadow_box(x, y, w, h, fc, ec=BD, lw=0.8, ls='-', shadow=True):
    if shadow:
        ax.add_patch(FancyBboxPatch(
            (x + 0.03, y - 0.03), w, h, boxstyle="round,pad=0.07",
            facecolor=SHADOW, edgecolor='none', linewidth=0, zorder=1))
    ax.add_patch(FancyBboxPatch(
        (x, y), w, h, boxstyle="round,pad=0.07",
        facecolor=fc, edgecolor=ec, linewidth=lw, linestyle=ls, zorder=2))


def txt(x, y, s, fs=8, fw='bold', c='black', ha='center', va='center', **kw):
    ax.text(x, y, s, fontsize=fs, fontweight=fw, color=c,
            ha=ha, va=va, zorder=3, **kw)


def curved_arr(x1, y1, x2, y2, lw=0.7, cs='arc3,rad=0.0'):
    ax.add_patch(FancyArrowPatch(
        (x1, y1), (x2, y2),
        arrowstyle='->', mutation_scale=8,
        connectionstyle=cs,
        color=AC, lw=lw, zorder=1))


def straight_arr(x1, y1, x2, y2, lw=0.7):
    ax.annotate('', xy=(x2, y2), xytext=(x1, y1),
                arrowprops=dict(arrowstyle='->', color=AC, lw=lw,
                                shrinkA=0, shrinkB=0), zorder=1)


# ─── Pipeline Constants ───
CY = 1.4
BH = 0.46
BY = CY - BH / 2
GAP = 0.15

# ── 1. Code + Test ──
bx, bw = 0.08, 0.82
shadow_box(bx, BY, bw, BH, '#E8EFF7', ec='#A8BDD4')
txt(bx + bw / 2, CY + 0.07, 'Code + Test', c='#2C3E50')
txt(bx + bw / 2, CY - 0.11, 'HumanEval+ / MBPP+',
    fs=5.5, fw='normal', c='#7F8C8D', fontstyle='italic')
straight_arr(bx + bw + 0.02, CY, bx + bw + GAP - 0.02, CY)

# ── 2. Execution ──
bx += bw + GAP
bw = 0.68
shadow_box(bx, BY, bw, BH, '#D4E4F2', ec='#8BAAC8')
txt(bx + bw / 2, CY + 0.07, 'Execution', c='#2C3E50')
txt(bx + bw / 2, CY - 0.11, 'Python tracer',
    fs=5.5, fw='normal', c='#7F8C8D', fontstyle='italic')
straight_arr(bx + bw + 0.02, CY, bx + bw + GAP - 0.02, CY)

# ── 3. Raw Trace ──
bx += bw + GAP
bw = 0.68
shadow_box(bx, BY, bw, BH, '#EDE8E0', ec='#B8AFA4')
txt(bx + bw / 2, CY + 0.07, 'Raw Trace', c='#2C3E50')
txt(bx + bw / 2, CY - 0.11, '~2k tokens avg.',
    fs=5.5, fw='normal', c='#7F8C8D', fontstyle='italic')
trace_r = bx + bw

# ── 4. Trace Conditions (no numbers!) ──
conds = [
    ("Exception Only", "Exception & error events",     '#FFF5D6', '#C89B00', True),
    ("VOTA",           "Exception + assertion + loops", '#D4EDDA', '#3D8B58', False),
    ("Full Trace",     "Complete line-by-line log",     '#FAE5CC', '#B87333', False),
    ("No Trace",       "Source code only (baseline)",   '#E8E3E3', '#888888', False),
]
CH, CG, N = 0.37, 0.07, 4
tot = N * CH + (N - 1) * CG
yb = CY - tot / 2

CX, CW = 3.05, 1.55

# Dashed group outline with shadow
ax.add_patch(FancyBboxPatch(
    (CX - 0.10 + 0.02, yb - 0.10 - 0.02), CW + 0.20, tot + 0.20,
    boxstyle="round,pad=0.06", facecolor='#00000006', edgecolor='none',
    linewidth=0, zorder=0))
ax.add_patch(FancyBboxPatch(
    (CX - 0.10, yb - 0.10), CW + 0.20, tot + 0.20,
    boxstyle="round,pad=0.06", facecolor='#FAFAF8', edgecolor='#CCCCCC',
    linewidth=0.6, linestyle=(0, (4, 3)), zorder=1))
txt(CX + CW / 2, yb + tot + 0.10 + 0.06, 'Trace Conditions',
    fs=6.5, fw='bold', c='#888888', va='bottom')

# Fan-out backbone
bk_out = trace_r + 0.22
ax.plot([trace_r + 0.02, bk_out], [CY, CY], color=AC, lw=0.7, zorder=1)

# Fan-in backbone
bk_in = CX + CW + 0.22

# Left accent bar (pill shape)
def accent_bar(x, y, h, color):
    bar_w = 0.045
    bar_r = bar_w / 2
    ax.add_patch(FancyBboxPatch(
        (x, y + 0.02), bar_w, h - 0.04,
        boxstyle=f"round,pad={bar_r}",
        facecolor=color, edgecolor='none', linewidth=0, zorder=3))

y_mids = []
for i, (name, desc, fc, accent_c, best) in enumerate(conds):
    y = yb + (N - 1 - i) * (CH + CG)
    ym = y + CH / 2
    y_mids.append(ym)

    ec = '#C89B00' if best else BD
    lw_box = 1.2 if best else 0.6
    ls = '--' if name == 'No Trace' else '-'
    shadow_box(CX, y, CW, CH, fc, ec=ec, lw=lw_box, ls=ls)

    # Left accent bar
    accent_bar(CX + 0.06, y, CH, accent_c)

    # Name (bold) + description (light)
    txt(CX + 0.15, ym + 0.05, name, fs=7, fw='bold', ha='left', c='#2C3E50')
    txt(CX + 0.15, ym - 0.08, desc, fs=5.2, fw='normal', ha='left',
        c='#7F8C8D', fontstyle='italic')

    if best:
        ax.plot(CX - 0.06, ym, marker='*', color='#C89B00', markersize=9,
                markeredgewidth=0, zorder=3)

    # Fan-out: backbone → condition
    straight_arr(bk_out, ym, CX - 0.01, ym, lw=0.5)
    # Fan-in: condition → backbone
    ax.plot([CX + CW + 0.01, bk_in], [ym, ym], color=AC, lw=0.5, zorder=1)

# Vertical backbones
ax.plot([bk_out, bk_out], [min(y_mids), max(y_mids)], color=AC, lw=0.7, zorder=1)
ax.plot([bk_in, bk_in], [min(y_mids), max(y_mids)], color=AC, lw=0.7, zorder=1)

# Junction dots
ax.plot(bk_out, CY, 'o', color=AC, markersize=2.5, zorder=3)
ax.plot(bk_in, CY, 'o', color=AC, markersize=2.5, zorder=3)
for ym in y_mids:
    ax.plot(bk_out, ym, '.', color=AC, markersize=1.8, zorder=3)
    ax.plot(bk_in, ym, '.', color=AC, markersize=1.8, zorder=3)

# Info density gradient bar (right side, continuous)
grad_x = CX + CW + 0.06
grad_w = 0.04
grad_bot = min(y_mids) - CH / 2
grad_top = max(y_mids) + CH / 2
n_grad = 100
for gi in range(n_grad):
    frac = gi / n_grad
    gy = grad_bot + frac * (grad_top - grad_bot)
    gh = (grad_top - grad_bot) / n_grad
    r = int(0xC8 + frac * (0xFA - 0xC8))
    g = int(0x9B + frac * (0xE5 - 0x9B))
    b = int(0x00 + frac * (0xCC - 0x00))
    ax.add_patch(plt.Rectangle((grad_x, gy), grad_w, gh + 0.002,
                                facecolor=f'#{r:02x}{g:02x}{b:02x}',
                                edgecolor='none', zorder=1))

# Gradient labels
txt(grad_x + grad_w / 2, grad_top + 0.08, 'Info\ndensity',
    fs=4.5, fw='normal', c='#999999', ha='center', va='bottom',
    linespacing=0.9)
ax.annotate('', xy=(grad_x + grad_w / 2, grad_top + 0.02),
            xytext=(grad_x + grad_w / 2, grad_bot - 0.02),
            arrowprops=dict(arrowstyle='->', color='#BBBBBB', lw=0.4))

# Bottom annotation
txt(CX + CW / 2, yb - 0.10 - 0.08, 'Less trace  →  higher accuracy',
    fs=5.5, fw='normal', c='#AAAAAA', va='top', fontstyle='italic')

# ── 5. SFT ──
sx = bk_in + 0.22
sw = 0.60
straight_arr(bk_in + 0.02, CY, sx - 0.02, CY)
shadow_box(sx, BY, sw, BH, '#C8DDEF', ec='#7EA8CC')
txt(sx + sw / 2, CY + 0.07, 'SFT', c='#2C3E50')
txt(sx + sw / 2, CY - 0.11, 'LoRA, 1.5B–13B',
    fs=5.5, fw='normal', c='#7F8C8D', fontstyle='italic')
straight_arr(sx + sw + 0.02, CY, sx + sw + GAP - 0.02, CY)

# ── 6. Verdict ──
vx = sx + sw + GAP
vw = 0.62

shadow_box(vx, BY, vw, BH, '#F0F0F0', ec='#AAAAAA')
txt(vx + vw / 2, CY + 0.07, 'Verdict', c='#2C3E50')
txt(vx + vw / 2, CY - 0.11, 'pass / fail',
    fs=5.5, fw='normal', c='#7F8C8D', fontstyle='italic')

# ── Save ──
out_dir = os.path.dirname(os.path.abspath(__file__))
paper_dir = os.path.join(out_dir, 'paper')
os.makedirs(paper_dir, exist_ok=True)
for fmt, fn in [('pdf', 'fig1_trace_overview.pdf'),
                ('png', 'fig1_trace_overview.png')]:
    p = os.path.join(paper_dir, fn)
    fig.savefig(p, format=fmt)
    print(f"Saved: {p}")
plt.close()
