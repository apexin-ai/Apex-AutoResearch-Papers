#!/usr/bin/env python3
"""Fig 4: Causal mechanism diagram — CIVO pathway (A) + non-CIVO pathway (B).
Both require trained dt_embedding; only Pathway A requires dt>1 imagination.
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib.patheffects as path_effects
import numpy as np
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from fig_style import apply_style
apply_style()

fig, ax = plt.subplots(figsize=(10, 5.5))
ax.set_xlim(-0.5, 10.5)
ax.set_ylim(-1.0, 5.5)
ax.axis('off')

def draw_box(ax, x, y, w, h, text, facecolor='#FDFEFE', edgecolor='#2C3E50',
             fontsize=9, fontweight='normal', text_color='#2C3E50', lw=1.5,
             style='round,pad=0.08'):
    rect = mpatches.FancyBboxPatch(
        (x, y), w, h, boxstyle=style,
        facecolor=facecolor, edgecolor=edgecolor, linewidth=lw, zorder=2)
    ax.add_patch(rect)
    ax.text(x + w/2, y + h/2, text, ha='center', va='center',
            fontsize=fontsize, fontweight=fontweight, color=text_color,
            zorder=3, multialignment='center')
    return (x, y, w, h)

def arrow(ax, x1, y1, x2, y2, color='#2C3E50', lw=1.5, style='-',
          connectionstyle='arc3,rad=0', label='', label_pos=0.5,
          label_offset=(0, 0.15), head_width=0.15):
    ax.annotate('', xy=(x2, y2), xytext=(x1, y1),
                arrowprops=dict(arrowstyle=f'->,head_width={head_width}',
                                color=color, lw=lw, linestyle=style,
                                connectionstyle=connectionstyle),
                zorder=1)
    if label:
        mx = x1 + (x2 - x1) * label_pos + label_offset[0]
        my = y1 + (y2 - y1) * label_pos + label_offset[1]
        txt = ax.text(mx, my, label, ha='center', va='center',
                      fontsize=8, color=color, style='italic', zorder=4)
        txt.set_path_effects([
            path_effects.withStroke(linewidth=2.5, foreground='white')])

# === ROOT CAUSE (shared) ===
draw_box(ax, 0.2, 3.4, 2.0, 0.8,
         'Trained\ndt_embedding',
         facecolor='#FDE8D0', edgecolor='#D55E00',
         fontsize=10, fontweight='bold', text_color='#D55E00')

# === PATHWAY A: CIVO (top) ===
ax.text(5.0, 5.2, 'Pathway A: CIVO (value-driven)',
        ha='center', va='center', fontsize=11, fontweight='bold',
        color='#D55E00')

draw_box(ax, 2.8, 4.0, 1.8, 0.7,
         'RSSM dt>1\npredictions\n(low fidelity)',
         facecolor='#FEF9E7', edgecolor='#D55E00', fontsize=8.5)

draw_box(ax, 5.2, 4.0, 1.8, 0.7,
         'Reward head\nsystematic bias\n(1.63× gap)',
         facecolor='#FEF9E7', edgecolor='#D55E00', fontsize=8.5)

draw_box(ax, 7.6, 4.0, 1.8, 0.7,
         'Critic value\noverestimation\n(nve > 2.0×)',
         facecolor='#FDE8D0', edgecolor='#D55E00', fontsize=8.5,
         fontweight='bold')

# Pathway A outcome
draw_box(ax, 7.6, 2.8, 1.8, 0.7,
         'Actor exploits\noverestimated\nvalues',
         facecolor='#FEF9E7', edgecolor='#D55E00', fontsize=8.5)

# Pathway A arrows
arrow(ax, 2.2, 3.8, 2.8, 4.35, color='#D55E00')
arrow(ax, 4.6, 4.35, 5.2, 4.35, color='#D55E00')
arrow(ax, 7.0, 4.35, 7.6, 4.35, color='#D55E00')
arrow(ax, 8.5, 4.0, 8.5, 3.5, color='#D55E00')

# === PATHWAY B: Non-CIVO (bottom) ===
ax.text(5.0, 0.7, 'Pathway B: Non-CIVO (eval-driven)',
        ha='center', va='center', fontsize=11, fontweight='bold',
        color='#0072B2')

draw_box(ax, 2.8, 1.2, 1.8, 0.7,
         'Policy\ninstability\n(entropy ↑)',
         facecolor='#EBF5FB', edgecolor='#0072B2', fontsize=8.5)

draw_box(ax, 5.2, 1.2, 1.8, 0.7,
         'Eval crash\n(value stable,\nnve normal)',
         facecolor='#EBF5FB', edgecolor='#0072B2', fontsize=8.5)

draw_box(ax, 7.6, 1.2, 1.8, 0.7,
         'Late nve spike\n(consequence,\nnot cause)',
         facecolor='#EBF5FB', edgecolor='#0072B2', fontsize=8.5)

# Pathway B arrows
arrow(ax, 2.2, 3.4, 2.8, 1.55, color='#0072B2', style='--',
      connectionstyle='arc3,rad=-0.15')
arrow(ax, 4.6, 1.55, 5.2, 1.55, color='#0072B2', style='--')
arrow(ax, 7.0, 1.55, 7.6, 1.55, color='#0072B2', style='--')

# === SHARED OUTCOME ===
draw_box(ax, 4.0, -0.5, 3.0, 0.7,
         'Performance Collapse\n(stochastic: 3/5 CIVO seeds)',
         facecolor='#FDE8D0', edgecolor='#D55E00',
         fontsize=10, fontweight='bold', text_color='#D55E00', lw=2)

# Arrows to collapse
arrow(ax, 8.5, 2.8, 6.5, 0.2, color='#D55E00',
      connectionstyle='arc3,rad=0.2',
      label='Pathway A\n(008d s1)', label_offset=(0.4, 0.1))
arrow(ax, 8.5, 1.2, 6.8, 0.2, color='#0072B2', style='--',
      connectionstyle='arc3,rad=-0.15',
      label='Pathway B\n(008e_v3 s0)', label_offset=(0.4, -0.1))

# === SELF-CORRECTION annotation ===
draw_box(ax, 0.0, 1.2, 2.2, 0.7,
         'Self-correction\n(009e s1: nve\n4.12× → 1.57×)',
         facecolor='#D6EAF8', edgecolor='#56B4E9', fontsize=8.5,
         text_color='#0072B2')
arrow(ax, 8.5, 3.15, 2.2, 1.55, color='#56B4E9', style=':',
      connectionstyle='arc3,rad=0.35',
      label='1/3 seeds\nself-correct', label_pos=0.4, label_offset=(0, 0.2))

# === KEY annotation ===
ax.text(0.0, 0.3, 'Key:', fontsize=9, fontweight='bold', color='#555')
ax.plot([0.4, 0.9], [0.0, 0.0], '-', color='#D55E00', lw=1.5)
ax.text(1.0, 0.0, 'Pathway A (CIVO)', fontsize=8, va='center', color='#D55E00')
ax.plot([0.4, 0.9], [-0.3, -0.3], '--', color='#0072B2', lw=1.5)
ax.text(1.0, -0.3, 'Pathway B (non-CIVO)', fontsize=8, va='center', color='#0072B2')
ax.plot([0.4, 0.9], [-0.6, -0.6], ':', color='#56B4E9', lw=1.5)
ax.text(1.0, -0.6, 'Self-correction', fontsize=8, va='center', color='#56B4E9')

outdir = '/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/figures/paper'
plt.savefig(f'{outdir}/fig4_mechanism_diagram.pdf')
plt.savefig(f'{outdir}/fig4_mechanism_diagram.png')
plt.close()
print('Saved fig4_mechanism_diagram.pdf and .png')
