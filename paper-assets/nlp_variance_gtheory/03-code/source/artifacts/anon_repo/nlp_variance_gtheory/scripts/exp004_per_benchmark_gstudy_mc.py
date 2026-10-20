"""
exp-004: 6-model per-benchmark Henderson I G-study for MC benchmarks.
Facets: model(6) x temperature(2) x prompt(6) x seed(6) x ordering(4) x item(200)
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
MC_BENCHMARKS = ["mmlu", "arc", "hellaswag"]
DATA_DIR = Path("results/exp002")
OUT_DIR = Path("results/exp004_8model_analysis")
N_BOOTSTRAP = 200


def load_benchmark(benchmark: str) -> pd.DataFrame:
    files = sorted(DATA_DIR.glob(f"*_{benchmark}.jsonl"))
    frames = [pd.read_json(f, lines=True) for f in files]
    df = pd.concat(frames, ignore_index=True)
    if "top_logprobs" in df.columns:
        df.drop(columns=["top_logprobs"], inplace=True)
    df["model"] = df["model"].map(normalize_model_name).fillna(df["model"])
    for f in FACETS:
        df[f] = df[f].astype(str)
    print(f"  {benchmark}: {len(df)} rows, {df['model'].nunique()} models", flush=True)
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


def compute_g_item(vc, n_levels):
    sigma_item = vc.get("item_id", 0.0)
    non_item_facets = [f for f in FACETS if f != "item_id"]
    sigma_delta = 0.0
    for key, est in vc.items():
        if key == "item_id" or est == 0.0:
            continue
        parts = key.split(":")
        if "item_id" in parts:
            other = [p for p in parts if p != "item_id"]
            divisor = prod(n_levels[o] for o in other) if other else 1
            sigma_delta += est / divisor
        elif key == "residual":
            divisor = prod(n_levels[f] for f in non_item_facets)
            sigma_delta += est / divisor
    g = sigma_item / (sigma_item + sigma_delta) if (sigma_item + sigma_delta) > 0 else 0.0
    return g, sigma_item, sigma_delta


def bootstrap_ci(df: pd.DataFrame, response: str, facets: list[str],
                 n_bootstrap=N_BOOTSTRAP, ci=0.95):
    rng = np.random.RandomState(42)
    items = sorted(df["item_id"].unique())
    n_items = len(items)

    # Pre-index: build dict of per-item dataframes (avoids repeated boolean indexing)
    item_frames = {}
    for item, grp in df.groupby("item_id", observed=True):
        item_frames[item] = grp

    boot_gs = []
    boot_vcs = []
    t0 = time.time()

    for b in range(n_bootstrap):
        sampled_items = rng.choice(items, size=n_items, replace=True)
        parts = []
        for i, item in enumerate(sampled_items):
            sub = item_frames[item].copy()
            sub["item_id"] = f"b{i}"
            parts.append(sub)
        df_boot = pd.concat(parts, ignore_index=True)
        try:
            vc_b, nl_b, _ = compute_henderson_i(df_boot, response, facets)
            g_b, _, _ = compute_g_item(vc_b, nl_b)
            boot_vcs.append(vc_b)
            boot_gs.append(g_b)
        except Exception:
            continue
        if (b + 1) % 50 == 0:
            elapsed = time.time() - t0
            rate = (b + 1) / elapsed
            remaining = (n_bootstrap - b - 1) / rate
            print(f"    bootstrap {b+1}/{n_bootstrap} ({elapsed:.0f}s elapsed, ~{remaining:.0f}s remaining)", flush=True)

    alpha = 1 - ci
    lo = alpha / 2 * 100
    hi = (1 - alpha / 2) * 100

    g_array = np.array(boot_gs)
    g_ci = (float(np.percentile(g_array, lo)), float(np.percentile(g_array, hi)))

    all_keys = set()
    for v in boot_vcs:
        all_keys.update(v.keys())
    vc_cis = {}
    for k in sorted(all_keys):
        vals = [v.get(k, 0.0) for v in boot_vcs]
        total = [sum(v.values()) for v in boot_vcs]
        pcts = [vals[i] / total[i] * 100 if total[i] > 0 else 0.0 for i in range(len(vals))]
        vc_cis[k] = {
            "pct_ci_lo": round(float(np.percentile(pcts, lo)), 4),
            "pct_ci_hi": round(float(np.percentile(pcts, hi)), 4),
        }
    return {"G_item_ci": [round(g_ci[0], 6), round(g_ci[1], 6)],
            "n_bootstrap": len(boot_gs), "vc_pct_cis": vc_cis}


def d_study_curve(vc, n_levels, item_counts):
    sigma_item = vc.get("item_id", 0.0)
    non_item_facets = [f for f in FACETS if f != "item_id"]
    n_actual = n_levels["item_id"]
    non_item_error = 0.0
    for key, est in vc.items():
        if key == "item_id" or est == 0.0:
            continue
        parts = key.split(":")
        if "item_id" in parts:
            other = [p for p in parts if p != "item_id"]
            divisor = prod(n_levels[o] for o in other) if other else 1
            non_item_error += est / divisor
        elif key == "residual":
            divisor = prod(n_levels[f] for f in non_item_facets)
            non_item_error += est / divisor
    curve = {}
    for ni in item_counts:
        ratio = n_actual / ni
        sigma_delta_ni = non_item_error * ratio
        g = sigma_item / (sigma_item + sigma_delta_ni) if (sigma_item + sigma_delta_ni) > 0 else 0.0
        curve[str(ni)] = round(g, 6)
    return curve


def find_min_items(vc, n_levels, target_g=0.80, max_items=2000):
    sigma_item = vc.get("item_id", 0.0)
    non_item_facets = [f for f in FACETS if f != "item_id"]
    n_actual = n_levels["item_id"]
    non_item_error = 0.0
    for key, est in vc.items():
        if key == "item_id" or est == 0.0:
            continue
        parts = key.split(":")
        if "item_id" in parts:
            other = [p for p in parts if p != "item_id"]
            divisor = prod(n_levels[o] for o in other) if other else 1
            non_item_error += est / divisor
        elif key == "residual":
            divisor = prod(n_levels[f] for f in non_item_facets)
            non_item_error += est / divisor
    for ni in range(1, max_items + 1):
        ratio = n_actual / ni
        sigma_delta_ni = non_item_error * ratio
        g = sigma_item / (sigma_item + sigma_delta_ni) if (sigma_item + sigma_delta_ni) > 0 else 0.0
        if g >= target_g:
            return ni
    return None


def analyze_benchmark(df_bm, benchmark):
    print(f"\n{'='*60}", flush=True)
    print(f"Benchmark: {benchmark} ({len(df_bm)} obs)", flush=True)

    t0 = time.time()
    vc, n_levels, effects = compute_henderson_i(df_bm, "correct", FACETS)
    total_var = sum(vc.values())
    g_item, sigma_tau, sigma_delta = compute_g_item(vc, n_levels)

    print(f"  Henderson I done in {time.time()-t0:.1f}s", flush=True)
    print(f"  G_item = {g_item:.6f}", flush=True)
    print(f"  item_id% = {vc.get('item_id', 0) / total_var * 100:.2f}%", flush=True)
    print(f"  model% = {vc.get('model', 0) / total_var * 100:.2f}%", flush=True)
    print(f"  model:item_id% = {vc.get('model:item_id', 0) / total_var * 100:.2f}%", flush=True)

    print(f"  Running bootstrap ({N_BOOTSTRAP} iterations)...", flush=True)
    t1 = time.time()
    boot = bootstrap_ci(df_bm, "correct", FACETS, n_bootstrap=N_BOOTSTRAP)
    print(f"  Bootstrap done in {time.time()-t1:.1f}s", flush=True)
    print(f"  G_item 95% CI: [{boot['G_item_ci'][0]:.4f}, {boot['G_item_ci'][1]:.4f}]", flush=True)

    item_counts = [25, 50, 75, 100, 150, 200, 300, 500, 1000]
    d_curve = d_study_curve(vc, n_levels, item_counts)
    min_80 = find_min_items(vc, n_levels, 0.80)

    return {
        "benchmark": benchmark,
        "n_observations": len(df_bm),
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
        "min_items_G_0.80": min_80,
        "bootstrap_95ci": boot,
    }


def main():
    t0 = time.time()
    OUT_DIR.mkdir(parents=True, exist_ok=True)

    # Load 4-model baseline
    baseline_path = Path("results/analysis/exp002_per_benchmark_gstudy.json")
    baseline = {}
    if baseline_path.exists():
        with open(baseline_path) as f:
            bl = json.load(f)
        for bm in MC_BENCHMARKS:
            if bm in bl.get("benchmarks", {}):
                r = bl["benchmarks"][bm]
                baseline[bm] = {
                    "n_models": r["n_levels"]["model"],
                    "G_item": r["G_item"],
                    "item_id_pct": r["variance_components"].get("item_id", {}).get("pct", 0),
                    "model_pct": r["variance_components"].get("model", {}).get("pct", 0),
                    "model_item_pct": r["variance_components"].get("model:item_id", {}).get("pct", 0),
                }

    results = {}
    for bm in MC_BENCHMARKS:
        df_bm = load_benchmark(bm)
        results[bm] = analyze_benchmark(df_bm, bm)

    comparison = {}
    for bm in MC_BENCHMARKS:
        r = results[bm]
        bl = baseline.get(bm, {})
        vc = r["variance_components"]
        comparison[bm] = {
            "6model_item_id_pct": vc.get("item_id", {}).get("pct", 0),
            "6model_model_pct": vc.get("model", {}).get("pct", 0),
            "6model_model_item_pct": vc.get("model:item_id", {}).get("pct", 0),
            "6model_G_item": r["G_item"],
            "4model_item_id_pct": bl.get("item_id_pct"),
            "4model_model_pct": bl.get("model_pct"),
            "4model_model_item_pct": bl.get("model_item_pct"),
            "4model_G_item": bl.get("G_item"),
        }

    output = {
        "experiment": "exp-004",
        "analysis": "6model_per_benchmark_henderson_i_gstudy_mc",
        "facets": FACETS,
        "n_models": 6,
        "benchmarks": results,
        "comparison_4model_vs_6model": comparison,
    }

    out_path = OUT_DIR / "per_benchmark_gstudy_mc.json"
    with open(out_path, "w") as f:
        json.dump(output, f, indent=2, default=lambda x: float(x) if hasattr(x, "item") else str(x))

    print(f"\n{'='*60}", flush=True)
    print("SUMMARY", flush=True)
    print(f"{'Benchmark':<12} {'item_id%':>10} {'model%':>8} {'m:item%':>10} {'G_item':>8} {'G_CI_lo':>8} {'G_CI_hi':>8} {'min_n(.80)':>11}", flush=True)
    for bm in MC_BENCHMARKS:
        r = results[bm]
        vc = r["variance_components"]
        item_pct = vc.get("item_id", {}).get("pct", 0)
        model_pct = vc.get("model", {}).get("pct", 0)
        mi_pct = vc.get("model:item_id", {}).get("pct", 0)
        ci = r["bootstrap_95ci"]["G_item_ci"]
        print(f"{bm:<12} {item_pct:>9.2f}% {model_pct:>7.2f}% {mi_pct:>9.2f}% {r['G_item']:>8.4f} {ci[0]:>8.4f} {ci[1]:>8.4f} {str(r['min_items_G_0.80']):>11}", flush=True)

    if comparison:
        print(f"\n4-model vs 6-model comparison:", flush=True)
        for bm in MC_BENCHMARKS:
            c = comparison[bm]
            d_item = c["6model_item_id_pct"] - (c["4model_item_id_pct"] or 0)
            d_model = c["6model_model_pct"] - (c["4model_model_pct"] or 0)
            d_g = c["6model_G_item"] - (c["4model_G_item"] or 0)
            print(f"  {bm}: item_id% {c.get('4model_item_id_pct','?'):.2f}→{c['6model_item_id_pct']:.2f} ({d_item:+.2f}), "
                  f"model% {c.get('4model_model_pct','?'):.2f}→{c['6model_model_pct']:.2f} ({d_model:+.2f}), "
                  f"G {c.get('4model_G_item','?'):.4f}→{c['6model_G_item']:.4f} ({d_g:+.4f})", flush=True)

    print(f"\nTotal runtime: {time.time()-t0:.1f}s", flush=True)
    print(f"-> {out_path}", flush=True)


if __name__ == "__main__":
    main()
