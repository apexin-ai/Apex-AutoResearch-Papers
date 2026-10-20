import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams.update({
    'font.family': 'DejaVu Sans',
    'font.size': 9,
    'axes.labelsize': 9,
    'xtick.labelsize': 8,
    'ytick.labelsize': 8,
    'figure.dpi': 300,
    'savefig.dpi': 300,
    'savefig.bbox': 'tight',
    'savefig.pad_inches': 0.05,
    'axes.spines.top': False,
    'axes.spines.right': False,
    'lines.linewidth': 2.0,
})

alpha = np.linspace(0, 1.02, 1000)

# S(α): monotonic sigmoid
s = 1.0 / (1.0 + np.exp(-22 * (alpha - 0.47)))

# R(α): flat with sync-collapse dip at α≈0.60
r = 0.88 - 0.62 * np.exp(-((alpha - 0.60) ** 2) / (2 * 0.055 ** 2))

sr = s * r

# Regime boundaries
B1, B2, B3 = 0.45, 0.55, 0.68
bounds = [0, B1, B2, B3, 1.02]
bg = ['#e8e8e8', '#c8e6c9', '#ffcdd2', '#bbdefb']
threshold = 0.37

# Staggered regime labels: (x_data, y_axes, label, fontsize)
# Alternate y heights so adjacent labels don't overlap horizontally
regime_labels = [
    (0.225, 1.025, 'Blind',     6.5),
    (0.50,  1.085, 'Onset',     6.0),
    (0.615, 1.025, 'Sync col.', 5.8),
    (0.85,  1.085, 'Detection', 6.5),
]

fig, (ax_a, ax_b, ax_c) = plt.subplots(1, 3, figsize=(6.5, 2.5))
plt.subplots_adjust(wspace=0.33, top=0.82, bottom=0.19, left=0.065, right=0.975)

# ── Shared setup ──
for ax in (ax_a, ax_b, ax_c):
    for i in range(4):
        ax.axvspan(bounds[i], bounds[i + 1], color=bg[i], alpha=0.35, lw=0, zorder=0)
    for b in (B1, B2, B3):
        ax.axvline(b, color='#bbbbbb', ls='--', lw=0.6, zorder=1)
    ax.set_xlim(0, 1.02)
    ax.set_ylim(-0.03, 1.08)
    ax.set_xticks([0, 0.25, 0.50, 0.75, 1.0])
    ax.set_xlabel(r'Contamination $\alpha$', fontsize=8)
    for x, y, lab, fs in regime_labels:
        ax.text(x, y, lab, transform=ax.get_xaxis_transform(),
                ha='center', va='bottom', fontsize=fs, fontstyle='italic',
                color='#555555', clip_on=False)

# ── Panel A: S(α) ──
ax_a.plot(alpha, s, color='#0072B2', lw=2.0, zorder=3)
ax_a.set_ylabel('Magnitude (schematic)', fontsize=7.5)
ax_a.set_title(r'(a)  Signal strength $\mathcal{S}(\alpha)$',
               fontsize=9, fontweight='bold', pad=22, loc='left')
ax_a.text(0.15, 0.14, 'weak', fontsize=7, color='#0072B2', ha='center',
          fontstyle='italic', alpha=0.7)
ax_a.text(0.88, 0.78, 'strong', fontsize=7, color='#0072B2', ha='center',
          fontstyle='italic', alpha=0.7)

# ── Panel B: R(α) ──
ax_b.plot(alpha, r, color='#D55E00', lw=2.0, zorder=3)
ax_b.set_title(r'(b)  Resolving power $\mathcal{R}(\alpha)$',
               fontsize=9, fontweight='bold', pad=22, loc='left')
ax_b.annotate('', xy=(0.60, 0.30), xytext=(0.60, 0.56),
              arrowprops=dict(arrowstyle='->', color='#D55E00', lw=1.2,
                              shrinkA=0, shrinkB=2))
ax_b.text(0.62, 0.58, 'sync-collapse\ndip', fontsize=6.5, color='#D55E00',
          ha='left', va='bottom', fontstyle='italic', linespacing=0.85)

# ── Panel C: S×R ──
ax_c.plot(alpha, sr, color='#222222', lw=2.2, zorder=3)
ax_c.axhline(threshold, color='#888888', ls=':', lw=1.2, zorder=2)
ax_c.set_title(r'(c)  Detectability $\mathcal{S}\!\times\!\mathcal{R}$',
               fontsize=9, fontweight='bold', pad=22, loc='left')

ax_c.text(1.04, threshold, r'$\tau_{\mathrm{det}}$', fontsize=8,
          color='#666666', va='center', ha='left', clip_on=False)

ax_c.fill_between(alpha, sr, threshold, where=(sr >= threshold),
                  color='#0072B2', alpha=0.10, zorder=2)
mask_sc = (alpha >= B1) & (alpha <= B3) & (sr < threshold)
ax_c.fill_between(alpha, sr, threshold, where=mask_sc,
                  color='#D55E00', alpha=0.08, zorder=2)

# callout: onset peak
i_pk = np.argmax(sr[(alpha >= 0.47) & (alpha <= 0.54)])
a_pk = alpha[(alpha >= 0.47) & (alpha <= 0.54)][i_pk]
v_pk = sr[(alpha >= 0.47) & (alpha <= 0.54)][i_pk]
ax_c.annotate('onset\npeak', xy=(a_pk, v_pk),
              xytext=(0.20, 0.80), fontsize=6.5, color='#333333',
              ha='center', linespacing=0.85,
              arrowprops=dict(arrowstyle='->', color='#555555', lw=0.8))

# callout: collapse trough
i_tr = np.argmin(sr[(alpha >= 0.55) & (alpha <= 0.68)])
a_tr = alpha[(alpha >= 0.55) & (alpha <= 0.68)][i_tr]
v_tr = sr[(alpha >= 0.55) & (alpha <= 0.68)][i_tr]
ax_c.annotate('trough', xy=(a_tr, v_tr),
              xytext=(0.82, 0.15), fontsize=6.5, color='#333333',
              ha='center',
              arrowprops=dict(arrowstyle='->', color='#555555', lw=0.8))

out = '/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/figures'
fig.savefig(f'{out}/fig_sr_framework.pdf', format='pdf')
fig.savefig(f'{out}/fig_sr_framework.png', format='png', dpi=300)
plt.close()
print(f'Saved to {out}/fig_sr_framework.{{pdf,png}}')
