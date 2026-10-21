import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
import os

plt.rcParams.update({
    'font.family': 'DejaVu Sans',
    'font.size': 10,
    'figure.dpi': 300,
    'savefig.dpi': 300,
    'savefig.bbox': 'tight',
    'savefig.pad_inches': 0.1,
})

C_CKA  = '#009E73'
C_RAND = '#E69F00'
C_STD  = '#CC79A7'
C_RASP = '#D55E00'
C_BLUE = '#0072B2'

def light(hx, f=0.82):
    r, g, b = int(hx[1:3],16), int(hx[3:5],16), int(hx[5:7],16)
    return '#{:02x}{:02x}{:02x}'.format(int(r+(255-r)*f), int(g+(255-g)*f), int(b+(255-b)*f))

fig, ax = plt.subplots(figsize=(14, 8))
ax.set_xlim(-0.3, 14.3)
ax.set_ylim(-0.5, 8.3)
ax.axis('off')

def rbox(x, y, w, h, ec='black', fc='white', lw=1.5, pad=0.08):
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle=f'round,pad={pad}',
                                facecolor=fc, edgecolor=ec, linewidth=lw, zorder=2))

def arr(x1, y1, x2, y2, color='#888', lw=1.2, ms=11):
    ax.add_patch(FancyArrowPatch((x1, y1), (x2, y2), arrowstyle='->', color=color,
                                 lw=lw, mutation_scale=ms, zorder=3))

# ── ROW 1: Pretrained LLM → Structural Analysis ──────────────
rbox(0.3, 6.55, 2.8, 1.15, ec=C_BLUE, fc=light(C_BLUE), lw=2)
ax.text(1.7, 7.28, 'Pretrained', fontsize=11, ha='center', va='center',
        fontweight='bold', color=C_BLUE)
ax.text(1.7, 6.95, 'Reasoning LLM', fontsize=10, ha='center', va='center', color=C_BLUE)

arr(3.1, 7.12, 4.15, 7.12, color=C_BLUE, lw=2, ms=14)

rbox(4.3, 6.15, 9.3, 1.55, ec='#555', fc='#FAFAFA', lw=2, pad=0.12)
ax.text(8.95, 7.4, 'Structural Analysis  (shared by all methods)', fontsize=11,
        ha='center', va='center', fontweight='bold', color='#333')

rbox(4.75, 6.35, 3.7, 0.75, ec='#bbb', fc='#FFF8F0', lw=1)
ax.text(6.6, 6.88, 'Taylor Importance', fontsize=9, ha='center', va='center', fontweight='bold')
ax.text(6.6, 6.55, r'$I(h) = |a_h \cdot \nabla_{a_h}\mathcal{L}|$', fontsize=9,
        ha='center', va='center')

rbox(8.9, 6.35, 4.2, 0.75, ec='#bbb', fc='#F0FFF8', lw=1)
ax.text(11.0, 6.88, 'CKA Overlap', fontsize=9, ha='center', va='center', fontweight='bold')
ax.text(11.0, 6.55, r'$F(h) = \mathrm{CKA}(h,\, h\!+\!1)$', fontsize=9,
        ha='center', va='center')

# ── ROW 2: 4 Scoring Criteria ────────────────────────────────
methods = [
    ('CKA-only', C_CKA,  r'Remove highest $F(h)$',
     'Preserves unique\nrepresentations', False),
    ('Random',   C_RAND, 'Uniform random',
     'No selection bias', False),
    ('Standard', C_STD,  r'Remove lowest $I(h)$',
     'Removes "unimportant"\nstructures', True),
    ('RASP',     C_RASP, r'$S = I(h)\!\cdot\!(1\!-\!F(h))^\alpha$',
     'Removes redundant\n+ unimportant', True),
]

bw, bh = 2.9, 1.65
bg = (13.0 - 4*bw) / 3
by = 3.85
xcs = []

