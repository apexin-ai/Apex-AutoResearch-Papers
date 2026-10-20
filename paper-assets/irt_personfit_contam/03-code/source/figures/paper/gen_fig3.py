import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from pathlib import Path

matplotlib.rcParams.update({
    'font.family': 'serif',
    'font.serif': ['Liberation Serif', 'DejaVu Serif'],
    'font.size': 8,
    'axes.labelsize': 8,
    'axes.titlesize': 9,
    'xtick.labelsize': 7,
    'ytick.labelsize': 7,
    'legend.fontsize': 6.5,
    'text.usetex': False,
    'figure.dpi': 300,
    'savefig.dpi': 300,
    'savefig.bbox': 'tight',
    'savefig.pad_inches': 0.05,
    'axes.linewidth': 0.6,
    'xtick.major.width': 0.5,
    'ytick.major.width': 0.5,
    'xtick.major.size': 3,
    'ytick.major.size': 3,
})

# === Data (n=3 clean seeds, ddof=1) ===
conditions = ['Clean s1', 'Clean s2', 'Clean s3', 'Contam 15%', 'Contam 50%']
lz_free  = [8.01, 5.94, 8.08, 3.00, 5.45]
lz_fixed = [7.95, 6.30, 7.78, 10.02, 15.71]
clean_baseline_mean = 7.345
clean_baseline_std  = 1.214
delta_free  = [0.67, -1.40, 0.74, -4.34, -1.90]
delta_fixed = [0.61, -1.04, 0.44, 2.68, 8.36]
theta = [-0.0987, -0.0842, -0.1068, 0.1971, 0.3703]
theta_fixed = -0.0966
accuracy_overall = [0.679, 0.679, 0.678, 0.731, 0.764]
accuracy_seen    = [None, None, None, 0.824, 0.805]
accuracy_unseen  = [None, None, None, 0.715, 0.724]
mem_frac_15 = 0.38
mem_frac_50 = 0.29

# === Colors ===
C_CLEAN1 = '#4393c3'
C_CLEAN2 = '#74add1'
C_CLEAN3 = '#a6d0e4'
C_CONTAM15 = '#e08214'
C_CONTAM50 = '#b2182b'
bar_colors = [C_CLEAN1, C_CLEAN2, C_CLEAN3, C_CONTAM15, C_CONTAM50]

C_FREE  = '#2166ac'
C_FIXED = '#92c5de'

C_OVERALL = '#888888'
C_SEEN    = '#b2182b'
C_UNSEEN  = '#1b7837'

# === Figure ===
fig, axes = plt.subplots(1, 3, figsize=(7.2, 2.8),
                         gridspec_kw={'width_ratios': [1.4, 0.8, 1.2], 'wspace': 0.38})

# ── Panel (a): lz* Free-θ vs Fixed-θ ──
ax = axes[0]
x = np.arange(len(conditions))
w = 0.32

bars_free = ax.bar(x - w/2, lz_free, w, color=C_FREE, edgecolor='white',
                   linewidth=0.4, label='Free-θ', zorder=3)
bars_fixed = ax.bar(x + w/2, lz_fixed, w, color=C_FIXED, edgecolor='white',
                    linewidth=0.4, label='Fixed-θ', zorder=3)

ax.axhspan(clean_baseline_mean - clean_baseline_std,
           clean_baseline_mean + clean_baseline_std,
           color='#dddddd', alpha=0.5, zorder=1)
ax.axhline(clean_baseline_mean, color='#999999', linewidth=0.7,
           linestyle='--', zorder=2)
ax.text(4.55, clean_baseline_mean + 0.3, 'clean μ±σ', fontsize=5.5,
        color='#777777', ha='right')

for i, (df_, dx_) in enumerate(zip(delta_free, delta_fixed)):
    sign_f = '+' if df_ >= 0 else ''
    sign_x = '+' if dx_ >= 0 else ''
    ax.text(x[i] - w/2, lz_free[i] + 0.3, f'{sign_f}{df_:.1f}',
            ha='center', va='bottom', fontsize=5, color=C_FREE, fontweight='bold')
    ax.text(x[i] + w/2, lz_fixed[i] + 0.3, f'{sign_x}{dx_:.1f}',
            ha='center', va='bottom', fontsize=5, color='#3a7fb5', fontweight='bold')

ax.text(0.55, 0.97, 'Free-θ: non-monotonic', fontsize=5.5, color=C_FREE,
        ha='left', va='top', transform=ax.transAxes, fontweight='bold')
ax.text(0.55, 0.89, 'Fixed-θ: monotonic', fontsize=5.5, color='#3a7fb5',
        ha='left', va='top', transform=ax.transAxes, fontweight='bold')

ax.set_xticks(x)
ax.set_xticklabels(conditions, rotation=15, ha='right')
ax.set_ylabel('$\\ell_z^*$ statistic')
ax.set_ylim(0, 19)
ax.set_title('(a) $\\ell_z^*$ under Free-θ vs Fixed-θ', fontsize=8, pad=6)
ax.legend(loc='upper left', framealpha=0.9, edgecolor='#cccccc',
          borderpad=0.3, handlelength=1.2)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

