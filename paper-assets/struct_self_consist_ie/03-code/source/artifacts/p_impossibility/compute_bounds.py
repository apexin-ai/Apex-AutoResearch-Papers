"""
Compute degeneracy upper bound vs actual SC gain for all configs.
Produces: bound_verification.json, bound_plot.png
"""
import json
import os

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

OUT_DIR = os.path.dirname(os.path.abspath(__file__))

# --- Data from routing_results.json (16 configs) ---
configs = [
    {"id": "Qwen3-8B/FT/SciERC/s456", "dataset": "SciERC", "model": "Qwen3-8B", "regime": "FT",
     "D": 0.1928, "greedy_f1": 0.6453, "oracle_f1": 0.7726, "best_delta_pp": 0.40},
    {"id": "Qwen3-8B/FT/SciERC/s789", "dataset": "SciERC", "model": "Qwen3-8B", "regime": "FT",
     "D": 0.2136, "greedy_f1": 0.6428, "oracle_f1": 0.7767, "best_delta_pp": 1.12},
    {"id": "Qwen3-8B/FT/CoNLL/s123", "dataset": "CoNLL", "model": "Qwen3-8B", "regime": "FT",
     "D": 0.6295, "greedy_f1": 0.9074, "oracle_f1": 0.9477, "best_delta_pp": -0.42},
    {"id": "Qwen3-8B/FT/CoNLL/s456", "dataset": "CoNLL", "model": "Qwen3-8B", "regime": "FT",
     "D": 0.6303, "greedy_f1": 0.9076, "oracle_f1": 0.9443, "best_delta_pp": -0.42},
    {"id": "Qwen3-8B/FT/FewNERD/s123", "dataset": "FewNERD", "model": "Qwen3-8B", "regime": "FT",
     "D": 0.1307, "greedy_f1": 0.7482, "oracle_f1": 0.8771, "best_delta_pp": 1.56},
    {"id": "Qwen3-8B/FT/FewNERD/s456", "dataset": "FewNERD", "model": "Qwen3-8B", "regime": "FT",
     "D": 0.1200, "greedy_f1": 0.7483, "oracle_f1": 0.8755, "best_delta_pp": 1.37},
    {"id": "Qwen3-8B/FT/FewNERD/s789", "dataset": "FewNERD", "model": "Qwen3-8B", "regime": "FT",
     "D": 0.1177, "greedy_f1": 0.7483, "oracle_f1": 0.8716, "best_delta_pp": 1.35},
    {"id": "Qwen2.5-72B/ZS/SciERC", "dataset": "SciERC", "model": "Qwen2.5-72B", "regime": "ZS",
     "D": 0.2098, "greedy_f1": 0.3993, "oracle_f1": 0.5489, "best_delta_pp": 1.53},
    {"id": "Qwen2.5-72B/ZS/CoNLL", "dataset": "CoNLL", "model": "Qwen2.5-72B", "regime": "ZS",
     "D": 0.6771, "greedy_f1": 0.7120, "oracle_f1": 0.7651, "best_delta_pp": -0.37},
    {"id": "Qwen2.5-72B/ZS/FewNERD", "dataset": "FewNERD", "model": "Qwen2.5-72B", "regime": "ZS",
     "D": 0.4622, "greedy_f1": 0.6281, "oracle_f1": 0.7072, "best_delta_pp": -0.19},
    {"id": "Qwen2.5-72B/FS/SciERC", "dataset": "SciERC", "model": "Qwen2.5-72B", "regime": "FS",
     "D": 0.1664, "greedy_f1": 0.4615, "oracle_f1": 0.6044, "best_delta_pp": -0.08},
    {"id": "Qwen2.5-72B/FS/CoNLL", "dataset": "CoNLL", "model": "Qwen2.5-72B", "regime": "FS",
     "D": 0.7003, "greedy_f1": 0.7450, "oracle_f1": 0.7958, "best_delta_pp": 0.24},
    {"id": "Qwen2.5-72B/FS/FewNERD", "dataset": "FewNERD", "model": "Qwen2.5-72B", "regime": "FS",
     "D": 0.4520, "greedy_f1": 0.6189, "oracle_f1": 0.7017, "best_delta_pp": 0.06},
    {"id": "Qwen2.5-7B/FT/FewNERD/s42", "dataset": "FewNERD", "model": "Qwen2.5-7B", "regime": "FT",
     "D": 0.3109, "greedy_f1": 0.7851, "oracle_f1": 0.8718, "best_delta_pp": 0.39},
    {"id": "Qwen2.5-7B/FT/FewNERD/s123", "dataset": "FewNERD", "model": "Qwen2.5-7B", "regime": "FT",
     "D": 0.3276, "greedy_f1": 0.7850, "oracle_f1": 0.8777, "best_delta_pp": 0.38},
    {"id": "Qwen2.5-7B/FT/FewNERD/s456", "dataset": "FewNERD", "model": "Qwen2.5-7B", "regime": "FT",
     "D": 0.3129, "greedy_f1": 0.7825, "oracle_f1": 0.8771, "best_delta_pp": 0.52},
]

