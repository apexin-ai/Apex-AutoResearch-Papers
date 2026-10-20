"""exp-004: Per-benchmark Henderson I G-study for free-form benchmarks (GSM8K, MATH).

8 models for GSM8K, 7 for MATH (deepseek incomplete).
Facets: model, temperature, prompt_template, seed, ordering, item_id
Bootstrap CIs: 1000 resamples over items.
Optimized: precompute item-condition matrix for fast bootstrap.
"""

import json
import sys
import time
from itertools import combinations
from math import prod
from pathlib import Path

import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from src.config.model_paths import normalize_model_name

FACETS = ["model", "temperature", "prompt_template", "seed", "ordering", "item_id"]


def load_data(data_dir, benchmark):
    data_path = Path(data_dir)
    frames = []
    for f in sorted(data_path.glob("*.jsonl")):
        if benchmark not in f.name:
            continue
        if benchmark == "math" and f.name == "deepseek_math.jsonl":
            continue
        if benchmark == "math" and "deepseek" in f.name:
            continue
        df_tmp = pd.read_json(f, lines=True)
        if "_placeholder" in df_tmp.columns:
            df_tmp = df_tmp[df_tmp["_placeholder"] != True]
        if "benchmark" in df_tmp.columns:
            df_tmp = df_tmp[df_tmp["benchmark"] == benchmark]
        if len(df_tmp) > 0:
            frames.append(df_tmp)
            print(f"  {f.name}: {len(df_tmp)} rows", flush=True)
    df = pd.concat(frames, ignore_index=True)
    if "top_logprobs" in df.columns:
        df.drop(columns=["top_logprobs"], inplace=True)
    df["model"] = df["model"].map(normalize_model_name).fillna(df["model"])
    for f in FACETS:
        df[f] = df[f].astype(str)
    return df


def compute_henderson_i(df, response, facets):
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


def compute_g_item(vc, n_levels):
    sigma_item = vc.get("item_id", 0.0)
    sigma_delta = 0.0
    for key, est in vc.items():
        if key == "item_id":
            continue
        parts = key.split(":")
        other = [p for p in parts if p != "item_id"]
        if "item_id" not in parts and key != "residual":
            continue
        if key == "residual":
            divisor = prod(n_levels[f] for f in n_levels if f != "item_id")
        else:
            divisor = prod(n_levels[o] for o in other) if other else 1
        sigma_delta += est / divisor
    g = sigma_item / (sigma_item + sigma_delta) if (sigma_item + sigma_delta) > 0 else 0.0
    return g, sigma_item, sigma_delta


def d_study_curve(vc, n_levels, item_counts):
    sigma_item = vc.get("item_id", 0.0)
    n_actual = n_levels.get("item_id", 200)
    non_item_error = 0.0
    for key, est in vc.items():
        if key == "item_id":
            continue
        parts = key.split(":")
        other = [p for p in parts if p != "item_id"]
        if "item_id" not in parts and key != "residual":
            continue
        if key == "residual":
            divisor = prod(n_levels[f] for f in n_levels if f != "item_id")
        else:
            divisor = prod(n_levels[o] for o in other) if other else 1
        non_item_error += est / divisor
    curve = {}
    for ni in item_counts:
        ratio = n_actual / ni
        sigma_delta_ni = non_item_error * ratio
        g = sigma_item / (sigma_item + sigma_delta_ni) if (sigma_item + sigma_delta_ni) > 0 else 0.0
        curve[str(ni)] = round(g, 6)
    return curve


