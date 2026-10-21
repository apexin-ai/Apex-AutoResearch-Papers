"""DDR (ρ, d) scatter plot: 7 features in Spearman ρ × Cohen's d space.
Three-cluster structure: drifting / intermediate / near-stationary."""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams.update({
    'font.family': 'serif',
    'font.serif': ['DejaVu Serif'],
    'font.size': 8,
    'axes.labelsize': 9,
    'xtick.labelsize': 7.5,
    'ytick.labelsize': 7.5,
    'figure.dpi': 300,
    'savefig.dpi': 300,
    'savefig.bbox': 'tight',
    'savefig.pad_inches': 0.05,
    'axes.spines.top': False,
    'axes.spines.right': False,
    'mathtext.fontset': 'cm',
})

C_DRIFT = '#2ca02c'
C_INTERM = '#7b4ea3'
C_STAT = '#d97706'

features = [
    ('hapax ratio',    0.64, 0.76, 'drifting',      'o'),
    ('TTR',            0.63, 0.88, 'drifting',      'o'),
    (r'$\bar{H}$',    0.60, 1.17, 'drifting',      'o'),
    (r'$\sigma_H$',   0.16, 0.55, 'intermediate',  's'),
    (r'$H_{\min}$',   0.40, 0.03, 'stationary',    'D'),
    (r'$H_{\max}$',   0.05, 0.08, 'stationary',    'o'),
    ('tail decay',     0.04, 0.08, 'stationary',    'o'),
]

zone_color = {'drifting': C_DRIFT, 'intermediate': C_INTERM, 'stationary': C_STAT}
zone_label = {'drifting': 'Drifting', 'intermediate': 'Intermediate', 'stationary': 'Near-stationary'}

fig, ax = plt.subplots(figsize=(3.25, 2.8))

for name, rho_abs, d, zone, marker in features:
    c = zone_color[zone]
    ms = 55 if marker == 'D' else 50
    edge = 'white' if marker != 'D' else c
    ax.scatter(rho_abs, d, c=c, marker=marker, s=ms, zorder=5,
               edgecolors=edge, linewidths=0.5)

offsets = {
    'hapax ratio':  (-0.02, -0.09),
    'TTR':          (0.02,   0.05),
    r'$\bar{H}$':  (-0.02,  0.06),
    r'$\sigma_H$': (0.02,   0.04),
    r'$H_{\min}$': (0.02,   0.05),
    r'$H_{\max}$': (0.02,   0.04),
    'tail decay':   (0.02,  -0.06),
}
align_override = {
    'hapax ratio': ('right', 'top'),
}

for name, rho_abs, d, zone, marker in features:
    dx, dy = offsets[name]
    suffix = r'$^{\dagger}$' if name == r'$H_{\min}$' else ''
    ha_def = 'left' if dx >= 0 else 'right'
    va_def = 'bottom' if dy >= 0 else 'top'
    if name in align_override:
        ha_def, va_def = align_override[name]
    ax.annotate(name + suffix, (rho_abs, d),
                xytext=(rho_abs + dx, d + dy),
                fontsize=6.5, color=zone_color[zone],
                ha=ha_def, va=va_def)

ax.axhline(y=0.20, color='gray', ls=':', lw=0.6, alpha=0.5, zorder=1)
ax.axvline(x=0.30, color='gray', ls=':', lw=0.6, alpha=0.5, zorder=1)
ax.text(0.31, 0.18, r'$d=0.20$', fontsize=5.5, color='gray', alpha=0.7, va='top')
ax.text(0.315, 1.22, r'$|\rho|=0.30$', fontsize=5.5, color='gray', alpha=0.7,
        va='top')

from matplotlib.lines import Line2D
legend_elements = [
    Line2D([0], [0], marker='o', color='w', markerfacecolor=C_DRIFT,
           markersize=6, label='Drifting'),
    Line2D([0], [0], marker='s', color='w', markerfacecolor=C_INTERM,
           markersize=6, label='Intermediate'),
    Line2D([0], [0], marker='o', color='w', markerfacecolor=C_STAT,
           markersize=6, label='Near-stationary'),
    Line2D([0], [0], marker='D', color='w', markerfacecolor=C_STAT,
           markeredgecolor=C_STAT, markersize=5,
           label=r'$H_{\min}$ (pooled $\rho$, gen-1/2+ $d$)'),
]
ax.legend(handles=legend_elements, fontsize=5.5, loc='upper left',
          frameon=True, framealpha=0.85, edgecolor='#cccccc',
          borderpad=0.4, handletextpad=0.4)

ax.set_xlabel(r'$|\rho|$ (Spearman, pooled class-balanced)')
ax.set_ylabel(r"Cohen's $d$ (gen-1 vs. gen-2+)")
ax.set_xlim(-0.02, 0.72)
ax.set_ylim(-0.08, 1.30)

out_dir = '/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/chart'
fig.savefig(f'{out_dir}/fig_ddr_scatter.pdf')
fig.savefig(f'{out_dir}/fig_ddr_scatter.png')
plt.close()
print('Saved fig_ddr_scatter.pdf + .png')
