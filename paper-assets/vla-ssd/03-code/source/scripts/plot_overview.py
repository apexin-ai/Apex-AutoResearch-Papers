import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib.patheffects as pe
import numpy as np
import os, shutil

plt.rcParams.update({
    'font.family': 'serif',
    'font.serif': ['Liberation Serif'],
    'pdf.fonttype': 42,
    'ps.fonttype': 42,
    'mathtext.fontset': 'custom',
    'mathtext.rm': 'Liberation Serif',
    'mathtext.it': 'Liberation Serif:italic',
    'mathtext.bf': 'Liberation Serif:bold',
    'font.size': 10,
    'figure.dpi': 300,
    'savefig.dpi': 300,
    'savefig.bbox': 'tight',
    'savefig.pad_inches': 0.08,
})

# ─── Pastel color palette ───────────────────────────────────
PASTEL = {
    'blue':   '#92C5DE',
    'gold':   '#FDB863',
    'orange': '#F4A582',
    'green':  '#A6DBA0',
    'pink':   '#E7B8D4',
    'cyan':   '#B2E2E2',
}
EDGE = {
    'blue':   '#4393C3',
    'gold':   '#E08214',
    'orange': '#D6604D',
    'green':  '#5AAE61',
    'pink':   '#C2669A',
    'cyan':   '#5AB4AC',
}

PASTEL_BLUE_L  = '#DBE9F4'
PASTEL_GOLD_L  = '#FEF0D9'
PASTEL_ORANGE_L = '#FDEAE3'
PASTEL_GREEN_L = '#E3F5E1'

TXT     = '#2B2B2B'
TXT2    = '#666666'
TXT3    = '#999999'
LN      = '#888888'

# ─── Figure (compact) ──────────────────────────────────────
fig = plt.figure(figsize=(10, 3.2), facecolor='white')

ax_a = fig.add_axes([0.01, 0.04, 0.28, 0.88])
ax_b = fig.add_axes([0.31, 0.04, 0.38, 0.88])
ax_c = fig.add_axes([0.71, 0.04, 0.28, 0.88])

for ax in [ax_a, ax_b, ax_c]:
    ax.axis('off')

# ─── Helpers ─────────────────────────────────────────────────
def rbox(ax, cx, cy, w, h, label='', fc='white', ec='#CCC',
         fontsize=9, fontweight='normal', tc=TXT,
         lw=0.7, ls='-', zorder=3, fontstyle='normal',
         shadow=False, radius=0.12, label_lines=None):
    if shadow:
        for dx, dy, sa in [(0.12, -0.12, 0.15), (0.06, -0.06, 0.10)]:
            sp = mpatches.FancyBboxPatch(
                (cx - w/2 + dx, cy - h/2 + dy), w, h,
                boxstyle=f'round,pad={radius}',
                facecolor='#B0B0B0', edgecolor='none', linewidth=0,
                alpha=sa, zorder=zorder - 1)
            ax.add_patch(sp)
    b = mpatches.FancyBboxPatch(
        (cx - w/2, cy - h/2), w, h,
        boxstyle=f'round,pad={radius}',
        facecolor=fc, edgecolor=ec, linewidth=lw,
        linestyle=ls, zorder=zorder)
    ax.add_patch(b)
    if label:
        ax.text(cx, cy, label, ha='center', va='center',
                fontsize=fontsize, color=tc, fontweight=fontweight,
                fontstyle=fontstyle, zorder=zorder + 1)

def farrow(ax, x1, y1, x2, y2, color=LN, lw=0.8, ms=10,
           style='->', conn=None, ls='-'):
    props = dict(arrowstyle=style, color=color, lw=lw, mutation_scale=ms,
                 linestyle=ls)
    if conn:
        props['connectionstyle'] = conn
    ax.annotate('', xy=(x2, y2), xytext=(x1, y1), arrowprops=props)

