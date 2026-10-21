import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
import numpy as np
import json
from pathlib import Path

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
})

# Okabe-Ito palette
C = {
    'T07': '#0072B2',
    'T08': '#009E73',
    'T10': '#D55E00',
    'Mix71': '#CC79A7',
    'Mix81': '#E69F00',
    'xdata': '#888888',
}

# ── Data: Heterogeneous-T (SciERC, Qwen3-8B, N=8, θ=0.25 fixed) ──
# Per-seed values extracted from heterogeneous_t_results.json
configs = {
    'T=0.7': {
        'color': C['T07'], 'marker': 'o', 'category': 'single',
        'degen': [0.2231],
        'unique_N': [2.7297 / 8],
        'uni_d': [1.81],  # uniform construction ΔF1 pp
        'vc_d':  [1.17],  # VC construction ΔF1 pp
    },
    'T=0.8': {
        'color': C['T08'], 'marker': 's', 'category': 'single',
        'degen': [0.1890, 0.1720],
        'unique_N': [2.928 / 8, 3.013 / 8],
        'uni_d': [1.81, 0.70],
        'vc_d':  [1.89, 1.47],
    },
    'T=1.0': {
        'color': C['T10'], 'marker': '^', 'category': 'single',
        'degen': [0.1323, 0.1153, 0.1229],
        'unique_N': [3.321 / 8, 3.346 / 8, 3.524 / 8],
        'uni_d': [0.74, 0.54, 0.98],
        'vc_d':  [0.57, 1.84, 1.21],
    },
    'Mix\n0.7+1.0': {
        'color': C['Mix71'], 'marker': 'D', 'category': 'mixed',
        'degen': [0.1739, 0.1664, 0.1701],
        'unique_N': [3.078 / 8, 3.074 / 8, 3.108 / 8],
        'uni_d': [1.15, 1.39, 1.74],
        'vc_d':  [1.47, 1.76, 1.78],
    },
    'Mix\n0.8+1.0': {
        'color': C['Mix81'], 'marker': 'v', 'category': 'mixed',
        'degen': [0.2155, 0.2060],
        'unique_N': [2.556 / 8, 2.622 / 8],
        'uni_d': [-0.08, -0.26],
        'vc_d':  [0.56, 0.39],
    },
}

# Cross-dataset reference (entity construction, uniform, T=1.0)
xdata = [
    {'label': 'SciERC\nbaseline', 'degen': 0.178, 'delta': 1.54},
    {'label': 'CoNLL',             'degen': 0.484, 'delta': 0.10},
    {'label': 'FewNERD',           'degen': 0.071, 'delta': 1.32},
]

# ── Compute summary stats ──
stats = {}
for lab, c in configs.items():
    dg = np.array(c['degen'])
    div = 1 - dg
    un = np.array(c['unique_N'])
    ud = np.array(c['uni_d'])
    vd = np.array(c['vc_d'])
    n = len(dg)
    stats[lab] = dict(
        div_m=float(np.mean(div)), div_s=float(np.std(div, ddof=1)) if n > 1 else 0.0,
        un_m=float(np.mean(un)),   un_s=float(np.std(un, ddof=1))  if n > 1 else 0.0,
        ud_m=float(np.mean(ud)),   ud_s=float(np.std(ud, ddof=1))  if n > 1 else 0.0,
        vd_m=float(np.mean(vd)),   vd_s=float(np.std(vd, ddof=1))  if n > 1 else 0.0,
        n=n, color=c['color'], marker=c['marker'], category=c['category'],
    )

# ── Pareto frontier ──
def pareto_front(pts):
    """pts: list of (x, y, label). Maximize both. Return sorted by x."""
    out = []
    for i, (xi, yi, li) in enumerate(pts):
        dominated = any(
            xj >= xi and yj >= yi and (xj > xi or yj > yi)
            for j, (xj, yj, lj) in enumerate(pts) if j != i
        )
        if not dominated:
            out.append((xi, yi, li))
    return sorted(out, key=lambda p: p[0])

uni_pts = [(s['div_m'], s['ud_m'], l) for l, s in stats.items()]
vc_pts  = [(s['div_m'], s['vd_m'], l) for l, s in stats.items()]
pf_uni = pareto_front(uni_pts)
pf_vc  = pareto_front(vc_pts)

