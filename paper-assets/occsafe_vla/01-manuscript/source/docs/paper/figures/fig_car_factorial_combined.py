#!/usr/bin/env python3
"""Combined Figure: (a) CAR horizontal dot chart + (b) Factorial 2x2 interaction plot."""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patheffects as pe
import numpy as np

COLORS = {
    'vanilla':     '#4C72B0',
    'full_occ_bn': '#C44E52',
    'full_occ_ln': '#E69F00',
    'detach_bn':   '#8172B3',
    'detach_ln':   '#937860',
}
UI = {'text': '#2C3E50', 'subtle': '#95A5A6'}

plt.rcParams.update({
    'font.family': 'serif',
    'font.serif': ['DejaVu Serif', 'Liberation Serif', 'Times New Roman'],
    'font.size': 7.5,
    'axes.titlesize': 8,
    'axes.labelsize': 8,
    'xtick.labelsize': 7,
    'ytick.labelsize': 7,
    'legend.fontsize': 7,
    'figure.dpi': 300,
    'savefig.dpi': 300,
    'savefig.bbox': 'tight',
    'savefig.pad_inches': 0.03,
    'axes.spines.top': False,
    'axes.spines.right': False,
    'axes.linewidth': 0.6,
    'pdf.fonttype': 42,
    'ps.fonttype': 42,
    'mathtext.fontset': 'cm',
    'text.color': UI['text'],
    'axes.labelcolor': UI['text'],
})

fig, (ax_bar, ax_fact) = plt.subplots(1, 2, figsize=(7.0, 3.0), dpi=300, facecolor='white')

# ============================================================
# (a) CAR horizontal dot chart
# ============================================================
cdata = [
    {'name': 'Full OCC\n(BN, Grad ON)',    'car': 0.725, 'sd': 0.064,
     'color': COLORS['full_occ_bn'], 'n_seeds': 3},
    {'name': 'Detach OCC\n(BN, Grad OFF)',  'car': 0.767, 'sd': 0.024,
     'color': COLORS['detach_bn'],   'n_seeds': 4},
    {'name': 'Full OCC+LN\n(LN, Grad ON)', 'car': 0.773, 'sd': 0.027,
     'color': COLORS['full_occ_ln'], 'n_seeds': 4},
    {'name': 'Detach+LN\n(LN, Grad OFF)',  'car': 0.802, 'sd': 0.024,
     'color': COLORS['detach_ln'],   'n_seeds': 3},
]
vanilla_car = 0.745

ax = ax_bar
ax.set_xlim(0.655, 0.87)
ax.set_ylim(-0.8, len(cdata) - 0.2)
ax.invert_yaxis()
ax.spines['left'].set_visible(False)
ax.set_xlabel('Collision Avoidance Rate (CAR)', fontsize=8, fontweight='bold', labelpad=5)

# Group background bands
ax.axhspan(-0.5, 1.5, alpha=0.02, color=COLORS['full_occ_bn'], zorder=0)
ax.axhspan(1.5, 3.5, alpha=0.02, color=COLORS['full_occ_ln'], zorder=0)
ax.text(0.865, 0.5, 'BN', fontsize=8, color=COLORS['full_occ_bn'], ha='center', va='center',
        fontweight='bold', alpha=0.35,
        bbox=dict(boxstyle='round,pad=0.15', facecolor='white', edgecolor='none', alpha=0.6))
ax.text(0.865, 2.5, 'LN', fontsize=8, color=COLORS['full_occ_ln'], ha='center', va='center',
        fontweight='bold', alpha=0.35,
        bbox=dict(boxstyle='round,pad=0.15', facecolor='white', edgecolor='none', alpha=0.6))

# Vanilla reference
ax.axvline(x=vanilla_car, color=COLORS['vanilla'], linestyle='--',
           linewidth=1.5, alpha=0.7, zorder=1)
