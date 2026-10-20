# -*- coding: utf-8 -*-
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patheffects as pe
import numpy as np

PI = 'π'  # π

plt.rcParams.update({
    'font.family': 'serif',
    'font.serif': ['Times New Roman', 'Liberation Serif', 'DejaVu Serif'],
    'mathtext.fontset': 'stix',
    'font.size': 11,
    'axes.titlesize': 13,
    'axes.labelsize': 12,
    'xtick.labelsize': 10,
    'ytick.labelsize': 10,
    'legend.fontsize': 9,
    'figure.dpi': 300,
    'savefig.dpi': 300,
    'savefig.bbox': 'tight',
    'savefig.pad_inches': 0.05,
    'axes.spines.top': False,
    'axes.spines.right': False,
    'pdf.fonttype': 42,
    'ps.fonttype': 42,
    'lines.linewidth': 1.8,
})

# Okabe-Ito inspired semantic colors
C_PI05 = '#009E73'     # green — uniformly critical
C_XVLA = '#0072B2'     # blue — threshold-graded
C_OPENVLA = '#E69F00'  # orange — smooth graded
C_SMOLVLA = '#D55E00'  # vermillion — catastrophic cliff

# ── Panel (a) data ──
pi05_random_k =   [0.3,  0.5,  0.7,  1.0]
pi05_random_acc =  [36.4, 69.4, 77.2, 98.2]

pi05_l2_k =   [0.3,  0.5,  0.7,  1.0]
pi05_l2_acc =  [51.0, 33.4, 55.0, 98.2]

xvla_k =   [0.1, 0.2, 0.3,  0.5,  0.7,  0.8,  0.85, 0.9,  0.95, 1.0]
xvla_acc = [2.0, 4.7, 22.3, 43.4, 57.2, 88.6, 67.8, 97.8, 99.1, 99.2]

openvla_k =   [0.3,  0.5,  0.7,  0.9,  0.95, 1.0]
openvla_acc = [20.6, 37.4, 49.0, 62.0, 69.4, 74.0]

smolvla_k =   [0.5, 0.7, 0.9, 0.95, 1.0]
smolvla_acc = [0.0, 0.0, 0.0, 0.0,  44.8]

# ── Panel (b) data ──
models_b = [f'{PI}0.5\n(CV=0.055)', 'X-VLA\n(CV=0.151)', 'OpenVLA\n(CV=0.215)']
delta_k05 = [36.0, 26.9, -3.4]
delta_k07 = [22.2, 6.5, -5.4]

# ── Figure layout ──
fig, (ax_a, ax_b) = plt.subplots(1, 2, figsize=(12, 4.5),
                                  gridspec_kw={'width_ratios': [1.4, 1]})

# ═══════════════════════════════════════════
# Panel (a): Degradation curves
# ═══════════════════════════════════════════

# Class region annotations (subtle background)
# We'll place text annotations at the right side instead of colored regions
# to avoid visual clutter

ax_a.plot(pi05_random_k, pi05_random_acc, '-o', color=C_PI05,
          markersize=6, label=f'{PI}0.5 (random)', zorder=5)
ax_a.plot(pi05_l2_k, pi05_l2_acc, '--^', color=C_PI05,
          markersize=6, label=f'{PI}0.5 (L2norm)', zorder=5)
ax_a.plot(xvla_k, xvla_acc, '-s', color=C_XVLA,
          markersize=5, label='X-VLA (L2norm)', zorder=5)
ax_a.plot(openvla_k, openvla_acc, '-D', color=C_OPENVLA,
          markersize=5, label='OpenVLA (random)', zorder=5)
ax_a.plot(smolvla_k, smolvla_acc, '-x', color=C_SMOLVLA,
          markersize=7, markeredgewidth=2, label='SmolVLA', zorder=5)

