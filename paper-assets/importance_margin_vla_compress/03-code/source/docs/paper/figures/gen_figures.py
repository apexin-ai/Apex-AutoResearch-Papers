import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib.font_manager as fm
import numpy as np
from pathlib import Path

OUT_DIR = Path(__file__).parent / 'paper'

plt.rcParams.update({
    'font.family': 'serif',
    'font.serif': ['Times New Roman', 'Liberation Serif', 'DejaVu Serif'],
    'font.size': 9,
    'axes.titlesize': 10,
    'axes.labelsize': 9,
    'xtick.labelsize': 8,
    'ytick.labelsize': 8,
    'legend.fontsize': 8,
    'figure.dpi': 300,
    'savefig.dpi': 300,
    'savefig.bbox': 'tight',
    'savefig.pad_inches': 0.03,
    'axes.spines.top': False,
    'axes.spines.right': False,
    'lines.linewidth': 1.5,
    'text.usetex': False,
    'mathtext.fontset': 'stix',
})

BLUE = '#0072B2'
RED = '#D55E00'
ORANGE = '#E69F00'
GRAY = '#888888'
GREEN = '#009E73'
PURPLE = '#882255'


def fig2_degradation_curve():
    fig, ax = plt.subplots(figsize=(3.5, 2.6))

    # X-VLA (linear + BART encoder) — solid + diamonds
    xx = [0.0, 0.05, 0.1, 0.3, 0.5, 0.7, 0.8, 0.9]
    xy = [99.2, 99.0, 97.6, 56.2, 42.6, 23.0, 4.0, 0.0]
    ax.plot(xx, xy, '-D', color=GREEN, markersize=4.5, markerfacecolor=GREEN,
            label=r'X-VLA (linear+enc., 880M)', zorder=3)

    # OpenVLA (MLP projection) — solid + squares
    ox = [0.0, 0.05, 0.1, 0.3, 0.5, 0.7]
    oy = [74.0, 69.4, 62.0, 49.0, 37.4, 20.6]
    ax.plot(ox, oy, '-s', color=BLUE, markersize=5, markerfacecolor=BLUE,
            label='OpenVLA (MLP proj., 7B)', zorder=3)

    # SmolVLA ours — solid + circles
    sx = [0.0, 0.05, 0.1, 0.3, 0.5, 0.7]
    sy = [44.8, 0.0, 0.0, 0.0, 0.0, 0.0]
    ax.plot(sx, sy, '-o', color=RED, markersize=5, markerfacecolor=RED,
            label='SmolVLA (pixel-shuffle, 0.5B)', zorder=3)

    ax.annotate('Threshold\nonset', xy=(0.3, 56.2), xytext=(0.48, 72.0),
                fontsize=7, color=GREEN, fontweight='bold',
                arrowprops=dict(arrowstyle='->', color=GREEN, lw=1.0),
                zorder=4)

    ax.annotate('Catastrophic\ncliff', xy=(0.08, 3.0), xytext=(0.22, 22.0),
                fontsize=7, color=RED, fontweight='bold',
                arrowprops=dict(arrowstyle='->', color=RED, lw=1.0),
                zorder=4)

    ax.set_xlabel('Fraction of Tokens Removed')
    ax.set_ylabel('Success Rate (%)')
    ax.set_xlim(-0.03, 0.95)
    ax.set_ylim(-3, 105)
    ax.set_xticks([0.0, 0.1, 0.3, 0.5, 0.7, 0.9])
    ax.legend(loc='lower left', fontsize=6.5, framealpha=0.9)
    ax.grid(True, alpha=0.2, zorder=0)

    plt.tight_layout()
    path = OUT_DIR / 'fig_degradation_curve.pdf'
    fig.savefig(path)
    plt.close(fig)
    print(f'Saved: {path}')


