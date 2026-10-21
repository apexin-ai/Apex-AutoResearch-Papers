"""Model-as-fixed G-study (MF2 defense).

Treats model as a fixed facet (not a random sample from a population of models).
Two methods:
  A) Per-model 5-facet G-study, then average (clean separation)
  B) Remove model:item from σ²δ in the crossed 6-facet design (quick adjustment)

Input:  results/analysis/cross_model_4way_bf16.csv (4 models × bf16 × fully crossed)
Output: results/analysis/model_as_fixed_gstudy.json
"""

import json
import time
from itertools import combinations
from math import prod
from pathlib import Path

import numpy as np
import pandas as pd

INPUT = "results/analysis/cross_model_4way_bf16.csv"
OUTPUT = "results/analysis/model_as_fixed_gstudy.json"
N_BOOT = 200
SEED = 42

FACETS_6 = ["model", "temperature", "prompt_template", "seed", "ordering", "item_id"]
FACETS_5 = ["temperature", "prompt_template", "seed", "ordering", "item_id"]

t_start = time.time()
df = pd.read_csv(INPUT)
print(f"Loaded {len(df)} obs ({time.time()-t_start:.1f}s)", flush=True)

models_sorted = sorted(df["model"].unique())
temps_sorted = sorted(df["temperature"].unique())
prompts_sorted = sorted(df["prompt_template"].unique())
seeds_sorted = sorted(df["seed"].unique())
orders_sorted = sorted(df["ordering"].unique())
items_sorted = sorted(df["item_id"].unique())

n_m, n_t, n_p, n_s, n_o, n_i = (
    len(models_sorted), len(temps_sorted), len(prompts_sorted),
    len(seeds_sorted), len(orders_sorted), len(items_sorted),
)
print(f"Design: {n_m}m x {n_t}t x {n_p}p x {n_s}s x {n_o}o x {n_i}i = {n_m*n_t*n_p*n_s*n_o*n_i}", flush=True)

model_map = {v: i for i, v in enumerate(models_sorted)}
temp_map = {v: i for i, v in enumerate(temps_sorted)}
prompt_map = {v: i for i, v in enumerate(prompts_sorted)}
seed_map = {v: i for i, v in enumerate(seeds_sorted)}
order_map = {v: i for i, v in enumerate(orders_sorted)}
item_map = {v: i for i, v in enumerate(items_sorted)}

Y = np.full((n_m, n_t, n_p, n_s, n_o, n_i), np.nan)
for _, row in df.iterrows():
    Y[model_map[row["model"]], temp_map[row["temperature"]],
      prompt_map[row["prompt_template"]], seed_map[row["seed"]],
      order_map[row["ordering"]], item_map[row["item_id"]]] = row["correct"]

assert np.isnan(Y).sum() == 0, f"Missing cells: {np.isnan(Y).sum()}"
print(f"6D array built ({time.time()-t_start:.1f}s)", flush=True)


