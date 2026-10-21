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
    'figure.dpi': 300,
    'savefig.dpi': 300,
    'savefig.bbox': 'tight',
    'savefig.pad_inches': 0.05,
    'axes.spines.top': False,
    'axes.spines.right': False,
})

# Monochromatic blue — darker = more DR reduction (better)
C_8B  = '#8BAED4'   # 浅蓝 (lower reduction)
C_70B = '#2B4C7E'   # 深蓝 (higher reduction)
C_TEXT = '#333333'
C_ARROW = '#888888'

models = ['8B\n(Qwen3-8B)', '70B\n(Llama-70B)']
dr_reduction = [24, 84]
bar_colors = [C_8B, C_70B]

fig, ax = plt.subplots(figsize=(8, 3.5))

bars = ax.bar([0, 1], dr_reduction, width=0.65, color=bar_colors,
              edgecolor='white', linewidth=0.8)

ax.axhline(y=100, color='#BBBBBB', linestyle='--', linewidth=0.8, zorder=0)
ax.text(1.65, 101, '100%', color='#AAAAAA', fontsize=8, ha='right', va='bottom')

ax.text(0, 27, '24%', ha='center', va='bottom', fontsize=12, fontweight='bold', color=C_TEXT)
ax.text(1, 87, '84%', ha='center', va='bottom', fontsize=12, fontweight='bold', color=C_TEXT)

ax.annotate('', xy=(0.62, 78), xytext=(0.38, 32),
            arrowprops=dict(arrowstyle='->', color=C_ARROW, lw=1.5))

ax.text(0.22, 58, '3.5×', fontsize=9, fontweight='bold', color='#555555',
        ha='center', va='center', rotation=0)

ax.set_xticks([0, 1])
ax.set_xticklabels(models)
ax.set_ylabel('Independent DR Reduction (%)')
ax.set_ylim(0, 115)
ax.set_xlim(-0.65, 1.65)

plt.tight_layout()

out_path = '/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/figures/fig_scale_dependency'
fig.savefig(out_path + '.pdf')
fig.savefig(out_path + '.png')
plt.close()
print('Done')
