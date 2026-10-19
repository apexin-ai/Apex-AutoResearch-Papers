#!/usr/bin/env python3
"""Fig 2: Negative Mining Strategies — 3-panel comparison for StructFuse paper.

Each panel shows the same mini-repo file graph in 2D embedding space.
Only the negative selection (highlighted nodes) differs across panels,
illustrating how each strategy picks negatives.
"""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch
from matplotlib.lines import Line2D
import numpy as np
from pathlib import Path

# ── Style (consistent with Fig 1 / Fig 4) ───────────────────────────────────
plt.rcParams.update({
    'font.family': 'serif',
    'font.serif': ['Times New Roman', 'Times', 'DejaVu Serif'],
    'font.size': 8,
    'figure.dpi': 300,
    'axes.linewidth': 0.6,
    'savefig.bbox': 'tight',
    'savefig.pad_inches': 0.08,
})

# Okabe-Ito palette (consistent across all figures)
C_RAND   = '#E69F00'   # orange — random strategy
C_EMBED  = '#0072B2'   # blue   — embedding-distance strategy
C_DFAW   = '#009E73'   # green  — dataflow-aware strategy
C_POS    = '#CC79A7'   # pink   — positive / gold file
C_GRAY   = '#E5E5E5'
C_GRAY_E = '#CCCCCC'
C_QUERY  = '#333333'
C_SUB    = '#777777'
C_EDGE   = '#AAAAAA'
C_EDGE_H = '#777777'
C_EXCL   = '#CC4444'

# ── Node Layout ──────────────────────────────────────────────────────────────
# 10 nodes: 1 query + 9 files.  Distance from Q ≈ pretrained cosine similarity.
#
# Structural graph G edges: P–a, P–i  →  reachable from gold {P}: {a, i}
# Disconnected from gold:  {c, d, e, f, g, h}

nodes = {
    'Q':  (0.28, 0.47),
    'P':  (0.40, 0.67),
    'd':  (0.44, 0.42),   # closest non-gold, disconnected
    'i':  (0.17, 0.68),   # close, CONNECTED to P
    'a':  (0.47, 0.26),   # close, CONNECTED to P
    'c':  (0.44, 0.83),   # close, disconnected
    'e':  (0.64, 0.69),   # medium, disconnected
    'h':  (0.77, 0.48),   # medium-far, disconnected
    'f':  (0.11, 0.15),   # far, disconnected
    'g':  (0.85, 0.22),   # far, disconnected
}

struct_edges = [('P', 'a'), ('P', 'i')]
reachable = {'a', 'i'}

neg_sel = {
    'random':   {'f', 'g', 'h'},     # scattered, far → easy negatives
    'embed':    {'d', 'i', 'a'},     # top-3 closest non-gold → hard (i,a connected)
    'dataflow': {'d', 'c', 'e'},     # top-3 closest AMONG disconnected
}

NODE_R = 0.028


def _edge(ax, n1, n2, color, lw=0.8):
    (x1, y1), (x2, y2) = nodes[n1], nodes[n2]
    dx, dy = x2 - x1, y2 - y1
    d = np.hypot(dx, dy)
    s = NODE_R * 1.6
    ax.add_patch(FancyArrowPatch(
        (x1 + dx / d * s, y1 + dy / d * s),
        (x2 - dx / d * s, y2 - dy / d * s),
        arrowstyle='-|>', mutation_scale=7, lw=lw, color=color, zorder=1,
    ))


def _node(ax, x, y, fc, ec, lw=0.6, zorder=2):
    ax.add_patch(plt.Circle((x, y), NODE_R, fc=fc, ec=ec, lw=lw, zorder=zorder))


# ── Figure ───────────────────────────────────────────────────────────────────
fig, axes = plt.subplots(1, 3, figsize=(7.0, 2.9))

panels = [
    ('(a) Random',             C_RAND,  'random',
     'negatives sampled uniformly'),
    ('(b) Embedding-Distance', C_EMBED, 'embed',
     'highest pretrained similarity to $q$'),
    ('(c) Dataflow-Aware',     C_DFAW,  'dataflow',
     'similar to $q$ + structurally disconnected'),
]

