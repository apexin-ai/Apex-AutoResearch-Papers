"""Draw Figure 1: pipeline overview for the generational depth estimation paper."""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
import numpy as np
import os

fig, ax = plt.subplots(1, 1, figsize=(14, 3.2))
ax.set_xlim(-0.5, 14.8)
ax.set_ylim(-0.5, 3.5)
ax.axis('off')

colors = {
    'seed': '#D6DCE4',
    'gen': '#FFF2CC',
    'feat': '#D5F5E3',
    'obd': '#E8DAEF',
    'out': '#FADBD8',
}

box_style = "round,pad=0.15"
box_h = 1.6
box_y = 0.0

boxes = [
    {'x': 0.0, 'w': 1.8, 'color': colors['seed'],
     'title': 'Seed Text', 'sub': '(C4, 256 tok)'},
    {'x': 2.8, 'w': 2.4, 'color': colors['gen'],
     'title': 'Recursive\nGeneration', 'sub': '$G_\\delta = \\mathrm{LLM} + \\delta$\n$X{\\to}Y_1{\\to}{\\cdots}{\\to}Y_K$'},
    {'x': 6.2, 'w': 2.6, 'color': colors['feat'],
     'title': '15D Feature\nExtraction',
     'sub': '· Surprisal moments\n· Surprisal derivatives\n· Vocab diversity\n· Frequency tail'},
    {'x': 9.8, 'w': 2.2, 'color': colors['obd'],
     'title': 'OBD\nLightGBM', 'sub': '$K$ binary classifiers\n$P(\\mathrm{depth} > k)$'},
    {'x': 12.6, 'w': 1.6, 'color': colors['out'],
     'title': 'Output', 'sub': 'Depth $\\hat{d}$\n$K^*_{\\mathrm{empirical}}$'},
]

for b in boxes:
    rect = FancyBboxPatch(
        (b['x'], box_y), b['w'], box_h,
        boxstyle=box_style, linewidth=1.2,
        edgecolor='#888888', facecolor=b['color'],
        zorder=2
    )
    ax.add_patch(rect)

    cx = b['x'] + b['w'] / 2
    if b['sub']:
        title_y = box_y + box_h * 0.72
        sub_y = box_y + box_h * 0.28
        ax.text(cx, title_y, b['title'],
                ha='center', va='center', fontsize=12, fontweight='bold',
                fontfamily='serif', zorder=3)
        ax.text(cx, sub_y, b['sub'],
                ha='center', va='center', fontsize=8.5,
                fontfamily='serif', fontstyle='italic', zorder=3,
                linespacing=1.3)
    else:
        ax.text(cx, box_y + box_h / 2, b['title'],
                ha='center', va='center', fontsize=14, fontweight='bold',
                fontfamily='serif', zorder=3)

arrow_props = dict(
    arrowstyle='->', color='#555555',
    lw=1.8, connectionstyle='arc3,rad=0',
    mutation_scale=15, zorder=1
)
arrow_pairs = [
    (0.0 + 1.8, 2.8),
    (2.8 + 2.4, 6.2),
    (6.2 + 2.6, 9.8),
    (9.8 + 2.2, 12.6),
]
arrow_y = box_y + box_h / 2
for x1, x2 in arrow_pairs:
    ax.annotate('', xy=(x2, arrow_y), xytext=(x1, arrow_y),
                arrowprops=arrow_props)

loop_cx = 2.8 + 2.4 / 2
loop_base = box_y + box_h + 0.08
from matplotlib.patches import Arc
arc_w, arc_h = 2.0, 1.2
arc = Arc((loop_cx, loop_base), arc_w, arc_h, angle=0,
          theta1=10, theta2=170, color='#555555', lw=2.0, zorder=3)
ax.add_patch(arc)
import math
theta_end = math.radians(170)
ax_tip = loop_cx + (arc_w / 2) * math.cos(theta_end)
ay_tip = loop_base + (arc_h / 2) * math.sin(theta_end)
theta_pre = math.radians(165)
ax_pre = loop_cx + (arc_w / 2) * math.cos(theta_pre)
ay_pre = loop_base + (arc_h / 2) * math.sin(theta_pre)
ax.annotate('', xy=(ax_tip, ay_tip), xytext=(ax_pre, ay_pre),
            arrowprops=dict(arrowstyle='->', color='#555555', lw=2.0,
                            mutation_scale=16), zorder=3)
ax.text(loop_cx, loop_base + arc_h / 2 + 0.18, 'depth $0{\\to}K$',
        ha='center', va='bottom', fontsize=10, fontweight='bold',
        fontfamily='serif', fontstyle='italic', color='#444444', zorder=3)

plt.subplots_adjust(top=0.95)

out_dir = os.path.dirname(os.path.abspath(__file__))
paper_fig_dir = os.path.join(os.path.dirname(out_dir), 'docs', 'paper', 'figures')
os.makedirs(paper_fig_dir, exist_ok=True)

pdf_path = os.path.join(paper_fig_dir, 'pipeline.pdf')
png_path = os.path.join(paper_fig_dir, 'pipeline.png')
fig.savefig(pdf_path, bbox_inches='tight', dpi=300, pad_inches=0.2)
fig.savefig(png_path, bbox_inches='tight', dpi=200, pad_inches=0.2)
plt.close()

print(f"PDF: {pdf_path} ({os.path.getsize(pdf_path)} bytes)")
print(f"PNG: {png_path} ({os.path.getsize(png_path)} bytes)")
print("Done.")