def fast_bootstrap_ci(df, facets, n_boot=1000, seed=42):
    """Optimized bootstrap: precompute per-item condition vectors."""
    rng = np.random.RandomState(seed)
    items = sorted(df["item_id"].unique())
    n_items = len(items)

    # Precompute: for each non-item facet combo, store item means
    # This avoids recreating DataFrames each iteration
    non_item_facets = [f for f in facets if f != "item_id"]

    # Build condition index: each unique combo of non-item facets
    cond_df = df.groupby(non_item_facets + ["item_id"], observed=True)["correct"].mean().reset_index()
    cond_pivot = cond_df.pivot_table(index="item_id", columns=non_item_facets, values="correct")

    # item_ids as ordered list matching pivot rows
    pivot_items = list(cond_pivot.index)
    item_to_idx = {item: i for i, item in enumerate(pivot_items)}
    data_matrix = cond_pivot.values  # shape: (n_items, n_conditions)

    # For each condition column, store its facet level mapping
    col_facet_levels = []
    for col in cond_pivot.columns:
        if isinstance(col, tuple):
            col_facet_levels.append(dict(zip(non_item_facets, col)))
        else:
            col_facet_levels.append({non_item_facets[0]: col})

    n_conditions = data_matrix.shape[1]
    n_levels_orig = {f: df[f].nunique() for f in facets}

    boot_results = []
    for b in range(n_boot):
        # Sample items with replacement
        sampled_indices = rng.choice(n_items, size=n_items, replace=True)
        boot_matrix = data_matrix[sampled_indices]  # (n_items, n_conditions)

        # Compute Henderson I from the matrix
        grand_mean = np.nanmean(boot_matrix)
        N = n_items * n_conditions

        # n_levels for bootstrap: item_id = n_items (same), others = original
        n_levels = dict(n_levels_orig)

        effects = {}
        vc = {}

        # Main effect of item_id: variance of item means
        item_means = np.nanmean(boot_matrix, axis=1)  # mean across conditions
        n_per_item = n_conditions
        ss_item = float(n_per_item * np.sum((item_means - grand_mean) ** 2))
        df_item = n_items - 1
        effects["item_id"] = {"ss": ss_item, "df": df_item, "ms": ss_item / df_item if df_item > 0 else 0}

        # Main effects of non-item facets
        for fi in non_item_facets:
            levels_fi = sorted(set(cl[fi] for cl in col_facet_levels))
            n_per = N // len(levels_fi)
            level_means = []
            for lv in levels_fi:
                col_mask = [j for j, cl in enumerate(col_facet_levels) if cl[fi] == lv]
                level_means.append(np.nanmean(boot_matrix[:, col_mask]))
            level_means = np.array(level_means)
            ss = float(n_per * np.sum((level_means - grand_mean) ** 2))
            df_eff = len(levels_fi) - 1
            effects[fi] = {"ss": ss, "df": df_eff, "ms": ss / df_eff if df_eff > 0 else 0}

        # Two-way interactions
        for fi, fj in combinations(facets, 2):
            if fi == "item_id" or fj == "item_id":
                # item_id × other_facet
                other = fi if fj == "item_id" else fj
                levels_other = sorted(set(cl[other] for cl in col_facet_levels))
                n_per = N // (n_items * len(levels_other))

                # item means (already computed)
                # other means
                other_means = {}
                for lv in levels_other:
                    col_mask = [j for j, cl in enumerate(col_facet_levels) if cl[other] == lv]
                    other_means[lv] = np.nanmean(boot_matrix[:, col_mask])

                ss = 0.0
                for i_idx in range(n_items):
                    for lv in levels_other:
                        col_mask = [j for j, cl in enumerate(col_facet_levels) if cl[other] == lv]
                        cell_mean = np.nanmean(boot_matrix[i_idx, col_mask])
                        interaction = cell_mean - item_means[i_idx] - other_means[lv] + grand_mean
                        ss += n_per * interaction ** 2

                df_eff = (n_items - 1) * (len(levels_other) - 1)
                key = f"item_id:{other}" if fi == "item_id" else f"{other}:item_id"
                # Normalize key order to match original
                if "item_id" in fi:
                    key = f"{fi}:{fj}"
                else:
                    key = f"{fi}:{fj}"
                effects[key] = {"ss": ss, "df": df_eff, "ms": ss / df_eff if df_eff > 0 else 0}
            else:
                # two non-item facets
                levels_fi = sorted(set(cl[fi] for cl in col_facet_levels))
                levels_fj = sorted(set(cl[fj] for cl in col_facet_levels))
                n_per = N // (len(levels_fi) * len(levels_fj))

                fi_means = {}
                for lv in levels_fi:
                    col_mask = [j for j, cl in enumerate(col_facet_levels) if cl[fi] == lv]
                    fi_means[lv] = np.nanmean(boot_matrix[:, col_mask])
                fj_means = {}
                for lv in levels_fj:
                    col_mask = [j for j, cl in enumerate(col_facet_levels) if cl[fj] == lv]
                    fj_means[lv] = np.nanmean(boot_matrix[:, col_mask])

                ss = 0.0
                for li in levels_fi:
                    for lj in levels_fj:
                        col_mask = [j for j, cl in enumerate(col_facet_levels) if cl[fi] == li and cl[fj] == lj]
                        cell_mean = np.nanmean(boot_matrix[:, col_mask])
                        interaction = cell_mean - fi_means[li] - fj_means[lj] + grand_mean
                        ss += n_per * interaction ** 2
                df_eff = (len(levels_fi) - 1) * (len(levels_fj) - 1)
                effects[f"{fi}:{fj}"] = {"ss": ss, "df": df_eff, "ms": ss / df_eff if df_eff > 0 else 0}

        # Residual
        ss_total = float(np.sum((boot_matrix - grand_mean) ** 2))
        ss_model_sum = sum(e["ss"] for e in effects.values())
        ss_res = max(0.0, ss_total - ss_model_sum)
        df_res = N - 1 - sum(e["df"] for e in effects.values())
        effects["residual"] = {"ss": ss_res, "df": df_res, "ms": ss_res / df_res if df_res > 0 else 0}

        # Extract variance components (same logic as compute_henderson_i)
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

        total = sum(vc.values())
        pcts = {k: v / total * 100 if total > 0 else 0 for k, v in vc.items()}
        g_boot, _, _ = compute_g_item(vc, n_levels)
        boot_results.append({"pcts": pcts, "g_item": g_boot})

        if (b + 1) % 100 == 0:
            print(f"    bootstrap {b+1}/{n_boot}", flush=True)

    # Compute CIs
    ci = {}
    all_keys = set()
    for br in boot_results:
        all_keys.update(br["pcts"].keys())
    for key in sorted(all_keys):
        vals = [br["pcts"].get(key, 0) for br in boot_results]
        ci[key] = {
            "mean": round(float(np.mean(vals)), 4),
            "ci_2.5": round(float(np.percentile(vals, 2.5)), 4),
            "ci_97.5": round(float(np.percentile(vals, 97.5)), 4),
        }
    g_vals = [br["g_item"] for br in boot_results]
    ci["G_item"] = {
        "mean": round(float(np.mean(g_vals)), 6),
        "ci_2.5": round(float(np.percentile(g_vals, 2.5)), 6),
        "ci_97.5": round(float(np.percentile(g_vals, 97.5)), 6),
    }
    return ci


