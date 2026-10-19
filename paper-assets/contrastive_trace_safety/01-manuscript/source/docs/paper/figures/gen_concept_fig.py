"""Generate concept figure: metric choice reverses probe conclusions.
Top-to-bottom flow for single-column ACL paper (3.25in width).
"""
import os
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

fig, ax = plt.subplots(figsize=(3.25, 3.6), dpi=300)
ax.set_xlim(0, 10)
ax.set_ylim(2.2, 11.5)
ax.axis('off')

GREEN = '#4CAF50'
GREEN_LIGHT = '#E8F5E9'
RED = '#E53935'
RED_LIGHT = '#FFEBEE'
BLUE = '#1565C0'
BLUE_LIGHT = '#E3F2FD'
ORANGE = '#E65100'
ORANGE_LIGHT = '#FFF3E0'
GRAY = '#616161'
BANNER_BG = '#FFF8E1'
BANNER_BORDER = '#F9A825'

def add_box(x, y, w, h, fc, ec, text, fs=5.5, fw='normal', tc='black'):
    box = FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.12",
                         facecolor=fc, edgecolor=ec, linewidth=0.7)
    ax.add_patch(box)
    ax.text(x + w/2, y + h/2, text, ha='center', va='center',
            fontsize=fs, fontweight=fw, color=tc)

# === Title ===
ax.text(5.0, 11.2, 'Reasoning Chain-of-Thought', ha='center', va='center',
        fontsize=7, fontweight='bold', color='#212121')

# === Row 1: CoT Trace bar (y=10.0) ===
y_t = 10.0
h_t = 0.8
add_box(0.4, y_t, 3.8, h_t, GREEN_LIGHT, GREEN,
        'Safety deliberation', fs=5.5, fw='bold', tc=GREEN)
add_box(5.8, y_t, 3.8, h_t, RED_LIGHT, RED,
        'Harmful generation', fs=5.5, fw='bold', tc=RED)

# CP dashed line between the two boxes
ax.plot([5.0, 5.0], [y_t - 0.05, y_t + h_t + 0.05],
        color=GRAY, linestyle='--', linewidth=0.9, zorder=5)
ax.text(5.0, y_t + h_t/2, 'CP', ha='center', va='center',
        fontsize=5, fontweight='bold', color='white',
        bbox=dict(boxstyle='round,pad=0.15', facecolor=GRAY, edgecolor='none', alpha=0.85))

# === Arrow down + label ===
y_fork = 9.0
ax.annotate('', xy=(5.0, y_fork + 0.15), xytext=(5.0, y_t - 0.05),
            arrowprops=dict(arrowstyle='->', color=GRAY, lw=0.9))
ax.text(5.0, y_fork + 0.5, 'Extract hidden states  →  Select optimal layer',
        ha='center', va='center', fontsize=4.5, color=GRAY, style='italic')

# === Fork lines ===
ax.plot([5.0, 2.5], [y_fork + 0.1, 8.35], color=BLUE, linewidth=0.7)
ax.plot([5.0, 7.5], [y_fork + 0.1, 8.35], color=ORANGE, linewidth=0.7)

# === Left path (blue): Crossing-rate ===
y_m = 7.65
add_box(0.4, y_m, 4.2, 0.7, BLUE_LIGHT, BLUE,
        'Crossing-rate composite', fs=5.5, fw='bold', tc=BLUE)
ax.annotate('', xy=(2.5, 6.75), xytext=(2.5, y_m),
            arrowprops=dict(arrowstyle='->', color=BLUE, lw=0.7))

y_l = 6.05
add_box(0.4, y_l, 4.2, 0.7, BLUE_LIGHT, BLUE,
        'Shallow layer (L2, 3%)', fs=5.5, tc=BLUE)
ax.annotate('', xy=(2.5, 5.15), xytext=(2.5, y_l),
            arrowprops=dict(arrowstyle='->', color=BLUE, lw=0.7))

y_r = 4.15
box_l = FancyBboxPatch((0.2, y_r), 4.6, 1.0,
    boxstyle="round,pad=0.12", facecolor='white', edgecolor=RED, linewidth=1.1)
ax.add_patch(box_l)
ax.text(2.5, y_r + 0.62, '✗  p = 0.83', ha='center', va='center',
        fontsize=7, fontweight='bold', color=RED)
ax.text(2.5, y_r + 0.25, '(non-significant)', ha='center', va='center',
        fontsize=4.5, color=RED)

# === Right path (orange): Threshold-based ===
add_box(5.4, y_m, 4.2, 0.7, ORANGE_LIGHT, ORANGE,
        'Threshold-based metrics', fs=5.5, fw='bold', tc=ORANGE)
ax.annotate('', xy=(7.5, 6.75), xytext=(7.5, y_m),
            arrowprops=dict(arrowstyle='->', color=ORANGE, lw=0.7))

add_box(5.4, y_l, 4.2, 0.7, ORANGE_LIGHT, ORANGE,
        'Deep layer (L63, 98%)', fs=5.5, tc=ORANGE)
ax.annotate('', xy=(7.5, 5.15), xytext=(7.5, y_l),
            arrowprops=dict(arrowstyle='->', color=ORANGE, lw=0.7))

box_r = FancyBboxPatch((5.2, y_r), 4.6, 1.0,
    boxstyle="round,pad=0.12", facecolor='white', edgecolor=GREEN, linewidth=1.1)
ax.add_patch(box_r)
ax.text(7.5, y_r + 0.62, '✓  p < 0.005', ha='center', va='center',
        fontsize=7, fontweight='bold', color=GREEN)
ax.text(7.5, y_r + 0.25, '(significant)', ha='center', va='center',
        fontsize=4.5, color=GREEN)

# === Bottom banner ===
y_b = 2.5
banner = FancyBboxPatch((0.2, y_b), 9.6, 1.2,
    boxstyle="round,pad=0.15", facecolor=BANNER_BG, edgecolor=BANNER_BORDER,
    linewidth=1.1)
ax.add_patch(banner)
ax.text(5.0, y_b + 0.75, 'Same data, same model (QwQ-32B)',
        ha='center', va='center', fontsize=6, fontweight='bold', color='#E65100')
ax.text(5.0, y_b + 0.32, 'Metric choice alone reverses the conclusion',
        ha='center', va='center', fontsize=5.5, color='#BF360C', style='italic')

# Dashed arrows from results to banner
ax.annotate('', xy=(3.5, y_b + 1.2), xytext=(2.5, y_r),
            arrowprops=dict(arrowstyle='->', color='#9E9E9E', lw=0.5, linestyle='--'))
ax.annotate('', xy=(6.5, y_b + 1.2), xytext=(7.5, y_r),
            arrowprops=dict(arrowstyle='->', color='#9E9E9E', lw=0.5, linestyle='--'))

_dir = os.path.dirname(os.path.abspath(__file__))
plt.subplots_adjust(left=0.01, right=0.99, top=0.99, bottom=0.22)
plt.savefig(os.path.join(_dir, 'fig_concept.png'), dpi=300, bbox_inches='tight',
            pad_inches=0.03, facecolor='white')
plt.savefig(os.path.join(_dir, 'fig_concept.pdf'), bbox_inches='tight',
            pad_inches=0.03, facecolor='white')
print('Saved: fig_concept.png + fig_concept.pdf')