# Class label annotations (right side of panel)
class_labels = [
    (C_PI05,    'Uniformly\nCritical',     0.42, 90, 'center'),
    (C_XVLA,   'Threshold-\ngraded',       0.18, 38, 'center'),
    (C_OPENVLA, 'Smooth\nGraded',          0.62, 46, 'center'),
    (C_SMOLVLA, 'Catastrophic\nCliff',     0.40, 3,  'center'),
]
for color, label, x_pos, y_pos, ha in class_labels:
    t = ax_a.text(x_pos, y_pos, label, fontsize=8, color=color,
                  ha=ha, va='center', fontstyle='italic', fontweight='bold',
                  alpha=0.7)
    t.set_path_effects([pe.withStroke(linewidth=2.5, foreground='white')])

# Annotate SmolVLA baseline jump
ax_a.annotate('baseline\n44.8%', xy=(1.0, 44.8), xytext=(0.88, 30),
              fontsize=7, color=C_SMOLVLA, ha='center',
              arrowprops=dict(arrowstyle='->', color=C_SMOLVLA, lw=0.8))

# Annotate X-VLA cliff at k=0.85
ax_a.annotate('cliff', xy=(0.85, 67.8), xytext=(0.78, 82),
              fontsize=7, color=C_XVLA, ha='center',
              arrowprops=dict(arrowstyle='->', color=C_XVLA, lw=0.8))

ax_a.set_xlabel('Token Retention Ratio (k)')
ax_a.set_ylabel('Task Success Rate (%)')
ax_a.set_xlim(0.05, 1.05)
ax_a.set_ylim(-3, 105)
ax_a.legend(loc='upper left', fontsize=9, framealpha=0.9)
ax_a.set_title('(a) Token Pruning Degradation Curves', fontsize=12,
               fontweight='bold', loc='left', pad=8)
ax_a.grid(True, alpha=0.15, zorder=0)

# ═══════════════════════════════════════════
# Panel (b): Dual-k grouped bar chart
# ═══════════════════════════════════════════

x = np.arange(len(models_b))
bar_width = 0.32

C_K05 = '#0072B2'  # deep blue
C_K07 = '#56B4E9'  # sky blue

bars1 = ax_b.bar(x - bar_width/2, delta_k05, bar_width,
                 color=C_K05, label='k = 0.5', zorder=3)
bars2 = ax_b.bar(x + bar_width/2, delta_k07, bar_width,
                 color=C_K07, label='k = 0.7', zorder=3)

# Horizontal line at y=0
ax_b.axhline(0, color='black', linewidth=0.8, linestyle='--', zorder=2)

# Annotate bar values
for bar_group in [bars1, bars2]:
    for bar in bar_group:
        val = bar.get_height()
        if val >= 0:
            y_pos = val + 0.8
            va = 'bottom'
        else:
            y_pos = val - 0.8
            va = 'top'
        sign = '+' if val > 0 else ''
        ax_b.text(bar.get_x() + bar.get_width()/2, y_pos,
                  f'{sign}{val:.1f}', ha='center', va=va,
                  fontsize=8.5, fontweight='bold')

# Zone labels
ax_b.text(2.35, 30, 'Random better ↑', fontsize=8, color='#555555',
          ha='center', va='center', fontstyle='italic', alpha=0.6)
ax_b.text(2.35, -8.5, 'L2 better ↓', fontsize=8, color='#555555',
          ha='center', va='center', fontstyle='italic', alpha=0.6)

ax_b.set_xticks(x)
ax_b.set_xticklabels(models_b, fontsize=9)
ax_b.set_xlabel('Model (sorted by CV →)', fontsize=11)
ax_b.set_ylabel('Δ(Random − L2norm) (pp)', fontsize=11)
ax_b.set_title('(b) CV Scaling Law', fontsize=12,
               fontweight='bold', loc='left', pad=8)
ax_b.legend(loc='upper right', fontsize=9, framealpha=0.9)
ax_b.set_ylim(-12, 42)
ax_b.grid(True, alpha=0.15, axis='y', zorder=0)

plt.tight_layout(w_pad=3)

outpath = '/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/figures/paper/fig_degradation_curve.pdf'
plt.savefig(outpath)
plt.close()
print(f'Saved: {outpath}')