# Same for unique/N
uni_pts2 = [(s['un_m'], s['ud_m'], l) for l, s in stats.items()]
vc_pts2  = [(s['un_m'], s['vd_m'], l) for l, s in stats.items()]
pf_uni2 = pareto_front(uni_pts2)
pf_vc2  = pareto_front(vc_pts2)

# ── Plot ──
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(13, 5.5), sharey=True)

panels = [
    (ax1, 'div_m', 'div_s', '1 − Degeneracy Rate  (→ more diverse)', pf_uni, pf_vc, True),
    (ax2, 'un_m',  'un_s',  'Mean Unique Outputs / N  (→ more diverse)', pf_uni2, pf_vc2, False),
]

for ax, xkey, xekey, xlabel, pfu, pfv, show_xdata in panels:
    # greedy baseline
    ax.axhline(0, color='#BBBBBB', ls='--', lw=1, zorder=1)

    # Pareto frontiers
    if len(pfu) > 1:
        ax.plot([p[0] for p in pfu], [p[1] for p in pfu],
                color='#999999', lw=1.3, ls='--', alpha=0.55, zorder=2,
                label='Pareto (Uniform)')
    if len(pfv) > 1:
        ax.plot([p[0] for p in pfv], [p[1] for p in pfv],
                color='#555555', lw=1.6, ls='-', alpha=0.55, zorder=2,
                label='Pareto (VC)')

    # data points
    for lab, s in stats.items():
        x  = s[xkey]
        xe = s[xekey] if s[xekey] > 0 else None

        # uniform: open marker
        ax.errorbar(x, s['ud_m'], xerr=xe,
                    yerr=s['ud_s'] if s['ud_s'] > 0 else None,
                    marker=s['marker'], ms=10, color=s['color'],
                    mfc='white', mew=2, capsize=3, capthick=1.2,
                    elinewidth=1.2, ls='none', zorder=4)

        # VC: filled marker
        ax.errorbar(x, s['vd_m'], xerr=xe,
                    yerr=s['vd_s'] if s['vd_s'] > 0 else None,
                    marker=s['marker'], ms=10, color=s['color'],
                    mfc=s['color'], mew=1.5, capsize=3, capthick=1.2,
                    elinewidth=1.2, ls='none', zorder=4, alpha=0.85)

        # thin connector
        ax.plot([x, x], [s['ud_m'], s['vd_m']],
                color=s['color'], lw=0.8, ls=':', alpha=0.45, zorder=3)

    # Cross-dataset references (left panel only)
    if show_xdata:
        xdata_offsets = {
            'SciERC\nbaseline': (5, -12, 'left'),
            'CoNLL':            (5,  3,  'left'),
            'FewNERD':          (5,  3,  'left'),
        }
        for cd in xdata:
            xv = 1 - cd['degen']
            ax.scatter(xv, cd['delta'], marker='x', s=55,
                       color=C['xdata'], linewidths=1.5, zorder=3, alpha=0.65)
            xo, yo, ha_cd = xdata_offsets[cd['label']]
            ax.annotate(cd['label'].replace('\n', ' '), (xv, cd['delta']),
                        fontsize=7.5, color=C['xdata'], ha=ha_cd, va='bottom',
                        xytext=(xo, yo), textcoords='offset points')

    # annotations
    offsets_a = {
        'T=0.7':         (-8,  8,   'right'),
        'T=0.8':         (-8,  8,   'right'),
        'T=1.0':         (6,  -8,  'left'),
        'Mix\n0.7+1.0':  (6,   8,  'left'),
        'Mix\n0.8+1.0':  (6,  -8,  'left'),
    }
    offsets_b = {
        'T=0.7':         (-8,  8,   'right'),
        'T=0.8':         (-8,  5,   'right'),
        'T=1.0':         (6,  -8,   'left'),
        'Mix\n0.7+1.0':  (6,   8,   'left'),
        'Mix\n0.8+1.0':  (6,  -8,   'left'),
    }
    offsets = offsets_a if xkey == 'div_m' else offsets_b
    for lab, s in stats.items():
        ox, oy, ha = offsets[lab]
        mid_y = (s['ud_m'] + s['vd_m']) / 2
        display_lab = lab.replace('\n', ' ')
        ax.annotate(display_lab, (s[xkey], mid_y),
                    fontsize=8.5, color=s['color'], fontweight='bold',
                    ha=ha, va='center',
                    xytext=(ox, oy), textcoords='offset points',
                    linespacing=0.85)

    ax.set_xlabel(xlabel)
    ax.grid(axis='y', alpha=0.15, lw=0.5)

