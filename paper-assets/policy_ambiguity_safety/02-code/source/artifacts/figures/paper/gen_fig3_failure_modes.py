import json
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patheffects as pe
import matplotlib.colors as mcolors
import numpy as np

plt.rcParams.update({
    'font.family': 'DejaVu Sans',
    'font.size': 11, 'axes.titlesize': 13, 'axes.labelsize': 12,
    'xtick.labelsize': 10, 'ytick.labelsize': 10, 'legend.fontsize': 10,
    'figure.dpi': 300, 'savefig.dpi': 300,
    'savefig.bbox': 'tight', 'savefig.pad_inches': 0.05,
    'axes.spines.top': False, 'axes.spines.right': False,
    'pdf.fonttype': 42, 'ps.fonttype': 42,
    'lines.linewidth': 1.8,
})

BASE = '/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/plan_005'
with open(f'{BASE}/summary.json') as f:
    d1 = json.load(f)
with open(f'{BASE}/summary_gpt41.json') as f:
    d2 = json.load(f)

FAILURE_MODES = [
    'assumption_based_action',
    'scope_misapplication',
    'unauthorized_escalation',
    'arbitrary_rule_selection',
    'conservative_refusal',
]
FM_SHORT = ['Assumption', 'Scope\nMisapply', 'Unauth.\nEscalation', 'Arbitrary\nRule', 'Conserv.\nRefusal']
FM_FULL = [
    'Agent acts on\nassumptions',
    'Misapplied\nscope boundary',
    'Unauthorized\nprivilege escalation',
    'Arbitrary rule\nselection',
    'Conservative\nrefusal to act',
]

TYPES = ['authorization_scope', 'incompleteness', 'conditional_precedence',
         'scopal', 'lexical', 'coreferential']
TYPE_LABELS = ['Authorization\nScope', 'Incomplete-\nness', 'Conditional\nPrecedence',
               'Scopal', 'Lexical', 'Coreferential']
LAYERS = ['Specification', 'Specification', 'Specification',
          'Linguistic', 'Linguistic', 'Linguistic']

fm1 = d1['per_type_failure_modes']
fm2 = d2['per_type_failure_modes']

data = np.zeros((len(TYPES), len(FAILURE_MODES)))
for i, t in enumerate(TYPES):
    p1 = fm1[t]['percentages']
    p2 = fm2[t]['percentages']
    for j, fm in enumerate(FAILURE_MODES):
        v1 = p1.get(fm, 0.0)
        v2 = p2.get(fm, 0.0)
        data[i, j] = (v1 + v2) / 2.0

print("Averaged data (%):")
for i, t in enumerate(TYPES):
    vals = ', '.join(f'{data[i,j]:.1f}' for j in range(len(FAILURE_MODES)))
    print(f"  {t}: [{vals}]")

fig, ax = plt.subplots(figsize=(7.5, 6.0))

cmap = plt.cm.OrRd
norm = mcolors.Normalize(vmin=0, vmax=80)

im = ax.imshow(data, cmap=cmap, norm=norm, aspect='auto')

spec_bg = '#FFF5F0'
ling_bg = '#F0F5FF'
for i in range(len(TYPES)):
    bg = spec_bg if LAYERS[i] == 'Specification' else ling_bg
    for j in range(len(FAILURE_MODES)):
        rect = plt.Rectangle((j - 0.5, i - 0.5), 1, 1,
                              facecolor=bg, alpha=0.15, zorder=0)
        ax.add_patch(rect)

row_max = data.max(axis=1)
for i in range(len(TYPES)):
    for j in range(len(FAILURE_MODES)):
        val = data[i, j]
        if val == 0:
            txt = '—'
            color = '#999999'
            weight = 'normal'
            fsize = 10
        else:
            txt = f'{val:.1f}%'
            is_dominant = (val == row_max[i]) and val > 0
            if val > 50:
                color = 'white'
            else:
                color = '#333333'
            weight = 'bold' if is_dominant else 'normal'
            fsize = 12 if is_dominant else 10
        t = ax.text(j, i, txt, ha='center', va='center',
                    fontsize=fsize, color=color, fontweight=weight, zorder=5)
        t.set_path_effects([pe.withStroke(linewidth=2.0, foreground='white', alpha=0.6)])

ax.axhline(2.5, color='#333333', linewidth=2.5, zorder=3)

ax.set_xticks(range(len(FAILURE_MODES)))
ax.set_xticklabels(FM_SHORT, ha='center', fontsize=9.5, linespacing=1.1)
ax.xaxis.set_ticks_position('top')
ax.xaxis.set_label_position('top')
ax.tick_params(axis='x', which='both', length=0, pad=8)

ax.set_yticks(range(len(TYPES)))
ax.set_yticklabels(TYPE_LABELS, fontsize=9.5, linespacing=1.1)
ax.tick_params(axis='y', which='both', length=0, pad=6)

layer_x = -1.85
ax.text(layer_x, 1.0, 'Spec.\nLayer', ha='center', va='center',
        fontsize=10, fontweight='bold', color='#C0392B',
        transform=ax.transData, fontstyle='italic')
ax.text(layer_x, 4.0, 'Ling.\nLayer', ha='center', va='center',
        fontsize=10, fontweight='bold', color='#2471A3',
        transform=ax.transData, fontstyle='italic')

for i in range(len(TYPES)):
    for j in range(len(FAILURE_MODES)):
        rect = plt.Rectangle((j - 0.5, i - 0.5), 1, 1,
                              fill=False, edgecolor='white', linewidth=1.5, zorder=2)
        ax.add_patch(rect)

ax.set_xlim(-0.5, len(FAILURE_MODES) - 0.5)
ax.set_ylim(len(TYPES) - 0.5, -0.5)

cbar = fig.colorbar(im, ax=ax, fraction=0.03, pad=0.04, shrink=0.8)
cbar.set_label('Failure Rate (%)', fontsize=10)
cbar.ax.tick_params(labelsize=9)

ax.set_title('Failure Mode Distribution by Ambiguity Type', fontsize=13, pad=55, fontweight='bold')

ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['bottom'].set_visible(False)
ax.spines['left'].set_visible(False)

plt.subplots_adjust(left=0.25, top=0.82)

OUT = '/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/figures/paper'
fig.savefig(f'{OUT}/fig3_failure_modes.pdf')
fig.savefig(f'{OUT}/fig3_failure_modes.png')
plt.close()
print(f'Saved: {OUT}/fig3_failure_modes.pdf')
print(f'Saved: {OUT}/fig3_failure_modes.png')

import os
for ext in ['pdf', 'png']:
    fpath = f'{OUT}/fig3_failure_modes.{ext}'
    sz = os.path.getsize(fpath)
    print(f'{ext.upper()} size: {sz} bytes')
