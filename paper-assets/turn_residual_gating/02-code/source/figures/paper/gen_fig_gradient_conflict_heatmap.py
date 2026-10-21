"""Generate appendix figure: Per-layer gradient conflict heatmap."""
import sys
sys.path.insert(0, '/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/figures/paper')
from palette import *
import matplotlib.colors as mcolors
import matplotlib.gridspec as gridspec
import numpy as np

apply_style()

v7_e0 = [-0.09966, -0.34061, -0.02584, -0.08468, -0.1169, -0.17352, -0.19893, -0.10927, 0.07293, -0.16859, -0.1044, -0.19693, -0.19432, -0.10473, -0.16717, -0.35358, -0.01945, -0.04127, -0.01693, 0.22415, 0.00582, 0.15542, -0.05973, 0.04468, -0.17934, -0.3229, 0.1215, -0.02931]
v7_e1 = [0.01154, -0.13178, -0.10433, -0.06913, 0.00246, 0.01631, -0.06498, -0.21307, -0.03736, -0.22762, -0.00478, -0.29175, -0.22969, -0.02319, -0.11004, -0.05521, 0.06097, -0.04534, -0.05398, -0.04271, 0.06027, 0.0973, 0.08479, 0.01795, -0.0427, -0.09064, -0.01727, -0.01137]
v7_e2 = [-0.05388, -0.04711, -0.05278, -0.05008, 0.00498, 0.01048, -0.04784, -0.22297, -0.0596, -0.17289, 0.03253, -0.26268, -0.2296, -0.07735, -0.03408, -0.0177, 0.06131, -0.02524, 0.00127, -0.02193, 0.01607, 0.0763, 0.10771, 0.0164, -0.0255, -0.063, -0.02907, -0.0066]

pc_e0 = [-0.05717, -0.04202, -0.25847, -0.05105, -0.11556, -0.17691, -0.20128, 0.01798, -0.03166, -0.18675, -0.01228, -0.12681, 0.11262, -0.02208, -0.30514, 0.00822, 0.118, 0.08625, -0.12413, 0.07597, -0.07797, -0.2657, -0.03465, -0.04033, -0.20435, -0.21349, -0.13738, -0.00196]
pc_e1 = [-0.06309, -0.0293, 0.03687, -0.13907, -0.26008, -0.10037, -0.07056, 0.02024, 0.06969, -0.03849, -0.04323, -0.13871, 0.1555, -0.1215, -0.21363, -0.00357, 0.14837, -0.03238, -0.2238, -0.1237, -0.03639, -0.02943, 0.01039, -0.02609, -0.16241, -0.09179, 0.01499, -0.00721]
pc_e2 = [-0.07265, 0.03592, 0.00477, -0.08197, -0.23412, -0.14663, -0.10467, 0.09796, 0.07074, -0.01057, -0.00025, -0.14205, 0.0545, -0.10868, -0.18567, -0.04958, 0.09965, -0.00712, -0.11836, -0.08411, -0.01728, -0.10465, 0.01282, -0.06115, -0.13717, -0.07273, 0.07125, -0.00095]

data_v7 = np.array([v7_e0, v7_e1, v7_e2])
data_pc = np.array([pc_e0, pc_e1, pc_e2])
neg_v7 = [22/28, 20/28, 19/28]
neg_pc = [22/28, 21/28, 20/28]

colors = ['#1B4965', '#5FA8D3', '#BEE3F8', '#FAFAFA', '#F5E6D3', '#E8D5BE']
positions = [0.0, 0.25, 0.45, 0.5, 0.75, 1.0]
cmap = mcolors.LinearSegmentedColormap.from_list(
    'navy_warm', list(zip(positions, colors)))

vmin, vmax = -0.35, 0.35

fig = plt.figure(figsize=(7.0, 3.0))
gs = gridspec.GridSpec(1, 3, figure=fig, width_ratios=[1, 1, 0.05], wspace=0.35)

ax_a = fig.add_subplot(gs[0, 0])
ax_b = fig.add_subplot(gs[0, 1])
cax = fig.add_subplot(gs[0, 2])

epoch_labels = ['Epoch 0', 'Epoch 1', 'Epoch 2']

for ax, data, neg_fracs, title in [
    (ax_a, data_v7, neg_v7, '(a) Standard Training (v7 TG)'),
    (ax_b, data_pc, neg_pc, '(b) PCGrad Training (v9)'),
]:
    im = ax.imshow(data, aspect='auto', cmap=cmap, vmin=vmin, vmax=vmax,
                   interpolation='nearest')
    ax.set_yticks(range(3))
    ax.set_yticklabels(epoch_labels, fontsize=7.5)
    ax.set_xlabel('Layer Index', fontsize=8)
    ax.set_xticks([0, 4, 8, 12, 16, 20, 24, 27])
    ax.set_xticklabels([0, 4, 8, 12, 16, 20, 24, 27], fontsize=7)
    ax.set_title(title, fontweight='bold', pad=6, fontsize=8.5)

    for i, nf in enumerate(neg_fracs):
        ax.text(data.shape[1] - 0.5, i, f'{nf*100:.0f}%',
                ha='right', va='center', fontsize=7, color='white',
                fontweight='bold', path_effects=[
                    __import__('matplotlib.patheffects', fromlist=['withStroke']).withStroke(
                        linewidth=2.0, foreground='#333333')])

cbar = fig.colorbar(im, cax=cax)
cbar.set_label(r'$\cos(\nabla_\theta \mathcal{L}_{\mathrm{NTP}},\, \nabla_\theta \mathcal{L}_{\mathrm{GAR}})$',
               fontsize=9)
cbar.ax.tick_params(labelsize=7.5)

cbar.ax.text(0.5, -0.10, 'conflict', transform=cbar.ax.transAxes,
             ha='center', va='top', fontsize=7, color='#1B4965', fontweight='bold')
cbar.ax.text(0.5, 1.10, 'alignment', transform=cbar.ax.transAxes,
             ha='center', va='bottom', fontsize=7, color='#C4A080', fontweight='bold')

save_fig(fig, 'fig_gradient_conflict_heatmap')
