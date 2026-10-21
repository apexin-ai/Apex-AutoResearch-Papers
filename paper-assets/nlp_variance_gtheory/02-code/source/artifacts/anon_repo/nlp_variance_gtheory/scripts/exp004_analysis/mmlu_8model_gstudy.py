"""8-model Henderson I G-study for MMLU — vectorized numpy implementation.

Facets: model(8), temperature(2), prompt_template(6), seed(6), ordering(4), item_id(200)
Fully crossed balanced design: 8×2×6×6×4×200 = 460,800 observations.
Reshape to 6D array, compute all marginals via axis-averaging. ~100x faster bootstrap.
"""

import json
import time
from itertools import combinations
from math import prod
from pathlib import Path

import numpy as np
import pandas as pd

FACET_NAMES = ["model", "temperature", "prompt_template", "seed", "ordering", "item_id"]
FACET_AXES = {name: i for i, name in enumerate(FACET_NAMES)}  # axis index in 6D array

MODEL_FILES = [
    "llama_mmlu.jsonl", "mistral_mmlu.jsonl", "qwen_mmlu.jsonl",
    "gemma_mmlu.jsonl", "internlm_mmlu.jsonl", "deepseek_mmlu.jsonl",
    "olmo_mmlu.jsonl", "yi_mmlu.jsonl",
]

MODEL_DISPLAY = {
    "meta-llama/Llama-3.1-8B-Instruct": "Llama-3.1-8B",
    "google/gemma-2-9b-it": "Gemma-2-9B",
    "mistralai/Mistral-7B-Instruct-v0.3": "Mistral-7B-v0.3",
    "Qwen/Qwen3-8B": "Qwen3-8B",
    "internlm/internlm2_5-7b-chat": "InternLM2.5-7B",
    "deepseek-ai/deepseek-llm-7b-chat": "DeepSeek-7B",
    "allenai/OLMo-2-1124-7B-Instruct": "OLMo-2-7B",
    "01-ai/Yi-1.5-9B-Chat": "Yi-1.5-9B",
}


def load_and_reshape(data_dir: str):
    """Load 8 JSONL files, return 6D numpy array + metadata."""
    frames = []
    for fn in MODEL_FILES:
        fp = Path(data_dir) / fn
        df = pd.read_json(fp, lines=True)
        frames.append(df)
    df = pd.concat(frames, ignore_index=True)
    if "top_logprobs" in df.columns:
        df.drop(columns=["top_logprobs"], inplace=True)
    df["model"] = df["model"].map(MODEL_DISPLAY).fillna(df["model"])

    facet_levels = {}
    facet_maps = {}
    for f in FACET_NAMES:
        levels = sorted(df[f].unique(), key=str)
        facet_levels[f] = levels
        facet_maps[f] = {v: i for i, v in enumerate(levels)}

    shape = tuple(len(facet_levels[f]) for f in FACET_NAMES)
    n_levels = {f: len(facet_levels[f]) for f in FACET_NAMES}
    print(f"Shape: {dict(zip(FACET_NAMES, shape))}", flush=True)
    assert prod(shape) == len(df), f"Design not fully crossed: {prod(shape)} != {len(df)}"

    Y = np.full(shape, np.nan)
    for _, row in df.iterrows():
        idx = tuple(facet_maps[f][row[f]] for f in FACET_NAMES)
        Y[idx] = row["correct"]
    assert not np.isnan(Y).any(), "Missing cells in design"

    return Y, n_levels, facet_levels, df