# ── Panel (b): Memorization Fingerprint ──
ax = axes[1]
cond_labels = ['Contam\n15%', 'Contam\n50%']
x_b = np.arange(2)
w_b = 0.22

vals_overall = [accuracy_overall[3], accuracy_overall[4]]
vals_seen    = [accuracy_seen[3], accuracy_seen[4]]
vals_unseen  = [accuracy_unseen[3], accuracy_unseen[4]]

ax.bar(x_b - w_b, vals_overall, w_b, color=C_OVERALL, edgecolor='white',
       linewidth=0.4, label='Overall', zorder=3)
ax.bar(x_b, vals_seen, w_b, color=C_SEEN, edgecolor='white',
       linewidth=0.4, label='Seen', zorder=3)
ax.bar(x_b + w_b, vals_unseen, w_b, color=C_UNSEEN, edgecolor='white',
       linewidth=0.4, label='Unseen', zorder=3)

clean_acc_mean = np.mean([0.679, 0.679, 0.678])
ax.axhline(clean_acc_mean, color='#999999', linewidth=0.7, linestyle='--', zorder=2)
ax.text(1.38, clean_acc_mean - 0.008, 'clean', fontsize=5.5, color='#777777',
        ha='right', va='top')

for i, mf in enumerate([mem_frac_15, mem_frac_50]):
    x_arrow = x_b[i] + w_b + 0.06
    ax.annotate('', xy=(x_arrow, vals_seen[i]),
                xytext=(x_arrow, vals_unseen[i]),
                arrowprops=dict(arrowstyle='<->', color='#555555', lw=0.7,
                                shrinkA=1, shrinkB=1))
    mid_y = (vals_seen[i] + vals_unseen[i]) / 2
    ax.text(x_arrow + 0.06, mid_y, f'mem\n{mf:.0%}', fontsize=5,
            color='#555555', va='center', ha='left')

ax.set_xticks(x_b)
ax.set_xticklabels(cond_labels)
ax.set_ylabel('Accuracy')
ax.set_ylim(0.62, 0.87)
ax.set_yticks([0.65, 0.70, 0.75, 0.80, 0.85])
ax.set_title('(b) Memorization Fingerprint', fontsize=8, pad=6)
ax.legend(loc='upper left', framealpha=0.9, edgecolor='#cccccc',
          borderpad=0.3, handlelength=1.0, labelspacing=0.3)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

# ── Panel (c): θ-Shift Mechanism ──
ax = axes[2]
x_c = np.arange(len(conditions))

for i in range(len(conditions)):
    ax.bar(x_c[i], theta[i], 0.5, color=bar_colors[i], edgecolor='white',
           linewidth=0.4, zorder=3)

ax.axhline(theta_fixed, color='#999999', linewidth=0.7, linestyle='--', zorder=2)
ax.text(4.55, theta_fixed + 0.012, f'θ_fixed = {theta_fixed:.4f}',
        fontsize=5.5, color='#777777', ha='right')

clean_mean_theta = np.mean(theta[:3])
delta_15 = theta[3] - clean_mean_theta
delta_50 = theta[4] - clean_mean_theta

ax.annotate('', xy=(3, theta[3]), xytext=(3, clean_mean_theta),
            arrowprops=dict(arrowstyle='->', color=C_CONTAM15, lw=1.2,
                            shrinkA=1, shrinkB=1))
ax.text(3.35, (theta[3] + clean_mean_theta) / 2,
        f'Δθ={delta_15:+.2f}', fontsize=6, color=C_CONTAM15, fontweight='bold',
        va='center')

ax.annotate('', xy=(4, theta[4]), xytext=(4, clean_mean_theta),
            arrowprops=dict(arrowstyle='->', color=C_CONTAM50, lw=1.2,
                            shrinkA=1, shrinkB=1))
ax.text(4.35, (theta[4] + clean_mean_theta) / 2,
        f'Δθ={delta_50:+.2f}', fontsize=6, color=C_CONTAM50, fontweight='bold',
        va='center')

ax.axhline(clean_mean_theta, color=C_CLEAN1, linewidth=0.5, linestyle=':',
           alpha=0.5, zorder=1)

ax.set_xticks(x_c)
ax.set_xticklabels(conditions, rotation=15, ha='right')
ax.set_ylabel('θ (MLE)')
ax.set_ylim(-0.20, 0.50)
ax.set_title('(c) θ-Shift Mechanism', fontsize=8, pad=6)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

# === Save ===
out = Path(__file__).resolve().parent
fig.savefig(out / 'fig_3_ctrl_contam.pdf', format='pdf')
fig.savefig(out / 'fig_3_ctrl_contam.png', format='png')
plt.close()
print("Done. Files saved.")
