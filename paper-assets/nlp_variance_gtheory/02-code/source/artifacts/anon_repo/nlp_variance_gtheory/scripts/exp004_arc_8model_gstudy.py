"""8-model Henderson I G-study for ARC benchmark (exp-004).

Facets: model, temperature, prompt_template, seed, ordering, item_id
+ all 2-way interactions. Residual absorbs >=3-way.
Bootstrap CI via item-level resampling (>=400 iterations).
"""

import json
import sys
import time
from itertools import combinations
from math import prod
from pathlib import Path

import numpy as np
import pandas as pd

sys.path.insert(0, ".")
from src.config.model_paths import normalize_model_name

FACETS = ["model", "temperature", "prompt_template", "seed", "ordering", "item_id"]


def load_arc_data(data_dir: str) -> pd.DataFrame:
    data_path = Path(data_dir)
    jsonl_files = sorted(data_path.glob("*_arc.jsonl"))
    if not jsonl_files:
        raise FileNotFoundError(f"No ARC JSONL files in {data_dir}")
    frames = []
    for f in jsonl_files:
        print(f"  Loading {f.name}...", flush=True)
        df = pd.read_json(f, lines=True)
        if "top_logprobs" in df.columns:
            df.drop(columns=["top_logprobs"], inplace=True)
        frames.append(df)
    df = pd.concat(frames, ignore_index=True)
    df["model"] = df["model"].map(normalize_model_name).fillna(df["model"])
    for f in FACETS:
        df[f] = df[f].astype(str)
    return df


def compute_henderson_i(df: pd.DataFrame, response: str, facets: list[str]):
    grand_mean = df[response].mean()
    N = len(df)
    n_levels = {f: df[f].nunique() for f in facets}

    effects = {}
    for f in facets:
        group_means = df.groupby(f, observed=True)[response].mean()
        n_per = N // n_levels[f]
        ss = float(n_per * ((group_means - grand_mean) ** 2).sum())
        df_eff = n_levels[f] - 1
        effects[f] = {"ss": ss, "df": df_eff, "ms": ss / df_eff if df_eff > 0 else 0.0}

    for fi, fj in combinations(facets, 2):
        cell_means = df.groupby([fi, fj], observed=True)[response].mean()
        main_fi = df.groupby(fi, observed=True)[response].mean()
        main_fj = df.groupby(fj, observed=True)[response].mean()
        n_per = N // (n_levels[fi] * n_levels[fj])
        ss = 0.0
        for (li, lj), cm in cell_means.items():
            interaction = cm - main_fi[li] - main_fj[lj] + grand_mean
            ss += n_per * interaction ** 2
        df_eff = (n_levels[fi] - 1) * (n_levels[fj] - 1)
        effects[f"{fi}:{fj}"] = {"ss": ss, "df": df_eff, "ms": ss / df_eff if df_eff > 0 else 0.0}

    ss_total = float(((df[response] - grand_mean) ** 2).sum())
    ss_model = sum(e["ss"] for e in effects.values())
    ss_res = max(0.0, ss_total - ss_model)
    df_res = N - 1 - sum(e["df"] for e in effects.values())
    effects["residual"] = {"ss": ss_res, "df": df_res, "ms": ss_res / df_res if df_res > 0 else 0.0}

    ms_res = effects["residual"]["ms"]
    vc = {}
    for fi, fj in combinations(facets, 2):
        key = f"{fi}:{fj}"
        coeff = prod(n_levels[f] for f in facets if f not in (fi, fj))
        raw = (effects[key]["ms"] - ms_res) / coeff if coeff > 0 else 0.0
        vc[key] = max(0.0, raw)

    for fi in facets:
        coeff_main = prod(n_levels[f] for f in facets if f != fi)
        interaction_contrib = 0.0
        for fj in facets:
            if fj == fi:
                continue
            int_key = f"{fi}:{fj}" if f"{fi}:{fj}" in vc else f"{fj}:{fi}"
            coeff_ij = prod(n_levels[f] for f in facets if f not in (fi, fj))
            interaction_contrib += coeff_ij * vc[int_key]
        raw = (effects[fi]["ms"] - interaction_contrib - ms_res) / coeff_main if coeff_main > 0 else 0.0
        vc[fi] = max(0.0, raw)

    vc["residual"] = ms_res
    return vc, n_levels, effects


def compute_g_item(vc: dict, n_levels: dict) -> tuple[float, float, float]:
    sigma_item = vc.get("item_id", 0.0)
    non_item_facets = [f for f in FACETS if f != "item_id"]

    sigma_delta = 0.0
    for comp, est in vc.items():
        if est == 0.0 or comp == "item_id":
            continue
        if comp == "residual":
            divisor = prod(n_levels[f] for f in non_item_facets)
            sigma_delta += est / divisor
            continue
        facets_in = set(comp.split(":"))
        if "item_id" not in facets_in:
            continue
        other = [f for f in facets_in if f != "item_id"]
        divisor = prod(n_levels[f] for f in other) if other else 1
        sigma_delta += est / divisor

    g = sigma_item / (sigma_item + sigma_delta) if (sigma_item + sigma_delta) > 0 else 0.0
    return g, sigma_item, sigma_delta


