#!/usr/bin/env python3
"""Phase 2 defensive analyses: Bernoulli baseline + MMLU subsampling + LOBO stability.

Produces: results/exp004_8model_analysis/defensive_analyses.json
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
DATA_DIR = Path("results/exp002")
OUTPUT_DIR = Path("results/exp004_8model_analysis")

BENCHMARK_FILES = {
    "mmlu": ["llama_mmlu", "mistral_mmlu", "gemma_mmlu", "qwen_mmlu",
             "internlm_mmlu", "deepseek_mmlu", "olmo_mmlu", "yi_mmlu"],
    "arc": ["llama_arc", "mistral_arc", "gemma_arc", "qwen_arc",
            "internlm_arc", "deepseek_arc", "olmo_arc", "yi_arc"],
    "hellaswag": ["llama_hellaswag", "mistral_hellaswag", "gemma_hellaswag",
                  "qwen_hellaswag", "internlm_hellaswag", "deepseek_hellaswag"],
    "gsm8k": ["llama_gsm8k", "mistral_gsm8k", "gemma_gsm8k", "qwen_gsm8k",
              "internlm_gsm8k", "deepseek_gsm8k", "olmo_gsm8k", "yi_gsm8k"],
    "math": ["llama_math", "mistral_math", "gemma_math", "qwen_math",
             "internlm_math", "olmo_math", "yi_math"],
}

FORMAT_GROUP = {"mmlu": "MC", "arc": "MC", "hellaswag": "MC", "gsm8k": "FF", "math": "FF"}
KEEP_COLS = ["model", "temperature", "prompt_template", "seed", "ordering", "item_id", "correct"]


def load_benchmark(benchmark):
    frames = []
    for fname in BENCHMARK_FILES[benchmark]:
        fpath = DATA_DIR / f"{fname}.jsonl"
        if not fpath.exists():
            print(f"  SKIP {fpath}", flush=True)
            continue
        df = pd.read_json(fpath, lines=True)
        if "_placeholder" in df.columns:
            df = df[df["_placeholder"] != True]
            if len(df) == 0:
                print(f"  SKIP {fpath} (placeholder)", flush=True)
                continue
        cols = [c for c in KEEP_COLS if c in df.columns]
        frames.append(df[cols])
    df = pd.concat(frames, ignore_index=True)
    df["model"] = df["model"].map(normalize_model_name).fillna(df["model"])
    for f in FACETS:
        df[f] = df[f].astype(str)
    return df[KEEP_COLS]


def henderson_i(df, response="correct"):
    """Henderson Method I variance component estimation."""
    grand_mean = df[response].mean()
    N = len(df)
    n_levels = {f: df[f].nunique() for f in FACETS}
    effects = {}

    for f in FACETS:
        gm = df.groupby(f, observed=True)[response].mean()
        n_per = N // n_levels[f]
        ss = float(n_per * ((gm - grand_mean) ** 2).sum())
        dof = n_levels[f] - 1
        effects[f] = {"ss": ss, "df": dof, "ms": ss / dof if dof > 0 else 0.0}

    for fi, fj in combinations(FACETS, 2):
        cm = df.groupby([fi, fj], observed=True)[response].mean()
        mi = df.groupby(fi, observed=True)[response].mean()
        mj = df.groupby(fj, observed=True)[response].mean()
        n_per = N // (n_levels[fi] * n_levels[fj])
        ss = 0.0
        for (li, lj), val in cm.items():
            ss += n_per * (val - mi[li] - mj[lj] + grand_mean) ** 2
        dof = (n_levels[fi] - 1) * (n_levels[fj] - 1)
        effects[f"{fi}:{fj}"] = {"ss": ss, "df": dof, "ms": ss / dof if dof > 0 else 0.0}

    ss_total = float(((df[response] - grand_mean) ** 2).sum())
    ss_model_sum = sum(e["ss"] for e in effects.values())
    ss_res = max(0.0, ss_total - ss_model_sum)
    df_res = N - 1 - sum(e["df"] for e in effects.values())
    effects["residual"] = {"ss": ss_res, "df": df_res,
                           "ms": ss_res / df_res if df_res > 0 else 0.0}

    ms_res = effects["residual"]["ms"]
    vc = {}

    for fi, fj in combinations(FACETS, 2):
        key = f"{fi}:{fj}"
        coeff = prod(n_levels[f] for f in FACETS if f not in (fi, fj))
        vc[key] = max(0.0, (effects[key]["ms"] - ms_res) / coeff if coeff > 0 else 0.0)

    for fi in FACETS:
        coeff_main = prod(n_levels[f] for f in FACETS if f != fi)
        ic = 0.0
        for fj in FACETS:
            if fj == fi:
                continue
            int_key = f"{fi}:{fj}" if f"{fi}:{fj}" in vc else f"{fj}:{fi}"
            coeff_ij = prod(n_levels[f] for f in FACETS if f not in (fi, fj))
            ic += coeff_ij * vc.get(int_key, 0.0)
        vc[fi] = max(0.0, (effects[fi]["ms"] - ic - ms_res) / coeff_main
                      if coeff_main > 0 else 0.0)

    vc["residual"] = ms_res
    return vc, n_levels


def g_item_coeff(vc, n_levels):
    """G coefficient with item_id as object of measurement."""
    sigma_item = vc.get("item_id", 0.0)
    non_item = [f for f in FACETS if f != "item_id"]
    sigma_delta = 0.0
    for comp, est in vc.items():
        if est == 0.0 or comp == "item_id":
            continue
        if comp == "residual":
            sigma_delta += est / prod(n_levels[f] for f in non_item)
            continue
        parts = set(comp.split(":"))
        if "item_id" not in parts:
            continue
        other = [f for f in parts if f != "item_id"]
        sigma_delta += est / (prod(n_levels[f] for f in other) if other else 1)
    denom = sigma_item + sigma_delta
    return sigma_item / denom if denom > 0 else 0.0


def part_a_bernoulli(data):
    """Compare observed between-item variance to Bernoulli sampling expectation."""
    results = {}
    for bm, df in data.items():
        item_stats = df.groupby("item_id", observed=True)["correct"].agg(["mean", "count"])
        p_i = item_stats["mean"].values
        n_i = item_stats["count"].values
        n_med = int(np.median(n_i))

        var_between = float(np.var(p_i, ddof=1))
        grand_p = float(np.mean(p_i))
        expected = grand_p * (1 - grand_p) / n_med
        ratio = var_between / expected if expected > 0 else float("inf")
        mean_bern = float(np.mean(p_i * (1 - p_i)))

        results[bm] = {
            "n_items": int(len(p_i)),
            "n_conditions_per_item": n_med,
            "grand_mean_accuracy": round(grand_p, 6),
            "observed_between_item_var": round(var_between, 8),
            "bernoulli_expected_sampling_var": round(expected, 8),
            "ratio": round(ratio, 1),
            "mean_item_bernoulli_var_p1mp": round(mean_bern, 6),
        }
    return results


def part_b_subsampling(df_mmlu, sizes=(50, 100, 150), n_rep=100):
    """Subsample items from MMLU, rerun Henderson I, check stability."""
    items = sorted(df_mmlu["item_id"].unique())
    rng = np.random.default_rng(42)
    results = {}

    for ns in sizes:
        pcts, gs = [], []
        t0 = time.time()
        for i in range(n_rep):
            sampled = set(rng.choice(items, size=ns, replace=False))
            sub = df_mmlu[df_mmlu["item_id"].isin(sampled)].reset_index(drop=True)
            vc, nl = henderson_i(sub)
            tv = sum(vc.values())
            pcts.append(vc.get("item_id", 0) / tv * 100 if tv > 0 else 0)
            gs.append(g_item_coeff(vc, nl))
            if (i + 1) % 25 == 0:
                elapsed = time.time() - t0
                eta = elapsed / (i + 1) * (n_rep - i - 1)
                print(f"    n={ns}: {i+1}/{n_rep} ({elapsed:.0f}s, ~{eta:.0f}s left)",
                      flush=True)

        results[str(ns)] = {
            "n_items": ns,
            "n_repeats": n_rep,
            "item_id_pct_mean": round(float(np.mean(pcts)), 4),
            "item_id_pct_std": round(float(np.std(pcts)), 4),
            "item_id_pct_min": round(float(np.min(pcts)), 4),
            "item_id_pct_max": round(float(np.max(pcts)), 4),
            "G_item_mean": round(float(np.mean(gs)), 6),
            "G_item_std": round(float(np.std(gs)), 6),
            "G_item_min": round(float(np.min(gs)), 6),
            "G_item_max": round(float(np.max(gs)), 6),
        }

    vc_full, nl_full = henderson_i(df_mmlu)
    tv_full = sum(vc_full.values())
    results["200_reference"] = {
        "n_items": 200,
        "item_id_pct": round(vc_full.get("item_id", 0) / tv_full * 100
                             if tv_full > 0 else 0, 4),
        "G_item": round(g_item_coeff(vc_full, nl_full), 6),
    }
    return results


def part_c_lobo(bm_item_pct):
    """LOBO: check MC > FF item_id% holds when dropping each benchmark."""
    benchmarks = list(bm_item_pct.keys())

    def mc_ff_stats(bms):
        mc = [bm_item_pct[b] for b in bms if FORMAT_GROUP[b] == "MC"]
        ff = [bm_item_pct[b] for b in bms if FORMAT_GROUP[b] == "FF"]
        mc_m = float(np.mean(mc)) if mc else float("nan")
        ff_m = float(np.mean(ff)) if ff else float("nan")
        return mc_m, ff_m, mc_m - ff_m

    mc_full, ff_full, diff_full = mc_ff_stats(benchmarks)
    full_concl = "MC > FF" if diff_full > 0 else "FF >= MC"

    lobo = {}
    for drop in benchmarks:
        rem = [b for b in benchmarks if b != drop]
        mc_m, ff_m, diff = mc_ff_stats(rem)
        concl = "MC > FF" if diff > 0 else "FF >= MC"
        lobo[drop] = {
            "removed": drop,
            "removed_format": FORMAT_GROUP[drop],
            "remaining_mc": [b for b in rem if FORMAT_GROUP[b] == "MC"],
            "remaining_ff": [b for b in rem if FORMAT_GROUP[b] == "FF"],
            "mc_mean_item_id_pct": round(mc_m, 4),
            "ff_mean_item_id_pct": round(ff_m, 4),
            "diff_mc_minus_ff": round(diff, 4),
            "conclusion": concl,
            "stable": concl == full_concl,
        }

    return {
        "full_set": {
            "mc_benchmarks": [b for b in benchmarks if FORMAT_GROUP[b] == "MC"],
            "ff_benchmarks": [b for b in benchmarks if FORMAT_GROUP[b] == "FF"],
            "mc_mean_item_id_pct": round(mc_full, 4),
            "ff_mean_item_id_pct": round(ff_full, 4),
            "diff_mc_minus_ff": round(diff_full, 4),
            "conclusion": full_concl,
        },
        "lobo_results": lobo,
        "all_stable": all(v["stable"] for v in lobo.values()),
        "note_hellaswag": f"Removing HellaSwag (lowest MC item_id%): diff={lobo.get('hellaswag', {}).get('diff_mc_minus_ff')}",
        "note_math": f"Removing MATH (highest FF item_id%): diff={lobo.get('math', {}).get('diff_mc_minus_ff')}",
    }


def main():
    t0 = time.time()
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    print("Loading benchmark data...", flush=True)
    data = {}
    for bm in ["mmlu", "arc", "hellaswag", "gsm8k", "math"]:
        data[bm] = load_benchmark(bm)
        nm = data[bm]["model"].nunique()
        ni = data[bm]["item_id"].nunique()
        print(f"  {bm}: {len(data[bm]):,} rows, {nm} models, {ni} items", flush=True)

    print("\n=== Part A: Bernoulli p(1-p) Baseline ===", flush=True)
    pa = part_a_bernoulli(data)
    print(f"  {'Benchmark':<12} {'obs_var':>12} {'bern_var':>12} {'ratio':>8}", flush=True)
    for bm, r in pa.items():
        print(f"  {bm:<12} {r['observed_between_item_var']:>12.6f} "
              f"{r['bernoulli_expected_sampling_var']:>12.8f} {r['ratio']:>8.1f}x", flush=True)

    print("\n=== Henderson I per benchmark ===", flush=True)
    bm_vc = {}
    for bm in data:
        vc, nl = henderson_i(data[bm])
        tv = sum(vc.values())
        ip = vc.get("item_id", 0) / tv * 100 if tv > 0 else 0
        gi = g_item_coeff(vc, nl)
        bm_vc[bm] = {
            "item_id_pct": round(ip, 4),
            "G_item": round(gi, 6),
            "n_models": data[bm]["model"].nunique(),
            "n_items": data[bm]["item_id"].nunique(),
        }
        print(f"  {bm}: item_id% = {ip:.2f}, G_item = {gi:.4f}, "
              f"models = {bm_vc[bm]['n_models']}", flush=True)

    print("\n=== Part C: LOBO Stability ===", flush=True)
    bm_pct = {bm: v["item_id_pct"] for bm, v in bm_vc.items()}
    pc = part_c_lobo(bm_pct)
    f_ = pc["full_set"]
    print(f"  Full: MC mean={f_['mc_mean_item_id_pct']:.2f}%, "
          f"FF mean={f_['ff_mean_item_id_pct']:.2f}%, "
          f"diff={f_['diff_mc_minus_ff']:.2f}pp -> {f_['conclusion']}", flush=True)
    for drop, r in pc["lobo_results"].items():
        tag = " ***" if not r["stable"] else ""
        print(f"  Drop {drop:>12} ({r['removed_format']}): "
              f"MC={r['mc_mean_item_id_pct']:.2f} FF={r['ff_mean_item_id_pct']:.2f} "
              f"diff={r['diff_mc_minus_ff']:.2f} stable={r['stable']}{tag}", flush=True)
    print(f"  All stable: {pc['all_stable']}", flush=True)

    print("\n=== Part B: MMLU Subsampling (300 Henderson I calls) ===", flush=True)
    pb = part_b_subsampling(data["mmlu"])
    print(f"\n  {'n_items':>8} {'item_id%':>20} {'G_item':>20}", flush=True)
    for k, v in pb.items():
        if k == "200_reference":
            print(f"  {'200*':>8} {v['item_id_pct']:>20.2f} {v['G_item']:>20.4f}",
                  flush=True)
        else:
            print(f"  {k:>8} {v['item_id_pct_mean']:>8.2f} +/- {v['item_id_pct_std']:<8.2f}"
                  f"  {v['G_item_mean']:>8.4f} +/- {v['G_item_std']:<8.4f}", flush=True)

    output = {
        "experiment": "exp-004",
        "analysis": "phase2_defensive_analyses",
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
        "data_note": {
            "hellaswag": "6 models (OLMo/Yi missing)",
            "math": "7 models (DeepSeek excluded, placeholder data)",
            "other_benchmarks": "8 models",
        },
        "part_a_bernoulli_baseline": pa,
        "part_b_mmlu_subsampling": pb,
        "part_c_lobo_stability": pc,
        "per_benchmark_gstudy": bm_vc,
    }
    outpath = OUTPUT_DIR / "defensive_analyses.json"
    with open(outpath, "w") as f:
        json.dump(output, f, indent=2, default=str)

    print(f"\nTotal runtime: {time.time()-t0:.0f}s", flush=True)
    print(f"Saved -> {outpath}", flush=True)


if __name__ == "__main__":
    main()
