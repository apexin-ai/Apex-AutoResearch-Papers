#!/usr/bin/env python3
"""Figure 1: Verdict prediction pipeline — publication-quality hero figure."""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
import os

plt.rcParams.update({
    'font.family': 'serif',
    'font.serif': ['Times New Roman', 'DejaVu Serif', 'Nimbus Roman', 'serif'],
    'font.size': 10,
    'figure.dpi': 300,
    'savefig.dpi': 300,
    'savefig.bbox': 'tight',
    'savefig.pad_inches': 0.08,
})

W, H = 14, 4.5
fig, ax = plt.subplots(figsize=(W, H))
ax.set_xlim(0, W)
ax.set_ylim(0, H)
ax.axis('off')
fig.patch.set_facecolor('white')

C_TEXT = '#2C3E50'
C_SUB = '#7F8C8D'
C_ARROW = '#95A5A6'
C_BORDER = '#BDC3C7'

def draw_box(x, y, w, h, fc, ec=C_BORDER, lw=1.0, ls='-'):
    s = FancyBboxPatch((x + 0.04, y - 0.04), w, h, boxstyle="round,pad=0.06",
                        fc='#000000', ec='none', alpha=0.07, zorder=1)
    ax.add_patch(s)
    b = FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.06",
                        fc=fc, ec=ec, lw=lw, ls=ls, zorder=2)
    ax.add_patch(b)

def draw_arrow(x1, y1, x2, y2, color=C_ARROW, lw=1.0):
    a = FancyArrowPatch((x1, y1), (x2, y2),
                         arrowstyle='->,head_length=5,head_width=3',
                         color=color, lw=lw, zorder=3)
    ax.add_patch(a)

def txt(x, y, s, **kw):
    d = dict(ha='center', va='center', color=C_TEXT, zorder=5)
    d.update(kw)
    ax.text(x, y, s, **d)

MY = H / 2
BH = 1.2
y_pipe = MY - BH / 2

# ========== 1. Source Code + Test Case ==========
x1, w1 = 0.3, 1.7
draw_box(x1, y_pipe, w1, BH, '#E8EDF2')
txt(x1 + w1/2, y_pipe + BH*0.63, 'Source Code', fontsize=10, fontweight='bold')
txt(x1 + w1/2, y_pipe + BH*0.37, '+ Test Case', fontsize=9, color='#555555')

# Arrow 1
a1_start = x1 + w1 + 0.06
a1_end = a1_start + 0.50
draw_arrow(a1_start, MY, a1_end, MY)
txt((a1_start + a1_end)/2, MY + 0.18, 'Execute', fontsize=7.5, color=C_SUB, style='italic')

# ========== 2. Raw Execution Trace ==========
x2 = a1_end
w2 = 1.8
draw_box(x2, y_pipe, w2, BH, '#FDF6E3', '#D5C4A1')
txt(x2 + w2/2, y_pipe + BH*0.78, 'Raw Execution', fontsize=9.5, fontweight='bold')
txt(x2 + w2/2, y_pipe + BH*0.60, 'Trace', fontsize=9.5, fontweight='bold')
for i, line in enumerate(['line 3: x = 0', 'line 5: for i in ...', 'line 7: x += i', '...']):
    txt(x2 + 0.18, y_pipe + BH*0.42 - i*0.11, line,
        fontsize=5.8, color='#AAAAAA', ha='left', family='monospace')
txt(x2 + w2/2, y_pipe - 0.10, '~2000 tokens', fontsize=6.5, color=C_SUB, style='italic')

# Arrow 2
a2_start = x2 + w2 + 0.06
a2_end = a2_start + 0.50
draw_arrow(a2_start, MY, a2_end, MY)
txt((a2_start + a2_end)/2, MY + 0.20, 'Filter', fontsize=7.5, color=C_SUB, style='italic',
    zorder=6, bbox=dict(fc='white', ec='none', pad=1, alpha=0.9))

# ========== 3. Four Condition Boxes ==========
cx_start = a2_end
cw = 1.12
cgap = 0.12
ch = 2.2
cy = MY - ch / 2