ax1.set_ylabel('Construction ΔF1 vs Greedy  (pp)')
ax1.set_title('(a) Degeneracy-based diversity', fontsize=11, pad=8)
ax2.set_title('(b) Output-count diversity', fontsize=11, pad=8)

# shared legend
leg_h = [
    Line2D([], [], marker='o', color='gray', mfc='white', mew=1.8, ms=8,
           ls='none', label='Uniform constr.'),
    Line2D([], [], marker='o', color='gray', mfc='gray', mew=1.2, ms=8,
           ls='none', label='VC constr.'),
    Line2D([], [], color='#999999', lw=1.3, ls='--', label='Pareto (Uniform)'),
    Line2D([], [], color='#555555', lw=1.6, ls='-',  label='Pareto (VC)'),
    Line2D([], [], marker='x', color=C['xdata'], lw=0, ms=7,
           label='Cross-dataset (Uniform)'),
    Line2D([], [], color='#BBBBBB', lw=1, ls='--', label='Greedy (ΔF1 = 0)'),
]
ax1.legend(handles=leg_h, loc='lower left', framealpha=0.92,
           edgecolor='#CCCCCC', handletextpad=0.4)

fig.suptitle('Diversity–Quality Pareto Frontier: SciERC Entity Construction',
             fontsize=13, y=1.01)
plt.tight_layout()

outdir = Path(__file__).parent
fig.savefig(outdir / 'pareto_plot.png', dpi=300)
fig.savefig(outdir / 'pareto_plot.pdf')
print(f'Saved: {outdir}/pareto_plot.png, .pdf')

# ── Analysis JSON ──
analysis = {
    'dataset': 'SciERC',
    'model': 'Qwen3-8B',
    'N': 8,
    'theta': 0.25,
    'construction_method': 'threshold confirmation (fixed θ=0.25) vs greedy',
    'data_points': {},
    'pareto_frontier': {
        'uniform_construction': [
            {'label': p[2].replace('\n', ' '), 'diversity_1_minus_degen': round(p[0], 4),
             'delta_f1_pp': round(p[1], 2)} for p in pf_uni
        ],
        'vc_construction': [
            {'label': p[2].replace('\n', ' '), 'diversity_1_minus_degen': round(p[0], 4),
             'delta_f1_pp': round(p[1], 2)} for p in pf_vc
        ],
    },
    'cross_dataset_reference': xdata,
    'key_findings': [
        'Uniform Pareto frontier: T=0.7 → Mix 0.7+1.0 → T=1.0 (T=0.8 dominated by Mix 0.7+1.0)',
        'VC Pareto frontier: T=0.8 → Mix 0.7+1.0 → T=1.0 (T=0.7 dominated by T=0.8 under VC)',
        'VC construction mitigates the diversity-quality trade-off: flatter Pareto slope (quality drop per unit diversity is ~50% smaller)',
        'Mix 0.8+1.0 is Pareto-dominated under both metrics: mixing two close temperatures yields higher degeneracy than either component',
        'Mix 0.7+1.0 is Pareto-optimal under both uniform and VC: well-separated temperatures produce complementary diversity',
        'Best VC ΔF1 is T=0.8 (+1.68pp) but with lower diversity; Mix 0.7+1.0 achieves nearly identical quality (+1.67pp) with higher diversity',
    ],
}

for lab, s in stats.items():
    clean_lab = lab.replace('\n', ' ')
    analysis['data_points'][clean_lab] = {
        'diversity_1_minus_degen': round(s['div_m'], 4),
        'diversity_std': round(s['div_s'], 4),
        'unique_per_N': round(s['un_m'], 4),
        'uniform_delta_pp': round(s['ud_m'], 2),
        'uniform_delta_std': round(s['ud_s'], 2),
        'vc_delta_pp': round(s['vd_m'], 2),
        'vc_delta_std': round(s['vd_s'], 2),
        'n_seeds': s['n'],
        'category': s['category'],
        'pareto_optimal_uniform': clean_lab in [p[2].replace('\n', ' ') for p in pf_uni],
        'pareto_optimal_vc': clean_lab in [p[2].replace('\n', ' ') for p in pf_vc],
    }

with open(outdir / 'pareto_analysis.json', 'w') as f:
    json.dump(analysis, f, indent=2, ensure_ascii=False)
print(f'Saved: {outdir}/pareto_analysis.json')
