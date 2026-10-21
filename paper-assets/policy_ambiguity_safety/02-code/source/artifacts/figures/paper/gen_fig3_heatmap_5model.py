"""Fig.3: 5-model × 6-type violation rate heatmap (ambiguous condition)."""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import os

SPEC_COLOR = '#C44E52'
LING_COLOR = '#4C72B0'

models = ['Claude', 'GPT-4.1', 'GPT-5.4', 'Qwen3-235B', 'DeepSeek-V3']
spec_types = ['auth_scope', 'incompleteness', 'cond_preced']
ling_types = ['scopal', 'lexical', 'coreferential']
all_types = spec_types + ling_types
type_labels = ['Auth.\nScope', 'Incompl.', 'Cond.\nPreced.', 'Scopal', 'Lexical', 'Corefer.']

data = np.array([
    [12, 48, 36, 32, 32, 22],   # Claude
    [46, 58, 36, 38, 34, 32],   # GPT-4.1
    [64, 46, 34, 42, 42, 18],   # GPT-5.4
    [26, 62, 40, 37, 52, 42],   # Qwen3-235B
    [60, 54, 38, 48, 54, 44],   # DeepSeek-V3
], dtype=float)

fig, ax = plt.subplots(figsize=(7, 4.5))

cmap = plt.cm.OrRd
norm = matplotlib.colors.Normalize(vmin=0, vmax=70)

im = ax.imshow(data, cmap=cmap, norm=norm, aspect='auto')

for i in range(len(models)):
    for j in range(len(all_types)):
        val = data[i, j]
        text_color = 'white' if val > 45 else 'black'
        fontweight = 'bold' if val >= 60 or val <= 18 else 'normal'
        ax.text(j, i, f'{val:.0f}%', ha='center', va='center',
                color=text_color, fontsize=11, fontweight=fontweight)

ax.set_xticks(range(len(all_types)))
ax.set_xticklabels(type_labels, fontsize=9)
ax.set_yticks(range(len(models)))
ax.set_yticklabels(models, fontsize=10)

ax.axvline(x=2.5, color='black', linewidth=1.5, linestyle='-')

ax.text(1, len(models) + 0.15, 'Specification Layer', ha='center', va='top',
        fontsize=9, color=SPEC_COLOR, fontweight='bold',
        transform=ax.transData)
ax.text(4, len(models) + 0.15, 'Linguistic Layer', ha='center', va='top',
        fontsize=9, color=LING_COLOR, fontweight='bold',
        transform=ax.transData)

for j in range(3):
    ax.add_patch(plt.Rectangle((j - 0.5, -0.5), 1, len(models),
                                fill=False, edgecolor=SPEC_COLOR,
                                linewidth=0, alpha=0.15))
for j in range(3, 6):
    ax.add_patch(plt.Rectangle((j - 0.5, -0.5), 1, len(models),
                                fill=False, edgecolor=LING_COLOR,
                                linewidth=0, alpha=0.15))

spec_bg = plt.Rectangle((-0.5, -0.5), 3, len(models),
                          fill=True, facecolor=SPEC_COLOR, alpha=0.04,
                          edgecolor='none')
ling_bg = plt.Rectangle((2.5, -0.5), 3, len(models),
                          fill=True, facecolor=LING_COLOR, alpha=0.04,
                          edgecolor='none')
ax.add_patch(spec_bg)
ax.add_patch(ling_bg)

cbar = fig.colorbar(im, ax=ax, shrink=0.8, pad=0.02)
cbar.set_label('Violation Rate (%)', fontsize=9)

ax.set_title('Model × Ambiguity Type Violation Rates\n(Ambiguous Condition, n = 2,997)',
             fontsize=11, fontweight='bold', pad=12)

ax.tick_params(top=False, bottom=True, labeltop=False, labelbottom=True)

plt.tight_layout()

outdir = os.path.dirname(os.path.abspath(__file__))
fig.savefig(os.path.join(outdir, 'fig3_heatmap_5model.pdf'), bbox_inches='tight', dpi=300)
fig.savefig(os.path.join(outdir, 'fig3_heatmap_5model.png'), bbox_inches='tight', dpi=300)
print('OK: fig3_heatmap_5model.pdf + .png saved')
