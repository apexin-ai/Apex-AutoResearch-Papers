"""Generate a top-tier framework overview figure for the paper."""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
import numpy as np

plt.rcParams.update({
    'font.family': 'serif',
    'font.serif': ['Times New Roman', 'DejaVu Serif'],
    'mathtext.fontset': 'cm',
    'font.size': 9,
})

C = {
    'panel_bg':    '#E8EEF5',   'panel_border':  '#4A6FA5',  'panel_title': '#2C4A7C',
    'adv_bg':      '#FCEAE8',   'adv_border':    '#C0504D',  'adv_title':   '#8B2F2D',
    'metric_bg':   '#E8F5E9',   'metric_border': '#5B9A5B',  'metric_title':'#2E6B2E',
    'agg_bg':      '#F3EBF8',   'agg_border':    '#7E57A0',  'agg_title':   '#4A2D6E',
    'arrow':       '#5A5A5A',
    'sub_bg':      '#FFFFFF',
    'sub_border':  '#D0D0D0',
    'text_main':   '#2C2C2C',
    'text_sub':    '#555555',
    'eq_bg':       '#FFFDE7',
    'eq_border':   '#E0D68A',
}

fig, ax = plt.subplots(figsize=(14.5, 4.0))
ax.set_xlim(-0.2, 14.7)
ax.set_ylim(-0.3, 4.0)
ax.set_aspect('equal')
ax.axis('off')

def draw_stage(x, y, w, h, bg, border, title, title_color, sec_ref):
    box = FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.10",
                         facecolor=bg, edgecolor=border, linewidth=1.6, zorder=2)
    ax.add_patch(box)
    # Title bar background
    th = 0.50
    tb = FancyBboxPatch((x + 0.08, y + h - th - 0.08), w - 0.16, th,
                         boxstyle="round,pad=0.06", facecolor=border,
                         edgecolor='none', alpha=0.13, zorder=3)
    ax.add_patch(tb)
    ax.text(x + w/2, y + h - th/2 - 0.05, title,
            ha='center', va='center', fontsize=10.5, fontweight='bold',
            color=title_color, zorder=4)
    ax.text(x + w - 0.15, y + h - th/2 - 0.05, sec_ref,
            ha='right', va='center', fontsize=7, color=title_color,
            alpha=0.65, fontstyle='italic', zorder=4)
    return y + h - th - 0.22  # content_top


def draw_sub_box(x, y, w, h, label, detail=None, bg='#FFFFFF', border='#D0D0D0',
                 label_size=8, detail_size=7):
    sb = FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.04",
                         facecolor=bg, edgecolor=border, linewidth=0.7, zorder=3)
    ax.add_patch(sb)
    if detail:
        ax.text(x + 0.10, y + h/2, label, ha='left', va='center',
                fontsize=label_size, fontweight='bold', color=C['text_main'], zorder=4)
        ax.text(x + w - 0.10, y + h/2, detail, ha='right', va='center',
                fontsize=detail_size, color=C['text_sub'], zorder=4)
    else:
        ax.text(x + w/2, y + h/2, label, ha='center', va='center',
                fontsize=label_size, fontweight='bold', color=C['text_main'], zorder=4)


# ── Layout ──
bw = 3.2
bh = 3.2
by = 0.1
gap = 0.45
xp = [0, bw + gap, 2*(bw + gap), 3*(bw + gap)]
sb_h = 0.42
sb_gap = 0.10
sb_margin = 0.14
sb_w = bw - 2 * sb_margin

# ── Stage 1: Panel Construction ──
ct = draw_stage(xp[0], by, bw, bh, C['panel_bg'], C['panel_border'],
                'Panel Construction', C['panel_title'], '§3')
items1 = [
    ('N = 15 judges', '6 families, 3 tiers'),
    ('K ∈ {3, 5, 7}', '455 – 6,435 panels'),
    ('2 benchmarks', 'MMLU, ARC'),
    ('Exhaustive', 'all C(N, K) combos'),
]
for i, (lab, det) in enumerate(items1):
    sy = ct - i * (sb_h + sb_gap)
    draw_sub_box(xp[0] + sb_margin, sy - sb_h, sb_w, sb_h, lab, det)

# ── Stage 2: Adversary Model ──
ct = draw_stage(xp[1], by, bw, bh, C['adv_bg'], C['adv_border'],
                'Adversary Model', C['adv_title'], '§3')