def d_study_curve(vc: dict, n_levels: dict, item_counts: list[int]) -> dict:
    non_item_facets = [f for f in FACETS if f != "item_id"]
    sigma_item = vc.get("item_id", 0.0)
    n_actual = n_levels["item_id"]

    non_item_error = 0.0
    for comp, est in vc.items():
        if est == 0.0 or comp == "item_id":
            continue
        if comp == "residual":
            divisor = prod(n_levels[f] for f in non_item_facets)
            non_item_error += est / divisor
            continue
        facets_in = set(comp.split(":"))
        if "item_id" not in facets_in:
            continue
        other = [f for f in facets_in if f != "item_id"]
        divisor = prod(n_levels[f] for f in other) if other else 1
        non_item_error += est / divisor

    curve = {}
    for ni in item_counts:
        ratio = n_actual / ni
        sigma_delta_ni = non_item_error * ratio
        g_ni = sigma_item / (sigma_item + sigma_delta_ni) if (sigma_item + sigma_delta_ni) > 0 else 0.0
        curve[ni] = round(g_ni, 6)
    return curve


def find_min_items_for_g(vc: dict, n_levels: dict, target_g: float, max_items: int = 2000) -> int | None:
    non_item_facets = [f for f in FACETS if f != "item_id"]
    sigma_item = vc.get("item_id", 0.0)
    n_actual = n_levels["item_id"]

    non_item_error = 0.0
    for comp, est in vc.items():
        if est == 0.0 or comp == "item_id":
            continue
        if comp == "residual":
            divisor = prod(n_levels[f] for f in non_item_facets)
            non_item_error += est / divisor
            continue
        facets_in = set(comp.split(":"))
        if "item_id" not in facets_in:
            continue
        other = [f for f in facets_in if f != "item_id"]
        divisor = prod(n_levels[f] for f in other) if other else 1
        non_item_error += est / divisor

    for ni in range(1, max_items + 1):
        ratio = n_actual / ni
        sigma_delta_ni = non_item_error * ratio
        g = sigma_item / (sigma_item + sigma_delta_ni) if (sigma_item + sigma_delta_ni) > 0 else 0.0
        if g >= target_g:
            return ni
    return None


def bootstrap_ci(df: pd.DataFrame, n_boot: int = 500, alpha: float = 0.05, seed: int = 42):
    rng = np.random.default_rng(seed)
    items = df["item_id"].unique()
    n_items = len(items)

    item_groups = {item: grp.drop(columns=["item_id"]).values for item, grp in df.groupby("item_id")}
    other_cols = [c for c in df.columns if c != "item_id"]
    rows_per_item = len(next(iter(item_groups.values())))

    boot_vc_list = []
    boot_g_list = []

    print(f"  Bootstrap ({n_boot} iterations, pre-grouped)...", flush=True)
    t0 = time.time()
    for b in range(n_boot):
        if (b + 1) % 50 == 0:
            elapsed = time.time() - t0
            print(f"    iter {b+1}/{n_boot} ({elapsed:.1f}s)", flush=True)
        sampled_items = rng.choice(items, size=n_items, replace=True)

        chunks = []
        new_ids = []
        for i, item in enumerate(sampled_items):
            chunks.append(item_groups[item])
            new_ids.extend([f"boot_{i}"] * rows_per_item)
        data = np.vstack(chunks)
        df_boot = pd.DataFrame(data, columns=other_cols)
        df_boot["item_id"] = new_ids
        for c in ["correct"]:
            df_boot[c] = pd.to_numeric(df_boot[c])

        vc_b, nl_b, _ = compute_henderson_i(df_boot, "correct", FACETS)
        g_b, _, _ = compute_g_item(vc_b, nl_b)
        boot_vc_list.append(vc_b)
        boot_g_list.append(g_b)

    boot_g = np.array(boot_g_list)
    ci_lo = float(np.percentile(boot_g, 100 * alpha / 2))
    ci_hi = float(np.percentile(boot_g, 100 * (1 - alpha / 2)))

    boot_vc_summaries = {}
    all_keys = set()
    for bvc in boot_vc_list:
        all_keys.update(bvc.keys())
    for k in all_keys:
        vals = [bvc.get(k, 0.0) for bvc in boot_vc_list]
        arr = np.array(vals)
        total_vars = [sum(bvc.values()) for bvc in boot_vc_list]
        pcts = [v / t * 100 if t > 0 else 0.0 for v, t in zip(vals, total_vars)]
        pct_arr = np.array(pcts)
        boot_vc_summaries[k] = {
            "estimate_ci_lo": float(np.percentile(arr, 100 * alpha / 2)),
            "estimate_ci_hi": float(np.percentile(arr, 100 * (1 - alpha / 2))),
            "pct_ci_lo": float(np.percentile(pct_arr, 100 * alpha / 2)),
            "pct_ci_hi": float(np.percentile(pct_arr, 100 * (1 - alpha / 2))),
        }

    elapsed = time.time() - t0
    print(f"  Bootstrap done ({elapsed:.1f}s)", flush=True)

    return {
        "G_item_ci_lo": round(ci_lo, 6),
        "G_item_ci_hi": round(ci_hi, 6),
        "G_item_se": round(float(np.std(boot_g)), 6),
        "n_boot": n_boot,
        "component_cis": boot_vc_summaries,
    }