def compute_gstudy_5facet(arr_5d):
    """5-facet Henderson I on (temp, prompt, seed, ordering, item) array."""
    nt, np_, ns, no, ni = arr_5d.shape
    N = arr_5d.size
    gm = arr_5d.mean()
    facet_names = FACETS_5
    n_lev = {"temperature": nt, "prompt_template": np_, "seed": ns, "ordering": no, "item_id": ni}

    effects = {}
    for idx, f in enumerate(facet_names):
        other_axes = tuple(j for j in range(5) if j != idx)
        level_means = arr_5d.mean(axis=other_axes)
        n_per = N // arr_5d.shape[idx]
        ss = float(n_per * np.sum((level_means - gm) ** 2))
        df_eff = arr_5d.shape[idx] - 1
        effects[f] = {"ss": ss, "df": df_eff, "ms": ss / df_eff if df_eff > 0 else 0.0}

    for i_idx in range(5):
        for j_idx in range(i_idx + 1, 5):
            fi, fj = facet_names[i_idx], facet_names[j_idx]
            other_axes = tuple(k for k in range(5) if k not in (i_idx, j_idx))
            cell_means = arr_5d.mean(axis=other_axes)
            main_i = arr_5d.mean(axis=tuple(k for k in range(5) if k != i_idx))
            main_j = arr_5d.mean(axis=tuple(k for k in range(5) if k != j_idx))
            interaction = cell_means - main_i[:, None] - main_j[None, :] + gm
            n_per = N // (arr_5d.shape[i_idx] * arr_5d.shape[j_idx])
            ss = float(n_per * np.sum(interaction ** 2))
            df_eff = (arr_5d.shape[i_idx] - 1) * (arr_5d.shape[j_idx] - 1)
            key = f"{fi}:{fj}"
            effects[key] = {"ss": ss, "df": df_eff, "ms": ss / df_eff if df_eff > 0 else 0.0}

    ss_total = float(np.sum((arr_5d - gm) ** 2))
    ss_model = sum(e["ss"] for e in effects.values())
    ss_res = max(0.0, ss_total - ss_model)
    df_res = N - 1 - sum(e["df"] for e in effects.values())
    effects["residual"] = {"ss": ss_res, "df": df_res, "ms": ss_res / df_res if df_res > 0 else 0.0}

    ms_res = effects["residual"]["ms"]
    vc = {}
    for fi, fj in combinations(facet_names, 2):
        key = f"{fi}:{fj}"
        coeff = prod(n_lev[f] for f in facet_names if f not in (fi, fj))
        raw = (effects[key]["ms"] - ms_res) / coeff if coeff > 0 else 0.0
        vc[key] = max(0.0, raw)

    for fi in facet_names:
        coeff_main = prod(n_lev[f] for f in facet_names if f != fi)
        interaction_contrib = 0.0
        for fj in facet_names:
            if fj == fi:
                continue
            int_key = f"{fi}:{fj}" if f"{fi}:{fj}" in vc else f"{fj}:{fi}"
            coeff_ij = prod(n_lev[f] for f in facet_names if f not in (fi, fj))
            interaction_contrib += coeff_ij * vc[int_key]
        raw = (effects[fi]["ms"] - interaction_contrib - ms_res) / coeff_main if coeff_main > 0 else 0.0
        vc[fi] = max(0.0, raw)

    vc["residual"] = ms_res
    return vc, n_lev, effects


def compute_g_item_5facet(vc, n_lev):
    """G_item for 5-facet within-model design.

    Object of measurement: item_id.
    σ²_τ = σ²(item_id)
    σ²_δ = Σ σ²(X:item_id)/n_X + σ²(residual)/Π(n_X for X ≠ item_id)
    """
    sigma_item = vc.get("item_id", 0.0)
    non_item_facets = ["temperature", "prompt_template", "seed", "ordering"]

    sigma_delta = 0.0
    for comp, est in vc.items():
        if est == 0.0 or comp == "item_id":
            continue
        if comp == "residual":
            divisor = prod(n_lev[f] for f in non_item_facets)
            sigma_delta += est / divisor
            continue
        facets_in = set(comp.split(":"))
        if "item_id" not in facets_in:
            continue
        other = [f for f in facets_in if f != "item_id"]
        divisor = prod(n_lev[f] for f in other) if other else 1
        sigma_delta += est / divisor

    g = sigma_item / (sigma_item + sigma_delta) if (sigma_item + sigma_delta) > 0 else 0.0
    return g, sigma_item, sigma_delta