# --- Compute bounds ---
results = []
for c in configs:
    oracle_gap_all = (c["oracle_f1"] - c["greedy_f1"]) * 100  # pp
    G_nd = oracle_gap_all / (1 - c["D"]) if c["D"] < 1.0 else float('inf')  # pp
    weak_bound = (1 - c["D"]) * G_nd  # = oracle_gap_all, by definition
    actual = c["best_delta_pp"]
    # alpha: signal alignment (actual / weak_bound), capped at [0, 1]
    alpha = max(0.0, actual / weak_bound) if weak_bound > 0 else 0.0
    alpha = min(alpha, 1.0)

    results.append({
        "config": c["id"],
        "dataset": c["dataset"],
        "model": c["model"],
        "regime": c["regime"],
        "D": round(c["D"], 4),
        "greedy_f1": c["greedy_f1"],
        "oracle_f1": c["oracle_f1"],
        "oracle_gap_all_pp": round(oracle_gap_all, 2),
        "G_nd_pp": round(G_nd, 2),
        "weak_bound_pp": round(weak_bound, 2),
        "actual_best_delta_pp": actual,
        "alpha_empirical": round(alpha, 4),
        "bound_ratio": round(actual / weak_bound, 4) if weak_bound > 0 else None,
    })

# --- Aggregate statistics ---
alphas = [r["alpha_empirical"] for r in results if r["actual_best_delta_pp"] > 0]
mean_alpha = np.mean(alphas) if alphas else 0
median_alpha = np.median(alphas) if alphas else 0

# Compute theta_critical for various alpha values
epsilon = 0.3  # 0.3pp significance threshold
G_nd_values = [r["G_nd_pp"] for r in results]
mean_G_nd = np.mean(G_nd_values)

theta_crit_scenarios = {}
for alpha_val in [0.05, 0.08, 0.10, 0.15, mean_alpha]:
    label = f"alpha={alpha_val:.3f}" if alpha_val != mean_alpha else f"alpha={alpha_val:.3f} (empirical mean)"
    if mean_G_nd * alpha_val > 0:
        theta_crit_scenarios[label] = round(1 - epsilon / (mean_G_nd * alpha_val), 4)

# Bound tightness: for configs with positive gain
positive_configs = [r for r in results if r["actual_best_delta_pp"] > 0]
if positive_configs:
    ratios_pos = [r["bound_ratio"] for r in positive_configs]
    mean_ratio_pos = np.mean(ratios_pos)
    closest_to_bound = max(positive_configs, key=lambda r: r["bound_ratio"])
else:
    mean_ratio_pos = 0
    closest_to_bound = None

output = {
    "experiment": "P_impossibility_bound_verification",
    "epsilon_pp": epsilon,
    "N": 8,
    "per_config": results,
    "aggregate": {
        "mean_G_nd_pp": round(mean_G_nd, 2),
        "mean_alpha_positive_configs": round(mean_alpha, 4),
        "median_alpha_positive_configs": round(median_alpha, 4),
        "mean_bound_ratio_positive_configs": round(mean_ratio_pos, 4),
        "closest_to_bound": closest_to_bound["config"] if closest_to_bound else None,
        "closest_to_bound_ratio": closest_to_bound["bound_ratio"] if closest_to_bound else None,
        "theta_critical_scenarios": theta_crit_scenarios,
        "n_configs_all_negative": sum(1 for r in results if r["actual_best_delta_pp"] <= 0),
        "n_configs_positive": len(positive_configs),
    },
}

with open(os.path.join(OUT_DIR, "bound_verification.json"), "w") as f:
    json.dump(output, f, indent=2)

print("Saved bound_verification.json")

# --- Visualization ---
fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# Color map by dataset
ds_colors = {"SciERC": "#e74c3c", "CoNLL": "#3498db", "FewNERD": "#2ecc71"}
ds_markers = {"SciERC": "o", "CoNLL": "s", "FewNERD": "D"}

# Panel 1: D vs actual gain with bound curve
ax1 = axes[0]
for r in results:
    ax1.scatter(r["D"], r["actual_best_delta_pp"],
                c=ds_colors[r["dataset"]], marker=ds_markers[r["dataset"]],
                s=70, zorder=5, edgecolors='k', linewidths=0.5)

