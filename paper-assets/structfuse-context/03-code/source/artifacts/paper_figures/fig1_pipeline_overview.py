#!/usr/bin/env python3
"""Fig 1: StructFuse Pipeline Overview — from input to fine-tuned retriever."""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Rectangle
from pathlib import Path

# ── Style ────────────────────────────────────────────────────────────────────
plt.rcParams.update({
    'font.family': 'serif',
    'font.serif': ['Times New Roman', 'Times', 'DejaVu Serif'],
    'font.size': 8,
    'figure.dpi': 300,
    'savefig.bbox': 'tight',
    'savefig.pad_inches': 0.08,
})

# Okabe-Ito palette (consistent with Fig 4)
C_RANDOM = '#E69F00'
C_EMBED  = '#0072B2'
C_DFAW   = '#009E73'
C_BG     = '#F7F7F7'
C_BORDER = '#999999'
C_ARROW  = '#555555'
C_TEXT   = '#333333'
C_SUB    = '#777777'
C_NOTE   = '#AAAAAA'

fig, ax = plt.subplots(figsize=(7.0, 2.8))
ax.set_xlim(-0.2, 10.2)
ax.set_ylim(-0.2, 4.2)
ax.axis('off')

# ── Helpers ──────────────────────────────────────────────────────────────────

def rbox(cx, cy, w, h, fc=C_BG, ec=C_BORDER, lw=0.8, ls='-', alpha=1.0, zorder=2, pad=0.1):
    p = FancyBboxPatch((cx - w/2, cy - h/2), w, h,
                        boxstyle=f'round,pad={pad}',
                        facecolor=fc, edgecolor=ec,
                        linewidth=lw, linestyle=ls, alpha=alpha, zorder=zorder)
    ax.add_patch(p)
    return p

def arr(x1, y1, x2, y2, c=C_ARROW, lw=1.0, rad=0):
    a = FancyArrowPatch((x1, y1), (x2, y2),
                         arrowstyle='-|>', mutation_scale=8, lw=lw, color=c,
                         connectionstyle=f'arc3,rad={rad}', zorder=3)
    ax.add_patch(a)

def txt(x, y, s, fs=8, c=C_TEXT, fw='normal', ha='center', va='center', **kw):
    ax.text(x, y, s, fontsize=fs, color=c, fontweight=fw, ha=ha, va=va, zorder=5, **kw)

# ── Coordinates ──────────────────────────────────────────────────────────────
y0 = 2.0

x_in  = 0.65;  w_in  = 1.0
x_cq  = 2.45;  w_cq  = 1.35
x_mn  = 5.0;   w_mn  = 1.75
x_tr  = 7.6;   w_tr  = 1.35
x_out = 9.45;  w_out = 1.0

bh = 1.05
dy = 0.72
sh = 0.42
am = 0.15

y_r = y0 + dy
y_e = y0
y_d = y0 - dy

# ── Block 1: Input ───────────────────────────────────────────────────────────
rbox(x_in, y0, w_in, bh)
txt(x_in, y0 + 0.17, 'Repository', fs=7.5, fw='bold')
txt(x_in, y0 - 0.17, '+ Bug Report', fs=6.5, c=C_SUB)

# ── Block 2: CodeQL Extraction ───────────────────────────────────────────────
rbox(x_cq, y0, w_cq, bh)
txt(x_cq, y0 + 0.25, 'CodeQL', fs=9, fw='bold')
txt(x_cq, y0 - 0.05, 'Scope-bounded', fs=6, c=C_SUB)
txt(x_cq, y0 - 0.28, 'data-flow analysis', fs=6, c=C_SUB)

txt(x_cq, y0 - bh/2 - 0.25, 'Structural Graph G', fs=6.5, c=C_NOTE, fontstyle='italic')
txt(x_cq, y0 - bh/2 - 0.50, '(drift-immune)', fs=5.5, c=C_NOTE, fontstyle='italic')

# ── Block 3: Negative Mining ─────────────────────────────────────────────────
container_h = 2 * dy + sh + 0.55
rbox(x_mn, y0, w_mn + 0.3, container_h,
     fc='white', ec='#BBBBBB', lw=0.6, ls=(0, (4, 3)), alpha=0.4, zorder=1)
txt(x_mn, y0 + container_h/2 - 0.15, 'Negative Mining', fs=8, fw='bold', c=C_SUB)

strats = [
    ('Random',              C_RANDOM, y_r),
    ('Embedding-distance',  C_EMBED,  y_e),
    ('Dataflow-aware',      C_DFAW,   y_d),
]
for name, color, sy in strats:
    rbox(x_mn, sy, w_mn, sh, fc=color, ec=color, alpha=0.12, pad=0.06)
    accent = Rectangle((x_mn - w_mn/2 + 0.02, sy - sh/2 + 0.04), 0.06, sh - 0.08,
                         facecolor=color, edgecolor='none', alpha=0.8, zorder=3)
    ax.add_patch(accent)
    txt(x_mn + 0.05, sy, name, fs=7, c=color, fw='semibold')

# ── Block 4: Contrastive Training ────────────────────────────────────────────
rbox(x_tr, y0, w_tr, bh)
txt(x_tr, y0 + 0.22, 'Contrastive', fs=8, fw='bold')
txt(x_tr, y0 - 0.02, 'Training', fs=8, fw='bold')
txt(x_tr, y0 - 0.30, 'InfoNCE + LoRA', fs=6, c=C_SUB)

# ── Block 5: Output ─────────────────────────────────────────────────────────
rbox(x_out, y0, w_out, bh)
txt(x_out, y0 + 0.14, 'Fine-tuned', fs=7.5, fw='bold')
txt(x_out, y0 - 0.14, 'Retriever', fs=7.5, fw='bold')

# ── Arrows ───────────────────────────────────────────────────────────────────
arr(x_in + w_in/2 + am, y0, x_cq - w_cq/2 - am, y0)

x_cq_r = x_cq + w_cq/2 + am
x_mn_l = x_mn - w_mn/2 - am + 0.05
for name, color, sy in strats:
    rad = 0 if sy == y0 else (-0.12 if sy > y0 else 0.12)
    arr(x_cq_r, y0, x_mn_l, sy, c=color, lw=1.1, rad=rad)

x_mn_r = x_mn + w_mn/2 + am - 0.05
x_tr_l = x_tr - w_tr/2 - am
for name, color, sy in strats:
    rad = 0 if sy == y0 else (0.12 if sy > y0 else -0.12)
    arr(x_mn_r, sy, x_tr_l, y0, c=color, lw=1.1, rad=rad)

arr(x_tr + w_tr/2 + am, y0, x_out - w_out/2 - am, y0)

# ── Annotations ──────────────────────────────────────────────────────────────
txt(x_mn, y_d - sh/2 - 0.2, '66% fallback → embedding',
    fs=5.5, c=C_DFAW, fontstyle='italic')

txt(5.0, -0.05, 'Static mining — computed once, no re-mining during training',
    fs=6.5, c='#CCCCCC', fontstyle='italic')

# ── Save ─────────────────────────────────────────────────────────────────────
out_dir = Path(__file__).parent
fig.savefig(out_dir / 'fig1_pipeline_overview.pdf', format='pdf')
fig.savefig(out_dir / 'fig1_pipeline_overview.png', format='png', dpi=300)
plt.close(fig)
print(f"Saved: {out_dir / 'fig1_pipeline_overview.pdf'}")
print(f"Saved: {out_dir / 'fig1_pipeline_overview.png'}")
