#!/usr/bin/env python3
"""Generate Figure 4: Pixel-shuffle 4×4 folding diagram for SmolVLA."""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib.patheffects as pe
import numpy as np
import os
import shutil

plt.rcParams.update({
    'font.family': 'serif',
    'font.serif': ['Liberation Serif', 'DejaVu Serif'],
    'font.size': 10,
    'figure.dpi': 300,
    'savefig.dpi': 300,
    'savefig.bbox': 'tight',
    'savefig.pad_inches': 0.01,
    'pdf.fonttype': 42,
    'ps.fonttype': 42,
    'axes.spines.top': False,
    'axes.spines.right': False,
    'axes.spines.left': False,
    'axes.spines.bottom': False,
})

COLOR_FAMILIES = [
    ['#6A9ECF', '#4E79A7', '#3A6591', '#2B4F73'],  # blues
    ['#F6B85C', '#F28E2B', '#D4751C', '#B05E14'],  # oranges
    ['#7DC48A', '#59A14F', '#458040', '#336630'],  # greens
    ['#C497C1', '#B07AA1', '#8E5E82', '#6D4564'],  # purples
]
GRAY_REMOVED = '#CCCCCC'
RED_ACCENT = '#D55E00'


def draw_pixel_shuffle_figure(outdir):
    fig_w = 3.8
    fig_h = 2.35
    fig, ax = plt.subplots(figsize=(fig_w, fig_h))
    ax.set_xlim(0, fig_w)
    ax.set_ylim(0, fig_h)
    ax.set_aspect('equal')
    ax.axis('off')

    # --- Main grid geometry ---
    cell = 0.26
    gap = 0.022
    grid_size = 4 * cell + 3 * gap

    token_w = 0.34
    arrow_len = 0.32
    h_gap = 0.09
    brace_label_w = 0.48

    total_w = grid_size + h_gap + arrow_len + h_gap + token_w + brace_label_w
    x0 = (fig_w - total_w) / 2

    # Vertical layout
    bottom_row_h = 0.48
    label_gap = 0.16
    grid_y0 = bottom_row_h + label_gap + 0.06
    mid_y = grid_y0 + grid_size / 2

    # ===== Main grid =====
    grid_x0 = x0

    # Subtle background behind grid to suggest "image"
    bg = mpatches.FancyBboxPatch(
        (grid_x0 - 0.03, grid_y0 - 0.03),
        grid_size + 0.06, grid_size + 0.06,
        boxstyle="round,pad=0.02",
        facecolor='#F5F5F5', edgecolor='#DDDDDD',
        linewidth=0.4, zorder=1
    )
    ax.add_patch(bg)

    for r in range(4):
        for c in range(4):
            x = grid_x0 + c * (cell + gap)
            y = grid_y0 + (3 - r) * (cell + gap)
            color = COLOR_FAMILIES[r][c]
            rect = mpatches.FancyBboxPatch(
                (x, y), cell, cell,
                boxstyle="round,pad=0.01",
                facecolor=color, edgecolor='#444444',
                linewidth=0.45, zorder=2
            )
            ax.add_patch(rect)

    ax.text(grid_x0 + grid_size / 2, grid_y0 - 0.08,
            '4×4 SigLIP patches', ha='center', va='top',
            fontsize=7.5, fontstyle='italic', color='#555555')

    # ===== Arrow =====
    ax0 = grid_x0 + grid_size + h_gap
    ax1 = ax0 + arrow_len

    ax.annotate('', xy=(ax1, mid_y), xytext=(ax0, mid_y),
                arrowprops=dict(arrowstyle='->', color='#333333',
                                lw=1.4, mutation_scale=11),
                zorder=3)
    ax.text((ax0 + ax1) / 2, mid_y + 0.09,
            'channel\nconcat', ha='center', va='bottom',
            fontsize=6.5, color='#444444', linespacing=0.85)

    # ===== Stacked token =====
    token_x0 = ax1 + h_gap
    group_gap = 0.018
    group_h = (grid_size - 3 * group_gap) / 4
    slice_h = group_h / 4

    for r in range(4):
        group_y = grid_y0 + grid_size - (r + 1) * group_h - r * group_gap
        for c in range(4):
            y = group_y + (3 - c) * slice_h
            color = COLOR_FAMILIES[r][c]
            rect = mpatches.FancyBboxPatch(
                (token_x0, y + 0.002), token_w, slice_h - 0.004,
                boxstyle="round,pad=0.002",
                facecolor=color, edgecolor='#555555',
                linewidth=0.25, zorder=2
            )
            ax.add_patch(rect)

    # Bracket
    bx = token_x0 + token_w + 0.045
    by0 = grid_y0
    by1 = grid_y0 + grid_size
    bym = (by0 + by1) / 2
    tk = 0.03

    ax.plot([bx - tk, bx, bx, bx - tk],
            [by1, by1, by0, by0],
            color='#555555', lw=0.55, zorder=2, solid_capstyle='round')
    ax.plot([bx, bx + tk], [bym, bym],
            color='#555555', lw=0.55, zorder=2, solid_capstyle='round')

    ax.text(bx + tk + 0.025, bym, '1 token\n(16·C)', ha='left', va='center',
            fontsize=7, color='#333333', linespacing=1.1)

    ax.text(token_x0 + token_w / 2, grid_y0 - 0.08,
            'output token', ha='center', va='top',
            fontsize=7.5, fontstyle='italic', color='#555555')

    # ===== Bottom: removal concept =====
    mini_cell = 0.085
    mini_gap = 0.008
    mini_grid = 4 * mini_cell + 3 * mini_gap

    # Center the bottom row
    removal_text_w = 1.55
    removal_total_w = mini_grid + 0.10 + removal_text_w
    mini_x0 = (fig_w - removal_total_w) / 2
    mini_y0 = 0.06

    for r in range(4):
        for c in range(4):
            x = mini_x0 + c * (mini_cell + mini_gap)
            y = mini_y0 + (3 - r) * (mini_cell + mini_gap)
            rect = mpatches.FancyBboxPatch(
                (x, y), mini_cell, mini_cell,
                boxstyle="round,pad=0.003",
                facecolor=GRAY_REMOVED, edgecolor='#BBBBBB',
                linewidth=0.25, zorder=2, alpha=0.55
            )
            ax.add_patch(rect)

    # Red dashed border
    border = mpatches.FancyBboxPatch(
        (mini_x0 - 0.012, mini_y0 - 0.012),
        mini_grid + 0.024, mini_grid + 0.024,
        boxstyle="round,pad=0.01",
        facecolor='none', edgecolor=RED_ACCENT,
        linewidth=0.9, linestyle=(0, (4, 2)), zorder=3
    )
    ax.add_patch(border)

    # Red X
    ax.plot([mini_x0 + 0.01, mini_x0 + mini_grid - 0.01],
            [mini_y0 + 0.01, mini_y0 + mini_grid - 0.01],
            color=RED_ACCENT, lw=1.0, zorder=4)
    ax.plot([mini_x0 + 0.01, mini_x0 + mini_grid - 0.01],
            [mini_y0 + mini_grid - 0.01, mini_y0 + 0.01],
            color=RED_ACCENT, lw=1.0, zorder=4)

    # Text right of mini grid
    tx = mini_x0 + mini_grid + 0.10
    ty = mini_y0 + mini_grid / 2
    ax.text(tx, ty,
            'Token removed → entire 4×4\nreceptive field lost (no overlap)',
            ha='left', va='center', fontsize=7, color=RED_ACCENT,
            linespacing=1.15,
            path_effects=[pe.withStroke(linewidth=1.8, foreground='white')])

    # ===== Save =====
    pdf_path = os.path.join(outdir, 'fig_pixel_shuffle.pdf')
    png_path = os.path.join(outdir, 'fig_pixel_shuffle.png')
    plt.savefig(pdf_path, format='pdf')
    plt.savefig(png_path, format='png')
    plt.close()
    print(f'Saved: {pdf_path} ({os.path.getsize(pdf_path)} bytes)')
    print(f'Saved: {png_path} ({os.path.getsize(png_path)} bytes)')
    return pdf_path, png_path


if __name__ == '__main__':
    script_dir = os.path.dirname(os.path.abspath(__file__))
    pdf_path, png_path = draw_pixel_shuffle_figure(script_dir)

    artifact_dir = os.path.join(
        os.path.dirname(script_dir), '..', '..', '..',
        'artifacts', '_project', 'chart'
    )
    artifact_dir = os.path.normpath(artifact_dir)
    os.makedirs(artifact_dir, exist_ok=True)
    artifact_pdf = os.path.join(artifact_dir, 'fig_pixel_shuffle.pdf')
    shutil.copy2(pdf_path, artifact_pdf)
    print(f'Copied to: {artifact_pdf}')
