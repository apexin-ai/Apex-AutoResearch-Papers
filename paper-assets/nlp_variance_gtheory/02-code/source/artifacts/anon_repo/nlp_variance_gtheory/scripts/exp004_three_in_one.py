#!/usr/bin/env python3
"""
exp004_three_in_one.py
Part A: 8-model MMLU cross-model G-study + bootstrap CI
Part B: MC vs FF permutation test on item_id%
Part C: D-study projections (per benchmark, 8-model where available)
"""
import json, sys, time
from itertools import combinations
from math import prod
from pathlib import Path

import numpy as np
import pandas as pd

sys.path.insert(0, '.')
from src.config.model_paths import normalize_model_name

FACETS = ["model", "temperature", "prompt_template", "seed", "ordering", "item_id"]
KEEP_COLS = FACETS + ["correct"]
DATA_DIR = Path("./results/exp002")
OUTPUT_DIR = Path("./results/exp004_8model_analysis")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

def load_benchmark(benchmark):
    files = list(DATA_DIR.glob(f"*_{benchmark}.jsonl"))
    for extra in DATA_DIR.glob(f"*_{benchmark}_*.jsonl"):
        if extra not in files:
            files.append(extra)
    files.sort()
    frames = []
    for fp in files:
        d = pd.read_json(fp, lines=True)
        if "benchmark" in d.columns:
            d = d[d["benchmark"] == benchmark]
        else:
            continue
        if len(d) > 0:
            frames.append(d)
    df = pd.concat(frames, ignore_index=True)
    df = df.dropna(subset=["model", "item_id", "correct"])
    df["model"] = df["model"].map(normalize_model_name).fillna(df["model"])
    for f in FACETS:
        df[f] = df[f].astype(str)
    df.drop_duplicates(subset=["condition_id", "item_id", "model"], inplace=True)
    acc = df["correct"].mean()
    n_models = df["model"].nunique()
    models = sorted(df["model"].unique().tolist())
    df_slim = df[KEEP_COLS].copy().reset_index(drop=True)
    return df_slim, acc, n_models, models, len(df)

def henderson_i(df):
    response = "correct"
    grand_mean = df[response].mean()
    N = len(df)
    nl = {f: df[f].nunique() for f in FACETS}
    eff = {}
    for f in FACETS:
        gm = df.groupby(f, observed=True)[response].mean()
        n_per = N // nl[f]
        ss = float(n_per * ((gm - grand_mean)**2).sum())
        dof = nl[f] - 1
        eff[f] = {"ss": ss, "df": dof, "ms": ss/dof if dof else 0.0}
    for fi, fj in combinations(FACETS, 2):
        cm = df.groupby([fi, fj], observed=True)[response].mean()
        mi = df.groupby(fi, observed=True)[response].mean()
        mj = df.groupby(fj, observed=True)[response].mean()
        n_per = N // (nl[fi] * nl[fj])
        ss = 0.0
        for (li, lj), val in cm.items():
            ss += n_per * (val - mi[li] - mj[lj] + grand_mean)**2
        dof = (nl[fi]-1) * (nl[fj]-1)
        eff[f"{fi}:{fj}"] = {"ss": ss, "df": dof, "ms": ss/dof if dof else 0.0}
    ss_total = float(((df[response] - grand_mean)**2).sum())
    ss_model_sum = sum(e["ss"] for e in eff.values())
    ss_res = max(0.0, ss_total - ss_model_sum)
    df_res = N - 1 - sum(e["df"] for e in eff.values())
    eff["residual"] = {"ss": ss_res, "df": df_res, "ms": ss_res/df_res if df_res > 0 else 0.0}
    ms_res = eff["residual"]["ms"]
    vc = {}
    for fi, fj in combinations(FACETS, 2):
        key = f"{fi}:{fj}"
        coeff = prod(nl[f] for f in FACETS if f not in (fi, fj))
        vc[key] = max(0.0, (eff[key]["ms"] - ms_res) / coeff if coeff else 0.0)
    for fi in FACETS:
        coeff_main = prod(nl[f] for f in FACETS if f != fi)
        int_contrib = 0.0
        for fj in FACETS:
            if fj == fi: continue
            ik = f"{fi}:{fj}" if f"{fi}:{fj}" in vc else f"{fj}:{fi}"
            coeff_ij = prod(nl[f] for f in FACETS if f not in (fi, fj))
            int_contrib += coeff_ij * vc[ik]
        vc[fi] = max(0.0, (eff[fi]["ms"] - int_contrib - ms_res) / coeff_main if coeff_main else 0.0)
    vc["residual"] = ms_res
    return vc, nl

