"""Leave-One-Model-Out (LOMO) analysis: 8 models × 5 benchmarks.

For each benchmark, remove each model one at a time, rerun Henderson I
6-facet variance decomposition on the remaining 7 models, and measure
stability of G_item.

Usage:
  cd .
  python scripts/lomo_8x5.py
"""

import json, sys, time
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from scripts.exp004_bootstrap_ci_all import (
    FACETS, DIM_ORDER, BENCHMARKS,
    load_benchmark_data, build_tensor, henderson_i_from_tensor, compute_g_item,
)

DATA_DIR = "results/exp002"
OUT_PATH = Path("results/exp004_8model_analysis/lomo_8x5_full.json")


def run_lomo_benchmark(data_dir, benchmark):
    t0 = time.time()
    print(f"\n{'='*60}", flush=True)
    print(f"LOMO: {benchmark}", flush=True)
    print(f"{'='*60}", flush=True)

    df = load_benchmark_data(data_dir, benchmark)
    models = sorted(df["model"].unique().tolist())
    print(f"  {len(df)} records, {len(models)} models: {models}", flush=True)

    temps = sorted(df["temperature"].unique().tolist())
    prompts = sorted(df["prompt_template"].unique().tolist())
    seeds = sorted(df["seed"].unique().tolist())
    orderings = sorted(df["ordering"].unique().tolist())
    items = sorted(df["item_id"].unique().tolist())

    dim_levels_full = {
        "model": models, "temperature": temps, "prompt_template": prompts,
        "seed": seeds, "ordering": orderings, "item_id": items,
    }
    dim_sizes_full = [len(v) for v in dim_levels_full.values()]

    print(f"  Full tensor {dim_sizes_full}", flush=True)
    Y_full = build_tensor(df, dim_levels_full)
    vc_full, nl_full = henderson_i_from_tensor(Y_full, dim_sizes_full)
    total_full = sum(vc_full.values())
    g_full, tau_full, delta_full = compute_g_item(vc_full, nl_full)
    item_pct_full = vc_full.get("item_id", 0) / total_full * 100 if total_full > 0 else 0
    model_item_pct_full = vc_full.get("model:item_id", 0) / total_full * 100 if total_full > 0 else 0

    print(f"  Full G_item={g_full:.6f}, item%={item_pct_full:.2f}, model:item%={model_item_pct_full:.2f}", flush=True)

    full_info = {
        "item_id_pct": round(item_pct_full, 4),
        "model_item_pct": round(model_item_pct_full, 4),
        "g_item": round(g_full, 6),
        "total_variance": round(total_full, 10),
        "n_models": len(models),
    }

    lomo_results = []
    for model_to_remove in models:
        df_sub = df[df["model"] != model_to_remove].copy()
        sub_models = sorted(df_sub["model"].unique().tolist())
        sub_temps = sorted(df_sub["temperature"].unique().tolist())
        sub_prompts = sorted(df_sub["prompt_template"].unique().tolist())
        sub_seeds = sorted(df_sub["seed"].unique().tolist())
        sub_orderings = sorted(df_sub["ordering"].unique().tolist())
        sub_items = sorted(df_sub["item_id"].unique().tolist())

        dim_levels_sub = {
            "model": sub_models, "temperature": sub_temps,
            "prompt_template": sub_prompts, "seed": sub_seeds,
            "ordering": sub_orderings, "item_id": sub_items,
        }
        dim_sizes_sub = [len(v) for v in dim_levels_sub.values()]

        Y_sub = build_tensor(df_sub, dim_levels_sub)
        vc_sub, nl_sub = henderson_i_from_tensor(Y_sub, dim_sizes_sub)
        total_sub = sum(vc_sub.values())
        g_sub, tau_sub, delta_sub = compute_g_item(vc_sub, nl_sub)

        item_pct_sub = vc_sub.get("item_id", 0) / total_sub * 100 if total_sub > 0 else 0
        model_item_pct_sub = vc_sub.get("model:item_id", 0) / total_sub * 100 if total_sub > 0 else 0

        delta_g = g_sub - g_full
        delta_item = item_pct_sub - item_pct_full

        vc_pcts = {}
        for k, v in sorted(vc_sub.items(), key=lambda x: -x[1]):
            pct = v / total_sub * 100 if total_sub > 0 else 0
            if pct >= 0.01:
                vc_pcts[k] = round(pct, 4)

        entry = {
            "removed": model_to_remove,
            "item_id_pct": round(item_pct_sub, 4),
            "model_item_pct": round(model_item_pct_sub, 4),
            "g_item": round(g_sub, 6),
            "delta_g": round(delta_g, 6),
            "delta_item_pct": round(delta_item, 4),
            "total_variance": round(total_sub, 10),
            "variance_components_pct": vc_pcts,
        }
        lomo_results.append(entry)
        print(f"  -{model_to_remove:<20} G={g_sub:.6f} (ΔG={delta_g:+.6f})  item%={item_pct_sub:.2f}  m:i%={model_item_pct_sub:.2f}", flush=True)

    g_values = [r["g_item"] for r in lomo_results]
    g_range = max(g_values) - min(g_values)
    g_sd = float(np.std(g_values, ddof=0))
    g_mean = float(np.mean(g_values))
    g_cv = g_sd / g_mean if g_mean > 0 else 0
    max_abs_delta = max(abs(r["delta_g"]) for r in lomo_results)
    max_delta_model = max(lomo_results, key=lambda r: abs(r["delta_g"]))["removed"]

    stability = {
        "g_range": round(g_range, 6),
        "g_sd": round(g_sd, 6),
        "g_mean": round(g_mean, 6),
        "g_cv": round(g_cv, 6),
        "max_abs_delta_g": round(max_abs_delta, 6),
        "max_delta_model": max_delta_model,
    }
    print(f"  Stability: range={g_range:.6f}, SD={g_sd:.6f}, CV={g_cv:.4f}, max|ΔG|={max_abs_delta:.6f} ({max_delta_model})", flush=True)
    print(f"  Done in {time.time()-t0:.1f}s", flush=True)

    return {
        "full_8model": full_info,
        "lomo": lomo_results,
        "stability": stability,
    }


