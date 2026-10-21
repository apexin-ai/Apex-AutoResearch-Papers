import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patheffects as pe
import numpy as np

plt.rcParams.update({
    'font.family': 'DejaVu Sans',
    'font.size': 11,
    'axes.titlesize': 13,
    'axes.labelsize': 11,
    'xtick.labelsize': 10,
    'ytick.labelsize': 10,
    'legend.fontsize': 9,
    'figure.dpi': 300,
    'savefig.dpi': 300,
    'savefig.bbox': 'tight',
    'savefig.pad_inches': 0.05,
    'axes.spines.top': False,
    'axes.spines.right': False,
    'pdf.fonttype': 42,
    'ps.fonttype': 42,
    'lines.linewidth': 1.8,
})

STROKE = [pe.withStroke(linewidth=2.8, foreground='white')]

# --- Data ---
M_labels = [16, 32, 64, 96, 128]
x_pos = np.arange(len(M_labels))  # equal spacing: 0,1,2,3,4
ca_mean = np.array([56.9, 60.1, 62.0, 54.5, 58.0])
ca_std = np.array([1.3, 1.3, 2.3, 3.2, 3.5])

mlp_x = 1  # M=32 position
mlp_mean = 63.4
mlp_std = 2.6

baseline_sr = 44.8

# --- Colors (Okabe-Ito) ---
C_CA = '#0072B2'
C_MLP = '#009E73'
C_BASELINE = '#E69F00'
C_FLOOR = '#999999'

# --- Figure ---
fig, ax = plt.subplots(figsize=(4.5, 3.5))

# Reference lines
ax.axhline(y=baseline_sr, color=C_BASELINE, linestyle='--', linewidth=1.2, alpha=0.7, zorder=1)
t_bl = ax.text(4.05, baseline_sr - 1.5, 'SmolVLA Baseline (44.8%)',
               fontsize=8, color=C_BASELINE, ha='right', va='top')
t_bl.set_path_effects(STROKE)

ax.axhline(y=0, color=C_FLOOR, linestyle=':', linewidth=0.8, alpha=0.5, zorder=1)
t_fl = ax.text(-0.4, 1.8, 'Hard Pruning (0%)',
               fontsize=7.5, color=C_FLOOR, ha='left', va='bottom', alpha=0.7)

# Cross-attention line + error bars
ax.errorbar(x_pos, ca_mean, yerr=ca_std,
            fmt='o-', color=C_CA, markersize=7,
            capsize=4, capthick=0.8, elinewidth=0.8,
            markeredgecolor='white', markeredgewidth=1.0,
            label='Cross-Attention VTR', zorder=3)

# Direct labels for cross-attention points
# (ox, oy in offset points, ha)
label_cfg = {
    0: (0, -12, 'center'),   # M=16: below
    1: (0, -12, 'center'),   # M=32: below
    2: (0, 10, 'center'),    # M=64: above
    3: (0, -12, 'center'),   # M=96: below
    4: (0, 10, 'center'),    # M=128: above
}
for i, (sr, std) in enumerate(zip(ca_mean, ca_std)):
    ox, oy, ha = label_cfg[i]
    t = ax.annotate(f'{sr:.1f}%', (x_pos[i], sr),
                    xytext=(ox, oy), textcoords='offset points',
                    fontsize=8.5, color=C_CA, ha=ha, va='center',
                    fontweight='bold')
    t.set_path_effects(STROKE)

# MLP adapter point + error bar
ax.errorbar(mlp_x, mlp_mean, yerr=mlp_std,
            fmt='D', color=C_MLP, markersize=8,
            capsize=4, capthick=0.8, elinewidth=0.8,
            markeredgecolor='white', markeredgewidth=1.0,
            label='MLP Adapter VTR', zorder=4)

# MLP adapter annotation
t_mlp = ax.annotate('MLP Adapter\n63.4%', (mlp_x, mlp_mean),
                     xytext=(16, 14), textcoords='offset points',
                     fontsize=8.5, color=C_MLP, ha='left', va='bottom',
                     fontweight='bold',
                     arrowprops=dict(arrowstyle='->', color=C_MLP, lw=0.8,
                                     shrinkB=3))
t_mlp.set_path_effects(STROKE)

# p=0.15 bracket: left side of M=32
bx = mlp_x - 0.12
ax.plot([bx, bx], [ca_mean[1], mlp_mean], color='#666666', lw=0.7, zorder=2)
ax.plot([bx - 0.04, bx + 0.04], [ca_mean[1], ca_mean[1]], color='#666666', lw=0.7, zorder=2)
ax.plot([bx - 0.04, bx + 0.04], [mlp_mean, mlp_mean], color='#666666', lw=0.7, zorder=2)
mid_y = (ca_mean[1] + mlp_mean) / 2
t_p = ax.text(bx - 0.06, mid_y, 'p=0.15\n(n.s.)', fontsize=7.5,
              color='#666666', ha='right', va='center', fontstyle='italic')
t_p.set_path_effects(STROKE)

# Axes
ax.set_xlabel('Number of Compressed Tokens (M)')
ax.set_ylabel('Success Rate (%)')
ax.set_xticks(x_pos)
ax.set_xticklabels([str(m) for m in M_labels])
ax.set_xlim(-0.5, 4.5)
ax.set_ylim(-5, 78)

ax.grid(True, alpha=0.15, axis='y', zorder=0)
ax.legend(loc='lower right', framealpha=0.9, edgecolor='none')

plt.tight_layout()

outdir = '/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/figures/paper'
fig.savefig(f'{outdir}/fig_compression_curve.pdf')
fig.savefig(f'{outdir}/fig_compression_curve.png')
plt.close()
print('Saved fig_compression_curve.pdf and .png')
