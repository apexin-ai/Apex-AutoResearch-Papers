import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patheffects as pe
import numpy as np
from matplotlib.patches import Patch

plt.rcParams.update({
    'font.family': 'DejaVu Sans',
    'font.size': 6,
    'axes.labelsize': 7,
    'xtick.labelsize': 6,
    'ytick.labelsize': 5.5,
    'figure.dpi': 300,
    'savefig.dpi': 300,
    'savefig.bbox': 'tight',
    'savefig.pad_inches': 0.02,
    'axes.spines.top': False,
    'axes.spines.right': False,
    'pdf.fonttype': 42,
    'ps.fonttype': 42,
})

raw_data = {
    "Prompt-Level": [
        ("Contrastive prompting", -1.1),
        ("Cross-model (Q14B→M)", -0.98),
        ("Cross-model (w→s)", 0.0),
        ("Z3 feedback", 0.0),
        ("Cross-trace UNSAT", 0.0),
        ("Multi-temperature", 0.0),
        ("Discrim. filtering", 0.0),
        ("Generational", 0.49),
        ("Cross-model (Q3→M)", 0.98),
    ],
    "Method-Level": [
        ("LLM-Debate", -18.63),
        ("Contrastive Scoring", -9.31),
        ("ICG", -0.49),
    ],
    "Additional": [
        ("MIN-UNSAT", -6.5),
        ("PROVE (code verif.)", -1.9),
        ("Prob. perturbation", -1.0),
        ("Cross-model SICA", -0.49),
        ("Z3 trace filter", -0.49),
        ("CEGIS (iterative)", 0.0),
        ("DeepConf (logprob)", 0.0),
        ("κ-aware SC", 0.0),
        ("Bootstrapped gold", 0.0),
        ("Sel. abstention", 0.0),
        ("ASCII perturbation", 0.0),
    ],
}

COLORS = {
    "Prompt-Level": '#56B4E9',
    "Method-Level": '#E69F00',
    "Additional": '#009E73',
}

CLIP_X = -12.0
ROW_STEP = 0.55
GROUP_GAP = 0.35

for cat in raw_data:
    raw_data[cat] = sorted(raw_data[cat], key=lambda x: x[1])

categories_order = ["Prompt-Level", "Method-Level", "Additional"]

names, values, colors, y_positions = [], [], [], []
cat_boundaries = []

y = 0
for gi, cat in enumerate(categories_order):
    if gi > 0:
        y += GROUP_GAP
    y_start = y
    for name, val in raw_data[cat]:
        names.append(name)
        values.append(val)
        colors.append(COLORS[cat])
        y_positions.append(y)
        y += ROW_STEP
    cat_boundaries.append((y_start, y - ROW_STEP, cat))

y_positions = np.array(y_positions)

display_values = []
is_clipped = []
for v in values:
    if v < CLIP_X:
        display_values.append(CLIP_X)
        is_clipped.append(True)
    else:
        display_values.append(v)
        is_clipped.append(False)

fig, ax = plt.subplots(figsize=(3.3, 3.3))

ax.axvspan(-1, 1, alpha=0.06, color='#888888', zorder=0)
ax.axvline(x=0, color='black', linewidth=0.5, zorder=2)

for gi, (y_start, y_end, cat) in enumerate(cat_boundaries):
    if gi > 0:
        sep_y = y_start - GROUP_GAP / 2
        ax.axhline(y=sep_y, color='#cccccc', linewidth=0.4, zorder=1)

bars = ax.barh(y_positions, display_values, height=0.36, color=colors, alpha=0.85,
               edgecolor='white', linewidth=0.2, zorder=3)

for i, (clipped, val) in enumerate(zip(is_clipped, values)):
    if clipped:
        bx = CLIP_X
        by = y_positions[i]
        zz_x = [bx + 0.06, bx - 0.09, bx + 0.09, bx - 0.06]
        zz_y = [by - 0.12, by - 0.04, by + 0.04, by + 0.12]
        ax.plot(zz_x, zz_y, color='white', linewidth=1.2, zorder=5,
                solid_capstyle='round')
        t = ax.text(bx + 0.15, by, f' {val:.1f}pp ←',
                    ha='left', va='center', fontsize=4.5, fontweight='bold',
                    color='#b37400')
        t.set_path_effects([pe.withStroke(linewidth=1.5, foreground='white')])

for i, (val, dv) in enumerate(zip(values, display_values)):
    if is_clipped[i]:
        continue
    if abs(val) < 0.01:
        continue
    if val <= -5:
        ax.text(dv / 2, y_positions[i], f'{val:.1f}', ha='center', va='center',
                fontsize=4.5, color='white', fontweight='bold')
    elif val < -1.2:
        ax.text(dv - 0.12, y_positions[i], f'{val:.1f}', ha='right', va='center',
                fontsize=4.5, color='#555555')
    elif val > 0:
        ax.text(dv + 0.12, y_positions[i], f'+{val:.2g}', ha='left', va='center',
                fontsize=4.5, color='#555555')

ax.set_yticks(y_positions)
ax.set_yticklabels(names)
ax.set_xlabel('Δ (pp) vs. Self-Consistency')
ax.set_xlim(-13.5, 2.2)
ax.set_ylim(y_positions[-1] + 0.45, y_positions[0] - 0.45)

ax.grid(axis='x', alpha=0.12, zorder=0)
ax.spines['left'].set_visible(False)
ax.tick_params(axis='y', length=0, pad=2)

legend_elements = [
    Patch(facecolor=COLORS["Prompt-Level"], alpha=0.85, label='Prompt-Level (9)'),
    Patch(facecolor=COLORS["Method-Level"], alpha=0.85, label='Method-Level (3)'),
    Patch(facecolor=COLORS["Additional"], alpha=0.85, label='Additional (11)'),
]
ax.legend(handles=legend_elements, loc='lower left', fontsize=5,
          framealpha=0.92, edgecolor='#dddddd', handlelength=0.8,
          handletextpad=0.3, borderpad=0.3, labelspacing=0.25)

ax.text(0, y_positions[0] - 0.38, '±1pp', ha='center', va='top',
        fontsize=4.5, color='#aaaaaa', fontstyle='italic')

plt.tight_layout(pad=0.2)

outdir = '/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/figures/paper'
plt.savefig(f'{outdir}/fig2_interventions_compact.pdf')
plt.savefig(f'{outdir}/fig2_interventions_compact.png', dpi=300)
plt.close()
print('Done: fig2_interventions_compact.pdf')
