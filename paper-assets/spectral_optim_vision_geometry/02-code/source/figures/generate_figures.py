import sys
sys.path.insert(0, '/root/spectral_optim_vision_geometry')

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patheffects as pe
import numpy as np

from plot_style import apply_style, COLORS, FONT_SIZES
apply_style()

plt.rcParams.update({
    'font.family': 'serif',
    'savefig.pad_inches': 0.05,
})


def fig1_heatmap():
    datasets = ['CIFAR-100', 'Tiny-ImageNet', 'ImageNet-100']
    architectures = ['ResNet-50', 'DeiT-S', 'ConvNeXt-T']
    data = np.array([
        [10.40, 13.44, 16.08],
        [ 5.90,  7.69, 15.00],
        [11.47, 10.92, 24.30],
    ])

    fig, ax = plt.subplots(figsize=(3.25, 2.4))
    im = ax.imshow(data, cmap='viridis', aspect='auto', vmin=4, vmax=26)

    ax.set_xticks(range(len(architectures)))
    ax.set_xticklabels(architectures, rotation=0)
    ax.set_yticks(range(len(datasets)))
    ax.set_yticklabels(datasets)
    ax.tick_params(top=True, bottom=False, labeltop=True, labelbottom=False)

    for i in range(len(datasets)):
        for j in range(len(architectures)):
            val = data[i, j]
            ax.text(j, i, f'+{val:.1f}', ha='center', va='center',
                    color='black', fontsize=10, fontweight='bold',
                    path_effects=[pe.withStroke(linewidth=2, foreground='white')])

    cbar = fig.colorbar(im, ax=ax, shrink=0.85, pad=0.08)
    cbar.set_label('Accuracy gap (pp)', fontsize=FONT_SIZES['annotation'])
    cbar.set_ticks(np.arange(4, 27, 2))
    cbar.ax.tick_params(labelsize=7)

    ax.set_title('Muon $-$ AdamW Accuracy Gap', fontsize=10, pad=12, fontweight='bold')

    for spine in ax.spines.values():
        spine.set_visible(False)
    ax.set_xticks(np.arange(data.shape[1]+1)-.5, minor=True)
    ax.set_yticks(np.arange(data.shape[0]+1)-.5, minor=True)
    ax.grid(which='minor', color='white', linewidth=1.5)
    ax.tick_params(which='minor', bottom=False, left=False)

    fig.savefig('fig1_spectral_gap_heatmap.pdf')
    fig.savefig('fig1_spectral_gap_heatmap.png')
    plt.close(fig)
    print('Figure 1 saved.')


def fig2_gap_evolution():
    settings = ['C100\nResNet-50', 'C100\nDeiT-S', 'C100\nConvNeXt-T',
                'IN100\nResNet-50', 'IN100\nConvNeXt-T']
    gap_20 = [9.03, 10.34, 16.08, 11.47, 24.30]
    gap_50 = [6.76, 10.37, 12.60, 3.56, 11.37]
    change_pp = [g5 - g2 for g2, g5 in zip(gap_20, gap_50)]

    c20 = COLORS['Muon']
    c50 = COLORS['AdamW']

    x = np.arange(len(settings))
    width = 0.32

    plt.rcParams['hatch.linewidth'] = 0.6

    fig, ax = plt.subplots(figsize=(5.5, 3.2))
    bars1 = ax.bar(x - width/2, gap_20, width, label='20 epochs', color=c20,
                   edgecolor='white', linewidth=0.5, zorder=3)
    bars2 = ax.bar(x + width/2, gap_50, width, label='50 epochs', color=c50,
                   edgecolor='white', linewidth=0.5, hatch='//', zorder=3)

    for i, (b1, b2) in enumerate(zip(bars1, bars2)):
        ax.text(b1.get_x() + b1.get_width()/2, b1.get_height() + 0.3,
                f'+{gap_20[i]:.1f}pp', ha='center', va='bottom',
                fontsize=6.5, color='#333333')
        ax.text(b2.get_x() + b2.get_width()/2, b2.get_height() + 0.3,
                f'+{gap_50[i]:.1f}pp', ha='center', va='bottom',
                fontsize=6.5, color='#333333')

    for i, (b1, b2) in enumerate(zip(bars1, bars2)):
        max_h = max(b1.get_height(), b2.get_height())
        bracket_y = max_h + 2.8
        x_left = b1.get_x() + b1.get_width()/2
        x_right = b2.get_x() + b2.get_width()/2
        x_mid = (x_left + x_right) / 2
        tick_h = 0.4

        bracket_color = '#888888' if abs(change_pp[i]) < 0.1 else '#CC3311'

        ax.plot([x_left, x_left, x_right, x_right],
                [bracket_y - tick_h, bracket_y, bracket_y, bracket_y - tick_h],
                color=bracket_color, linewidth=0.8, zorder=5)

        delta = change_pp[i]
        if abs(delta) < 0.1:
            label = "0pp"
        else:
            arrow = "\u2193" if delta < 0 else "\u2191"
            label = f"{arrow}{abs(delta):.1f}pp"

        ax.text(x_mid, bracket_y + 0.15, label, ha='center', va='bottom',
                fontsize=7, fontweight='bold', color=bracket_color)

    ax.set_ylabel('Muon $-$ AdamW gap (pp)', fontsize=FONT_SIZES['axis_label'])
    ax.set_xticks(x)
    ax.set_xticklabels(settings, fontsize=7.5)
    ax.set_ylim(0, 32)
    ax.legend(fontsize=8, loc='upper right', framealpha=0.9, edgecolor='none')
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.grid(axis='y', alpha=0.3, linewidth=0.5)
    ax.set_axisbelow(True)

    ax.set_title('Spectral Optimizer Advantage: Training Duration Effect',
                 fontsize=10, fontweight='bold', pad=10)

    fig.savefig('fig2_gap_evolution.pdf')
    fig.savefig('fig2_gap_evolution.png')
    plt.close(fig)
    print('Figure 2 saved.')

if __name__ == '__main__':
    fig1_heatmap()
    fig2_gap_evolution()
