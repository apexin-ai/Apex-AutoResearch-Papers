"""
Dose-Response Curve: OCC Gradient Flow Duration → Collision Avoidance Rate (CAR)
Generates publication-quality PDF figure for CoRL 2026.
"""
import json
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from pathlib import Path

plt.rcParams.update({
    'font.family': 'serif',
    'font.serif': ['Times New Roman', 'DejaVu Serif'],
    'font.size': 9,
    'axes.labelsize': 10,
    'axes.titlesize': 11,
    'xtick.labelsize': 8,
    'ytick.labelsize': 8,
    'legend.fontsize': 8,
    'figure.dpi': 300,
    'savefig.dpi': 300,
    'savefig.bbox': 'tight',
    'pdf.fonttype': 42,
    'ps.fonttype': 42,
})

DATA_PATH = Path(__file__).parent / "dose_response_data.json"
OUTPUT_PATH = Path(__file__).parent / "figures" / "dose_response_curve.pdf"
OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)

with open(DATA_PATH) as f:
    data = json.load(f)

# Extract forward-cutoff conditions (monotonic x-axis)
forward_conditions = []
for cond in data["conditions"]:
    if cond["condition"] == "reverse_cutoff":
        continue
    cars = [v["CAR"] for v in cond["seeds"].values() if v["CAR"] is not None]
    forward_conditions.append({
        "name": cond["condition"],
        "x": cond["gradient_flow_steps"],
        "cars": cars,
        "mean": np.mean(cars),
        "std": np.std(cars) if len(cars) > 1 else 0,
        "n": len(cars),
    })

forward_conditions.sort(key=lambda c: c["x"])

# Reverse cutoff (separate marker)
rc = next(c for c in data["conditions"] if c["condition"] == "reverse_cutoff")
rc_cars = [v["CAR"] for v in rc["seeds"].values() if v["CAR"] is not None]
rc_mean = np.mean(rc_cars)
rc_std = np.std(rc_cars) if len(rc_cars) > 1 else 0

# Vanilla baseline
vanilla_mean = data["vanilla_baseline"]["mean_CAR"]
vanilla_std = data["vanilla_baseline"]["std_CAR"]

# Plot
fig, ax = plt.subplots(1, 1, figsize=(4.5, 3.2))

xs = [c["x"] / 1000 for c in forward_conditions]
means = [c["mean"] for c in forward_conditions]
stds = [c["std"] for c in forward_conditions]
ns = [c["n"] for c in forward_conditions]

# Main curve with error band
ax.plot(xs, means, 'o-', color='#2166AC', linewidth=1.8, markersize=6, zorder=5)
ax.fill_between(xs, [m - s for m, s in zip(means, stds)],
                [m + s for m, s in zip(means, stds)],
                alpha=0.2, color='#2166AC', zorder=2)

# Individual seed points
for cond in forward_conditions:
    x = cond["x"] / 1000
    for car in cond["cars"]:
        ax.scatter(x, car, color='#2166AC', alpha=0.3, s=20, zorder=4, edgecolors='none')

# Annotate seed counts
for i, c in enumerate(forward_conditions):
    if c["n"] < 3:
        ax.annotate(f'n={c["n"]}', (xs[i], means[i] + stds[i] + 0.008),
                    ha='center', fontsize=6.5, color='#666666')

# Reverse cutoff (diamond marker at x=15K with offset for clarity)
rc_x = 15 + 1.5  # slight offset to avoid overlap with cutoff_15k
ax.errorbar(rc_x, rc_mean, yerr=rc_std, fmt='D', color='#B2182B', markersize=7,
            capsize=3, linewidth=1.5, zorder=6, label='Reverse cutoff (late 35K–50K)')
for car in rc_cars:
    ax.scatter(rc_x, car, color='#B2182B', alpha=0.3, s=20, zorder=4, edgecolors='none')

# Vanilla baseline
ax.axhline(vanilla_mean, color='#666666', linestyle='--', linewidth=1.0, zorder=1)
ax.fill_between([0, 52], vanilla_mean - vanilla_std, vanilla_mean + vanilla_std,
                alpha=0.08, color='#666666', zorder=0)
ax.text(51, vanilla_mean + 0.005, 'Vanilla', ha='right', va='bottom',
        fontsize=7.5, color='#666666', style='italic')

# Arrow annotation: early > late
ax.annotate('', xy=(15, 0.804), xytext=(rc_x, rc_mean),
            arrowprops=dict(arrowstyle='->', color='#B2182B', lw=1.2,
                            connectionstyle='arc3,rad=-0.2'))
ax.text(18, 0.755, 'Early > Late\n(same duration)', fontsize=7,
        ha='center', color='#B2182B', style='italic')

# Formatting
ax.set_xlabel('Gradient Flow Duration (K steps)')
ax.set_ylabel('Collision Avoidance Rate (CAR)')
ax.set_xlim(-1, 53)
ax.set_ylim(0.65, 0.87)
ax.set_xticks([0, 15, 25, 35, 45, 50])
ax.set_xticklabels(['0\n(Detach)', '15K', '25K', '35K', '45K', '50K\n(Full)'])
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.grid(axis='y', alpha=0.3, linewidth=0.5)

# Legend
forward_patch = mpatches.Patch(color='#2166AC', alpha=0.6, label='Forward cutoff (early → off)')
reverse_marker = plt.Line2D([0], [0], marker='D', color='w', markerfacecolor='#B2182B',
                            markersize=7, label='Reverse cutoff (off → late)')
vanilla_line = plt.Line2D([0], [0], linestyle='--', color='#666666', label='Vanilla baseline')
ax.legend(handles=[forward_patch, reverse_marker, vanilla_line],
          loc='lower right', framealpha=0.9, edgecolor='#CCCCCC')

plt.tight_layout()
plt.savefig(OUTPUT_PATH)
plt.savefig(OUTPUT_PATH.with_suffix('.png'), dpi=300)
print(f"Saved: {OUTPUT_PATH}")
print(f"Saved: {OUTPUT_PATH.with_suffix('.png')}")
plt.close()