group_pad = 0.18
group_w = 4 * cw + 3 * cgap + 2 * group_pad
group_h = ch + 2 * group_pad + 0.25
group_y = cy - group_pad
bg = FancyBboxPatch((cx_start - group_pad, group_y), group_w, group_h,
                     boxstyle="round,pad=0.10", fc='#FAFAFA', ec='#DDDDDD',
                     lw=0.8, ls=(0, (5, 3)), zorder=0)
ax.add_patch(bg)

txt(cx_start - group_pad + group_w / 2, group_y + group_h + 0.12,
    'Trace Filtering Conditions', fontsize=9.5, fontweight='bold', color='#666666')

conditions = [
    ('No Trace',        '75.13%', '#F0F0F0', '#CCCCCC', 0.8, (0, (4, 3))),
    ('Full Trace',      '81.44%', '#E8EDF2', C_BORDER,  1.0, '-'),
    ('VOTA',            '99.05%', '#D4E6F1', '#5DADE2', 1.2, '-'),
    ('Exception\nOnly', '99.83%', '#FFF3CD', '#27AE60', 2.0, '-'),
]

for i, (name, acc, fc, ec, lw, ls) in enumerate(conditions):
    cx = cx_start + i * (cw + cgap)
    draw_box(cx, cy, cw, ch, fc, ec, lw, ls)

    is_best = (i == 3)
    txt(cx + cw/2, cy + ch*0.70, name, fontsize=9.5, fontweight='bold')
    txt(cx + cw/2, cy + ch*0.40, acc,
        fontsize=12 if is_best else 10,
        fontweight='bold' if is_best else 'normal',
        color='#27AE60' if is_best else C_TEXT)
    if is_best:
        ax.plot(cx + cw/2, cy + ch*0.20, marker='*', markersize=18,
                color='#F39C12', markeredgecolor='#E67E22', markeredgewidth=0.5,
                zorder=5, linestyle='none')

wl = cx_start + 0.15
wr = cx_start + 3*(cw + cgap) + cw - 0.15
txt(wl, cy - 0.22, 'weakest', fontsize=6.5, color='#AAAAAA', style='italic', ha='left')
txt(wr, cy - 0.22, 'strongest', fontsize=6.5, color='#AAAAAA', style='italic', ha='right')
draw_arrow(wl + 0.32, cy - 0.22, wr - 0.38, cy - 0.22, color='#CCCCCC', lw=0.6)

# Arrow 3
last_right = cx_start + 3*(cw + cgap) + cw
a3_start = last_right + 0.06 + group_pad
a3_end = a3_start + 0.45
draw_arrow(a3_start, MY, a3_end, MY)

# ========== 4. SFT Training (LoRA) ==========
sx = a3_end
sw = 1.3
draw_box(sx, y_pipe, sw, BH, '#D6EAF8')
txt(sx + sw/2, y_pipe + BH*0.63, 'SFT Training', fontsize=9.5, fontweight='bold')
txt(sx + sw/2, y_pipe + BH*0.37, '(LoRA)', fontsize=8.5, color='#555555')

# Arrow 4
a4_start = sx + sw + 0.06
a4_end = a4_start + 0.40
draw_arrow(a4_start, MY, a4_end, MY)

# ========== 5. Verdict ==========
vx = a4_end
vw = 1.05
draw_box(vx, y_pipe, vw, BH, '#E8F8F5', '#27AE60', 1.3)
txt(vx + vw/2, y_pipe + BH*0.63, 'Verdict', fontsize=10, fontweight='bold')
txt(vx + vw/2, y_pipe + BH*0.37, 'pass / fail', fontsize=8.5, color='#555555')

# ========== Save ==========
out_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'paper')
os.makedirs(out_dir, exist_ok=True)
png = os.path.join(out_dir, 'fig1_trace_overview_pb.png')
pdf = os.path.join(out_dir, 'fig1_trace_overview_pb.pdf')
fig.savefig(png, format='png')
fig.savefig(pdf, format='pdf')
plt.close()
print(f'Saved: {png}')
print(f'Saved: {pdf}')