def g_item_calc(vc, nl):
    tau = vc.get("item_id", 0.0)
    delta = 0.0
    bd = {}
    for comp, est in vc.items():
        if comp == "item_id": continue
        if comp == "residual":
            div = prod(nl[f] for f in FACETS if f != "item_id")
            c = est / div
            bd["residual"] = {"est": est, "divisor": div, "contrib": c}
            delta += c
            continue
        parts = comp.split(":")
        if "item_id" not in parts: continue
        other = [f for f in parts if f != "item_id"]
        div = prod(nl[f] for f in other) if other else 1
        c = est / div
        bd[comp] = {"est": est, "divisor": div, "contrib": c}
        delta += c
    g = tau / (tau + delta) if (tau + delta) > 0 else 0.0
    return g, tau, delta, bd

def d_study(vc, nl, item_counts):
    tau = vc.get("item_id", 0.0)
    n_actual = nl["item_id"]
    err = 0.0
    for comp, est in vc.items():
        if comp == "item_id": continue
        if comp == "residual":
            div = prod(nl[f] for f in FACETS if f != "item_id")
            err += est / div
            continue
        parts = comp.split(":")
        if "item_id" not in parts: continue
        other = [f for f in parts if f != "item_id"]
        div = prod(nl[f] for f in other) if other else 1
        err += est / div
    curve = {}
    for ni in item_counts:
        delta_ni = err * (n_actual / ni)
        g = tau / (tau + delta_ni) if (tau + delta_ni) > 0 else 0.0
        curve[ni] = round(g, 6)
    return curve

def find_min_items(vc, nl, target=0.80, max_n=2000):
    tau = vc.get("item_id", 0.0)
    n_actual = nl["item_id"]
    err = 0.0
    for comp, est in vc.items():
        if comp == "item_id": continue
        if comp == "residual":
            div = prod(nl[f] for f in FACETS if f != "item_id")
            err += est / div
            continue
        parts = comp.split(":")
        if "item_id" not in parts: continue
        other = [f for f in parts if f != "item_id"]
        div = prod(nl[f] for f in other) if other else 1
        err += est / div
    for ni in range(1, max_n + 1):
        delta_ni = err * (n_actual / ni)
        g = tau / (tau + delta_ni) if (tau + delta_ni) > 0 else 0.0
        if g >= target:
            return ni
    return None

