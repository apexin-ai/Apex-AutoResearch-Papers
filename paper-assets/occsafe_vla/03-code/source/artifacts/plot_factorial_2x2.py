"""
2×2 Factorial Interaction Plot: Gradient Flow × Normalization Type → CAR
All data from v2 codebase (Table 1 & Table 2 in paper).
CoRL 2026.
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patheffects as pe
import numpy as np
from pathlib import Path

# === Style: match Fig 1 (serif, academic palette) ===
plt.rcParams.update({
    'font.family': 'serif',
    'font.serif': ['Liberation Serif', 'DejaVu Serif'],
    'font.size': 11,
    'axes.labelsize': 12,
    'axes.titlesize': 12,
    'xtick.labelsize': 11,
    'ytick.labelsize': 11,
    'legend.fontsize': 10,
    'figure.dpi': 300,
    'savefig.dpi': 300,
    'savefig.bbox': 'tight',
    'savefig.pad_inches': 0.05,
    'pdf.fonttype': 42,
    'ps.fonttype': 42,
    'axes.spines.top': False,
    'axes.spines.right': False,
    'lines.linewidth': 2.0,
    'mathtext.fontset': 'cm',
})

# Paper color palette
COLORS = {
    'bn':      '#C44E52',
    'ln':      '#E69F00',
    'vanilla': '#4C72B0',
}

# === v2 data (Table 1) ===
# Gradient Flow: OFF (Detach) = x=0, ON (Full) = x=1
# BN row
bn_off_mean, bn_off_sd, bn_off_n = 0.767, 0.024, 4   # Detach OCC
bn_on_mean,  bn_on_sd,  bn_on_n  = 0.725, 0.064, 3   # Full OCC

# LN row
ln_off_mean, ln_off_sd, ln_off_n = 0.802, 0.024, 3   # Detach+LN
ln_on_mean,  ln_on_sd,  ln_on_n  = 0.773, 0.027, 4   # Full OCC+LN

vanilla_car = 0.745

# === Figure ===
fig, ax = plt.subplots(figsize=(4.8, 4.2))

x_pos = np.array([0, 1])
x_labels = ['OFF (Detach)', 'ON (Full)']

# Vanilla baseline
ax.axhline(vanilla_car, color=COLORS['vanilla'], linestyle=':', linewidth=1.2, alpha=0.6, zorder=1)
ax.text(1.12, vanilla_car + 0.003, f'Vanilla ({vanilla_car:.3f})',
        fontsize=9.5, color=COLORS['vanilla'], va='bottom', ha='left',
        style='italic', alpha=0.8,
        path_effects=[pe.withStroke(linewidth=2.5, foreground='white')])

# Below-baseline zone
ax.axhspan(0.68, vanilla_car, alpha=0.03, color=COLORS['bn'], zorder=0)

# BN line (solid)
ax.errorbar(x_pos, [bn_off_mean, bn_on_mean], yerr=[bn_off_sd, bn_on_sd],
            fmt='o-', color=COLORS['bn'], linewidth=2.0, markersize=9,
            capsize=5, capthick=1.5, markeredgecolor='white', markeredgewidth=1.0,
            label='BatchNorm (BN)', zorder=5)

# LN line (dashed)
ax.errorbar(x_pos, [ln_off_mean, ln_on_mean], yerr=[ln_off_sd, ln_on_sd],
            fmt='s--', color=COLORS['ln'], linewidth=2.0, markersize=9,
            capsize=5, capthick=1.5, markeredgecolor='white', markeredgewidth=1.0,
            label='LayerNorm (LN)', zorder=5)

# Delta annotations
# BN delta: -4.2 pp
mid_bn_y = (bn_off_mean + bn_on_mean) / 2
ax.annotate(f'$-$4.2 pp', xy=(0.5, mid_bn_y - 0.006),
            fontsize=10.5, color=COLORS['bn'], ha='center', va='top',
            fontweight='bold',
            path_effects=[pe.withStroke(linewidth=2.5, foreground='white')])

# LN delta: -2.9 pp
mid_ln_y = (ln_off_mean + ln_on_mean) / 2
ax.annotate(f'$-$2.9 pp', xy=(0.5, mid_ln_y + 0.006),
            fontsize=10.5, color=COLORS['ln'], ha='center', va='bottom',
            fontweight='bold',
            path_effects=[pe.withStroke(linewidth=2.5, foreground='white')])

# n= annotations (hand-tuned offsets to avoid overlap)
n_positions = [
    (0, bn_off_n, bn_off_mean, COLORS['bn'], -0.07, -0.016),  # BN OFF: left-below
    (1, bn_on_n,  bn_on_mean,  COLORS['bn'],  0.06, -0.016),  # BN ON: right-below
    (0, ln_off_n, ln_off_mean, COLORS['ln'], -0.07,  0.012),  # LN OFF: left-above
    (1, ln_on_n,  ln_on_mean,  COLORS['ln'],  0.06,  0.012),  # LN ON: right-above
]
for x, n, y, color, dx, dy in n_positions:
    ha = 'right' if dx < 0 else 'left'
    ax.text(x + dx, y + dy, f'n={n}', fontsize=8.5,
            color=color, va='center', ha=ha, alpha=0.7, style='italic',
            path_effects=[pe.withStroke(linewidth=2, foreground='white')])

ax.set_xticks(x_pos)
ax.set_xticklabels(x_labels)
ax.set_xlabel('Gradient Flow', fontsize=12, fontweight='bold')
ax.set_ylabel('Collision Avoidance Rate (CAR)', fontsize=12, fontweight='bold')
ax.set_xlim(-0.35, 1.35)
ax.set_ylim(0.68, 0.86)
ax.set_yticks(np.arange(0.68, 0.87, 0.02))
ax.grid(axis='y', alpha=0.12, linewidth=0.5, zorder=0)

ax.legend(loc='upper right', framealpha=0.95, edgecolor='#CCCCCC',
          fancybox=True, borderpad=0.6)

plt.tight_layout()

# Save
out_dir = Path(__file__).parent / '..' / 'docs' / 'paper' / 'figures'
out_dir = out_dir.resolve()
out_dir.mkdir(parents=True, exist_ok=True)
fig.savefig(out_dir / 'factorial_2x2.pdf', bbox_inches='tight', pad_inches=0.05)
fig.savefig(out_dir / 'factorial_2x2.png', dpi=300, bbox_inches='tight', pad_inches=0.05)
print(f"Saved: {out_dir / 'factorial_2x2.pdf'}")
plt.close()