def compute_gstudy_6facet(Y_6d):
    """Full 6-facet Henderson I on (model, temp, prompt, seed, ordering, item) array."""
    nm, nt, np_, ns, no, ni = Y_6d.shape
    N = Y_6d.size
    gm = Y_6d.mean()
    facet_names = FACETS_6
    n_lev = {"model": nm, "temperature": nt, "prompt_template": np_, "seed": ns, "ordering": no, "item_id": ni}

    effects = {}
    for idx, f in enumerate(facet_names):
        other_axes = tuple(j for j in range(6) if j != idx)
        level_means = Y_6d.mean(axis=other_axes)
        n_per = N // Y_6d.shape[idx]
        ss = float(n_per * np.sum((level_means - gm) ** 2))
        df_eff = Y_6d.shape[idx] - 1
        effects[f] = {"ss": ss, "df": df_eff, "ms": ss / df_eff if df_eff > 0 else 0.0}

    for i_idx in range(6):
        for j_idx in range(i_idx + 1, 6):
            fi, fj = facet_names[i_idx], facet_names[j_idx]
            other_axes = tuple(k for k in range(6) if k not in (i_idx, j_idx))
            cell_means = Y_6d.mean(axis=other_axes)
            main_i = Y_6d.mean(axis=tuple(k for k in range(6) if k != i_idx))
            main_j = Y_6d.mean(axis=tuple(k for k in range(6) if k != j_idx))
            interaction = cell_means - main_i[:, None] - main_j[None, :] + gm
            n_per = N // (Y_6d.shape[i_idx] * Y_6d.shape[j_idx])
            ss = float(n_per * np.sum(interaction ** 2))
            df_eff = (Y_6d.shape[i_idx] - 1) * (Y_6d.shape[j_idx] - 1)
            key = f"{fi}:{fj}"
            effects[key] = {"ss": ss, "df": df_eff, "ms": ss / df_eff if df_eff > 0 else 0.0}

    ss_total = float(np.sum((Y_6d - gm) ** 2))
    ss_model = sum(e["ss"] for e in effects.values())
    ss_res = max(0.0, ss_total - ss_model)
    df_res = N - 1 - sum(e["df"] for e in effects.values())
    effects["residual"] = {"ss": ss_res, "df": df_res, "ms": ss_res / df_res if df_res > 0 else 0.0}

    ms_res = effects["residual"]["ms"]
    vc = {}
    for fi, fj in combinations(facet_names, 2):
        key = f"{fi}:{fj}"
        coeff = prod(n_lev[f] for f in facet_names if f not in (fi, fj))
        raw = (effects[key]["ms"] - ms_res) / coeff if coeff > 0 else 0.0
        vc[key] = max(0.0, raw)

    for fi in facet_names:
        coeff_main = prod(n_lev[f] for f in facet_names if f != fi)
        interaction_contrib = 0.0
        for fj in facet_names:
            if fj == fi:
                continue
            int_key = f"{fi}:{fj}" if f"{fi}:{fj}" in vc else f"{fj}:{fi}"
            coeff_ij = prod(n_lev[f] for f in facet_names if f not in (fi, fj))
            interaction_contrib += coeff_ij * vc[int_key]
        raw = (effects[fi]["ms"] - interaction_contrib - ms_res) / coeff_main if coeff_main > 0 else 0.0
        vc[fi] = max(0.0, raw)

    vc["residual"] = ms_res
    return vc, n_lev, effects


def compute_g_item_random(vc, n_lev):
    """G_item with model as RANDOM.

    σ²_δ = σ²(model:item)/n_m + σ²(temp:item)/n_t + ... + σ²(res)/(n_m·n_t·n_p·n_s·n_o)
    """
    sigma_item = vc.get("item_id", 0.0)
    delta = (
        vc.get("model:item_id", 0.0) / n_lev["model"]
        + vc.get("temperature:item_id", 0.0) / n_lev["temperature"]
        + vc.get("prompt_template:item_id", 0.0) / n_lev["prompt_template"]
        + vc.get("seed:item_id", 0.0) / n_lev["seed"]
        + vc.get("ordering:item_id", 0.0) / n_lev["ordering"]
        + vc["residual"] / (n_lev["model"] * n_lev["temperature"] * n_lev["prompt_template"]
                            * n_lev["seed"] * n_lev["ordering"])
    )
    g = sigma_item / (sigma_item + delta) if (sigma_item + delta) > 0 else 0.0
    return g, sigma_item, delta


def compute_g_item_fixed_methodB(vc, n_lev):
    """G_item with model as FIXED (Method B: remove model:item from σ²δ).

    Same residual divisor (n_m still in denominator since we average over 4 fixed models).
    """
    sigma_item = vc.get("item_id", 0.0)
    delta = (
        vc.get("temperature:item_id", 0.0) / n_lev["temperature"]
        + vc.get("prompt_template:item_id", 0.0) / n_lev["prompt_template"]
        + vc.get("seed:item_id", 0.0) / n_lev["seed"]
        + vc.get("ordering:item_id", 0.0) / n_lev["ordering"]
        + vc["residual"] / (n_lev["model"] * n_lev["temperature"] * n_lev["prompt_template"]
                            * n_lev["seed"] * n_lev["ordering"])
    )
    g = sigma_item / (sigma_item + delta) if (sigma_item + delta) > 0 else 0.0
    return g, sigma_item, delta


# ============================================================
# Full 6-facet G-study (reproduce random-model baseline)
# ============================================================
print("\n=== 6-facet G-study (model=random baseline) ===", flush=True)
vc_6, nl_6, eff_6 = compute_gstudy_6facet(Y)
total_var_6 = sum(vc_6.values())

