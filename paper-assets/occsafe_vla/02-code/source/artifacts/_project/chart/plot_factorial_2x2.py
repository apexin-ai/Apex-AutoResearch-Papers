"""
2×2 Factorial Plot: Gradient Flow × Normalization Type → CAR
Generates heatmap + interaction plot for CoRL 2026.
"""
import json
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap
from pathlib import Path

plt.rcParams.update({
    'font.family': 'serif',
    'font.serif': ['Times New Roman', 'DejaVu Serif'],
    'font.size': 9,
    'axes.labelsize': 10,
    'axes.titlesize': 11,
    'xtick.labelsize': 9,
    'ytick.labelsize': 9,
    'legend.fontsize': 8.5,
    'figure.dpi': 300,
    'savefig.dpi': 300,
    'savefig.bbox': 'tight',
    'pdf.fonttype': 42,
    'ps.fonttype': 42,
})

DATA_PATH = Path(__file__).parent / "factorial_2x2_config.json"
OUTPUT_PATH = Path(__file__).parent / "figures" / "factorial_2x2.pdf"
OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)

with open(DATA_PATH) as f:
    data = json.load(f)

cells = data["cells"]

# Extract means and stds (use None placeholder for RUNNING cells)
flow_on_bn = cells["flow_ON_BN"]
flow_on_ln = cells["flow_ON_LN"]
flow_off_bn = cells["flow_OFF_BN"]
flow_off_ln = cells["flow_OFF_LN"]

# For plotting: use available data, mark RUNNING as hatched
has_flow_on_ln = flow_on_ln["mean_CAR"] is not None

fig, axes = plt.subplots(1, 2, figsize=(7.5, 3.0), gridspec_kw={'width_ratios': [1, 1.3]})

# ═══════════════════════════════════════════════
# Panel A: Heatmap
# ═══════════════════════════════════════════════
ax = axes[0]

# Build matrix: rows = Gradient Flow [ON, OFF], cols = Norm [BN, LN]
car_matrix = np.array([
    [flow_on_bn["mean_CAR"], flow_on_ln["mean_CAR"] if has_flow_on_ln else np.nan],
    [flow_off_bn["mean_CAR"], flow_off_ln["mean_CAR"]]
])

cmap = LinearSegmentedColormap.from_list('car', ['#FDDBC7', '#F4A582', '#D6604D', '#B2182B'])
vmin, vmax = 0.72, 0.84

im = ax.imshow(car_matrix, cmap=cmap, vmin=vmin, vmax=vmax, aspect='auto')

# Annotate cells
for i in range(2):
    for j in range(2):
        val = car_matrix[i, j]
        if np.isnan(val):
            ax.text(j, i, 'RUNNING', ha='center', va='center',
                    fontsize=9, color='#333333', style='italic')
            ax.add_patch(plt.Rectangle((j - 0.5, i - 0.5), 1, 1,
                         fill=False, hatch='///', edgecolor='#999999', linewidth=0))
        else:
            cell_key = ["flow_ON_BN", "flow_ON_LN", "flow_OFF_BN", "flow_OFF_LN"][i * 2 + j]
            std = cells[cell_key]["std_CAR"]
            text = f'{val:.3f}\n±{std:.3f}' if std else f'{val:.3f}'
            ax.text(j, i, text, ha='center', va='center',
                    fontsize=9, fontweight='bold', color='white' if val > 0.77 else '#333333')

ax.set_xticks([0, 1])
ax.set_xticklabels(['BatchNorm', 'LayerNorm'])
ax.set_yticks([0, 1])
ax.set_yticklabels(['Grad Flow ON\n(Full OCC)', 'Grad Flow OFF\n(Detach)'])
ax.set_xlabel('Normalization Type')
ax.set_title('(a) CAR Heatmap', fontsize=10, pad=8)

cbar = fig.colorbar(im, ax=ax, fraction=0.046, pad=0.04)
cbar.set_label('CAR', fontsize=8)

