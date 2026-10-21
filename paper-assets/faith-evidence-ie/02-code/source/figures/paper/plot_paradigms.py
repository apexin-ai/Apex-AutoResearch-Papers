import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

FONT = 'DejaVu Sans'

SFT_BG = '#F0F0F0'
SFT_BORDER = '#999999'
GRPO_BG = '#D6E6F5'
GRPO_BORDER = '#497CAA'
DPO_BG = '#C8E6D8'
DPO_BORDER = '#1A7A5A'
RSFT_BG = '#F5DFA8'
RSFT_BORDER = '#BA862D'
ARROW_COLOR = '#AAAAAA'
TEXT_DARK = '#333333'
TEXT_MID = '#555555'
TEXT_LIGHT = '#888888'
UPDATE_BG = '#FAFAFA'
UPDATE_BORDER = '#CCCCCC'

fig, ax = plt.subplots(figsize=(3.3, 3.0), dpi=300)
ax.set_xlim(0, 3.3)
ax.set_ylim(0, 3.0)
ax.axis('off')
ax.set_aspect('equal')

center_x = 1.65
sft_y = 2.62
sft_w, sft_h = 1.4, 0.42
paradigm_y = 1.70
paradigm_w, paradigm_h = 0.78, 0.40
ced_label_y = 1.18
update_y = 0.68
update_w, update_h = 0.76, 0.26

branch_xs = [0.52, 1.65, 2.78]

def draw_shadow_box(ax, x, y, w, h, facecolor, edgecolor, lw=0.6):
    shadow = FancyBboxPatch(
        (x - w/2 + 0.012, y - h/2 - 0.012), w, h,
        boxstyle="round,pad=0.035,rounding_size=0.045",
        facecolor='#000000', edgecolor='none', alpha=0.04, zorder=1
    )
    ax.add_patch(shadow)
    box = FancyBboxPatch(
        (x - w/2, y - h/2), w, h,
        boxstyle="round,pad=0.035,rounding_size=0.045",
        facecolor=facecolor, edgecolor=edgecolor, linewidth=lw, zorder=2
    )
    ax.add_patch(box)

# SFT box
draw_shadow_box(ax, center_x, sft_y, sft_w, sft_h, SFT_BG, SFT_BORDER, lw=0.7)
ax.text(center_x, sft_y + 0.05, 'SFT Checkpoint', fontsize=9, fontweight='bold',
        fontfamily=FONT, color=TEXT_DARK, ha='center', va='center', zorder=3)
ax.text(center_x, sft_y - 0.09, 'LoRA r=64, DocRED', fontsize=7,
        fontfamily=FONT, color=TEXT_LIGHT, ha='center', va='center', zorder=3)

# Paradigm boxes
paradigm_data = [
    ('GRPO', 'Online RL', GRPO_BG, GRPO_BORDER),
    ('DPO', 'Implicit RL', DPO_BG, DPO_BORDER),
    ('RSFT', 'Selection', RSFT_BG, RSFT_BORDER),
]
ced_labels = ['CED → Reward', 'CED → Preference', 'CED → Filter']
update_labels = ['Gradient', 'Gradient', 'Supervised']

for i, (name, subtitle, bg, border) in enumerate(paradigm_data):
    bx = branch_xs[i]
    draw_shadow_box(ax, bx, paradigm_y, paradigm_w, paradigm_h, bg, border, lw=0.6)
    ax.text(bx, paradigm_y + 0.055, name, fontsize=8.5, fontweight='bold',
            fontfamily=FONT, color=TEXT_DARK, ha='center', va='center', zorder=3)
    ax.text(bx, paradigm_y - 0.075, subtitle, fontsize=7,
            fontfamily=FONT, color=TEXT_MID, ha='center', va='center', zorder=3)

for i, label in enumerate(ced_labels):
    ax.text(branch_xs[i], ced_label_y, label, fontsize=7,
            fontfamily=FONT, color=TEXT_MID, ha='center', va='center', zorder=3,
            fontstyle='italic')

# Update boxes (small rounded pill shapes)
for i, label in enumerate(update_labels):
    bx = branch_xs[i]
    draw_shadow_box(ax, bx, update_y, update_w, update_h, UPDATE_BG, UPDATE_BORDER, lw=0.4)
    ax.text(bx, update_y, label, fontsize=7,
            fontfamily=FONT, color=TEXT_DARK, ha='center', va='center', zorder=3)

# Arrows
def add_arrow(start, end):
    ax.annotate('', xy=end, xytext=start,
                arrowprops=dict(
                    arrowstyle='-|>',
                    color=ARROW_COLOR,
                    linewidth=0.6,
                    mutation_scale=6,
                    shrinkA=0, shrinkB=0,
                ),
                zorder=1)

for bx in branch_xs:
    start_x = center_x + (bx - center_x) * 0.4
    add_arrow(
        (start_x, sft_y - sft_h/2 - 0.01),
        (bx, paradigm_y + paradigm_h/2 + 0.01),
    )

for bx in branch_xs:
    add_arrow(
        (bx, paradigm_y - paradigm_h/2 - 0.01),
        (bx, ced_label_y + 0.06),
    )

for bx in branch_xs:
    add_arrow(
        (bx, ced_label_y - 0.06),
        (bx, update_y + update_h/2 + 0.01),
    )

out = '/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/figures/paper/fig_paradigms'
plt.savefig(f'{out}.png', dpi=300, bbox_inches='tight', pad_inches=0.04, facecolor='white')
plt.savefig(f'{out}.pdf', bbox_inches='tight', pad_inches=0.04, facecolor='white')
plt.close()
print("Done")