def main():
    data_dir = "results/exp002"
    output_path = "results/exp004_8model_analysis/per_benchmark_gstudy_arc.json"

    t0 = time.time()
    print("Loading 8-model ARC data...", flush=True)
    df = load_arc_data(data_dir)
    df_arc = df[df["benchmark"] == "arc"].reset_index(drop=True) if "benchmark" in df.columns else df
    print(f"Loaded {len(df_arc)} records ({time.time()-t0:.1f}s)", flush=True)
    print(f"Models: {sorted(df_arc['model'].unique())}", flush=True)
    print(f"Items: {df_arc['item_id'].nunique()}", flush=True)

    n_models = df_arc["model"].nunique()
    if n_models != 8:
        print(f"WARNING: Expected 8 models, got {n_models}", flush=True)

    print("\nRunning Henderson I...", flush=True)
    vc, n_levels, effects = compute_henderson_i(df_arc, "correct", FACETS)
    total_var = sum(vc.values())
    g_item, sigma_tau, sigma_delta = compute_g_item(vc, n_levels)

    print(f"\n{'='*60}", flush=True)
    print(f"ARC 8-model Henderson I Results", flush=True)
    print(f"N = {len(df_arc)}, Grand mean = {df_arc['correct'].mean():.6f}", flush=True)
    print(f"G_item = {g_item:.6f}", flush=True)

    print(f"\n{'Component':<25} {'Estimate':>12} {'%Var':>8}", flush=True)
    print("-" * 50, flush=True)
    for k, v in sorted(vc.items(), key=lambda x: -x[1]):
        pct = v / total_var * 100 if total_var > 0 else 0
        print(f"{k:<25} {v:>12.8f} {pct:>7.2f}%", flush=True)

    print(f"\nRunning bootstrap CI...", flush=True)
    boot = bootstrap_ci(df_arc, n_boot=500, alpha=0.05)
    print(f"G_item 95% CI: [{boot['G_item_ci_lo']:.6f}, {boot['G_item_ci_hi']:.6f}]", flush=True)

    item_counts = [25, 50, 75, 100, 150, 200, 300, 500, 1000]
    d_curve = d_study_curve(vc, n_levels, item_counts)
    min_80 = find_min_items_for_g(vc, n_levels, 0.80)

    result = {
        "experiment": "exp-004",
        "analysis": "8model_henderson_i_gstudy_arc",
        "benchmark": "arc",
        "n_models": n_models,
        "n_observations": len(df_arc),
        "n_levels": {k: int(v) for k, v in n_levels.items()},
        "grand_mean_accuracy": round(float(df_arc["correct"].mean()), 6),
        "facets": FACETS,
        "variance_components": {
            k: {
                "estimate": round(v, 10),
                "pct": round(v / total_var * 100, 4) if total_var > 0 else 0.0,
                "pct_ci_lo": round(boot["component_cis"].get(k, {}).get("pct_ci_lo", 0), 4),
                "pct_ci_hi": round(boot["component_cis"].get(k, {}).get("pct_ci_hi", 0), 4),
            }
            for k, v in sorted(vc.items(), key=lambda x: -x[1])
        },
        "total_variance": round(total_var, 10),
        "G_item": round(g_item, 6),
        "G_item_ci_lo": boot["G_item_ci_lo"],
        "G_item_ci_hi": boot["G_item_ci_hi"],
        "G_item_se": boot["G_item_se"],
        "sigma_tau": round(sigma_tau, 10),
        "sigma_delta": round(sigma_delta, 10),
        "d_study_curve": d_curve,
        "min_items_G_0.80": min_80,
        "bootstrap": {"n_iterations": boot["n_boot"], "method": "item_level_resampling"},
        "models": sorted(df_arc["model"].unique().tolist()),
    }

    Path(output_path).parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(result, f, indent=2, default=str)

    print(f"\n{'='*60}", flush=True)
    print(f"SUMMARY", flush=True)
    print(f"  item_id%: {vc.get('item_id', 0) / total_var * 100:.2f}%", flush=True)
    print(f"  model:item_id%: {vc.get('model:item_id', 0) / total_var * 100:.2f}%", flush=True)
    print(f"  G_item: {g_item:.6f} [{boot['G_item_ci_lo']:.6f}, {boot['G_item_ci_hi']:.6f}]", flush=True)
    print(f"  min_items(G>=0.80): {min_80}", flush=True)
    print(f"  D-study: {d_curve}", flush=True)
    print(f"\nTotal runtime: {time.time()-t0:.1f}s", flush=True)
    print(f"-> {output_path}", flush=True)


if __name__ == "__main__":
    main()
