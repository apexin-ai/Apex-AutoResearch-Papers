"""
Grouped bar chart: method sensitivity across contamination levels.
Replaces Table 1 in main text.
narrative_intent: "Different statistical methods yield dramatically different
conclusions on the same data — making method choice a first-order concern."
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib.patheffects as pe
import numpy as np

plt.rcParams.update({
    'font.family': 'DejaVu Sans',
    'font.size': 9,
    'axes.titlesize': 10,
    'axes.labelsize': 9,
    'xtick.labelsize': 8,
    'ytick.labelsize': 8,
    'legend.fontsize': 7.5,
    'figure.dpi': 300,
    'savefig.dpi': 300,
    'savefig.bbox': 'tight',
    'savefig.pad_inches': 0.02,
    'axes.spines.top': False,
    'axes.spines.right': False,
    'pdf.fonttype': 42,
    'ps.fonttype': 42,
    'lines.linewidth': 1.8,
})

# ── Data ──
alpha_labels = [r'$\alpha{=}0$', r'$\alpha{=}.25$', r'$\alpha{=}.50$',
                r'$\alpha{=}.75$', r'$\alpha{=}1$']
methods = ['Naive XCorr', 'Diff. XCorr', r'Threshold ($3\sigma$)',
           'Perm. Granger', 'Toda–Yamamoto']

data = {
    'Naive XCorr':            [25.0, 12.5, 37.5, 87.5, 87.5],
    'Diff. XCorr':            [50.0, 12.5, 75.0, 75.0, 75.0],
    r'Threshold ($3\sigma$)': [37.5, 0.0,  50.0, 0.0,  25.0],
    'Perm. Granger':          [0.0,  0.0,  75.0, 75.0, 75.0],
    'Toda–Yamamoto':          [25.0, 12.5, 37.5, 25.0, 37.5],
}

# ── Colors (softened Okabe-Ito) ──
colors = {
    'Naive XCorr':            '#CC5A5A',
    'Diff. XCorr':            '#E8A04C',
    r'Threshold ($3\sigma$)': '#8B6BB0',
    'Perm. Granger':          '#4A90C4',
    'Toda–Yamamoto':          '#4DAF7C',
}

n_groups = len(alpha_labels)
n_methods = len(methods)
bar_width = 0.14
x = np.arange(n_groups)

fig, ax = plt.subplots(figsize=(3.35, 1.9))

# ── Background bands ──
ax.axvspan(-0.45, 0.45, color='#FDEDEC', alpha=0.45, zorder=0)
ax.text(0, 106, 'null', ha='center', va='bottom',
        fontsize=5, color='#B03A2E', fontstyle='italic', fontweight='bold')

ax.axvspan(1.55, 2.45, color='#EBF5FB', alpha=0.35, zorder=0)
ax.text(2, 106, 'onset', ha='center', va='bottom',
        fontsize=5, color='#1A5276', fontstyle='italic', fontweight='bold')

# ── 5% nominal FPR reference line ──
ax.axhline(y=5, color='#B03A2E', linewidth=0.5, linestyle='--', alpha=0.45, zorder=1)

# ── Draw bars ──
bar_containers = {}
for i, method in enumerate(methods):
    offset = (i - n_methods / 2 + 0.5) * bar_width
    vals = data[method]
    c = colors[method]
    is_hero = method == 'Perm. Granger'
    alpha_val = 1.0 if is_hero else 0.72
    edgecolor = '#222222' if is_hero else 'none'
    linewidth = 1.0 if is_hero else 0
    bars = ax.bar(x + offset, vals, bar_width * 0.92,
                  color=c, alpha=alpha_val, label=method,
                  edgecolor=edgecolor, linewidth=linewidth, zorder=2)
    bar_containers[method] = (bars, offset)

# ── Value labels on PermG bars ──
hero_bars, hero_offset = bar_containers['Perm. Granger']
hero_vals = data['Perm. Granger']
for j, v in enumerate(hero_vals):
    if v > 0:
        ax.text(x[j] + hero_offset, v + 1.5, f'{int(v)}',
                ha='center', va='bottom', fontsize=4.5,
                fontweight='bold', color='#2166AC')
    else:
        ax.text(x[j] + hero_offset, 1.5, '0',
                ha='center', va='bottom', fontsize=4.5,
                fontweight='bold', color='#2166AC', alpha=0.65)

# ── Axes ──
ax.set_xticks(x)
ax.set_xticklabels(alpha_labels)
ax.set_ylabel('FDR-significant pairs (%)', fontsize=9)
ax.set_ylim(0, 113)
ax.set_yticks([0, 25, 50, 75, 100])
ax.set_xlim(-0.55, n_groups - 0.45)

# ── Light grid ──
ax.yaxis.grid(True, alpha=0.2, linewidth=0.5, zorder=0)
ax.set_axisbelow(True)

# ── Legend (below chart, compact horizontal strip) ──
leg = ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.12),
                frameon=True, framealpha=0.95,
                edgecolor='#cccccc', ncol=3, handlelength=0.9,
                handletextpad=0.25, columnspacing=0.4, borderpad=0.2)
leg.get_frame().set_linewidth(0.4)

plt.tight_layout(pad=0.2)
plt.subplots_adjust(bottom=0.22)
plt.savefig('docs/paper/figures/fig_method_comparison.pdf')
plt.savefig('docs/paper/figures/fig_method_comparison.png')
print('Saved fig_method_comparison.pdf + .png')