for ax, (title, color, key, sub) in zip(axes, panels):
    ax.set_xlim(-0.02, 1.02)
    ax.set_ylim(0.02, 0.98)
    ax.set_aspect('equal')
    ax.axis('off')

    nset = neg_sel[key]
    ec = C_EDGE_H if key == 'dataflow' else C_EDGE
    ew = 1.4 if key == 'dataflow' else 0.9

    # ── structural (dataflow) edges ──────────────────────────────────────
    for s, t in struct_edges:
        _edge(ax, s, t, ec, ew)

    # ── embedding-distance circle (panel b only) ─────────────────────────
    if key == 'embed':
        qx, qy = nodes['Q']
        ax.add_patch(plt.Circle((qx, qy), 0.25, fill=False,
                                ec=C_EMBED, lw=0.6, ls='--', alpha=0.25))
        ax.text(qx + 0.27, qy + 0.01, 'high\nsim$(q,f)$', fontsize=5,
                color=C_EMBED, alpha=0.5, fontstyle='italic',
                ha='left', va='center', linespacing=1.1)

    # ── draw file nodes ──────────────────────────────────────────────────
    for name, (x, y) in nodes.items():
        if name == 'Q':
            ax.plot(x, y, '*', ms=14, color=C_QUERY,
                    mec='white', mew=0.3, zorder=5)
            ax.text(x, y - 0.055, '$q$', fontsize=7.5, ha='center',
                    va='top', color=C_QUERY, fontweight='bold')
        elif name == 'P':
            _node(ax, x, y, '#FDF0F5', C_POS, lw=1.5, zorder=3)
            ax.plot(x, y, 'D', ms=3.5, color=C_POS, zorder=4)
            ax.text(x + 0.045, y + 0.005, '$f^+$', fontsize=7,
                    color=C_POS, ha='left', va='center')
        elif name in nset:
            _node(ax, x, y, color, 'white', lw=0.6, zorder=3)
        else:
            _node(ax, x, y, C_GRAY, C_GRAY_E, lw=0.5)

    # ── exclusion marks (panel c): reachable nodes get ✕ ─────────────────
    if key == 'dataflow':
        for rn in reachable:
            rx, ry = nodes[rn]
            ax.plot(rx, ry, 'X', ms=7, color=C_EXCL, mew=1.2, zorder=6)
        ax.annotate('reachable via $G$',
                    xy=(nodes['a'][0] + 0.01, nodes['a'][1]),
                    xytext=(nodes['a'][0] + 0.14, nodes['a'][1] + 0.04),
                    fontsize=5, color=C_EXCL, fontstyle='italic',
                    ha='left', va='center',
                    arrowprops=dict(arrowstyle='->', color=C_EXCL, lw=0.5))

    # ── title + subtitle ─────────────────────────────────────────────────
    ax.text(0.5, 1.05, title, transform=ax.transAxes, fontsize=8.5,
            fontweight='bold', ha='center', va='bottom')
    ax.text(0.5, -0.06, sub, transform=ax.transAxes, fontsize=5.5,
            ha='center', va='top', color=C_SUB, fontstyle='italic')

# ── Unified Legend ────────────────────────────────────────────────────────────
handles = [
    Line2D([], [], marker='*', ls='None', color='w',
           mfc=C_QUERY, ms=10, label='Query ($q$)'),
    Line2D([], [], marker='D', ls='None', color='w',
           mfc=C_POS, ms=5, label='Positive ($f^+$)'),
    Line2D([], [], marker='o', ls='None', color='w',
           mfc='#999999', ms=6, label='Selected $f^-$'),
    Line2D([], [], marker='o', ls='None', color='w',
           mfc=C_GRAY, mec=C_GRAY_E, ms=6, label='Candidate file'),
    Line2D([], [], marker='>', color=C_EDGE_H, lw=1.0,
           ms=4, label='Dataflow edge'),
    Line2D([], [], marker='X', ls='None', color=C_EXCL,
           mew=1.0, ms=5, label='Excluded (reachable)'),
]
fig.legend(handles=handles, loc='lower center', ncol=6,
           frameon=True, fancybox=False, edgecolor='#cccccc', framealpha=0.95,
           fontsize=6.5, bbox_to_anchor=(0.5, 0.005),
           handletextpad=0.3, columnspacing=1.0)

plt.tight_layout(rect=[0, 0.11, 1, 0.96], w_pad=0.5)

# ── Save ─────────────────────────────────────────────────────────────────────
out_dir = Path(__file__).parent
fig.savefig(out_dir / 'fig2_mining_strategies.pdf', format='pdf')
fig.savefig(out_dir / 'fig2_mining_strategies.png', format='png', dpi=300)
plt.close(fig)
print(f"Saved: {out_dir / 'fig2_mining_strategies.pdf'}")
print(f"Saved: {out_dir / 'fig2_mining_strategies.png'}")
