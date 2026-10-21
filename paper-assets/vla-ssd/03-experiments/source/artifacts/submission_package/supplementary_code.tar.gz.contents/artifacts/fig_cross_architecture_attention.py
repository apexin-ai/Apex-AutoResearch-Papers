import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

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

layers = np.arange(32)

# Data extracted from server JSON files
ovla_trained = [20, 22, 0, 0, 3, 2, 2, 3, 5, 5, 1, 4, 6, 5, 7, 4, 5, 0, 1, 1, 0, 0, 5, 1, 0, 0, 1, 2, 1, 0, 0, 0]
ovla_untrained = [0]*32
phi3v_trained = [3, 32, 32, 0, 0, 0, 1, 2, 3, 6, 3, 4, 4, 7, 11, 4, 7, 3, 5, 8, 5, 3, 5, 9, 5, 11, 10, 12, 8, 17, 17, 18]
phi3v_untrained = [3, 28, 17, 18, 31, 10, 18, 23, 32, 32, 32, 32, 30, 32, 32, 32, 32, 32, 31, 31, 32, 32, 31, 32, 30, 30, 29, 32, 32, 28, 30, 31]

blue_dark = '#1f77b4'
blue_light = '#aec7e8'
orange_dark = '#e55100'
orange_light = '#ffb74d'

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 5.5), sharex=True, sharey=True)
fig.subplots_adjust(hspace=0.18)

# Panel (a): OpenVLA
ax1.fill_between(layers, ovla_untrained, alpha=0.08, color=blue_dark)
ax1.plot(layers, ovla_untrained, color=blue_light, linestyle='--', linewidth=1.5,
         marker='o', markersize=3, label='Untrained (LLaMA-2)', zorder=3)
ax1.fill_between(layers, ovla_trained, alpha=0.10, color=blue_dark)
ax1.plot(layers, ovla_trained, color=blue_dark, linestyle='-', linewidth=2.0,
         marker='o', markersize=3.5, label='Trained (LIBERO fine-tuned)', zorder=4)

ax1.axhline(y=16, color='gray', linestyle=':', linewidth=0.8, alpha=0.6)
ax1.set_title('(a)  OpenVLA  (LLaMA-2-7B backbone)', fontweight='semibold', loc='left')
ax1.set_ylabel('Instruction-dominant\nheads  (/32)')
ax1.set_ylim(-1, 34)
ax1.set_yticks([0, 8, 16, 24, 32])
ax1.legend(loc='upper right', frameon=False)

ax1.annotate(f'{ovla_trained[1]}', xy=(1, ovla_trained[1]), xytext=(4, 28),
             fontsize=9, color=blue_dark, fontweight='bold',
             arrowprops=dict(arrowstyle='->', color=blue_dark, lw=1.0))

# Panel (b): Phi3V
ax2.fill_between(layers, phi3v_untrained, alpha=0.08, color=orange_dark)
ax2.plot(layers, phi3v_untrained, color=orange_light, linestyle='--', linewidth=1.5,
         marker='s', markersize=3, label='Untrained (Phi-3V base)', zorder=3)
ax2.fill_between(layers, phi3v_trained, alpha=0.10, color=orange_dark)
ax2.plot(layers, phi3v_trained, color=orange_dark, linestyle='-', linewidth=2.0,
         marker='s', markersize=3.5, label='Trained (TraceVLA)', zorder=4)

ax2.axhline(y=16, color='gray', linestyle=':', linewidth=0.8, alpha=0.6)
ax2.set_title('(b)  Phi-3V  (Phi-3-mini backbone)', fontweight='semibold', loc='left')
ax2.set_xlabel('Layer index')
ax2.set_ylabel('Instruction-dominant\nheads  (/32)')
ax2.set_xticks(np.arange(0, 32, 2))
ax2.set_xticklabels([f'L{i}' for i in range(0, 32, 2)], fontsize=8)
ax2.legend(loc='center right', frameon=False)

ax2.annotate(f'{phi3v_trained[1]}', xy=(1, phi3v_trained[1]), xytext=(4, 28),
             fontsize=9, color=orange_dark, fontweight='bold',
             arrowprops=dict(arrowstyle='->', color=orange_dark, lw=1.0))

ax2.annotate(f'{phi3v_untrained[1]}', xy=(1, phi3v_untrained[1]), xytext=(4.5, 22),
             fontsize=9, color='#c68600', fontweight='bold',
             arrowprops=dict(arrowstyle='->', color='#c68600', lw=1.0))

ax1.text(31.3, 16, '50%', fontsize=8, color='gray', va='center')
ax2.text(31.3, 16, '50%', fontsize=8, color='gray', va='center')

_REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
out_dir = os.path.join(_REPO_ROOT, 'artifacts')
fig.savefig(f'{out_dir}/fig_cross_architecture_attention.pdf')
fig.savefig(f'{out_dir}/fig_cross_architecture_attention.png')
print('Done')
plt.close()