def henderson_i_from_array(Y, n_levels):
    """Henderson I on a fully-crossed balanced 6D array. Pure numpy."""
    N = Y.size
    grand_mean = Y.mean()
    n_facets = len(FACET_NAMES)
    axes = list(range(n_facets))

    effects = {}
    vc = {}

    # Main effects: SS_f = n_per * sum((marginal_mean_f - grand_mean)^2)
    for i, f in enumerate(FACET_NAMES):
        other_axes = tuple(j for j in axes if j != i)
        marginal = Y.mean(axis=other_axes)  # shape: (n_levels[f],)
        n_per = N // n_levels[f]
        ss = float(n_per * np.sum((marginal - grand_mean) ** 2))
        df_eff = n_levels[f] - 1
        effects[f] = {"ss": ss, "df": df_eff, "ms": ss / df_eff if df_eff > 0 else 0.0}

    # 2-way interactions: SS_{fi,fj}
    for fi, fj in combinations(FACET_NAMES, 2):
        ai, aj = FACET_AXES[fi], FACET_AXES[fj]
        other_axes = tuple(k for k in axes if k not in (ai, aj))
        cell_mean = Y.mean(axis=other_axes)  # shape: (n_fi, n_fj) — axes ordered by original position

        # marginals for subtraction
        main_fi = Y.mean(axis=tuple(k for k in axes if k != ai))  # shape: (n_fi,)
        main_fj = Y.mean(axis=tuple(k for k in axes if k != aj))  # shape: (n_fj,)

        # Expand for broadcasting
        if ai < aj:
            interaction = cell_mean - main_fi[:, None] - main_fj[None, :] + grand_mean
        else:
            interaction = cell_mean - main_fi[None, :] - main_fj[:, None] + grand_mean

        n_per = N // (n_levels[fi] * n_levels[fj])
        ss = float(n_per * np.sum(interaction ** 2))
        df_eff = (n_levels[fi] - 1) * (n_levels[fj] - 1)
        key = f"{fi}:{fj}"
        effects[key] = {"ss": ss, "df": df_eff, "ms": ss / df_eff if df_eff > 0 else 0.0}

    ss_total = float(np.sum((Y - grand_mean) ** 2))
    ss_model = sum(e["ss"] for e in effects.values())
    ss_res = max(0.0, ss_total - ss_model)
    df_res = N - 1 - sum(e["df"] for e in effects.values())
    effects["residual"] = {"ss": ss_res, "df": df_res, "ms": ss_res / df_res if df_res > 0 else 0.0}

    ms_res = effects["residual"]["ms"]

    # Variance components: interactions first
    for fi, fj in combinations(FACET_NAMES, 2):
        key = f"{fi}:{fj}"
        coeff = prod(n_levels[f] for f in FACET_NAMES if f not in (fi, fj))
        raw = (effects[key]["ms"] - ms_res) / coeff if coeff > 0 else 0.0
        vc[key] = max(0.0, raw)

    # Main effects
    for fi in FACET_NAMES:
        coeff_main = prod(n_levels[f] for f in FACET_NAMES if f != fi)
        interaction_contrib = 0.0
        for fj in FACET_NAMES:
            if fj == fi:
                continue
            int_key = f"{fi}:{fj}" if f"{fi}:{fj}" in vc else f"{fj}:{fi}"
            coeff_ij = prod(n_levels[f] for f in FACET_NAMES if f not in (fi, fj))
            interaction_contrib += coeff_ij * vc[int_key]
        raw = (effects[fi]["ms"] - interaction_contrib - ms_res) / coeff_main if coeff_main > 0 else 0.0
        vc[fi] = max(0.0, raw)

    vc["residual"] = ms_res
    return vc, n_levels


def compute_g_item(vc, n_levels):
    tau = vc.get("item_id", 0.0)
    delta = 0.0
    for comp, est in vc.items():
        if comp == "item_id":
            continue
        if comp == "residual":
            divisor = prod(n_levels[f] for f in FACET_NAMES if f != "item_id")
            delta += est / divisor
            continue
        facets_in = comp.split(":")
        if "item_id" not in facets_in:
            continue
        other = [f for f in facets_in if f != "item_id"]
        divisor = prod(n_levels[f] for f in other) if other else 1
        delta += est / divisor
    g = tau / (tau + delta) if (tau + delta) > 0 else 0.0
    return g, tau, delta


def bootstrap_ci(Y, n_levels, n_boot=400, seed=42):
    """Bootstrap CI via item-level resampling on the 6D array."""
    rng = np.random.RandomState(seed)
    item_axis = FACET_AXES["item_id"]
    n_items = Y.shape[item_axis]

    boot_vc_list = []
    boot_g_list = []

    for b in range(n_boot):
        if (b + 1) % 100 == 0:
            print(f"  bootstrap {b+1}/{n_boot}", flush=True)
        sampled_idx = rng.randint(0, n_items, size=n_items)
        Y_boot = np.take(Y, sampled_idx, axis=item_axis)

        vc_b, nl_b = henderson_i_from_array(Y_boot, n_levels)
        total_b = sum(vc_b.values())
        pct_b = {k: v / total_b * 100 if total_b > 0 else 0 for k, v in vc_b.items()}
        boot_vc_list.append(pct_b)

        g_b, _, _ = compute_g_item(vc_b, nl_b)
        boot_g_list.append(g_b)

    ci = {}
    for k in boot_vc_list[0]:
        vals = [b[k] for b in boot_vc_list]
        ci[k] = {
            "ci_lower": round(float(np.percentile(vals, 2.5)), 4),
            "ci_upper": round(float(np.percentile(vals, 97.5)), 4),
        }

    g_arr = np.array(boot_g_list)
    g_ci = {
        "ci_lower": round(float(np.percentile(g_arr, 2.5)), 6),
        "ci_upper": round(float(np.percentile(g_arr, 97.5)), 6),
        "mean": round(float(np.mean(g_arr)), 6),
        "std": round(float(np.std(g_arr)), 6),
    }
    return ci, g_ci


