import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import matplotlib.patheffects as pe
import numpy as np
import os
from palette import DARK, GRAY, LIGHT, RCPARAMS

plt.rcParams.update(RCPARAMS)

archs = ['GDN', 'RetNet', 'HGRN2', 'GLA', 'DeltaNet']
n = len(archs)

lambada_helped = np.array([
    [np.nan, 0.13, 0.12, 0.12, 0.12],
    [np.nan, np.nan, 0.11, 0.12, 0.12],
    [np.nan, np.nan, np.nan, 0.13, 0.12],
    [np.nan, np.nan, np.nan, np.nan, 0.13],
    [np.nan, np.nan, np.nan, np.nan, np.nan],
])
lambada_hurt = np.array([
    [np.nan, np.nan, np.nan, np.nan, np.nan],
    [0.12,   np.nan, np.nan, np.nan, np.nan],
    [0.08,   0.08,   np.nan, np.nan, np.nan],
    [0.10,   0.11,   0.09,   np.nan, np.nan],
    [0.10,   0.10,   0.09,   0.08,   np.nan],
])

arceasy_helped = np.array([
    [np.nan, 0.09, 0.12, 0.11, 0.08],
    [np.nan, np.nan, 0.09, 0.11, 0.14],
    [np.nan, np.nan, np.nan, 0.10, 0.11],
    [np.nan, np.nan, np.nan, np.nan, 0.13],
    [np.nan, np.nan, np.nan, np.nan, np.nan],
])
arceasy_hurt = np.array([
    [np.nan, np.nan, np.nan, np.nan, np.nan],
    [0.11,   np.nan, np.nan, np.nan, np.nan],
    [0.10,   0.12,   np.nan, np.nan, np.nan],
    [0.11,   0.11,   0.09,   np.nan, np.nan],
    [0.10,   0.12,   0.09,   0.10,   np.nan],
])

def combine_triangles(helped, hurt):
    combined = np.full((n, n), np.nan)
    for i in range(n):
        for j in range(n):
            if i == j:
                combined[i, j] = np.nan
            elif j > i:
                combined[i, j] = helped[i, j]
            else:
                combined[i, j] = hurt[i, j]
    return combined

lambada_combined = combine_triangles(lambada_helped, lambada_hurt)
arceasy_combined = combine_triangles(arceasy_helped, arceasy_hurt)

colors_seq = ['#F7FBFF', '#D4E1EE', '#A3C4D9', '#6A9BBF', '#4E79A7', '#334F6E']
cmap = mcolors.LinearSegmentedColormap.from_list('academic_blue', colors_seq, N=256)
norm = mcolors.Normalize(vmin=0.04, vmax=0.16)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(6.7, 2.7),
                                gridspec_kw={'wspace': 0.35})

for ax, data_mat, title in [(ax1, lambada_combined, 'LAMBADA'),
                             (ax2, arceasy_combined, 'ARC-Easy')]:
    display = np.where(np.isnan(data_mat), 0, data_mat)

    im = ax.imshow(display, cmap=cmap, norm=norm, aspect='equal')

    for i in range(n):
        ax.add_patch(plt.Rectangle((i - 0.5, i - 0.5), 1, 1,
                                   fill=True, facecolor='#EEEEEE',
                                   edgecolor='white', linewidth=1.2))

    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            val = data_mat[i, j]
            if np.isnan(val):
                continue
            text_color = 'white' if val > 0.12 else DARK
            ax.text(j, i, f'{val:.2f}', ha='center', va='center',
                    fontsize=7, color=text_color, fontweight='medium')

    for i in range(n + 1):
        ax.axhline(i - 0.5, color='white', linewidth=1.2)
        ax.axvline(i - 0.5, color='white', linewidth=1.2)

    ax.set_xticks(range(n))
    ax.set_yticks(range(n))
    ax.set_xticklabels(archs, fontsize=6, ha='center')
    ax.set_yticklabels(archs, fontsize=6)
    ax.set_title(title, fontsize=8.5, fontweight='bold', pad=6)

    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    ax.spines['left'].set_visible(False)
    ax.tick_params(length=0)

    ax.plot([n - 0.5, -0.5], [-0.5, n - 0.5], color='#cccccc',
            linewidth=0.4, linestyle='--', zorder=5, clip_on=True)

    # Triangle labels along the diagonal margin
    t_h = ax.text(n - 0.5 + 0.15, -0.5 - 0.15, '$J_{h}$  ▶', fontsize=5,
                  color='#999999', ha='left', va='top', fontstyle='italic')
    t_u = ax.text(-0.5 - 0.15, n - 0.5 + 0.15, '◀  $J_{u}$', fontsize=5,
                  color='#999999', ha='right', va='bottom', fontstyle='italic')

cbar = fig.colorbar(plt.cm.ScalarMappable(norm=norm, cmap=cmap),
                    ax=[ax1, ax2], fraction=0.022, pad=0.04,
                    shrink=0.85)
cbar.set_label('Jaccard similarity', fontsize=7)
cbar.ax.tick_params(labelsize=6)
cbar.outline.set_linewidth(0.3)

fig.text(0.5, -0.01,
         'Upper triangle: $J_{\\mathrm{helped}}$;  '
         'Lower triangle: $J_{\\mathrm{hurt}}$.  '
         'All values $\\leq$ 0.14, all $p \\leq$ .002.',
         fontsize=5.5, color='#999999', ha='center')

out_dir = os.path.dirname(os.path.abspath(__file__))
paper_fig_dir = '/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/figures'
os.makedirs(paper_fig_dir, exist_ok=True)

for d in [out_dir, paper_fig_dir]:
    fig.savefig(os.path.join(d, 'jaccard_heatmap_5arch.pdf'))
    fig.savefig(os.path.join(d, 'jaccard_heatmap_5arch.png'), dpi=300)
plt.close()
print('Saved jaccard_heatmap_5arch')
