import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import matplotlib.transforms as mtransforms
from matplotlib.patches import FancyBboxPatch

mpl.rcParams.update({
    'font.family': 'serif',
    'font.serif': ['Liberation Serif', 'Times New Roman', 'DejaVu Serif'],
    'mathtext.fontset': 'cm',
    'pdf.fonttype': 42,
    'axes.linewidth': 0.8,
    'xtick.major.width': 0.6,
    'ytick.major.width': 0.6,
    'xtick.major.size': 3,
    'ytick.major.size': 3,
    'xtick.direction': 'in',
    'ytick.direction': 'in',
    'axes.grid': False,
    'font.size': 8,
    'axes.labelsize': 8.5,
    'axes.titlesize': 9,
})

alpha = np.linspace(0, 1, 500)

S = alpha ** 0.8

R_base = 1 / (1 + np.exp(-15 * (alpha - 0.30)))
R_dip = 0.55 * np.exp(-((alpha - 0.58) / 0.055) ** 2)
R = R_base - R_dip
R = np.clip(R, 0, 1)

detection = S * R

regime_bounds = [0, 0.35, 0.52, 0.72, 1.0]
regime_colors_bg = ['#eeeeee', '#d0e1f2', '#f2d0d0', '#d0ecd0']
regime_colors_bar = ['#c0c0c0', '#8db3d9', '#d98b8b', '#8bc98b']
regime_labels = ['Blind', 'Onset', 'Collapse', 'Detection']

fig = plt.figure(figsize=(7.2, 3.0))

# Create gridspec: panel(c) needs extra space above for regime bar
gs = fig.add_gridspec(2, 3, height_ratios=[0.08, 1],
                       left=0.065, right=0.975, bottom=0.15, top=0.88,
                       wspace=0.36, hspace=0.05)

ax_a = fig.add_subplot(gs[:, 0])  # panel a spans both rows
ax_b = fig.add_subplot(gs[:, 1])  # panel b spans both rows
ax_bar = fig.add_subplot(gs[0, 2])  # regime bar
ax_c = fig.add_subplot(gs[1, 2])   # panel c

# --- Panel (a): Signal Strength S(α) ---
ax = ax_a
ax.plot(alpha, S, color='#2166ac', linewidth=1.8, zorder=3)
ax.set_xlabel(r'Canary fraction $\alpha$')
ax.set_ylabel(r'Signal strength $S(\alpha)$')
ax.set_xlim(0, 1)
ax.set_ylim(-0.05, 1.12)
ax.set_xticks([0, 0.25, 0.50, 0.75, 1.0])
ax.set_yticks([0, 0.25, 0.50, 0.75, 1.0])
ax.text(0.02, 1.03, '(a)', transform=ax.transAxes, fontsize=10, fontweight='bold', va='bottom')

ax.annotate('Signal grows\nwith contamination',
            xy=(0.7, 0.7**0.8), xytext=(0.22, 0.88),
            fontsize=6.5, fontstyle='italic', color='#333333',
            arrowprops=dict(arrowstyle='->', color='#666666', lw=0.7),
            ha='center')

# --- Panel (b): Detection Reliability R(α) ---
ax = ax_b
ax.plot(alpha, R, color='#d6604d', linewidth=1.8, zorder=3)
ax.set_xlabel(r'Canary fraction $\alpha$')
ax.set_ylabel(r'Detection reliability $R(\alpha)$')
ax.set_xlim(0, 1)
ax.set_ylim(-0.05, 1.12)
ax.set_xticks([0, 0.25, 0.50, 0.75, 1.0])
ax.set_yticks([0, 0.25, 0.50, 0.75, 1.0])
ax.text(0.02, 1.03, '(b)', transform=ax.transAxes, fontsize=10, fontweight='bold', va='bottom')

dip_idx = np.argmin(R[250:400]) + 250
dip_alpha = alpha[dip_idx]
dip_R = R[dip_idx]
ax.annotate('Synchronization\ncollapse',
            xy=(dip_alpha, dip_R), xytext=(0.80, 0.22),
            fontsize=6.5, fontstyle='italic', color='#b2182b',
            arrowprops=dict(arrowstyle='->', color='#b2182b', lw=0.7),
            ha='center')

# --- Regime bar above panel (c) ---
ax_bar.set_xlim(0, 1)
ax_bar.set_ylim(0, 1)
ax_bar.axis('off')

for i, (lb, rb) in enumerate(zip(regime_bounds[:-1], regime_bounds[1:])):
    mid = (lb + rb) / 2
    ax_bar.axvspan(lb, rb, ymin=0.15, ymax=0.85,
                   facecolor=regime_colors_bar[i], edgecolor='white',
                   linewidth=1.2, alpha=0.65)
    ax_bar.text(mid, 0.5, regime_labels[i],
                ha='center', va='center', fontsize=5.5, fontweight='semibold',
                color='#111111')

ax_bar.text(-0.07, 0.5, '(c)', fontsize=10, fontweight='bold', va='center',
            transform=ax_bar.transAxes, ha='right')

# --- Panel (c): Detection Rate = S(α) × R(α) ---
ax = ax_c
ymax = detection.max() * 1.12

for i in range(4):
    ax.axvspan(regime_bounds[i], regime_bounds[i+1],
               color=regime_colors_bg[i], alpha=0.5, zorder=0)

for b in regime_bounds[1:-1]:
    ax.axvline(b, color='#aaaaaa', linewidth=0.5, linestyle='--', zorder=1)

ax.plot(alpha, detection, color='#4a1486', linewidth=1.8, zorder=3)
ax.set_xlabel(r'Canary fraction $\alpha$')
ax.set_ylabel(r'Detection rate $S \times R$')
ax.set_xlim(0, 1)
ax.set_ylim(-0.02, ymax)
ax.set_xticks([0, 0.25, 0.50, 0.75, 1.0])

ax.text(0.22, ymax * 0.90, r'$D(\alpha) = S(\alpha) \cdot R(\alpha)$',
        fontsize=7, ha='center', va='top', color='#4a1486',
        bbox=dict(boxstyle='round,pad=0.25', facecolor='white', edgecolor='#4a1486',
                  alpha=0.9, linewidth=0.5))

out_base = '/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/figures/fig_sr_framework'
fig.savefig(f'{out_base}.pdf', dpi=300, bbox_inches='tight')
fig.savefig(f'{out_base}.png', dpi=300, bbox_inches='tight')
plt.close()
print(f'Saved: {out_base}.pdf and .png')