# Upper bound curve: (1-D) * G_nd * alpha_mean
D_range = np.linspace(0, 0.95, 200)
# Use median G_nd and mean alpha for the bound curve
bound_curve_alpha1 = (1 - D_range) * mean_G_nd
bound_curve_alpha_emp = (1 - D_range) * mean_G_nd * mean_alpha
ax1.plot(D_range, bound_curve_alpha1, 'k--', linewidth=1.5, label=f'Weak bound ($\\alpha=1$, $G_{{nd}}$={mean_G_nd:.1f}pp)')
ax1.plot(D_range, bound_curve_alpha_emp, 'r-', linewidth=2,
         label=f'Signal-adj. ($\\alpha$={mean_alpha:.3f})')

# Significance threshold
ax1.axhline(y=epsilon, color='gray', linestyle=':', linewidth=1, label=f'$\\varepsilon$={epsilon}pp')
ax1.axhline(y=0, color='gray', linestyle='-', linewidth=0.5, alpha=0.5)

# theta_critical vertical line
theta_crit_emp = 1 - epsilon / (mean_G_nd * mean_alpha) if mean_G_nd * mean_alpha > 0 else 1.0
if 0 < theta_crit_emp < 1:
    ax1.axvline(x=theta_crit_emp, color='red', linestyle=':', linewidth=1.5, alpha=0.7,
                label=f'$\\theta_{{crit}}$={theta_crit_emp:.2f}')

# Legend entries for datasets
for ds in ["SciERC", "CoNLL", "FewNERD"]:
    ax1.scatter([], [], c=ds_colors[ds], marker=ds_markers[ds], s=70,
                edgecolors='k', linewidths=0.5, label=ds)

ax1.set_xlabel("Degeneracy Rate $D$", fontsize=12)
ax1.set_ylabel("SC Gain (pp)", fontsize=12)
ax1.set_title("Degeneracy vs SC Gain with Upper Bound", fontsize=13)
ax1.legend(fontsize=8, loc='upper right')
ax1.set_xlim(-0.02, 0.82)
ax1.set_ylim(-1.5, max(r["actual_best_delta_pp"] for r in results) + 1)

# Panel 2: Bound ratio (actual/bound) vs D
ax2 = axes[1]
for r in results:
    ratio = r["bound_ratio"] if r["bound_ratio"] is not None else 0
    ax2.scatter(r["D"], ratio,
                c=ds_colors[r["dataset"]], marker=ds_markers[r["dataset"]],
                s=70, zorder=5, edgecolors='k', linewidths=0.5)

ax2.axhline(y=0, color='gray', linestyle='-', linewidth=0.5, alpha=0.5)
ax2.axhline(y=1, color='k', linestyle='--', linewidth=1, alpha=0.3, label='Bound = Actual ($\\alpha=1$)')

for ds in ["SciERC", "CoNLL", "FewNERD"]:
    ax2.scatter([], [], c=ds_colors[ds], marker=ds_markers[ds], s=70,
                edgecolors='k', linewidths=0.5, label=ds)

ax2.set_xlabel("Degeneracy Rate $D$", fontsize=12)
ax2.set_ylabel("Bound Ratio (actual / weak bound)", fontsize=12)
ax2.set_title("Bound Tightness", fontsize=13)
ax2.legend(fontsize=9, loc='lower left')
ax2.set_xlim(-0.02, 0.82)

plt.tight_layout()
plt.savefig(os.path.join(OUT_DIR, "bound_plot.png"), dpi=150, bbox_inches='tight')
print("Saved bound_plot.png")

# --- Print summary table ---
print("\n" + "="*100)
print(f"{'Config':<35s} {'D':>6s} {'Oracle Gap':>10s} {'G_nd':>8s} {'Bound':>8s} {'Actual':>8s} {'alpha':>8s} {'Ratio':>8s}")
print("="*100)
for r in results:
    print(f"{r['config']:<35s} {r['D']:>6.3f} {r['oracle_gap_all_pp']:>9.2f}pp {r['G_nd_pp']:>7.2f}pp "
          f"{r['weak_bound_pp']:>7.2f}pp {r['actual_best_delta_pp']:>7.2f}pp "
          f"{r['alpha_empirical']:>7.4f} {r['bound_ratio']:>8.4f}")
print("="*100)
print(f"\nMean G_nd: {mean_G_nd:.2f}pp")
print(f"Mean alpha (positive configs): {mean_alpha:.4f}")
print(f"Mean bound ratio (positive configs): {mean_ratio_pos:.4f}")
print(f"\nTheta_critical scenarios (epsilon={epsilon}pp, mean G_nd={mean_G_nd:.1f}pp):")
for label, val in theta_crit_scenarios.items():
    print(f"  {label}: theta_crit = {val:.4f}")
