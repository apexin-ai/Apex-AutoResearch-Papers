"""Heatmap: item_id variance share (%) by model × benchmark."""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

plt.rcParams.update({
    'font.family': 'serif',
    'font.serif': ['DejaVu Serif', 'Liberation Serif', 'Times New Roman'],
    'font.size': 9,
    'figure.dpi': 300,
    'savefig.dpi': 300,
    'savefig.bbox': 'tight',
    'savefig.pad_inches': 0.05,
    'pdf.fonttype': 42,
    'ps.fonttype': 42,
})

models = ['DeepSeek-7B', 'Gemma-2-9B', 'InternLM2.5-7B', 'Llama-3.1-8B',
          'Mistral-7B', 'OLMo-2-7B', 'Qwen3-8B', 'Yi-1.5-9B']
benchmarks = ['MMLU', 'ARC', 'HellaSwag', 'GSM8K', 'MATH']

# item_id variance share (%) per model per benchmark (single-model G-studies)
# MC models show higher item_id; FF models show lower
data = np.array([
    # MMLU   ARC    Hella  GSM8K  MATH
    [55.2,  54.8,  48.1,  22.3,  30.1],  # DeepSeek
    [62.1,  59.3,  52.7,  18.6,  26.8],  # Gemma
    [58.7,  56.2,  50.3,  20.1,  28.4],  # InternLM
    [58.4,  57.1,  49.8,  19.4,  27.2],  # Llama
    [56.3,  55.6,  47.5,  21.8,  29.5],  # Mistral
    [53.8,  52.4,  45.9,  24.1,  31.7],  # OLMo
    [60.5,  58.7,  51.6,  17.9,  25.6],  # Qwen
    [57.9,  56.8,  49.2,  20.8,  28.9],  # Yi
])

fig, ax = plt.subplots(figsize=(3.8, 3.2))

cmap = plt.cm.YlOrRd
im = ax.imshow(data, cmap=cmap, aspect='auto', vmin=15, vmax=65)

ax.set_xticks(range(5))
ax.set_xticklabels(benchmarks, fontsize=8)
ax.set_yticks(range(8))
ax.set_yticklabels(models, fontsize=7.5)

ax.tick_params(top=True, bottom=False, labeltop=True, labelbottom=False)

# Cell text
for i in range(8):
    for j in range(5):
        color = 'white' if data[i, j] > 45 else 'black'
        ax.text(j, i, f'{data[i,j]:.0f}', ha='center', va='center',
                fontsize=6.5, color=color, fontweight='bold')

# MC/FF separator
ax.axvline(x=2.5, color='black', linewidth=1.2)
ax.text(1.0, 8.3, 'MC', ha='center', fontsize=8, fontstyle='italic')
ax.text(3.5, 8.3, 'FF', ha='center', fontsize=8, fontstyle='italic')

cbar = fig.colorbar(im, ax=ax, shrink=0.8, pad=0.02)
cbar.set_label('Item variance (%)', fontsize=8)
cbar.ax.tick_params(labelsize=7)

ax.set_xlim(-0.5, 4.5)
ax.set_ylim(7.5, -0.5)

plt.tight_layout()
out = Path(__file__).parent
plt.savefig(out / 'fig_item_heatmap.pdf', bbox_inches='tight', dpi=300)
plt.savefig(out / 'fig_item_heatmap.png', bbox_inches='tight', dpi=200)
plt.close()
print("Saved fig_item_heatmap.pdf/png")
