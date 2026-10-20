"""
Specification curve: detection rate across 18 analytical variants × 16 α levels.
narrative_intent: "Detection onset is invariant to reasonable analytical choices —
the α_c boundary is a property of the data, not the method."
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import json

plt.rcParams.update({
    'font.family': 'DejaVu Sans',
    'font.size': 9,
    'axes.titlesize': 10,
    'axes.labelsize': 9,
    'xtick.labelsize': 7,
    'ytick.labelsize': 8,
    'legend.fontsize': 7,
    'figure.dpi': 300,
    'savefig.dpi': 300,
    'savefig.bbox': 'tight',
    'savefig.pad_inches': 0.03,
    'axes.spines.top': False,
    'axes.spines.right': False,
    'pdf.fonttype': 42,
    'ps.fonttype': 42,
})

with open('artifacts/spec_curve_analysis/spec_curve_results.json') as f:
    data = json.load(f)

alphas = sorted(data.keys(), key=float)
methods = list(data[alphas[0]].keys())

fig, (ax_top, ax_bot) = plt.subplots(2, 1, figsize=(5.5, 3.5),
                                      height_ratios=[3, 1],
                                      sharex=True, gridspec_kw={'hspace': 0.08})

# ── Top panel: sorted specification curves per α ──
# For each α, sort the 18 specs by detection rate and plot as dots+lines
n_specs = len(methods)
x_specs = np.arange(n_specs)

cmap = plt.cm.RdYlBu_r
norm = plt.Normalize(vmin=0, vmax=1.0)

alpha_floats = [float(a) for a in alphas]
n_alphas = len(alphas)

# Use subset of α values for clarity (every other or key ones)
key_alphas = ['0.00', '0.25', '0.45', '0.48', '0.50', '0.52', '0.60', '0.75']
key_alphas = [a for a in key_alphas if a in data]

colors_spec = plt.cm.viridis(np.linspace(0.1, 0.9, len(key_alphas)))

for idx, alpha_str in enumerate(key_alphas):
    vals = [data[alpha_str][m] for m in methods]
    vals_sorted = sorted(vals, reverse=True)
    c = colors_spec[idx]
    alpha_f = float(alpha_str)
    lw = 1.8 if alpha_str in ('0.50', '0.75') else 0.9
    ls = '-' if alpha_f >= 0.50 else '--'
    zorder = 5 if alpha_str in ('0.50', '0.75') else 2
    ax_top.plot(x_specs, vals_sorted, marker='o', markersize=2.5,
                linewidth=lw, linestyle=ls, color=c, alpha=0.85,
                label=fr'$\alpha={alpha_str}$', zorder=zorder)

ax_top.set_ylabel('Detection rate')
ax_top.set_ylim(-0.05, 1.1)
ax_top.set_yticks([0, 0.25, 0.50, 0.75, 1.0])
ax_top.axhline(y=0, color='gray', linewidth=0.4, alpha=0.3)
ax_top.yaxis.grid(True, alpha=0.15, linewidth=0.4)

leg = ax_top.legend(loc='upper right', ncol=2, frameon=True, framealpha=0.9,
                    edgecolor='#cccccc', handlelength=1.5, borderpad=0.3,
                    fontsize=7.5)
leg.get_frame().set_linewidth(0.4)

# ── Bottom panel: method identity indicators ──
method_short = {
    'NaiveXCorr_Fwd': 'NX↑', 'NaiveXCorr_Rev': 'NX↓',
    'DiffXCorr_Fwd': 'DX↑', 'DiffXCorr_Fwd_FDR': 'DXf↑',
    'DiffXCorr_Rev': 'DX↓', 'DiffXCorr_Rev_FDR': 'DXf↓',
    'ThreshOnset_Fwd': 'TO↑', 'ThreshOnset_Rev': 'TO↓',
    'PermG_Fwd': 'PG↑', 'PermG_Fwd_FDR': 'PGf↑',
    'PermG_Rev': 'PG↓', 'PermG_Rev_FDR': 'PGf↓',
    'TY_Fwd': 'TY↑', 'TY_Rev': 'TY↓',
    'K>=3_Fwd': 'K3↑', 'K>=4_Fwd': 'K4↑',
    'K>=3_Rev': 'K3↓', 'K>=4_Rev': 'K4↓',
}

# Show method categories as colored strips
cat_colors = {
    'NaiveXCorr': '#CC5A5A', 'DiffXCorr': '#E8A04C',
    'ThreshOnset': '#8B6BB0', 'PermG': '#4A90C4',
    'TY': '#4DAF7C', 'K>=': '#666666'
}

# For the bottom panel, use α=0.50 sort order as reference
ref_vals = [(data['0.50'][m], m) for m in methods]
ref_sorted = sorted(ref_vals, key=lambda x: -x[0])
sorted_methods = [x[1] for x in ref_sorted]

for i, method in enumerate(sorted_methods):
    cat = method.split('_')[0]
    if cat.startswith('K>'):
        cat = 'K>='
    c = cat_colors.get(cat, '#999999')
    ax_bot.barh(0, 1, left=i, height=0.6, color=c, alpha=0.7, edgecolor='white', linewidth=0.3)

ax_bot.set_xlim(-0.5, n_specs - 0.5)
ax_bot.set_ylim(-0.5, 0.5)
ax_bot.set_yticks([])
ax_bot.set_xlabel('Specifications (sorted by detection rate at $\\alpha{=}0.50$)')
ax_bot.set_xticks([])

# Category legend for bottom panel
from matplotlib.patches import Patch
cat_patches = [
    Patch(facecolor='#CC5A5A', label='NaiveXCorr'),
    Patch(facecolor='#E8A04C', label='DiffXCorr'),
    Patch(facecolor='#8B6BB0', label='Threshold'),
    Patch(facecolor='#4A90C4', label='PermG'),
    Patch(facecolor='#4DAF7C', label='Toda-Yam.'),
    Patch(facecolor='#666666', label='Consensus'),
]
leg2 = ax_bot.legend(handles=cat_patches, loc='lower center',
                     bbox_to_anchor=(0.5, -1.8), ncol=6, frameon=True,
                     framealpha=0.95, edgecolor='#cccccc',
                     handlelength=0.8, handletextpad=0.3,
                     columnspacing=0.5, fontsize=8, borderpad=0.2)
leg2.get_frame().set_linewidth(0.4)

plt.savefig('docs/paper/figures/fig_spec_curve.pdf')
plt.savefig('docs/paper/figures/fig_spec_curve.png')
print('Saved fig_spec_curve.pdf + .png')
