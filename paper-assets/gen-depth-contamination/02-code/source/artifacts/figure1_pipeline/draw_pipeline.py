import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
import matplotlib.patheffects as pe

fig, ax = plt.subplots(figsize=(7.2, 2.5), dpi=300)
ax.set_xlim(-0.05, 7.25)
ax.set_ylim(-0.5, 2.1)
ax.axis('off')
fig.patch.set_facecolor('white')

C_BLUE     = '#4A90D9'
C_ORANGE   = '#E8724A'
C_TEAL     = '#2EAF7D'
C_PURPLE   = '#7B61A8'
C_CHARCOAL = '#4A4A5A'
C_ARROW    = '#555555'
C_GRAY     = '#777777'

colors = [C_BLUE, C_ORANGE, C_TEAL, C_PURPLE, C_CHARCOAL]
titles = ['Seed Corpus', 'Recursive\nGeneration', 'Feature\nExtraction', 'OBD\nClassifier', r'$K^*$ Estimation']
below_labels = [
    r'$\mathbf{X}$ (depth 0)',
    r'$Y_1, Y_2, \ldots, Y_K$',
    '15D feature vector',
    'Pairwise AUC',
    r'$K^* \!=\! \max\{k : \mathrm{AUC}_k > \theta\}$',
]

box_w = 1.15
box_h = 1.6
gap = 0.28
x_start = 0.1
y_center = 0.95
shadow_off = 0.03

positions = [x_start + i * (box_w + gap) for i in range(5)]
y_top = y_center + box_h / 2
y_bot = y_center - box_h / 2

def draw_box(x, w, h, color):
    ax.add_patch(FancyBboxPatch(
        (x + shadow_off, y_top - h + shadow_off), w, h,
        boxstyle="round,pad=0.06",
        facecolor='#bbbbbb', edgecolor='none', alpha=0.2, zorder=1))
    ax.add_patch(FancyBboxPatch(
        (x, y_top - h), w, h,
        boxstyle="round,pad=0.06",
        facecolor=color, edgecolor='none', alpha=0.93, zorder=2))

for i in range(5):
    draw_box(positions[i], box_w, box_h, colors[i])
    ax.text(positions[i] + box_w / 2, y_top - 0.12, titles[i],
            ha='center', va='top', fontsize=6.5, fontweight='bold',
            color='white', zorder=3, fontfamily='sans-serif', linespacing=1.15)

# ===== Stage 1: stacked documents =====
sx = positions[0]
for j in range(3):
    dx = sx + 0.22 + j * 0.08
    dy = y_center + 0.12 - j * 0.12
    ax.add_patch(FancyBboxPatch(
        (dx, dy - 0.16), 0.5, 0.35, boxstyle="round,pad=0.02",
        facecolor='white', edgecolor='#3a78b5', linewidth=0.6, alpha=0.8, zorder=3))
    for li in range(3):
        ly = dy + 0.12 - li * 0.07
        ax.plot([dx + 0.06, dx + 0.42], [ly, ly],
                color='#3a78b5', linewidth=0.4, alpha=0.45, zorder=4)

# ===== Stage 2: depth chain with proper arrows =====
sx = positions[1]
chain_x = sx + box_w * 0.38
depth_texts = [r'$d\!=\!0$', r'$d\!=\!1$', r'$d\!=\!2$', r'$\vdots$', r'$d\!=\!K$']
dy_positions = []
dy_start = y_center + 0.28
dy_step = 0.2
for j, dt in enumerate(depth_texts):
    dy = dy_start - j * dy_step
    dy_positions.append(dy)
    ax.text(chain_x, dy, dt, ha='center', va='center',
            fontsize=5.5, color='white', zorder=3)

for j in range(len(depth_texts) - 1):
    if depth_texts[j] == r'$\vdots$' or depth_texts[j + 1] == r'$\vdots$':
        continue
    y_from = dy_positions[j] - 0.065
    y_to = dy_positions[j + 1] + 0.065
    ax.annotate('', xy=(chain_x, y_to), xytext=(chain_x, y_from),
                arrowprops=dict(arrowstyle='-|>', color='white',
                                lw=0.6, mutation_scale=5),
                zorder=3)

