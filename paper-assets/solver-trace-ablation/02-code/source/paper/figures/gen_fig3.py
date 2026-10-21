import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams.update({
    'pdf.fonttype': 42, 'ps.fonttype': 42,
    'font.family': 'DejaVu Sans', 'font.size': 8,
    'axes.labelsize': 8, 'axes.titlesize': 9,
    'xtick.labelsize': 8, 'ytick.labelsize': 8,
})

C_TSa = '#D55E00'
C_TSb = '#CC79A7'
C_CE = '#E69F00'
C_PG = '#56B4E9'
C_GENUINE = '#009E73'

conditions = [
    'ISR $\\beta$=0.3',
    'ISR $\\beta$=0.1',
    'Rand $\\beta$=0.3',
    'Rand $\\beta$=0.1',
    'Exec-only',
    'SFT',
]

raw = {
    'ce':      [ 73,  42, 149, 180,  81,  3],
    'tsa':     [ 99, 149,  11,  36,   0,  0],
    'tsb':     [  0,  14,   0,   0,   0,  0],
    'pg':      [  6,  12,   0,  21,   5,  0],
    'genuine': [ 21,  14,   3,  25,   7, 36],
}

totals = [sum(raw[k][i] for k in raw) for i in range(len(conditions))]

ce      = [raw['ce'][i]      / totals[i] * 100 for i in range(len(conditions))]
tsa     = [raw['tsa'][i]     / totals[i] * 100 for i in range(len(conditions))]
tsb     = [raw['tsb'][i]     / totals[i] * 100 for i in range(len(conditions))]
pg      = [raw['pg'][i]      / totals[i] * 100 for i in range(len(conditions))]
genuine = [raw['genuine'][i] / totals[i] * 100 for i in range(len(conditions))]

y = np.arange(len(conditions))
bar_h = 0.52

fig, ax = plt.subplots(figsize=(3.25, 2.6))

kw = dict(height=bar_h, edgecolor='white', linewidth=0.4, zorder=3)

left = np.zeros(len(conditions))
ax.barh(y, tsa, left=left, color=C_TSa, label='TS$_a$ (tautological)', hatch='///', **kw)
left += tsa
ax.barh(y, tsb, left=left, color=C_TSb, label='TS$_b$ (ISR-specific)', hatch='\\\\\\', **kw)
left += tsb
ax.barh(y, ce, left=left, color=C_CE, label='CE (shortcut)', **kw)
left += ce
ax.barh(y, pg, left=left, color=C_PG, label='PG (degenerate)', hatch='...', **kw)
left += pg
ax.barh(y, genuine, left=left, color=C_GENUINE, label='Genuine', hatch='xxx', **kw)
left += genuine

for i, g in enumerate(genuine):
    ax.text(left[i] + 1.0, y[i], f'{g:.0f}%', va='center', ha='left',
            fontsize=8, color=C_GENUINE, fontweight='bold')

isr_ts = tsa[1] + tsb[1]
rand_ts = tsa[3] + tsb[3]
ax.annotate(
    f'TS: {isr_ts:.0f}% vs {rand_ts:.0f}%',
    xy=(rand_ts / 2, y[3]),
    xytext=(62, y[1] + 0.5),
    fontsize=8, fontweight='bold', color=C_TSa,
    ha='center',
    arrowprops=dict(arrowstyle='->', color=C_TSa, lw=0.8),
)

ax.set_yticks(y)
ax.set_yticklabels(conditions)
ax.set_xlabel('Percentage of proved samples (%)')
ax.set_xlim(0, 112)
ax.set_xticks([0, 20, 40, 60, 80, 100])
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

ax.legend(fontsize=8, loc='upper center', bbox_to_anchor=(0.5, -0.16),
          frameon=False, ncol=3, columnspacing=0.5, handletextpad=0.3,
          handlelength=1.2)

base = '/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/figures/fig3_hacking_composition'
fig.savefig(f'{base}.pdf', dpi=300, bbox_inches='tight', pad_inches=0.05)
fig.savefig(f'{base}.png', dpi=300, bbox_inches='tight', pad_inches=0.05)
plt.close()
print(f'Saved: {base}.pdf')
print(f'Saved: {base}.png')
