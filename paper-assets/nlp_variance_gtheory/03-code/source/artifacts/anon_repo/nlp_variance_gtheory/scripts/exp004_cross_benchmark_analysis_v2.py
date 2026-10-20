"""exp-004 v2: Cross-benchmark analysis with balanced 6-model design.

Fixes: filters to 6 common models for B1/B2 to ensure fair comparison.
Also runs B3/B4 with both 6-model (balanced) and 8-model (full) variants.
"""

import argparse
import json
import sys
import time
from itertools import combinations, permutations
from math import prod
from pathlib import Path

import numpy as np
import pandas as pd
from scipy.stats import spearmanr, kendalltau

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from src.config.model_paths import normalize_model_name

FACETS = ["model", "temperature", "prompt_template", "seed", "ordering", "item_id"]
BENCHMARK_ORDER = ["mmlu", "arc", "hellaswag", "gsm8k", "math"]
G_TARGETS = [0.80, 0.90, 0.95]
ITEM_COUNTS = [10, 25, 50, 75, 100, 150, 200, 300, 500, 750, 1000]


def load_data(data_dir):
    data_path = Path(data_dir)
    frames = [pd.read_json(f, lines=True) for f in sorted(data_path.glob("*.jsonl"))]
    df = pd.concat(frames, ignore_index=True)
    if "top_logprobs" in df.columns:
        df.drop(columns=["top_logprobs"], inplace=True)
    df = df.dropna(subset=["benchmark"])
    df["model"] = df["model"].map(normalize_model_name).fillna(df["model"])
    for f in FACETS:
        df[f] = df[f].astype(str)
    return df


def get_common_models(df):
    benchmarks = df["benchmark"].unique()
    models_per_bm = [set(df[df["benchmark"] == bm]["model"].unique()) for bm in benchmarks]
    return sorted(set.intersection(*models_per_bm))


def compute_henderson_i(df, facets):
    grand_mean = df["correct"].mean()
    N = len(df)
    n_levels = {f: df[f].nunique() for f in facets}
    effects = {}
    for f in facets:
        group_means = df.groupby(f, observed=True)["correct"].mean()
        n_per = N // n_levels[f]
        ss = float(n_per * ((group_means - grand_mean) ** 2).sum())
        df_eff = n_levels[f] - 1
        effects[f] = {"ss": ss, "df": df_eff, "ms": ss / df_eff if df_eff > 0 else 0.0}
    for fi, fj in combinations(facets, 2):
        cell_means = df.groupby([fi, fj], observed=True)["correct"].mean()
        main_fi = df.groupby(fi, observed=True)["correct"].mean()
        main_fj = df.groupby(fj, observed=True)["correct"].mean()
        n_per = N // (n_levels[fi] * n_levels[fj])
        ss = 0.0
        for (li, lj), cm in cell_means.items():
            ss += n_per * (cm - main_fi[li] - main_fj[lj] + grand_mean) ** 2
        df_eff = (n_levels[fi] - 1) * (n_levels[fj] - 1)
        effects[f"{fi}:{fj}"] = {"ss": ss, "df": df_eff, "ms": ss / df_eff if df_eff > 0 else 0.0}
    ss_total = float(((df["correct"] - grand_mean) ** 2).sum())
    ss_model_sum = sum(e["ss"] for e in effects.values())
    ss_res = max(0.0, ss_total - ss_model_sum)
    df_res = N - 1 - sum(e["df"] for e in effects.values())
    effects["residual"] = {"ss": ss_res, "df": df_res, "ms": ss_res / df_res if df_res > 0 else 0.0}
    ms_res = effects["residual"]["ms"]
    vc = {}
    for fi, fj in combinations(facets, 2):
        key = f"{fi}:{fj}"
        coeff = prod(n_levels[f] for f in facets if f not in (fi, fj))
        vc[key] = max(0.0, (effects[key]["ms"] - ms_res) / coeff if coeff > 0 else 0.0)
    for fi in facets:
        coeff_main = prod(n_levels[f] for f in facets if f != fi)
        ic = 0.0
        for fj in facets:
            if fj == fi: continue
            ik = f"{fi}:{fj}" if f"{fi}:{fj}" in vc else f"{fj}:{fi}"
            ic += prod(n_levels[f] for f in facets if f not in (fi, fj)) * vc[ik]
        vc[fi] = max(0.0, (effects[fi]["ms"] - ic - ms_res) / coeff_main if coeff_main > 0 else 0.0)
    vc["residual"] = ms_res
    return vc, {k: int(v) for k, v in n_levels.items()}