def bootstrap_g_numpy(df, n_boot=500, seed=42):
    """Fast bootstrap using numpy array reshaping for balanced design."""
    items = sorted(df["item_id"].unique())
    n_items = len(items)
    models = sorted(df["model"].unique())
    temps = sorted(df["temperature"].unique())
    prompts = sorted(df["prompt_template"].unique())
    seeds = sorted(df["seed"].unique())
    orderings = sorted(df["ordering"].unique())

    dims = [n_items, len(models), len(temps), len(prompts), len(seeds), len(orderings)]
    expected_n = prod(dims)
    print(f"  Expected balanced N={expected_n}, actual N={len(df)}", flush=True)

    item_map = {v: i for i, v in enumerate(items)}
    model_map = {v: i for i, v in enumerate(models)}
    temp_map = {v: i for i, v in enumerate(temps)}
    prompt_map = {v: i for i, v in enumerate(prompts)}
    seed_map = {v: i for i, v in enumerate(seeds)}
    ord_map = {v: i for i, v in enumerate(orderings)}

    arr = np.full(dims, np.nan)
    for _, row in df.iterrows():
        i0 = item_map[row["item_id"]]
        i1 = model_map[row["model"]]
        i2 = temp_map[row["temperature"]]
        i3 = prompt_map[row["prompt_template"]]
        i4 = seed_map[row["seed"]]
        i5 = ord_map[row["ordering"]]
        arr[i0, i1, i2, i3, i4, i5] = row["correct"]

    nan_count = np.isnan(arr).sum()
    if nan_count > 0:
        print(f"  WARNING: {nan_count} NaN cells in balanced array, filling with grand mean", flush=True)
        arr[np.isnan(arr)] = np.nanmean(arr)

    def henderson_i_array(a):
        # a: [items, models, temps, prompts, seeds, orderings]
        gm = a.mean()
        N = a.size
        dims_a = a.shape
        nl = {"item_id": dims_a[0], "model": dims_a[1], "temperature": dims_a[2],
              "prompt_template": dims_a[3], "seed": dims_a[4], "ordering": dims_a[5]}
        facet_axes = {"item_id": 0, "model": 1, "temperature": 2,
                      "prompt_template": 3, "seed": 4, "ordering": 5}

        # Main effects: mean over all other axes
        main_means = {}
        eff = {}
        for f in FACETS:
            ax = facet_axes[f]
            other_axes = tuple(i for i in range(6) if i != ax)
            mm = a.mean(axis=other_axes)  # shape: (n_f,)
            main_means[f] = mm
            n_per = N // nl[f]
            ss = float(n_per * ((mm - gm)**2).sum())
            dof = nl[f] - 1
            eff[f] = {"ss": ss, "df": dof, "ms": ss/dof if dof else 0.0}

        # 2-way interactions
        for fi, fj in combinations(FACETS, 2):
            ax_i = facet_axes[fi]
            ax_j = facet_axes[fj]
            other_axes = tuple(i for i in range(6) if i not in (ax_i, ax_j))
            cm = a.mean(axis=other_axes)  # shape: (n_fi, n_fj) or transposed
            # Ensure correct shape order
            if ax_i > ax_j:
                cm = cm.T
            # cm[i, j] = mean over other axes for (fi=i, fj=j)
            mi = main_means[fi]
            mj = main_means[fj]
            interaction = cm - mi[:, None] - mj[None, :] + gm
            n_per = N // (nl[fi] * nl[fj])
            ss = float(n_per * (interaction**2).sum())
            dof = (nl[fi]-1) * (nl[fj]-1)
            eff[f"{fi}:{fj}"] = {"ss": ss, "df": dof, "ms": ss/dof if dof else 0.0}

        ss_total = float(((a - gm)**2).sum())
        ss_model_sum = sum(e["ss"] for e in eff.values())
        ss_res = max(0.0, ss_total - ss_model_sum)
        df_res = N - 1 - sum(e["df"] for e in eff.values())
        eff["residual"] = {"ss": ss_res, "df": df_res, "ms": ss_res/df_res if df_res > 0 else 0.0}

        ms_res = eff["residual"]["ms"]
        vc = {}
        for fi, fj in combinations(FACETS, 2):
            key = f"{fi}:{fj}"
            coeff = prod(nl[f] for f in FACETS if f not in (fi, fj))
            vc[key] = max(0.0, (eff[key]["ms"] - ms_res) / coeff if coeff else 0.0)
        for fi in FACETS:
            coeff_main = prod(nl[f] for f in FACETS if f != fi)
            int_contrib = 0.0
            for fj in FACETS:
                if fj == fi: continue
                ik = f"{fi}:{fj}" if f"{fi}:{fj}" in vc else f"{fj}:{fi}"
                coeff_ij = prod(nl[f] for f in FACETS if f not in (fi, fj))
                int_contrib += coeff_ij * vc[ik]
            vc[fi] = max(0.0, (eff[fi]["ms"] - int_contrib - ms_res) / coeff_main if coeff_main else 0.0)
        vc["residual"] = ms_res
        return vc, nl

    # Verify: array-based Henderson I matches pandas-based
    vc_check, nl_check = henderson_i_array(arr)
    g_check, _, _, _ = g_item_calc(vc_check, nl_check)
    print(f"  Array Henderson I check: G_item={g_check:.6f}", flush=True)

    rng = np.random.RandomState(seed)
    g_samples = []
    t_start = time.time()
    for b in range(n_boot):
        if b % 100 == 0 and b > 0:
            elapsed = time.time() - t_start
            rate = b / elapsed
            eta = (n_boot - b) / rate
            print(f"  bootstrap {b}/{n_boot} ({rate:.1f} it/s, ETA {eta:.0f}s)", flush=True)
        boot_idx = rng.choice(n_items, size=n_items, replace=True)
        boot_arr = arr[boot_idx]
        vc_b, nl_b = henderson_i_array(boot_arr)
        g_b, _, _, _ = g_item_calc(vc_b, nl_b)
        g_samples.append(g_b)

    g_arr = np.array(g_samples)
    return {
        "mean": round(float(g_arr.mean()), 6),
        "std": round(float(g_arr.std()), 6),
        "ci_lower": round(float(np.percentile(g_arr, 2.5)), 6),
        "ci_upper": round(float(np.percentile(g_arr, 97.5)), 6),
        "n_boot": n_boot,
    }