def num_circle(ax, x, y, num, color, ec_color=None, size=0.35):
    if ec_color is None:
        ec_color = 'white'
    circle = mpatches.Circle((x, y), size, facecolor=color,
                              edgecolor=ec_color, linewidth=0.8, zorder=6)
    ax.add_patch(circle)
    ax.text(x, y, str(num), ha='center', va='center',
            fontsize=7.5, color='white', fontweight='bold', zorder=7)

def section_title(ax, x, y, panel_label, subtitle):
    ax.text(x, y, panel_label, fontsize=12, fontweight='bold', va='top',
            color=TXT)
    ax.text(x + 1.5, y - 0.1, subtitle, fontsize=8.5, va='top', color=TXT2)

# ═══════════════════════════════════════════════════════════════
# PANEL (a): VLA sequence structure
# ═══════════════════════════════════════════════════════════════
ax_a.set_xlim(-2, 11)
ax_a.set_ylim(-0.5, 10.5)

section_title(ax_a, -1.5, 10.2, '(a)', 'VLA sequence structure')

CX = 4.5
BW = 7.0
BH = 1.3

# Image tokens — pastel blue
y_img = 8.2
rbox(ax_a, CX, y_img, BW, BH, fc=PASTEL_BLUE_L, ec=EDGE['blue'], ls='--', lw=0.6,
     radius=0.15)
ax_a.text(CX - 1.5, y_img + 0.1, 'Image tokens', fontsize=9,
          ha='center', va='center', color=TXT, fontweight='medium', zorder=4)
for k in range(4):
    px = CX + 0.6 + k * 0.85
    ax_a.add_patch(mpatches.FancyBboxPatch(
        (px - 0.25, y_img - 0.25), 0.5, 0.5,
        boxstyle='round,pad=0.05', facecolor=PASTEL['blue'], alpha=0.5,
        edgecolor=EDGE['blue'], linewidth=0.4, zorder=4))

# Instruction tokens — pastel gold
y_ins = 5.6
rbox(ax_a, CX, y_ins, BW, BH, fc=PASTEL_GOLD_L, ec=EDGE['gold'], ls='--', lw=0.6,
     radius=0.15)
ax_a.text(CX, y_ins + 0.28, 'Instruction tokens', fontsize=9,
          ha='center', va='center', color=TXT, fontweight='medium', zorder=4)
ax_a.text(CX, y_ins - 0.28, 'pick up the red block', fontsize=7.5,
          ha='center', va='center', color=TXT3, fontstyle='italic', zorder=4)

# Readout (R) — pastel orange; Action (Act) — pastel green
y_bot = 3.0
rbox(ax_a, CX - 1.8, y_bot, 2.2, 1.0, 'R', PASTEL['orange'], EDGE['orange'],
     fontsize=12, fontweight='bold', tc='white', lw=0.8, shadow=True,
     radius=0.14)
rbox(ax_a, CX + 1.8, y_bot, 2.2, 1.0, 'Act', PASTEL['green'], EDGE['green'],
     fontsize=11, fontweight='bold', tc='white', lw=0.8, shadow=True,
     radius=0.14)

# Vertical arrows
farrow(ax_a, CX, y_img - BH/2, CX, y_ins + BH/2,
       color=TXT3, lw=0.9, style='-|>', ms=9)
farrow(ax_a, CX - 1.0, y_ins - BH/2, CX - 1.8, y_bot + 0.55,
       color=TXT3, lw=0.9, style='-|>', ms=9)
farrow(ax_a, CX + 1.0, y_ins - BH/2, CX + 1.8, y_bot + 0.55,
       color=TXT3, lw=0.9, style='-|>', ms=9)

# Red X — causal mask constraint
mid_y = (y_img + y_ins) / 2
xx = 9.2
d = 0.25
ax_a.plot([xx - d, xx + d], [mid_y - d, mid_y + d],
          color='#CC0000', lw=2.0, zorder=5, solid_capstyle='round')