def pcts(vc):
    t = sum(vc.values())
    return {k: v / t * 100 if t > 0 else 0 for k, v in vc.items()}


def g_for_n(vc, nl, ni, facets):
    si = vc.get("item_id", 0.0)
    na = nl["item_id"]
    non_item = [f for f in facets if f != "item_id"]
    sd = 0.0
    for c, e in vc.items():
        if e == 0 or c == "item_id": continue
        if c == "residual":
            sd += e / prod(nl[f] for f in non_item)
            continue
        fs = set(c.split(":"))
        if "item_id" not in fs: continue
        other = [f for f in fs if f != "item_id"]
        sd += e / (prod(nl[f] for f in other) if other else 1)
    sd_n = sd * (na / ni)
    return si / (si + sd_n) if (si + sd_n) > 0 else 0.0


def find_min(vc, nl, tgt, facets, mx=5000):
    for n in range(1, mx + 1):
        if g_for_n(vc, nl, n, facets) >= tgt:
            return n
    return None


def spearman_perm(values, order, direction):
    obs = [values[bm] for bm in order]
    n = len(order)
    exp = list(range(n, 0, -1)) if direction == "decreasing" else list(range(1, n + 1))
    obs_rho, _ = spearmanr(exp, obs)
    obs_tau, tau_p = kendalltau(exp, obs)
    ne = sum(1 for p in permutations(range(n))
             if spearmanr(exp, [obs[i] for i in p])[0] >= obs_rho)
    pv = ne / len(list(permutations(range(n))))
    return {
        "observed_values": {bm: round(values[bm], 4) for bm in order},
        "observed_rho": round(float(obs_rho), 6),
        "p_value": round(pv, 6),
        "n_extreme": ne,
        "n_permutations": len(list(permutations(range(n)))),
        "significant_at_0.05": pv < 0.05,
        "kendall_tau": round(float(obs_tau), 6),
        "kendall_p": round(float(tau_p), 6),
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--data-dir", default="results/exp002")
    parser.add_argument("--output-dir", default="results/exp004_8model_analysis")
    args = parser.parse_args()

    t0 = time.time()
    out = Path(args.output_dir)
    out.mkdir(parents=True, exist_ok=True)

    print("Loading data...", flush=True)
    df = load_data(args.data_dir)
    common_models = get_common_models(df)
    all_models = sorted(df["model"].unique())
    print(f"Total: {len(df)} obs, {len(all_models)} models, {df['benchmark'].nunique()} benchmarks", flush=True)
    print(f"All models: {all_models}", flush=True)
    print(f"Common models (in all 5 benchmarks): {common_models} ({len(common_models)})", flush=True)

    df_balanced = df[df["model"].isin(common_models)].reset_index(drop=True)
    print(f"Balanced subset: {len(df_balanced)} obs", flush=True)

    # =============== B1: Permutation test (balanced 6-model) ===============
    print("\n" + "=" * 70, flush=True)
    print("B1: Permutation test (5 benchmarks, 6 common models)", flush=True)
    print("=" * 70, flush=True)

    bm_stats = {}
    avail = [bm for bm in BENCHMARK_ORDER if bm in df_balanced["benchmark"].unique()]
    for bm in avail:
        d = df_balanced[df_balanced["benchmark"] == bm].reset_index(drop=True)
        vc, nl = compute_henderson_i(d, FACETS)
        p = pcts(vc)
        bm_stats[bm] = {
            "item_id_pct": p.get("item_id", 0),
            "model_item_pct": p.get("model:item_id", 0),
            "n_obs": len(d),
            "n_models": nl["model"],
            "accuracy": round(float(d["correct"].mean()), 6),
        }
        print(f"  {bm}: item_id={p.get('item_id', 0):.2f}%, model:item={p.get('model:item_id', 0):.2f}%, "
              f"n={len(d)}, models={nl['model']}", flush=True)

    ip = {bm: bm_stats[bm]["item_id_pct"] for bm in avail}
    mip = {bm: bm_stats[bm]["model_item_pct"] for bm in avail}
    t_item = spearman_perm(ip, avail, "decreasing")
    t_mi = spearman_perm(mip, avail, "increasing")

    b1 = {
        "experiment": f"exp-004 ({len(common_models)} common models × 5 benchmarks)",
        "design_note": "Filtered to 6 models present in ALL benchmarks for fair comparison",
        "common_models": common_models,
        "test_statistic": "spearman_rho",
        "n_benchmarks": len(avail),
        "n_permutations": 120,
        "benchmark_order_hypothesis": BENCHMARK_ORDER,
        "benchmarks_used": avail,
        "benchmark_stats": bm_stats,
        "item_id_gradient": {
            "hypothesis": "item_id% decreasing: MC (MMLU/ARC/HellaSwag) > FF (GSM8K/MATH)",
            "direction": "decreasing",
            **t_item,
        },
        "model_item_gradient": {
            "hypothesis": "model:item% increasing from MC to FF",
            "direction": "increasing",
            **t_mi,
        },
    }
    with open(out / "permutation_test_5bm.json", "w") as f:
        json.dump(b1, f, indent=2)
    print(f"\n  item_id:    rho={t_item['observed_rho']:.4f}, p={t_item['p_value']:.4f} "
          f"{'*' if t_item['significant_at_0.05'] else 'n.s.'}", flush=True)
    print(f"  model:item: rho={t_mi['observed_rho']:.4f}, p={t_mi['p_value']:.4f} "
          f"{'*' if t_mi['significant_at_0.05'] else 'n.s.'}", flush=True)
    print(f"  -> {out / 'permutation_test_5bm.json'}", flush=True)

    # =============== B2: LOBO (balanced 6-model) ===============
    print("\n" + "=" * 70, flush=True)
    print("B2: Leave-one-benchmark-out stability (6 common models)", flush=True)
    print("=" * 70, flush=True)

    lobo = {}
    for drop in avail:
        rem = [bm for bm in avail if bm != drop]
        iv = {bm: bm_stats[bm]["item_id_pct"] for bm in rem}
        mv = {bm: bm_stats[bm]["model_item_pct"] for bm in rem}
        ti = spearman_perm(iv, rem, "decreasing")
        tm = spearman_perm(mv, rem, "increasing")
        il = [iv[bm] for bm in rem]
        ml = [mv[bm] for bm in rem]
        i_mono = all(il[i] >= il[i + 1] for i in range(len(il) - 1))
        m_mono = all(ml[i] <= ml[i + 1] for i in range(len(ml) - 1))
        lobo[drop] = {
            "dropped": drop,
            "remaining": rem,
            "item_id_values": {bm: round(iv[bm], 4) for bm in rem},
            "model_item_values": {bm: round(mv[bm], 4) for bm in rem},
            "item_id_monotonic": i_mono,
            "model_item_monotonic": m_mono,
            "both_monotonic": i_mono and m_mono,
            "item_id_rho": ti["observed_rho"],
            "item_id_p": ti["p_value"],
            "model_item_rho": tm["observed_rho"],
            "model_item_p": tm["p_value"],
        }
        s = "OK" if (i_mono and m_mono) else "BROKEN"
        print(f"  Drop {drop}: {s} | item rho={ti['observed_rho']:.3f} p={ti['p_value']:.3f}, "
              f"mi rho={tm['observed_rho']:.3f} p={tm['p_value']:.3f}", flush=True)

    np_ = sum(1 for r in lobo.values() if r["both_monotonic"])
    b2 = {
        "experiment": "exp-004",
        "design_note": "6 common models, balanced",
        "benchmark_order": avail,
        "full_set": {
            "item_id_values": {bm: round(bm_stats[bm]["item_id_pct"], 4) for bm in avail},
            "model_item_values": {bm: round(bm_stats[bm]["model_item_pct"], 4) for bm in avail},
        },
        "lobo_results": lobo,
        "summary": {"n_benchmarks": len(avail), "n_drops": len(lobo),
                     "n_gradient_preserved": np_, "gradient_robust": np_ == len(lobo)},
    }
    with open(out / "lobo_stability.json", "w") as f:
        json.dump(b2, f, indent=2)
    print(f"  Gradient preserved: {np_}/{len(lobo)}", flush=True)
    print(f"  -> {out / 'lobo_stability.json'}", flush=True)

    # =============== B3: D-study (both balanced and full) ===============
    print("\n" + "=" * 70, flush=True)
    print("B3: D-study projections", flush=True)
    print("=" * 70, flush=True)

    ds_results = {}
    for label, dfx in [("6model_balanced", df_balanced), ("full", df)]:
        ds_results[label] = {}
        print(f"\n  --- {label} ({dfx['model'].nunique()} models) ---", flush=True)
        for bm in avail:
            d = dfx[dfx["benchmark"] == bm].reset_index(drop=True)
            if len(d) == 0: continue
            vc, nl = compute_henderson_i(d, FACETS)
            p = pcts(vc)
            gc = g_for_n(vc, nl, nl["item_id"], FACETS)
            curve = {str(ni): round(g_for_n(vc, nl, ni, FACETS), 6) for ni in ITEM_COUNTS}
            mi = {str(t): find_min(vc, nl, t, FACETS) for t in G_TARGETS}
            ds_results[label][bm] = {
                "n_obs": len(d), "n_levels": nl,
                "accuracy": round(float(d["correct"].mean()), 6),
                "G_current": round(gc, 6),
                "item_id_pct": round(p.get("item_id", 0), 4),
                "model_item_pct": round(p.get("model:item_id", 0), 4),
                "d_study_curve": curve,
                "min_items_for_G": mi,
                "top_variance_pct": {k: round(v, 4) for k, v in sorted(p.items(), key=lambda x: -x[1])[:8] if v > 0.01},
            }
            print(f"    {bm:<10} G={gc:.4f} n_m={nl['model']} | "
                  f"G>=.80={mi.get('0.8', '>5k')}, G>=.90={mi.get('0.9', '>5k')}, G>=.95={mi.get('0.95', '>5k')}", flush=True)

    b3 = {
        "experiment": "exp-004",
        "facets": FACETS,
        "g_targets": G_TARGETS,
        "common_models": common_models,
        "all_models": all_models,
        "balanced_6model": ds_results["6model_balanced"],
        "full_data": ds_results["full"],
    }
    with open(out / "dstudy_8model.json", "w") as f:
        json.dump(b3, f, indent=2)
    print(f"  -> {out / 'dstudy_8model.json'}", flush=True)

    # =============== B4: Cross-model G-study ===============
    print("\n" + "=" * 70, flush=True)
    print("B4: Cross-model G-study", flush=True)
    print("=" * 70, flush=True)

    prev_4model = {"item_id_pct": 41.55, "model_item_pct": 32.81, "model_pct": 0.75, "G_item": 0.8159, "n_models": 4}

    per_bm_6 = {}
    per_bm_full = {}
    for label, dfx, target in [("6model", df_balanced, per_bm_6), ("full", df, per_bm_full)]:
        print(f"\n  --- {label} ---", flush=True)
        for bm in avail:
            d = dfx[dfx["benchmark"] == bm].reset_index(drop=True)
            if len(d) == 0: continue
            vc, nl = compute_henderson_i(d, FACETS)
            p = pcts(vc)
            gi = g_for_n(vc, nl, nl["item_id"], FACETS)
            target[bm] = {
                "n_obs": len(d), "n_levels": nl,
                "accuracy": round(float(d["correct"].mean()), 6),
                "item_id_pct": round(p.get("item_id", 0), 4),
                "model_item_pct": round(p.get("model:item_id", 0), 4),
                "model_pct": round(p.get("model", 0), 4),
                "G_item": round(gi, 6),
                "top_components": {k: round(v, 4) for k, v in sorted(p.items(), key=lambda x: -x[1])[:6]},
            }
            print(f"    {bm:<10} item_id={p.get('item_id',0):.2f}% m:item={p.get('model:item_id',0):.2f}% "
                  f"model={p.get('model',0):.2f}% G={gi:.4f} (n_m={nl['model']})", flush=True)

    mmlu_6 = per_bm_6.get("mmlu", {})
    b4 = {
        "experiment": "exp-004",
        "common_models": common_models,
        "all_models": all_models,
        "facets": FACETS,
        "mmlu_6model": mmlu_6,
        "comparison_4model": prev_4model,
        "delta_vs_4model": {
            "item_id_pct_change": round(mmlu_6.get("item_id_pct", 0) - prev_4model["item_id_pct"], 4),
            "model_item_pct_change": round(mmlu_6.get("model_item_pct", 0) - prev_4model["model_item_pct"], 4),
            "G_item_change": round(mmlu_6.get("G_item", 0) - prev_4model["G_item"], 6),
        },
        "per_benchmark_6model": per_bm_6,
        "per_benchmark_full": per_bm_full,
    }
    with open(out / "cross_model_gstudy_8model.json", "w") as f:
        json.dump(b4, f, indent=2)
    print(f"  -> {out / 'cross_model_gstudy_8model.json'}", flush=True)

    print(f"\n{'=' * 70}", flush=True)
    print(f"All done. Runtime: {time.time()-t0:.1f}s", flush=True)
    print(f"Files: {out}/", flush=True)
    for f in sorted(out.glob("*.json")):
        print(f"  {f.name}", flush=True)


if __name__ == "__main__":
    main()
