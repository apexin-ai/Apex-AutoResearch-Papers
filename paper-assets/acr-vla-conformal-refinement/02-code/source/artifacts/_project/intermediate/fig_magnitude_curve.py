import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import numpy as np

# ---------- data (from magnitude_multiseed_data.md, ground truth) ----------
eps = [0.03, 0.05, 0.10, 0.20, 0.30, 1.42]

# obs_only: mean SR (%) per norm
obs_mean = [16.0, 13.0, 15.7, 17.5, 18.5, 16.5]
obs_std  = [None, None, 3.5,  3.0,  0.7,  0.7]
obs_n    = [1,    1,    3,    4,    2,    2]

# perdof: mean SR (%) per norm
per_mean = [14.0, 14.0, 10.3, 10.0, 4.0,  0.0]
per_std  = [None, None, 2.1,  1.4,  None, None]
per_n    = [1,    1,    3,    2,    1,    1]

# argmin baseline: mean=14.0%, std=2.6, n=3
argmin_mean = 14.0
argmin_std  = 2.6

# ---------- style ----------
plt.rcParams.update({
    'font.family': 'serif',
    'font.serif': ['Times New Roman', 'DejaVu Serif'],
    'font.size': 11,
    'axes.linewidth': 0.8,
    'xtick.major.width': 0.8,
    'ytick.major.width': 0.8,
    'xtick.direction': 'in',
    'ytick.direction': 'in',
    'xtick.major.pad': 4,
    'ytick.major.pad': 4,
    'legend.framealpha': 0.95,
    'legend.edgecolor': '0.8',
})

fig, ax = plt.subplots(figsize=(5.0, 3.4))

# ---------- per-DOF collapse shading ----------
_xfine = np.logspace(np.log10(0.27), np.log10(1.8), 200)
_yfine = np.interp(_xfine, eps, per_mean)
ax.fill_between(_xfine, 0, _yfine, color='#D6604D', alpha=0.10, zorder=0)
ax.text(0.62, 5.5, 'per-DOF\ncollapse region', fontsize=8, color='#CC4444',
        ha='center', va='bottom', fontstyle='italic')

# ---------- argmin baseline with shaded band ----------
ax.axhline(argmin_mean, color='0.55', ls='--', lw=1.0, zorder=1,
           label=f'Argmin (n=3, {argmin_mean:.0f}%$\\pm${argmin_std:.1f})')
ax.axhspan(argmin_mean - argmin_std, argmin_mean + argmin_std,
           color='0.55', alpha=0.10, zorder=0)

# ---------- obs_only: shaded error regions where multi-seed ----------
eps_arr = np.array(eps)
obs_mean_arr = np.array(obs_mean)

# multi-seed points (n >= 2): shaded region
multi_idx = [i for i, n in enumerate(obs_n) if n >= 2]
if multi_idx:
    x_multi = eps_arr[multi_idx]
    y_multi = obs_mean_arr[multi_idx]
    std_multi = np.array([obs_std[i] for i in multi_idx])
    ax.fill_between(x_multi, y_multi - std_multi, y_multi + std_multi,
                    color='#2166AC', alpha=0.15, zorder=2)

# perdof: shaded error regions where multi-seed
per_mean_arr = np.array(per_mean)
multi_idx_p = [i for i, n in enumerate(per_n) if n >= 2]
if multi_idx_p:
    x_multi_p = eps_arr[multi_idx_p]
    y_multi_p = per_mean_arr[multi_idx_p]
    std_multi_p = np.array([per_std[i] for i in multi_idx_p])
    ax.fill_between(x_multi_p, y_multi_p - std_multi_p, y_multi_p + std_multi_p,
                    color='#D6604D', alpha=0.15, zorder=2)

# ---------- main curves ----------
# Single-seed points: open markers; multi-seed: filled markers
obs_single = [i for i, n in enumerate(obs_n) if n == 1]
obs_multi  = [i for i, n in enumerate(obs_n) if n >= 2]

ax.plot(eps, obs_mean, '-', color='#2166AC', lw=1.8, zorder=3)
ax.plot(eps_arr[obs_multi], obs_mean_arr[obs_multi], 'o', color='#2166AC',
        ms=6, mew=0, zorder=4, label='Obs-Only CRM (multi-seed)')
ax.plot(eps_arr[obs_single], obs_mean_arr[obs_single], 'o', color='#2166AC',
        ms=6, mew=1.2, mfc='white', zorder=4, label='Obs-Only CRM (single seed)')

per_single = [i for i, n in enumerate(per_n) if n == 1]
per_multi  = [i for i, n in enumerate(per_n) if n >= 2]

ax.plot(eps, per_mean, '-', color='#D6604D', lw=1.8, zorder=3)
ax.plot(eps_arr[per_multi], per_mean_arr[per_multi], '^', color='#D6604D',
        ms=6, mew=0, zorder=4, label='Per-DOF CRM (multi-seed)')
ax.plot(eps_arr[per_single], per_mean_arr[per_single], '^', color='#D6604D',
        ms=6, mew=1.2, mfc='white', zorder=4, label='Per-DOF CRM (single seed)')

# ---------- perdof zero annotation ----------
ax.annotate('0%',
            xy=(1.42, 0), xytext=(0.75, 4.0),
            fontsize=9.5, fontweight='bold', color='#D6604D',
            arrowprops=dict(arrowstyle='->', color='#D6604D', lw=0.9),
            zorder=5)

# ---------- axes ----------
ax.set_xscale('log')
ax.set_xlim(0.025, 1.8)
ax.set_ylim(-1, 25)

ax.set_xticks(eps)
ax.xaxis.set_major_formatter(mticker.FuncFormatter(
    lambda v, _: 'uncapped' if v > 1.0 else f'{v:g}'))
ax.xaxis.set_minor_formatter(mticker.NullFormatter())
ax.tick_params(axis='x', which='minor', length=0)

ax.set_xlabel('Correction Magnitude Norm ($\\varepsilon$)', fontsize=11)
ax.set_ylabel('10-Task Success Rate (%)', fontsize=11)

# ---------- grid ----------
ax.grid(True, which='major', ls='--', lw=0.4, color='0.82', zorder=0)
ax.set_axisbelow(True)

# ---------- legend ----------
leg = ax.legend(loc='upper center', fontsize=7.5, handlelength=1.8,
                borderpad=0.4, labelspacing=0.3, ncol=2,
                bbox_to_anchor=(0.5, 1.18), columnspacing=1.0,
                frameon=False)

fig.tight_layout(pad=0.5)
fig.subplots_adjust(top=0.84)

# ---------- save ----------
out = '/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/figures/'
import os
os.makedirs(out, exist_ok=True)
fig.savefig(out + 'magnitude_curve.pdf', bbox_inches='tight', dpi=300)
fig.savefig(out + 'magnitude_curve.png', bbox_inches='tight', dpi=300)
# Also save to artifacts root for backward compat
root = '/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/'
fig.savefig(root + 'magnitude_curve.pdf', bbox_inches='tight', dpi=300)
fig.savefig(root + 'magnitude_curve.png', bbox_inches='tight', dpi=300)
print('saved: figures/magnitude_curve.pdf, figures/magnitude_curve.png')