ax_a.plot([xx - d, xx + d], [mid_y + d, mid_y - d],
          color='#CC0000', lw=2.0, zorder=5, solid_capstyle='round')
ax_a.text(xx, mid_y - 0.55, 'cannot attend\nto instruction', fontsize=6.5,
          ha='center', va='top', color='#CC0000', linespacing=1.3)

# Arc arrow: image → readout
farrow(ax_a, CX - BW/2 - 0.2, y_img,
       CX - 1.8 - 1.1, y_bot + 0.2,
       color=EDGE['blue'], lw=1.0, conn='arc3,rad=0.45', style='-|>', ms=10)
ax_a.text(-0.8, (y_img + y_bot) / 2 - 0.3, 'attends to\nall context',
          fontsize=7, ha='center', va='center', color=EDGE['blue'],
          fontstyle='italic', linespacing=1.3)

# Position labels
ax_a.text(CX, y_img - BH/2 - 0.15, 'image_mean', fontsize=7,
          ha='center', va='top', color=TXT2, fontstyle='italic')
ax_a.text(CX - 1.8, y_bot - 0.6, 'readout', fontsize=7,
          ha='center', va='top', color=TXT2, fontstyle='italic')

# ═══════════════════════════════════════════════════════════════
# PANEL (b): Three analysis methods
# ═══════════════════════════════════════════════════════════════
ax_b.set_xlim(-0.5, 14)
ax_b.set_ylim(-0.5, 10.5)

section_title(ax_b, -0.3, 10.2, '(b)', 'Three analysis methods')

# ── Method 1: Layer-wise action probes ────────────────────────
num_circle(ax_b, -0.1, 8.95, '1', EDGE['blue'])
ax_b.text(0.5, 9.0, 'Layer-wise action probes', fontsize=9,
          fontweight='bold', color=TXT)

m1y = 8.0
for i, lbl in enumerate(['L1', 'L2', 'L3']):
    rbox(ax_b, 0.7 + i * 1.1, m1y, 0.8, 0.6, lbl, PASTEL_BLUE_L, EDGE['blue'],
         fontsize=8, radius=0.08)

farrow(ax_b, 3.2, m1y, 4.0, m1y, color=TXT3, style='-|>', ms=8)
rbox(ax_b, 4.8, m1y, 1.5, 0.6, 'Probe', '#F5F5F5', '#BBBBBB',
     fontsize=8, radius=0.08)
farrow(ax_b, 5.55, m1y, 6.3, m1y, color=TXT3, style='-|>', ms=8)
rbox(ax_b, 7.5, m1y, 2.2, 0.6, '7-DoF action', PASTEL_ORANGE_L, EDGE['orange'],
     fontsize=8, radius=0.08)

# R² badge
rbox(ax_b, 9.0, m1y + 0.50, 0.6, 0.45, 'R²', PASTEL_ORANGE_L, EDGE['orange'],
     fontsize=7.5, fontweight='bold', tc=EDGE['orange'], radius=0.1)

# ── Method 2: Counterfactual perturbation ─────────────────────
num_circle(ax_b, -0.1, 6.15, '2', EDGE['blue'])
ax_b.text(0.5, 6.2, 'Counterfactual perturbation', fontsize=9,
          fontweight='bold', color=TXT)

m2y = 5.3
capsules = [
    ('+ correct instr.', PASTEL_GREEN_L, EDGE['green'],  2.5),
    ('- empty',          '#F0F0F0',      '#888888',       1.5),
    ('x wrong',          '#FFEEEE',      '#CC0000',       1.5),
    ('o shuffle',        PASTEL_GOLD_L,  EDGE['gold'],    1.7),
    ('~ paraph.',        '#F3E0ED',      EDGE['pink'],    1.7),
]
x_pos = 0.2
for label, fc, ec, w in capsules:
    cx = x_pos + w / 2
    rbox(ax_b, cx, m2y, w, 0.6, label, fc, ec,
         fontsize=6.5, fontweight='bold', tc=ec, radius=0.1)
    x_pos += w + 0.25

