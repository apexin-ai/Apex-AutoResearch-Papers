import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import numpy as np
import json
import os

# ---------- load data from JSON ----------
_script_dir = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(_script_dir, 'magnitude_curve_data.json')) as f:
    _data = json.load(f)

_eps_order = ["0.03", "0.05", "0.1", "0.2", "0.3", "default"]
_DEFAULT_X = 1.42

eps = [float(e) if e != "default" else _DEFAULT_X for e in _eps_order]

def _extract(section):
    means, stds, ns = [], [], []
    for key in _eps_order:
        entry = section[key]
        means.append(entry["mean"] * 100)
        stds.append(entry["std"] * 100 if entry["n_seeds"] >= 2 else None)
        ns.append(entry["n_seeds"])
    return means, stds, ns

obs_mean, obs_std, obs_n = _extract(_data["obs_only"])
per_mean, per_std, per_n = _extract(_data["perdof"])

_argmin = _data["baselines"]["argmin"]
argmin_mean = _argmin["mean"] * 100
argmin_std = _argmin["std"] * 100
argmin_n = _argmin["n_seeds"]

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
           label=f'Argmin (n={argmin_n}, {argmin_mean:.0f}%$\\pm${argmin_std:.1f})')
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

# ---------- seed count annotations ----------
for i, (x, n) in enumerate(zip(eps, obs_n)):
    if n >= 4:
        ax.annotate(f'n={n}', xy=(x, obs_mean[i]), xytext=(0, 6),
                    textcoords='offset points', fontsize=7, color='#2166AC',
                    ha='center', va='bottom')

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
_figures_dir = os.path.join(_script_dir, 'figures')
os.makedirs(_figures_dir, exist_ok=True)
fig.savefig(os.path.join(_figures_dir, 'magnitude_curve.pdf'), bbox_inches='tight', dpi=300)
fig.savefig(os.path.join(_figures_dir, 'magnitude_curve.png'), bbox_inches='tight', dpi=300)
fig.savefig(os.path.join(_script_dir, 'magnitude_curve.pdf'), bbox_inches='tight', dpi=300)
fig.savefig(os.path.join(_script_dir, 'magnitude_curve.png'), bbox_inches='tight', dpi=300)
print('saved: figures/magnitude_curve.pdf, figures/magnitude_curve.png')