def fig3_compression_curve():
    fig, ax = plt.subplots(figsize=(3.5, 2.6))

    # Smart Compress — 3-seed means from Table 2
    cx = [16, 32, 64, 96, 128]
    cy = [56.9, 60.1, 62.0, 54.5, 58.0]

    ax.plot(cx, cy, '-o', color=BLUE, markersize=5, markerfacecolor=BLUE,
            label='Cross-attention VTR', zorder=3)

    # Value labels
    ax.annotate('56.9%', xy=(16, 56.9), xytext=(16, 50.5),
                fontsize=7, ha='center', color=BLUE, fontweight='bold')
    ax.annotate('60.1%', xy=(32, 60.1), xytext=(32, 66.0),
                fontsize=7, ha='center', color=BLUE, fontweight='bold')
    ax.annotate('62.0%', xy=(64, 62.0), xytext=(64, 67.5),
                fontsize=7, ha='center', color=BLUE, fontweight='bold')
    ax.annotate('54.5%', xy=(96, 54.5), xytext=(82, 50.0),
                fontsize=7, ha='center', color=BLUE, fontweight='bold',
                arrowprops=dict(arrowstyle='-', color=BLUE, lw=0.5))
    ax.annotate('58.0%', xy=(128, 58.0), xytext=(128, 63.5),
                fontsize=7, ha='center', color=BLUE, fontweight='bold')

    # Baselines
    ax.axhline(44.8, color=RED, linestyle='--', linewidth=1.0, zorder=2)
    ax.text(125, 42.0, 'SmolVLA Baseline (44.8%)', fontsize=7,
            ha='right', color=RED)

    ax.axhline(0.0, color=GRAY, linestyle=':', linewidth=1.0, zorder=2)
    ax.text(125, 2.5, 'Hard Pruning (all methods, 0%)', fontsize=7,
            ha='right', color=GRAY)

    ax.set_xlabel('Number of Compressed Tokens ($M$)')
    ax.set_ylabel('Success Rate (%)')
    ax.set_xlim(8, 136)
    ax.set_ylim(-5, 75)
    ax.set_xticks([16, 32, 64, 96, 128])
    ax.legend(loc='center right', fontsize=7, framealpha=0.9)
    ax.grid(True, alpha=0.2, zorder=0)

    plt.tight_layout()
    path = OUT_DIR / 'fig_compression_curve.pdf'
    fig.savefig(path)
    plt.close(fig)
    print(f'Saved: {path}')


