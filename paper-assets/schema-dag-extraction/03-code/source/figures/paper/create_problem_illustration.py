#!/usr/bin/env python3
"""Problem illustration figure for page 1: two dimensions of schema complexity."""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

OUT = '/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/figures/paper/fig_problem_illustration.pdf'

C = dict(
    head='#1A5276', tail='#6C3483',
    head_bg='#D4E6F1', tail_bg='#E8DAEF',
    ok='#1E8449', err='#B03A2E',
    sim='#D35400', sim_bg='#FDEBD0',
    panel_bg='#F8F9FA', border='#CCD1D1',
    text='#2C3E50', light='#808B96',
    dim1='#2471A3', dim2='#CA6F1E',
    sent_bg='#EBF5FB',
)


def main():
    fig = plt.figure(figsize=(6.5, 3.1), facecolor='white')
    ax = fig.add_axes([0.0, 0.0, 1.0, 1.0])
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 4.55)
    ax.set_axis_off()

    draw_sentence(ax)
    draw_small_schema(ax)
    draw_large_schema(ax)
    draw_dimensions(ax)

    fig.savefig(OUT, bbox_inches='tight', dpi=300,
                facecolor='white', edgecolor='none', pad_inches=0.03)
    plt.close()
    print(f'Saved to {OUT}')


def draw_sentence(ax):
    sy = 4.10
    bar = FancyBboxPatch((0.1, 3.82), 9.8, 0.58,
                         boxstyle="round,pad=0.05",
                         fc=C['sent_bg'], ec=C['border'], lw=0.5)
    ax.add_patch(bar)

    ax.text(0.35, sy, 'RE task:', fontsize=6.5, color=C['light'],
            fontweight='bold', va='center', family='sans-serif')

    ax.text(2.3, sy, '"', fontsize=7.5, color=C['text'],
            va='center', ha='right', family='serif')

    hx1, hx2 = 2.35, 3.85
    hbox = FancyBboxPatch((hx1, 3.90), hx2 - hx1, 0.40,
                          boxstyle="round,pad=0.03",
                          fc=C['head_bg'], ec=C['head'], lw=0.4, alpha=0.8)
    ax.add_patch(hbox)
    ax.text((hx1 + hx2) / 2, sy, 'Barack Obama', fontsize=7, color=C['head'],
            fontweight='bold', ha='center', va='center', family='sans-serif')
    ax.text((hx1 + hx2) / 2, 3.76, 'head', fontsize=5, color=C['head'],
            ha='center', va='top', style='italic')

    ax.text(3.90, sy, ' was born in ', fontsize=7.5, color=C['text'],
            va='center', family='serif')

    tx1, tx2 = 5.55, 6.50
    tbox = FancyBboxPatch((tx1, 3.90), tx2 - tx1, 0.40,
                          boxstyle="round,pad=0.03",
                          fc=C['tail_bg'], ec=C['tail'], lw=0.4, alpha=0.8)
    ax.add_patch(tbox)
    ax.text((tx1 + tx2) / 2, sy, 'Honolulu', fontsize=7, color=C['tail'],
            fontweight='bold', ha='center', va='center', family='sans-serif')
    ax.text((tx1 + tx2) / 2, 3.76, 'tail', fontsize=5, color=C['tail'],
            ha='center', va='top', style='italic')

    ax.text(6.55, sy, ', Hawaii."', fontsize=7.5, color=C['text'],
            va='center', family='serif')

    ax.text(7.8, sy, 'Gold:', fontsize=6.5, color=C['light'],
            fontweight='bold', va='center')
    ax.text(8.35, sy, 'place of birth', fontsize=7, color=C['ok'],
            fontweight='bold', va='center', family='sans-serif')


def draw_small_schema(ax):
    lx, ly, lw, lh = 0.1, 0.55, 4.35, 3.05
    panel = FancyBboxPatch((lx, ly), lw, lh,
                           boxstyle="round,pad=0.08",
                           fc=C['panel_bg'], ec=C['border'], lw=0.7)
    ax.add_patch(panel)

    ax.text(lx + lw / 2, ly + lh - 0.12, 'Few candidate types (k = 4)',
            fontsize=7.5, fontweight='bold', ha='center', va='top',
            color=C['text'], family='sans-serif')

    types = ['place of birth', 'genre', 'manufacturer', 'member of']
    for i, t in enumerate(types):
        y = ly + lh - 0.55 - i * 0.38
        is_gold = (i == 0)
        dot_c = C['ok'] if is_gold else C['light']
        ax.text(lx + 0.35, y, '●', fontsize=5.5, color=dot_c, va='center')
        ax.text(lx + 0.58, y, t, fontsize=7, color=C['text'],
                va='center', family='sans-serif',
                fontweight='bold' if is_gold else 'normal')

    sep_y = ly + 0.72
    ax.plot([lx + 0.25, lx + lw - 0.25], [sep_y, sep_y],
            color=C['border'], lw=0.4, ls='--')

    ax.text(lx + 0.30, ly + 0.40, 'Prediction:', fontsize=6.5,
            color=C['light'], va='center', fontweight='bold')
    ax.text(lx + 1.45, ly + 0.40, 'place of birth', fontsize=7.5,
            color=C['ok'], va='center', fontweight='bold', family='sans-serif')
    ax.text(lx + lw - 0.25, ly + 0.40, '✓', fontsize=12, color=C['ok'],
            ha='right', va='center', fontweight='bold')