def analyze_benchmark(df_bm, benchmark):
    print(f"\n{'='*60}", flush=True)
    print(f"Benchmark: {benchmark} ({len(df_bm)} obs)", flush=True)
    print(f"Models: {sorted(df_bm['model'].unique())}", flush=True)
    print(f"Items: {df_bm['item_id'].nunique()}", flush=True)

    vc, n_levels, effects = compute_henderson_i(df_bm, "correct", FACETS)
    total_var = sum(vc.values())
    g_item, sigma_tau, sigma_delta = compute_g_item(vc, n_levels)

    print(f"  G_item = {g_item:.6f}", flush=True)
    print(f"  item_id% = {vc.get('item_id', 0) / total_var * 100:.2f}%", flush=True)
    print(f"  model% = {vc.get('model', 0) / total_var * 100:.2f}%", flush=True)
    print(f"  prompt_template% = {vc.get('prompt_template', 0) / total_var * 100:.2f}%", flush=True)

    item_counts = [25, 50, 75, 100, 150, 200, 300, 500, 1000]
    d_curve = d_study_curve(vc, n_levels, item_counts)

    print(f"\n  Running 1000-resample bootstrap...", flush=True)
    t_boot = time.time()
    ci = fast_bootstrap_ci(df_bm, FACETS, n_boot=1000)
    print(f"  Bootstrap done in {time.time()-t_boot:.1f}s", flush=True)

    return {
        "benchmark": benchmark,
        "n_observations": len(df_bm),
        "n_models": int(df_bm["model"].nunique()),
        "models": sorted(df_bm["model"].unique().tolist()),
        "n_levels": {k: int(v) for k, v in n_levels.items()},
        "grand_mean_accuracy": round(float(df_bm["correct"].mean()), 6),
        "variance_components": {
            k: {"estimate": round(v, 10), "pct": round(v / total_var * 100, 4) if total_var > 0 else 0.0}
            for k, v in sorted(vc.items(), key=lambda x: -x[1])
        },
        "total_variance": round(total_var, 10),
        "G_item": round(g_item, 6),
        "sigma_tau": round(sigma_tau, 10),
        "sigma_delta": round(sigma_delta, 10),
        "d_study_curve": d_curve,
        "bootstrap_ci_95": ci,
    }


