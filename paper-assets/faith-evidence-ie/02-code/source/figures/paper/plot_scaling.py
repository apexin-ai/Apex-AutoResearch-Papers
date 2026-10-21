import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patheffects as pe
import numpy as np

plt.rcParams.update({
    'font.family': 'serif',
    'font.serif': ['Liberation Serif'],
    'mathtext.fontset': 'stix',
    'font.size': 10,
    'axes.labelsize': 11,
    'xtick.labelsize': 9.5,
    'ytick.labelsize': 9.5,
    'figure.dpi': 300,
    'savefig.dpi': 300,
    'savefig.bbox': 'tight',
    'savefig.pad_inches': 0.05,
    'axes.spines.top': False,
    'axes.spines.right': False,
    'axes.linewidth': 0.6,
    'pdf.fonttype': 42,
    'ps.fonttype': 42,
})

COL_EVI  = "#5B9BD5"
COL_NO   = "#B0B0B0"
COL_RSFT = "#E8A838"
COL_EVI_E  = "#497CAA"
COL_NO_E   = "#8C8C8C"
COL_RSFT_E = "#BA862D"

models = ["Qwen3-1.7B", "Qwen3-4B", "Qwen3-8B", "LLaMA-3.1-8B"]
with_evi =   [47.86, 39.74, 50.51, 53.84]
no_evi =     [39.82, 47.21, 50.79, 54.52]
rsft =       [51.19, 44.82, 54.33, 56.54]

fig, ax = plt.subplots(figsize=(6.5, 3.8), dpi=300)

x = np.arange(len(models))
width = 0.22
gap = 0.025

bars_evi  = ax.bar(x - width - gap, with_evi, width, color=COL_EVI,
                   edgecolor=COL_EVI_E, linewidth=0.4, zorder=3, alpha=0.88)
bars_no   = ax.bar(x,               no_evi,   width, color=COL_NO,
                   edgecolor=COL_NO_E, linewidth=0.4, zorder=3, alpha=0.88)
bars_rsft = ax.bar(x + width + gap, rsft,     width, color=COL_RSFT,
                   edgecolor=COL_RSFT_E, linewidth=0.4, zorder=3, alpha=0.88)

for bars, col in [(bars_evi, '#333'), (bars_no, '#333'), (bars_rsft, '#333')]:
    for bar in bars:
        h = bar.get_height()
        t = ax.text(bar.get_x() + bar.get_width() / 2, h + 0.25,
                    f"{h:.1f}", ha="center", va="bottom", fontsize=6.5,
                    color=col, fontweight='bold')
        t.set_path_effects([pe.withStroke(linewidth=1.5, foreground='white')])

d = 0.008
kwargs = dict(transform=ax.transAxes, color='black', clip_on=False, linewidth=0.6)
ax.plot((-d, +d), (-d-0.005, +d+0.005), **kwargs)
ax.plot((-d, +d), (-d+0.005, +d+0.015), **kwargs)

ax.set_ylabel("Ign-F1 (%)", fontsize=11)
ax.set_xticks(x)
ax.set_xticklabels(models, fontsize=9.5)
ax.set_ylim(35, 60)
ax.grid(axis='y', alpha=0.12, color='#999999', linestyle='-', linewidth=0.3, zorder=0)

from matplotlib.patches import Patch
handles = [
    Patch(facecolor=COL_EVI,  edgecolor=COL_EVI_E, linewidth=0.4, alpha=0.88,
          label="SFT with evidence"),
    Patch(facecolor=COL_NO,   edgecolor=COL_NO_E, linewidth=0.4, alpha=0.88,
          label="SFT without evidence"),
    Patch(facecolor=COL_RSFT, edgecolor=COL_RSFT_E, linewidth=0.4, alpha=0.88,
          label="RSFT"),
]
ax.legend(handles=handles, loc="upper left", fontsize=8, framealpha=0.95,
          edgecolor='#e0e0e0', borderpad=0.5)

fig.tight_layout()
out_dir = "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/figures/paper"
fig.savefig(f"{out_dir}/fig_scaling.pdf", bbox_inches="tight", dpi=300)
fig.savefig(f"{out_dir}/fig_scaling.png", bbox_inches="tight", dpi=300)
plt.close()
print("Saved fig_scaling.pdf and fig_scaling.png")
