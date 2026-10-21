"""exp-004: Cross-benchmark comprehensive analysis (6 models × 5 benchmarks).

B1: Permutation test (Spearman rho, exact, 5! = 120)
B2: Leave-one-benchmark-out stability
B3: D-study projections (per-benchmark, all 6 models)
B4: Cross-model G-study (6 models, model-as-facet)

Output: results/exp004_8model_analysis/
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


def load_data(data_dir: str) -> pd.DataFrame:
    data_path = Path(data_dir)
    jsonl_files = sorted(data_path.glob("*.jsonl"))
    if not jsonl_files:
        raise FileNotFoundError(f"No JSONL files in {data_dir}")
    frames = [pd.read_json(f, lines=True) for f in jsonl_files]
    df = pd.concat(frames, ignore_index=True)
    if "top_logprobs" in df.columns:
        df.drop(columns=["top_logprobs"], inplace=True)
    df = df.dropna(subset=["benchmark"])
    df["model"] = df["model"].map(normalize_model_name).fillna(df["model"])
    for f in FACETS:
        df[f] = df[f].astype(str)
    return df


def compute_henderson_i(df: pd.DataFrame, facets: list[str]) -> tuple[dict, dict]:
    """Henderson Method I -> variance components."""
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
            interaction = cm - main_fi[li] - main_fj[lj] + grand_mean
            ss += n_per * interaction ** 2
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
    return vc, {k: int(v) for k, v in n_levels.items()}


def compute_pcts(vc: dict) -> dict[str, float]:
    total = sum(vc.values())
    return {k: v / total * 100 if total > 0 else 0.0 for k, v in vc.items()}


# ============================================================
# B1: Permutation test
# ============================================================
def spearman_permutation_test(values: dict, order: list, direction: str):
    """Exact permutation test using Spearman rho."""
    observed = [values[bm] for bm in order]
    n = len(order)
    if direction == "decreasing":
        expected = list(range(n, 0, -1))
    else:
        expected = list(range(1, n + 1))

    obs_rho, _ = spearmanr(expected, observed)
    obs_tau, tau_p = kendalltau(expected, observed)

    all_perms = list(permutations(range(n)))
    n_extreme = 0
    for perm in all_perms:
        perm_vals = [observed[i] for i in perm]
        rho, _ = spearmanr(expected, perm_vals)
        if direction == "decreasing":
            if rho >= obs_rho:
                n_extreme += 1
        else:
            if rho >= obs_rho:
                n_extreme += 1

    p_value = n_extreme / len(all_perms)
    return {
        "observed_values": {bm: round(values[bm], 4) for bm in order},
        "observed_rho": round(float(obs_rho), 6),
        "p_value": round(p_value, 6),
        "n_extreme": n_extreme,
        "n_permutations": len(all_perms),
        "significant_at_0.05": p_value < 0.05,
        "kendall_tau": round(float(obs_tau), 6),
        "kendall_p": round(float(tau_p), 6),
    }


def run_b1_permutation_test(df: pd.DataFrame, output_dir: Path):
    print("\n" + "=" * 70, flush=True)
    print("B1: Permutation test (5 benchmarks)", flush=True)
    print("=" * 70, flush=True)

    benchmark_stats = {}
    available = [bm for bm in BENCHMARK_ORDER if bm in df["benchmark"].unique()]

    for bm in available:
        df_bm = df[df["benchmark"] == bm].reset_index(drop=True)
        vc, _ = compute_henderson_i(df_bm, FACETS)
        pcts = compute_pcts(vc)
        benchmark_stats[bm] = {
            "item_id_pct": pcts.get("item_id", 0.0),
            "model_item_pct": pcts.get("model:item_id", 0.0),
            "n_obs": len(df_bm),
            "accuracy": float(df_bm["correct"].mean()),
        }
        print(f"  {bm}: item_id={pcts.get('item_id', 0):.2f}%, "
              f"model:item={pcts.get('model:item_id', 0):.2f}%", flush=True)

    item_pcts = {bm: benchmark_stats[bm]["item_id_pct"] for bm in available}
    model_item_pcts = {bm: benchmark_stats[bm]["model_item_pct"] for bm in available}

    test_item = spearman_permutation_test(item_pcts, available, "decreasing")
    test_model_item = spearman_permutation_test(model_item_pcts, available, "increasing")

    result = {
        "experiment": "exp-004 (6 models × 5 benchmarks)",
        "test_statistic": "spearman_rho",
        "n_benchmarks": len(available),
        "n_permutations": test_item["n_permutations"],
        "benchmark_order_hypothesis": BENCHMARK_ORDER,
        "benchmarks_used": available,
        "benchmark_stats": benchmark_stats,
        "item_id_gradient": {
            "hypothesis": "MC benchmarks (MMLU/ARC/HellaSwag) > FF benchmarks (GSM8K/MATH)",
            "direction": "decreasing (knowledge-retrieval → reasoning)",
            **test_item,
        },
        "model_item_gradient": {
            "hypothesis": "model×item increases from MC to FF",
            "direction": "increasing",
            **test_model_item,
        },
    }

    out_path = output_dir / "permutation_test_5bm.json"
    with open(out_path, "w") as f:
        json.dump(result, f, indent=2)

    print(f"\n  item_id gradient:    rho={test_item['observed_rho']:.4f}, "
          f"p={test_item['p_value']:.4f}", flush=True)
    print(f"  model:item gradient: rho={test_model_item['observed_rho']:.4f}, "
          f"p={test_model_item['p_value']:.4f}", flush=True)
    print(f"  -> {out_path}", flush=True)
    return result


# ============================================================
# B2: Leave-one-benchmark-out
# ============================================================
def run_b2_lobo(df: pd.DataFrame, benchmark_stats: dict, output_dir: Path):
    print("\n" + "=" * 70, flush=True)
    print("B2: Leave-one-benchmark-out stability", flush=True)
    print("=" * 70, flush=True)

    available = [bm for bm in BENCHMARK_ORDER if bm in benchmark_stats]

    full_item_vals = [benchmark_stats[bm]["item_id_pct"] for bm in available]
    full_mi_vals = [benchmark_stats[bm]["model_item_pct"] for bm in available]

    print(f"  Full set item_id%:    {[f'{v:.2f}' for v in full_item_vals]}", flush=True)
    print(f"  Full set model:item%: {[f'{v:.2f}' for v in full_mi_vals]}", flush=True)

    lobo_results = {}
    for drop_bm in available:
        remaining = [bm for bm in available if bm != drop_bm]
        item_vals = {bm: benchmark_stats[bm]["item_id_pct"] for bm in remaining}
        mi_vals = {bm: benchmark_stats[bm]["model_item_pct"] for bm in remaining}

        test_item = spearman_permutation_test(item_vals, remaining, "decreasing")
        test_mi = spearman_permutation_test(mi_vals, remaining, "increasing")

        item_list = [item_vals[bm] for bm in remaining]
        mi_list = [mi_vals[bm] for bm in remaining]
        item_monotonic = all(item_list[i] >= item_list[i + 1] for i in range(len(item_list) - 1))
        mi_monotonic = all(mi_list[i] <= mi_list[i + 1] for i in range(len(mi_list) - 1))

        lobo_results[drop_bm] = {
            "dropped": drop_bm,
            "remaining": remaining,
            "item_id_values": {bm: round(benchmark_stats[bm]["item_id_pct"], 4) for bm in remaining},
            "model_item_values": {bm: round(benchmark_stats[bm]["model_item_pct"], 4) for bm in remaining},
            "item_id_monotonic_decreasing": item_monotonic,
            "model_item_monotonic_increasing": mi_monotonic,
            "both_monotonic": item_monotonic and mi_monotonic,
            "item_id_spearman_rho": test_item["observed_rho"],
            "item_id_p_value": test_item["p_value"],
            "model_item_spearman_rho": test_mi["observed_rho"],
            "model_item_p_value": test_mi["p_value"],
        }

        status = "PRESERVED" if (item_monotonic and mi_monotonic) else "BROKEN"
        print(f"  Drop {drop_bm}: {status} | item rho={test_item['observed_rho']:.3f} "
              f"p={test_item['p_value']:.3f}, mi rho={test_mi['observed_rho']:.3f} "
              f"p={test_mi['p_value']:.3f}", flush=True)

    n_preserved = sum(1 for r in lobo_results.values() if r["both_monotonic"])

    result = {
        "experiment": "exp-004",
        "analysis": "leave_one_benchmark_out",
        "benchmark_order": available,
        "full_set": {
            "item_id_values": {bm: round(benchmark_stats[bm]["item_id_pct"], 4) for bm in available},
            "model_item_values": {bm: round(benchmark_stats[bm]["model_item_pct"], 4) for bm in available},
        },
        "lobo_results": lobo_results,
        "summary": {
            "n_benchmarks": len(available),
            "n_drops": len(lobo_results),
            "n_gradient_preserved": n_preserved,
            "gradient_robust": n_preserved == len(lobo_results),
        },
    }

    out_path = output_dir / "lobo_stability.json"
    with open(out_path, "w") as f:
        json.dump(result, f, indent=2)
    print(f"  Gradient preserved: {n_preserved}/{len(lobo_results)}", flush=True)
    print(f"  -> {out_path}", flush=True)
    return result


# ============================================================
# B3: D-study projections
# ============================================================
def compute_g_for_n_items(vc: dict, n_levels: dict, n_items: int, facets: list[str]) -> float:
    sigma_item = vc.get("item_id", 0.0)
    n_actual = n_levels["item_id"]
    non_item = [f for f in facets if f != "item_id"]

    sigma_delta_actual = 0.0
    for comp, est in vc.items():
        if est == 0.0 or comp == "item_id":
            continue
        if comp == "residual":
            sigma_delta_actual += est / prod(n_levels[f] for f in non_item)
            continue
        facets_in = set(comp.split(":"))
        if "item_id" not in facets_in:
            continue
        other = [f for f in facets_in if f != "item_id"]
        sigma_delta_actual += est / (prod(n_levels[f] for f in other) if other else 1)

    sigma_delta_n = sigma_delta_actual * (n_actual / n_items)
    total = sigma_item + sigma_delta_n
    return sigma_item / total if total > 0 else 0.0


def find_min_items(vc: dict, n_levels: dict, target_g: float, facets: list[str], max_items: int = 5000):
    for ni in range(1, max_items + 1):
        g = compute_g_for_n_items(vc, n_levels, ni, facets)
        if g >= target_g:
            return ni
    return None


def run_b3_dstudy(df: pd.DataFrame, output_dir: Path):
    print("\n" + "=" * 70, flush=True)
    print("B3: D-study projections (per-benchmark, all models)", flush=True)
    print("=" * 70, flush=True)

    available = [bm for bm in BENCHMARK_ORDER if bm in df["benchmark"].unique()]
    n_models = df["model"].nunique()
    print(f"  Models: {n_models}, Benchmarks: {available}", flush=True)

    results = {}
    for bm in available:
        df_bm = df[df["benchmark"] == bm].reset_index(drop=True)
        vc, n_levels = compute_henderson_i(df_bm, FACETS)
        total_var = sum(vc.values())
        pcts = compute_pcts(vc)

        g_current = compute_g_for_n_items(vc, n_levels, n_levels["item_id"], FACETS)

        curve = {}
        for ni in ITEM_COUNTS:
            g = compute_g_for_n_items(vc, n_levels, ni, FACETS)
            curve[str(ni)] = round(g, 6)

        min_items = {}
        for target in G_TARGETS:
            n = find_min_items(vc, n_levels, target, FACETS)
            min_items[str(target)] = n

        # Multi-facet vs single-condition ratio
        sigma_item = vc.get("item_id", 0.0)
        sigma_delta_multi = sum(v for k, v in vc.items() if k != "item_id")
        sigma_single = total_var - sigma_item  # all non-item variance
        ratio = sigma_single / sigma_delta_multi if sigma_delta_multi > 0 else float("inf")

        results[bm] = {
            "n_observations": len(df_bm),
            "n_levels": n_levels,
            "accuracy": round(float(df_bm["correct"].mean()), 6),
            "G_current": round(g_current, 6),
            "item_id_pct": round(pcts.get("item_id", 0), 4),
            "model_item_pct": round(pcts.get("model:item_id", 0), 4),
            "d_study_curve": curve,
            "min_items_for_G": min_items,
            "variance_components_pct": {k: round(v, 4) for k, v in sorted(pcts.items(), key=lambda x: -x[1]) if v > 0.01},
        }

        m80 = min_items.get("0.8", ">5000")
        m90 = min_items.get("0.9", ">5000")
        m95 = min_items.get("0.95", ">5000")
        print(f"  {bm:<10} G={g_current:.4f} | min items: G>=.80={m80}, G>=.90={m90}, G>=.95={m95}", flush=True)

    result = {
        "experiment": "exp-004",
        "analysis": "dstudy_projections",
        "n_models": n_models,
        "models": sorted(df["model"].unique()),
        "facets": FACETS,
        "g_targets": G_TARGETS,
        "benchmarks": results,
    }

    out_path = output_dir / "dstudy_8model.json"
    with open(out_path, "w") as f:
        json.dump(result, f, indent=2)
    print(f"  -> {out_path}", flush=True)
    return result


# ============================================================
# B4: Cross-model G-study (model-as-facet)
# ============================================================
def run_b4_cross_model_gstudy(df: pd.DataFrame, output_dir: Path):
    print("\n" + "=" * 70, flush=True)
    print("B4: Cross-model G-study (model-as-facet, MMLU)", flush=True)
    print("=" * 70, flush=True)

    df_mmlu = df[df["benchmark"] == "mmlu"].reset_index(drop=True)
    n_models = df_mmlu["model"].nunique()
    print(f"  MMLU: {len(df_mmlu)} obs, {n_models} models", flush=True)
    print(f"  Models: {sorted(df_mmlu['model'].unique())}", flush=True)

    vc_mmlu, nl_mmlu = compute_henderson_i(df_mmlu, FACETS)
    pcts_mmlu = compute_pcts(vc_mmlu)
    g_item_mmlu = compute_g_for_n_items(vc_mmlu, nl_mmlu, nl_mmlu["item_id"], FACETS)

    print(f"  item_id%:       {pcts_mmlu.get('item_id', 0):.2f}%", flush=True)
    print(f"  model:item_id%: {pcts_mmlu.get('model:item_id', 0):.2f}%", flush=True)
    print(f"  model%:         {pcts_mmlu.get('model', 0):.2f}%", flush=True)
    print(f"  G_item:         {g_item_mmlu:.6f}", flush=True)

    # Compare with 4-model results
    prev_4model = {
        "item_id_pct": 41.55,
        "model_item_pct": 32.81,
        "model_pct": 0.75,
        "G_item": 0.8159,
        "n_models": 4,
    }

    # Per-benchmark cross-model analysis
    per_bm = {}
    for bm in BENCHMARK_ORDER:
        df_bm = df[df["benchmark"] == bm].reset_index(drop=True)
        if len(df_bm) == 0:
            continue
        vc, nl = compute_henderson_i(df_bm, FACETS)
        pcts = compute_pcts(vc)
        g_item = compute_g_for_n_items(vc, nl, nl["item_id"], FACETS)

        per_bm[bm] = {
            "n_obs": len(df_bm),
            "n_levels": nl,
            "accuracy": round(float(df_bm["correct"].mean()), 6),
            "item_id_pct": round(pcts.get("item_id", 0), 4),
            "model_item_pct": round(pcts.get("model:item_id", 0), 4),
            "model_pct": round(pcts.get("model", 0), 4),
            "G_item": round(g_item, 6),
            "top_components": {k: round(v, 4) for k, v in sorted(pcts.items(), key=lambda x: -x[1])[:6]},
        }

    result = {
        "experiment": "exp-004",
        "analysis": "cross_model_gstudy",
        "n_models": n_models,
        "models": sorted(df["model"].unique()),
        "facets": FACETS,
        "mmlu_focus": {
            "n_observations": len(df_mmlu),
            "n_levels": nl_mmlu,
            "item_id_pct": round(pcts_mmlu.get("item_id", 0), 4),
            "model_item_pct": round(pcts_mmlu.get("model:item_id", 0), 4),
            "model_pct": round(pcts_mmlu.get("model", 0), 4),
            "G_item": round(g_item_mmlu, 6),
            "variance_components_pct": {k: round(v, 4) for k, v in sorted(pcts_mmlu.items(), key=lambda x: -x[1]) if v > 0.01},
        },
        "comparison_4model": prev_4model,
        "delta_vs_4model": {
            "item_id_pct_change": round(pcts_mmlu.get("item_id", 0) - prev_4model["item_id_pct"], 4),
            "model_item_pct_change": round(pcts_mmlu.get("model:item_id", 0) - prev_4model["model_item_pct"], 4),
            "G_item_change": round(g_item_mmlu - prev_4model["G_item"], 6),
        },
        "per_benchmark": per_bm,
    }

    out_path = output_dir / "cross_model_gstudy_8model.json"
    with open(out_path, "w") as f:
        json.dump(result, f, indent=2)

    print(f"\n  Per-benchmark summary:", flush=True)
    print(f"  {'Benchmark':<12} {'item_id%':>9} {'m:item%':>9} {'model%':>8} {'G_item':>8}", flush=True)
    print(f"  {'-'*48}", flush=True)
    for bm in per_bm:
        r = per_bm[bm]
        print(f"  {bm:<12} {r['item_id_pct']:>8.2f}% {r['model_item_pct']:>8.2f}% "
              f"{r['model_pct']:>7.2f}% {r['G_item']:>8.4f}", flush=True)

    print(f"\n  vs 4-model: item_id% {pcts_mmlu.get('item_id',0):.2f} vs {prev_4model['item_id_pct']:.2f}, "
          f"model:item% {pcts_mmlu.get('model:item_id',0):.2f} vs {prev_4model['model_item_pct']:.2f}", flush=True)
    print(f"  -> {out_path}", flush=True)
    return result


def main():
    parser = argparse.ArgumentParser(description="exp-004 cross-benchmark analysis")
    parser.add_argument("--data-dir", default="results/exp002")
    parser.add_argument("--output-dir", default="results/exp004_8model_analysis")
    args = parser.parse_args()

    t0 = time.time()
    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    print("Loading data...", flush=True)
    df = load_data(args.data_dir)
    print(f"Loaded {len(df)} records, {df['model'].nunique()} models, "
          f"{df['benchmark'].nunique()} benchmarks ({time.time()-t0:.1f}s)", flush=True)
    print(f"Models: {sorted(df['model'].unique())}", flush=True)
    print(f"Benchmarks: {sorted(df['benchmark'].unique())}", flush=True)

    # B1
    b1 = run_b1_permutation_test(df, output_dir)

    # B2 (reuse B1's benchmark_stats)
    run_b2_lobo(df, b1["benchmark_stats"], output_dir)

    # B3
    run_b3_dstudy(df, output_dir)

    # B4
    run_b4_cross_model_gstudy(df, output_dir)

    print(f"\n{'=' * 70}", flush=True)
    print(f"All analyses complete. Runtime: {time.time()-t0:.1f}s", flush=True)
    print(f"Output: {output_dir}/", flush=True)


if __name__ == "__main__":
    main()
