"""Stratified vs Simple bootstrap comparison for MMLU.

Stratified bootstrap resamples within each of 10 subjects (20 items each),
preserving the natural subject structure. Compares CI widths with simple
(global) bootstrap.

Usage:
  cd .
  python scripts/stratified_bootstrap_mmlu.py
"""

import json, sys, time
from itertools import combinations
from math import prod
from pathlib import Path
from collections import defaultdict

import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from src.config.model_paths import normalize_model_name

FACETS = ["model", "temperature", "prompt_template", "seed", "ordering", "item_id"]
DIM_ORDER = ["model", "temperature", "prompt_template", "seed", "ordering", "item_id"]
ALL_MODELS = ["llama", "mistral", "qwen", "gemma", "internlm", "deepseek", "olmo", "yi"]
N_BOOT = 1000
SEED = 42


def load_mmlu_data(data_dir):
    dfs = []
    for prefix in ALL_MODELS:
        p = Path(data_dir) / f"{prefix}_mmlu.jsonl"
        if p.exists():
            d = pd.read_json(p, lines=True)
            dfs.append(d)
    df = pd.concat(dfs, ignore_index=True)
    df["model"] = df["model"].map(normalize_model_name)
    for f in FACETS:
        df[f] = df[f].astype(str)
    return df


def build_tensor(df, dim_levels):
    shape = [len(v) for v in dim_levels.values()]
    Y = np.full(shape, np.nan, dtype=np.float64)
    idx_maps = {name: {v: i for i, v in enumerate(vals)} for name, vals in dim_levels.items()}
    for _, row in df.iterrows():
        indices = tuple(idx_maps[name][row[name]] for name in dim_levels.keys())
        Y[indices] = row["correct"]
    n_nan = np.isnan(Y).sum()
    if n_nan > 0:
        print(f"  WARNING: {n_nan} NaN cells in tensor, filling with 0", flush=True)
        Y = np.nan_to_num(Y, nan=0.0)
    return Y


def henderson_i_from_tensor(Y, dim_sizes, dim_names=None):
    grand_mean = Y.mean()
    N = Y.size
    n_dims = len(dim_sizes)
    if dim_names is None:
        dim_names = DIM_ORDER[:n_dims]

    effects = {}
    for d, name in enumerate(dim_names):
        ax = tuple(i for i in range(n_dims) if i != d)
        gm = Y.mean(axis=ax)
        n_per = N // dim_sizes[d]
        ss = float(n_per * ((gm - grand_mean) ** 2).sum())
        df_eff = dim_sizes[d] - 1
        effects[name] = {"ss": ss, "df": df_eff, "ms": ss / df_eff if df_eff > 0 else 0.0}

    for (d1, n1), (d2, n2) in combinations(enumerate(zip(dim_names, dim_sizes)), 2):
        di, ni = d1, n1[1]
        dj, nj = d2, n2[1]
        name_i, name_j = n1[0], n2[0]
        ax = tuple(k for k in range(n_dims) if k != di and k != dj)
        cell_mean = Y.mean(axis=ax)
        main_i = Y.mean(axis=tuple(k for k in range(n_dims) if k != di))
        main_j = Y.mean(axis=tuple(k for k in range(n_dims) if k != dj))
        n_per = N // (ni * nj)
        interaction = cell_mean - main_i.reshape([-1 if k == 0 else 1 for k in range(cell_mean.ndim)]) \
                      - main_j.reshape([1 if k == 0 else -1 for k in range(cell_mean.ndim)]) + grand_mean
        ss = float(n_per * (interaction ** 2).sum())
        df_eff = (ni - 1) * (nj - 1)
        key = f"{name_i}:{name_j}"
        effects[key] = {"ss": ss, "df": df_eff, "ms": ss / df_eff if df_eff > 0 else 0.0}

    ss_total = float(((Y - grand_mean) ** 2).sum())
    ss_model = sum(e["ss"] for e in effects.values())
    ss_res = max(0.0, ss_total - ss_model)
    df_res = N - 1 - sum(e["df"] for e in effects.values())
    effects["residual"] = {"ss": ss_res, "df": df_res, "ms": ss_res / df_res if df_res > 0 else 0.0}

    ms_res = effects["residual"]["ms"]
    n_levels = dict(zip(dim_names, dim_sizes))
    vc = {}

    for fi, fj in combinations(dim_names, 2):
        key = f"{fi}:{fj}"
        coeff = prod(n_levels[f] for f in dim_names if f not in (fi, fj))
        raw = (effects[key]["ms"] - ms_res) / coeff if coeff > 0 else 0.0
        vc[key] = max(0.0, raw)

    for fi in dim_names:
        coeff_main = prod(n_levels[f] for f in dim_names if f != fi)
        ic = 0.0
        for fj in dim_names:
            if fj == fi:
                continue
            ik = f"{fi}:{fj}" if f"{fi}:{fj}" in vc else f"{fj}:{fi}"
            cij = prod(n_levels[f] for f in dim_names if f not in (fi, fj))
            ic += cij * vc[ik]
        raw = (effects[fi]["ms"] - ic - ms_res) / coeff_main if coeff_main > 0 else 0.0
        vc[fi] = max(0.0, raw)

    vc["residual"] = ms_res
    return vc, n_levels


