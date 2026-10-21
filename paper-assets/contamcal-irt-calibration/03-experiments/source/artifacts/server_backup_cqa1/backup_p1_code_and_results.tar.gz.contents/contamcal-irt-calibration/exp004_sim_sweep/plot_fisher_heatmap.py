import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import numpy as np
import json

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
    'lines.linewidth': 1.8,
})

with open('/root/contamcal-irt-calibration/exp004_sim_sweep/results/sweep_summary.json') as f:
    data = json.load(f)

auc_vals = sorted(set(d['auc'] for d in data))
n_vals = sorted(set(d['n_models'] for d in data))

lookup = {}
for d in data:
    lookup[(d['auc'], d['n_models'])] = d

# ── Figure 1: CI Width Heatmap ──
ci_matrix = np.zeros((len(auc_vals), len(n_vals)))
for i, auc in enumerate(auc_vals):
    for j, n in enumerate(n_vals):
        ci_matrix[i, j] = lookup[(auc, n)]['ci95_width_avg']

fig, ax = plt.subplots(figsize=(5.5, 3.8))
im = ax.imshow(ci_matrix, cmap='YlOrRd', aspect='auto',
               norm=mcolors.LogNorm(vmin=ci_matrix.min(), vmax=ci_matrix.max()))

ax.set_xticks(range(len(n_vals)))
ax.set_xticklabels([str(n) for n in n_vals])
ax.set_yticks(range(len(auc_vals)))
auc_labels = {0.55: 'Low (0.55)', 0.65: 'Med-Low (0.65)',
              0.8: 'Med-High (0.80)', 0.9: 'High (0.90)'}
ax.set_yticklabels([auc_labels.get(a, str(a)) for a in auc_vals])
ax.set_xlabel('Number of Respondents ($N$)')
ax.set_ylabel('Signal Strength (AUC)')

for i in range(len(auc_vals)):
    for j in range(len(n_vals)):
        val = ci_matrix[i, j]
        color = 'white' if val > 0.25 else 'black'
        ax.text(j, i, f'{val:.3f}', ha='center', va='center',
                fontsize=9, fontweight='bold', color=color)

cbar = fig.colorbar(im, ax=ax, shrink=0.85, pad=0.02)
cbar.set_label('95% CI Width of $\\hat{\\gamma}$', fontsize=11)

ax.set_title('$\\gamma$ Identifiability: CI Width Shrinks with $N$', fontsize=12, pad=10)

plt.savefig('/root/autodl-tmp/exp006/figures/fisher_info_heatmap.pdf')
plt.savefig('/root/autodl-tmp/exp006/figures/fisher_info_heatmap.png')
plt.close()
print("Heatmap saved.")

# ── Figure 2: CI Width Scaling Plot ──
COLORS_AUC = {0.55: '#0072B2', 0.65: '#009E73', 0.8: '#E69F00', 0.9: '#D55E00'}
MARKERS = {0.55: 'o', 0.65: 's', 0.8: '^', 0.9: 'D'}

fig, ax = plt.subplots(figsize=(5.5, 4.0))

all_log_n = []
all_log_ci = []

for auc in auc_vals:
    ns = []
    cis = []
    for n in n_vals:
        ns.append(n)
        cis.append(lookup[(auc, n)]['ci95_width_avg'])
    ns = np.array(ns, dtype=float)
    cis = np.array(cis)

    all_log_n.extend(np.log(ns))
    all_log_ci.extend(np.log(cis))

    ax.plot(ns, cis, marker=MARKERS[auc], color=COLORS_AUC[auc],
            label=f'AUC = {auc}', markersize=7, zorder=3)

# Global power-law fit: CI ~ C * N^alpha
all_log_n = np.array(all_log_n)
all_log_ci = np.array(all_log_ci)
coeffs = np.polyfit(all_log_n, all_log_ci, 1)
alpha = coeffs[0]
C_fit = np.exp(coeffs[1])

n_smooth = np.linspace(6, 120, 200)
ci_fit = C_fit * n_smooth ** alpha
ax.plot(n_smooth, ci_fit, '--', color='#666666', linewidth=1.5, alpha=0.7,
        label=f'Fit: $\\propto N^{{{alpha:.2f}}}$', zorder=2)

ax.set_xscale('log')
ax.set_yscale('log')
ax.set_xticks(n_vals)
ax.set_xticklabels([str(n) for n in n_vals])
ax.get_xaxis().set_major_formatter(matplotlib.ticker.ScalarFormatter())
ax.set_xlabel('Number of Respondents ($N$)')
ax.set_ylabel('95% CI Width of $\\hat{\\gamma}$')
ax.set_title(f'$\\gamma$ CI Width Scaling ($\\propto N^{{{alpha:.2f}}}$)', fontsize=12, pad=10)
ax.legend(loc='upper right', frameon=True, fancybox=False, edgecolor='#cccccc')
ax.grid(True, alpha=0.3, linestyle='--')

plt.savefig('/root/autodl-tmp/exp006/figures/ci_width_scaling.pdf')
plt.savefig('/root/autodl-tmp/exp006/figures/ci_width_scaling.png')
plt.close()
print(f"Scaling plot saved. Fitted exponent: alpha = {alpha:.4f}")

# ── Per-AUC power law fits ──
print("\nPer-AUC power-law exponents:")
for auc in auc_vals:
    ns = np.array([float(n) for n in n_vals])
    cis = np.array([lookup[(auc, n)]['ci95_width_avg'] for n in n_vals])
    c = np.polyfit(np.log(ns), np.log(cis), 1)
    print(f"  AUC={auc}: alpha={c[0]:.4f}")