attacks = [
    ('Prompt injection', 'targeted'),
    ('Sycophancy', 'shared-bias'),
    ('Score manipulation', 'targeted'),
    ('Verbosity bias', 'shared-bias'),
    ('Position / Authority', 'shared-bias'),
]
atk_h = 0.34
atk_gap = 0.07
for i, (lab, det) in enumerate(attacks):
    sy = ct - i * (atk_h + atk_gap)
    draw_sub_box(xp[1] + sb_margin, sy - atk_h, sb_w, atk_h, lab, det,
                 bg='#FFF8F7', border='#E8C4C4', label_size=7.5, detail_size=6.5)

# ── Stage 3: Vulnerability Metrics ──
ct = draw_stage(xp[2], by, bw, bh, C['metric_bg'], C['metric_border'],
                'Vulnerability Metrics', C['metric_title'], '§3')

# Metric boxes side by side
mbox_w = (sb_w - 0.12) / 2
my = ct - 0.05
# eta_max box
draw_sub_box(xp[2] + sb_margin, my - 0.65, mbox_w, 0.65,
             '', bg='#F1F8F1', border='#A8D0A8')
ax.text(xp[2] + sb_margin + mbox_w/2, my - 0.20,
        r'$\eta_{\max}$', ha='center', va='center', fontsize=13,
        color=C['metric_title'], zorder=4)
ax.text(xp[2] + sb_margin + mbox_w/2, my - 0.48,
        'weakest-link\nvulnerability', ha='center', va='center', fontsize=7,
        color=C['text_sub'], zorder=4, linespacing=1.3)

# K_eff box
draw_sub_box(xp[2] + sb_margin + mbox_w + 0.12, my - 0.65, mbox_w, 0.65,
             '', bg='#F1F8F1', border='#A8D0A8')
ax.text(xp[2] + sb_margin + mbox_w + 0.12 + mbox_w/2, my - 0.20,
        r'$K_{\mathrm{eff}}$', ha='center', va='center', fontsize=13,
        color=C['metric_title'], zorder=4)
ax.text(xp[2] + sb_margin + mbox_w + 0.12 + mbox_w/2, my - 0.48,
        'effective\nindependence', ha='center', va='center', fontsize=7,
        color=C['text_sub'], zorder=4, linespacing=1.3)

# Regression equation
eq_y = my - 0.95
eq_box = FancyBboxPatch((xp[2] + sb_margin, eq_y - 0.38), sb_w, 0.50,
                          boxstyle="round,pad=0.05", facecolor=C['eq_bg'],
                          edgecolor=C['eq_border'], linewidth=0.8, zorder=3)
ax.add_patch(eq_box)
ax.text(xp[2] + bw/2, eq_y - 0.13,
        r'$\log\,\mathrm{ASR} = \alpha + \beta_1 \log K_{\mathrm{eff}} + \beta_2 \log \eta_{\max}$',
        ha='center', va='center', fontsize=8.5, color=C['text_main'], zorder=4)

# Bullet items
bullets = ['Wild cluster bootstrap', 'Dominance analysis']
for i, b in enumerate(bullets):
    iy = eq_y - 0.58 - i * 0.30
    ax.text(xp[2] + sb_margin + 0.06, iy, f'▸  {b}',
            ha='left', va='center', fontsize=7.5, color=C['text_sub'], zorder=4)

# ── Stage 4: Aggregation ──
ct = draw_stage(xp[3], by, bw, bh, C['agg_bg'], C['agg_border'],
                'Aggregation', C['agg_title'], '§3')
agg_items = [
    ('Majority vote', 'baseline'),
    ('Weighted vote', 'acc-weighted'),
    ('Threshold', 'unanimity, t = K'),
    ('Bayesian calibration', 'posterior > 0.5'),
]
for i, (lab, det) in enumerate(agg_items):
    sy = ct - i * (sb_h + sb_gap)
    draw_sub_box(xp[3] + sb_margin, sy - sb_h, sb_w, sb_h, lab, det)

# ── Arrows ──
arrow_y = by + bh / 2
for i in range(3):
    x1 = xp[i] + bw + 0.02
    x2 = xp[i+1] - 0.02
    arr = FancyArrowPatch(
        (x1, arrow_y), (x2, arrow_y),
        arrowstyle='->,head_width=5,head_length=4',
        connectionstyle='arc3,rad=0',
        color=C['arrow'], linewidth=1.8, zorder=5, mutation_scale=1)
    ax.add_patch(arr)

plt.tight_layout(pad=0.05)
out = '/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/figures'
fig.savefig(f'{out}/fig_framework.pdf', bbox_inches='tight', dpi=300, pad_inches=0.03)
fig.savefig(f'{out}/fig_framework.png', bbox_inches='tight', dpi=200, pad_inches=0.03)
print('Done')
