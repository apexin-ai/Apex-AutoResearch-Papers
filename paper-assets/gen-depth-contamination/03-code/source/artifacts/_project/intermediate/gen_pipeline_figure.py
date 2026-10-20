#!/usr/bin/env python3
"""Generate the method pipeline overview figure for the paper."""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

fig, ax = plt.subplots(figsize=(7.2, 2.2))
ax.set_xlim(-0.2, 10.7)
ax.set_ylim(-0.1, 2.3)
ax.set_aspect('equal')
ax.axis('off')

# -- Style --
F_TITLE = {'family': 'serif', 'size': 8.5, 'weight': 'bold'}
F_BODY = {'family': 'serif', 'size': 6.2}
F_TINY = {'family': 'serif', 'size': 5.5, 'style': 'italic'}
F_MATH = {'family': 'serif', 'size': 6.5}
ARR = dict(arrowstyle='->', color='#333333', lw=1.2,
           connectionstyle='arc3,rad=0', mutation_scale=11)
BOX = dict(boxstyle='round,pad=0.12', linewidth=0.7, edgecolor='#444444')

C = {'seed': '#E0E8F0', 'gen': '#FFF3E0', 'feat': '#E0F0E4',
     'cls': '#EDE0F0', 'out': '#E8EAEC'}

def box(cx, cy, w, h, color):
    p = FancyBboxPatch((cx - w/2, cy - h/2), w, h, facecolor=color, **BOX)
    ax.add_patch(p)

def arrow(x1, y1, x2, y2):
    ax.add_patch(FancyArrowPatch((x1, y1), (x2, y2), **ARR))

def txt(x, y, s, fd):
    ax.text(x, y, s, ha='center', va='center', fontdict=fd)

# Center y for all boxes
CY = 1.1

# ── 1. Seed Text ──
x1, w1, h1 = 0.5, 1.1, 0.85
box(x1, CY, w1, h1, C['seed'])
txt(x1, CY + 0.12, 'Seed Text', F_TITLE)
txt(x1, CY - 0.16, '(C4, 256 tok)', F_TINY)

# Arrow →
arrow(x1 + w1/2 + 0.06, CY, 1.7, CY)

# ── 2. Recursive Generation ──
x2, w2, h2 = 2.85, 1.9, 1.35
box(x2, CY, w2, h2, C['gen'])
txt(x2, CY + 0.35, 'Recursive', F_TITLE)
txt(x2, CY + 0.12, 'Generation', F_TITLE)
txt(x2, CY - 0.12, r'$G_\delta$ = LLM + $\delta$', {**F_BODY, 'style': 'italic'})
txt(x2, CY - 0.35, r'$X \!\to\! Y_1 \!\to\! \cdots \!\to\! Y_K$', F_MATH)

# Loop arrow above box
lx = x2
ly_top = CY + h2/2 + 0.04
loop = FancyArrowPatch((lx - 0.35, ly_top), (lx + 0.35, ly_top),
                       arrowstyle='->', color='#666666', lw=0.8,
                       connectionstyle='arc3,rad=-0.75', mutation_scale=9)
ax.add_patch(loop)
txt(lx, ly_top + 0.22, 'depth 0→K', {**F_TINY, 'color': '#555555'})

# Arrow →
arrow(x2 + w2/2 + 0.06, CY, 4.55, CY)

# ── 3. 15D Feature Extraction ──
x3, w3, h3 = 5.55, 1.7, 1.75
box(x3, CY, w3, h3, C['feat'])
txt(x3, CY + 0.58, '15D Feature', F_TITLE)
txt(x3, CY + 0.36, 'Extraction', F_TITLE)
feats = ['Surprisal moments', 'Surprisal derivatives',
         'Vocab diversity', 'Frequency tail']
for i, f in enumerate(feats):
    txt(x3, CY + 0.08 - i * 0.21, f'· {f}', F_TINY)

# Arrow →
arrow(x3 + w3/2 + 0.06, CY, 7.15, CY)

# ── 4. OBD-LightGBM ──
x4, w4, h4 = 8.05, 1.5, 1.35
box(x4, CY, w4, h4, C['cls'])
txt(x4, CY + 0.33, 'OBD', F_TITLE)
txt(x4, CY + 0.12, 'LightGBM', F_TITLE)
txt(x4, CY - 0.12, r'$K$ binary classifiers', F_TINY)
txt(x4, CY - 0.33, r'$P(\mathrm{depth} > k)$', F_MATH)

# Arrow →
arrow(x4 + w4/2 + 0.06, CY, 9.35, CY)

# ── 5. Output ──
x5, w5, h5 = 9.95, 0.9, 1.0
box(x5, CY, w5, h5, C['out'])
txt(x5, CY + 0.18, r'$\hat{d}$', {'family': 'serif', 'size': 11, 'weight': 'bold'})
txt(x5, CY - 0.2, r'$K^*$', {'family': 'serif', 'size': 9})

# ── Save ──
out = '/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/figures/pipeline.pdf'
fig.savefig(out, format='pdf', bbox_inches='tight', dpi=300, pad_inches=0.04)
fig.savefig(out.replace('.pdf', '.png'), format='png', bbox_inches='tight', dpi=300, pad_inches=0.04)
plt.close()
print(f'Saved: {out}')
print(f'Saved: {out.replace(".pdf", ".png")}')
