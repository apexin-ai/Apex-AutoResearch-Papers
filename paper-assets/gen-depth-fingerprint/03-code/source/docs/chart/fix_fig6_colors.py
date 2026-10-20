"""Regenerate Figure 6 (variance decomposition) with main-text color convention.

Main text uses: blue=drifting, amber=stationary, wine=intermediate
(matching Figures 1, 3, 4)
"""
import matplotlib
matplotlib.use('Agg')
matplotlib.rcParams['pdf.fonttype'] = 42
matplotlib.rcParams['ps.fonttype'] = 42
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams.update({
    'font.family': 'serif',
    'font.serif': ['Times New Roman', 'DejaVu Serif'],
    'font.size': 9,
    'axes.labelsize': 10,
    'axes.titlesize': 10,
    'xtick.labelsize': 8,
    'ytick.labelsize': 8,
    'legend.fontsize': 7.5,
    'figure.dpi': 300,
    'savefig.dpi': 300,
    'savefig.bbox': 'tight',
    'savefig.pad_inches': 0.02,
    'axes.spines.top': False,
    'axes.spines.right': False,
    'mathtext.fontset': 'cm',
})

# Main-text DDR palette (consistent with Figures 1, 3, 4)
C_DRIFT = '#2166AC'    # blue (drifting)
C_STAT = '#E8A838'     # amber (near-stationary)
C_INTERM = '#8C4A6E'   # wine (intermediate)

fig, ax = plt.subplots(figsize=(3.4, 2.4))

feat_names = ['Ent. Mean', 'TTR', 'Hapax', 'Ent. Max', 'Ent. Min', 'Tail Decay', 'Ent. Std']
eta_depth = [0.341, 0.370, 0.364, 0.007, 0.002, 0.002, 0.054]
eta_gen   = [0.022, 0.024, 0.017, 0.002, 0.001, 0.023, 0.020]
eta_int   = [0.010, 0.007, 0.006, 0.003, 0.001, 0.009, 0.011]

x = np.arange(len(feat_names))
w = 0.25

# Color depth bars by DDR zone (main-text convention)
depth_colors = [C_DRIFT]*3 + [C_STAT]*3 + [C_INTERM]

bars1 = ax.bar(x - w, eta_depth, w, label=r'$\eta^2_{\mathrm{depth}}$',
               color=depth_colors, edgecolor='white', linewidth=0.5)
bars2 = ax.bar(x, eta_gen, w, label=r'$\eta^2_{\mathrm{gen}}$',
               color='#AAAAAA', edgecolor='white', linewidth=0.5)
bars3 = ax.bar(x + w, eta_int, w, label=r'$\eta^2_{\mathrm{int}}$',
               color='#D9D9D9', edgecolor='white', linewidth=0.5)

ax.axvline(x=2.5, color='#AAAAAA', linestyle='--', linewidth=0.6, alpha=0.5)
ax.axvline(x=5.5, color='#AAAAAA', linestyle='--', linewidth=0.6, alpha=0.5)

ax.text(1.0, 0.39, 'Drifting', ha='center', fontsize=7, fontstyle='italic', color=C_DRIFT)
ax.text(4.0, 0.39, 'Near-stationary', ha='center', fontsize=7, fontstyle='italic', color=C_STAT)
ax.text(6.0, 0.39, 'Interm.', ha='center', fontsize=7, fontstyle='italic', color=C_INTERM)

ax.set_xticks(x)
ax.set_xticklabels(feat_names, rotation=30, ha='right')
ax.set_ylabel(r'$\eta^2$ (proportion of total SS)')
ax.legend(loc='upper right', framealpha=0.9, edgecolor='#CCCCCC')
ax.set_ylim(0, 0.44)

plt.tight_layout()
plt.savefig('fig_appendix_variance_decomp.pdf')
plt.savefig('fig_appendix_variance_decomp.png')
plt.close()
print("OK fig_appendix_variance_decomp (main-text palette: blue/amber/wine)")
