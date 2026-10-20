import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

plt.rcParams.update({
    'font.family': 'DejaVu Sans',
    'font.size': 11,
    'axes.titlesize': 13,
    'axes.labelsize': 12,
    'xtick.labelsize': 10,
    'ytick.labelsize': 10,
    'legend.fontsize': 10,
    'figure.dpi': 300,
    'savefig.dpi': 300,
    'savefig.bbox': 'tight',
    'savefig.pad_inches': 0.05,
    'axes.spines.top': False,
    'axes.spines.right': False,
    'lines.linewidth': 1.8,
})

generations = [0, 1, 2]

curated = {
    'C1: LoRA K=4':      [107.54, 106.73, 107.25],
    'C2: LoRA K=8':      [107.21, 107.26, 107.25],
    'C3: Full-FT lr=5e-6': [107.10, 107.61, 108.07],
    'C4: Full-FT lr=2e-5': [107.81, 108.03, 108.54],
    'C8: Full-FT K=16':   [107.32, 106.73, 107.11],
}

random_bl = {
    'C5: LoRA K=4':        [105.42, 108.21, 108.72],
    'C6: Full-FT lr=5e-6': [107.17, 107.87, 108.64],
    'C7: Full-FT lr=2e-5': [108.08, 107.85, 108.13],
}

# Okabe-Ito colors for curated
curated_styles = {
    'C1: LoRA K=4':        dict(color='#E69F00', marker='o', ms=5, lw=1.8),
    'C2: LoRA K=8':        dict(color='#56B4E9', marker='o', ms=5, lw=1.8),
    'C3: Full-FT lr=5e-6': dict(color='#009E73', marker='o', ms=5, lw=1.8),
    'C4: Full-FT lr=2e-5': dict(color='#0072B2', marker='o', ms=5, lw=1.8),
    'C8: Full-FT K=16':    dict(color='#D55E00', marker='^', ms=7, lw=2.2),
}

# Gray shades for random baselines
gray_shades = ['#888888', '#AAAAAA', '#666666']
random_styles = {}
for i, k in enumerate(random_bl):
    random_styles[k] = dict(color=gray_shades[i], marker='s', ms=5, lw=1.5)

fig, ax = plt.subplots(figsize=(6.5, 4.2))

# ±1% band centered at 107.4
band_center = 107.4
band_lo = band_center * 0.99
band_hi = band_center * 1.01
ax.axhspan(band_lo, band_hi, color='#CCCCCC', alpha=0.25, zorder=0)
ax.text(2.03, band_center, f'±1% of mean init ({band_center:.1f})',
        va='center', ha='left', fontsize=8.5, color='#888888')

# Plot curated (solid)
for label, vals in curated.items():
    s = curated_styles[label]
    ax.plot(generations, vals, '-', color=s['color'], marker=s['marker'],
            markersize=s['ms'], linewidth=s['lw'], label=label, zorder=3)

# Plot random baselines (dashed)
for label, vals in random_bl.items():
    s = random_styles[label]
    ax.plot(generations, vals, '--', color=s['color'], marker=s['marker'],
            markersize=s['ms'], linewidth=s['lw'], label=label, zorder=2)

# Grid
ax.grid(True, color='#CCCCCC', linestyle='--', alpha=0.3, zorder=0)

ax.set_xlabel('Generation')
ax.set_ylabel('Vendi Score')
ax.set_xticks([0, 1, 2])
ax.set_ylim(104.5, 109.5)
ax.set_xlim(-0.1, 2.35)

# Build grouped legend
curated_handles = []
random_handles = []
for label in curated:
    s = curated_styles[label]
    h = plt.Line2D([0], [0], color=s['color'], marker=s['marker'],
                   markersize=s['ms'], linewidth=s['lw'], linestyle='-', label=label)
    curated_handles.append(h)
for label in random_bl:
    s = random_styles[label]
    h = plt.Line2D([0], [0], color=s['color'], marker=s['marker'],
                   markersize=s['ms'], linewidth=s['lw'], linestyle='--', label=label)
    random_handles.append(h)

curated_title = mpatches.Patch(color='none', label='Curated (ArmoRM top-1)')
random_title = mpatches.Patch(color='none', label='Random baseline')

all_handles = [curated_title] + curated_handles + [random_title] + random_handles
all_labels = [h.get_label() for h in all_handles]

ax.legend(handles=all_handles, labels=all_labels, loc='upper left',
          fontsize=9, framealpha=0.9, edgecolor='#CCCCCC')

plt.tight_layout()

outdir = '/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/collapse_aware_reward_rebalancing/artifacts/figures/paper'
fig.savefig(f'{outdir}/fig2_vendi_trajectories.pdf')
fig.savefig(f'{outdir}/fig2_vendi_trajectories.png')
plt.close()
print('Done: PDF + PNG saved')
