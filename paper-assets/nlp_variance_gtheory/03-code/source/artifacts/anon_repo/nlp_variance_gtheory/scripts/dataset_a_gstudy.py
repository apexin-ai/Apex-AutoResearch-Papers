"""Dataset A full G-study: 3 models × bf16 only, 6 facets. Fully vectorized."""

import json
import sys
import time
from itertools import combinations
from math import prod
from pathlib import Path

import numpy as np
import pandas as pd

sys.path.insert(0, ".")
from src.analysis.variance_decomposition import compute_ss, estimate_variance_components

INPUT = "results/analysis/cross_model_3way_bf16.csv"
OUTPUT = "results/analysis/dataset_a_gstudy.json"
RESPONSE = "correct"
N_BOOT = 200
SEED = 42

FACETS = ["model", "temperature", "prompt_template", "seed", "ordering", "item_id"]
FIXED_FACETS = ["temperature"]
RANDOM_FACETS = ["model", "prompt_template", "seed", "ordering", "item_id"]

t_start = time.time()
df = pd.read_csv(INPUT)
for f in FACETS:
    df[f] = df[f].astype(str)

print(f"Loaded {len(df)} obs, {df['model'].nunique()} models, {df['item_id'].nunique()} items ({time.time()-t_start:.1f}s)", flush=True)

# Step 1: ANOVA on full data
effects, n_levels = compute_ss(df, RESPONSE, FACETS)
vc = estimate_variance_components(effects, FACETS, n_levels)
total_var = sum(vc.values())

print(f"\n{'Component':<30} {'Estimate':>12} {'%':>8}", flush=True)
print("-" * 52, flush=True)
for name, est in sorted(vc.items(), key=lambda x: -x[1]):
    pct = est / total_var * 100
    if pct >= 0.01:
        print(f"{name:<30} {est:>12.8f} {pct:>7.2f}%", flush=True)

# Step 2: Build 6D numpy array (vectorized)
facet_order = FACETS
facet_vals = {}
facet_maps = {}
for f in facet_order:
    vals = sorted(df[f].unique())
    facet_vals[f] = vals
    facet_maps[f] = {v: i for i, v in enumerate(vals)}

shape = tuple(len(facet_vals[f]) for f in facet_order)
print(f"\nBuilding {shape} array (vectorized)...", flush=True)

indices = tuple(df[f].map(facet_maps[f]).values for f in facet_order)
data_array = np.zeros(shape, dtype=np.float64)
data_array[indices] = df[RESPONSE].values
print(f"Array built. Grand mean: {data_array.mean():.4f}", flush=True)

# Vectorized SS computation
def compute_ss_numpy(arr, facet_names):
    ndim = arr.ndim
    N = arr.size
    gm = arr.mean()
    n_lev = {facet_names[i]: arr.shape[i] for i in range(ndim)}
    effects = {}
    
    for i in range(ndim):
        axes = tuple(j for j in range(ndim) if j != i)
        level_means = arr.mean(axis=axes)
        n_per = N // arr.shape[i]
        ss = float(n_per * np.sum((level_means - gm)**2))
        df_eff = arr.shape[i] - 1
        effects[facet_names[i]] = {"ss": ss, "df": df_eff, "ms": ss / df_eff if df_eff > 0 else 0.0}
    
    for i, j in combinations(range(ndim), 2):
        axes = tuple(k for k in range(ndim) if k not in (i, j))
        cell_means = arr.mean(axis=axes)
        main_i = arr.mean(axis=tuple(k for k in range(ndim) if k != i))
        main_j = arr.mean(axis=tuple(k for k in range(ndim) if k != j))
        interaction = cell_means - main_i[:, None] - main_j[None, :] + gm
        n_per = N // (arr.shape[i] * arr.shape[j])
        ss = float(n_per * np.sum(interaction**2))
        df_eff = (arr.shape[i] - 1) * (arr.shape[j] - 1)
        key = f"{facet_names[i]}:{facet_names[j]}"
        effects[key] = {"ss": ss, "df": df_eff, "ms": ss / df_eff if df_eff > 0 else 0.0}
    
    ss_total = float(np.sum((arr - gm)**2))
    ss_model = sum(e["ss"] for e in effects.values())
    ss_res = max(0.0, ss_total - ss_model)
    df_res = N - 1 - sum(e["df"] for e in effects.values())
    effects["residual"] = {"ss": ss_res, "df": df_res, "ms": ss_res / df_res if df_res > 0 else 0.0}
    
    return effects, n_lev

