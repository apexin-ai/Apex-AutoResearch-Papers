"""DeepSeek leave-one-model-out cross-benchmark analysis (ARC, HellaSwag, GSM8K).

Drops DeepSeek-7B from 8-model data, recomputes Henderson I G-study
for each benchmark with 7 remaining models, compares with 8-model baseline.
"""

import json, sys, time
from itertools import combinations
from math import prod
from pathlib import Path

import numpy as np
import pandas as pd

sys.path.insert(0, ".")
sys.path.insert(0, "./scripts")
from src.config.model_paths import normalize_model_name
from hellaswag_2temp_gstudy_v2 import (
    load_local_hellaswag, decode_binary, reconstruct_df,
    OLMO_B64, YI_B64, OLMO_SUM, YI_SUM, OLMO_MD5, YI_MD5,
    OLMO_MODEL, YI_MODEL,
)

FACETS = ["model", "temperature", "prompt_template", "seed", "ordering", "item_id"]
DEEPSEEK_NAME = "DeepSeek-7B"
DATA_DIR = "./results/exp002"
HS_TEMPS = [0.0, 0.7]
HS_PTS = [1, 2, 3, 4, 5, 6]
HS_SEEDS = [42, 123, 456, 789, 1024, 2048]
HS_ORDS = [1, 2, 3, 4]
N_ITEMS = 200

REF_8MODEL = {
    "arc": {"item_id_pct": 37.8845, "model_item_pct": 33.7293, "residual_pct": 15.4448, "G_item": 0.891748},
    "hellaswag": {"item_id_pct": 34.2733, "model_item_pct": 36.0022, "residual_pct": 21.4128, "G_item": 0.871599},
    "gsm8k": {"item_id_pct": 16.8559, "model_item_pct": 14.5515, "residual_pct": 39.8941, "G_item": 0.862852},
}


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
    return vc, n_levels


def compute_g_item(vc, n_levels):
    sigma_item = vc.get("item_id", 0.0)
    non_item_facets = [f for f in FACETS if f != "item_id"]
    sigma_delta = 0.0
    for comp, est in vc.items():
        if est == 0.0 or comp == "item_id":
            continue
        if comp == "residual":
            sigma_delta += est / prod(n_levels[f] for f in non_item_facets)
            continue
        facets_in = set(comp.split(":"))
        if "item_id" not in facets_in:
            continue
        other = [f for f in facets_in if f != "item_id"]
        divisor = prod(n_levels[f] for f in other) if other else 1
        sigma_delta += est / divisor
    g = sigma_item / (sigma_item + sigma_delta) if (sigma_item + sigma_delta) > 0 else 0.0
    return g, sigma_item, sigma_delta


def load_benchmark(benchmark):
    data_path = Path(DATA_DIR)
    if benchmark == "hellaswag":
        df_local = load_local_hellaswag(DATA_DIR)
        df_local = df_local[df_local["benchmark"] == "hellaswag"].reset_index(drop=True)
        df_local["temperature"] = df_local["temperature"].apply(lambda x: round(float(x), 1))
        df_local = df_local[df_local["temperature"].isin(HS_TEMPS)].reset_index(drop=True)
        item_ids = sorted(df_local["item_id"].unique().tolist())
        n_bits = len(HS_TEMPS) * len(HS_PTS) * len(HS_SEEDS) * len(HS_ORDS) * N_ITEMS
        olmo_bits = decode_binary(OLMO_B64, n_bits, OLMO_SUM, OLMO_MD5)
        yi_bits = decode_binary(YI_B64, n_bits, YI_SUM, YI_MD5)
        df_olmo = reconstruct_df(OLMO_MODEL, olmo_bits, item_ids)
        df_yi = reconstruct_df(YI_MODEL, yi_bits, item_ids)
        for d in [df_olmo, df_yi]:
            d["model"] = d["model"].map(normalize_model_name).fillna(d["model"])
        df = pd.concat([df_local, df_olmo, df_yi], ignore_index=True)
        df["temperature"] = df["temperature"].apply(lambda x: round(float(x), 1))
    else:
        jsonl_files = sorted(data_path.glob(f"*_{benchmark}.jsonl"))
        frames = []
        for f in jsonl_files:
            df_tmp = pd.read_json(f, lines=True)
            if "top_logprobs" in df_tmp.columns:
                df_tmp.drop(columns=["top_logprobs"], inplace=True)
            if "_placeholder" in df_tmp.columns:
                df_tmp = df_tmp[df_tmp["_placeholder"] != True]
            frames.append(df_tmp)
            print(f"  {f.name}: {len(df_tmp)} rows", flush=True)
        df = pd.concat(frames, ignore_index=True)
        df["model"] = df["model"].map(normalize_model_name).fillna(df["model"])
    for f in FACETS:
        df[f] = df[f].astype(str)
    return df


