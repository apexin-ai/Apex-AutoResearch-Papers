import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import os

K3_rates = np.array([0.004, 0.012, 0.008, 0.008, 0.009, 0.008,
                      0.006, 0.016, 0.011, 0.016, 0.004, 0.01]) * 100
K5_rates = np.array([0.001, 0.006, 0.001, 0.003, 0.003, 0.008,
                      0.006, 0.004, 0.006, 0.003, 0.0, 0.002]) * 100
K7_rates = np.array([0.001, 0.003, 0.0, 0.002, 0.001, 0.002,
                      0.0, 0.001, 0.0, 0.002, 0.001, 0.001]) * 100

colors = {'K3': '#1E88E5', 'K5': '#43A047', 'K7': '#8E24AA'}

fig, ax = plt.subplots(figsize=(6, 3.5))

x_k3 = np.arange(12)
x_k5 = np.arange(12) + 13
x_k7 = np.arange(12) + 26

ax.scatter(x_k3, K3_rates, c=colors['K3'], s=40, zorder=5, edgecolors='white', linewidths=0.5, label='$K=3$')
ax.scatter(x_k5, K5_rates, c=colors['K5'], s=40, zorder=5, edgecolors='white', linewidths=0.5, label='$K=5$')
ax.scatter(x_k7, K7_rates, c=colors['K7'], s=40, zorder=5, edgecolors='white', linewidths=0.5, label='$K=7$')

ax.axhline(y=5.0, color='#E53935', linestyle='--', linewidth=1.2, zorder=3)
ax.text(36.5, 5.0, r'Nominal $\alpha$ = 5%', va='center', ha='left', color='#E53935',
        fontsize=8.5, fontfamily='DejaVu Sans')

ax.axhline(y=7.5, color='#E53935', linestyle=':', linewidth=0.8, alpha=0.5, zorder=3)
ax.text(36.5, 7.5, 'Over-rejection\nthreshold', va='center', ha='left', color='#E53935',
        fontsize=7, fontfamily='DejaVu Sans', alpha=0.6)

for sep_x in [12.5, 25.5]:
    ax.axvline(x=sep_x, color='#BDBDBD', linestyle='-', linewidth=0.6, zorder=1)

ax.set_xlim(-1, 42)
ax.set_ylim(0, 7)
ax.set_ylabel('Empirical null rejection rate (%)', fontsize=10, fontfamily='DejaVu Sans')

group_centers = [np.mean(x_k3), np.mean(x_k5), np.mean(x_k7)]
group_labels = ['$K$=3\n(12 conditions)', '$K$=5\n(12 conditions)', '$K$=7\n(12 conditions)']
ax.set_xticks(group_centers)
ax.set_xticklabels(group_labels, fontsize=9, fontfamily='DejaVu Sans')
ax.tick_params(axis='x', length=0)
ax.tick_params(axis='y', labelsize=9)

ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['bottom'].set_linewidth(0.6)
ax.spines['left'].set_linewidth(0.6)

ax.yaxis.set_major_locator(plt.MultipleLocator(1))
ax.yaxis.set_minor_locator(plt.MultipleLocator(0.5))
ax.grid(axis='y', linestyle=':', linewidth=0.4, alpha=0.5, zorder=0)

ax.legend(loc='upper left', fontsize=8.5, framealpha=0.9, edgecolor='#E0E0E0',
          handletextpad=0.3, borderpad=0.4)

plt.tight_layout()

out_dir = os.path.dirname(os.path.abspath(__file__))
fig.savefig(os.path.join(out_dir, 'fig_bootstrap_null.pdf'), dpi=300, bbox_inches='tight')
fig.savefig(os.path.join(out_dir, 'fig_bootstrap_null.png'), dpi=300, bbox_inches='tight')
plt.close()
print('Saved fig_bootstrap_null.pdf and .png')
