#!/usr/bin/env python3
"""Figure 1 (DDR bar chart): Spearman rho per feature, grouped by drift category.
Fixes: correct categorization (entropy_std→Moderate, not Near-stationary),
uses class-balanced rho values consistent with DDR trends appendix figure."""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patheffects as pe
import numpy as np

plt.rcParams.update({
    'font.family': 'serif',
    'font.serif': ['Times New Roman', 'DejaVu Serif', 'Nimbus Roman'],
    'font.size': 8,
    'axes.labelsize': 9,
    'axes.titlesize': 9,
    'xtick.labelsize': 7,
    'ytick.labelsize': 7,
    'legend.fontsize': 6,
    'figure.dpi': 300,
    'savefig.dpi': 300,
    'savefig.bbox': 'tight',
    'savefig.pad_inches': 0.05,
    'axes.spines.top': False,
    'axes.spines.right': False,
    'axes.grid': False,
    'mathtext.fontset': 'cm',
    'pdf.fonttype': 42,
    'ps.fonttype': 42,
})

# --- Class-balanced Spearman rho (from DDR trends appendix) ---
# Ordered: drifting | moderate | near-stationary
features = [
    ('Hapax\nRatio', -0.640, 'drifting'),
    ('TTR',          -0.625, 'drifting'),
    (r'$\bar{H}$',  -0.598, 'drifting'),
    (r'$H_{\min}$', -0.404, 'moderate'),
    (r'$\sigma_H$', -0.157, 'moderate'),
    (r'$H_{\max}$',  0.061, 'stationary'),
    ('Tail\nDec.',   -0.041, 'stationary'),
]

names = [f[0] for f in features]
rhos  = [f[1] for f in features]
cats  = [f[2] for f in features]

# Zone colors (semantic)
ZONE = {
    'drifting':   {'bar': '#2166AC', 'bg': '#2166AC', 'label': 'Drifting'},
    'moderate':   {'bar': '#666666', 'bg': '#666666', 'label': 'Moderate'},
    'stationary': {'bar': '#B2182B', 'bg': '#B2182B', 'label': 'Near-stationary'},
}

x = np.arange(len(features))
fig, ax = plt.subplots(figsize=(3.25, 2.6))

# --- Background bands (Pattern A) ---
# Near-stationary zone: |rho| < 0.10
ax.axhspan(-0.10, 0.10, color='#f0f0f0', alpha=0.8, zorder=0)
ax.text(6.45, 0.065, r'$|\rho|<0.10$', fontsize=4.5, color='#aaaaaa',
        ha='right', va='center', fontstyle='italic')

# Threshold lines
ax.axhline(0, color='black', linewidth=0.4, zorder=1)
ax.axhline(-0.10, color='#cccccc', linewidth=0.4, linestyle='--', zorder=1)
ax.axhline(0.10, color='#cccccc', linewidth=0.4, linestyle='--', zorder=1)

# --- Bars ---
bar_colors = [ZONE[c]['bar'] for c in cats]
bars = ax.bar(x, rhos, width=0.6, color=bar_colors, alpha=0.85, zorder=2,
              edgecolor='white', linewidth=0.3)

# Hatching for near-stationary bars
for i, cat in enumerate(cats):
    if cat == 'stationary':
        bars[i].set_hatch('///')
        bars[i].set_edgecolor(ZONE[cat]['bar'])
        bars[i].set_linewidth(0.3)

# --- Value labels ---
for i, (name, rho, cat) in enumerate(features):
    offset = -0.03 if rho < 0 else 0.02
    va = 'top' if rho < 0 else 'bottom'
    if abs(rho) < 0.12:
        offset = 0.025 if rho > 0 else -0.025
    label = f'{rho:+.3f}' if abs(rho) >= 0.1 else f'{rho:+.3f}'
    t = ax.text(i, rho + offset, label, ha='center', va=va,
                fontsize=5.5, color=ZONE[cat]['bar'], fontweight='bold')
    t.set_path_effects([pe.withStroke(linewidth=2, foreground='white')])

# --- Bracket annotations ---
bracket_y = 0.22
tick_len = 0.015

def draw_bracket(ax, x_left, x_right, y, color, name, rho_range):
    ax.plot([x_left, x_left, x_right, x_right],
            [y - tick_len, y, y, y - tick_len],
            color=color, lw=0.8, clip_on=False, solid_capstyle='butt')
    cx = (x_left + x_right) / 2
    ax.text(cx, y + 0.01, name,
            fontsize=5.5, fontstyle='italic', fontweight='bold', color=color,
            ha='center', va='bottom', clip_on=False)
    ax.text(cx, y + 0.065, rho_range,
            fontsize=4.5, color=color,
            ha='center', va='bottom', clip_on=False)

draw_bracket(ax, -0.35, 2.35, bracket_y, ZONE['drifting']['bar'],
             'Drifting', r'$|\rho|>0.60$')
draw_bracket(ax, 2.65, 4.35, bracket_y, ZONE['moderate']['bar'],
             'Moderate', r'$|\rho|\approx 0.2$–$0.4$')
draw_bracket(ax, 4.65, 6.35, bracket_y, ZONE['stationary']['bar'],
             'Near-stationary', r'$|\rho|<0.10$')

# --- Axes ---
ax.set_xticks(x)
ax.set_xticklabels(names, fontsize=7)
ax.set_ylabel(r"Spearman $\rho$ with Depth", fontsize=8)
ax.set_ylim(-0.72, 0.35)
ax.set_xlim(-0.5, 6.5)

plt.tight_layout()
fig.savefig('fig1_differential_response.pdf', facecolor='white')
fig.savefig('fig1_differential_response.png', dpi=300, facecolor='white')
print('Saved fig1_differential_response.{pdf,png}')
plt.close()
