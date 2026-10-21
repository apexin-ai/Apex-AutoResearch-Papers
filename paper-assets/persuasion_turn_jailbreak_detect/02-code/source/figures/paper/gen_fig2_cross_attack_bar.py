import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

plt.rcParams.update({
    'font.family': 'serif',
    'font.serif': ['Times New Roman', 'DejaVu Serif'],
    'font.size': 8,
    'axes.labelsize': 8,
    'axes.titlesize': 9,
    'xtick.labelsize': 7,
    'ytick.labelsize': 7,
    'legend.fontsize': 7,
    'figure.dpi': 300,
    'savefig.dpi': 300,
    'savefig.bbox': 'tight',
    'savefig.pad_inches': 0.05,
    'axes.spines.top': False,
    'axes.spines.right': False,
    'axes.linewidth': 0.6,
    'pdf.fonttype': 42,
    'ps.fonttype': 42,
})

conditions = ['IID\n(Crescendo)', 'OOD\n(Decep. Delight)', 'OOD\n(FITD)', 'OOD\n(ActorAttack)']
treatment_f1 = [1.00, 0.997, 1.00, 0.972]
baseline_f1  = [1.00, 0.312, 1.00, 0.258]
tfidf_f1     = [1.00, 0.961, 1.00, 0.261]

colors = {
    'treatment': '#0072B2',
    'baseline': '#D55E00',
    'tfidf': '#009E73',
}

x = np.arange(len(conditions))
bar_width = 0.20
gap = 0.03

fig, ax = plt.subplots(figsize=(3.5, 2.2))

offsets = [-(bar_width + gap), 0, bar_width + gap]

bars_t = ax.bar(x + offsets[0], treatment_f1, bar_width, color=colors['treatment'], label='DisPeD (ours)', zorder=3)
bars_b = ax.bar(x + offsets[1], baseline_f1, bar_width, color=colors['baseline'], label='Vanilla DeBERTa', zorder=3)
bars_tf = ax.bar(x + offsets[2], tfidf_f1, bar_width, color=colors['tfidf'], label='TF-IDF LR', zorder=3)

def add_labels_smart(all_bars_list, all_values_list, highlight_map=None):
    """Place bar labels with overlap avoidance.

    all_bars_list: list of bar containers (one per series)
    all_values_list: list of value lists (one per series)
    highlight_map: dict {series_idx: set of group_indices to highlight}
    """
    if highlight_map is None:
        highlight_map = {}
    n_groups = len(all_values_list[0])

    for gi in range(n_groups):
        labels = []
        for si, (bars, values) in enumerate(zip(all_bars_list, all_values_list)):
            bar = bars[gi]
            val = values[gi]
            hl = gi in highlight_map.get(si, set())
            labels.append((bar, val, si, hl))

        # Skip if all values round to 1.00
        if all(v >= 0.995 for _, v, _, _ in labels):
            continue

        # Collect labels to place, sorted by y position
        to_place = []
        for bar, val, si, hl in labels:
            if val >= 0.995:
                continue
            bx = bar.get_x() + bar.get_width() / 2
            to_place.append({'x': bx, 'y': val, 'text': f'{val:.2f}',
                             'hl': hl, 'y_offset': 0.015})

        # Detect and resolve vertical overlaps for nearby labels
        to_place.sort(key=lambda p: p['y'])
        for j in range(1, len(to_place)):
            prev = to_place[j-1]
            curr = to_place[j]
            prev_top = prev['y'] + prev['y_offset']
            curr_top = curr['y'] + curr['y_offset']
            if abs(curr_top - prev_top) < 0.06:
                # Stagger: move lower label below its bar
                to_place[j-1]['y_offset'] = -0.055
                to_place[j-1]['va'] = 'top'

        for p in to_place:
            color = '#C00000' if p['hl'] else 'black'
            weight = 'bold' if p['hl'] else 'normal'
            va = p.get('va', 'bottom')
            ax.text(p['x'], p['y'] + p['y_offset'], p['text'],
                    ha='center', va=va, fontsize=6, color=color,
                    fontweight=weight, zorder=4)

add_labels_smart(
    [bars_t, bars_b, bars_tf],
    [treatment_f1, baseline_f1, tfidf_f1],
    highlight_map={1: {1, 3}, 2: {3}}
)

aa_idx = 3
t_bar = bars_t[aa_idx]
b_bar = bars_b[aa_idx]
arrow_x = (t_bar.get_x() + t_bar.get_width() + b_bar.get_x()) / 2
ax.annotate('', xy=(arrow_x, 0.952),
            xytext=(arrow_x, 0.28),
            arrowprops=dict(arrowstyle='<->', color='#333333', lw=1.3, shrinkA=0, shrinkB=0),
            zorder=5)
ax.text(arrow_x + 0.06, 0.59,
        '+71pp', ha='left', va='center', fontsize=6.5, fontweight='bold', color='#333333', zorder=5,
        bbox=dict(boxstyle='round,pad=0.15', facecolor='white', edgecolor='none', alpha=0.85))

ax.axhline(y=1.0, color='#BBBBBB', linestyle='--', linewidth=0.8, zorder=1)

ax.set_ylim(0, 1.15)
ax.set_ylabel('F1 Score')
ax.set_xticks(x)
ax.set_xticklabels(conditions)
ax.yaxis.grid(True, alpha=0.3, zorder=0)
ax.set_axisbelow(True)

ax.legend(ncol=3, loc='upper center', framealpha=0.95, edgecolor='#CCCCCC',
          bbox_to_anchor=(0.5, 1.15), columnspacing=0.8, handletextpad=0.4,
          borderpad=0.3, handlelength=1.2)

plt.tight_layout()

out_dir = '/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/figures/paper'
fig.savefig(f'{out_dir}/fig2_cross_attack_bar.pdf', format='pdf', bbox_inches='tight', pad_inches=0.05)
fig.savefig(f'{out_dir}/fig2_cross_attack_bar.png', format='png', bbox_inches='tight', pad_inches=0.05, dpi=300)
plt.close()

print('Done: fig2_cross_attack_bar.pdf and .png generated.')
