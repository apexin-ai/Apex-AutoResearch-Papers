#!/usr/bin/env python3
"""Compute MI lower bounds between token_entropy and diversity metrics across alpha sweep."""

import json
import numpy as np
from collections import defaultdict
import warnings
warnings.filterwarnings('ignore')

DATA_PATH = "/tmp/mi_all_data.json"
OUT_JSON = "/tmp/mi_lower_bounds.json"
OUT_FIG_PDF = "/tmp/fig_mi_vs_alpha.pdf"
OUT_FIG_PNG = "/tmp/fig_mi_vs_alpha.png"

DIVERSITY_METRICS = ["distinct_1", "distinct_2", "distinct_3", "mauve"]
N_BOOTSTRAP = 2000
SEED = 42

def mi_gaussian_lb(x, y):
    """MI lower bound via Gaussian assumption: -0.5 * log(1 - r^2)."""
    if len(x) < 4:
        return np.nan
    r = np.corrcoef(x, y)[0, 1]
    if np.isnan(r) or abs(r) > 0.9999:
        return np.nan
    return -0.5 * np.log(1 - r**2) / np.log(2)  # bits

def mi_ksg(x, y, k=3):
    """KSG MI estimator via sklearn."""
    try:
        from sklearn.feature_selection import mutual_info_regression
        mi = mutual_info_regression(
            x.reshape(-1, 1), y, n_neighbors=min(k, len(x) - 1), random_state=SEED
        )
        return float(mi[0]) / np.log(2)  # nats -> bits
    except Exception:
        return np.nan

def bootstrap_mi(x, y, func, n_boot=N_BOOTSTRAP):
    """Bootstrap CI for MI estimate."""
    rng = np.random.RandomState(SEED)
    n = len(x)
    vals = []
    for _ in range(n_boot):
        idx = rng.choice(n, size=n, replace=True)
        v = func(x[idx], y[idx])
        if not np.isnan(v):
            vals.append(v)
    if len(vals) < 100:
        return np.nan, np.nan
    return np.percentile(vals, 2.5), np.percentile(vals, 97.5)

# Load data
with open(DATA_PATH) as f:
    all_data = json.load(f)

# Organize by alpha
alpha_seeds = defaultdict(list)
for exp_name, info in all_data.items():
    alpha = info["alpha"]
    metrics_list = info["metrics"]
    entropy = np.array([m["token_entropy"] for m in metrics_list])
    div_data = {}
    for dm in DIVERSITY_METRICS:
        div_data[dm] = np.array([m[dm] for m in metrics_list])
    alpha_seeds[alpha].append({
        "seed": info["seed"],
        "exp": exp_name,
        "entropy": entropy,
        "diversity": div_data,
        "T": len(metrics_list),
    })

alphas_sorted = sorted(alpha_seeds.keys())

