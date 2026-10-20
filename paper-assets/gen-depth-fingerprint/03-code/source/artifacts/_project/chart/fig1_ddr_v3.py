"""Figure 1: Differential Depth Response — redesigned as strip/forest plot.
Wong colorblind-safe palette, diamond grand means, per-generator dots."""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
import json

# ── Data ──
with open('/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/rebuttal/spearman_per_generator.json') as f:
    data = json.load(f)

features = [
    ('hapax_ratio',   r'Hapax ratio',                      'drifting',     0.76),
    ('ttr',           r'TTR',                               'drifting',     0.88),
    ('entropy_mean',  r'$\bar{H}$ (entropy mean)',          'drifting',     1.17),
    ('entropy_std',   r'$\sigma_H$ (entropy std)',          'intermediate', 0.55),
    ('entropy_min',   r'$H_{\min}$ (entropy min)',          'near-stat',    0.016),
    ('entropy_max',   r'$H_{\max}$ (entropy max)',          'near-stat',    0.08),
    ('tail_decay',    r'Tail decay',                        'near-stat',    0.08),
]

generators = list(data.keys())
gen_short = ['Py-1B', 'Py-2.8B', 'OLMo', 'Qw-0.6B', 'Qw-1.7B', 'Qw-8B', 'Llama', 'Mistral']

# ── Style ── Unified DDR palette
C_DRIFT  = '#D6604D'   # warm red
C_INTERM = '#7570B3'   # muted purple
C_STAT   = '#4393C3'   # cool blue
C_BG_DRIFT  = '#D6604D'
C_BG_INTERM = '#7570B3'
C_BG_STAT   = '#4393C3'

zone_color = {'drifting': C_DRIFT, 'intermediate': C_INTERM, 'near-stat': C_STAT}

plt.rcParams.update({
    'font.family': 'serif',
    'font.serif': ['DejaVu Serif'],
    'font.size': 8,
    'axes.labelsize': 9,
    'xtick.labelsize': 7.5,
    'ytick.labelsize': 8,
    'figure.dpi': 300,
    'savefig.dpi': 300,
    'savefig.bbox': 'tight',
    'savefig.pad_inches': 0.04,
    'mathtext.fontset': 'cm',
})

n = len(features)
y_pos = np.arange(n)[::-1]

fig, ax = plt.subplots(figsize=(3.25, 2.6))

# ── Zone background shading ──
# Order: [0]=hapax, [1]=TTR, [2]=ent_mean, [3]=ent_std, [4]=ent_min, [5]=ent_max, [6]=tail
zone_ranges = {
    'drifting':     (y_pos[2] - 0.42, y_pos[0] + 0.42),
    'intermediate': (y_pos[3] - 0.42, y_pos[3] + 0.42),
    'near-stat':    (y_pos[6] - 0.42, y_pos[4] + 0.42),
}
for zone, (ylo, yhi) in zone_ranges.items():
    ax.axhspan(ylo, yhi, color=zone_color[zone], alpha=0.045, zorder=0)

# ── Separator lines between zones ──
sep1 = (y_pos[2] + y_pos[3]) / 2
sep2 = (y_pos[3] + y_pos[4]) / 2
ax.axhline(sep1, color='#cccccc', linewidth=0.5, linestyle='-', zorder=1)
ax.axhline(sep2, color='#cccccc', linewidth=0.5, linestyle='-', zorder=1)

# ── Zero line ──
ax.axvline(0, color='#bbbbbb', linewidth=0.6, linestyle='-', zorder=1)

# ── Per-generator dots + grand mean diamond ──
gen_markers = ['o', 's', '^', 'D', 'v', 'P', 'X', '*']
np.random.seed(42)

for i, (feat_key, label, zone, d_val) in enumerate(features):
    yi = y_pos[i]
    c = zone_color[zone]

    vals = [data[g][feat_key] for g in generators]
    grand_mean = np.mean(vals)

    jitter = np.linspace(-0.18, 0.18, len(vals))

    for j, (v, gm) in enumerate(zip(vals, gen_markers)):
        ax.scatter(v, yi + jitter[j], marker='o', s=12,
                   color=c, alpha=0.40, edgecolors='none', zorder=3,
                   linewidths=0)

    # Grand mean: diamond marker with white edge
    ax.scatter(grand_mean, yi, marker='D', s=45, color=c,
               edgecolors='white', linewidths=0.7, zorder=5)

    # Thin connecting line from min to max (range)
    ax.plot([min(vals), max(vals)], [yi, yi],
            color=c, linewidth=0.9, alpha=0.30, zorder=2, solid_capstyle='round')

# ── Y-axis labels ──
ax.set_yticks(y_pos)
ax.set_yticklabels([f[1] for f in features], fontsize=7)

# ── X-axis ──
ax.set_xlabel(r'Spearman $\rho$ with generation depth', fontsize=8)
ax.set_xlim(-0.82, 0.22)
ax.set_ylim(-0.55, n - 0.45)

# ── Axis styling ──
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.spines['bottom'].set_color('#999999')
ax.spines['bottom'].set_linewidth(0.5)
ax.tick_params(axis='y', length=0)
ax.tick_params(axis='x', length=3, width=0.5, color='#999999')

# ── Zone labels on right margin ──
zone_info = [
    ('drifting',     (y_pos[0] + y_pos[2]) / 2,  'Drifting',         r'$d = 0.76$–$1.17$'),
    ('intermediate', y_pos[3],                     'Intermediate',     r'$d = 0.55$'),
    ('near-stat',    (y_pos[4] + y_pos[6]) / 2,   'Near-stationary',  r'$d < 0.10$'),
]
for zone, ym, lbl, sub in zone_info:
    ax.text(0.20, ym + 0.15, lbl, fontsize=5.5, color=zone_color[zone],
            fontweight='bold', va='bottom', ha='right', style='italic')
    ax.text(0.20, ym - 0.15, sub, fontsize=5, color=zone_color[zone],
            va='top', ha='right')

# ── Legend ──
legend_elements = [
    plt.scatter([], [], marker='o', s=14, color='#666', alpha=0.5,
                edgecolors='none', label='Per-generator'),
    plt.scatter([], [], marker='D', s=50, color='#666',
                edgecolors='white', linewidths=0.8, label='Grand mean'),
]
leg = ax.legend(handles=legend_elements, loc='lower left',
                fontsize=5.5, frameon=True, framealpha=0.9,
                edgecolor='#dddddd', fancybox=False,
                handletextpad=0.3, borderpad=0.4,
                bbox_to_anchor=(0.0, 0.0))
leg.get_frame().set_linewidth(0.4)

plt.tight_layout()

out = '/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/chart'
fig.savefig(f'{out}/fig1_differential_response.pdf', format='pdf')
fig.savefig(f'{out}/fig1_differential_response.png', format='png')
print(f'Saved to {out}/')