def fig4_pixel_shuffle_viz():
    fig, ax = plt.subplots(figsize=(7, 2.2))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 3)
    ax.set_aspect('equal')
    ax.axis('off')

    # --- Left: 32x32 grid ---
    left_x, left_y = 0.5, 0.3
    grid_size = 2.4
    n_left = 32
    cell = grid_size / n_left

    # Draw grid background
    rect_bg = mpatches.FancyBboxPatch((left_x, left_y), grid_size, grid_size,
                                       boxstyle='round,pad=0.02',
                                       facecolor='#F0F0F0', edgecolor='#AAAAAA',
                                       linewidth=0.5, zorder=1)
    ax.add_patch(rect_bg)

    # Highlight two 4x4 regions
    colors_highlight = ['#4393C3', '#F4A582']
    regions = [(4, 4), (12, 20)]  # (row, col) of top-left corner
    for (r, c), color in zip(regions, colors_highlight):
        hx = left_x + c * cell
        hy = left_y + (n_left - r - 4) * cell
        rect_h = mpatches.Rectangle((hx, hy), 4 * cell, 4 * cell,
                                     facecolor=color, edgecolor='black',
                                     linewidth=0.8, alpha=0.7, zorder=2)
        ax.add_patch(rect_h)

    # Grid lines (sparse, every 4 cells)
    for i in range(0, n_left + 1, 4):
        lw = 0.3
        ax.plot([left_x + i * cell, left_x + i * cell],
                [left_y, left_y + grid_size], color='#CCCCCC', lw=lw, zorder=1)
        ax.plot([left_x, left_x + grid_size],
                [left_y + i * cell, left_y + i * cell], color='#CCCCCC', lw=lw, zorder=1)

    # Label
    ax.text(left_x + grid_size / 2, left_y - 0.18,
            '1024 SigLIP Patches (32$\\times$32)',
            ha='center', va='top', fontsize=8, fontweight='bold')

    # --- Arrow ---
    arrow_x_start = left_x + grid_size + 0.3
    arrow_x_end = arrow_x_start + 1.8
    arrow_y = left_y + grid_size / 2
    ax.annotate('', xy=(arrow_x_end, arrow_y), xytext=(arrow_x_start, arrow_y),
                arrowprops=dict(arrowstyle='->', color='black', lw=1.5))
    ax.text((arrow_x_start + arrow_x_end) / 2, arrow_y + 0.25,
            'Pixel-Shuffle\n(4$\\times$4 fold)', ha='center', va='bottom',
            fontsize=8, fontweight='bold')

    # --- Right: 8x8 grid ---
    right_x = arrow_x_end + 0.3
    right_y = left_y + 0.3
    n_right = 8
    grid_size_r = 1.8
    cell_r = grid_size_r / n_right

    # Draw all cells
    for r in range(n_right):
        for c in range(n_right):
            rx = right_x + c * cell_r
            ry = right_y + (n_right - 1 - r) * cell_r
            rect = mpatches.Rectangle((rx, ry), cell_r, cell_r,
                                       facecolor='#E8E8E8', edgecolor='#999999',
                                       linewidth=0.4, zorder=1)
            ax.add_patch(rect)

    # Highlight corresponding tokens
    token_positions = [(1, 1), (3, 5)]  # (row, col) in 8x8 grid
    for (r, c), color in zip(token_positions, colors_highlight):
        rx = right_x + c * cell_r
        ry = right_y + (n_right - 1 - r) * cell_r
        rect_h = mpatches.Rectangle((rx, ry), cell_r, cell_r,
                                     facecolor=color, edgecolor='black',
                                     linewidth=1.0, alpha=0.85, zorder=2)
        ax.add_patch(rect_h)

    # Label
    ax.text(right_x + grid_size_r / 2, right_y - 0.18,
            '64 Tokens (8$\\times$8)', ha='center', va='top',
            fontsize=8, fontweight='bold')

    ax.text(right_x + grid_size_r / 2, right_y - 0.45,
            'Each token encodes 16 patches', ha='center', va='top',
            fontsize=7, color=GRAY, style='italic')

    # Draw connection lines (dashed) from highlighted 4x4 regions to tokens
    for (lr, lc), (tr, tc), color in zip(regions, token_positions, colors_highlight):
        # Source center (left grid)
        src_x = left_x + (lc + 2) * cell
        src_y = left_y + (n_left - lr - 2) * cell
        # Target center (right grid)
        dst_x = right_x + (tc + 0.5) * cell_r
        dst_y = right_y + (n_right - 1 - tr + 0.5) * cell_r
        ax.annotate('', xy=(dst_x, dst_y),
                    xytext=(src_x + 0.15, src_y),
                    arrowprops=dict(arrowstyle='->', color=color,
                                    lw=1.0, linestyle='--',
                                    connectionstyle='arc3,rad=0.15'))

    plt.tight_layout()
    path = OUT_DIR / 'fig_pixel_shuffle.pdf'
    fig.savefig(path)
    plt.close(fig)
    print(f'Saved: {path}')