# Compute MI for each alpha x seed x metric
results = {}
for alpha in alphas_sorted:
    alpha_key = f"{alpha:.2f}"
    results[alpha_key] = {"alpha": alpha, "seeds": {}, "aggregate": {}}

    all_mi_gauss = defaultdict(list)
    all_mi_ksg_vals = defaultdict(list)

    for seed_data in alpha_seeds[alpha]:
        seed_key = str(seed_data["seed"])
        ent = seed_data["entropy"]
        T = seed_data["T"]
        seed_result = {"exp": seed_data["exp"], "T": T, "metrics": {}}

        for dm in DIVERSITY_METRICS:
            div = seed_data["diversity"][dm]
            mi_g = mi_gaussian_lb(ent, div)
            mi_k = mi_ksg(ent, div)

            ci_lo, ci_hi = bootstrap_mi(ent, div, mi_gaussian_lb)

            r_val = np.corrcoef(ent, div)[0, 1] if len(ent) >= 4 else np.nan

            seed_result["metrics"][dm] = {
                "mi_gaussian_bits": round(mi_g, 6) if not np.isnan(mi_g) else None,
                "mi_ksg_bits": round(mi_k, 6) if not np.isnan(mi_k) else None,
                "pearson_r": round(float(r_val), 6) if not np.isnan(r_val) else None,
                "bootstrap_ci_95": [round(ci_lo, 6) if not np.isnan(ci_lo) else None,
                                     round(ci_hi, 6) if not np.isnan(ci_hi) else None],
            }

            if not np.isnan(mi_g):
                all_mi_gauss[dm].append(mi_g)
            if not np.isnan(mi_k):
                all_mi_ksg_vals[dm].append(mi_k)

        results[alpha_key]["seeds"][seed_key] = seed_result

    # Aggregate across seeds: mean MI
    for dm in DIVERSITY_METRICS:
        g_vals = all_mi_gauss[dm]
        k_vals = all_mi_ksg_vals[dm]
        results[alpha_key]["aggregate"][dm] = {
            "mi_gaussian_mean": round(np.mean(g_vals), 6) if g_vals else None,
            "mi_gaussian_std": round(np.std(g_vals), 6) if len(g_vals) > 1 else None,
            "mi_ksg_mean": round(np.mean(k_vals), 6) if k_vals else None,
            "mi_ksg_std": round(np.std(k_vals), 6) if len(k_vals) > 1 else None,
            "n_seeds": len(g_vals),
        }

    # Max MI across diversity metrics (Gaussian)
    max_mi_vals = []
    for dm in DIVERSITY_METRICS:
        g_vals = all_mi_gauss[dm]
        if g_vals:
            max_mi_vals.append(np.mean(g_vals))
    results[alpha_key]["aggregate"]["max_mi_gaussian"] = round(max(max_mi_vals), 6) if max_mi_vals else None
    results[alpha_key]["aggregate"]["mean_mi_gaussian"] = round(np.mean(max_mi_vals), 6) if max_mi_vals else None

# Save JSON
with open(OUT_JSON, "w") as f:
    json.dump(results, f, indent=2)
print(f"Saved MI results to {OUT_JSON}")

# === Plotting ===
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

plt.rcParams.update({
    "font.family": "serif",
    "font.serif": ["Times New Roman", "DejaVu Serif"],
    "font.size": 10,
    "axes.labelsize": 11,
    "axes.titlesize": 12,
    "legend.fontsize": 8.5,
    "xtick.labelsize": 9,
    "ytick.labelsize": 9,
    "figure.dpi": 150,
    "savefig.dpi": 300,
    "savefig.bbox": "tight",
    "pdf.fonttype": 42,
    "ps.fonttype": 42,
})

fig, axes = plt.subplots(1, 2, figsize=(10, 4))

# Panel A: MI (Gaussian LB) per diversity metric vs alpha
ax = axes[0]
colors = {"distinct_1": "#1f77b4", "distinct_2": "#ff7f0e", "distinct_3": "#2ca02c", "mauve": "#d62728"}
labels = {"distinct_1": "Distinct-1", "distinct_2": "Distinct-2", "distinct_3": "Distinct-3", "mauve": "MAUVE"}
markers = {"distinct_1": "o", "distinct_2": "s", "distinct_3": "^", "mauve": "D"}

for dm in DIVERSITY_METRICS:
    xs, ys, yerr_lo, yerr_hi = [], [], [], []
    for alpha in alphas_sorted:
        agg = results[f"{alpha:.2f}"]["aggregate"][dm]
        if agg["mi_gaussian_mean"] is not None:
            xs.append(alpha)
            ys.append(agg["mi_gaussian_mean"])
            # Use cross-seed std if available, else 0
            std = agg["mi_gaussian_std"] if agg["mi_gaussian_std"] is not None else 0
            yerr_lo.append(std)
            yerr_hi.append(std)

    xs, ys = np.array(xs), np.array(ys)
    yerr_lo, yerr_hi = np.array(yerr_lo), np.array(yerr_hi)

    ax.errorbar(xs, ys, yerr=[yerr_lo, yerr_hi], label=labels[dm],
                color=colors[dm], marker=markers[dm], markersize=5, linewidth=1.2,
                capsize=3, capthick=0.8, elinewidth=0.8)

ax.set_xlabel(r"Replacement fraction $\alpha$")
ax.set_ylabel("MI lower bound (bits)")
ax.set_title(r"$I(\mathrm{entropy};\,\mathrm{diversity})$ Gaussian LB")
ax.legend(loc="upper left", framealpha=0.9)
ax.set_xlim(-0.02, 0.82)
ax.grid(True, alpha=0.3)

