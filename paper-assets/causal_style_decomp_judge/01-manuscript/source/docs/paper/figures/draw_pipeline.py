#!/usr/bin/env python3
"""
CSD Pipeline Diagram (Figure 1) — Publication-quality 2-row layout v8.
Column-width (3.35"), height ~1.8". Row 1: stages 1-3, Row 2: stages 4-5.
Both rows centered. Curved connecting arrow.
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
import numpy as np

fig_w, fig_h = 3.35, 1.90
fig, ax = plt.subplots(1, 1, figsize=(fig_w, fig_h), dpi=300)
ax.set_xlim(0, fig_w)
ax.set_ylim(0, fig_h)
ax.axis('off')
fig.patch.set_facecolor('white')
ax.set_facecolor('white')

plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.serif'] = ['Times New Roman', 'DejaVu Serif', 'serif']

pal = {
    'source':  {'bg': '#F7F5F2', 'bdr': '#C8C0B5', 'acc': '#A89880'},
    'gen':     {'bg': '#EDF1F8', 'bdr': '#90A8C5', 'acc': '#5C7FA5'},
    'nli':     {'bg': '#EAF5EA', 'bdr': '#80B580', 'acc': '#4A8A4A'},
    'score':   {'bg': '#EDEBF5', 'bdr': '#A090C5', 'acc': '#7060A5'},
    'analyze': {'bg': '#3A4C5B', 'bdr': '#2D3E4D', 'acc': '#8EAAB8'},
}

rr = 0.04
circ_r = 0.07

# ── Row 1: 3 boxes ──
box_w1 = 0.88
box_h = 0.56
r1_gap = 0.22
r1_total = 3 * box_w1 + 2 * r1_gap
r1_x0 = (fig_w - r1_total) / 2
r1_cy = fig_h - 0.06 - box_h / 2

# ── Row 2: 2 boxes (wider) ──
box_w2 = 1.15
r2_gap = 0.25
r2_total = 2 * box_w2 + r2_gap
r2_x0 = (fig_w - r2_total) / 2
r2_cy = 0.06 + box_h / 2

row1_data = [
    ('source',  '1', 'Source Data',      'LLMBar Nat.+Adv.'),
    ('gen',     '2', 'CF Generation',    'Qwen3-32B'),
    ('nli',     '3', 'NLI Verification', 'DeBERTa ≥ 0.90'),
]
row2_data = [
    ('score',   '4', 'Pairwise Scoring',    'A/B swap × 2 trials'),
    ('analyze', '5', 'Statistical Analysis', 'BT + GEE + Likert'),
]

flow_r1 = ['n=100', '100 pairs']
flow_r2 = ['173 comp.']

def draw_box(x, y_bot, bw, key, num, title, subtitle):
    c = pal[key]
    is_dark = (key == 'analyze')
    cy = y_bot + box_h / 2

    # Shadow
    ax.add_patch(FancyBboxPatch(
        (x + 0.008, y_bot - 0.008), bw, box_h,
        boxstyle=f"round,pad=0,rounding_size={rr}",
        facecolor='#000000', edgecolor='none', alpha=0.04, zorder=1
    ))
    # Box
    ax.add_patch(FancyBboxPatch(
        (x, y_bot), bw, box_h,
        boxstyle=f"round,pad=0,rounding_size={rr}",
        facecolor=c['bg'], edgecolor=c['bdr'],
        linewidth=0.55, zorder=2
    ))
    # Number circle
    ccx, ccy = x + 0.12, cy + 0.11
    ax.add_patch(plt.Circle(
        (ccx, ccy), circ_r,
        facecolor=c['acc'] if not is_dark else '#E0E0E0',
        edgecolor='none', alpha=0.9, zorder=4
    ))
    ax.text(ccx, ccy, num, ha='center', va='center',
            fontsize=6, fontweight='bold',
            color='white' if not is_dark else c['bg'],
            zorder=5, fontfamily='serif')
    # Title
    ax.text(x + bw / 2, cy - 0.02, title, ha='center', va='center',
            fontsize=6.2, fontweight='bold',
            color='#FFFFFF' if is_dark else '#252530',
            zorder=5, fontfamily='serif')
    # Subtitle
    ax.text(x + bw / 2, cy - 0.15, subtitle, ha='center', va='center',
            fontsize=4.8,
            color='#A0B5C2' if is_dark else '#6E6E78',
            zorder=5, fontfamily='serif')
    return x, y_bot

# ── Draw Row 1 ──
r1_pos = []
for j, (key, num, title, sub) in enumerate(row1_data):
    x = r1_x0 + j * (box_w1 + r1_gap)
    yb = r1_cy - box_h / 2
    draw_box(x, yb, box_w1, key, num, title, sub)
    r1_pos.append(x)

# Row 1 arrows
for j in range(2):
    xs = r1_pos[j] + box_w1 + 0.01
    xe = r1_pos[j + 1] - 0.01
    ax.annotate('', xy=(xe, r1_cy), xytext=(xs, r1_cy),
                arrowprops=dict(arrowstyle='-|>', color='#AAAAAA', lw=0.45, mutation_scale=4.5),
                zorder=2)
    mx = (xs + xe) / 2
    ax.text(mx, r1_cy - 0.18, flow_r1[j], ha='center', va='center',
            fontsize=4, fontstyle='italic', color='#A0A0A0',
            zorder=5, fontfamily='serif')

# ── Draw Row 2 ──
r2_pos = []
for j, (key, num, title, sub) in enumerate(row2_data):
    x = r2_x0 + j * (box_w2 + r2_gap)
    yb = r2_cy - box_h / 2
    draw_box(x, yb, box_w2, key, num, title, sub)
    r2_pos.append(x)

# Row 2 arrow
xs2 = r2_pos[0] + box_w2 + 0.01
xe2 = r2_pos[1] - 0.01
ax.annotate('', xy=(xe2, r2_cy), xytext=(xs2, r2_cy),
            arrowprops=dict(arrowstyle='-|>', color='#AAAAAA', lw=0.45, mutation_scale=4.5),
            zorder=2)
mx2 = (xs2 + xe2) / 2
ax.text(mx2, r2_cy - 0.18, flow_r2[0], ha='center', va='center',
        fontsize=4, fontstyle='italic', color='#A0A0A0',
        zorder=5, fontfamily='serif')

# ── Connecting arrow: NLI (row1, rightmost) → Scoring (row2, leftmost) ──
nli_cx = r1_pos[2] + box_w1 / 2
nli_bot = r1_cy - box_h / 2
score_cx = r2_pos[0] + box_w2 / 2
score_top = r2_cy + box_h / 2

mid_y = (nli_bot + score_top) / 2

# Curved arrow from NLI bottom to Scoring top
ax.annotate(
    '', xy=(score_cx, score_top + 0.01), xytext=(nli_cx, nli_bot - 0.01),
    arrowprops=dict(
        arrowstyle='-|>', color='#AAAAAA', lw=0.45, mutation_scale=4.5,
        connectionstyle='arc3,rad=0.25'
    ),
    zorder=2
)

# "88 verified" + "×12 filtered"
ax.text(
    (nli_cx + score_cx) / 2 + 0.22, mid_y,
    '88 verified',
    ha='center', va='center',
    fontsize=4, fontstyle='italic', color='#A0A0A0',
    zorder=5, fontfamily='serif'
)
ax.text(
    (nli_cx + score_cx) / 2 - 0.15, mid_y + 0.06,
    '×12 filtered',
    ha='center', va='center',
    fontsize=3.5, fontstyle='italic', color='#C0392B',
    zorder=5, fontfamily='serif', alpha=0.55
)

plt.subplots_adjust(left=0, right=1, top=1, bottom=0)

out = '/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/figures'
plt.savefig(f'{out}/pipeline_diagram.png', dpi=300, bbox_inches='tight', pad_inches=0.015, facecolor='white')
plt.savefig(f'{out}/pipeline_diagram.pdf', dpi=300, bbox_inches='tight', pad_inches=0.015, facecolor='white')
print("Saved pipeline_diagram v8")
plt.close()