farrow(ax_b, x_pos + 0.3, m2y, x_pos + 1.1, m2y,
       color=TXT3, style='-|>', ms=8)
ax_b.text(x_pos + 1.3, m2y, 'Δaction', fontsize=7.5,
          ha='left', va='center', color=TXT, fontweight='medium')

# ── Method 3: L1 attention profiling ──────────────────────────
num_circle(ax_b, -0.1, 3.25, '3', EDGE['gold'])
ax_b.text(0.5, 3.3, 'L1 attention profiling', fontsize=9,
          fontweight='bold', color=TXT)

hm_x0, hm_y0 = 0.5, 0.3
cell = 0.65

attn = np.array([
    [0.1, 0.1, 0.7, 0.1],
    [0.2, 0.2, 0.6, 0.0],
    [0.3, 0.7, 0.0, 0.0],
    [0.8, 0.0, 0.0, 0.0],
])
row_labels = ['ro', 'inst', 'img', 'img']

for r in range(4):
    ax_b.text(hm_x0 - 0.15, hm_y0 + r * cell + cell / 2,
              row_labels[r], fontsize=6.5, ha='right', va='center',
              color=TXT2, fontstyle='italic')
    for c in range(4):
        v = attn[r, c]
        if v < 0.01:
            fc = '#F5F5F5'
        else:
            fc = plt.cm.Blues(v * 0.65 + 0.18)
        rect = mpatches.FancyBboxPatch(
            (hm_x0 + c * cell + 0.02, hm_y0 + r * cell + 0.02),
            cell - 0.04, cell - 0.04,
            boxstyle='round,pad=0.02',
            facecolor=fc, edgecolor='white', linewidth=0.6, zorder=3)
        ax_b.add_patch(rect)

# Highlight readout→instruction cell
rect_h = mpatches.FancyBboxPatch(
    (hm_x0 + 2 * cell + 0.02, hm_y0 + 0.02),
    cell - 0.04, cell - 0.04,
    boxstyle='round,pad=0.02',
    facecolor='none', edgecolor=EDGE['blue'], linewidth=1.5, zorder=5)
ax_b.add_patch(rect_h)

# Arrow from heatmap
hm_right = hm_x0 + 4 * cell + 0.3
hm_mid_y = hm_y0 + 2 * cell
farrow(ax_b, hm_right, hm_mid_y, hm_right + 1.2, hm_mid_y,
       color=TXT3, style='-|>', ms=8)

tx = hm_right + 1.5
ax_b.plot([tx - 0.5, tx - 0.15], [hm_mid_y + 0.45, hm_mid_y + 0.45],
          color=PASTEL['blue'], lw=2.5, solid_capstyle='round', zorder=4)
ax_b.plot([tx - 0.5, tx - 0.15], [hm_mid_y - 0.45, hm_mid_y - 0.45],
          color=PASTEL['orange'], lw=2.5, solid_capstyle='round', zorder=4)
ax_b.text(tx, hm_mid_y + 0.45, 'readout → instruction', fontsize=8,
          ha='left', va='center', color=EDGE['blue'], fontweight='bold')
ax_b.text(tx, hm_mid_y - 0.45, 'readout → image', fontsize=8,
          ha='left', va='center', color=EDGE['orange'], fontweight='bold')

br_x = tx + 4.5
ax_b.plot([br_x, br_x], [hm_mid_y - 0.65, hm_mid_y + 0.65],
          color=TXT3, lw=0.6, zorder=3)
ax_b.plot([br_x - 0.15, br_x], [hm_mid_y - 0.65, hm_mid_y - 0.65],
          color=TXT3, lw=0.6, zorder=3)
ax_b.plot([br_x - 0.15, br_x], [hm_mid_y + 0.65, hm_mid_y + 0.65],
          color=TXT3, lw=0.6, zorder=3)