g_random, tau_random, delta_random = compute_g_item_random(vc_6, nl_6)
print(f"G_item (model=random) = {g_random:.6f}", flush=True)
print(f"  sigma_tau={tau_random:.8f}, sigma_delta={delta_random:.8f}", flush=True)


# ============================================================
# Method B: Fixed model in crossed design
# ============================================================
print("\n=== Method B: model-as-fixed (remove model:item from delta) ===", flush=True)
g_fixedB, tau_fixedB, delta_fixedB = compute_g_item_fixed_methodB(vc_6, nl_6)
print(f"G_item (model=fixed, Method B) = {g_fixedB:.6f}", flush=True)
print(f"  sigma_delta: {delta_random:.8f} -> {delta_fixedB:.8f}", flush=True)
print(f"  removed: model:item/n_m = {vc_6.get('model:item_id', 0)/nl_6['model']:.8f}", flush=True)


# ============================================================
# Method A: Per-model 5-facet G-study
# ============================================================
print("\n=== Method A: per-model 5-facet G-study ===", flush=True)
per_model_results = {}
g_items_per_model = []

for mi, model_name in enumerate(models_sorted):
    Y_m = Y[mi]
    vc_m, nl_m, eff_m = compute_gstudy_5facet(Y_m)
    g_m, tau_m, delta_m = compute_g_item_5facet(vc_m, nl_m)
    g_items_per_model.append(g_m)

    total_var_m = sum(vc_m.values())
    per_model_results[model_name] = {
        "g_item": round(g_m, 6),
        "sigma_tau": round(tau_m, 8),
        "sigma_delta": round(delta_m, 8),
        "variance_components": {
            k: {"estimate": v, "pct": v / total_var_m * 100 if total_var_m > 0 else 0.0}
            for k, v in sorted(vc_m.items(), key=lambda x: -x[1])
        },
        "accuracy": float(Y_m.mean()),
    }
    print(f"  {model_name}: G_item={g_m:.6f}, acc={Y_m.mean():.4f}, "
          f"s2_item={vc_m['item_id']:.6f}, s2_delta={delta_m:.6f}", flush=True)

g_fixed_A = float(np.mean(g_items_per_model))
print(f"\nAverage G_item (model=fixed, Method A) = {g_fixed_A:.6f}", flush=True)

pooled_vc = {}
for key in per_model_results[models_sorted[0]]["variance_components"]:
    vals = [per_model_results[m]["variance_components"][key]["estimate"] for m in models_sorted]
    pooled_vc[key] = float(np.mean(vals))
pooled_total = sum(pooled_vc.values())


# ============================================================
# Bootstrap CI
# ============================================================
print(f"\nBootstrapping ({N_BOOT} resamples)...", flush=True)
rng = np.random.default_rng(SEED)
boot_g_fixed_A = []
boot_g_fixed_B = []
boot_g_random = []

for b in range(N_BOOT):
    if b % 50 == 0:
        print(f"  {b}/{N_BOOT}...", flush=True)
    idx = rng.choice(n_i, size=n_i, replace=True)
    Y_b = Y[:, :, :, :, :, idx]

    vc_b6, nl_b6, _ = compute_gstudy_6facet(Y_b)
    g_r, _, _ = compute_g_item_random(vc_b6, nl_b6)
    boot_g_random.append(g_r)

    g_fB, _, _ = compute_g_item_fixed_methodB(vc_b6, nl_b6)
    boot_g_fixed_B.append(g_fB)

    g_per_model_b = []
    for mi in range(n_m):
        vc_bm, nl_bm, _ = compute_gstudy_5facet(Y_b[mi])
        g_bm, _, _ = compute_g_item_5facet(vc_bm, nl_bm)
        g_per_model_b.append(g_bm)
    boot_g_fixed_A.append(float(np.mean(g_per_model_b)))

ci_random = [float(np.percentile(boot_g_random, 2.5)), float(np.percentile(boot_g_random, 97.5))]
ci_fixed_A = [float(np.percentile(boot_g_fixed_A, 2.5)), float(np.percentile(boot_g_fixed_A, 97.5))]
ci_fixed_B = [float(np.percentile(boot_g_fixed_B, 2.5)), float(np.percentile(boot_g_fixed_B, 97.5))]

