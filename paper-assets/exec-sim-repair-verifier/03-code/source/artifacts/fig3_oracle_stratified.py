import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams.update({
    'font.family': 'serif',
    'font.serif': ['Times New Roman', 'Times', 'STIXGeneral', 'DejaVu Serif'],
    'mathtext.fontset': 'stix',
    'font.size': 11,
    'axes.labelsize': 12,
    'xtick.labelsize': 10,
    'ytick.labelsize': 10,
    'legend.fontsize': 10,
    'figure.dpi': 300,
    'savefig.dpi': 300,
    'savefig.bbox': 'tight',
    'savefig.pad_inches': 0.05,
    'pdf.fonttype': 42,
    'ps.fonttype': 42,
    'axes.spines.top': False,
    'axes.spines.right': False,
})

IID_COLOR = '#56B4E9'
BLOCK_COLOR = '#0072B2'
ANNOT_COLOR = '#D55E00'

bins = ['T=1', 'T=2', 'T=3–5', r'T$\geq$6']
instance_pct = [68.7, 19.1, 7.1, 5.1]
iid_adv = [-0.04, 18.49, 25.0, 30.0]
block_adv = [-0.09, 31.69, 40.74, 40.06]

x = np.arange(len(bins))
width = 0.35

fig, ax = plt.subplots(figsize=(7, 5))

bars_iid = ax.bar(x - width/2, iid_adv, width, label='i.i.d. model',
                   color=IID_COLOR, edgecolor='white', linewidth=0.5)
bars_block = ax.bar(x + width/2, block_adv, width, label='Block-corr model (ICC=0.19)',
                     color=BLOCK_COLOR, edgecolor='white', linewidth=0.5)

ax.axhline(y=0, color='gray', linestyle='--', linewidth=0.8, zorder=0)

for i, pct in enumerate(instance_pct):
    max_val = max(iid_adv[i], block_adv[i])
    y_pos = max(max_val + 2.5, 3)
    ax.text(x[i], y_pos, f'{pct}%', ha='center', va='bottom',
            fontsize=9, color='#000000', fontstyle='italic')

ax.annotate('55.3% of\ntotal adv.',
            xy=(x[1] + width/2, block_adv[1]),
            xytext=(x[1] + width/2 + 0.1, block_adv[1] + 5),
            fontsize=9, color=ANNOT_COLOR, fontweight='bold',
            ha='left', va='bottom',
            arrowprops=dict(arrowstyle='->', color=ANNOT_COLOR, lw=1.5))

ax.set_xlabel('FAIL_TO_PASS Test Count (T)')
ax.set_ylabel('Oracle Per-Test Advantage (pp)')
ax.set_xticks(x)
ax.set_xticklabels(bins)
ax.set_ylim(-5, 50)
ax.legend(loc='upper left', frameon=True, framealpha=0.9, edgecolor='#cccccc')

ax.text(0.98, 0.02, 'Overall: 10.93pp  |  P2P reg.: 1.0%',
        transform=ax.transAxes, ha='right', va='bottom',
        fontsize=8.5, color='#000000')

plt.tight_layout()

out_dir = '/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts'
fig.savefig(f'{out_dir}/fig3_oracle_stratified.pdf')
fig.savefig(f'{out_dir}/fig3_oracle_stratified.png')
fig.savefig(f'{out_dir}/figures/paper/fig3_oracle_stratified.pdf')
fig.savefig(f'{out_dir}/figures/paper/fig3_oracle_stratified.png')
plt.close()
print('Done: fig3_oracle_stratified.pdf + .png')
