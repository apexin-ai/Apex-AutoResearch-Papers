import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

matplotlib.rcParams['font.size'] = 9
matplotlib.rcParams['font.family'] = 'sans-serif'

# Llama2base: full L0-L31
llama2base_layers = list(range(32))
llama2base_acc = [
    0.1, 0.802, 0.987, 0.991, 0.995, 1.0, 1.0, 0.999, 0.999, 1.0,
    1.0, 0.999, 1.0, 1.0, 0.999, 0.999, 0.998, 0.998, 0.998, 0.998,
    0.999, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0
]

# Trained: dense L0-L8 + sparse L16, L24, L31
trained_layers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 16, 24, 31]
trained_acc = [0.1, 0.996, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]

# Untrained: dense L0-L8 + sparse L16, L24, L31
untrained_layers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 16, 24, 31]
untrained_acc = [0.1, 1.0, 1.0, 1.0, 0.998, 0.999, 0.996, 0.996, 0.986, 0.923, 0.864, 0.82]

fig, ax = plt.subplots(figsize=(5, 3.5))

# Plot lines (order: trained first for legend ordering)
ax.plot(trained_layers, trained_acc, color='#4C72B0', linestyle='-',
        marker='o', markersize=4, linewidth=1.5, label='Trained VLA', zorder=4)
ax.plot(untrained_layers, untrained_acc, color='#C44E52', linestyle=':',
        marker='^', markersize=4, linewidth=1.5, label='Untrained VLA', zorder=4)
ax.plot(llama2base_layers, llama2base_acc, color='#55A868', linestyle='--',
        marker='s', markersize=3.5, linewidth=1.5, label='Llama-2 Base', zorder=3)

# Chance level
ax.axhline(y=0.1, color='gray', linestyle='--', linewidth=0.8, alpha=0.7)
ax.text(12.5, 0.13, 'chance', va='bottom', ha='center', fontsize=7.5, color='gray')

# Annotate L1 divergence for llama2base
ax.annotate('80.2%', xy=(1, 0.802), xytext=(4, 0.72),
            fontsize=7.5, color='#55A868', ha='center',
            arrowprops=dict(arrowstyle='->', color='#55A868', lw=0.8))

# Axes
ax.set_xlabel('Layer')
ax.set_ylabel('10-way Classification Accuracy')
ax.set_xlim(-0.5, 32)
ax.set_ylim(0.0, 1.05)
ax.set_xticks([0, 4, 8, 12, 16, 20, 24, 28, 31])
ax.set_yticks([0.0, 0.2, 0.4, 0.6, 0.8, 1.0])

# Grid
ax.yaxis.grid(True, alpha=0.3, color='gray', linewidth=0.5)
ax.set_axisbelow(True)

# Legend
ax.legend(loc='lower right', framealpha=0.9, fontsize=8)

plt.tight_layout()

_REPO_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
outdir = os.path.join(_REPO_ROOT, 'artifacts', 'cross_instruction')
plt.savefig(f'{outdir}/fig_three_condition_probe.pdf', bbox_inches='tight', dpi=300)
plt.savefig(f'{outdir}/fig_three_condition_probe.png', bbox_inches='tight', dpi=200)
print("Done: saved PDF and PNG")
