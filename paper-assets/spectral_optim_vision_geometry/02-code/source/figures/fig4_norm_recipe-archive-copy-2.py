import sys
sys.path.insert(0, '/root/spectral_optim_vision_geometry')

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

from plot_style import apply_style, COLORS, FONT_SIZES
apply_style()

plt.rcParams.update({
    'font.family': 'serif',
    'savefig.pad_inches': 0.05,
})

# ============================================================
# Panel (a): Normalization Swap — SGD failure on LN architectures
# ============================================================
def panel_norm_swap(ax):
    # x-labels: architecture + norm type
    labels = ['ResNet-50\n(BatchNorm)', 'DeiT-S\n(LayerNorm)', 'ConvNeXt-T\n(LayerNorm)']

    # Data from Table 1 (CIFAR-100, 20ep)
    muon_acc  = [76.88, 62.67, 74.62]
    adamw_acc = [67.85, 52.33, 58.54]
    sgd_acc   = [69.50, 43.98, 11.51]

    x = np.arange(len(labels))
    width = 0.22
    gap = 0.04

    bars_muon = ax.bar(x - width - gap/2, muon_acc, width,
                       label='Muon', color=COLORS['Muon'],
                       edgecolor='white', linewidth=0.5, zorder=3)
    bars_adamw = ax.bar(x, adamw_acc, width,
                        label='AdamW', color=COLORS['AdamW'],
                        edgecolor='white', linewidth=0.5, zorder=3)
    bars_sgd = ax.bar(x + width + gap/2, sgd_acc, width,
                      label='SGD', color=COLORS['SGD'],
                      edgecolor=COLORS['SGD'], linewidth=0.5, zorder=3,
                      hatch='..', alpha=0.85)

    # Random chance line at 1%
    ax.axhline(y=1.0, color='#888888', linestyle='--', linewidth=0.8, zorder=2)
    ax.text(2.62, 1.0, 'random (1%)',
            va='center', ha='left', fontsize=12, color='#333333', fontstyle='italic')

    # "11.5%" annotation on SGD ConvNeXt-T bar
    sgd_convnext_bar = bars_sgd[2]
    ax.text(sgd_convnext_bar.get_x() + sgd_convnext_bar.get_width()/2,
            sgd_convnext_bar.get_height() + 1.5,
            '11.5%', ha='center', va='bottom', fontsize=11, fontweight='bold',
            color='black',
            bbox=dict(boxstyle='round,pad=0.3', facecolor='white', edgecolor='none', alpha=0.8))

    ax.set_xticks(x)
    ax.set_xticklabels(labels, fontsize=13, linespacing=1.3)

    ax.set_ylabel('Validation Accuracy (%)')
    ax.set_ylim(0, 88)
    ax.set_xlim(-0.55, 2.85)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.grid(axis='y', alpha=0.3, linewidth=0.5)
    ax.set_axisbelow(True)

    ax.legend(fontsize=11, loc='upper right',
              framealpha=0.9, edgecolor='none', ncol=1)

    ax.set_title('(a) Normalization-Dependent SGD Failure', fontsize=10,
                 fontweight='bold', pad=10)


# ============================================================
# Panel (b): Recipe Robustness — Base vs Enhanced
# ============================================================
def panel_recipe(ax):
    archs = ['ResNet-50', 'DeiT-S', 'ConvNeXt-T']

    # Gap = Muon - AdamW (from Table 15 / enhanced recipe table)
    gap_base     = [9.03, 10.34, 16.08]
    gap_enhanced = [10.92, 20.67, 11.91]

    x = np.arange(len(archs))
    width = 0.30
    gap_offset = 0.02

    bars_base = ax.bar(x - width/2 - gap_offset, gap_base, width,
                       label='Base recipe', color=COLORS['Muon'],
                       edgecolor='white', linewidth=0.5, zorder=3)
    bars_enh = ax.bar(x + width/2 + gap_offset, gap_enhanced, width,
                      label='Enhanced recipe', color=COLORS['Muon'],
                      edgecolor=COLORS['Muon'], linewidth=0.5, zorder=3,
                      hatch='xx', alpha=0.7)

    # Bracket annotations with gap delta
    for i in range(len(archs)):
        b_h = gap_base[i]
        e_h = gap_enhanced[i]
        delta = e_h - b_h
        sign = '+' if delta >= 0 else ''
        max_h = max(b_h, e_h)

        bx_center = x[i] - width/2 - gap_offset
        ex_center = x[i] + width/2 + gap_offset
        bracket_y = max_h + 1.5

        # Bracket lines
        ax.plot([bx_center, bx_center], [b_h + 0.3, bracket_y],
                color='black', linewidth=1.5, zorder=4, clip_on=False)
        ax.plot([bx_center, ex_center], [bracket_y, bracket_y],
                color='black', linewidth=1.5, zorder=4, clip_on=False)
        ax.plot([ex_center, ex_center], [e_h + 0.3, bracket_y],
                color='black', linewidth=1.5, zorder=4, clip_on=False)

        # Delta text
        color = '#CC3311' if delta > 0 else '#009988'
        ax.text((bx_center + ex_center) / 2, bracket_y + 0.6,
                f'{sign}{delta:.2f} pp', ha='center', va='bottom',
                fontsize=10.5, fontweight='bold', color=color)

        # Bar value labels inside
        ax.text(bx_center, b_h / 2, f'{b_h:.1f}', ha='center', va='center',
                fontsize=10.5, color='white', fontweight='bold')
        ax.text(ex_center, e_h / 2, f'{e_h:.1f}', ha='center', va='center',
                fontsize=10.5, color='white', fontweight='bold')

    ax.set_xticks(x)
    ax.set_xticklabels(archs, fontsize=13)
    ax.set_ylabel('Muon $-$ AdamW Gap (pp)')
    ax.set_ylim(0, 27)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.grid(axis='y', alpha=0.3, linewidth=0.5)
    ax.set_axisbelow(True)

    ax.legend(fontsize=11, loc='upper left',
              framealpha=0.9, edgecolor='none')

    ax.set_title('(b) Recipe Robustness: Muon–AdamW Gap', fontsize=10,
                 fontweight='bold', pad=10)


# ============================================================
# Combined figure
# ============================================================
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 4.5))

panel_norm_swap(ax1)
panel_recipe(ax2)

plt.subplots_adjust(left=0.06, right=0.96, bottom=0.14, top=0.90, wspace=0.28)

outdir = '/root/spectral_optim_vision_geometry/paper/figures'
fig.savefig(f'{outdir}/fig4_norm_recipe.pdf')
fig.savefig(f'{outdir}/fig4_norm_recipe.png')
plt.close(fig)
print('Saved fig4_norm_recipe.pdf and fig4_norm_recipe.png')
