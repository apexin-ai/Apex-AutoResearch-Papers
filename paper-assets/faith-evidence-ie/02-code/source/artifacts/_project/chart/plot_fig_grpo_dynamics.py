import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patheffects as pe
import numpy as np

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
    'axes.linewidth': 0.6,
    'pdf.fonttype': 42,
    'ps.fonttype': 42,
    'lines.linewidth': 1.8,
})

sft = {'rel_f1': 0.4057, 'evi_f1': 0.7979, 'edcr': 0.7118}

qlora = {
    'steps':  [0,      10,     20,     30,     50,     60,     90,     100],
    'rel_f1': [0.4057, 0.0030, 0.0095, 0.0349, 0.1546, 0.1472, 0.2108, 0.2167],
    'evi_f1': [0.7979, 0.7200, 0.4230, 0.5889, 0.5643, 0.5763, 0.5666, 0.5746],
    'edcr':   [0.7118, 0.9983, 0.9954, 0.9798, 0.8858, 0.9062, 0.8584, 0.8539],
}

bf16 = {
    'steps':  [0,      80,     90,     100],
    'rel_f1': [0.4057, 0.4456, 0.4523, 0.4549],
    'evi_f1': [0.7979, 0.8034, 0.8052, 0.8086],
    'edcr':   [0.7118, 0.6409, 0.6414, 0.6318],
}

C_ORANGE = '#D55E00'
C_BLUE   = '#009E73'

fig, axes = plt.subplots(1, 3, figsize=(14, 3.8))

for ax in axes:
    ax.set_xlabel('Training Step', fontsize=10)
    ax.set_xlim(-5, 108)
    ax.tick_params(labelsize=9)

# (a) Relation F1
ax = axes[0]
ax.plot(qlora['steps'], qlora['rel_f1'], '-o', color=C_ORANGE, markersize=4.5,
        linewidth=1.6, label='QLoRA (4-bit)', alpha=0.9, markeredgewidth=0)
ax.plot(bf16['steps'],  bf16['rel_f1'],  '-s', color=C_BLUE, markersize=4.5,
        linewidth=1.6, label='bf16', alpha=0.9, markeredgewidth=0)
ax.axhline(sft['rel_f1'], color='#999999', linestyle='--', linewidth=0.8,
           alpha=0.5, zorder=0)
t = ax.text(103, sft['rel_f1'] + 0.012, 'SFT', fontsize=8, color='#999999',
            ha='right', va='bottom')
t.set_path_effects([pe.withStroke(linewidth=2, foreground='white')])
t2 = ax.annotate('Catastrophic\ncollapse', xy=(10, 0.003), xytext=(35, 0.06),
                 fontsize=8, color=C_ORANGE, fontstyle='italic',
                 ha='center', va='bottom', linespacing=0.85,
                 arrowprops=dict(arrowstyle='->', color=C_ORANGE, lw=0.8,
                                 mutation_scale=8))
t2.set_path_effects([pe.withStroke(linewidth=2, foreground='white')])
ax.set_ylabel('Relation F1', fontsize=10)
ax.set_ylim(-0.02, 0.52)
ax.set_title('(a) Relation Extraction', fontsize=11, fontweight='bold', pad=8)
ax.grid(True, alpha=0.08, linewidth=0.3)

# (b) Evidence F1
ax = axes[1]
ax.plot(qlora['steps'], qlora['evi_f1'], '-o', color=C_ORANGE, markersize=4.5,
        linewidth=1.6, label='QLoRA (4-bit)', alpha=0.9, markeredgewidth=0)
ax.plot(bf16['steps'],  bf16['evi_f1'],  '-s', color=C_BLUE, markersize=4.5,
        linewidth=1.6, label='bf16', alpha=0.9, markeredgewidth=0)
ax.axhline(sft['evi_f1'], color='#999999', linestyle='--', linewidth=0.8,
           alpha=0.5, zorder=0)
t = ax.text(103, sft['evi_f1'] + 0.006, 'SFT', fontsize=8, color='#999999',
            ha='right', va='bottom')
t.set_path_effects([pe.withStroke(linewidth=2, foreground='white')])
ax.set_ylabel('Evidence F1', fontsize=10)
ax.set_ylim(0.38, 0.84)
ax.set_title('(b) Evidence Quality', fontsize=11, fontweight='bold', pad=8)
ax.grid(True, alpha=0.08, linewidth=0.3)

# (c) EDCR
ax = axes[2]
ax.axhspan(0.85, 1.02, color='#D55E00', alpha=0.05, zorder=0)
t = ax.text(50, 0.975, 'Near-total decoupling', fontsize=8, color='#D55E00',
            fontstyle='italic', ha='center', va='center', alpha=0.6)
t.set_path_effects([pe.withStroke(linewidth=2, foreground='white')])
ax.plot(qlora['steps'], qlora['edcr'], '-o', color=C_ORANGE, markersize=4.5,
        linewidth=1.6, label='QLoRA (4-bit)', alpha=0.9, markeredgewidth=0)
ax.plot(bf16['steps'],  bf16['edcr'],  '-s', color=C_BLUE, markersize=4.5,
        linewidth=1.6, label='bf16', alpha=0.9, markeredgewidth=0)
ax.axhline(sft['edcr'], color='#999999', linestyle='--', linewidth=0.8,
           alpha=0.5, zorder=0)
t = ax.text(103, sft['edcr'] - 0.02, 'SFT', fontsize=8, color='#999999',
            ha='right', va='top')
t.set_path_effects([pe.withStroke(linewidth=2, foreground='white')])
ax.set_ylabel('EDCR', fontsize=10)
ax.set_ylim(0.58, 1.02)
ax.set_title('(c) Evidence-Decoupling Ratio (EDCR)', fontsize=11,
             fontweight='bold', pad=8)
ax.grid(True, alpha=0.08, linewidth=0.3)

handles, labels = axes[0].get_legend_handles_labels()
fig.legend(handles, labels, loc='upper center', ncol=2, fontsize=9,
           framealpha=0.95, edgecolor='#e0e0e0', borderpad=0.4,
           bbox_to_anchor=(0.5, 1.0), columnspacing=2.0)
fig.subplots_adjust(left=0.05, right=0.98, wspace=0.30, top=0.85, bottom=0.15)
out_dir = '/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/figures/paper'
fig.savefig(f'{out_dir}/fig_grpo_dynamics.pdf', bbox_inches='tight', dpi=300)
fig.savefig(f'{out_dir}/fig_grpo_dynamics.png', bbox_inches='tight', dpi=300)
print('Saved fig_grpo_dynamics.pdf and .png')
