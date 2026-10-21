import json
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from pathlib import Path

OUT = Path(__file__).parent

with open(OUT.parent / "power_simulation" / "power_artifact_test.json") as f:
    data = json.load(f)

alphas = [0.45, 0.50, 0.60, 0.75, 1.0]
Ts = [5, 10, 15, 20, 25]

observed = {
    (5, 0.45): 0.0, (5, 0.50): 0.0, (5, 0.60): 0.0, (5, 0.75): 0.0, (5, 1.0): 0.0,
    (10, 0.45): 0.0, (10, 0.50): 0.750, (10, 0.60): 0.0, (10, 0.75): 0.750, (10, 1.0): 0.750,
    (15, 0.45): 0.750, (15, 0.50): 0.750, (15, 0.60): 0.0, (15, 0.75): 0.750, (15, 1.0): 0.750,
    (20, 0.45): 0.625, (20, 0.50): 0.750, (20, 0.60): 0.0, (20, 0.75): 0.750, (20, 1.0): 0.750,
    (25, 0.45): 0.750, (25, 0.50): 0.750, (25, 0.60): 0.625, (25, 0.75): 0.750, (25, 1.0): 0.750,
}

def get_det_frac(results, alpha, T):
    a_str = f"{alpha:.2f}" if alpha < 1.0 else "1.00"
    key = f"a{a_str}_T{T}"
    return results[key]["mean_detection_fraction"]

table = {"alphas": alphas, "T_values": Ts, "observed": {}, "H0_linear": {}, "H0_concave": {}, "H1_step": {}}

for T in Ts:
    t_key = str(T)
    table["observed"][t_key] = {}
    table["H0_linear"][t_key] = {}
    table["H0_concave"][t_key] = {}
    table["H1_step"][t_key] = {}
    for a in alphas:
        a_key = str(a)
        table["observed"][t_key][a_key] = observed[(T, a)]
        table["H0_linear"][t_key][a_key] = get_det_frac(data["H0_results"], a, T)
        table["H0_concave"][t_key][a_key] = get_det_frac(data["H0_concave_results"], a, T)
        table["H1_step"][t_key][a_key] = get_det_frac(data["H1_results"], a, T)

obs_flat = []
h0_flat = []
h0c_flat = []
h1_flat = []
for T in Ts:
    for a in alphas:
        obs_flat.append(observed[(T, a)])
        h0_flat.append(get_det_frac(data["H0_results"], a, T))
        h0c_flat.append(get_det_frac(data["H0_concave_results"], a, T))
        h1_flat.append(get_det_frac(data["H1_results"], a, T))

obs_arr = np.array(obs_flat)
rmse_h0 = np.sqrt(np.mean((np.array(h0_flat) - obs_arr)**2))
rmse_h0c = np.sqrt(np.mean((np.array(h0c_flat) - obs_arr)**2))
rmse_h1 = np.sqrt(np.mean((np.array(h1_flat) - obs_arr)**2))

table["RMSE"] = {"H0_linear": round(rmse_h0, 4), "H0_concave": round(rmse_h0c, 4), "H1_step": round(rmse_h1, 4)}

intermediate_h0 = sum(1 for v in h0_flat if 0.1 < v < 0.7)
intermediate_h0c = sum(1 for v in h0c_flat if 0.1 < v < 0.7)
intermediate_h1 = sum(1 for v in h1_flat if 0.1 < v < 0.7)
intermediate_obs = sum(1 for v in obs_flat if 0.1 < v < 0.7)

table["intermediate_cells"] = {
    "H0_linear": intermediate_h0,
    "H0_concave": intermediate_h0c,
    "H1_step": intermediate_h1,
    "observed": intermediate_obs,
    "note": "count of cells with detection_fraction in (0.1, 0.7) — intermediate regime"
}

with open(OUT / "shape_comparison_table.json", "w") as f:
    json.dump(table, f, indent=2)

# --- 4-panel figure ---
# Okabe-Ito palette
OI_BLUE = "#0072B2"
OI_ORANGE = "#E69F00"
OI_GREEN = "#009E73"
OI_BLACK = "#000000"

fig, axes = plt.subplots(1, 4, figsize=(14, 3.2), sharey=True)
plot_Ts = [10, 15, 20, 25]

for idx, T in enumerate(plot_Ts):
    ax = axes[idx]
    h0_vals = [get_det_frac(data["H0_results"], a, T) for a in alphas]
    h0c_vals = [get_det_frac(data["H0_concave_results"], a, T) for a in alphas]
    h1_vals = [get_det_frac(data["H1_results"], a, T) for a in alphas]
    obs_vals = [observed[(T, a)] for a in alphas]

    ax.plot(alphas, h0_vals, '--', color=OI_BLUE, linewidth=1.5, label='$H_0$: linear', zorder=3)
    ax.plot(alphas, h0c_vals, ':', color=OI_ORANGE, linewidth=1.8, label="$H_0'$: concave", zorder=3)
    ax.plot(alphas, h1_vals, '-', color=OI_GREEN, linewidth=1.5, label='$H_1$: step', zorder=3)
    ax.scatter(alphas, obs_vals, color=OI_BLACK, s=40, zorder=5, label='Observed')

    ax.axhline(y=0.75, color='grey', linewidth=0.5, linestyle='-', alpha=0.4)

    ax.set_title(f'$T = {T}$', fontsize=11)
    ax.set_xlabel(r'$\alpha$', fontsize=10)
    ax.set_xlim(0.4, 1.05)
    ax.set_ylim(-0.05, 1.05)
    ax.set_xticks([0.45, 0.60, 0.75, 1.0])
    ax.set_xticklabels(['0.45', '0.60', '0.75', '1.0'], fontsize=8)
    if idx == 0:
        ax.set_ylabel('Detection fraction', fontsize=10)
    ax.tick_params(axis='both', labelsize=8)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

handles, labels = axes[0].get_legend_handles_labels()
fig.legend(handles, labels, loc='upper center', ncol=4, fontsize=9, frameon=False,
           bbox_to_anchor=(0.5, 1.02))

fig.tight_layout(rect=[0, 0, 1, 0.90])
fig.savefig(OUT / "shape_comparison_figure.pdf", dpi=300, bbox_inches='tight')
fig.savefig(OUT / "shape_comparison_figure.png", dpi=300, bbox_inches='tight')
plt.close()

print(f"RMSE — H0: {rmse_h0:.4f}, H0': {rmse_h0c:.4f}, H1: {rmse_h1:.4f}")
print(f"Intermediate cells — H0: {intermediate_h0}, H0': {intermediate_h0c}, H1: {intermediate_h1}, Obs: {intermediate_obs}")
print("Done.")
