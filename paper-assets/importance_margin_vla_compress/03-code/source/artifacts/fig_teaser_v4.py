import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch
import matplotlib.patheffects as pe
import numpy as np
import os

plt.rcParams.update({
    'font.family': 'DejaVu Sans',
    'font.size': 11,
    'axes.titlesize': 12,
    'axes.labelsize': 11,
    'xtick.labelsize': 10,
    'ytick.labelsize': 10,
    'legend.fontsize': 10,
    'figure.dpi': 300,
    'savefig.dpi': 300,
    'savefig.bbox': 'tight',
    'savefig.pad_inches': 0.08,
    'axes.spines.top': False,
    'axes.spines.right': False,
    'lines.linewidth': 2.0,
})

C_BLUE = '#0072B2'
C_RED = '#D55E00'
C_GREEN = '#009E73'

fig = plt.figure(figsize=(14, 5.8))
gs = fig.add_gridspec(1, 2, width_ratios=[1, 1.15], wspace=0.10)

# ============================================================
# Panel (a): 2x2 Vulnerability Map
# ============================================================
ax1 = fig.add_subplot(gs[0])
ax1.set_xlim(-1.5, 11.5)
ax1.set_ylim(-1.8, 12.8)
ax1.axis('off')

# 2D gradient background (green top-left -> red bottom-right)
x_g = np.linspace(0, 1, 300)
y_g = np.linspace(0, 1, 300)
X, Y = np.meshgrid(x_g, y_g)
severity = 0.45 * X + 0.55 * (1 - Y)
grad = np.zeros((*severity.shape, 4))
grad[..., 0] = 0.15 + 0.55 * severity
grad[..., 1] = 0.72 - 0.32 * severity
grad[..., 2] = 0.35 - 0.18 * severity
grad[..., 3] = 0.13 + 0.18 * severity
ax1.imshow(grad, extent=[0.5, 10.5, -0.5, 10], aspect='auto', zorder=0,
           origin='upper', interpolation='bilinear')

border = mpatches.FancyBboxPatch((0.5, -0.5), 10, 10.5, boxstyle='round,pad=0',
                                  facecolor='none', edgecolor='#cccccc',
                                  linewidth=0.8, zorder=1)
ax1.add_patch(border)

# Grid dividers (thin lines separating 2x2 cells)
ax1.plot([5.5, 5.5], [-0.5, 10.0], color='#cccccc', linewidth=0.7, zorder=1, alpha=0.6)
ax1.plot([0.5, 10.5], [5.0, 5.0], color='#cccccc', linewidth=0.7, zorder=1, alpha=0.6)

# Panel title
ax1.text(5.5, 12.4, r'$\mathbf{(a)}$  Pruning Vulnerability Map',
         ha='center', fontsize=13, fontweight='bold')
ax1.text(5.5, 11.6, 'Success rate at  $k = 0.9$  (L2-norm pruning, 10% tokens removed)',
         ha='center', fontsize=9, color='#666')

# Axis arrows
ax1.annotate('', xy=(10.3, 10.8), xytext=(0.8, 10.8),
             arrowprops=dict(arrowstyle='->', color='#555', lw=1.5, mutation_scale=15))
ax1.text(5.5, 11.0, 'Token Coupling', ha='center', fontsize=10.5,
         color='#444', fontstyle='italic')

ax1.annotate('', xy=(0.15, -0.3), xytext=(0.15, 9.8),
             arrowprops=dict(arrowstyle='->', color='#555', lw=1.5, mutation_scale=15))
ax1.text(-0.6, 4.75, 'Task Complexity', ha='center', va='center', fontsize=10.5,
         color='#444', fontstyle='italic', rotation=90)

# Tick labels — slightly bolder
ax1.text(3.0, 10.35, 'Independent', ha='center', fontsize=10, color='#555',
         fontweight='medium')
ax1.text(8.0, 10.35, 'Entangling', ha='center', fontsize=10, color='#555',
         fontweight='medium')
ax1.text(0.30, 7.3, 'Simple', ha='center', fontsize=10, color='#555',
         fontweight='medium', rotation=90)
ax1.text(0.30, 2.3, 'Complex', ha='center', fontsize=10, color='#555',
         fontweight='medium', rotation=90)

# Cell data
cells = [
    (1.0, 5.3, r'$\pi_{0.5}$', 'CV = 0.055', '98.4%', '−0.0 pp',
     '#d5edda', '#2ecc71', '#1a7a3a'),
    (5.8, 5.3, 'X-VLA', 'CV = 0.151', '97.6%', '−1.6 pp',
     '#d6eaf8', '#3498db', '#1a5276'),
    (1.0, 0.0, r'$\pi_{0.5}$', 'CV = 0.055', '91.0%', '−5.4 pp',
     '#fef9e7', '#f39c12', '#7d6608'),
    (5.8, 0.0, 'X-VLA', 'CV = 0.151', '70.2%', '−27.8 pp',
     '#fadbd8', '#e74c3c', '#922b21'),
]