# Self-loop: curved arrow from d=K back up to d=0 on the right side
loop_x = sx + box_w * 0.75
arc = FancyArrowPatch(
    (loop_x, dy_positions[-1] + 0.02),
    (loop_x, dy_positions[0] - 0.02),
    connectionstyle="arc3,rad=-0.65",
    arrowstyle='-|>', mutation_scale=7,
    color='white', linewidth=0.9, alpha=0.8, zorder=3
)
ax.add_patch(arc)
ax.text(sx + box_w * 0.92, y_center - 0.02, r'$G_\delta$',
        ha='center', va='center', fontsize=5.5, color='white', zorder=4,
        path_effects=[pe.withStroke(linewidth=1.5, foreground=C_ORANGE)])

# ===== Stage 3: 4 feature group rows =====
sx = positions[2]
feat_labels = ['Surprisal\nmoments', 'Surprisal\nderivatives', 'Vocab\ndiversity', 'Freq. tail\nstats']
fy_start = y_center + 0.26
fy_step = 0.26
for j, fl in enumerate(feat_labels):
    fy = fy_start - j * fy_step
    ax.add_patch(FancyBboxPatch(
        (sx + 0.1, fy - 0.09), box_w - 0.2, 0.21,
        boxstyle="round,pad=0.02",
        facecolor='white', edgecolor='none', alpha=0.2, zorder=3))
    ax.text(sx + box_w / 2, fy + 0.015, fl, ha='center', va='center',
            fontsize=4.2, color='white', fontweight='bold', zorder=4,
            fontfamily='sans-serif', linespacing=0.95)

# ===== Stage 4: binary classifiers =====
sx = positions[3]
obd_labels = [r'$k > 0$ ?', r'$k > 1$ ?', r'$\cdots$', r'$k > K\!-\!1$ ?']
oy_start = y_center + 0.26
oy_step = 0.26
for j, ol in enumerate(obd_labels):
    oy = oy_start - j * oy_step
    ax.add_patch(FancyBboxPatch(
        (sx + 0.12, oy - 0.09), box_w - 0.24, 0.21,
        boxstyle="round,pad=0.02",
        facecolor='white', edgecolor='none', alpha=0.2, zorder=3))
    ax.text(sx + box_w / 2, oy + 0.015, ol, ha='center', va='center',
            fontsize=5, color='white', fontweight='bold', zorder=4)

# ===== Stage 5: bar chart with threshold =====
sx = positions[4]
bar_x0 = sx + 0.15
bw = 0.12
bg = 0.04
auc_vals = [0.92, 0.83, 0.71, 0.55, 0.42]
theta_val = 0.60
max_bh = 0.7
bar_y0 = y_center - 0.38

for j, auc in enumerate(auc_vals):
    bx = bar_x0 + j * (bw + bg)
    bh = auc * max_bh
    bc = '#6fcf97' if auc >= theta_val else '#999999'
    ba = 0.85 if auc >= theta_val else 0.35
    ax.add_patch(plt.Rectangle(
        (bx, bar_y0), bw, bh,
        facecolor=bc, edgecolor='white', linewidth=0.3, alpha=ba, zorder=3))

thresh_y = bar_y0 + theta_val * max_bh
line_end = bar_x0 + 5 * (bw + bg) - bg + 0.02
ax.plot([bar_x0 - 0.02, line_end], [thresh_y, thresh_y],
        color='white', linewidth=0.7, linestyle='--', alpha=0.8, zorder=4)
ax.text(line_end + 0.03, thresh_y, r'$\theta$',
        ha='left', va='center', fontsize=5.5, color='white', zorder=4)

# ===== Below-box labels =====
for i in range(5):
    ax.text(positions[i] + box_w / 2, y_bot - 0.12, below_labels[i],
            ha='center', va='top', fontsize=7.5, color=C_GRAY,
            fontstyle='italic', zorder=5)

# ===== Arrows between stages =====
for i in range(4):
    x_from = positions[i] + box_w + 0.02
    x_to = positions[i + 1] - 0.02
    lw = 1.6 if i == 0 else 1.2
    ax.annotate('', xy=(x_to, y_center), xytext=(x_from, y_center),
                arrowprops=dict(arrowstyle='-|>', color=C_ARROW, lw=lw,
                                mutation_scale=9),
                zorder=5)

plt.tight_layout(pad=0.1)
for ext in ['png', 'pdf']:
    plt.savefig(f'pipeline.{ext}', dpi=300, bbox_inches='tight',
                pad_inches=0.05, facecolor='white', edgecolor='none')
print("Done")