print(f"\nResults with 95% CI:", flush=True)
print(f"  G_item (random):  {g_random:.6f} [{ci_random[0]:.6f}, {ci_random[1]:.6f}]", flush=True)
print(f"  G_item (fixed A): {g_fixed_A:.6f} [{ci_fixed_A[0]:.6f}, {ci_fixed_A[1]:.6f}]", flush=True)
print(f"  G_item (fixed B): {g_fixedB:.6f} [{ci_fixed_B[0]:.6f}, {ci_fixed_B[1]:.6f}]", flush=True)


# ============================================================
# Ranking consistency
# ============================================================
from scipy.stats import spearmanr

per_model_item_means = {}
for mi, m in enumerate(models_sorted):
    per_model_item_means[m] = Y[mi].mean(axis=(0, 1, 2, 3))

rank_corrs = []
for i in range(len(models_sorted)):
    for j in range(i + 1, len(models_sorted)):
        mi, mj = models_sorted[i], models_sorted[j]
        rho, _ = spearmanr(per_model_item_means[mi], per_model_item_means[mj])
        rank_corrs.append({"pair": f"{mi} vs {mj}", "spearman_rho": round(float(rho), 4)})

mean_rho = float(np.mean([r["spearman_rho"] for r in rank_corrs]))
print(f"\nItem ranking consistency across models:", flush=True)
for r in rank_corrs:
    print(f"  {r['pair']}: rho={r['spearman_rho']:.4f}", flush=True)
print(f"  Mean rho = {mean_rho:.4f}", flush=True)


# ============================================================
# Save
# ============================================================
results = {
    "random_model": {
        "G_item": round(g_random, 6),
        "ci_95": ci_random,
        "sigma_tau": round(tau_random, 8),
        "sigma_delta": round(delta_random, 8),
        "variance_components": {
            k: {"estimate": v, "pct": v / total_var_6 * 100}
            for k, v in sorted(vc_6.items(), key=lambda x: -x[1])
        },
    },
    "fixed_model": {
        "method_A_per_model_average": {
            "G_item": round(g_fixed_A, 6),
            "ci_95": ci_fixed_A,
            "description": "Average of per-model 5-facet G_item values",
        },
        "method_B_remove_model_item": {
            "G_item": round(g_fixedB, 6),
            "ci_95": ci_fixed_B,
            "sigma_tau": round(tau_fixedB, 8),
            "sigma_delta": round(delta_fixedB, 8),
            "description": "6-facet VC with model:item_id removed from sigma_delta",
        },
        "per_model_gstudy": per_model_results,
        "pooled_variance_components": {
            k: {"estimate": v, "pct": v / pooled_total * 100 if pooled_total > 0 else 0.0}
            for k, v in sorted(pooled_vc.items(), key=lambda x: -x[1])
        },
    },
    "comparison": {
        "G_item_random": round(g_random, 6),
        "G_item_fixed_A": round(g_fixed_A, 6),
        "G_item_fixed_B": round(g_fixedB, 6),
        "G_item_delta_A": round(g_fixed_A - g_random, 6),
        "G_item_delta_B": round(g_fixedB - g_random, 6),
        "ranking_consistency": {
            "pairwise_spearman": rank_corrs,
            "mean_spearman_rho": round(mean_rho, 4),
            "consistent": mean_rho > 0.7,
        },
        "interpretation": (
            "Model-as-fixed G_item is higher because model:item variance "
            "(differential item difficulty across models) is no longer treated as "
            "measurement error. This is appropriate when generalizing to these "
            "specific 4 models rather than a hypothetical population of models."
        ),
    },
    "design": {
        "n_observations": int(Y.size),
        "n_levels": {"model": n_m, "temperature": n_t, "prompt_template": n_p,
                     "seed": n_s, "ordering": n_o, "item_id": n_i},
        "models": models_sorted,
        "fixed_facets_random_design": ["temperature"],
        "fixed_facets_fixed_model_design": ["model", "temperature"],
    },
    "bootstrap": {"n_resamples": N_BOOT, "seed": SEED, "method": "item cluster resampling"},
}

Path(OUTPUT).parent.mkdir(parents=True, exist_ok=True)
with open(OUTPUT, "w") as f:
    json.dump(results, f, indent=2, default=str)

print(f"\nTotal runtime: {time.time()-t_start:.1f}s", flush=True)
print(f"-> Saved to {OUTPUT}", flush=True)
