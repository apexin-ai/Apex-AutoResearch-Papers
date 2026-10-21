import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import os

layers = np.arange(33)

probe_r2 = [0.629, 0.625, 0.622, 0.624, 0.629, 0.627, 0.632, 0.632, 0.636, 0.637,
            0.624, 0.623, 0.626, 0.624, 0.623, 0.619, 0.619, 0.609, 0.613, 0.613,
            0.611, 0.589, 0.586, 0.578, 0.577, 0.553, 0.536, 0.552, 0.544, 0.530,
            0.511, 0.488, 0.535]

trained_r2 = [-5.60, -5.84, -6.01, -5.58, -5.94, -5.42, -4.61, -5.04, -5.57, -6.02,
              -6.70, -6.97, -6.16, -6.63, -7.08, -5.82, -5.59, -4.79, -4.68, -4.02,
              -4.01, -4.38, -4.41, -3.71, -3.65, -4.13, -4.15, -4.18, -4.18, -3.71,
              -3.40, -2.77, -3.04]

untrained_r2 = [-5.612, -4.891, -4.625, -4.676, -4.342, -4.082, -3.611, -4.200, -4.680,
                -5.295, -5.241, -5.520, -5.320, -5.152, -5.203, -5.360, -5.351, -4.508,
                -4.444, -4.367, -4.296, -4.376, -4.404, -4.352, -4.334, -4.145, -4.126,
                -3.998, -4.003, -4.032, -4.040, -3.814, -3.547]

plt.rcParams.update({
    'font.size': 12,
    'font.family': 'serif',
    'axes.linewidth': 0.8,
    'axes.spines.top': False,
    'axes.spines.right': False,
    'xtick.direction': 'out',
    'ytick.direction': 'out',
    'figure.dpi': 150,
})

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 6), sharex=True,
                                gridspec_kw={'height_ratios': [1, 1], 'hspace': 0.22})

# --- Upper panel: Independent Linear Probe ---
ax1.plot(layers, probe_r2, color='#2171B5', linewidth=2.0, marker='o', markersize=3.5,
         label='Trained OpenVLA', zorder=3)
ax1.set_ylabel(r'$R^2$', fontsize=13)
ax1.set_ylim(0.42, 0.68)
ax1.set_title('Independent Linear Probe', fontsize=13, fontweight='bold', pad=8)
ax1.legend(loc='lower left', frameon=False, fontsize=10.5)

peak_idx = int(np.argmax(probe_r2))
ax1.annotate('mid-layer peak',
             xy=(peak_idx, probe_r2[peak_idx]),
             xytext=(peak_idx + 6, probe_r2[peak_idx] + 0.02),
             fontsize=9.5, color='#2171B5',
             arrowprops=dict(arrowstyle='->', color='#2171B5', lw=1.2),
             ha='left', va='bottom')

ax1.annotate('exit collapse',
             xy=(31, probe_r2[31]),
             xytext=(23, 0.45),
             fontsize=9.5, color='#2171B5',
             arrowprops=dict(arrowstyle='->', color='#2171B5', lw=1.2),
             ha='center', va='bottom')

ax1.axhline(y=0, color='gray', linewidth=0.5, linestyle=':', alpha=0.5)

# --- Lower panel: Frozen Action Head ---
ax2.plot(layers, trained_r2, color='#CB181D', linewidth=2.0, marker='s', markersize=3.5,
         label='Trained OpenVLA', zorder=3)
ax2.plot(layers, untrained_r2, color='#888888', linewidth=1.8, marker='^', markersize=3,
         linestyle='--', label='Untrained OpenVLA', zorder=2)
ax2.set_ylabel(r'$R^2$', fontsize=13)
ax2.set_ylim(-8, -2)
ax2.set_xlabel('Layer Index', fontsize=13)
ax2.set_title('Frozen Action Head (LM Head)', fontsize=13, fontweight='bold', pad=8)
ax2.legend(loc='lower right', frameon=False, fontsize=10.5)

ax2.text(16, -2.5, r'All layers $R^2 < 0$', fontsize=10, color='#666666',
         ha='center', va='top', style='italic')

ax2.axhline(y=0, color='gray', linewidth=0.5, linestyle=':', alpha=0.5)

for ax in [ax1, ax2]:
    ax.axvline(x=32, color='#999999', linewidth=1.0, linestyle='--', alpha=0.7)

ax1.text(32.5, 0.55, 'exit\nlayer', fontsize=8.5, color='#777777', va='top', ha='left')

ax2.set_xticks([0, 4, 8, 12, 16, 20, 24, 28, 32])
ax2.set_xlim(-0.5, 33.5)

plt.tight_layout()

out_dir = os.path.dirname(os.path.abspath(__file__))
fig.savefig(os.path.join(out_dir, 'action_head_vs_probe_comparison.pdf'), bbox_inches='tight', dpi=300)
fig.savefig(os.path.join(out_dir, 'action_head_vs_probe_comparison.png'), bbox_inches='tight', dpi=300)
print('Done.')
