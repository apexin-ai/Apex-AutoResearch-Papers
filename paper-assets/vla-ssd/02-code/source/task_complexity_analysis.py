# --- Path configuration (set env vars to override defaults) ---
import os as _os
PROJECT_ROOT = _os.environ.get("VLA_SSD_ROOT", ".")
LIBERO_ROOT = _os.environ.get("LIBERO_ROOT", "./LIBERO")
# ---
import json
import numpy as np
from scipy import stats
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Patch
import os

with open(f"{PROJECT_ROOT}/results/per_task_r2_distribution.json") as f:
    data = json.load(f)

baseline_l1 = data['mlp_probe_5demo']['conditions']['baseline']['L1']['per_task_R2']
ablated_l1 = data['mlp_probe_5demo']['conditions']['ablate_all24']['L1']['per_task_R2']

tasks = list(baseline_l1.keys())
delta_r2 = {}
for t in tasks:
    delta_r2[t] = baseline_l1[t] - ablated_l1[t]

print("=== Per-task delta_R2 (baseline - ablated) ===")
for t in sorted(delta_r2.keys(), key=lambda x: delta_r2[x]):
    print(f"  {t}: baseline={baseline_l1[t]:.4f}, ablated={ablated_l1[t]:.4f}, delta={delta_r2[t]:.4f}")

# Task grouping by instruction-dependence
# Complex: paired tasks where same object has multiple goal destinations
complex_tasks = [
    "put the bowl on the plate",
    "put the bowl on the stove",
    "put the bowl on top of the cabinet",
    "put the wine bottle on the rack",
    "put the wine bottle on top of the cabinet",
    "open the top drawer and put the bowl inside",
]

simple_tasks = [
    "open the middle drawer of the cabinet",
    "push the plate to the front of the stove",
    "put the cream cheese in the bowl",
    "turn on the stove",
]

assert set(complex_tasks + simple_tasks) == set(tasks), f"Mismatch: {set(tasks) - set(complex_tasks + simple_tasks)}"

complex_abs = [abs(delta_r2[t]) for t in complex_tasks]
simple_abs = [abs(delta_r2[t]) for t in simple_tasks]

complex_mean = np.mean(complex_abs)
complex_median = np.median(complex_abs)
simple_mean = np.mean(simple_abs)
simple_median = np.median(simple_abs)

U_stat, p_value = stats.mannwhitneyu(complex_abs, simple_abs, alternative='greater')
effect_ratio = complex_mean / simple_mean if simple_mean > 0 else float('inf')

print(f"\n=== Group Statistics (|delta_R2|) ===")
print(f"Complex (n={len(complex_tasks)}): mean={complex_mean:.4f}, median={complex_median:.4f}")
print(f"Simple  (n={len(simple_tasks)}):  mean={simple_mean:.4f}, median={simple_median:.4f}")
print(f"Mann-Whitney U = {U_stat:.1f}, p = {p_value:.4f}")
print(f"Effect ratio (complex/simple) = {effect_ratio:.2f}x")

# Build results
task_results = []
for t in tasks:
    group = "complex" if t in complex_tasks else "simple"
    task_results.append({
        "name": t,
        "baseline_r2": baseline_l1[t],
        "ablated_r2": ablated_l1[t],
        "delta_r2": round(delta_r2[t], 4),
        "abs_delta_r2": round(abs(delta_r2[t]), 4),
        "group": group
    })
task_results.sort(key=lambda x: x['abs_delta_r2'], reverse=True)

results = {
    "description": "Task complexity x routing dependence analysis. delta_R2 = baseline_R2 - ablated_R2 (L1, ablate_all24). All negative: ablation increased R2. |delta_R2| measures sensitivity to instruction routing.",
    "tasks": task_results,
    "complex_mean": round(complex_mean, 4),
    "complex_median": round(complex_median, 4),
    "simple_mean": round(simple_mean, 4),
    "simple_median": round(simple_median, 4),
    "mann_whitney_U": round(float(U_stat), 2),
    "p_value": round(float(p_value), 4),
    "effect_ratio": round(effect_ratio, 2),
    "n_complex": len(complex_tasks),
    "n_simple": len(simple_tasks)
}

with open(f"{PROJECT_ROOT}/results/task_complexity_routing.json", 'w') as f:
    json.dump(results, f, indent=2)
print("\nJSON saved to task_complexity_routing.json")

# === Visualization ===
os.makedirs(f"{PROJECT_ROOT}/results/figures", exist_ok=True)

sorted_tasks = sorted(tasks, key=lambda t: abs(delta_r2[t]), reverse=True)
short_names = {
    "open the middle drawer of the cabinet": "open middle drawer",
    "open the top drawer and put the bowl inside": "open top drawer + bowl",
    "push the plate to the front of the stove": "push plate to stove",
    "put the bowl on the plate": "bowl on plate",
    "put the bowl on the stove": "bowl on stove",
    "put the bowl on top of the cabinet": "bowl on cabinet",
    "put the cream cheese in the bowl": "cream cheese in bowl",
    "put the wine bottle on the rack": "wine on rack",
    "put the wine bottle on top of the cabinet": "wine on cabinet",
    "turn on the stove": "turn on stove",
}

fig, ax = plt.subplots(figsize=(10, 5))

colors = []
x_labels = []
y_vals = []
for t in sorted_tasks:
    y_vals.append(abs(delta_r2[t]))
    x_labels.append(short_names.get(t, t))
    if t in complex_tasks:
        colors.append('#D95F02')
    else:
        colors.append('#1B9E77')

bars = ax.bar(range(len(sorted_tasks)), y_vals, color=colors, width=0.7,
              edgecolor='white', linewidth=0.5)

legend_elements = [
    Patch(facecolor='#D95F02', label=f'Instruction-discriminative (n={len(complex_tasks)})'),
    Patch(facecolor='#1B9E77', label=f'Visually unambiguous (n={len(simple_tasks)})')
]
ax.legend(handles=legend_elements, loc='upper right', frameon=True, fontsize=9)

ax.axhline(y=complex_mean, color='#D95F02', linestyle='--', linewidth=1.2, alpha=0.7)
ax.axhline(y=simple_mean, color='#1B9E77', linestyle='--', linewidth=1.2, alpha=0.7)
ax.text(len(sorted_tasks)-0.5, complex_mean + 0.005, f'complex mean={complex_mean:.3f}',
        ha='right', va='bottom', fontsize=8, color='#D95F02')
ax.text(len(sorted_tasks)-0.5, simple_mean + 0.005, f'simple mean={simple_mean:.3f}',
        ha='right', va='bottom', fontsize=8, color='#1B9E77')

ax.set_xticks(range(len(sorted_tasks)))
ax.set_xticklabels(x_labels, rotation=35, ha='right', fontsize=8)
ax.set_ylabel(r'|$\Delta R^2$|  (ablation effect magnitude)', fontsize=10)
ax.set_title(f'L1 Instruction-Routing Ablation Effect by Task Complexity\n'
             f'Mann-Whitney U={U_stat:.0f}, p={p_value:.3f}, effect ratio={effect_ratio:.1f}x',
             fontsize=11)

ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.set_xlim(-0.5, len(sorted_tasks)-0.5)

plt.tight_layout()
plt.savefig(f"{PROJECT_ROOT}/results/figures/fig_task_complexity_routing.pdf",
            dpi=300, bbox_inches='tight')
plt.savefig(f"{PROJECT_ROOT}/results/figures/fig_task_complexity_routing.png",
            dpi=300, bbox_inches='tight')
print("Figure saved to figures/fig_task_complexity_routing.{pdf,png}")