def compute_g_item(vc, n_levels):
    tau = vc.get("item_id", 0.0)
    non_item_facets = [f for f in FACETS if f != "item_id"]
    delta = 0.0
    for comp, est in vc.items():
        if est == 0.0 or comp == "item_id":
            continue
        if comp == "residual":
            delta += est / prod(n_levels[f] for f in non_item_facets)
            continue
        parts = set(comp.split(":"))
        if "item_id" not in parts:
            continue
        other = [f for f in parts if f != "item_id"]
        delta += est / (prod(n_levels[f] for f in other) if other else 1)
    g = tau / (tau + delta) if (tau + delta) > 0 else 0.0
    return g, tau, delta


def bootstrap_run(Y, dim_sizes, rng, n_boot, resample_fn, label):
    boot_pcts = []
    boot_raws = []
    boot_g = []
    t0 = time.time()
    n_levels_ref = dict(zip(DIM_ORDER, dim_sizes))

    for b in range(n_boot):
        if b % 200 == 0:
            print(f"  [{label}] iter {b}/{n_boot} ({time.time()-t0:.1f}s)", flush=True)
        idx = resample_fn(rng)
        Y_b = Y[:, :, :, :, :, idx]
        vc_b, nl_b = henderson_i_from_tensor(Y_b, dim_sizes)
        tot_b = sum(vc_b.values())
        pct_b = {k: v / tot_b * 100 if tot_b > 0 else 0 for k, v in vc_b.items()}
        g_b, _, _ = compute_g_item(vc_b, nl_b)
        boot_pcts.append(pct_b)
        boot_raws.append(vc_b)
        boot_g.append(g_b)

    print(f"  [{label}] Done ({time.time()-t0:.1f}s)", flush=True)
    return boot_pcts, boot_raws, boot_g


def summarize_bootstrap(vc, boot_pcts, boot_raws, boot_g, g_item_point, total_var):
    all_keys = set()
    for bp in boot_pcts:
        all_keys.update(bp.keys())

    components = {}
    for key in sorted(all_keys):
        pct_vals = np.array([bp.get(key, 0) for bp in boot_pcts])
        raw_vals = np.array([br.get(key, 0) for br in boot_raws])
        point_pct = vc[key] / total_var * 100 if total_var > 0 else 0
        components[key] = {
            "pct": round(point_pct, 4),
            "ci_lower": round(float(np.percentile(pct_vals, 2.5)), 4),
            "ci_upper": round(float(np.percentile(pct_vals, 97.5)), 4),
            "ci_width": round(float(np.percentile(pct_vals, 97.5) - np.percentile(pct_vals, 2.5)), 4),
        }

    g_arr = np.array(boot_g)
    g_item_out = {
        "value": round(g_item_point, 6),
        "ci_lower": round(float(np.percentile(g_arr, 2.5)), 6),
        "ci_upper": round(float(np.percentile(g_arr, 97.5)), 6),
        "ci_width": round(float(np.percentile(g_arr, 97.5) - np.percentile(g_arr, 2.5)), 6),
    }

    return components, g_item_out