ax.text(vanilla_car + 0.003, -0.55, f'Vanilla  {vanilla_car:.3f}',
        fontsize=8, color=COLORS['vanilla'], va='top', ha='left',
        fontweight='bold',
        path_effects=[pe.withStroke(linewidth=2.5, foreground='white')])

# Below-baseline shading
ax.axvspan(0.655, vanilla_car, alpha=0.04, color=COLORS['full_occ_bn'], zorder=0)

# Connecting lines: BN pair
ax.plot([0.725, 0.767], [0, 1], color=COLORS['full_occ_bn'],
        lw=1.1, linestyle=':', alpha=0.5, zorder=1)
ax.text(0.730, 0.55, '$-$4.2 pp', fontsize=7.5,
        color=COLORS['full_occ_bn'], ha='left', va='center',
        fontweight='bold', alpha=0.8,
        path_effects=[pe.withStroke(linewidth=2.5, foreground='white')])

# LN pair
ax.plot([0.773, 0.802], [2, 3], color=COLORS['full_occ_ln'],
        lw=1.1, linestyle=':', alpha=0.5, zorder=1)
ax.text(0.778, 2.55, '$-$2.9 pp', fontsize=7.5,
        color=COLORS['full_occ_ln'], ha='left', va='center',
        fontweight='bold', alpha=0.8,
        path_effects=[pe.withStroke(linewidth=2.5, foreground='white')])

# Plot data points
for i, d in enumerate(cdata):
    ax.plot(d['car'], i, 'o', color=d['color'], markersize=7.5,
            markeredgecolor='white', markeredgewidth=0.8, zorder=5)
    ax.errorbar(d['car'], i, xerr=d['sd'], fmt='none', ecolor=d['color'],
                elinewidth=1.8, capsize=4, capthick=1.3, zorder=4, alpha=0.7)
    right_x = d['car'] + d['sd'] + 0.005
    label_text = f'{d["car"]:.3f} ± {d["sd"]:.3f}'
    ax.text(right_x, i + 0.02, label_text, fontsize=7.5, ha='left',
            va='center', color=d['color'], fontweight='bold',
            path_effects=[pe.withStroke(linewidth=2.5, foreground='white')])

ax.set_yticks(list(range(len(cdata))))
ax.set_yticklabels([d['name'] for d in cdata], fontsize=7.5, linespacing=1.1)
ax.tick_params(axis='y', length=0, pad=5)
ax.tick_params(axis='x', labelsize=7)
ax.grid(axis='x', alpha=0.10, color='#999', zorder=0)
ax.set_xticks([0.68, 0.72, 0.76, 0.80, 0.84])

# Panel label
ax.text(-0.02, 1.06, '(a)', transform=ax.transAxes, fontsize=10, fontweight='bold', va='top')

# ============================================================
# (b) Factorial 2x2 interaction plot
# ============================================================
factorial_data = {
    'BN': {
        'OFF': {'mean': 0.767, 'std': 0.024, 'n': 4},
        'ON':  {'mean': 0.725, 'std': 0.064, 'n': 3},
    },
    'LN': {
        'OFF': {'mean': 0.802, 'std': 0.024, 'n': 3},
        'ON':  {'mean': 0.773, 'std': 0.027, 'n': 4},
    },
}

C_BN = COLORS['full_occ_bn']
C_LN = COLORS['full_occ_ln']
C_VAN = COLORS['vanilla']

ax = ax_fact
ax.axhspan(0.68, vanilla_car, color=C_BN, alpha=0.03, zorder=0)
ax.axhline(y=vanilla_car, color=C_VAN, linestyle=':', linewidth=0.8, alpha=0.5, zorder=1)
t_van = ax.text(0.97, vanilla_car + 0.002, 'Vanilla (0.745)', fontsize=7,
                color=C_VAN, va='bottom', ha='right',
                transform=ax.get_yaxis_transform(), fontweight='medium')
t_van.set_path_effects([pe.withStroke(linewidth=2.5, foreground='white')])

x_positions = [0, 1]

