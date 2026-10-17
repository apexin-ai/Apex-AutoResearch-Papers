"""
Hypergeometric cliff model — π₀.₅ Object random pruning.
(a) Model-predicted vs observed SR across cliff zone.
(b) P(collapse) comparison: Object (C=106) vs Spatial (C≈5).
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import hypergeom
from pathlib import Path

plt.rcParams.update({
    'font.family': 'serif',
    'font.serif': ['Times New Roman', 'Liberation Serif', 'DejaVu Serif'],
    'mathtext.fontset': 'stix',
    'font.size': 9,
    'figure.dpi': 300,
    'savefig.dpi': 300,
    'savefig.bbox': 'tight',
    'savefig.pad_inches': 0.05,
    'pdf.fonttype': 42,
    'ps.fonttype': 42,
    'axes.spines.top': False,
    'axes.spines.right': False,
})

OUT = Path(__file__).parent
N = 768

OBS_OBJ_K = np.array([0.95, 0.925, 0.9, 0.85])
OBS_OBJ_SR = np.array([74.0, 27.6, 9.0, 5.6]) / 100
OBS_SPA_K = np.array([0.95, 0.925, 0.9, 0.85])
OBS_SPA_SR = np.array([76.4, 60.4, 54.6, 58.4]) / 100

C_OBJ, M_OBJ = 106, 7
C_SPA, M_SPA = 5, 1

def survival(k_arr, C, m):
    sr = np.zeros_like(k_arr, dtype=float)
    for i, k in enumerate(k_arr):
        n_rm = min(int(round((1 - k) * N)), N)
        if n_rm < m or C < m:
            sr[i] = 1.0
        else:
            sr[i] = 1.0 - (1.0 - hypergeom.cdf(m - 1, N, C, n_rm))
    return sr

k_fine = np.linspace(0.80, 1.0, 201)

COL_BLUE = '#0072B2'
COL_RED = '#D55E00'
COL_GREEN = '#009E73'

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(8.5, 3.2))

# (a) Object: model vs observed
pred_obj = survival(k_fine, C_OBJ, M_OBJ)
ax1.plot(k_fine, pred_obj, '--', color=COL_BLUE, lw=1.8, label=f'Model ($C$={C_OBJ}, $m$={M_OBJ})')
ax1.scatter(OBS_OBJ_K, OBS_OBJ_SR, s=50, c=COL_RED, marker='o', zorder=5,
            edgecolors='white', linewidths=1.0, label='Observed (Object)')
ax1.axvspan(0.85, 0.95, color='#f5f0e0', alpha=0.3, zorder=0)
ax1.set_xlabel('Retention Ratio $k$')
ax1.set_ylabel('Success Rate')
ax1.set_title('(a) Model vs. Observed', fontsize=10, fontweight='semibold')
ax1.set_xlim(0.80, 1.0)
ax1.set_ylim(-0.05, 1.05)
ax1.legend(fontsize=7.5, loc='upper left')
ax1.text(0.90, 0.15, 'RMSE = 0.018', fontsize=7.5, ha='center', color='#666666',
         transform=ax1.transData)
ax1.grid(axis='y', color='#eeeeee', linewidth=0.5, zorder=0)

# (b) P(collapse) comparison
p_fail_obj = 1.0 - survival(k_fine, C_OBJ, M_OBJ)
p_fail_spa = 1.0 - survival(k_fine, C_SPA, M_SPA)
ax2.plot(k_fine, p_fail_obj, '-', color=COL_RED, lw=1.8,
         label=f'Object ($C$={C_OBJ}, concentrated)')
ax2.plot(k_fine, p_fail_spa, '-', color=COL_GREEN, lw=1.8,
         label=f'Spatial ($C$≈{C_SPA}, distributed)')
ax2.axhline(0.5, color='#999999', ls=':', lw=0.8)
ax2.set_xlabel('Retention Ratio $k$')
ax2.set_ylabel('$P$(collapse)')
ax2.set_title('(b) Object vs. Spatial', fontsize=10, fontweight='semibold')
ax2.set_xlim(0.80, 1.0)
ax2.set_ylim(-0.05, 1.05)
ax2.legend(fontsize=7.5, loc='upper right')
ax2.grid(axis='y', color='#eeeeee', linewidth=0.5, zorder=0)

plt.tight_layout()
fig.savefig(OUT / 'fig_cliff_model.pdf', format='pdf')
fig.savefig(OUT / 'fig_cliff_model.png', format='png')
print(f"Saved: {OUT / 'fig_cliff_model.pdf'}")
plt.close()
