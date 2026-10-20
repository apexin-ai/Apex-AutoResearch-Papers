"""Figure 1: Differential Depth Response (DDR) tri-partition.
Horizontal bar chart of Spearman rho, grouped by DDR zone."""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Patch
import numpy as np

plt.rcParams.update({
    'font.family': 'serif',
    'font.serif': ['DejaVu Serif'],
    'font.size': 8,
    'axes.labelsize': 8,
    'xtick.labelsize': 7,
    'ytick.labelsize': 7,
    'figure.dpi': 300,
    'savefig.dpi': 300,
    'savefig.bbox': 'tight',
    'savefig.pad_inches': 0.03,
    'axes.spines.top': False,
    'axes.spines.right': False,
    'mathtext.fontset': 'cm',
})

C_DRIFT = '#2ca02c'
C_INTERM = '#7b4ea3'
C_STAT = '#d97706'

features_grouped = [
    ('hapax ratio',              -0.647, 'drifting',       0.76),
    ('TTR',                      -0.630, 'drifting',       0.88),
    (r'$\bar{H}$ (entropy mean)',-0.610, 'drifting',       1.17),
    (r'$\sigma_H$ (entropy std)',-0.200, 'intermediate',   0.55),
    (r'$H_{\min}$ (entropy min)$^{\dagger}$',-0.406, 'stationary', 0.03),
    (r'$H_{\max}$ (entropy max)', 0.050, 'stationary',     0.08),
    ('tail decay',               -0.040, 'stationary',     0.08),
]

zone_color = {'drifting': C_DRIFT, 'intermediate': C_INTERM, 'stationary': C_STAT}

n = len(features_grouped)
y_pos = np.arange(n)[::-1]

fig, ax = plt.subplots(figsize=(3.25, 2.5))

for i, (label, rho, zone, d) in enumerate(features_grouped):
    c = zone_color[zone]
    yi = y_pos[i]
    ax.barh(yi, rho, height=0.58, color=c, edgecolor='none', alpha=0.85, zorder=2)
    if abs(rho) >= 0.35:
        ax.text(rho + 0.025, yi, f'{rho:+.2f}', va='center', ha='left',
                fontsize=6, color='#333', fontweight='bold')
    elif rho < 0:
        ax.text(rho - 0.015, yi, f'{rho:+.2f}', va='center', ha='right',
                fontsize=6, color='#333')
    else:
        ax.text(rho + 0.015, yi, f'{rho:+.2f}', va='center', ha='left',
                fontsize=6, color='#333')

ax.axvline(0, color='#aaa', linewidth=0.4, zorder=1)

sep_y_1 = y_pos[2] - 0.45
sep_y_2 = y_pos[3] - 0.45
ax.axhline(sep_y_1, color='#ccc', linewidth=0.5, linestyle='--', zorder=1)
ax.axhline(sep_y_2, color='#ccc', linewidth=0.5, linestyle='--', zorder=1)

ax.set_yticks(y_pos)
ax.set_yticklabels([f[0] for f in features_grouped], fontsize=6.5)
ax.set_xlabel(r'Spearman $\rho$ with generation depth', fontsize=7.5)
ax.set_xlim(-0.82, 0.28)
ax.set_ylim(-0.6, n - 0.4)
ax.tick_params(axis='y', length=0)
ax.spines['left'].set_visible(False)
ax.spines['bottom'].set_color('#999')
ax.spines['bottom'].set_linewidth(0.5)

zone_mid = {
    'drifting': (y_pos[0] + y_pos[2]) / 2,
    'intermediate': y_pos[3],
    'stationary': (y_pos[4] + y_pos[6]) / 2,
}
zone_labels = {
    'drifting': ('Drifting', r'$|\rho|>0.6$'),
    'intermediate': ('Intermediate', r'$|\rho|\approx 0.2$'),
    'stationary': ('Near-stationary', r'$|\rho|<0.1^{\dagger}$'),
}
for zone, ym in zone_mid.items():
    lbl, sub = zone_labels[zone]
    ax.text(0.24, ym + 0.12, lbl, fontsize=5.5, color=zone_color[zone],
            fontweight='bold', va='bottom', ha='right')
    ax.text(0.24, ym - 0.12, sub, fontsize=5, color=zone_color[zone],
            va='top', ha='right')

plt.tight_layout()

out = '/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/chart'
fig.savefig(f'{out}/fig1_differential_response.pdf', format='pdf')
fig.savefig(f'{out}/fig1_differential_response.png', format='png')
print(f'Saved fig1 to {out}/')
