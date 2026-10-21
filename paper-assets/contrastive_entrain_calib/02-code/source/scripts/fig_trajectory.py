import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patheffects as pe
import numpy as np
import os

plt.rcParams.update({
    'font.family': 'DejaVu Sans',
    'font.size': 9,
    'axes.titlesize': 10,
    'axes.labelsize': 9,
    'xtick.labelsize': 8,
    'ytick.labelsize': 8,
    'legend.fontsize': 7,
    'figure.dpi': 300,
    'savefig.dpi': 300,
    'savefig.bbox': 'tight',
    'savefig.pad_inches': 0.05,
    'axes.spines.top': False,
    'axes.spines.right': False,
    'pdf.fonttype': 42,
    'ps.fonttype': 42,
    'lines.linewidth': 1.6,
})

C_ACT = '#0072B2'
C_R3  = '#D55E00'
C_R3_S2 = '#D55E00'
C_VAN = '#999999'

# ACT seed 1 (16/16 > vanilla)
act_steps = [500, 1000, 1500, 2000, 2500, 3000, 3500, 4000, 4500, 5000, 5500, 6000, 6500, 7000, 7500, 8000]
act_sycon = [0.170, 0.205, 0.170, 0.255, 0.239, 0.206, 0.231, 0.214, 0.188, 0.263, 0.238, 0.262, 0.253, 0.286, 0.277, 0.301]

# R3-only seed 1 (3/12 > vanilla)
r3s1_steps = [1000, 2000, 3000, 4000, 4500, 5000, 5500, 6000, 6500, 7000, 7500, 8000]
r3s1_sycon = [0.074, 0.085, 0.095, 0.114, 0.134, 0.114, 0.114, 0.085, 0.153, 0.105, 0.105, 0.143]

# R3-only seed 2 (1/12 > vanilla)
r3s2_steps = [500, 1000, 1500, 2000, 2500, 3000, 3500, 4000, 4500, 5000, 5500, 6000, 6500]
r3s2_sycon = [0.085, 0.084, 0.104, 0.085, 0.105, 0.095, 0.074, 0.143, 0.104, 0.104, 0.114, 0.095, 0.105]

vanilla_baseline = 0.134

fig, ax = plt.subplots(figsize=(3.5, 2.5))

ax.axhspan(0, vanilla_baseline, color='#f0f0f0', alpha=0.8, zorder=0)

ax.axhline(y=vanilla_baseline, color=C_VAN, linestyle='--', linewidth=1.0, zorder=2)
ax.text(8300, vanilla_baseline + 0.005, 'Vanilla', fontsize=7, color=C_VAN,
        ha='right', va='bottom')

# ACT seed 1
ax.plot(act_steps, act_sycon, '-o', color=C_ACT, markersize=3,
        markerfacecolor=C_ACT, markeredgecolor='white', markeredgewidth=0.5,
        label='ACT s1 (16/16)', zorder=4)

# R3-only seed 1
ax.plot(r3s1_steps, r3s1_sycon, '-s', color=C_R3, markersize=3,
        markerfacecolor=C_R3, markeredgecolor='white', markeredgewidth=0.5,
        label=r'$R_3$-only s1 (3/12)', zorder=3)

# R3-only seed 2
ax.plot(r3s2_steps, r3s2_sycon, '--^', color=C_R3_S2, markersize=3, alpha=0.6,
        markerfacecolor=C_R3_S2, markeredgecolor='white', markeredgewidth=0.5,
        label=r'$R_3$-only s2 (1/13)', zorder=3)

# Annotation: reliability gap
t = ax.text(6500, 0.27, '16/16 vs 4/26', fontsize=6, color='#333333',
            ha='center', va='bottom', fontstyle='italic',
            bbox=dict(boxstyle='round,pad=0.3', facecolor='white', edgecolor='#cccccc', alpha=0.9))

ax.set_xlim(0, 8500)
ax.set_ylim(0, 0.35)
ax.set_xlabel('Training Step')
ax.set_ylabel('SYCONScore')
ax.set_xticks([0, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000])
ax.set_xticklabels(['0', '1k', '2k', '3k', '4k', '5k', '6k', '7k', '8k'])

ax.grid(True, alpha=0.15, linewidth=0.5, zorder=0)

ax.legend(loc='upper left', frameon=True, framealpha=0.9, edgecolor='#cccccc',
          borderpad=0.4, handlelength=1.8)

plt.tight_layout()

outdir = os.path.dirname(os.path.abspath(__file__))
outdir = os.path.join(os.path.dirname(outdir), 'artifacts', 'figures')
os.makedirs(outdir, exist_ok=True)

pdf_path = os.path.join(outdir, 'fig_trajectory.pdf')
png_path = os.path.join(outdir, 'fig_trajectory.png')
fig.savefig(pdf_path)
fig.savefig(png_path)
plt.close()
print(f'Saved: {pdf_path}')
print(f'Saved: {png_path}')
