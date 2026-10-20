"""Figure 1: Differential Depth Response — vertical strip plot.
Wong colorblind-safe palette, per-feature marker shapes, diamond grand means."""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import json

matplotlib.rcParams['pdf.fonttype'] = 42
matplotlib.rcParams['ps.fonttype'] = 42

# ── Data ──
with open('/root/gen-depth-fingerprint/spearman_per_generator.json') as f:
    data = json.load(f)

# Feature order: user-specified |rho| descending
features = [
    ('hapax_ratio',  'Hapax\nratio',  'drifting',     'o'),
    ('ttr',          'TTR',           'drifting',     's'),
    ('entropy_mean', r'$\bar{H}$',   'drifting',     '^'),
    ('entropy_std',  r'$\sigma_H$',  'intermediate', 'D'),
    ('entropy_min',  r'$H_{\min}$',  'near-stat',    'v'),
    ('entropy_max',  r'$H_{\max}$',  'near-stat',    'h'),
    ('tail_decay',   'Tail\ndecay',  'near-stat',    'p'),
]

generators = list(data.keys())
n = len(features)
x_pos = np.arange(n)

# ── Colors (Wong / Tol colorblind-safe) ──
C_DRIFT  = '#0072B2'
C_INTERM = '#882255'
C_STAT   = '#E69F00'
zone_color = {'drifting': C_DRIFT, 'intermediate': C_INTERM, 'near-stat': C_STAT}

plt.rcParams.update({
    'font.family': 'serif',
    'font.serif': ['DejaVu Serif'],
    'font.size': 8,
    'axes.labelsize': 9,
    'xtick.labelsize': 7,
    'ytick.labelsize': 8,
    'figure.dpi': 300,
    'savefig.dpi': 300,
    'savefig.bbox': 'tight',
    'savefig.pad_inches': 0.04,
    'mathtext.fontset': 'cm',
})

fig, ax = plt.subplots(figsize=(3.25, 2.6))

# ── Zone background shading (vertical bands) ──
ax.axvspan(-0.42, 2.42, color=C_DRIFT,  alpha=0.045, zorder=0)
ax.axvspan(2.58,  3.42, color=C_INTERM, alpha=0.045, zorder=0)
ax.axvspan(3.58,  6.42, color=C_STAT,   alpha=0.045, zorder=0)

# ── Separator lines between zones ──
ax.axvline(2.5, color='#cccccc', linewidth=0.5, zorder=1)
ax.axvline(3.5, color='#cccccc', linewidth=0.5, zorder=1)

# ── Horizontal zero line ──
ax.axhline(0, color='#bbbbbb', linewidth=0.6, zorder=1)

# ── Per-generator dots + grand mean ──
for i, (feat_key, label, zone, mkr) in enumerate(features):
    xi = x_pos[i]
    c = zone_color[zone]

    vals = [data[g][feat_key] for g in generators]
    grand_mean = np.mean(vals)

    # Horizontal jitter for per-generator dots
    jitter = np.linspace(-0.20, 0.20, len(vals))

    for j, v in enumerate(vals):
        ax.scatter(xi + jitter[j], v, marker=mkr, s=12,
                   color=c, alpha=0.40, edgecolors='none', zorder=3)

    # Thin range line (min to max)
    ax.plot([xi, xi], [min(vals), max(vals)],
            color=c, linewidth=0.9, alpha=0.30, zorder=2, solid_capstyle='round')

    # Grand mean: diamond
    ax.scatter(xi, grand_mean, marker='D', s=45, color=c,
               edgecolors='white', linewidths=0.7, zorder=5)

# ── X-axis ──
ax.set_xticks(x_pos)
ax.set_xticklabels([f[1] for f in features], fontsize=6.5)

# ── Y-axis ──
ax.set_ylabel(r'Spearman $\rho$ with generation depth', fontsize=8)
ax.set_xlim(-0.55, n - 0.45)
ax.set_ylim(-0.82, 0.25)

# ── Axis styling ──
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['bottom'].set_visible(False)
ax.spines['left'].set_color('#999999')
ax.spines['left'].set_linewidth(0.5)
ax.tick_params(axis='x', length=0)
ax.tick_params(axis='y', length=3, width=0.5, color='#999999')

# ── Zone labels at top ──
zone_labels = [
    ('drifting',     1.0, 'Drifting',        r'$d\!=\!0.76$--$1.17$'),
    ('intermediate', 3.0, 'Intermediate',    r'$d\!=\!0.55$'),
    ('near-stat',    5.0, 'Near-stationary', r'$d\!<\!0.10$'),
]
for zone, xm, lbl, sub in zone_labels:
    ax.text(xm, 0.245, lbl, fontsize=5.5, color=zone_color[zone],
            fontweight='bold', va='bottom', ha='center', style='italic',
            transform=ax.transData, clip_on=False)
    ax.text(xm, 0.20, sub, fontsize=5, color=zone_color[zone],
            va='top', ha='center')

# ── Legend ──
legend_elements = [
    plt.scatter([], [], marker='o', s=14, color='#666', alpha=0.5,
                edgecolors='none', label='Per-generator'),
    plt.scatter([], [], marker='D', s=50, color='#666',
                edgecolors='white', linewidths=0.8, label='Grand mean'),
]
leg = ax.legend(handles=legend_elements, loc='lower right',
                fontsize=5.5, frameon=True, framealpha=0.9,
                edgecolor='#dddddd', fancybox=False,
                handletextpad=0.3, borderpad=0.4)
leg.get_frame().set_linewidth(0.4)

plt.tight_layout()

out = '/root/gen-depth-fingerprint'
fig.savefig(f'{out}/fig1_differential_response.pdf', format='pdf')
fig.savefig(f'{out}/fig1_differential_response.png', format='png')
print('Saved to', out)
