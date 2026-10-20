#!/usr/bin/env python3
"""Figure 1: Trace-based verdict prediction pipeline overview.

Narrative: Full traces hurt accuracy; compact exception events achieve
near-perfect results -- the 'less is more' finding.
"""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
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
fig.patch.set_facecolor('white')

# ─── Colors ───
BD = '#999999'
AC = '#777777'


def rbox(x, y, w, h, fc, ec=BD, lw=0.8, ls='-'):
    ax.add_patch(FancyBboxPatch(
        (x, y), w, h, boxstyle="round,pad=0.07",
        facecolor=fc, edgecolor=ec, linewidth=lw, linestyle=ls, zorder=2))


def txt(x, y, s, fs=8, fw='bold', c='black', ha='center', va='center', **kw):
    ax.text(x, y, s, fontsize=fs, fontweight=fw, color=c,
            ha=ha, va=va, zorder=3, **kw)


def arr(x1, y1, x2, y2, lw=0.8):
    ax.annotate('', xy=(x2, y2), xytext=(x1, y1),
                arrowprops=dict(arrowstyle='->', color=AC, lw=lw), zorder=1)


# ─── Pipeline Constants ───
CY = 1.4
BH = 0.46
BY = CY - BH / 2
GAP = 0.15

# ── 1. Code + Test ──
bx, bw = 0.08, 0.82
rbox(bx, BY, bw, BH, '#D6E4F0')
txt(bx + bw / 2, CY + 0.07, 'Code + Test')
txt(bx + bw / 2, CY - 0.11, 'HumanEval+ / MBPP+',
    fs=5.5, fw='normal', c='#666', fontstyle='italic')
arr(bx + bw, CY, bx + bw + GAP, CY)

# ── 2. Execution ──
bx += bw + GAP
bw = 0.68
rbox(bx, BY, bw, BH, '#C5D9EC')
txt(bx + bw / 2, CY + 0.07, 'Execution')
txt(bx + bw / 2, CY - 0.11, 'Python tracer',
    fs=5.5, fw='normal', c='#666', fontstyle='italic')
arr(bx + bw, CY, bx + bw + GAP, CY)

# ── 3. Raw Trace ──
bx += bw + GAP
bw = 0.68
rbox(bx, BY, bw, BH, '#E5E0D8')
txt(bx + bw / 2, CY + 0.07, 'Raw Trace')
txt(bx + bw / 2, CY - 0.11, '~2000 tokens',
    fs=5.5, fw='normal', c='#666', fontstyle='italic')
trace_r = bx + bw

# ── 4. Trace Conditions ──
conds = [
    ("Exception Only", "99.83%", '#FFF0B0', '#7A6B00', True),
    ("VOTA",           "99.05%", '#B8E0C4', '#28854A', False),
    ("Full Trace",     "81.44%", '#F5DDB8', '#B06018', False),
    ("No Trace",       "75.13%", '#E0D3D3', '#A02828', False),
]
CH, CG, N = 0.37, 0.07, 4
tot = N * CH + (N - 1) * CG
yb = CY - tot / 2

CX, CW = 3.05, 1.50

# Dashed group outline
gp = 0.10
ax.add_patch(FancyBboxPatch(
    (CX - gp, yb - gp), CW + 2 * gp, tot + 2 * gp,
    boxstyle="round,pad=0.06", facecolor='#FAFAFA', edgecolor='#BBBBBB',
    linewidth=0.7, linestyle=(0, (4, 3)), zorder=1))
txt(CX + CW / 2, yb + tot + gp + 0.06, 'Trace Conditions',
    fs=6.5, fw='bold', c='#888', va='bottom')

# Fan-out backbone (vertical bus from Raw Trace)
bk_out = trace_r + 0.24
ax.plot([trace_r, bk_out], [CY, CY], color=AC, lw=0.8, zorder=1)

# Fan-in backbone (vertical bus toward SFT)
bk_in = CX + CW + 0.24

y_mids = []
for i, (name, acc, fc, ac, best) in enumerate(conds):
    y = yb + (N - 1 - i) * (CH + CG)
    ym = y + CH / 2
    y_mids.append(ym)

    ec = '#C89B00' if best else BD
    lw = 1.3 if best else 0.7
    ls = '--' if name == 'No Trace' else '-'
    rbox(CX, y, CW, CH, fc, ec=ec, lw=lw, ls=ls)

    txt(CX + 0.10, ym, name, fs=7, ha='left')
    txt(CX + CW - 0.08, ym, acc, fs=7, fw='bold', c=ac, ha='right')

    if best:
        ax.plot(CX - 0.06, ym, marker='*', color='#C89B00', markersize=8,
                markeredgewidth=0, zorder=3)

    # Fan-out: backbone branch -> condition
    arr(bk_out, ym, CX - 0.01, ym, lw=0.55)
    # Fan-in: condition -> backbone branch
    ax.plot([CX + CW + 0.01, bk_in], [ym, ym], color=AC, lw=0.55, zorder=1)

# Vertical backbones
ax.plot([bk_out, bk_out], [min(y_mids), max(y_mids)], color=AC, lw=0.8, zorder=1)
ax.plot([bk_in, bk_in], [min(y_mids), max(y_mids)], color=AC, lw=0.8, zorder=1)

# Junction dots (main + branches)
ax.plot(bk_out, CY, 'o', color=AC, markersize=3, zorder=3)
ax.plot(bk_in, CY, 'o', color=AC, markersize=3, zorder=3)
for ym in y_mids:
    ax.plot(bk_out, ym, '.', color=AC, markersize=2, zorder=3)
    ax.plot(bk_in, ym, '.', color=AC, markersize=2, zorder=3)

# Paradox annotation
txt(CX + CW / 2, yb - gp - 0.05, 'More trace ≠ higher accuracy',
    fs=5.5, fw='normal', c='#999', va='top', fontstyle='italic')

# ── 5. SFT ──
sx = bk_in + 0.22
sw = 0.60
arr(bk_in, CY, sx, CY)
rbox(sx, BY, sw, BH, '#B8D4F0')
txt(sx + sw / 2, CY + 0.07, 'SFT')
txt(sx + sw / 2, CY - 0.11, 'LoRA',
    fs=5.5, fw='normal', c='#666', fontstyle='italic')
arr(sx + sw, CY, sx + sw + GAP, CY)

# ── 6. Verdict ──
vx = sx + sw + GAP
vw = 0.62
rbox(vx, BY, vw, BH, '#DEDEDE')
txt(vx + vw / 2, CY + 0.07, 'Verdict')
txt(vx + vw / 2, CY - 0.11, 'pass / fail',
    fs=5.5, fw='normal', c='#666', fontstyle='italic')

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