ax_b.text(br_x + 0.25, hm_mid_y, 'attention\nratio', fontsize=6.5,
          ha='left', va='center', color=TXT2, linespacing=1.3)

# ═══════════════════════════════════════════════════════════════
# PANEL (c): Finding classification
# ═══════════════════════════════════════════════════════════════
ax_c.set_xlim(-0.5, 11)
ax_c.set_ylim(-0.5, 10.5)

section_title(ax_c, -0.3, 10.2, '(c)', 'Finding classification')

rows_c = [
    ('1', 'Exit collapse\n(ΔR² > 0.10)',  PASTEL_BLUE_L, EDGE['blue'],   'Training-\nassociated'),
    ('2', 'CF sensitivity\n(d ≥ 0.45)',    PASTEL_BLUE_L, EDGE['blue'],   'Action-\nlinked'),
    ('3', 'L1 instruction\nattention',     PASTEL_GOLD_L, EDGE['gold'],   'Inherited\nprior'),
]
row_ys = [7.8, 5.3, 2.8]

# Badge colors per row: Training-associated=orange, Action-linked=blue, Inherited prior=gold
badge_colors = [
    (PASTEL['orange'], EDGE['orange']),
    (PASTEL['blue'],   EDGE['blue']),
    (PASTEL['gold'],   EDGE['gold']),
]

for idx, ((num, finding, box_fc, box_ec, badge_lbl), ry) in enumerate(zip(rows_c, row_ys)):
    circ_color = EDGE['blue'] if box_ec == EDGE['blue'] else EDGE['gold']
    num_circle(ax_c, 0.0, ry, num, circ_color)

    box_cx = 2.8
    box_w = 4.0
    box_h = 1.3
    rbox(ax_c, box_cx, ry, box_w, box_h, finding, fc='white', ec='#CCCCCC',
         fontsize=8.5, lw=0.6, shadow=True, radius=0.14)
    accent = mpatches.FancyBboxPatch(
        (box_cx - box_w/2 - 0.14, ry - box_h/2 + 0.08),
        0.12, box_h - 0.16,
        boxstyle='round,pad=0.03',
        facecolor=box_ec, edgecolor='none', zorder=4, alpha=0.8)
    ax_c.add_patch(accent)

    farrow(ax_c, box_cx + box_w/2 + 0.2, ry, 6.7, ry,
           color=TXT3, lw=0.7, style='-|>', ms=8, ls='--')

    b_fc, b_ec = badge_colors[idx]
    rbox(ax_c, 8.5, ry, 3.2, 1.1, badge_lbl, fc=b_fc, ec=b_ec,
         fontsize=8.5, fontweight='bold', tc=b_ec, lw=0.8,
         shadow=True, radius=0.14)

# ── Panel separators ─────────────────────────────────────────
for sep_x in [0.30, 0.70]:
    line = plt.Line2D([sep_x, sep_x], [0.08, 0.92],
                      transform=fig.transFigure, color='#E0E0E0',
                      linewidth=0.6, zorder=0)
    fig.add_artist(line)

# ═══════════════════════════════════════════════════════════════
# Save
# ═══════════════════════════════════════════════════════════════
base = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
out_paper = f'{base}/docs/paper/figures/fig_overview'
out_artifact = f'{base}/artifacts/figures/paper/fig_overview'

os.makedirs(os.path.dirname(out_paper), exist_ok=True)
os.makedirs(os.path.dirname(out_artifact), exist_ok=True)

plt.savefig(f'{out_paper}.png', dpi=300)
plt.savefig(f'{out_paper}.pdf', dpi=300)

# Copy to artifacts if not the same directory (may be symlinked)
if os.path.realpath(os.path.dirname(out_paper)) != os.path.realpath(os.path.dirname(out_artifact)):
    shutil.copy2(f'{out_paper}.png', f'{out_artifact}.png')
    shutil.copy2(f'{out_paper}.pdf', f'{out_artifact}.pdf')

plt.close()
print(f'Saved: {out_paper}.{{png,pdf}}')
