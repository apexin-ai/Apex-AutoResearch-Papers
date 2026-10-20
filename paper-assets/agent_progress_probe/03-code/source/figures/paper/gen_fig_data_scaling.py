import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams.update({
    'font.family': 'DejaVu Sans',
    'font.size': 11,
    'axes.titlesize': 13,
    'axes.labelsize': 12,
    'xtick.labelsize': 10,
    'ytick.labelsize': 10,
    'legend.fontsize': 10,
    'figure.dpi': 300,
    'savefig.dpi': 300,
    'savefig.bbox': 'tight',
    'savefig.pad_inches': 0.05,
    'axes.spines.top': False,
    'axes.spines.right': False,
})

# Data
pct = [10, 25, 50, 100]
macro_f1 = [0.8054, 0.8203, 0.8715, 0.9055]
structural_baseline = 0.9951
llm_baseline = 0.6625

fig, ax = plt.subplots(figsize=(5, 3.5))

# Shaded gap between probe@100% and structural baseline
ax.fill_between([90, 105], structural_baseline, macro_f1[-1],
                color='#0072B2', alpha=0.07, zorder=0)
ax.annotate(f'~9 pp gap',
            xy=(100, (structural_baseline + macro_f1[-1]) / 2),
            xytext=(78, 0.965),
            fontsize=8, color='#555555', style='italic',
            arrowprops=dict(arrowstyle='->', color='#999999', lw=0.8))

# Horizontal baselines
ax.axhline(structural_baseline, color='#009E73', linestyle='--', linewidth=1.5, zorder=1)
ax.text(102, structural_baseline, 'Structural (RF/GB)', fontsize=9,
        color='#009E73', va='center', ha='left')

ax.axhline(llm_baseline, color='#999999', linestyle=':', linewidth=1.2, zorder=1)
ax.text(102, llm_baseline, 'LLM-as-Judge', fontsize=9,
        color='#999999', va='center', ha='left')

# Main probe line
ax.plot(pct, macro_f1, color='#0072B2', marker='o', markersize=7,
        linewidth=2.0, zorder=3, label='NL Embedding Probe')

# Annotate each point
offsets = [(0, 8), (0, 8), (0, 8), (-12, 8)]
for i, (x, y) in enumerate(zip(pct, macro_f1)):
    ax.annotate(f'{y:.3f}', (x, y), textcoords='offset points',
                xytext=offsets[i], fontsize=8, color='#0072B2',
                ha='center', va='bottom')

# Axes
ax.set_xlabel('Training Data (%)')
ax.set_ylabel('Macro-F1')
ax.set_xticks(pct)
ax.set_xticklabels(['10', '25', '50', '100'])
ax.set_xlim(5, 130)
ax.set_ylim(0.60, 1.03)

# Grid
ax.yaxis.grid(True, alpha=0.3, linestyle='-', linewidth=0.5)
ax.set_axisbelow(True)

# Legend
ax.legend(loc='lower right', framealpha=0.9, edgecolor='none')

out_dir = '/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/figures/paper'
fig.savefig(f'{out_dir}/fig_data_scaling.pdf', format='pdf')
fig.savefig(f'{out_dir}/fig_data_scaling.png', format='png')
plt.close(fig)
print('Done')
