import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patheffects as pe
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
    'pdf.fonttype': 42,
    'ps.fonttype': 42,
    'lines.linewidth': 1.8,
})

OUTDIR = '/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/figures/paper'

# Data
k_vals = [1, 5, 10]
means = [10.33, 16.0, 16.8]
stds = [1.53, 2.16, 1.83]
n_samples = [3, 7, 6]

vla_baseline = 11.3
vla_std = 1.14
argmin_baseline = 12.3
argmin_std = 2.6

# Figure: 4:3 aspect
fig, ax = plt.subplots(figsize=(5.5, 4.125))

# --- Pattern C: Reference lines ---
# VLA-only baseline
ax.axhline(y=vla_baseline, color='#999999', linestyle='--', linewidth=1.0, zorder=1)
t_vla = ax.text(10.3, vla_baseline + 0.35, 'VLA-only baseline (11.3%)',
                fontsize=8, color='#777777', va='bottom', ha='right')
t_vla.set_path_effects([pe.withStroke(linewidth=2.5, foreground='white')])

# Argmin selection baseline
ax.axhline(y=argmin_baseline, color='#009E73', linestyle=':', linewidth=1.0, zorder=1)
t_arg = ax.text(10.3, argmin_baseline + 0.35, 'Argmin selection, K=10 (12.3%)',
                fontsize=8, color='#009E73', va='bottom', ha='right')
t_arg.set_path_effects([pe.withStroke(linewidth=2.5, foreground='white')])

# --- Main line: CRM with K samples ---
color_main = '#0072B2'

# Plot connecting line first (all points)
ax.plot(k_vals, means, '-', color=color_main, linewidth=2.0, zorder=3)

# K=1: solid marker with error bar (n=3)
ax.errorbar(1, means[0], yerr=stds[0], fmt='o', color=color_main,
            markersize=8, markeredgecolor='white', markeredgewidth=1.0,
            capsize=4, capthick=1.0, elinewidth=1.0, zorder=4)

# K=5: solid marker with error bar (n=2)
ax.errorbar(5, means[1], yerr=stds[1], fmt='o', color=color_main,
            markersize=8, markeredgecolor='white', markeredgewidth=1.0,
            capsize=4, capthick=1.0, elinewidth=1.0, zorder=4)
t_n2 = ax.annotate('n=7', (5, means[1]), xytext=(6, 8),
                    textcoords='offset points', fontsize=7,
                    color=color_main, fontstyle='italic')
t_n2.set_path_effects([pe.withStroke(linewidth=2.0, foreground='white')])

# K=10: solid marker with error bar (n=6)
ax.errorbar(10, means[2], yerr=stds[2], fmt='o', color=color_main,
            markersize=8, markeredgecolor='white', markeredgewidth=1.0,
            capsize=4, capthick=1.0, elinewidth=1.0, zorder=4)

# --- Annotations ---

# K=1: "correction alone ~ baseline"
t_k1 = ax.annotate('correction alone\n$\\approx$ baseline', xy=(1, means[0]),
                    xytext=(2.2, 7.5), fontsize=8, fontstyle='italic',
                    color='#555555',
                    arrowprops=dict(arrowstyle='->', color='#999999', lw=0.8))
t_k1.set_path_effects([pe.withStroke(linewidth=2.0, foreground='white')])

# K=10: result annotation
t_k10 = ax.annotate('16.8%', xy=(10, means[2]),
                     xytext=(-35, 12), textcoords='offset points',
                     fontsize=9, fontweight='bold', color=color_main,
                     arrowprops=dict(arrowstyle='->', color=color_main, lw=0.8))
t_k10.set_path_effects([pe.withStroke(linewidth=2.0, foreground='white')])

# --- Axes ---
ax.set_xlabel('Number of VLA samples (K)')
ax.set_ylabel('Success Rate (%)')
ax.set_xticks(k_vals)
ax.set_xticklabels(['1', '5', '10'])
ax.set_xlim(-0.5, 11.5)
ax.set_ylim(5, 22)
ax.set_yticks([6, 8, 10, 12, 14, 16, 18, 20])

# Light grid on y-axis only
ax.grid(True, axis='y', alpha=0.2, zorder=0)

# Direct label on the main line
t_label = ax.text(7.5, 15.0, 'CRM refinement', fontsize=9,
                  color=color_main, fontweight='bold', rotation=5)
t_label.set_path_effects([pe.withStroke(linewidth=2.5, foreground='white')])

plt.tight_layout()

# Save PDF + PNG
pdf_path = f'{OUTDIR}/fig3_kvalue.pdf'
png_path = f'{OUTDIR}/fig3_kvalue.png'
plt.savefig(pdf_path)
plt.savefig(png_path)
plt.close()
print(f'Saved: {pdf_path}')
print(f'Saved: {png_path}')
