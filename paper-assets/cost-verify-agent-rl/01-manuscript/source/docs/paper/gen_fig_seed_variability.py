import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
import os

PAPER_DIR = os.path.dirname(os.path.abspath(__file__))

# --- Unified palette (D143 color unification) ---
C_BASELINE  = '#4477AA'   # blue
C_TREATMENT = '#EE7733'   # orange
C_COLLAPSE  = '#4477AA'   # blue — Collapsed
C_SAFE      = '#228833'   # green — Generalized
C_NEUTRAL   = '#808080'   # gray

# --- Unified rcParams ---
plt.rcParams.update({
    'font.family': 'DejaVu Sans',
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
    'lines.linewidth': 1.8,
    'pdf.fonttype': 42,
    'ps.fonttype': 42,
    'mathtext.fontset': 'dejavuserif',
})

# --- Data from Table 2 (sorted by OOD % descending within each category) ---
seeds_data = [
    # (name, category, ood_pct, ci_lo, ci_hi)
    ('seed 4',    'G', 30.60, 23.5, 38.7),
    ('seed 6',    'G', 29.10, 22.1, 37.3),
    ('seed 5',    'G', 29.10, 22.1, 37.3),
    ('seed 1',    'G', 23.88, 17.4, 31.8),
    ('seed 2',    'S', 15.67, 10.5, 22.8),
    ('seed 100',  'S', 12.69,  8.0, 19.4),
    ('seed 300',  'S', 10.45,  6.3, 16.8),
    ('seed 200',  'S', 10.45,  6.3, 16.8),
    ('seed 42',   'C', 12.69,  8.0, 19.4),
    ('seed 8',    'C', 11.94,  7.5, 18.5),
    ('seed 2048', 'C',  8.21,  4.6, 14.2),
]

# Category config
CAT_CONFIG = {
    'G': {'color': C_SAFE,      'marker': 'o', 'label': 'Generalized', 'bg': '#E8F5E9'},
    'S': {'color': C_TREATMENT, 'marker': 'o', 'label': 'Stagnant',    'bg': '#FFF3E0'},
    'C': {'color': C_COLLAPSE,  'marker': 'X', 'label': 'Collapsed',   'bg': '#E3EEF9'},
}

n = len(seeds_data)
fig, ax = plt.subplots(figsize=(3.5, 3.0))

# --- Background bands per category group ---
# Find y-index ranges for each category
y_positions = list(range(n))
cat_ranges = {}
for i, (_, cat, *_) in enumerate(seeds_data):
    if cat not in cat_ranges:
        cat_ranges[cat] = [i, i]
    else:
        cat_ranges[cat][1] = i

for cat, (y_start, y_end) in cat_ranges.items():
    bg = CAT_CONFIG[cat]['bg']
    ax.axhspan(y_start - 0.45, y_end + 0.45, color=bg, alpha=0.35, zorder=0, linewidth=0)

# --- Plot data points and CIs ---
for i, (name, cat, ood, ci_lo, ci_hi) in enumerate(seeds_data):
    cfg = CAT_CONFIG[cat]
    color = cfg['color']
    marker = cfg['marker']
    ms = 5.5 if marker == 'o' else 6.5

    # CI error bar
    ax.plot([ci_lo, ci_hi], [i, i], color=color, linewidth=1.2, zorder=2, solid_capstyle='round')

    # Marker
    ax.plot(ood, i, marker=marker, color=color, markersize=ms, zorder=4,
            markeredgecolor='white', markeredgewidth=0.6)

# --- SFT baseline ---
sft_baseline = 6.72
ax.axvline(x=sft_baseline, color=C_NEUTRAL, linestyle='--', linewidth=1.0, zorder=1)
sft_line = plt.Line2D([], [], color=C_NEUTRAL, linestyle='--', linewidth=1.0,
                       label='SFT baseline (6.7%)')
ax.legend(handles=[sft_line], loc='lower right', fontsize=7.5,
          frameon=False, borderpad=0.3, bbox_to_anchor=(0.98, 0.02))

# --- Category labels on right side ---
for cat, (y_start, y_end) in cat_ranges.items():
    cfg = CAT_CONFIG[cat]
    y_mid = (y_start + y_end) / 2
    count = y_end - y_start + 1
    ax.text(41, y_mid, f'{cfg["label"]}\n({count}/11)',
            fontsize=7, color=cfg['color'], ha='left', va='center',
            fontweight='bold', linespacing=0.85)

# --- Axes ---
ax.set_yticks(range(n))
ax.set_yticklabels([d[0] for d in seeds_data], fontsize=8)
ax.set_xlabel('OOD Success Rate (%)')
ax.set_xlim(0, 42)
ax.set_ylim(n - 0.6, -0.6)  # Inverted so highest OOD is at top
ax.tick_params(axis='y', length=0, pad=4)  # Remove y-tick marks

# No grid
ax.grid(False)

plt.tight_layout(pad=0.4)
fig.savefig(os.path.join(PAPER_DIR, 'fig_seed_variability.pdf'))
fig.savefig(os.path.join(PAPER_DIR, 'fig_seed_variability.png'))
print('Saved fig_seed_variability.pdf and .png')