def analyze_benchmark(benchmark):
    print(f"\n{'='*60}", flush=True)
    print(f"Benchmark: {benchmark}", flush=True)
    print(f"{'='*60}", flush=True)

    df = load_benchmark(benchmark)
    models = sorted(df["model"].unique())
    print(f"Loaded {len(df)} records, {len(models)} models: {models}", flush=True)

    assert DEEPSEEK_NAME in models, f"DeepSeek not found: {models}"

    df_7 = df[df["model"] != DEEPSEEK_NAME].reset_index(drop=True)
    remaining = sorted(df_7["model"].unique())
    print(f"After dropping {DEEPSEEK_NAME}: {len(df_7)} records, {len(remaining)} models", flush=True)

    vc, n_levels = compute_henderson_i(df_7, "correct", FACETS)
    total_var = sum(vc.values())
    g_item, sigma_tau, sigma_delta = compute_g_item(vc, n_levels)

    components = {}
    for k, v in sorted(vc.items(), key=lambda x: -x[1]):
        pct = v / total_var * 100 if total_var > 0 else 0.0
        components[k] = {"estimate": round(v, 10), "pct": round(pct, 4)}

    item_id_pct = components["item_id"]["pct"]
    model_item_pct = components["model:item_id"]["pct"]
    residual_pct = components["residual"]["pct"]
    ref = REF_8MODEL[benchmark]

    result = {
        "n_models_remaining": len(remaining),
        "remaining_models": remaining,
        "n_records": len(df_7),
        "n_levels": {k: int(v) for k, v in n_levels.items()},
        "grand_mean_accuracy": round(float(df_7["correct"].astype(float).mean()), 6),
        "components_7model": components,
        "total_variance": round(total_var, 10),
        "G_item_7model": round(g_item, 6),
        "sigma_tau": round(sigma_tau, 10),
        "sigma_delta": round(sigma_delta, 10),
        "ref_8model": ref,
        "delta": {
            "item_id_pct": round(item_id_pct - ref["item_id_pct"], 4),
            "model_item_pct": round(model_item_pct - ref["model_item_pct"], 4),
            "residual_pct": round(residual_pct - ref["residual_pct"], 4),
            "G_item": round(g_item - ref["G_item"], 6),
        },
    }

    print(f"  item_id:      {item_id_pct:>7.2f}%  (delta={result['delta']['item_id_pct']:+.2f}pp)", flush=True)
    print(f"  model:item_id:{model_item_pct:>7.2f}%  (delta={result['delta']['model_item_pct']:+.2f}pp)", flush=True)
    print(f"  residual:     {residual_pct:>7.2f}%  (delta={result['delta']['residual_pct']:+.2f}pp)", flush=True)
    print(f"  G_item:       {g_item:.6f}  (delta={result['delta']['G_item']:+.6f})", flush=True)
    return result


def main():
    t0 = time.time()
    results = {}
    for bm in ["arc", "hellaswag", "gsm8k"]:
        results[bm] = analyze_benchmark(bm)

    deltas_item = [abs(results[bm]["delta"]["item_id_pct"]) for bm in results]
    deltas_g = [abs(results[bm]["delta"]["G_item"]) for bm in results]
    max_d_item = max(deltas_item)
    max_d_g = max(deltas_g)

    if max_d_g < 0.02:
        conclusion = (f"Dropping DeepSeek-7B has minimal impact on G_item across all 3 benchmarks "
                      f"(max |delta_G| = {max_d_g:.4f} < 0.02), confirming measurement stability.")
    else:
        conclusion = f"Dropping DeepSeek-7B shows notable impact on some benchmarks (max |delta_G| = {max_d_g:.4f})."

    output = {
        "model_dropped": DEEPSEEK_NAME,
        "benchmarks": results,
        "summary": {
            "max_delta_item_id_pct": round(max_d_item, 4),
            "max_delta_G_item": round(max_d_g, 6),
            "conclusion": conclusion,
        },
        "runtime_seconds": round(time.time() - t0, 1),
    }

    out_path = Path("results/exp004_8model_analysis/deepseek_lomo_cross_benchmark.json")
    out_path.parent.mkdir(parents=True, exist_ok=True)
    with open(out_path, "w") as f:
        json.dump(output, f, indent=2)
    print(f"\n=> {out_path}")
    print(f"Total runtime: {time.time()-t0:.1f}s")


if __name__ == "__main__":
    main()