def main():
    data_dir = "results/exp002"
    t_total = time.time()

    print("Loading MMLU data...", flush=True)
    df = load_mmlu_data(data_dir)
    models = sorted(df["model"].unique().tolist())
    print(f"  {len(df)} records, {len(models)} models", flush=True)

    temps = sorted(df["temperature"].unique().tolist())
    prompts = sorted(df["prompt_template"].unique().tolist())
    seeds = sorted(df["seed"].unique().tolist())
    orderings = sorted(df["ordering"].unique().tolist())
    items = sorted(df["item_id"].unique().tolist())

    dim_levels = {"model": models, "temperature": temps, "prompt_template": prompts,
                  "seed": seeds, "ordering": orderings, "item_id": items}
    dim_sizes = [len(v) for v in dim_levels.values()]

    print(f"Building tensor {dim_sizes}...", flush=True)
    Y = build_tensor(df, dim_levels)
    n_levels = dict(zip(DIM_ORDER, dim_sizes))
    n_items = len(items)
    print(f"  shape={Y.shape}, mean={Y.mean():.6f}", flush=True)

    # Build subject-to-index mapping from item_ids
    # item_ids are like "abstract_algebra_81" — subject is everything before the last "_"
    subject_indices = defaultdict(list)
    for i, item_id in enumerate(items):
        parts = item_id.rsplit("_", 1)
        subject = parts[0]
        subject_indices[subject].append(i)

    subject_list = sorted(subject_indices.keys())
    print(f"\nSubject structure: {len(subject_list)} subjects", flush=True)
    for s in subject_list:
        print(f"  {s}: indices {subject_indices[s][0]}-{subject_indices[s][-1]} ({len(subject_indices[s])} items)", flush=True)

    # Verify structure
    for s, idxs in subject_indices.items():
        assert len(idxs) == 20, f"Subject {s} has {len(idxs)} items, expected 20"
    assert sum(len(v) for v in subject_indices.values()) == 200

    # Point estimate (same for both methods)
    print("\nHenderson I (point estimate)...", flush=True)
    vc, _ = henderson_i_from_tensor(Y, dim_sizes)
    total_var = sum(vc.values())
    g_item, sigma_tau, sigma_delta = compute_g_item(vc, n_levels)
    print(f"  G_item={g_item:.6f}, total_var={total_var:.10f}", flush=True)

    item_pct = vc["item_id"] / total_var * 100
    print(f"  item_id%={item_pct:.4f}", flush=True)

    # Prepare stratified index groups as numpy arrays
    strat_groups = [np.array(subject_indices[s]) for s in subject_list]

    def simple_resample(rng):
        return rng.choice(n_items, size=n_items, replace=True)

    def stratified_resample(rng):
        idx = np.empty(n_items, dtype=int)
        pos = 0
        for group in strat_groups:
            n = len(group)
            idx[pos:pos+n] = rng.choice(group, size=n, replace=True)
            pos += n
        return idx

    # Run both bootstraps with same seed
    print(f"\n=== Simple Bootstrap ({N_BOOT} iterations) ===", flush=True)
    rng_simple = np.random.default_rng(SEED)
    simple_pcts, simple_raws, simple_g = bootstrap_run(
        Y, dim_sizes, rng_simple, N_BOOT, simple_resample, "simple")

    print(f"\n=== Stratified Bootstrap ({N_BOOT} iterations) ===", flush=True)
    rng_strat = np.random.default_rng(SEED)
    strat_pcts, strat_raws, strat_g = bootstrap_run(
        Y, dim_sizes, rng_strat, N_BOOT, stratified_resample, "stratified")

    # Summarize
    simple_comps, simple_g_out = summarize_bootstrap(
        vc, simple_pcts, simple_raws, simple_g, g_item, total_var)
    strat_comps, strat_g_out = summarize_bootstrap(
        vc, strat_pcts, strat_raws, strat_g, g_item, total_var)

    # Compare CI widths
    g_simple_w = simple_g_out["ci_width"]
    g_strat_w = strat_g_out["ci_width"]
    g_change = (g_strat_w - g_simple_w) / g_simple_w * 100 if g_simple_w > 0 else 0

    item_simple_w = simple_comps["item_id"]["ci_width"]
    item_strat_w = strat_comps["item_id"]["ci_width"]
    item_change = (item_strat_w - item_simple_w) / item_simple_w * 100 if item_simple_w > 0 else 0

    print(f"\n{'='*60}", flush=True)
    print(f"COMPARISON: Simple vs Stratified Bootstrap", flush=True)
    print(f"{'='*60}", flush=True)
    print(f"\nG_item:", flush=True)
    print(f"  Simple:     {simple_g_out['value']:.6f} [{simple_g_out['ci_lower']:.6f}, {simple_g_out['ci_upper']:.6f}] width={g_simple_w:.6f}", flush=True)
    print(f"  Stratified: {strat_g_out['value']:.6f} [{strat_g_out['ci_lower']:.6f}, {strat_g_out['ci_upper']:.6f}] width={g_strat_w:.6f}", flush=True)
    print(f"  CI width change: {g_change:+.2f}%", flush=True)

    print(f"\nitem_id%:", flush=True)
    print(f"  Simple:     {simple_comps['item_id']['pct']:.4f}% [{simple_comps['item_id']['ci_lower']:.4f}, {simple_comps['item_id']['ci_upper']:.4f}] width={item_simple_w:.4f}", flush=True)
    print(f"  Stratified: {strat_comps['item_id']['pct']:.4f}% [{strat_comps['item_id']['ci_lower']:.4f}, {strat_comps['item_id']['ci_upper']:.4f}] width={item_strat_w:.4f}", flush=True)
    print(f"  CI width change: {item_change:+.2f}%", flush=True)

    # All components comparison
    print(f"\nAll components CI width comparison:", flush=True)
    print(f"  {'Component':<30} {'Simple':>10} {'Stratified':>10} {'Change':>10}", flush=True)
    print(f"  {'-'*60}", flush=True)
    for key in sorted(simple_comps.keys(), key=lambda x: -simple_comps[x]["pct"]):
        sw = simple_comps[key]["ci_width"]
        stw = strat_comps.get(key, {}).get("ci_width", 0)
        ch = (stw - sw) / sw * 100 if sw > 0 else 0
        if simple_comps[key]["pct"] >= 0.1:
            print(f"  {key:<30} {sw:>10.4f} {stw:>10.4f} {ch:>+9.2f}%", flush=True)

    conclusion = "stratified CI significantly narrower" if g_change < -10 else \
                 "stratified CI significantly wider" if g_change > 10 else \
                 "stratification has minimal impact on CI (<10% change)"

    output = {
        "benchmark": "mmlu",
        "n_subjects": len(subject_list),
        "subjects": subject_list,
        "items_per_subject": 20,
        "n_bootstrap": N_BOOT,
        "seed": SEED,
        "point_estimates": {
            "g_item": round(g_item, 6),
            "item_id_pct": round(item_pct, 4),
            "total_variance": round(total_var, 10),
        },
        "simple": {
            "g_item": simple_g_out,
            "item_id_pct": {
                "value": simple_comps["item_id"]["pct"],
                "ci_lower": simple_comps["item_id"]["ci_lower"],
                "ci_upper": simple_comps["item_id"]["ci_upper"],
                "ci_width": simple_comps["item_id"]["ci_width"],
            },
        },
        "stratified": {
            "g_item": strat_g_out,
            "item_id_pct": {
                "value": strat_comps["item_id"]["pct"],
                "ci_lower": strat_comps["item_id"]["ci_lower"],
                "ci_upper": strat_comps["item_id"]["ci_upper"],
                "ci_width": strat_comps["item_id"]["ci_width"],
            },
        },
        "comparison": {
            "g_item_ci_width_change_pct": round(g_change, 4),
            "item_id_pct_ci_width_change_pct": round(item_change, 4),
            "all_components": {},
            "conclusion": conclusion,
        },
        "runtime_seconds": round(time.time() - t_total, 1),
    }

    # Add all component comparisons
    for key in sorted(simple_comps.keys(), key=lambda x: -simple_comps[x]["pct"]):
        sw = simple_comps[key]["ci_width"]
        stw = strat_comps.get(key, {}).get("ci_width", 0)
        ch = (stw - sw) / sw * 100 if sw > 0 else 0
        output["comparison"]["all_components"][key] = {
            "simple_ci_width": sw,
            "stratified_ci_width": stw,
            "change_pct": round(ch, 4),
        }

    out_path = Path("results/exp004_8model_analysis/stratified_bootstrap_comparison.json")
    with open(out_path, "w") as f:
        json.dump(output, f, indent=2, default=str)
    print(f"\n=> {out_path}", flush=True)
    print(f"Total runtime: {time.time()-t_total:.1f}s", flush=True)


if __name__ == "__main__":
    main()