# ============================================================
t0 = time.time()

# -------- Part A: 8-model MMLU G-study --------
print("=" * 60)
print("PART A: 8-model MMLU Cross-model G-study")
print("=" * 60, flush=True)

df_mmlu, acc_mmlu, nm_mmlu, models_mmlu, nobs_mmlu = load_benchmark("mmlu")
print(f"MMLU: {nobs_mmlu} obs, {nm_mmlu} models: {models_mmlu}", flush=True)

t1 = time.time()
vc_mmlu, nl_mmlu = henderson_i(df_mmlu)
tv_mmlu = sum(vc_mmlu.values())
g_mmlu, tau_mmlu, delta_mmlu, bd_mmlu = g_item_calc(vc_mmlu, nl_mmlu)
print(f"Henderson I done in {time.time()-t1:.1f}s", flush=True)

print(f"\nVariance components:")
for comp in sorted(vc_mmlu, key=lambda x: -vc_mmlu[x]):
    pct = vc_mmlu[comp] / tv_mmlu * 100
    if pct >= 0.01:
        print(f"  {comp:30s}: {vc_mmlu[comp]:.8f} ({pct:.4f}%)")
print(f"\nG_item = {g_mmlu:.6f}")
print(f"item_id% = {vc_mmlu['item_id']/tv_mmlu*100:.2f}%")
print(f"model:item_id% = {vc_mmlu.get('model:item_id',0)/tv_mmlu*100:.2f}%")

# Bootstrap CI using numpy array approach
print("\nBootstrapping G_item (500 iterations, numpy-accelerated)...", flush=True)
t_boot = time.time()
boot = bootstrap_g_numpy(df_mmlu, n_boot=500)
print(f"Bootstrap done in {time.time()-t_boot:.1f}s")
print(f"G_item = {boot['mean']:.4f} [{boot['ci_lower']:.4f}, {boot['ci_upper']:.4f}]")

print(f"\n4-model comparison:")
print(f"  item_id%:     41.55% -> {vc_mmlu['item_id']/tv_mmlu*100:.2f}%")
print(f"  model:item%:  32.81% -> {vc_mmlu.get('model:item_id',0)/tv_mmlu*100:.2f}%")
print(f"  G_item:       0.816  -> {g_mmlu:.4f}")

part_a = {
    "benchmark": "mmlu",
    "n_models": nm_mmlu,
    "models": models_mmlu,
    "n_obs": nobs_mmlu,
    "n_levels": {k: int(v) for k, v in nl_mmlu.items()},
    "accuracy": round(acc_mmlu, 6),
    "variance_components": {
        k: {"estimate": round(v, 10), "pct": round(v/tv_mmlu*100, 4)}
        for k, v in sorted(vc_mmlu.items(), key=lambda x: -x[1])
    },
    "total_variance": round(tv_mmlu, 10),
    "G_item": round(g_mmlu, 6),
    "sigma_tau": round(tau_mmlu, 10),
    "sigma_delta": round(delta_mmlu, 10),
    "bootstrap_ci": boot,
    "comparison_4model": {
        "4model": {"item_id_pct": 41.55, "model_item_pct": 32.81, "G_item": 0.816, "n_models": 4},
        "8model": {
            "item_id_pct": round(vc_mmlu["item_id"]/tv_mmlu*100, 4),
            "model_item_pct": round(vc_mmlu.get("model:item_id",0)/tv_mmlu*100, 4),
            "G_item": round(g_mmlu, 6),
            "n_models": nm_mmlu,
        },
    },
}

# -------- Compute all benchmarks for Part B & C --------
print("\n" + "=" * 60)
print("Computing Henderson I for all benchmarks...")
print("=" * 60, flush=True)

bm_results = {"mmlu": {"vc": vc_mmlu, "nl": nl_mmlu, "nm": nm_mmlu, "acc": acc_mmlu}}