def main():
    t_total = time.time()
    output = {"benchmarks": {}}

    for bm in BENCHMARKS:
        output["benchmarks"][bm] = run_lomo_benchmark(DATA_DIR, bm)

    all_deltas = []
    print(f"\n{'='*60}", flush=True)
    print("SUMMARY", flush=True)
    print(f"{'='*60}", flush=True)
    for bm in BENCHMARKS:
        s = output["benchmarks"][bm]["stability"]
        f = output["benchmarks"][bm]["full_8model"]
        print(f"  {bm:<12} G_full={f['g_item']:.6f}  range={s['g_range']:.6f}  SD={s['g_sd']:.6f}  CV={s['g_cv']:.4f}  max|ΔG|={s['max_abs_delta_g']:.6f} ({s['max_delta_model']})", flush=True)
        for r in output["benchmarks"][bm]["lomo"]:
            all_deltas.append({"benchmark": bm, "removed": r["removed"], "abs_delta_g": abs(r["delta_g"])})

    global_max = max(all_deltas, key=lambda x: x["abs_delta_g"])
    print(f"\n  Global max |ΔG| = {global_max['abs_delta_g']:.6f} ({global_max['benchmark']}, -{global_max['removed']})", flush=True)
    output["global_max_abs_delta_g"] = {
        "value": round(global_max["abs_delta_g"], 6),
        "benchmark": global_max["benchmark"],
        "removed_model": global_max["removed"],
    }

    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    with open(OUT_PATH, "w") as f:
        json.dump(output, f, indent=2, default=str)
    print(f"\n=> {OUT_PATH}", flush=True)
    print(f"Total: {time.time()-t_total:.1f}s", flush=True)


if __name__ == "__main__":
    main()