# Panel B: Max MI across metrics vs alpha, with bootstrap CIs from individual seeds
ax2 = axes[1]
xs_max, ys_max = [], []
ci_lo_list, ci_hi_list = [], []

for alpha in alphas_sorted:
    alpha_key = f"{alpha:.2f}"
    # For each seed, compute max MI across diversity metrics, then average
    seed_max_mis = []
    seed_ci_ranges = []
    for seed_key, seed_data in results[alpha_key]["seeds"].items():
        seed_mis = []
        for dm in DIVERSITY_METRICS:
            mi_val = seed_data["metrics"][dm]["mi_gaussian_bits"]
            if mi_val is not None:
                seed_mis.append(mi_val)
        if seed_mis:
            seed_max_mis.append(max(seed_mis))
        # Get bootstrap CI for best metric
        best_dm = None
        best_mi = -1
        for dm in DIVERSITY_METRICS:
            mi_val = seed_data["metrics"][dm]["mi_gaussian_bits"]
            if mi_val is not None and mi_val > best_mi:
                best_mi = mi_val
                best_dm = dm
        if best_dm:
            ci = seed_data["metrics"][best_dm]["bootstrap_ci_95"]
            if ci[0] is not None:
                seed_ci_ranges.append(ci)

    if seed_max_mis:
        xs_max.append(alpha)
        mean_max = np.mean(seed_max_mis)
        ys_max.append(mean_max)
        if seed_ci_ranges:
            ci_lo_list.append(mean_max - np.mean([c[0] for c in seed_ci_ranges]))
            ci_hi_list.append(np.mean([c[1] for c in seed_ci_ranges]) - mean_max)
        else:
            ci_lo_list.append(0)
            ci_hi_list.append(0)

xs_max = np.array(xs_max)
ys_max = np.array(ys_max)

ax2.errorbar(xs_max, ys_max, yerr=[ci_lo_list, ci_hi_list],
             color="#333333", marker="o", markersize=6, linewidth=1.5,
             capsize=3, capthick=0.8, elinewidth=0.8, label="Max MI (Gaussian LB)")

# Shade critical region
ax2.axvspan(0.40, 0.60, alpha=0.08, color="red", label=r"$\alpha_c$ region")
ax2.axvline(0.50, color="red", linestyle="--", alpha=0.4, linewidth=0.8)

ax2.set_xlabel(r"Replacement fraction $\alpha$")
ax2.set_ylabel("MI lower bound (bits)")
ax2.set_title(r"Max $I(\mathrm{entropy};\,\mathrm{diversity})$ vs $\alpha$")
ax2.legend(loc="upper left", framealpha=0.9)
ax2.set_xlim(-0.02, 0.82)
ax2.grid(True, alpha=0.3)

# Add T annotation
ax2.annotate(f"T = 10–11 per run", xy=(0.98, 0.02), xycoords="axes fraction",
             ha="right", va="bottom", fontsize=7.5, color="gray", fontstyle="italic")

plt.tight_layout()
plt.savefig(OUT_FIG_PDF, format="pdf")
plt.savefig(OUT_FIG_PNG, format="png")
print(f"Saved figures to {OUT_FIG_PDF} and {OUT_FIG_PNG}")

# Print summary table
print("\n=== MI Summary (Gaussian LB, bits) ===")
print(f"{'alpha':>6} | {'D1':>8} | {'D2':>8} | {'D3':>8} | {'MAUVE':>8} | {'Max':>8} | {'seeds':>5}")
print("-" * 65)
for alpha in alphas_sorted:
    agg = results[f"{alpha:.2f}"]["aggregate"]
    d1 = agg["distinct_1"]["mi_gaussian_mean"]
    d2 = agg["distinct_2"]["mi_gaussian_mean"]
    d3 = agg["distinct_3"]["mi_gaussian_mean"]
    mv = agg["mauve"]["mi_gaussian_mean"]
    mx = agg["max_mi_gaussian"]
    ns = agg["distinct_1"]["n_seeds"]
    fmt = lambda v: f"{v:.4f}" if v is not None else "   N/A"
    print(f"{alpha:>6.2f} | {fmt(d1):>8} | {fmt(d2):>8} | {fmt(d3):>8} | {fmt(mv):>8} | {fmt(mx):>8} | {ns:>5}")
