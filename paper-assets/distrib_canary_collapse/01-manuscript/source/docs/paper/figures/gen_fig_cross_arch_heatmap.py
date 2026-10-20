"""
Cross-architecture detection heatmap: PermG fwd detection across model families.
narrative_intent: "The canary mechanism generalizes across architectures,
with interpretable failure modes in specific conditions."
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import csv

plt.rcParams.update({
    'font.family': 'DejaVu Sans',
    'font.size': 9,
    'axes.titlesize': 10,
    'axes.labelsize': 9,
    'xtick.labelsize': 8,
    'ytick.labelsize': 8,
    'legend.fontsize': 7,
    'figure.dpi': 300,
    'savefig.dpi': 300,
    'savefig.bbox': 'tight',
    'savefig.pad_inches': 0.03,
    'axes.spines.top': False,
    'axes.spines.right': False,
    'pdf.fonttype': 42,
    'ps.fonttype': 42,
})

rows = []
with open('artifacts/cross_arch_table7.csv') as f:
    reader = csv.DictReader(f)
    for row in reader:
        if row['PermG_fwd'] and row['note'] not in ('RUNNING', 'RUNNING (~50h)', 'FAILED EXIT_CODE=1'):
            rows.append(row)

def parse_frac(s):
    if not s:
        return np.nan
    num, den = s.split('/')
    return int(num) / int(den)

models = []
permg_fwd = []
k3_vals = []
labels = []

for r in rows:
    model = r['model']
    seed = r['seed']
    domain = r['domain']
    prec = r['precision']
    suffix = ''
    if domain == 'C4':
        suffix = ' (C4)'
    elif prec == 'bf16':
        suffix = ' (bf16)'
    label = f"{model} {seed}{suffix}"
    labels.append(label)
    permg_fwd.append(parse_frac(r['PermG_fwd']))
    k3_vals.append(parse_frac(r['K3_3sigma']))

n = len(labels)
y = np.arange(n)

fig, ax = plt.subplots(figsize=(4.5, 3.2))

bar_height = 0.35
bars1 = ax.barh(y + bar_height/2, [v*100 for v in permg_fwd], bar_height,
                color='#4A90C4', alpha=0.9, label='PermG fwd', edgecolor='#222222', linewidth=0.5)
bars2 = ax.barh(y - bar_height/2, [v*100 for v in k3_vals], bar_height,
                color='#B8D4E8', alpha=0.75, label=r'$K{\geq}3$ consensus')

# Value labels
for i, (pv, kv) in enumerate(zip(permg_fwd, k3_vals)):
    ax.text(pv*100 + 1.5, i + bar_height/2, f'{int(pv*8)}/8',
            va='center', ha='left', fontsize=6, color='#4A90C4', fontweight='bold')
    ax.text(kv*100 + 1.5, i - bar_height/2, f'{int(kv*8)}/8',
            va='center', ha='left', fontsize=6, color='#7BBBD6')

ax.set_yticks(y)
ax.set_yticklabels(labels, fontsize=7)
ax.set_xlabel('Detection rate (%)')
ax.set_xlim(0, 115)
ax.set_xticks([0, 25, 50, 75, 100])
ax.invert_yaxis()

ax.xaxis.grid(True, alpha=0.15, linewidth=0.4)
ax.set_axisbelow(True)

# 75% reference
ax.axvline(x=75, color='#4A90C4', linewidth=0.5, linestyle=':', alpha=0.4)

leg = ax.legend(loc='lower center', bbox_to_anchor=(0.5, 1.02),
                ncol=2, frameon=True, framealpha=0.9,
                edgecolor='#cccccc', borderpad=0.3)
leg.get_frame().set_linewidth(0.4)

fig.subplots_adjust(top=0.92)
plt.savefig('docs/paper/figures/fig_cross_arch_heatmap.pdf')
plt.savefig('docs/paper/figures/fig_cross_arch_heatmap.png')
print('Saved fig_cross_arch_heatmap.pdf + .png')