def main():
    t0 = time.time()
    data_dir = "results/exp002"
    results = {}

    for benchmark in ["gsm8k", "math"]:
        print(f"\nLoading {benchmark} data...", flush=True)
        df = load_data(data_dir, benchmark)
        print(f"  Total: {len(df)} rows, {df['model'].nunique()} models", flush=True)
        results[benchmark] = analyze_benchmark(df, benchmark)

    gsm8k_r = results["gsm8k"]
    math_r = results["math"]
    gsm8k_item = gsm8k_r["variance_components"].get("item_id", {}).get("pct", 0)
    math_item = math_r["variance_components"].get("item_id", {}).get("pct", 0)
    gsm8k_model = gsm8k_r["variance_components"].get("model", {}).get("pct", 0)
    math_model = math_r["variance_components"].get("model", {}).get("pct", 0)
    gsm8k_prompt = gsm8k_r["variance_components"].get("prompt_template", {}).get("pct", 0)
    math_prompt = math_r["variance_components"].get("prompt_template", {}).get("pct", 0)

    comparison = {
        "gsm8k_vs_math": {
            "item_id_pct": {"gsm8k": gsm8k_item, "math": math_item, "diff_pp": round(gsm8k_item - math_item, 2)},
            "model_pct": {"gsm8k": gsm8k_model, "math": math_model},
            "prompt_pct": {"gsm8k": gsm8k_prompt, "math": math_prompt},
            "G_item": {"gsm8k": gsm8k_r["G_item"], "math": math_r["G_item"]},
            "both_methodology_dominated": gsm8k_item < 20 and math_item < 20,
        }
    }

    output = {
        "experiment": "exp-004",
        "analysis": "per_benchmark_henderson_i_gstudy_freeform",
        "facets": FACETS,
        "note_math": "DeepSeek excluded from MATH (incomplete data: 37400/57600 lines)",
        "benchmarks": results,
        "comparison": comparison,
    }

    out_dir = Path("results/exp004_8model_analysis")
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / "per_benchmark_gstudy_ff.json"
    with open(out_path, "w") as f:
        json.dump(output, f, indent=2, default=str)

    print(f"\n{'='*60}", flush=True)
    print("SUMMARY", flush=True)
    print(f"{'Benchmark':<10} {'#mod':>4} {'item%':>8} {'model%':>8} {'prompt%':>8} {'G_item':>8}", flush=True)
    for bm in ["gsm8k", "math"]:
        r = results[bm]
        ip = r["variance_components"].get("item_id", {}).get("pct", 0)
        mp = r["variance_components"].get("model", {}).get("pct", 0)
        pp = r["variance_components"].get("prompt_template", {}).get("pct", 0)
        print(f"{bm:<10} {r['n_models']:>4} {ip:>7.2f}% {mp:>7.2f}% {pp:>7.2f}% {r['G_item']:>8.4f}", flush=True)

    print(f"\nBoth methodology-dominated (item_id% < 20%)? {comparison['gsm8k_vs_math']['both_methodology_dominated']}", flush=True)
    print(f"\nTotal runtime: {time.time()-t0:.1f}s", flush=True)
    print(f"-> {out_path}", flush=True)


if __name__ == "__main__":
    main()