# Verify numpy matches pandas
effects_np, n_levels_np = compute_ss_numpy(data_array, facet_order)
vc_np = estimate_variance_components(effects_np, facet_order, n_levels_np)
max_diff = max(abs(vc.get(k, 0) - vc_np.get(k, 0)) for k in vc)
print(f"Numpy vs Pandas max diff: {max_diff:.2e} {'OK' if max_diff < 1e-8 else 'MISMATCH!'}", flush=True)

# Step 3: Fast bootstrap
print(f"\nBootstrapping ({N_BOOT} iterations, numpy-vectorized)...", flush=True)
t0 = time.time()

rng = np.random.RandomState(SEED)
n_items = data_array.shape[5]

boot_vcs = []
for b in range(N_BOOT):
    if (b + 1) % 50 == 0:
        elapsed = time.time() - t0
        rate = (b + 1) / elapsed
        eta = (N_BOOT - b - 1) / rate
        print(f"  bootstrap {b+1}/{N_BOOT}  ({elapsed:.1f}s elapsed, ETA {eta:.0f}s)", flush=True)
    
    boot_idx = rng.choice(n_items, size=n_items, replace=True)
    boot_arr = data_array[:, :, :, :, :, boot_idx]
    eff, nl = compute_ss_numpy(boot_arr, facet_order)
    bvc = estimate_variance_components(eff, facet_order, nl)
    boot_vcs.append(bvc)

elapsed = time.time() - t0
print(f"Bootstrap done in {elapsed:.1f}s ({elapsed/N_BOOT:.3f}s/iter)", flush=True)

ci = {}
for key in boot_vcs[0]:
    values = [bv[key] for bv in boot_vcs]
    ci[key] = {
        "lower": float(np.percentile(values, 2.5)),
        "upper": float(np.percentile(values, 97.5)),
        "mean": float(np.mean(values)),
        "std": float(np.std(values)),
    }

# Step 4: G_item
def compute_g_item(vc_dict, n_lev, n_model_override=None):
    sigma_item = vc_dict.get("item_id", 0.0)
    random_n = {f: n_lev[f] for f in RANDOM_FACETS}
    if n_model_override is not None:
        random_n["model"] = n_model_override
    delta = 0.0
    for comp, est in vc_dict.items():
        if comp == "item_id" or est == 0.0:
            continue
        if comp == "residual":
            delta += est / prod(random_n[f] for f in RANDOM_FACETS)
            continue
        facets_in = comp.split(":")
        if "item_id" not in facets_in:
            continue
        random_in = [f for f in facets_in if f in set(RANDOM_FACETS)]
        divisor = prod(random_n[f] for f in random_in if f != "item_id")
        if divisor > 0:
            delta += est / divisor
    g = sigma_item / (sigma_item + delta) if (sigma_item + delta) > 0 else 0.0
    return g, sigma_item, delta

g_item, tau_item, delta_item = compute_g_item(vc, n_levels)
print(f"\nG_item = {g_item:.4f}  (tau={tau_item:.6f}, delta={delta_item:.6f})", flush=True)

# D-study
print(f"\nD-study: n_models sweep", flush=True)
print(f"{'n_models':>10} {'G_item':>10}", flush=True)
print("-" * 22, flush=True)
d_study = []
for n_m in [1, 2, 3, 4, 5, 6, 8, 10]:
    g, tau, delta = compute_g_item(vc, n_levels, n_model_override=n_m)
    d_study.append({"n_models": n_m, "g_item": round(g, 6), "sigma_tau": round(tau, 8), "sigma_delta": round(delta, 8)})
    print(f"{n_m:>10} {g:>10.4f}", flush=True)

