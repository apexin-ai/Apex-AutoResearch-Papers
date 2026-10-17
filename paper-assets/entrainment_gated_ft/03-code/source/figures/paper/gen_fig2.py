import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patheffects as pe
import matplotlib.patches as mpatches
import numpy as np
import os
from palette import BLUE, CORAL, TEAL, AMBER, GRAY, DARK, LIGHT, RCPARAMS

plt.rcParams.update(RCPARAMS)

data = [
    ('LAMBADA',       'retrieval',      -1.0,  0.0167),
    ('HellaSwag',     'reasoning',       0.3,  0.683),
    ('ARC-Challenge', 'reasoning',       0.6,  0.35),
    ('WinoGrande',    'reasoning',       0.1,  0.95),
    ('ARC-Easy',      'mixed',          -0.7,  0.2333),
    ('MMLU',          'mixed',          -0.7,  0.2333),
    ('BoolQ',         'comprehension',   0.2,  0.7833),
    ('PIQA',          'reasoning',      -0.5,  0.45),
    ('SciQ',          'mixed',           0.1,  0.95),
    ('XStoryCloze',   'mixed',          -0.6,  0.35),
]

benchmarks = [d[0] for d in data]
taxonomies = [d[1] for d in data]
rhos = [d[2] for d in data]
pvals = [d[3] for d in data]

order = np.argsort(rhos)
benchmarks = [benchmarks[i] for i in order]
taxonomies = [taxonomies[i] for i in order]
rhos = [rhos[i] for i in order]
pvals = [pvals[i] for i in order]

tax_colors = {
    'retrieval': BLUE,
    'reasoning': AMBER,
    'comprehension': TEAL,
    'mixed': GRAY,
}

fig, ax = plt.subplots(figsize=(3.3, 2.8))

ax.axvline(0, color='#DDDDDD', linewidth=0.5, zorder=1)

y_positions = np.arange(len(benchmarks))

for i, (bench, tax, rho, p) in enumerate(zip(benchmarks, taxonomies, rhos, pvals)):
    color = tax_colors[tax]
    is_lambada = bench == 'LAMBADA'

    ax.plot([0, rho], [i, i], '-', color=color,
            linewidth=0.6 if not is_lambada else 0.9,
            alpha=0.25 if not is_lambada else 0.45, zorder=2)

    if is_lambada:
        ax.plot(rho, i, 'o', color=color, markersize=5.5, zorder=5,
                markeredgecolor='white', markeredgewidth=0.5)
    else:
        ax.plot(rho, i, 'o', markersize=4, zorder=4,
                markerfacecolor='white', markeredgecolor=color, markeredgewidth=0.8)

    text_x = max(rho + 0.07, 0.12)
    if is_lambada:
        label = r'$\rho$=$-$1.0, p=.017'
        t = ax.text(text_x, i, label, fontsize=5.5, fontweight='bold',
                    color=color, va='center', ha='left')
    else:
        rho_str = f'{rho:.1f}'
        p_str = f'{p:.3f}'.lstrip('0')
        label = f'$\\rho$={rho_str}, p={p_str}'
        t = ax.text(text_x, i, label, fontsize=5, color='#AAAAAA',
                    va='center', ha='left')
    t.set_path_effects([pe.withStroke(linewidth=1.5, foreground='white')])

ax.set_yticks(y_positions)
ax.set_yticklabels(benchmarks, fontsize=6.5)
ax.set_xlim(-1.15, 1.10)
ax.set_ylim(-0.5, len(benchmarks) - 0.5)
ax.set_xlabel(r'Spearman $\rho$  (attention ratio vs. cross-arch. $\sigma$)')
ax.invert_yaxis()

ytick_labels = ax.get_yticklabels()
for lbl in ytick_labels:
    txt = lbl.get_text()
    for bench_name, tax_name in zip(benchmarks, taxonomies):
        if txt == bench_name:
            lbl.set_color(tax_colors[tax_name])
            if txt == 'LAMBADA':
                lbl.set_fontweight('bold')
            break

legend_handles = [
    mpatches.Patch(color=BLUE, label='Retrieval'),
    mpatches.Patch(color=AMBER, label='Reasoning'),
    mpatches.Patch(color=TEAL, label='Compr.'),
    mpatches.Patch(color=GRAY, label='Mixed'),
]
ax.legend(handles=legend_handles, loc='lower left',
          frameon=False, borderpad=0.3, handletextpad=0.4,
          handlelength=0.8, fontsize=5.5, ncol=2,
          columnspacing=0.6,
          bbox_to_anchor=(0.0, 0.0))

out_dir = os.path.dirname(os.path.abspath(__file__))
paper_fig_dir = '/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/figures'
os.makedirs(paper_fig_dir, exist_ok=True)

for d in [out_dir, paper_fig_dir]:
    fig.savefig(os.path.join(d, 'fig2_task_specificity.pdf'))
    fig.savefig(os.path.join(d, 'fig2_task_specificity.png'), dpi=300)
plt.close()
print('Saved fig2_task_specificity')
