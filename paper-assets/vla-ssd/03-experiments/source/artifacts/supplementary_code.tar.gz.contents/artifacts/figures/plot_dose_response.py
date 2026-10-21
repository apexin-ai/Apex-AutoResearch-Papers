"""Dose-response curve: instruction-routing head ablation vs action divergence."""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import os

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
})

dose_n_heads = np.array([4, 8, 12, 16, 20, 24, 28, 32])

dose_cohen_d = np.array([
    0.4815412850770599, 0.5082040281351017, 0.5600389203470800,
    0.5916585965181512, 0.5929310917614178, 0.6106991692401877,
    0.6192428662864000, 0.6385059409290664
])

dose_ci_lower = np.array([
    0.4493981998904407, 0.4792767313857140, 0.5292064204814684,
    0.5593699517760848, 0.5591344210287796, 0.5784721762082760,
    0.5866794567732834, 0.6033325798526022
])

dose_ci_upper = np.array([
    0.5111655435414341, 0.5407791509767693, 0.5928744039295671,
    0.6253230923848914, 0.6273837044447675, 0.6453009849211714,
    0.6538126323060768, 0.6711688584188803
])

ref_control_d = 0.41

fig, ax = plt.subplots(figsize=(3.25, 2.6))

C_MAIN = '#1f77b4'
C_CTRL = '#d62728'
C_REGION = '#999999'

ax.fill_between(dose_n_heads, dose_ci_lower, dose_ci_upper,
                color=C_MAIN, alpha=0.15, edgecolor='none', zorder=2)

ax.plot(dose_n_heads, dose_cohen_d,
        '-o', color=C_MAIN, markersize=4.5, linewidth=1.4, zorder=3)

ax.axhline(ref_control_d, color=C_CTRL, linestyle='--', linewidth=0.7, alpha=0.5, zorder=1)
ax.text(33, 0.415, 'Control (8 random): $d$ = 0.41',
        fontsize=6.5, color=C_CTRL, ha='right', va='bottom')

for xb in [13, 20]:
    ax.axvline(xb, color=C_REGION, linestyle=':', linewidth=0.5, alpha=0.25, zorder=1)

y_lab = 0.72
ax.text(8, y_lab, 'Steep rise', fontsize=7, ha='center', color=C_REGION, style='italic')
ax.text(16.5, y_lab, 'Plateau', fontsize=7, ha='center', color=C_REGION, style='italic')
ax.text(27, y_lab, 'Slow rise', fontsize=7, ha='center', color=C_REGION, style='italic')

ax.set_xlabel('Number of heads ablated')
ax.set_ylabel("Cohen's $d$ (action MSE)")
ax.set_xticks(dose_n_heads)
ax.set_xlim(2, 34)
ax.set_ylim(0.35, 0.76)
ax.tick_params(direction='out', length=3)

plt.tight_layout()

out_dir = os.path.dirname(os.path.abspath(__file__))
fig.savefig(os.path.join(out_dir, 'fig_dose_response_curve.pdf'))
fig.savefig(os.path.join(out_dir, 'fig_dose_response_curve.png'))
print(f"Saved to {out_dir}/fig_dose_response_curve.pdf/.png")
