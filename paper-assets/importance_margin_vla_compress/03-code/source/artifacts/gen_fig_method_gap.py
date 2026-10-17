import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib.patheffects as pe
import numpy as np
import os

plt.rcParams.update({
    'font.family': 'DejaVu Sans',
    'font.size': 10,
    'axes.titlesize': 12,
    'axes.labelsize': 11,
    'xtick.labelsize': 10,
    'ytick.labelsize': 9.5,
    'legend.fontsize': 8.5,
    'figure.dpi': 300,
    'savefig.dpi': 300,
    'savefig.bbox': 'tight',
    'savefig.pad_inches': 0.1,
    'axes.spines.top': False,
    'axes.spines.right': False,
})

# ── Data ──
suites = ['Object', 'Spatial', 'Goal', 'Long-Horizon']
model_order = [r'$\pi$0.5', 'X-VLA', 'OpenVLA', 'SmolVLA']
cv_map = {r'$\pi$0.5': 0.055, 'X-VLA': 0.151, 'OpenVLA': 0.215, 'SmolVLA': 0.314}

gap_data = {
    r'$\pi$0.5':  [24.2, 21.0,  8.2, 23.8],
    'X-VLA':      [None,  1.4,  0.2,  1.2],
    'OpenVLA':    [ 1.4,  4.8,  4.8,  3.2],
    'SmolVLA':    [ 0.0,  0.0,  0.0,  0.0],
}

colors = {
    r'$\pi$0.5':  '#D55E00',
    'X-VLA':      '#0072B2',
    'OpenVLA':    '#56B4E9',
    'SmolVLA':    '#BBBBBB',
}

# ── Layout ──
n_suites = len(suites)
n_models = len(model_order)
bar_w = 0.17
gap_between = 0.035
x_base = np.arange(n_suites) * 1.2

fig, ax = plt.subplots(figsize=(7.5, 5.0))

# Method-independent zone (below 2pp)
ax.axhspan(0, 2, color='#F5F5F5', alpha=0.7, zorder=0)
ax.axhline(y=2, color='#CCCCCC', linestyle='--', linewidth=0.6, zorder=1)

for mi, model in enumerate(model_order):
    offset = (mi - (n_models - 1) / 2) * (bar_w + gap_between)
    vals = gap_data[model]

    for si in range(n_suites):
        pos = x_base[si] + offset
        val = vals[si]

        if val is None:
            t = ax.text(pos, 1.0, 'N/A', ha='center', va='bottom', fontsize=7.5,
                        color='#AAAAAA', fontstyle='italic')
            t.set_path_effects([pe.withStroke(linewidth=2.5, foreground='white')])
            continue

        bar_kw = dict(width=bar_w, color=colors[model], zorder=2,
                      edgecolor='white', linewidth=0.6)

        if model == 'SmolVLA':
            bar_kw.update(alpha=0.30, hatch='///', edgecolor='#999999',
                          linewidth=0.5)
            display_h = 0.5
        else:
            bar_kw['alpha'] = 0.88
            display_h = val

        ax.bar(pos, display_h, **bar_kw)

        if val == 0:
            t = ax.text(pos, display_h + 0.3, '0', ha='center', va='bottom',
                        fontsize=7.5, color='#999999', fontstyle='italic')
        elif val < 2:
            t = ax.text(pos, val + 0.3, f'{val:.1f}', ha='center', va='bottom',
                        fontsize=8, fontweight='bold', color=colors[model])
            t.set_path_effects([pe.withStroke(linewidth=2.5, foreground='white')])
        else:
            t = ax.text(pos, val + 0.3, f'{val:.1f}', ha='center', va='bottom',
                        fontsize=8, fontweight='bold', color=colors[model])
            t.set_path_effects([pe.withStroke(linewidth=2.5, foreground='white')])

# 2pp line label - right edge, above the dashed line
t = ax.text(x_base[-1] + 0.64, 2.15, '2 pp', fontsize=7, color='#AAAAAA',
            ha='right', va='bottom', fontstyle='italic')
t.set_path_effects([pe.withStroke(linewidth=2, foreground='white')])

# ── Axes ──
ax.set_xticks(x_base)
ax.set_xticklabels(suites, fontsize=10)
ax.set_ylabel('Method Gap (pp)', fontsize=11)
ax.set_ylim(0, 28)
ax.set_xlim(x_base[0] - 0.55, x_base[-1] + 0.68)

ax.set_title('Low CV amplifies pruning-method sensitivity',
             fontsize=11.5, fontweight='medium', pad=12)

# ── Legend ──
handles = []
for model in model_order:
    kw = dict(facecolor=colors[model], edgecolor='white', linewidth=0.5)
    if model == 'SmolVLA':
        kw.update(alpha=0.30, hatch='///', edgecolor='#999999')
        label = f'{model}  (CV={cv_map[model]:.3f})  [collapsed]'
    else:
        kw.update(alpha=0.88)
        label = f'{model}  (CV={cv_map[model]:.3f})'
    handles.append(mpatches.Patch(**kw, label=label))

ax.legend(handles=handles, loc='upper right', framealpha=0.95,
          edgecolor='#DDDDDD', fancybox=False, handlelength=1.4,
          borderpad=0.6)

# Footnote
fig.text(0.5, -0.025,
         r'Gap = $|\mathrm{SR_{L2\text{-}norm}} - \mathrm{SR_{Random}}|$ at $k$=0.95.'
         '  OpenVLA Spatial/Goal/Long-Horizon at $k$=0.9.  X-VLA Object: L2-norm data N/A.',
         ha='center', fontsize=7.5, color='#888888', fontstyle='italic')

# Grid
ax.yaxis.grid(True, alpha=0.1, zorder=0)
ax.set_axisbelow(True)

plt.tight_layout()

outdir = os.path.dirname(os.path.abspath(__file__))
plt.savefig(f'{outdir}/fig_method_gap.pdf', dpi=300)
plt.savefig(f'{outdir}/fig_method_gap.png', dpi=150)
plt.close()
print(f'Saved to {outdir}')