def fig5_entropy_comparison():
    smolvla_entropy = {
        0: 0.9826, 1: 0.9561, 2: 0.9597, 3: 0.9434, 4: 0.9408,
        5: 0.9406, 6: 0.9474, 7: 0.9628, 8: 0.9614, 9: 0.9572,
        10: 0.9455, 11: 0.951, 12: 0.9485, 13: 0.9311, 14: 0.9482,
        15: 0.9566,
    }
    smolvla_mean = 0.9521

    openvla_entropy = {
        0: 0.979, 1: 0.9523, 2: 0.7995, 3: 0.7256, 4: 0.7008,
        5: 0.678, 6: 0.688, 7: 0.6744, 8: 0.6514, 9: 0.6526,
        10: 0.6612, 11: 0.6505, 12: 0.622, 13: 0.6508, 14: 0.6618,
        15: 0.622, 16: 0.6372, 17: 0.6069, 18: 0.597, 19: 0.5662,
        20: 0.5672, 21: 0.5904, 22: 0.5861, 23: 0.5806, 24: 0.5653,
        25: 0.5719, 26: 0.5709, 27: 0.5419, 28: 0.5298, 29: 0.4774,
        30: 0.5241, 31: 0.5739,
    }
    openvla_mean = 0.6393

    pi0_entropy = {
        0: 0.9493, 1: 0.9831, 2: 0.9772, 3: 0.9608, 4: 0.9606,
        5: 0.9578, 6: 0.9672, 7: 0.9574, 8: 0.9620, 9: 0.9552,
        10: 0.9697, 11: 0.9310, 12: 0.9558, 13: 0.9715, 14: 0.9344,
        15: 0.9725, 16: 0.9582, 17: 0.9456,
    }
    pi0_mean = 0.9594

    smol_x = [i / 15 for i in range(16)]
    smol_y = [smolvla_entropy[i] for i in range(16)]

    open_x = [i / 31 for i in range(32)]
    open_y = [openvla_entropy[i] for i in range(32)]

    pi0_x = [i / 17 for i in range(18)]
    pi0_y = [pi0_entropy[i] for i in range(18)]

    fig, ax = plt.subplots(figsize=(3.5, 2.6))

    ax.plot(pi0_x, pi0_y, '-^', color=ORANGE, markersize=4,
            markerfacecolor=ORANGE, label=r'$\pi_0$ (linear proj., 3.3B)', zorder=3)
    ax.plot(smol_x, smol_y, '-o', color=BLUE, markersize=4,
            markerfacecolor=BLUE, label='SmolVLA (pixel-shuffle, 0.5B)', zorder=3)
    ax.plot(open_x, open_y, '-s', color=RED, markersize=4,
            markerfacecolor=RED, label='OpenVLA (MLP proj., 7B)', zorder=3)

    ax.axhline(pi0_mean, color=ORANGE, linestyle='--', linewidth=0.8, zorder=2)
    ax.text(0.25, pi0_mean + 0.015, f'mean = {pi0_mean:.2f}',
            fontsize=6, color=ORANGE, va='bottom', ha='center')

    ax.axhline(smolvla_mean, color=BLUE, linestyle='--', linewidth=0.8, zorder=2)
    ax.text(0.75, smolvla_mean - 0.03, f'mean = {smolvla_mean:.2f}',
            fontsize=6, color=BLUE, va='top', ha='center')

    ax.axhline(openvla_mean, color=RED, linestyle='--', linewidth=0.8, zorder=2)
    ax.text(0.55, openvla_mean + 0.02, f'mean = {openvla_mean:.2f}',
            fontsize=6, color=RED, va='bottom', ha='center')

    ax.set_xlabel('Normalized Layer Depth')
    ax.set_ylabel('Entropy Ratio')
    ax.set_xlim(-0.03, 1.03)
    ax.set_ylim(0.4, 1.05)
    ax.legend(loc='lower left', fontsize=6, framealpha=0.9)
    ax.grid(True, alpha=0.2, zorder=0)

    plt.tight_layout()
    path = OUT_DIR / 'fig_entropy_layers.pdf'
    fig.savefig(path)
    plt.close(fig)
    print(f'Saved: {path}')


if __name__ == '__main__':
    fig2_degradation_curve()
    fig3_compression_curve()
    fig4_pixel_shuffle_viz()
    fig5_entropy_comparison()
    print('All figures generated.')