bn_y = [factorial_data['BN']['OFF']['mean'], factorial_data['BN']['ON']['mean']]
bn_err = [factorial_data['BN'][gf]['std'] for gf in ['OFF', 'ON']]
ax.errorbar(x_positions, bn_y, yerr=bn_err, color=C_BN,
            marker='o', markersize=5.5, markeredgecolor='white', markeredgewidth=0.7,
            linestyle='-', linewidth=1.4, capsize=3, capthick=0.8,
            elinewidth=0.8, label='BatchNorm (BN)', zorder=3)

ln_y = [factorial_data['LN']['OFF']['mean'], factorial_data['LN']['ON']['mean']]
ln_err = [factorial_data['LN'][gf]['std'] for gf in ['OFF', 'ON']]
ax.errorbar(x_positions, ln_y, yerr=ln_err, color=C_LN,
            marker='s', markersize=5.5, markeredgecolor='white', markeredgewidth=0.7,
            linestyle=(0, (4, 2.5)), linewidth=1.4, capsize=3, capthick=0.8,
            elinewidth=0.8, label='LayerNorm (LN)', zorder=3)

# Delta annotations
delta_bn = (factorial_data['BN']['ON']['mean'] - factorial_data['BN']['OFF']['mean']) * 100
delta_ln = (factorial_data['LN']['ON']['mean'] - factorial_data['LN']['OFF']['mean']) * 100

mid_bn_y = np.mean(bn_y)
t_bn = ax.annotate(f'−{abs(delta_bn):.1f} pp', xy=(0.55, mid_bn_y - 0.008),
                   fontsize=7.5, fontweight='bold', color=C_BN, ha='center', va='top', zorder=5)
t_bn.set_path_effects([pe.withStroke(linewidth=2, foreground='white')])

mid_ln_y = np.mean(ln_y)
t_ln = ax.annotate(f'−{abs(delta_ln):.1f} pp', xy=(0.45, mid_ln_y + 0.008),
                   fontsize=7.5, fontweight='bold', color=C_LN, ha='center', va='bottom', zorder=5)
t_ln.set_path_effects([pe.withStroke(linewidth=2, foreground='white')])

# n-labels
n_offsets = {
    ('BN', 'OFF'): (-12, -10),
    ('BN', 'ON'):  (12, -14),
    ('LN', 'OFF'): (-12, 8),
    ('LN', 'ON'):  (12, 10),
}
for gf_idx, gf in enumerate(['OFF', 'ON']):
    for norm in ['BN', 'LN']:
        n_val = factorial_data[norm][gf]['n']
        y_val = factorial_data[norm][gf]['mean']
        ox, oy = n_offsets[(norm, gf)]
        c = C_BN if norm == 'BN' else C_LN
        ax.annotate(f'n={n_val}', (x_positions[gf_idx], y_val),
                    xytext=(ox, oy), textcoords='offset points',
                    fontsize=7, color=c, ha='center', fontstyle='italic', alpha=0.6)

ax.set_xticks(x_positions)
ax.set_xticklabels(['OFF\n(Detach)', 'ON\n(Full)'], fontsize=7)
ax.set_xlabel('Gradient Flow', fontsize=8)
ax.set_ylabel('Collision Avoidance Rate (CAR)', fontsize=8)
ax.set_xlim(-0.3, 1.3)
ax.set_ylim(0.68, 0.86)
ax.yaxis.set_major_locator(plt.MultipleLocator(0.02))
ax.legend(loc='upper right', frameon=True, framealpha=0.95, edgecolor='none',
          handlelength=2.0, handletextpad=0.4, fontsize=7)

# Panel label
ax.text(-0.02, 1.06, '(b)', transform=ax.transAxes, fontsize=10, fontweight='bold', va='top')

plt.tight_layout(w_pad=2.0)

# Save
OUT_DIR = '/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/figures'
for fmt in ['pdf', 'png']:
    path = f'{OUT_DIR}/fig_car_factorial_combined.{fmt}'
    fig.savefig(path, facecolor='white')
    print(f'Saved: {path}')
plt.close(fig)
