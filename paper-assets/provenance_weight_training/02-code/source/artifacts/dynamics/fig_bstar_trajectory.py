import json
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

C = {
    'baseline':  '#4A90D9',   # steel blue — Adaptive b* / primary data / ours
    'treatment': '#E8913A',   # warm amber — ESS-only / contrast methods
    'collapse':  '#C75C5C',   # muted coral — Random / degradation / failure
    'safe':      '#43A888',   # sage green — Grid-best / Oracle / D&R / good outcome
    'neutral':   '#90A4AE',   # blue-gray — Uniform baseline / reference
}

# ── Premium rcParams (publication-grade, PaperBanana-equivalent) ──
plt.rcParams.update({
    'font.family': 'serif',
    'font.serif': ['Liberation Serif', 'DejaVu Serif'],
    'mathtext.fontset': 'dejavuserif',
    'font.size': 8.5,
    'axes.titlesize': 9.5,
    'axes.labelsize': 9,
    'xtick.labelsize': 7.5,
    'ytick.labelsize': 7.5,
    'legend.fontsize': 7,
    'axes.linewidth': 0.6,
    'axes.spines.top': False,
    'axes.spines.right': False,
    'axes.axisbelow': True,
    'xtick.major.width': 0.5,  'ytick.major.width': 0.5,
    'xtick.minor.width': 0.3,  'ytick.minor.width': 0.3,
    'xtick.major.size': 3.5,   'ytick.major.size': 3.5,
    'xtick.minor.size': 2.0,   'ytick.minor.size': 2.0,
    'xtick.direction': 'out',  'ytick.direction': 'out',
    'xtick.major.pad': 4,      'ytick.major.pad': 4,
    'lines.linewidth': 1.5,
    'lines.markersize': 5,
    'legend.frameon': False,
    'legend.borderpad': 0.3,
    'legend.handlelength': 1.5,
    'legend.handletextpad': 0.5,
    'grid.linewidth': 0.3,
    'grid.alpha': 0.4,
    'grid.linestyle': '--',
    'grid.color': '#E0E0E0',
    'figure.dpi': 300,
    'figure.facecolor': 'white',
    'axes.facecolor': 'white',
    'savefig.dpi': 300,
    'savefig.bbox': 'tight',
    'savefig.pad_inches': 0.04,
    'savefig.facecolor': 'white',
    'pdf.fonttype': 42,
    'ps.fonttype': 42,
})

data_path = Path(__file__).parent / "training_dynamics_data.json"
with open(data_path) as f:
    data = json.load(f)

center = np.array(data["bstar"]["center"])
mean = np.array(data["bstar"]["mean"])
median = np.array(data["bstar"]["median"])
p25 = np.array(data["bstar"]["p25"])
p75 = np.array(data["bstar"]["p75"])

fig, ax = plt.subplots(figsize=(5.5, 3.2))

ax.fill_between(center, p25, p75, color=C['baseline'], alpha=0.12, label="P25–P75")
ax.plot(center, median, color=C['baseline'], linewidth=1.5, label="Median")
ax.plot(center, mean, color=C['baseline'], linewidth=1.0, linestyle="--", alpha=0.7, label="Mean")

ax.set_xlabel("Training Step")
ax.set_ylabel("$b^*$")
ax.legend(loc="upper right", edgecolor='none')
ax.set_xlim(0, center[-1])
ax.set_ylim(0, 2.0)
ax.grid(axis='y', lw=0.3, alpha=0.4, color='#E0E0E0', linestyle='--')

out_dir = Path(__file__).parent
fig.savefig(out_dir / "fig_bstar_trajectory.pdf", dpi=300, bbox_inches='tight')
fig.savefig(out_dir / "fig_bstar_trajectory.png", dpi=300, bbox_inches='tight')
plt.close()
print(f"Saved to {out_dir / 'fig_bstar_trajectory.pdf'}")
