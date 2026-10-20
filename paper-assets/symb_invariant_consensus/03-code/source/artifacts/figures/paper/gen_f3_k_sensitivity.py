import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams.update({
    'font.family': 'DejaVu Sans',
    'font.size': 11,
    'axes.titlesize': 12,
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
})

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(7.5, 3.8), gridspec_kw={'width_ratios': [1.1, 1]})

# ── Panel (a): K sensitivity inverted-U ──
k_vals = [4, 8, 12, 16]
delta_pp = [-1.47, -0.98, 4.90, 1.47]
p_vals = [0.629, 0.754, 0.013, 0.629]
sc_acc = [54.41, 57.35, 54.41, 55.88]

colors_k = ['#888' if p >= 0.05 else '#2E7D32' for p in p_vals]
markers_k = ['o' if p >= 0.05 else '*' for p in p_vals]

ax1.axhline(y=0, color='#888', ls='--', lw=0.8, zorder=1)

for i, (k, d, p, c, m) in enumerate(zip(k_vals, delta_pp, p_vals, colors_k, markers_k)):
    size = 120 if m == '*' else 60
    ax1.scatter(k, d, marker=m, s=size, c=c, edgecolors='#333', linewidths=0.6, zorder=3)

ax1.plot(k_vals, delta_pp, color='#CC79A7', lw=1.5, ls='-', alpha=0.7, zorder=2)

ax1.annotate('+4.90 pp*\n($p$=0.013)',
             xy=(12, 4.90), xytext=(13.5, 6.0),
             fontsize=8, fontweight='bold', ha='left',
             arrowprops=dict(arrowstyle='->', color='#555', lw=0.8))

ax1.set_xlabel('$K$ (number of traces)')
ax1.set_ylabel('SICA $\\Delta$ (pp)')
ax1.set_xticks(k_vals)
ax1.set_xlim(2, 18)
ax1.set_ylim(-3, 7.5)
ax1.set_title('(a) K Sensitivity (Mistral-7B, FOLIO)')

# ── Panel (b): Actual K vs Eff-K grouped bars ──
conditions = [
    'Qwen-14B\nLogiQA',
    'Qwen-14B\nFOLIO',
    'Mistral\ns42',
    'Mistral\ns123',
    'Mistral\ns456',
    'Mistral\nPW-D5',
]
kappa_vals = [0.821, 0.744, 0.500, 0.412, 0.401, 0.210]
eff_k_vals = [1.20, 1.31, 1.85, 2.17, 2.22, 3.63]
delta_vals = [-0.50, -0.49, 4.90, 3.43, -0.49, -2.83]
nominal_k = 12

bar_colors = ['#0072B2', '#0072B2', '#CC79A7', '#CC79A7', '#CC79A7', '#CC79A7']

x = np.arange(len(conditions))
w = 0.35

bars_nom = ax2.bar(x - w/2, [nominal_k]*len(conditions), w,
                   color='#E0E0E0', edgecolor='#999', linewidth=0.5,
                   label='Nominal $K$', zorder=2)
bars_eff = ax2.bar(x + w/2, eff_k_vals, w,
                   color=bar_colors, edgecolor='#333', linewidth=0.5,
                   alpha=0.85, label='Eff-$K$', zorder=2)

for i, (ek, kap) in enumerate(zip(eff_k_vals, kappa_vals)):
    ax2.text(x[i] + w/2, ek + 0.3, f'{ek:.2f}\n($\\kappa$={kap:.2f})',
             ha='center', fontsize=6.5, fontweight='bold', va='bottom', linespacing=1.3)

ax2.set_ylabel('Number of traces')
ax2.set_xticks(x)
ax2.set_xticklabels(conditions, fontsize=7)
ax2.set_ylim(0, 15)
ax2.set_title('(b) Independence Deficit ($K$=12)')

handles = [
    plt.Rectangle((0,0), 1, 1, fc='#E0E0E0', ec='#999'),
    plt.Rectangle((0,0), 1, 1, fc='#888', ec='#333', alpha=0.85),
]
ax2.legend(handles, ['Nominal $K$', 'Eff-$K$'], loc='upper right',
           framealpha=0.9, edgecolor='#ccc', fontsize=8)

plt.tight_layout(w_pad=2.5)

out = '/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/figures/paper'
fig.savefig(f'{out}/f3_k_sensitivity.pdf')
fig.savefig(f'{out}/f3_k_sensitivity.png')
plt.close()
print(f'Done. Panel (a): {len(k_vals)} K values. Panel (b): {len(conditions)} conditions.')