# G_condition
def compute_g_condition(vc_dict, n_lev):
    random_n = {f: n_lev[f] for f in RANDOM_FACETS}
    sigma_tau = 0.0
    sigma_delta = 0.0
    for comp, est in vc_dict.items():
        if est == 0.0:
            continue
        if comp == "residual":
            sigma_delta += est / prod(random_n[f] for f in RANDOM_FACETS)
            continue
        facets_in = set(comp.split(":"))
        random_in = [f for f in facets_in if f in set(RANDOM_FACETS)]
        if len(random_in) == 0:
            sigma_tau += est
        else:
            sigma_delta += est / prod(random_n[f] for f in random_in)
    g = sigma_tau / (sigma_tau + sigma_delta) if (sigma_tau + sigma_delta) > 0 else 0.0
    return g, sigma_tau, sigma_delta

g_cond, tau_cond, delta_cond = compute_g_condition(vc, n_levels)
print(f"\nG_condition = {g_cond:.4f}  (tau={tau_cond:.6f}, delta={delta_cond:.6f})", flush=True)

# Full table with CI
print(f"\n{'='*70}", flush=True)
print("FULL RESULTS WITH 95% CI", flush=True)
print(f"{'='*70}", flush=True)
print(f"\n{'Component':<30} {'%':>8} {'95% CI':>24}", flush=True)
print("-" * 64, flush=True)
for name, est in sorted(vc.items(), key=lambda x: -x[1]):
    pct = est / total_var * 100
    lo_pct = ci[name]["lower"] / total_var * 100
    hi_pct = ci[name]["upper"] / total_var * 100
    if pct >= 0.01:
        print(f"{name:<30} {pct:>7.2f}%  [{lo_pct:>7.2f}%, {hi_pct:>7.2f}%]", flush=True)

# Bootstrap CI for G_item
boot_g_items = [compute_g_item(bvc, n_levels)[0] for bvc in boot_vcs]
g_item_ci = [float(np.percentile(boot_g_items, 2.5)), float(np.percentile(boot_g_items, 97.5))]
print(f"\nG_item = {g_item:.4f}  95% CI [{g_item_ci[0]:.4f}, {g_item_ci[1]:.4f}]", flush=True)

# Model accuracies
print(f"\nModel accuracies:", flush=True)
model_accs = {}
for i, m in enumerate(facet_vals["model"]):
    acc = float(data_array[i].mean())
    model_accs[m] = acc
    print(f"  {m}: {acc:.4f}", flush=True)

# Save
results = {
    "dataset": "A",
    "description": "3 models (Llama-3.1-8B, Gemma-2-9B, Mistral-7B) x bf16 only, 6 facets",
    "n_observations": int(data_array.size),
    "n_levels": {k: int(v) for k, v in n_levels.items()},
    "facets": FACETS,
    "fixed_facets": FIXED_FACETS,
    "random_facets": RANDOM_FACETS,
    "grand_mean": float(data_array.mean()),
    "total_variance": total_var,
    "variance_components": {
        k: {"estimate": v, "pct": v / total_var * 100,
            "ci_95_lower": ci[k]["lower"], "ci_95_upper": ci[k]["upper"],
            "ci_95_lower_pct": ci[k]["lower"] / total_var * 100,
            "ci_95_upper_pct": ci[k]["upper"] / total_var * 100}
        for k, v in vc.items()
    },
    "g_item": {"g": round(g_item, 6), "ci_95": g_item_ci,
               "sigma_tau": round(tau_item, 8), "sigma_delta": round(delta_item, 8)},
    "g_condition": {"g": round(g_cond, 6),
                    "sigma_tau": round(tau_cond, 8), "sigma_delta": round(delta_cond, 8)},
    "d_study_model_sweep": d_study,
    "anova_table": {k: {"ss": v["ss"], "df": v["df"], "ms": v["ms"]} for k, v in effects.items()},
    "bootstrap": {"n_resamples": N_BOOT, "seed": SEED, "method": "item cluster resampling (numpy 6D array)"},
    "model_accuracies": model_accs,
}

Path(OUTPUT).parent.mkdir(parents=True, exist_ok=True)
with open(OUTPUT, "w") as f:
    json.dump(results, f, indent=2)

print(f"\nTotal runtime: {time.time()-t_start:.1f}s", flush=True)
print(f"-> Saved to {OUTPUT}", flush=True)