def draw_large_schema(ax):
    rx, ry, rw, rh = 5.55, 0.55, 4.35, 3.05
    panel = FancyBboxPatch((rx, ry), rw, rh,
                           boxstyle="round,pad=0.08",
                           fc=C['panel_bg'], ec=C['border'], lw=0.7)
    ax.add_patch(panel)

    ax.text(rx + rw / 2, ry + rh - 0.12, 'Many candidate types (k = 80)',
            fontsize=7.5, fontweight='bold', ha='center', va='top',
            color=C['text'], family='sans-serif')

    types = [
        ('place of birth',         False, False),
        ('place of death',         True,  False),
        ('residence',              True,  True),
        ('headquarters location',  True,  False),
        ('country of citizenship', True,  False),
        ('... + 75 more types',    False, False),
    ]

    spacing = 0.32
    for i, (t, is_sim, is_pred) in enumerate(types):
        y = ry + rh - 0.55 - i * spacing
        if is_sim:
            hl = FancyBboxPatch((rx + 0.20, y - 0.12), 2.95, 0.25,
                                boxstyle="round,pad=0.02",
                                fc=C['sim_bg'], ec='none')
            ax.add_patch(hl)

        if t.startswith('...'):
            ax.text(rx + 0.38, y, t, fontsize=6, color=C['light'],
                    va='center', family='sans-serif', style='italic')
        else:
            dot_c = C['err'] if is_pred else (C['sim'] if is_sim else C['light'])
            dot = '●' if (is_pred or i == 0) else '○'
            tc = C['err'] if is_pred else (C['sim'] if is_sim else C['text'])
            ax.text(rx + 0.35, y, dot, fontsize=5.5, color=dot_c, va='center')
            ax.text(rx + 0.58, y, t, fontsize=7, color=tc,
                    va='center', family='sans-serif',
                    fontweight='bold' if is_pred else 'normal')

    # Bracket for confusable types (indices 1-4)
    by_top = ry + rh - 0.55 - 1 * spacing + 0.13
    by_bot = ry + rh - 0.55 - 4 * spacing - 0.13
    bx = rx + 3.25
    ax.plot([bx, bx + 0.10, bx + 0.10, bx],
            [by_top, by_top, by_bot, by_bot],
            color=C['sim'], lw=0.7, solid_capstyle='round')
    ax.text(bx + 0.16, (by_top + by_bot) / 2, 'semantically\nsimilar',
            fontsize=5.5, color=C['sim'], va='center',
            style='italic', linespacing=1.15)

    sep_y = ry + 0.72
    ax.plot([rx + 0.25, rx + rw - 0.25], [sep_y, sep_y],
            color=C['border'], lw=0.4, ls='--')

    ax.text(rx + 0.30, ry + 0.40, 'Prediction:', fontsize=6.5,
            color=C['light'], va='center', fontweight='bold')
    ax.text(rx + 1.45, ry + 0.40, 'residence', fontsize=7.5,
            color=C['err'], va='center', fontweight='bold', family='sans-serif')
    ax.text(rx + rw - 0.25, ry + 0.40, '✗', fontsize=12, color=C['err'],
            ha='right', va='center', fontweight='bold')


def draw_dimensions(ax):
    # Arrow between panels
    ax.annotate('', xy=(5.35, 2.1), xytext=(4.65, 2.1),
                arrowprops=dict(arrowstyle='->', color=C['dim1'],
                               lw=1.5, mutation_scale=12))

    # Dim 1 + Dim 2 labels at bottom
    ax.text(2.3, 0.28, '■  Dimension 1: type count',
            fontsize=6.5, color=C['dim1'], fontweight='bold',
            ha='center', va='center', family='sans-serif')
    ax.text(7.7, 0.28, '■  Dimension 2: inter-type confusability',
            fontsize=6.5, color=C['dim2'], fontweight='bold',
            ha='center', va='center', family='sans-serif')


if __name__ == '__main__':
    main()