# ═══════════════════════════════════════════════
# Panel B: Interaction Plot
# ═══════════════════════════════════════════════
ax = axes[1]

x_pos = [0, 1]  # BN, LN
labels = ['BatchNorm', 'LayerNorm']

# Gradient Flow ON line
flow_on_means = [flow_on_bn["mean_CAR"]]
flow_on_stds = [flow_on_bn["std_CAR"]]
if has_flow_on_ln:
    flow_on_means.append(flow_on_ln["mean_CAR"])
    flow_on_stds.append(flow_on_ln["std_CAR"])
else:
    flow_on_means.append(None)
    flow_on_stds.append(None)

# Gradient Flow OFF line
flow_off_means = [flow_off_bn["mean_CAR"], flow_off_ln["mean_CAR"]]
flow_off_stds = [flow_off_bn["std_CAR"], flow_off_ln["std_CAR"]]

# Plot OFF line (complete)
ax.errorbar(x_pos, flow_off_means, yerr=flow_off_stds, fmt='s-',
            color='#B2182B', linewidth=1.8, markersize=8, capsize=4,
            label='Grad Flow OFF (Detach)', zorder=5)

# Plot ON line
valid_on_x = [x for x, m in zip(x_pos, flow_on_means) if m is not None]
valid_on_m = [m for m in flow_on_means if m is not None]
valid_on_s = [s for s in flow_on_stds if s is not None]
ax.errorbar(valid_on_x, valid_on_m, yerr=valid_on_s, fmt='o-',
            color='#2166AC', linewidth=1.8, markersize=8, capsize=4,
            label='Grad Flow ON (Full OCC)', zorder=5)

if not has_flow_on_ln:
    # Dashed projection line to indicate pending result
    ax.plot([0, 1], [flow_on_bn["mean_CAR"], flow_off_ln["mean_CAR"]],
            '--', color='#2166AC', alpha=0.3, linewidth=1.2)
    ax.scatter([1], [flow_off_ln["mean_CAR"] + 0.02], marker='?',
               s=100, color='#2166AC', alpha=0.5, zorder=6)
    ax.annotate('Pending', xy=(1, 0.785), fontsize=7, ha='center',
                color='#2166AC', alpha=0.7, style='italic')

# Vanilla baseline
vanilla_car = data.get("vanilla_baseline_car", 0.780)
ax.axhline(0.780, color='#666666', linestyle=':', linewidth=1.0, alpha=0.7)
ax.text(0.98, 0.782, 'Vanilla', ha='right', fontsize=7, color='#666666', style='italic')

# Effect annotations
delta_bn = flow_on_bn["mean_CAR"] - flow_off_bn["mean_CAR"]
delta_ln = flow_off_ln["mean_CAR"] - flow_off_bn["mean_CAR"]
ax.annotate(f'Δ={delta_bn:+.3f}', xy=(0.05, (flow_on_bn["mean_CAR"] + flow_off_bn["mean_CAR"]) / 2),
            fontsize=7.5, color='#333333', ha='left')

ax.set_xticks(x_pos)
ax.set_xticklabels(labels)
ax.set_ylabel('Collision Avoidance Rate (CAR)')
ax.set_xlabel('Normalization Type')
ax.set_xlim(-0.3, 1.3)
ax.set_ylim(0.72, 0.86)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.grid(axis='y', alpha=0.3, linewidth=0.5)
ax.legend(loc='upper left', framealpha=0.9, edgecolor='#CCCCCC')
ax.set_title('(b) Interaction Plot', fontsize=10, pad=8)

plt.tight_layout(w_pad=2)
plt.savefig(OUTPUT_PATH)
plt.savefig(OUTPUT_PATH.with_suffix('.png'), dpi=300)
print(f"Saved: {OUTPUT_PATH}")
print(f"Saved: {OUTPUT_PATH.with_suffix('.png')}")
plt.close()