def main():
    t0 = time.time()
    data_dir = "results/exp002"
    output_path = "results/exp004_8model_analysis/per_benchmark_gstudy_mmlu.json"

    print("Loading 8-model MMLU data...", flush=True)
    Y, n_levels, facet_levels, df = load_and_reshape(data_dir)
    print(f"Loaded {Y.size} records ({time.time()-t0:.1f}s)", flush=True)
    print(f"Models: {facet_levels['model']}", flush=True)
    print(f"Items: {n_levels['item_id']}", flush=True)

    print("\nHenderson I variance decomposition...", flush=True)
    vc, _ = henderson_i_from_array(Y, n_levels)
    total_var = sum(vc.values())
    g_item, sigma_tau, sigma_delta = compute_g_item(vc, n_levels)

    print(f"\nPoint estimates:", flush=True)
    for k, v in sorted(vc.items(), key=lambda x: -x[1]):
        pct = v / total_var * 100
        print(f"  {k:<30s}: {v:.10f} ({pct:.4f}%)", flush=True)
    print(f"  Total: {total_var:.10f}", flush=True)
    print(f"  G_item = {g_item:.6f}", flush=True)

    print(f"\nBootstrap CI (400 iterations)...", flush=True)
    t1 = time.time()
    ci, g_ci = bootstrap_ci(Y, n_levels, n_boot=400, seed=42)
    print(f"Bootstrap done ({time.time()-t1:.1f}s)", flush=True)
    print(f"G_item 95% CI: [{g_ci['ci_lower']:.4f}, {g_ci['ci_upper']:.4f}]", flush=True)

    result = {
        "experiment": "exp-004",
        "analysis": "8model_henderson_i_gstudy_mmlu",
        "benchmark": "mmlu",
        "n_models": 8,
        "n_observations": int(Y.size),
        "n_levels": {k: int(v) for k, v in n_levels.items()},
        "grand_mean_accuracy": round(float(Y.mean()), 6),
        "facets": FACET_NAMES,
        "variance_components": {
            k: {
                "estimate": round(v, 10),
                "pct": round(v / total_var * 100, 4) if total_var > 0 else 0.0,
                "ci_lower": ci[k]["ci_lower"],
                "ci_upper": ci[k]["ci_upper"],
            }
            for k, v in sorted(vc.items(), key=lambda x: -x[1])
        },
        "total_variance": round(total_var, 10),
        "G_item": round(g_item, 6),
        "G_item_CI": g_ci,
        "sigma_tau": round(sigma_tau, 10),
        "sigma_delta": round(sigma_delta, 10),
        "models": facet_levels["model"],
    }

    Path(output_path).parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(result, f, indent=2, default=str)

    print(f"\n{'='*60}", flush=True)
    print(f"MMLU 8-Model G-Study Results", flush=True)
    print(f"{'='*60}", flush=True)
    print(f"N = {Y.size}, Models = {n_levels['model']}, Items = {n_levels['item_id']}", flush=True)
    print(f"Grand mean = {Y.mean():.6f}", flush=True)
    print(f"\n{'Facet':<30s} {'pct':>8s} {'95% CI':>20s}", flush=True)
    print("-" * 60, flush=True)
    for k, v in sorted(vc.items(), key=lambda x: -x[1]):
        pct = v / total_var * 100
        print(f"{k:<30s} {pct:>7.2f}% [{ci[k]['ci_lower']:>6.2f}%, {ci[k]['ci_upper']:>6.2f}%]", flush=True)
    print(f"\nG_item = {g_item:.4f}  [{g_ci['ci_lower']:.4f}, {g_ci['ci_upper']:.4f}]", flush=True)
    print(f"-> {output_path}", flush=True)
    print(f"Total runtime: {time.time()-t0:.1f}s", flush=True)


if __name__ == "__main__":
    main()
