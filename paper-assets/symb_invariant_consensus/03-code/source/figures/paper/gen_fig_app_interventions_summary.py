import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patheffects as pe
import numpy as np
from matplotlib.patches import Patch

plt.rcParams.update({
    'font.family': 'DejaVu Sans',
    'font.size': 10,
    'axes.labelsize': 11,
    'xtick.labelsize': 9,
    'ytick.labelsize': 9,
    'figure.dpi': 300,
    'savefig.dpi': 300,
    'savefig.bbox': 'tight',
    'savefig.pad_inches': 0.05,
    'axes.spines.top': False,
    'axes.spines.right': False,
    'pdf.fonttype': 42,
    'ps.fonttype': 42,
})

raw_data = {
    "Prompt-Level": [
        ("Contrastive prompting", -1.1),
        ("Cross-model weak→strong", 0.0),
        ("Cross-model Qwen3→Mistral", 0.98),
        ("Cross-model Qwen14B→Mistral", -0.98),
        ("Generational (Qwen3-14B)", 0.49),
        ("Z3 feedback", 0.0),
        ("Cross-trace UNSAT", 0.0),
        ("Multi-temperature", 0.0),
        ("Discriminative filtering", 0.0),
    ],
    "Method-Level": [
        ("ICG", -0.49),
        ("Contrastive Scoring", -9.31),
        ("LLM-Debate", -18.63),
    ],
    "Additional Directions": [
        ("PROVE (code verif.)", -1.9),
        ("CEGIS (iterative)", 0.0),
        ("DeepConf (logprob)", 0.0),
        ("Cross-model SICA", -0.49),
        ("Problem perturbation", -1.0),
        ("MIN-UNSAT", -6.5),
        ("κ-aware SC", 0.0),
        ("Z3 trace filter", -0.49),
        ("Bootstrapped gold", 0.0),
        ("Selective abstention", 0.0),
        ("ASCII perturbation", 0.0),
    ],
}

COLORS = {
    "Prompt-Level": '#56B4E9',
    "Method-Level": '#E69F00',
    "Additional Directions": '#009E73',
}

CLIP_X = -11.5
GROUP_GAP = 1.2  # vertical space between category groups

for cat in raw_data:
    raw_data[cat] = sorted(raw_data[cat], key=lambda x: x[1])

categories_order = ["Prompt-Level", "Method-Level", "Additional Directions"]

# Build y positions with gaps between groups
names = []
values = []
colors = []
y_positions = []
cat_spans = []  # (y_start, y_end, cat_name)

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
        y += 1
    cat_spans.append((y_start, y - 1, cat))

y_positions = np.array(y_positions)
n = len(names)

display_values = []
is_clipped = []
for v in values:
    if v < CLIP_X:
        display_values.append(CLIP_X)
        is_clipped.append(True)
    else:
        display_values.append(v)
        is_clipped.append(False)

fig, ax = plt.subplots(figsize=(7, 9))

# Noise zone
ax.axvspan(-1, 1, alpha=0.06, color='#888888', zorder=0)

# Zero line
ax.axvline(x=0, color='black', linewidth=0.8, zorder=2)

# Category headers + separators
for gi, (y_start, y_end, cat) in enumerate(cat_spans):
    header_y = y_start - 0.55
    ax.text(-13, header_y, cat, ha='left', va='bottom',
            fontsize=10, fontweight='bold', color=COLORS[cat], clip_on=False)
    if gi > 0:
        sep_y = y_start - GROUP_GAP / 2
        ax.axhline(y=sep_y, color='#cccccc', linewidth=0.6, zorder=1,
                    xmin=0.0, xmax=1.0)

# Bars
bars = ax.barh(y_positions, display_values, height=0.6, color=colors, alpha=0.85,
               edgecolor='white', linewidth=0.3, zorder=3)

# Clipped bar annotation (Debate)
for i, (clipped, val) in enumerate(zip(is_clipped, values)):
    if clipped:
        bx = CLIP_X
        by = y_positions[i]
        zz_x = [bx + 0.08, bx - 0.12, bx + 0.12, bx - 0.08]
        zz_y = [by - 0.2, by - 0.07, by + 0.07, by + 0.2]
        ax.plot(zz_x, zz_y, color='white', linewidth=1.8, zorder=5,
                solid_capstyle='round')
        t = ax.text(bx + 0.2, by, f'  {val:.1f} pp  ←',
                    ha='left', va='center', fontsize=8, fontweight='bold',
                    color='#b37400')
        t.set_path_effects([pe.withStroke(linewidth=2.5, foreground='white')])

# Value labels
for i, (val, dv) in enumerate(zip(values, display_values)):
    if is_clipped[i]:
        continue
    if abs(val) < 0.01:
        continue
    if val <= -5:
        ax.text(dv / 2, y_positions[i], f'{val:.1f}', ha='center', va='center',
                fontsize=7.5, color='white', fontweight='bold')
    elif val < 0:
        ax.text(dv - 0.15, y_positions[i], f'{val:.1f}', ha='right', va='center',
                fontsize=7.5, color='#555555')
    else:
        ax.text(dv + 0.15, y_positions[i], f'+{val:.2g}', ha='left', va='center',
                fontsize=7.5, color='#555555')

# Noise zone label
ax.text(0, y_positions[0] - 1.2, 'noise zone (±1 pp)', ha='center', va='bottom',
        fontsize=7.5, color='#aaaaaa', fontstyle='italic', clip_on=False)

ax.set_yticks(y_positions)
ax.set_yticklabels(names, fontsize=9)
ax.set_xlabel('Δ (pp) vs. Self-Consistency', fontsize=11)
ax.set_xlim(-13, 2.5)
ax.set_ylim(y_positions[-1] + 0.8, y_positions[0] - 1.0)

ax.grid(axis='x', alpha=0.15, zorder=0)
ax.spines['left'].set_visible(False)
ax.tick_params(axis='y', length=0)

legend_elements = [
    Patch(facecolor=COLORS["Prompt-Level"], alpha=0.85, label='Prompt-Level (9)'),
    Patch(facecolor=COLORS["Method-Level"], alpha=0.85, label='Method-Level (3)'),
    Patch(facecolor=COLORS["Additional Directions"], alpha=0.85, label='Additional Directions (11)'),
]
ax.legend(handles=legend_elements, loc='lower left', fontsize=8.5,
          framealpha=0.9, edgecolor='#dddddd')

plt.tight_layout()

outdir = '/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/figures/paper'
plt.savefig(f'{outdir}/fig_app_interventions_summary.pdf')
plt.savefig(f'{outdir}/fig_app_interventions_summary.png', dpi=300)
plt.close()
print('Done.')