for x, y, model, cv, sr, drop, bg, edge, tcol in cells:
    w, h = 4.2, 4.7
    card = FancyBboxPatch((x, y), w, h, boxstyle='round,pad=0.3',
                           facecolor=bg, edgecolor=edge,
                           linewidth=2.0, alpha=0.94, zorder=2)
    ax1.add_patch(card)
    cx, cy = x + w/2, y + h/2
    ax1.text(cx, cy + 1.45, model, ha='center', fontsize=15, fontweight='bold',
             color='#333', zorder=3)
    ax1.text(cx, cy + 0.65, cv, ha='center', fontsize=8.5, color='#888', zorder=3)
    ax1.text(cx, cy - 0.35, sr, ha='center', fontsize=22, fontweight='bold',
             color=tcol, zorder=3)
    ax1.text(cx, cy - 1.45, f'({drop})', ha='center', fontsize=10, color=tcol,
             fontstyle='italic', zorder=3)

# SmolVLA footnote
ax1.text(5.5, -1.4,
         'SmolVLA (pixel-shuffle, CV = 0.314) → 0% SR at $k = 0.95$ on all 4 suites',
         ha='center', fontsize=8, color='#aaa', fontstyle='italic')

# ============================================================
# Panel (b): X-VLA SR vs keep ratio k
# ============================================================
ax2 = fig.add_subplot(gs[1])

k_vals = [0.5, 0.7, 0.9, 1.0]
object_sr = [43.4, 58.2, 97.6, 99.2]
goal_sr = [59.0, 53.4, 70.2, 98.0]

ax2.plot(k_vals, object_sr, 'o-', color=C_BLUE, markersize=9,
         markeredgecolor='white', markeredgewidth=1.8, zorder=4,
         label='Object (simple)', solid_capstyle='round')
ax2.plot(k_vals, goal_sr, 's-', color=C_RED, markersize=9,
         markeredgecolor='white', markeredgewidth=1.8, zorder=4,
         label='Goal (complex)', solid_capstyle='round')

# Baselines
ax2.axhline(99.2, color=C_BLUE, linestyle=':', alpha=0.25, linewidth=1, zorder=1)
ax2.axhline(98.0, color=C_RED, linestyle=':', alpha=0.25, linewidth=1, zorder=1)

# Vertical ref at k=0.9
ax2.axvline(0.9, color='#bbb', linestyle='--', linewidth=0.8, alpha=0.5, zorder=1)

# Shaded gap at k=0.9
ax2.fill_betweenx([70.2, 97.6], 0.882, 0.918,
                   alpha=0.10, color='#888', zorder=1)

# Double-arrow bracket
ax2.annotate('', xy=(0.94, 97), xytext=(0.94, 70.8),
             arrowprops=dict(arrowstyle='<->', color='#333', lw=1.8,
                             shrinkA=0, shrinkB=0))
ax2.text(0.96, 83.9, '27.8 pp\ngap', fontsize=11, fontweight='bold',
         ha='left', va='center', color='#333',
         bbox=dict(boxstyle='round,pad=0.35', facecolor='white',
                   edgecolor='#bbb', alpha=0.95, linewidth=0.8))

# Value annotations at k=0.9
t1 = ax2.text(0.878, 100.5, '97.6%', fontsize=10.5, fontweight='bold',
              color=C_BLUE, ha='right')
t1.set_path_effects([pe.withStroke(linewidth=3, foreground='white')])
t2 = ax2.text(0.878, 65.5, '70.2%', fontsize=10.5, fontweight='bold',
              color=C_RED, ha='right')
t2.set_path_effects([pe.withStroke(linewidth=3, foreground='white')])

# Baseline labels — right side near k=1.0, vertically offset to avoid overlap
t3 = ax2.text(1.045, 102.0, '99.2%', fontsize=8.5, color=C_BLUE,
              alpha=0.6, va='center', ha='left', fontweight='bold')
t3.set_path_effects([pe.withStroke(linewidth=2.5, foreground='white')])
t4 = ax2.text(1.045, 95.0, '98.0%', fontsize=8.5, color=C_RED,
              alpha=0.6, va='center', ha='left', fontweight='bold')
t4.set_path_effects([pe.withStroke(linewidth=2.5, foreground='white')])

ax2.set_xlabel('Keep Ratio  $k$', fontsize=12)
ax2.set_ylabel('Success Rate (%)', fontsize=12)
ax2.set_title(r'$\mathbf{(b)}$  X-VLA: Simple vs Complex Task Degradation',
              fontsize=13, fontweight='bold', pad=12)
ax2.set_xlim(0.44, 1.08)
ax2.set_ylim(0, 112)
ax2.set_xticks([0.5, 0.6, 0.7, 0.8, 0.9, 1.0])
ax2.set_yticks([0, 20, 40, 60, 80, 100])
ax2.legend(loc='upper left', fontsize=10, framealpha=0.95, edgecolor='#ddd',
           fancybox=True)
ax2.grid(True, alpha=0.10, zorder=0)

outdir = '/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/artifacts'
os.makedirs(outdir, exist_ok=True)
fig.savefig(f'{outdir}/fig_teaser.pdf', dpi=300)
fig.savefig(f'{outdir}/fig_teaser.png', dpi=300)
print(f'Saved to {outdir}/fig_teaser.pdf and .png')
