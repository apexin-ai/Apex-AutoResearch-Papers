import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import pandas as pd
import numpy as np
from scipy.optimize import curve_fit

# ---------- data ----------
df = pd.read_csv(
    '/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/'
    'artifacts/_project/supplement/data/features_all_models.csv'
)

features = ['entropy_mean', 'entropy_std', 'entropy_min', 'entropy_max',
            'tail_decay', 'ttr', 'hapax_ratio']

# per-generator mean at each depth, then cross-generator mean +/- std
agg = df.groupby(['model_name', 'depth'])[features].mean()
cross = agg.groupby('depth').agg(['mean', 'std'])

depths = np.array([0, 1, 2, 3, 4])

feat_data = {}
for f in features:
    y_mean = cross[(f, 'mean')].values
    y_std  = cross[(f, 'std')].values
    mn, mx = y_mean.min(), y_mean.max()
    if mx - mn < 1e-12:
        y_norm = np.zeros_like(y_mean)
        s_norm = np.zeros_like(y_std)
    else:
        y_norm = (y_mean - mn) / (mx - mn)
        s_norm = y_std / (mx - mn)
    feat_data[f] = (y_norm, s_norm)

# ---------- groups ----------
drifting     = ['entropy_mean', 'ttr', 'hapax_ratio']
intermediate = ['entropy_std']
stationary   = ['entropy_max', 'tail_decay', 'entropy_min']

colors = {
    'entropy_mean': '#D6604D', 'ttr': '#C14D3A', 'hapax_ratio': '#E67E6E',
    'entropy_std':  '#7570B3',
    'entropy_max':  '#4393C3', 'tail_decay': '#2E7AAD', 'entropy_min': '#6BB0D4',
}
markers = {
    'entropy_mean': 'o', 'ttr': 's', 'hapax_ratio': '^',
    'entropy_std':  'D',
    'entropy_max':  'v', 'tail_decay': '<', 'entropy_min': '>',
}
labels = {
    'entropy_mean': 'Entropy (mean)', 'ttr': 'TTR',
    'hapax_ratio': 'Hapax ratio', 'entropy_std': 'Entropy (std)',
    'entropy_max': 'Entropy (max)', 'tail_decay': 'Tail decay',
    'entropy_min': 'Entropy (min)',
}
linestyles = {}
for f in drifting:     linestyles[f] = '-'
for f in intermediate: linestyles[f] = '--'
for f in stationary:   linestyles[f] = ':'

# ---------- exponential fit ----------
def exp_decay(x, a, b, c):
    return a * np.exp(-b * x) + c

fit_params = {}
for f in drifting:
    y, _ = feat_data[f]
    try:
        popt, _ = curve_fit(exp_decay, depths, y, p0=[1, 0.5, 0], maxfev=5000)
        fit_params[f] = popt
    except RuntimeError:
        pass

# ---------- plot ----------
plt.rcParams.update({
    'font.family': 'serif',
    'font.size': 7,
    'axes.linewidth': 0.6,
    'xtick.major.width': 0.5,
    'ytick.major.width': 0.5,
    'xtick.major.size': 2.5,
    'ytick.major.size': 2.5,
})

fig, (ax1, ax2) = plt.subplots(
    2, 1, figsize=(3.25, 3.6), sharex=True,
    gridspec_kw={'hspace': 0.12, 'height_ratios': [1.15, 1]}
)

x_fine = np.linspace(0, 4, 200)

def plot_feature(ax, f):
    y, s = feat_data[f]
    ax.plot(depths, y, color=colors[f], marker=markers[f], markersize=3.5,
            linestyle=linestyles[f], linewidth=1.1, label=labels[f],
            zorder=3, markeredgewidth=0.4, markeredgecolor='white')
    ax.fill_between(depths, y - s, y + s, color=colors[f], alpha=0.12,
                    linewidth=0, zorder=1)

# upper: drifting + intermediate
for f in drifting:
    plot_feature(ax1, f)
    if f in fit_params:
        a, b, c = fit_params[f]
        y_fit = exp_decay(x_fine, a, b, c)
        ax1.plot(x_fine, y_fit, color=colors[f],
                 linestyle='--', linewidth=0.65, alpha=0.5, zorder=2)

for f in intermediate:
    plot_feature(ax1, f)

# lower: near-stationary
for f in stationary:
    plot_feature(ax2, f)

# ---------- styling ----------
for ax in (ax1, ax2):
    ax.set_xticks(depths)
    ax.yaxis.grid(True, color='#cccccc', alpha=0.35, linewidth=0.4)
    ax.set_axisbelow(True)
    ax.tick_params(labelsize=7)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

ax1.set_ylim(-0.25, 1.2)
ax2.set_ylim(-0.6, 1.6)
ax2.set_xlabel('Generation depth', fontsize=8)
ax1.set_ylabel('Normalized value\n(drifting)', fontsize=7.5, linespacing=1.1)
ax2.set_ylabel('Normalized value\n(stationary)', fontsize=7.5, linespacing=1.1)

# legends with convergence rate for drifting
leg1_labels = []
leg1_handles = []
for f in drifting + intermediate:
    lbl = labels[f]
    if f in fit_params:
        b_val = fit_params[f][1]
        lbl += rf'  ($\lambda$={b_val:.2f})'
    h = plt.Line2D([0], [0], color=colors[f], marker=markers[f],
                    markersize=3, linestyle=linestyles[f], linewidth=1,
                    label=lbl)
    leg1_handles.append(h)

ax1.legend(handles=leg1_handles, fontsize=6, loc='lower left',
           framealpha=0, edgecolor='none', handlelength=2.0,
           borderpad=0.35, labelspacing=0.25, handletextpad=0.5)

leg2_handles = [
    plt.Line2D([0], [0], color=colors[f], marker=markers[f],
               markersize=3, linestyle=linestyles[f], linewidth=1,
               label=labels[f])
    for f in stationary
]
ax2.legend(handles=leg2_handles, fontsize=6, loc='lower left',
           framealpha=0, edgecolor='none', handlelength=2.0,
           borderpad=0.35, labelspacing=0.25, handletextpad=0.5)

# subplot labels
ax1.text(0.01, 0.95, '(a)', transform=ax1.transAxes, fontsize=8,
         fontweight='bold', va='top')
ax2.text(0.01, 0.95, '(b)', transform=ax2.transAxes, fontsize=8,
         fontweight='bold', va='top')

out_base = ('/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/'
            'gen-depth-fingerprint/artifacts/_project/chart/fig_convergence_dynamics')
fig.savefig(out_base + '.pdf', dpi=300, bbox_inches='tight')
fig.savefig(out_base + '.png', dpi=300, bbox_inches='tight')
plt.close()

# ---------- report ----------
for f in drifting:
    if f in fit_params:
        a, b, c = fit_params[f]
        print(f'{labels[f]}: a={a:.3f}, b={b:.3f}, c={c:.3f}')
    else:
        print(f'{labels[f]}: fit failed')

import os
for ext in ('.pdf', '.png'):
    p = out_base + ext
    print(f'{p}: {os.path.getsize(p)} bytes')
