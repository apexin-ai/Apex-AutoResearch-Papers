import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np

# --- Data (ordered bottom-to-top for forest plot) ---
methods = [
    'Binoculars',
    'FastDetectGPT',
    'LD-Score (corrected)',
    'Avg-LogProb',
    '7-Feature Ensemble',
]
f1 =       [0.579,  0.6269, 0.7212, 0.7653, 0.798]
ci_lower = [0.405,  0.511,  0.588,  0.616,  0.786]
ci_upper = [0.664,  0.762,  0.770,  0.820,  0.799]

n = len(methods)
y_pos = np.arange(n)

# Okabe-Ito palette (colorblind-safe)
OI_BLUE    = '#0072B2'
OI_ORANGE  = '#E69F00'
OI_GREEN   = '#009E73'
OI_VERMIL  = '#D55E00'
OI_PURPLE  = '#CC79A7'

colors = [OI_PURPLE, OI_VERMIL, OI_GREEN, OI_ORANGE, OI_BLUE]

# --- Figure ---
fig, ax = plt.subplots(figsize=(6, 4.5))  # ~4:3

for i in range(n):
    is_ensemble = (methods[i] == '7-Feature Ensemble')
    marker = 'o'
    ms = 9 if is_ensemble else 7
    mfc = colors[i] if is_ensemble else 'white'
    mec = colors[i]
    lw = 2.2 if is_ensemble else 1.6
    zorder = 5 if is_ensemble else 4

    ax.plot(f1[i], y_pos[i], marker=marker, markersize=ms,
            markerfacecolor=mfc, markeredgecolor=mec, markeredgewidth=1.5,
            zorder=zorder, clip_on=False)
    ax.hlines(y_pos[i], ci_lower[i], ci_upper[i],
              colors=colors[i], linewidth=lw, zorder=zorder - 1)

    # Right-side annotation: F1 [CI_low, CI_up]
    label = f'{f1[i]:.3f}  [{ci_lower[i]:.3f}, {ci_upper[i]:.3f}]'
    ax.text(0.87, y_pos[i], label, va='center', ha='left', fontsize=9,
            fontfamily='monospace', color='#333333')

# Chance level (3-class)
ax.axvline(x=1/3, color='#999999', linestyle='--', linewidth=1.0, zorder=1)
ax.text(1/3 + 0.008, n - 0.15, 'chance', fontsize=8, color='#999999', va='top')

# Light grid
ax.xaxis.set_major_locator(ticker.MultipleLocator(0.1))
ax.grid(axis='x', color='#E0E0E0', linewidth=0.5, zorder=0)
ax.set_axisbelow(True)

# Axes
ax.set_yticks(y_pos)
ax.set_yticklabels(methods, fontsize=11)
ax.set_xlabel('LOGO Macro-F1', fontsize=11)
ax.set_xlim(0.25, 0.86)
ax.set_ylim(-0.5, n - 0.5)

# Remove top/right spines
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

# Title (optional, can remove for paper)
# ax.set_title('Baseline Comparison', fontsize=12, pad=10)

plt.tight_layout()

out_dir = '/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/figures/paper'
fig.savefig(f'{out_dir}/fig3_baseline_comparison.pdf', bbox_inches='tight', dpi=300)
fig.savefig(f'{out_dir}/fig3_baseline_comparison.png', bbox_inches='tight', dpi=300)
print('Saved PDF and PNG.')