for i, (name, col, formula, prop, warn) in enumerate(methods):
    x = 0.5 + i*(bw+bg)
    xc = x + bw/2
    xcs.append(xc)

    rbox(x, by, bw, bh, ec=col, fc=light(col), lw=2)
    ax.text(xc, by+bh-0.28, name, fontsize=11, ha='center', va='center',
            fontweight='bold', color=col)
    ax.text(xc, by+bh-0.72, formula, fontsize=9, ha='center', va='center', color='#333')
    ax.plot([x+0.25, x+bw-0.25], [by+bh-1.0, by+bh-1.0],
            color=col, alpha=0.3, lw=0.8, zorder=3)
    ax.text(xc, by+0.35, prop, fontsize=8, ha='center', va='center',
            color='#555', style='italic')

    if warn:
        ax.text(x+bw-0.12, by+bh-0.08, r'$\triangle\!$ I(h)', fontsize=6.5,
                ha='right', va='top', color='#CC0000', fontweight='bold')

    arr(xc, 6.15, xc, by+bh+0.12, color='#aaa', lw=1.0, ms=9)

# ── Recovery Pipeline ─────────────────────────────────────────
py, ph = 2.7, 0.6
rbox(0.5, py, 13.0, ph, ec='#777', fc='#F0F0F0', lw=1.5)
ax.text(7.0, py+ph/2, 'Identical Recovery:   SFT Warmup  →  GRPO RL Alignment',
        fontsize=11, ha='center', va='center', fontweight='bold', color='#555')

for xc in xcs:
    arr(xc, by, xc, py+ph+0.1, color='#aaa', lw=1.0, ms=9)

# ── ROW 3: Divergent Outcomes ─────────────────────────────────
outcomes = [
    ('Active\nLearning',    C_CKA,  'reward 0.354',  'frac_zero 0.125', 2.5),
    ('Stagnation',          C_RAND, 'reward ≈0.17', 'flat trajectory', 1.8),
    ('Collapse',            C_STD,  'reward →0',    'grad vanishing',  1.2),
    ('Immediate\nCollapse', C_RASP, 'reward ≈0.01', '85% max-len',     0.8),
]

oy, oh, ow = 0.4, 1.7, bw

for i, (name, col, l1, l2, alw) in enumerate(outcomes):
    x = 0.5 + i*(ow+bg)
    xc = xcs[i]

    arr(xc, py, xc, oy+oh+0.1, color=col, lw=alw, ms=12)
    rbox(x, oy, ow, oh, ec=col, fc=light(col), lw=2)
    ax.text(xc, oy+oh-0.42, name, fontsize=10, ha='center', va='center',
            fontweight='bold', color=col)
    ax.text(xc, oy+0.52, l1, fontsize=8.5, ha='center', va='center',
            color='#444', family='monospace')
    ax.text(xc, oy+0.22, l2, fontsize=8, ha='center', va='center',
            color='#666', family='monospace')

# ── Recovery Capacity Gradient (horizontal bar below outcomes) ─
import numpy as np
from matplotlib.colors import LinearSegmentedColormap
grad_y = 0.0
grad_h = 0.15
x_left = 0.5 + bw/2
x_right = 0.5 + 3*(bw+bg) + bw/2
grad_img = np.linspace(0, 1, 256).reshape(1, -1)
cmap = LinearSegmentedColormap.from_list('rc', [C_CKA, C_RAND, C_STD, C_RASP])
ax.imshow(grad_img, aspect='auto', cmap=cmap, alpha=0.7,
          extent=[x_left, x_right, grad_y - grad_h, grad_y + grad_h], zorder=2)
ax.text((x_left+x_right)/2, grad_y - 0.28, 'Recovery Capacity',
        fontsize=9, ha='center', va='top', color='#444', fontweight='bold')
ax.text(x_left - 0.1, grad_y, 'High', fontsize=8, ha='right', va='center',
        color=C_CKA, fontweight='bold')
ax.text(x_right + 0.1, grad_y, 'None', fontsize=8, ha='left', va='center',
        color=C_RASP, fontweight='bold')

plt.tight_layout()

outdir = '/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/artifacts/figures'
fig.savefig(f'{outdir}/fig1_framework.pdf')
fig.savefig(f'{outdir}/fig1_framework.png')
plt.close()

for ext in ['pdf', 'png']:
    p = f'{outdir}/fig1_framework.{ext}'
    print(f'{p}: {os.path.getsize(p)} bytes')
print('Done')