for bm in ["arc", "hellaswag", "gsm8k", "math"]:
    t_bm = time.time()
    df_bm, acc_bm, nm_bm, models_bm, nobs_bm = load_benchmark(bm)
    print(f"{bm}: {nobs_bm} obs, {nm_bm} models: {models_bm}", flush=True)
    vc_bm, nl_bm = henderson_i(df_bm)
    tv_bm = sum(vc_bm.values())
    g_bm, _, _, _ = g_item_calc(vc_bm, nl_bm)
    print(f"  item_id%={vc_bm['item_id']/tv_bm*100:.2f}%, G_item={g_bm:.4f} ({time.time()-t_bm:.1f}s)", flush=True)
    bm_results[bm] = {"vc": vc_bm, "nl": nl_bm, "nm": nm_bm, "acc": acc_bm}

# -------- Part B: MC vs FF permutation test --------
print("\n" + "=" * 60)
print("PART B: MC vs FF Permutation Test")
print("=" * 60, flush=True)

mc_labels = ["MMLU", "ARC", "HellaSwag"]
ff_labels = ["GSM8K", "MATH"]

mc_item_pcts = []
ff_item_pcts = []
mc_meta = {}
ff_meta = {}

for label, bm_key in zip(mc_labels, ["mmlu", "arc", "hellaswag"]):
    r = bm_results[bm_key]
    tv = sum(r["vc"].values())
    pct = r["vc"]["item_id"] / tv * 100
    mc_item_pcts.append(pct)
    mc_meta[label] = {"item_id_pct": round(pct, 4), "n_models": r["nm"]}

for label, bm_key in zip(ff_labels, ["gsm8k", "math"]):
    r = bm_results[bm_key]
    tv = sum(r["vc"].values())
    pct = r["vc"]["item_id"] / tv * 100
    ff_item_pcts.append(pct)
    ff_meta[label] = {"item_id_pct": round(pct, 4), "n_models": r["nm"]}

print(f"MC group: {dict(zip(mc_labels, [f'{v:.2f}%' for v in mc_item_pcts]))}")
print(f"FF group: {dict(zip(ff_labels, [f'{v:.2f}%' for v in ff_item_pcts]))}")

obs_diff = np.mean(mc_item_pcts) - np.mean(ff_item_pcts)
print(f"Observed diff (MC mean - FF mean): {obs_diff:.2f}%")

all_vals = np.array(mc_item_pcts + ff_item_pcts)
n_mc = len(mc_item_pcts)
n_perm = 10000
rng = np.random.RandomState(42)

count_ge = 0
perm_diffs = np.empty(n_perm)
for i in range(n_perm):
    perm = rng.permutation(len(all_vals))
    d = all_vals[perm[:n_mc]].mean() - all_vals[perm[n_mc:]].mean()
    perm_diffs[i] = d
    if d >= obs_diff:
        count_ge += 1

p_value = count_ge / n_perm

mc_arr = np.array(mc_item_pcts)
ff_arr = np.array(ff_item_pcts)
n1, n2 = len(mc_arr), len(ff_arr)
pooled_var = ((n1-1)*mc_arr.var(ddof=1) + (n2-1)*ff_arr.var(ddof=1)) / (n1 + n2 - 2) if (n1+n2-2) > 0 else 0
cohens_d = obs_diff / np.sqrt(pooled_var) if pooled_var > 0 else float('inf')

boot_diffs = np.empty(10000)
for i in range(10000):
    mc_b = rng.choice(mc_item_pcts, size=n1, replace=True)
    ff_b = rng.choice(ff_item_pcts, size=n2, replace=True)
    boot_diffs[i] = np.mean(mc_b) - np.mean(ff_b)

ci_lo = float(np.percentile(boot_diffs, 2.5))
ci_hi = float(np.percentile(boot_diffs, 97.5))

print(f"\nPermutation test (one-sided, H1: MC > FF):")
print(f"  p-value = {p_value:.4f} ({n_perm} permutations)")
print(f"  Cohen's d = {cohens_d:.2f}")
print(f"  95% bootstrap CI for diff: [{ci_lo:.2f}%, {ci_hi:.2f}%]")

if p_value > 0.05:
    interp = (f"p={p_value:.3f} > 0.05: not statistically significant at alpha=0.05 "
              f"(n=5 benchmarks limits power). Cohen's d={cohens_d:.2f} indicates "
              f"a format-conditional variance structure with large effect size.")
