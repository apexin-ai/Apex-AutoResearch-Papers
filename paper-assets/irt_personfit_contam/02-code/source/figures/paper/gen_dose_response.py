"""
Dose-response curve: Cohen's |d| vs contamination level.
Round 3: Fix annotation clipping, legend order, fill_between continuity.
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patheffects as pe
import numpy as np

plt.rcParams.update({
    'font.family': 'DejaVu Sans',
    'font.size': 8,
    'axes.titlesize': 9,
    'axes.labelsize': 9,
    'xtick.labelsize': 8,
    'ytick.labelsize': 8,
    'legend.fontsize': 7.5,
    'figure.dpi': 300,
    'savefig.dpi': 300,
    'savefig.bbox': 'tight',
    'savefig.pad_inches': 0.03,
    'axes.spines.top': False,
    'axes.spines.right': False,
    'pdf.fonttype': 42,
    'ps.fonttype': 42,
    'lines.linewidth': 1.5,
})

C_BASELINE = '#2166ac'
C_COLLAPSE = '#b2182b'
C_NEUTRAL  = '#4393c3'
C_SAFE     = '#999999'

x = np.array([0, 1, 2, 3])

qwen_free_d   = np.array([4.15, 5.36, 7.44, 5.08])
qwen_free_sd  = np.array([0.0,  1.10, 1.86, 3.02])

qwen_fixed_d  = np.array([3.52, 6.85, 5.89, 12.32])
qwen_fixed_sd = np.array([0.0,  1.80, 1.27, 2.38])

llama_free_d  = np.array([2.57, 2.80, 2.56, 2.30])
llama_free_sd = np.array([0.99, 0.60, 0.52, 0.30])

fig, ax = plt.subplots(figsize=(3.4, 2.7))

# Reference line
ax.axhline(y=0.8, color=C_SAFE, linestyle=':', linewidth=0.6, alpha=0.35, zorder=1)
ax.text(3.35, 1.05, '$|d|{=}0.8$', fontsize=5.5, color=C_SAFE, alpha=0.5,
        va='bottom', ha='right')

# --- Llama free-θ ---
ax.fill_between(x, llama_free_d - llama_free_sd,
                llama_free_d + llama_free_sd,
                alpha=0.10, color=C_NEUTRAL, zorder=2)
ax.plot(x, llama_free_d, '^-', color=C_NEUTRAL, markersize=5,
        zorder=4, label='Llama free-$\\theta$', linewidth=1.2)

# --- Qwen free-θ ---
# Continuous fill_between (use small SD placeholder at 5% for visual continuity)
qf_sd_vis = qwen_free_sd.copy()
qf_sd_vis[0] = 0.3  # placeholder for visual continuity
ax.fill_between(x, qwen_free_d - qf_sd_vis,
                qwen_free_d + qf_sd_vis,
                alpha=0.10, color=C_BASELINE, zorder=2)
ax.plot(x, qwen_free_d, 'o-', color=C_BASELINE, markersize=5.5,
        zorder=5, label='Qwen free-$\\theta$')
# Hollow marker for 5% (single-seed)
ax.plot(x[0], qwen_free_d[0], 'o', color=C_BASELINE, markersize=5.5,
        markerfacecolor='white', markeredgecolor=C_BASELINE,
        markeredgewidth=1.2, zorder=6)

# --- Qwen fixed-θ ---
ax.plot(x, qwen_fixed_d, 's--', color=C_COLLAPSE, markersize=5.5,
        zorder=5, label='Qwen fixed-$\\theta$', linewidth=1.5)
for i in range(len(x)):
    if qwen_fixed_sd[i] > 0:
        ax.errorbar(x[i], qwen_fixed_d[i], yerr=qwen_fixed_sd[i],
                    fmt='none', ecolor=C_COLLAPSE, capsize=2.5,
                    capthick=0.8, elinewidth=0.8, zorder=4)
ax.plot(x[0], qwen_fixed_d[0], 's', color=C_COLLAPSE, markersize=5.5,
        markerfacecolor='white', markeredgecolor=C_COLLAPSE,
        markeredgewidth=1.2, zorder=6)

# --- Annotations ---
# θ-shift absorption: curved arrow from peak to dip
ax.annotate('',
            xy=(3, 5.35), xycoords='data',
            xytext=(2, 7.44), textcoords='data',
            arrowprops=dict(arrowstyle='->', color=C_BASELINE,
                            lw=0.9, connectionstyle='arc3,rad=0.25'))
t_abs = ax.text(2.3, 5.0, '$\\theta$-shift\nabsorption',
                fontsize=6.5, color=C_BASELINE, ha='left', va='top',
                linespacing=1.1)
t_abs.set_path_effects([pe.withStroke(linewidth=2, foreground='white')])

# θ-anchoring annotation
t_fix = ax.text(2.3, 14.2, '$\\theta$-anchoring\nrecovers signal',
                fontsize=6.5, color=C_COLLAPSE, ha='center', va='bottom',
                fontstyle='italic', linespacing=1.1)
t_fix.set_path_effects([pe.withStroke(linewidth=2, foreground='white')])

# Single-seed notation
ax.text(-0.18, 4.6, '$n{=}1$', fontsize=5.5, color=C_SAFE, fontstyle='italic')

# --- Axes ---
ax.set_xticks(x)
ax.set_xticklabels(['5%', '15%', '25%', '50%'])
ax.set_xlabel('Contamination level')
ax.set_ylabel("Cohen's $|d|$")
ax.set_ylim(0, 15.5)
ax.set_xlim(-0.4, 3.5)

# Legend: group by model (Qwen pair first, then Llama)
handles, labels = ax.get_legend_handles_labels()
order = [1, 2, 0]  # Qwen free, Qwen fixed, Llama
ax.legend([handles[i] for i in order], [labels[i] for i in order],
          loc='upper left', framealpha=0.92, edgecolor='none',
          handlelength=1.8, handletextpad=0.4)

plt.tight_layout()
outdir = '/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/figures/paper'
plt.savefig(f'{outdir}/fig_dose_response.pdf')
plt.savefig(f'{outdir}/fig_dose_response.png')
plt.close()
print('Saved fig_dose_response.pdf and .png')
