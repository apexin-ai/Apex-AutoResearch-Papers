"""G_item consistency diagnostic: 4-model vs 8-model GSM8K.

Root cause hypothesis: exp004_ff_gstudy.py has divisor=1 for residual in compute_g_item,
while per_benchmark_gstudy.py correctly divides by prod(non_item_facet_levels).
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
KEEP_COLS = ["model", "temperature", "prompt_template", "seed", "ordering", "item_id", "correct"]

MODEL_ORDER = ["Llama-3.1-8B", "Mistral-7B-v0.3", "Qwen3-8B", "Gemma-2-9B",
               "InternLM2.5-7B", "DeepSeek-7B", "OLMo-2-7B", "Yi-1.5-9B"]

GSM8K_FILES = ["llama_gsm8k", "mistral_gsm8k", "qwen_gsm8k", "gemma_gsm8k",
               "internlm_gsm8k", "deepseek_gsm8k", "olmo_gsm8k", "yi_gsm8k"]

MMLU_FILES = ["llama_mmlu", "mistral_mmlu", "qwen_mmlu", "gemma_mmlu",
              "internlm_mmlu", "deepseek_mmlu", "olmo_mmlu", "yi_mmlu"]


def load_benchmark_data(benchmark_files):
    frames = []
    for fname in benchmark_files:
        fpath = DATA_DIR / f"{fname}.jsonl"
        if not fpath.exists():
            print(f"  SKIP {fpath}")
            continue
        df = pd.read_json(fpath, lines=True)
        if "_placeholder" in df.columns:
            df = df[df["_placeholder"] != True]
        if "top_logprobs" in df.columns:
            df.drop(columns=["top_logprobs"], inplace=True)
        df["model"] = df["model"].map(normalize_model_name).fillna(df["model"])
        for f in FACETS:
            df[f] = df[f].astype(str)
        frames.append(df[KEEP_COLS])
    return pd.concat(frames, ignore_index=True)


def henderson_i(df):
    grand_mean = df["correct"].mean()
    N = len(df)
    n_levels = {f: df[f].nunique() for f in FACETS}
    effects = {}

    for f in FACETS:
        gm = df.groupby(f, observed=True)["correct"].mean()
        n_per = N // n_levels[f]
        ss = float(n_per * ((gm - grand_mean) ** 2).sum())
        dof = n_levels[f] - 1
        effects[f] = {"ss": ss, "df": dof, "ms": ss / dof if dof > 0 else 0.0}

    for fi, fj in combinations(FACETS, 2):
        cm = df.groupby([fi, fj], observed=True)["correct"].mean()
        mi = df.groupby(fi, observed=True)["correct"].mean()
        mj = df.groupby(fj, observed=True)["correct"].mean()
        n_per = N // (n_levels[fi] * n_levels[fj])
        ss = 0.0
        for (li, lj), val in cm.items():
            ss += n_per * (val - mi[li] - mj[lj] + grand_mean) ** 2
        dof = (n_levels[fi] - 1) * (n_levels[fj] - 1)
        effects[f"{fi}:{fj}"] = {"ss": ss, "df": dof, "ms": ss / dof if dof > 0 else 0.0}

    ss_total = float(((df["correct"] - grand_mean) ** 2).sum())
    ss_model_sum = sum(e["ss"] for e in effects.values())
    ss_res = max(0.0, ss_total - ss_model_sum)
    df_res = N - 1 - sum(e["df"] for e in effects.values())
    effects["residual"] = {"ss": ss_res, "df": df_res, "ms": ss_res / df_res if df_res > 0 else 0.0}

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
            ik = f"{fi}:{fj}" if f"{fi}:{fj}" in vc else f"{fj}:{fi}"
            cij = prod(n_levels[f] for f in FACETS if f not in (fi, fj))
            ic += cij * vc[ik]
        vc[fi] = max(0.0, (effects[fi]["ms"] - ic - ms_res) / coeff_main if coeff_main > 0 else 0.0)

    vc["residual"] = ms_res
    return vc, n_levels


def g_item_correct(vc, n_levels):
    """Correct formula: residual / prod(non_item_facets)."""
    non_item = [f for f in FACETS if f != "item_id"]
    sigma_item = vc.get("item_id", 0.0)
    sigma_delta = 0.0
    for key, est in vc.items():
        if est == 0.0 or key == "item_id":
            continue
        if key == "residual":
            sigma_delta += est / prod(n_levels[f] for f in non_item)
            continue
        parts = set(key.split(":"))
        if "item_id" not in parts:
            continue
        other = [p for p in parts if p != "item_id"]
        sigma_delta += est / (prod(n_levels[o] for o in other) if other else 1)
    g = sigma_item / (sigma_item + sigma_delta) if (sigma_item + sigma_delta) > 0 else 0.0
    return g, sigma_item, sigma_delta


def g_item_buggy(vc, n_levels):
    """Buggy formula from exp004_ff_gstudy.py: residual / 1."""
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
            divisor = 1
        else:
            divisor = prod(n_levels[o] for o in other) if other else 1
        sigma_delta += est / divisor
    g = sigma_item / (sigma_item + sigma_delta) if (sigma_item + sigma_delta) > 0 else 0.0
    return g, sigma_item, sigma_delta


def item_accuracy_profiles(df):
    """Per-model item accuracy vector (200 items)."""
    items = sorted(df["item_id"].unique())
    models = sorted(df["model"].unique())
    profiles = {}
    for m in models:
        acc = df[df["model"] == m].groupby("item_id")["correct"].mean()
        profiles[m] = np.array([acc.get(i, np.nan) for i in items])
    return profiles, items


def pairwise_correlations(profiles):
    models = sorted(profiles.keys())
    n = len(models)
    corr = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            mask = ~(np.isnan(profiles[models[i]]) | np.isnan(profiles[models[j]]))
            corr[i, j] = np.corrcoef(profiles[models[i]][mask], profiles[models[j]][mask])[0, 1]
    return corr, models


def main():
    t0 = time.time()
    results = {}

    # === Step 1: Load all GSM8K data ===
    print("Loading GSM8K data...", flush=True)
    df_gsm = load_benchmark_data(GSM8K_FILES)
    print(f"  {len(df_gsm)} rows, {df_gsm['model'].nunique()} models", flush=True)
    print(f"  Models: {sorted(df_gsm['model'].unique())}", flush=True)

    # === Step 2: Bug confirmation ===
    print("\n=== Bug Confirmation: 8-model GSM8K ===", flush=True)
    vc8, nl8 = henderson_i(df_gsm)
    g_correct, st_c, sd_c = g_item_correct(vc8, nl8)
    g_buggy, st_b, sd_b = g_item_buggy(vc8, nl8)

    non_item_prod = prod(nl8[f] for f in FACETS if f != "item_id")
    print(f"  residual = {vc8['residual']:.6f}", flush=True)
    print(f"  prod(non_item) = {non_item_prod}", flush=True)
    print(f"  residual/prod = {vc8['residual']/non_item_prod:.8f}", flush=True)
    print(f"  residual/1    = {vc8['residual']:.8f}", flush=True)
    print(f"  G_item (correct, /prod): {g_correct:.6f}  sigma_delta={sd_c:.8f}", flush=True)
    print(f"  G_item (buggy, /1):      {g_buggy:.6f}  sigma_delta={sd_b:.8f}", flush=True)
    print(f"  Reported 8-model G_item: 0.283713", flush=True)
    print(f"  Reported 4-model G_item: 0.728948", flush=True)

    results["step2_bug_confirmation"] = {
        "eight_model_correct_G": round(g_correct, 6),
        "eight_model_buggy_G": round(g_buggy, 6),
        "reported_8model_G": 0.283713,
        "reported_4model_G": 0.728948,
        "residual": round(vc8["residual"], 10),
        "prod_non_item": non_item_prod,
        "bug_location": "exp004_ff_gstudy.py:compute_g_item line ~120, divisor=1 for residual",
        "correct_divisor": f"prod(non_item_facets) = {non_item_prod}",
    }

    # === Step 2b: 4-model subset verification ===
    print("\n=== 4-Model Subset Verification ===", flush=True)
    original_4 = ["Llama-3.1-8B", "Mistral-7B-v0.3", "Qwen3-8B", "Gemma-2-9B"]
    df_4sub = df_gsm[df_gsm["model"].isin(original_4)].reset_index(drop=True)
    vc4, nl4 = henderson_i(df_4sub)
    g4_correct, _, _ = g_item_correct(vc4, nl4)
    g4_buggy, _, _ = g_item_buggy(vc4, nl4)
    print(f"  4-model subset G_item (correct): {g4_correct:.6f}", flush=True)
    print(f"  4-model subset G_item (buggy):   {g4_buggy:.6f}", flush=True)
    print(f"  Original 4-model G_item:         0.728948", flush=True)

    results["step2b_4model_subset"] = {
        "subset_correct_G": round(g4_correct, 6),
        "subset_buggy_G": round(g4_buggy, 6),
        "original_4model_G": 0.728948,
        "match": abs(g4_correct - 0.728948) < 0.01,
    }

    # === Step 3: Incremental model analysis (correct formula) ===
    print("\n=== Step 3: Incremental Model Addition ===", flush=True)
    add_order = ["Llama-3.1-8B", "Mistral-7B-v0.3", "Qwen3-8B", "Gemma-2-9B",
                 "InternLM2.5-7B", "DeepSeek-7B", "OLMo-2-7B", "Yi-1.5-9B"]
    incremental = []
    for k in range(4, len(add_order) + 1):
        models_k = add_order[:k]
        df_k = df_gsm[df_gsm["model"].isin(models_k)].reset_index(drop=True)
        if df_k["model"].nunique() < k:
            print(f"  {k} models: only {df_k['model'].nunique()} found, skip")
            continue
        vc_k, nl_k = henderson_i(df_k)
        g_c, si_c, sd_c = g_item_correct(vc_k, nl_k)
        g_b, si_b, sd_b = g_item_buggy(vc_k, nl_k)
        added = add_order[k-1] if k > 4 else "base-4"
        total_var = sum(vc_k.values())
        item_pct = vc_k["item_id"] / total_var * 100 if total_var > 0 else 0
        mi_pct = vc_k.get("model:item_id", 0) / total_var * 100 if total_var > 0 else 0
        res_pct = vc_k["residual"] / total_var * 100 if total_var > 0 else 0
        print(f"  {k} models (+{added:20s}): G_correct={g_c:.4f}  G_buggy={g_b:.4f}  "
              f"item%={item_pct:.1f}  m:i%={mi_pct:.1f}  res%={res_pct:.1f}", flush=True)
        incremental.append({
            "n_models": k,
            "added_model": added,
            "G_item_correct": round(g_c, 6),
            "G_item_buggy": round(g_b, 6),
            "sigma_item": round(si_c, 8),
            "sigma_delta_correct": round(sd_c, 8),
            "sigma_delta_buggy": round(sd_b, 8),
            "item_pct": round(item_pct, 2),
            "model_item_pct": round(mi_pct, 2),
            "residual_pct": round(res_pct, 2),
        })
    results["step3_incremental_gsm8k"] = incremental

    # === Step 4: Pairwise item accuracy correlations ===
    print("\n=== Step 4: Pairwise Item Accuracy Correlations (GSM8K) ===", flush=True)
    profiles, items = item_accuracy_profiles(df_gsm)
    corr, corr_models = pairwise_correlations(profiles)
    print(f"  {'':20s}", end="")
    for m in corr_models:
        print(f"  {m[:8]:>8s}", end="")
    print()
    for i, m in enumerate(corr_models):
        print(f"  {m:20s}", end="")
        for j in range(len(corr_models)):
            print(f"  {corr[i,j]:8.3f}", end="")
        print()

    # Mean off-diagonal correlation
    n_m = len(corr_models)
    off_diag = [corr[i,j] for i in range(n_m) for j in range(n_m) if i != j]
    mean_corr = np.mean(off_diag)
    print(f"\n  Mean off-diagonal r = {mean_corr:.4f}")

    # Original 4 vs new 4 comparison
    orig_idx = [i for i, m in enumerate(corr_models) if m in original_4]
    new_idx = [i for i, m in enumerate(corr_models) if m not in original_4]
    orig_corrs = [corr[i,j] for i in orig_idx for j in orig_idx if i != j]
    cross_corrs = [corr[i,j] for i in orig_idx for j in new_idx]
    new_corrs = [corr[i,j] for i in new_idx for j in new_idx if i != j]
    print(f"  Mean r (orig 4x4): {np.mean(orig_corrs):.4f}")
    print(f"  Mean r (cross):    {np.mean(cross_corrs):.4f}")
    print(f"  Mean r (new 4x4):  {np.mean(new_corrs):.4f}")

    results["step4_correlations"] = {
        "models": corr_models,
        "correlation_matrix": [[round(corr[i,j], 4) for j in range(n_m)] for i in range(n_m)],
        "mean_off_diagonal": round(mean_corr, 4),
        "mean_original_4": round(np.mean(orig_corrs), 4),
        "mean_cross": round(np.mean(cross_corrs), 4),
        "mean_new_4": round(np.mean(new_corrs), 4),
    }

    # === Step 5: MMLU comparison ===
    print("\n=== Step 5: MMLU Incremental (Correct Formula) ===", flush=True)
    df_mmlu = load_benchmark_data(MMLU_FILES)
    print(f"  {len(df_mmlu)} rows, {df_mmlu['model'].nunique()} models", flush=True)
    mmlu_incremental = []
    for k in range(4, len(add_order) + 1):
        models_k = add_order[:k]
        df_k = df_mmlu[df_mmlu["model"].isin(models_k)].reset_index(drop=True)
        actual_n = df_k["model"].nunique()
        if actual_n < 4:
            continue
        vc_k, nl_k = henderson_i(df_k)
        g_c, _, _ = g_item_correct(vc_k, nl_k)
        g_b, _, _ = g_item_buggy(vc_k, nl_k)
        added = add_order[k-1] if k > 4 else "base-4"
        print(f"  {actual_n} models (+{added:20s}): G_correct={g_c:.4f}  G_buggy={g_b:.4f}", flush=True)
        mmlu_incremental.append({
            "n_models": actual_n,
            "added_model": added,
            "G_item_correct": round(g_c, 6),
            "G_item_buggy": round(g_b, 6),
        })
    results["step5_mmlu_incremental"] = mmlu_incremental

    # === Summary ===
    results["conclusion"] = {
        "root_cause": "BUG in exp004_ff_gstudy.py: compute_g_item divides residual by 1 instead of prod(non_item_facet_levels)",
        "impact": "sigma_delta inflated ~2300x for residual term, causing G_item to appear much lower than reality",
        "corrected_8model_gsm8k_G": results["step2_bug_confirmation"]["eight_model_correct_G"],
        "real_phenomenon": "After bug fix, 4→8 model G_item change is small and should be verified in step3",
    }

    # Save
    out_path = Path("results/exp004_8model_analysis/gitem_consistency_check.json")
    out_path.parent.mkdir(parents=True, exist_ok=True)
    with open(out_path, "w") as f:
        json.dump(results, f, indent=2, default=str)
    print(f"\nSaved -> {out_path}")
    print(f"Runtime: {time.time()-t0:.1f}s")


if __name__ == "__main__":
    main()