else:
    interp = f"p={p_value:.4f}: statistically significant MC > FF item_id% difference."

print(f"  Interpretation: {interp}")

part_b = {
    "mc_group": mc_meta,
    "ff_group": ff_meta,
    "mc_item_id_pcts": [round(v, 4) for v in mc_item_pcts],
    "ff_item_id_pcts": [round(v, 4) for v in ff_item_pcts],
    "mc_mean": round(float(np.mean(mc_item_pcts)), 4),
    "ff_mean": round(float(np.mean(ff_item_pcts)), 4),
    "observed_diff": round(obs_diff, 4),
    "permutation_p_value": round(p_value, 4),
    "n_permutations": n_perm,
    "cohens_d": round(cohens_d, 4),
    "bootstrap_ci_diff": {"ci_lower": round(ci_lo, 4), "ci_upper": round(ci_hi, 4)},
    "interpretation": interp,
    "notes": {
        "hellaswag": f"{bm_results['hellaswag']['nm']}-model (OLMo/Yi HellaSwag not on this server)" if bm_results['hellaswag']['nm'] < 8 else "8-model",
    },
}

# -------- Part C: D-study projections --------
print("\n" + "=" * 60)
print("PART C: D-study Projections")
print("=" * 60, flush=True)

ITEM_COUNTS = [25, 50, 100, 150, 200, 300, 500, 1000]

part_c = {}
print(f"\n{'Benchmark':<12} {'n_mod':>5} {'G_curr':>7} {'item%':>7} {'n(G>=.80)':>10}")
print("-" * 50)

for bm in ["mmlu", "arc", "hellaswag", "gsm8k", "math"]:
    r = bm_results[bm]
    vc, nl, nm = r["vc"], r["nl"], r["nm"]
    tv = sum(vc.values())
    g, tau, delta, _ = g_item_calc(vc, nl)
    curve = d_study(vc, nl, ITEM_COUNTS)
    min_80 = find_min_items(vc, nl, 0.80)

    vals = list(curve.values())
    for i in range(len(vals)-1):
        assert vals[i] <= vals[i+1] + 1e-9, \
            f"{bm}: monotonicity failed at {ITEM_COUNTS[i]}->{ITEM_COUNTS[i+1]}: {vals[i]:.6f} > {vals[i+1]:.6f}"

    item_pct = vc["item_id"] / tv * 100
    mi_pct = vc.get("model:item_id", vc.get("item_id:model", 0.0)) / tv * 100
    print(f"{bm:<12} {nm:>5} {g:>7.4f} {item_pct:>6.2f}% {str(min_80):>10}")

    part_c[bm] = {
        "n_models": nm,
        "n_levels": {k: int(v) for k, v in nl.items()},
        "G_current": round(g, 6),
        "item_id_pct": round(item_pct, 4),
        "model_item_pct": round(mi_pct, 4),
        "sigma_tau": round(tau, 10),
        "sigma_delta": round(delta, 10),
        "d_study_curve": curve,
        "min_items_G_0.80": min_80,
        "variance_components": {
            k: {"estimate": round(v, 10), "pct": round(v/tv*100, 4)}
            for k, v in sorted(vc.items(), key=lambda x: -x[1])
        },
    }

for bm in ["mmlu", "arc", "hellaswag", "gsm8k", "math"]:
    print(f"\n  {bm} D-study (n_items -> G_item):")
    for ni, gv in part_c[bm]["d_study_curve"].items():
        marker = " *" if ni == part_c[bm]["min_items_G_0.80"] else ""
        print(f"    n={ni:>5d}: G={gv:.4f}{marker}")
    print(f"    min_items(G>=0.80) = {part_c[bm]['min_items_G_0.80']}")

# ===== Save =====
output = {
    "experiment": "exp-004",
    "analysis": "three_in_one_8model",
    "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
    "runtime_seconds": round(time.time() - t0, 1),
    "part_a_mmlu_gstudy": part_a,
    "part_b_permutation_test": part_b,
    "part_c_dstudy": part_c,
}

outfile = OUTPUT_DIR / "three_in_one_8model.json"
with open(outfile, "w") as f:
    json.dump(output, f, indent=2, default=str)

print(f"\n{'='*60}")
print(f"Saved -> {outfile}")
print(f"Total runtime: {time.time()-t0:.1f}s")
