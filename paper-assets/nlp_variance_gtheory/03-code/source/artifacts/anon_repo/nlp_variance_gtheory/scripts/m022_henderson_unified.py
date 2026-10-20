"""
M022: Henderson Method I — Unified variance decomposition for ALL analyses.
Output: results/henderson_i_unified_numbers.json

Recomputes exp001 single-model and exp001b resampling (previously η²).
Pulls exp001 cross-model 4-model and exp002 per-benchmark from existing
Henderson I JSON files.
"""
import json
import time
from datetime import datetime, timezone
from itertools import combinations
from math import prod
from pathlib import Path

import numpy as np
import pandas as pd


def compute_henderson_i(df, response, facets):
    """Henderson Method I: SS -> EMS -> variance components σ²."""
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


def compute_g_item(vc, n_levels, facets):
    """G_item: object of measurement = item_id."""
    sigma_item = vc.get("item_id", 0.0)
    non_item_facets = [f for f in facets if f != "item_id"]

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


def d_study_curve(vc, n_levels, facets, item_counts):
    """D-study: vary n_items, hold other facets at actual levels."""
    non_item_facets = [f for f in facets if f != "item_id"]
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

    result = {}
    for ni in item_counts:
        ratio = n_actual / ni
        sigma_delta_ni = non_item_error * ratio
        g = sigma_item / (sigma_item + sigma_delta_ni) if (sigma_item + sigma_delta_ni) > 0 else 0.0
        result[str(ni)] = round(g, 6)
    return result


def find_min_items_g80(vc, n_levels, facets):
    non_item_facets = [f for f in facets if f != "item_id"]
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

    for ni in range(1, 2001):
        ratio = n_actual / ni
        sigma_delta_ni = non_item_error * ratio
        g = sigma_item / (sigma_item + sigma_delta_ni) if (sigma_item + sigma_delta_ni) > 0 else 0.0
        if g >= 0.80:
            return ni
    return None


def analyze_single_model():
    """exp001 single-model 6-facet Henderson I."""
    print("\n" + "=" * 60, flush=True)
    print("exp001: Single-model 6-facet (Llama-3.1-8B)", flush=True)

    df = pd.read_csv("results/analysis/llama_full.csv")
    for f in ["precision", "temperature", "prompt_template", "seed", "ordering", "item_id"]:
        df[f] = df[f].astype(str)
    print(f"  Loaded {len(df)} records", flush=True)

    facets = ["precision", "temperature", "prompt_template", "seed", "ordering", "item_id"]
    vc, n_levels, effects = compute_henderson_i(df, "correct", facets)
    total_var = sum(vc.values())
    g_item, sigma_tau, sigma_delta = compute_g_item(vc, n_levels, facets)

    vc_pct = {k: round(v / total_var * 100, 4) for k, v in sorted(vc.items(), key=lambda x: -x[1])}

    print(f"  item_id% = {vc_pct.get('item_id', 0):.4f}%", flush=True)
    print(f"  G_item = {g_item:.6f}", flush=True)

    item_counts = [25, 50, 75, 100, 150, 200, 300, 500]
    d_study = d_study_curve(vc, n_levels, facets, item_counts)
    min_80 = find_min_items_g80(vc, n_levels, facets)

    return {
        "data_source": "results/analysis/llama_full.csv",
        "n_records": len(df),
        "n_conditions": int(len(df) // n_levels["item_id"]),
        "facets": facets,
        "n_levels": {k: int(v) for k, v in n_levels.items()},
        "grand_mean": round(float(df["correct"].mean()), 6),
        "total_variance_sigma2": round(float(total_var), 10),
        "variance_components_pct": vc_pct,
        "variance_components_sigma2": {k: round(float(v), 10) for k, v in sorted(vc.items(), key=lambda x: -x[1])},
        "G_item": round(g_item, 6),
        "sigma_tau": round(sigma_tau, 10),
        "sigma_delta": round(sigma_delta, 10),
        "d_study": d_study,
        "min_items_G_0.80": min_80,
    }


def analyze_resampling():
    """exp001b resampling 5-facet Henderson I for 3 samples."""
    print("\n" + "=" * 60, flush=True)
    print("exp001b: Resampling 5-facet (3 samples)", flush=True)

    facets = ["temperature", "prompt_template", "seed", "ordering", "item_id"]
    sample_paths = {
        "sample_0": "results/exp001b/sample1/all_results.jsonl",
        "sample_7": "results/exp001b/sample2/all_results.jsonl",
        "sample_99": "results/exp001b/sample3/all_results.jsonl",
    }

    samples = {}
    item_pcts = []
    g_items = []

    for name, path in sample_paths.items():
        df = pd.read_json(path, lines=True)
        if "top_logprobs" in df.columns:
            df.drop(columns=["top_logprobs"], inplace=True)
        for f in facets:
            df[f] = df[f].astype(str)
        print(f"  {name}: {len(df)} records", flush=True)

        vc, n_levels, effects = compute_henderson_i(df, "correct", facets)
        total_var = sum(vc.values())
        g_item, sigma_tau, sigma_delta = compute_g_item(vc, n_levels, facets)

        vc_pct = {k: round(v / total_var * 100, 4) for k, v in sorted(vc.items(), key=lambda x: -x[1])}
        item_pct = vc_pct.get("item_id", 0.0)
        item_pcts.append(item_pct)
        g_items.append(g_item)

        print(f"    item_id% = {item_pct:.4f}, G_item = {g_item:.6f}", flush=True)

        d_study = d_study_curve(vc, n_levels, facets, [25, 50, 75, 100, 150, 200, 300, 500])
        min_80 = find_min_items_g80(vc, n_levels, facets)

        samples[name] = {
            "data_source": path,
            "n_records": len(df),
            "n_levels": {k: int(v) for k, v in n_levels.items()},
            "grand_mean": round(float(df["correct"].mean()), 6),
            "variance_components_pct": vc_pct,
            "item_id_pct": round(item_pct, 4),
            "G_item": round(g_item, 6),
            "sigma_tau": round(sigma_tau, 10),
            "sigma_delta": round(sigma_delta, 10),
            "d_study": d_study,
            "min_items_G_0.80": min_80,
        }

    mean_item = float(np.mean(item_pcts))
    std_item = float(np.std(item_pcts, ddof=1))
    cv_item = (std_item / mean_item * 100) if mean_item > 0 else 0
    mean_g = float(np.mean(g_items))
    std_g = float(np.std(g_items, ddof=1))
    cv_g = (std_g / mean_g * 100) if mean_g > 0 else 0

    return {
        "facets": facets,
        "samples": samples,
        "mean_item_id_pct": round(mean_item, 4),
        "std_item_id_pct": round(std_item, 4),
        "cv_item_id_pct": round(cv_item, 2),
        "mean_G_item": round(mean_g, 6),
        "std_G_item": round(std_g, 6),
        "cv_G_item": round(cv_g, 2),
    }


def pull_cross_model():
    """Pull existing Henderson I results for 4-model cross-model."""
    print("\n" + "=" * 60, flush=True)
    print("exp001 cross-model 4-model: pulling from existing Henderson I JSON", flush=True)

    with open("results/analysis/dataset_a4_gstudy.json") as f:
        data = json.load(f)

    vc_ems = data["variance_components_ems"]
    vc_pct = {k: round(v["pct"], 4) for k, v in sorted(vc_ems.items(), key=lambda x: -x[1]["pct"])}

    return {
        "data_source": "results/analysis/cross_model_4way_bf16.csv",
        "already_henderson_i": True,
        "n_records": data["n_observations"],
        "n_levels": data["n_levels"],
        "facets": list(data["n_levels"].keys()),
        "grand_mean": data["grand_mean"],
        "total_variance_sigma2": data["total_variance"],
        "variance_components_pct": vc_pct,
        "variance_components_sigma2": {k: round(v["estimate"], 10) for k, v in sorted(vc_ems.items(), key=lambda x: -x[1]["pct"])},
        "G_item": round(data["g_item"]["g"], 6),
        "sigma_tau": data["g_item"]["sigma_tau"],
        "sigma_delta": data["g_item"]["sigma_delta"],
    }


def pull_exp002():
    """Pull existing Henderson I results for exp002 per-benchmark."""
    print("\n" + "=" * 60, flush=True)
    print("exp002 per-benchmark: pulling from existing Henderson I JSON", flush=True)

    with open("results/analysis/exp002_per_benchmark_gstudy.json") as f:
        data = json.load(f)

    benchmarks = {}
    for bm_name, bm_data in data["benchmarks"].items():
        vc = bm_data["variance_components"]
        vc_pct = {k: round(v["pct"], 4) for k, v in sorted(vc.items(), key=lambda x: -x[1]["pct"])}
        benchmarks[bm_name] = {
            "n_observations": bm_data["n_observations"],
            "n_levels": bm_data["n_levels"],
            "grand_mean": bm_data["grand_mean_accuracy"],
            "item_id_pct": vc.get("item_id", {}).get("pct", 0),
            "model_pct": vc.get("model", {}).get("pct", 0),
            "model_item_pct": vc.get("model:item_id", {}).get("pct", 0),
            "prompt_pct": vc.get("prompt_template", {}).get("pct", 0),
            "G_item": bm_data["G_item"],
            "min_items_G_0.80": bm_data["min_items_G_0.80"],
            "variance_components_pct": vc_pct,
        }
        print(f"  {bm_name}: item_id={vc.get('item_id', {}).get('pct', 0):.2f}%, G_item={bm_data['G_item']:.6f}", flush=True)

    return {
        "already_henderson_i": True,
        "facets": data["facets"],
        "benchmarks": benchmarks,
    }


def main():
    t0 = time.time()

    exp001_single = analyze_single_model()
    exp001b_resamp = analyze_resampling()
    exp001_cross = pull_cross_model()
    exp002 = pull_exp002()

    output = {
        "method": "Henderson Method I",
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "note": "All percentages = sigma2_component / sum(sigma2_all_components). This is the single source of truth for all paper numbers.",
        "analyses": {
            "exp001_single_model_6facet": exp001_single,
            "exp001_cross_model_4model": exp001_cross,
            "exp001b_resampling": exp001b_resamp,
            "exp002_per_benchmark": exp002,
        },
    }

    out_path = Path("results/henderson_i_unified_numbers.json")
    out_path.parent.mkdir(parents=True, exist_ok=True)
    with open(out_path, "w") as f:
        json.dump(output, f, indent=2, default=str)

    print(f"\n{'=' * 60}", flush=True)
    print("SUMMARY: Henderson I unified numbers", flush=True)
    print(f"{'=' * 60}", flush=True)

    print(f"\nexp001 single-model 6-facet:", flush=True)
    print(f"  item_id% = {exp001_single['variance_components_pct'].get('item_id', 0)}", flush=True)
    print(f"  G_item = {exp001_single['G_item']}", flush=True)

    print(f"\nexp001 cross-model 4-model:", flush=True)
    print(f"  item_id% = {exp001_cross['variance_components_pct'].get('item_id', 0)}", flush=True)
    print(f"  G_item = {exp001_cross['G_item']}", flush=True)

    print(f"\nexp001b resampling:", flush=True)
    for sname, sdata in exp001b_resamp["samples"].items():
        print(f"  {sname}: item_id% = {sdata['item_id_pct']}, G_item = {sdata['G_item']}", flush=True)
    print(f"  mean item_id% = {exp001b_resamp['mean_item_id_pct']}, CV = {exp001b_resamp['cv_item_id_pct']}%", flush=True)
    print(f"  mean G_item = {exp001b_resamp['mean_G_item']}, CV = {exp001b_resamp['cv_G_item']}%", flush=True)

    print(f"\nexp002 per-benchmark:", flush=True)
    for bm, bdata in exp002["benchmarks"].items():
        print(f"  {bm}: item_id% = {bdata['item_id_pct']:.2f}, G_item = {bdata['G_item']:.6f}", flush=True)

    print(f"\n-> {out_path}", flush=True)
    print(f"Total runtime: {time.time()-t0:.1f}s", flush=True)


if __name__ == "__main__":
    main()
