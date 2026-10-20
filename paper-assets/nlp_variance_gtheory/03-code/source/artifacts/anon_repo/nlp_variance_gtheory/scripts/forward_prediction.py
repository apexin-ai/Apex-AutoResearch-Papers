"""Forward prediction validation: 4-model D-study -> 8-model G coefficient."""

import json, sys, time, gzip, base64, hashlib
from itertools import combinations
from math import prod
from pathlib import Path

import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from src.config.model_paths import normalize_model_name

FACETS = ["model", "temperature", "prompt_template", "seed", "ordering", "item_id"]
DIM_ORDER = ["model", "temperature", "prompt_template", "seed", "ordering", "item_id"]
BENCHMARKS = ["mmlu", "arc", "hellaswag", "gsm8k", "math"]
SOURCE_MODELS = {"Llama-3.1-8B", "Gemma-2-9B", "Mistral-7B-v0.3", "Qwen3-8B"}
LOCAL_MODELS = ["llama", "mistral", "qwen", "gemma", "internlm", "deepseek"]

OLMO_B64 = "H4sIAPGID2oC/+3YsWsaURwH8O0gQ/NfODg4Brp0CIUMGQLlBiGbhFss5xGOIniEbgGhbuIWQoaAB7ktLekQQoeKBNNSiCEVtTnE6YI3Fant3et7v3fqndUQvV/scvOHy/d8Pt/7fVOuxtWcdZGSje09p6uUBNe1+gUifi9HEEEIaCZUrUNMee1ScmJvP1TctkVOiFiPIIIwUDVUzSJsw71xupnixn2bbjg7SXdiAg+MJUBiCU/819ddxheF91a3uprrUNAbkmPSg6xHN1zBFh0AK4IIFoNqYjdnHZryeUN2Ysq+0HMtYtjs5owggsWhSQEuyIZMPimnq3/ohsvb4rcIIggD1byaZgP9eWOPHmT7MNBf2clfE1AJCx0Gm+PS8BXaBCLEd3kx8YUXIPxBIHM8odNhIsfCjU0GpS23zctPALohIeHBtsw/IAUDG3SvxF3C5xDG4WjABnq6ut5Ar5Qq7oAeZET8CTsRDbJa5wKgRUvDF1Ya3pFXdVzwhxdnvdVUkB8NWW2H/6nW8ShcrKPCC1Xb6ZvK2oBC1t+8EIEt4rjEBd8KCWo6/9XqdKA3M9cCG+jhkKnF0YBuam0I3UyJlQbShNt5CrQWg9ro9KHhaR4OxQQRePkxR+WHDqn9AzgsA3A9Cx71BFQyUwFIFyH8xEIGX4kbflEHk+0uJNx6++ojDPQ3q73hZkAGX+dkQK7sl+jAwo/oRX+k3LBiwjaDgwuB7rwF5YeITwLHA4l0vYJFB+H6AxCf+4lAieNf1CgcCaorbKBPTZn0EeEZgOTBxpMAO2R+pOT3/4Qjwqj8SDy8DRckOrw+vKPhEg9v//aHzwRzAQgsIkGFMz5MwCKSdaXoDfTJ2fB87icCpWGdlgZ2CeeViTYRDs5aPFzxwoX7htWHt8KDcpMN2xAuQflh4SvQihCBDdvkTonRQ+azciqwRYzb/D/beOANkBBe5Is4bHc48BfEFh+fIBwAAA=="
YI_B64 = "H4sIAAeJD2oC/+3Yv2/TQBQH8Al1ZOyYP4GJdmumKlPFgBADgxWohdSSZKhCBivxX1AxMlUwWkVVgSFEtRqPDFA6FoX8ECptBpKYSpFR4p4fd74zaRJfHKfnoqKu/ej53dlX+32jNSBb0NGxXK4AUqE4B2CCCjlH44N5AxMg958s93L72K5B1jFBTu1WTZR7hCF10lNeHIJGAODJCJg+kKewPQYZHuR5PbiXYqsKguQUFXkeBC03xKryAaAFNE9Gcq/Cr2rm56HVzGxGR3LKqLfRom19BOiChFSDQg9DBYNiJShAECAGNgPgVUQBl2+OIuhxFbckwh4zPdrtLciu0XOF0KJqJRz8IovhV5kPAB8kH5ibWBETUvHvQbpZrh/s1QhAUjbqJnoOxQT5QMbhtzMC1g2MwdNrtdyiwA0GQwlDwUZJOY4PXE597/aQQO9zwGAAw9DgVTR4FYMe014qfPNIKiD0vQoPUW4w8EFdGuiq8EBvoO/yEhvoHTrQe3DMgxAVLFo2U+U6ixkqOdQqiATcXNX3T7xggjfYxH/esAUDbo6h7oWfJmnuB2ZoGLoU+bD4VgiE5Cj0BUJpy3Hz4MputYNy94u3nNazMzzQN9660BgAzAqvWOZ8TEMDmfouBpPpIBVQ8brmkGDCmm8Ul6G1ejYJGsOgEPjhUzEE/bvn5jd5ZafaaT/4ZS07n1ffKZufYgLBjWQ/cT7f8TYIF7LaECAewLTQpjDnXmrTD2BWKNU6bPD6igcvpZjooPOedKAYAuALhnsYyGEo6PYqSxOnR+adLsRwzGAgCwANN1/Xeycpo0pzrYm6SKopgqDnQdptXm0RODrc7/ZuH/AhTiATssLMpt/YXj4/fQlGlwzChj8gHkAgwF+YnwxoFiixgV42KoM8KJGvGoWkACChoaADfSFjmCehIc7ShCDQtkx6GMpkg27zphtMBIObtvcxLKjWwzCACExxKfKgyAZZxbyXz68Z7CF8GAxyGPCD8kKDBB8cHvTDA3nJqOOhAUAgkAFyfTzjTIC90ECaZ64SFqKDtD0OjkAgt33NG+hVlQ7bXpoQCAXanL4A6I/9IBboACkvYbgQfmwKwANcUeaBb8WgufePY/fFwWgPiwH0hQK7icB+dJoK0qHgDyeAYD4gHAAA"
OLMO_SUM, YI_SUM = 36500, 44242
OLMO_MD5, YI_MD5 = "46893fa2e0bd1bdc336ab86b97a2974f", "d6ec052ecc8bbbdf37b8e8836c9b88b6"
OLMO_MODEL = "allenai/OLMo-2-1124-7B-Instruct"
YI_MODEL = "01-ai/Yi-1.5-9B-Chat"
HS_TEMPERATURES = [0.0, 0.7]
HS_PROMPTS = [1, 2, 3, 4, 5, 6]
HS_SEEDS = [42, 123, 456, 789, 1024, 2048]
HS_ORDERINGS = [1, 2, 3, 4]
HS_N_ITEMS = 200


def decode_binary(b64_str, n_bits, expected_sum, expected_md5):
    raw = gzip.decompress(base64.b64decode(b64_str))
    assert hashlib.md5(raw).hexdigest() == expected_md5
    bits = []
    for byte_val in raw:
        for j in range(8):
            if len(bits) < n_bits:
                bits.append((byte_val >> (7 - j)) & 1)
    assert sum(bits) == expected_sum
    return bits


def reconstruct_hellaswag_df(model_name, correct_bits, item_ids):
    rows = []
    idx = 0
    for temp in HS_TEMPERATURES:
        for pt in HS_PROMPTS:
            for seed in HS_SEEDS:
                for ordering in HS_ORDERINGS:
                    for item_id in item_ids:
                        rows.append({
                            "model": model_name,
                            "temperature": temp,
                            "prompt_template": pt,
                            "seed": seed,
                            "ordering": ordering,
                            "item_id": item_id,
                            "correct": correct_bits[idx],
                            "benchmark": "hellaswag",
                        })
                        idx += 1
    return pd.DataFrame(rows)


def normalize_facets(df):
    """Normalize facet columns to consistent string representation."""
    for col in ["temperature"]:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors="coerce").round(4)
    for col in ["prompt_template", "seed", "ordering"]:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors="coerce").astype(int)
    for f in FACETS:
        df[f] = df[f].astype(str)
    return df


def load_benchmark_data(data_dir, benchmark):
    frames = []
    for model_key in LOCAL_MODELS:
        path = Path(data_dir) / f"{model_key}_{benchmark}.jsonl"
        if not path.exists():
            continue
        df = pd.read_json(path, lines=True)
        if "top_logprobs" in df.columns:
            df.drop(columns=["top_logprobs"], inplace=True)
        df["model"] = df["model"].map(normalize_model_name).fillna(df["model"])
        frames.append(df[["model", "temperature", "prompt_template", "seed",
                          "ordering", "item_id", "correct", "benchmark"]])

    if benchmark == "hellaswag":
        hs_items = sorted(frames[0]["item_id"].unique().tolist()) if frames else list(range(HS_N_ITEMS))
        n_bits = len(HS_TEMPERATURES)*len(HS_PROMPTS)*len(HS_SEEDS)*len(HS_ORDERINGS)*HS_N_ITEMS
        olmo_bits = decode_binary(OLMO_B64, n_bits, OLMO_SUM, OLMO_MD5)
        yi_bits = decode_binary(YI_B64, n_bits, YI_SUM, YI_MD5)
        frames.append(reconstruct_hellaswag_df(normalize_model_name(OLMO_MODEL), olmo_bits, hs_items))
        frames.append(reconstruct_hellaswag_df(normalize_model_name(YI_MODEL), yi_bits, hs_items))
    else:
        for extra_model in ["olmo", "yi"]:
            path = Path(data_dir) / f"{extra_model}_{benchmark}.jsonl"
            if not path.exists():
                continue
            df = pd.read_json(path, lines=True)
            if "top_logprobs" in df.columns:
                df.drop(columns=["top_logprobs"], inplace=True)
            df["model"] = df["model"].map(normalize_model_name).fillna(df["model"])
            frames.append(df[["model", "temperature", "prompt_template", "seed",
                              "ordering", "item_id", "correct", "benchmark"]])

    df = pd.concat(frames, ignore_index=True)
    df = normalize_facets(df)
    return df


def build_tensor_fast(df, dim_levels):
    shape = [len(v) for v in dim_levels.values()]
    Y = np.full(shape, np.nan, dtype=np.float64)
    idx_maps = {name: {v: i for i, v in enumerate(vals)} for name, vals in dim_levels.items()}
    dim_names = list(dim_levels.keys())
    indices = []
    for name in dim_names:
        mapped = df[name].map(idx_maps[name])
        n_unmapped = mapped.isna().sum()
        if n_unmapped > 0:
            print(f"  WARNING: {n_unmapped} unmapped values in {name}", flush=True)
            unmapped_vals = df[name][mapped.isna()].unique()[:5]
            available_vals = list(idx_maps[name].keys())[:5]
            print(f"    unmapped samples: {unmapped_vals.tolist()}", flush=True)
            print(f"    available samples: {available_vals}", flush=True)
            mapped = mapped.fillna(-1)
        indices.append(mapped.astype(int).values)
    
    valid = np.ones(len(df), dtype=bool)
    for idx_arr in indices:
        valid &= (idx_arr >= 0)
    
    valid_indices = tuple(idx_arr[valid] for idx_arr in indices)
    Y[valid_indices] = df["correct"].values[valid]
    
    n_nan = np.isnan(Y).sum()
    if n_nan > 0:
        print(f"  WARNING: {n_nan} NaN cells in tensor, filling with 0", flush=True)
        Y = np.nan_to_num(Y, nan=0.0)
    return Y


def henderson_i_from_tensor(Y, dim_sizes, dim_names=None):
    grand_mean = Y.mean()
    N = Y.size
    n_dims = len(dim_sizes)
    if dim_names is None:
        dim_names = DIM_ORDER[:n_dims]

    effects = {}
    for d, name in enumerate(dim_names):
        ax = tuple(i for i in range(n_dims) if i != d)
        gm = Y.mean(axis=ax)
        n_per = N // dim_sizes[d]
        ss = float(n_per * ((gm - grand_mean) ** 2).sum())
        df_eff = dim_sizes[d] - 1
        effects[name] = {"ss": ss, "df": df_eff, "ms": ss / df_eff if df_eff > 0 else 0.0}

    for (d1, n1), (d2, n2) in combinations(enumerate(zip(dim_names, dim_sizes)), 2):
        di, ni = d1, n1[1]
        dj, nj = d2, n2[1]
        name_i, name_j = n1[0], n2[0]
        ax = tuple(k for k in range(n_dims) if k != di and k != dj)
        cell_mean = Y.mean(axis=ax)
        main_i = Y.mean(axis=tuple(k for k in range(n_dims) if k != di))
        main_j = Y.mean(axis=tuple(k for k in range(n_dims) if k != dj))
        n_per = N // (ni * nj)
        interaction = cell_mean - main_i.reshape([-1 if k == 0 else 1 for k in range(cell_mean.ndim)]) \
                      - main_j.reshape([1 if k == 0 else -1 for k in range(cell_mean.ndim)]) + grand_mean
        ss = float(n_per * (interaction ** 2).sum())
        df_eff = (ni - 1) * (nj - 1)
        key = f"{name_i}:{name_j}"
        effects[key] = {"ss": ss, "df": df_eff, "ms": ss / df_eff if df_eff > 0 else 0.0}

    ss_total = float(((Y - grand_mean) ** 2).sum())
    ss_model = sum(e["ss"] for e in effects.values())
    ss_res = max(0.0, ss_total - ss_model)
    df_res = N - 1 - sum(e["df"] for e in effects.values())
    effects["residual"] = {"ss": ss_res, "df": df_res, "ms": ss_res / df_res if df_res > 0 else 0.0}

    ms_res = effects["residual"]["ms"]
    n_levels = dict(zip(dim_names, dim_sizes))
    vc = {}

    for fi, fj in combinations(dim_names, 2):
        key = f"{fi}:{fj}"
        coeff = prod(n_levels[f] for f in dim_names if f not in (fi, fj))
        raw = (effects[key]["ms"] - ms_res) / coeff if coeff > 0 else 0.0
        vc[key] = max(0.0, raw)

    for fi in dim_names:
        coeff_main = prod(n_levels[f] for f in dim_names if f != fi)
        ic = 0.0
        for fj in dim_names:
            if fj == fi:
                continue
            ik = f"{fi}:{fj}" if f"{fi}:{fj}" in vc else f"{fj}:{fi}"
            cij = prod(n_levels[f] for f in dim_names if f not in (fi, fj))
            ic += cij * vc[ik]
        raw = (effects[fi]["ms"] - ic - ms_res) / coeff_main if coeff_main > 0 else 0.0
        vc[fi] = max(0.0, raw)

    vc["residual"] = ms_res
    return vc, n_levels


def compute_g_item(vc, n_levels):
    tau = vc.get("item_id", 0.0)
    non_item_facets = [f for f in FACETS if f != "item_id"]
    delta = 0.0
    for comp, est in vc.items():
        if est == 0.0 or comp == "item_id":
            continue
        if comp == "residual":
            delta += est / prod(n_levels[f] for f in non_item_facets)
            continue
        parts = set(comp.split(":"))
        if "item_id" not in parts:
            continue
        other = [f for f in parts if f != "item_id"]
        delta += est / (prod(n_levels[f] for f in other) if other else 1)
    g = tau / (tau + delta) if (tau + delta) > 0 else 0.0
    return g, tau, delta


def run_forward_prediction(data_dir):
    results = {}

    for benchmark in BENCHMARKS:
        t0 = time.time()
        print(f"\n{'='*60}", flush=True)
        print(f"Benchmark: {benchmark}", flush=True)
        print(f"{'='*60}", flush=True)

        print("Loading data...", flush=True)
        df_all = load_benchmark_data(data_dir, benchmark)
        all_models = sorted(df_all["model"].unique().tolist())
        n_target = len(all_models)
        print(f"  All models ({n_target}): {all_models}", flush=True)

        # Get common facet levels from full dataset
        temps = sorted(df_all["temperature"].unique().tolist())
        prompts = sorted(df_all["prompt_template"].unique().tolist())
        seeds = sorted(df_all["seed"].unique().tolist())
        orderings = sorted(df_all["ordering"].unique().tolist())
        items = sorted(df_all["item_id"].unique().tolist())
        print(f"  Levels: T={len(temps)} P={len(prompts)} S={len(seeds)} O={len(orderings)} I={len(items)}", flush=True)

        # Step 1: 4-model G-study
        print("Step 1: 4-model G-study...", flush=True)
        df_4m = df_all[df_all["model"].isin(SOURCE_MODELS)].copy()
        models_4 = sorted(df_4m["model"].unique().tolist())
        assert len(models_4) == 4, f"Expected 4, got {len(models_4)}: {models_4}"

        dim_levels_4 = {"model": models_4, "temperature": temps, "prompt_template": prompts,
                        "seed": seeds, "ordering": orderings, "item_id": items}
        dim_sizes_4 = [len(v) for v in dim_levels_4.values()]
        Y_4 = build_tensor_fast(df_4m, dim_levels_4)
        n_levels_4 = dict(zip(DIM_ORDER, dim_sizes_4))

        vc_4, _ = henderson_i_from_tensor(Y_4, dim_sizes_4)
        total_var_4 = sum(vc_4.values())
        g_4, tau_4, delta_4 = compute_g_item(vc_4, n_levels_4)
        print(f"  G_item(4m) = {g_4:.6f}", flush=True)

        # Step 2: D-study prediction
        n_levels_pred = n_levels_4.copy()
        n_levels_pred["model"] = n_target
        g_pred, tau_pred, delta_pred = compute_g_item(vc_4, n_levels_pred)
        print(f"  G_predicted({n_target}m) = {g_pred:.6f}", flush=True)

        # Step 3: Actual G-study
        print("Step 3: Actual G-study...", flush=True)
        dim_levels_8 = {"model": all_models, "temperature": temps, "prompt_template": prompts,
                        "seed": seeds, "ordering": orderings, "item_id": items}
        dim_sizes_8 = [len(v) for v in dim_levels_8.values()]
        Y_8 = build_tensor_fast(df_all, dim_levels_8)
        n_levels_8 = dict(zip(DIM_ORDER, dim_sizes_8))

        vc_8, _ = henderson_i_from_tensor(Y_8, dim_sizes_8)
        g_8, tau_8, delta_8 = compute_g_item(vc_8, n_levels_8)
        print(f"  G_actual({n_target}m) = {g_8:.6f}", flush=True)

        delta_g = g_pred - g_8
        rel_err = abs(delta_g) / g_8 * 100 if g_8 > 0 else float('inf')
        print(f"  dG = {delta_g:+.6f} ({rel_err:.2f}%) [{time.time()-t0:.1f}s]", flush=True)

        source_components = {}
        for k in sorted(vc_4.keys(), key=lambda x: -vc_4[x]):
            pct = vc_4[k] / total_var_4 * 100 if total_var_4 > 0 else 0
            if pct >= 0.01:
                source_components[k] = round(vc_4[k], 10)

        results[benchmark] = {
            "n_models_source": 4,
            "n_models_target": n_target,
            "source_models": models_4,
            "target_models": all_models,
            "source_n_levels": {k: int(v) for k, v in n_levels_4.items()},
            "target_n_levels": {k: int(v) for k, v in n_levels_8.items()},
            "source_components": source_components,
            "source_total_variance": round(total_var_4, 10),
            "G_source_4model": round(g_4, 6),
            "G_predicted": round(g_pred, 6),
            "G_actual": round(g_8, 6),
            "delta_G": round(delta_g, 6),
            "abs_delta_G": round(abs(delta_g), 6),
            "relative_error_pct": round(rel_err, 2),
            "sigma_tau_source": round(tau_pred, 10),
            "sigma_delta_predicted": round(delta_pred, 10),
            "sigma_delta_actual": round(delta_8, 10),
        }

    abs_deltas = [r["abs_delta_G"] for r in results.values()]
    rel_errs = [r["relative_error_pct"] for r in results.values()]
    summary = {
        "mean_abs_delta_G": round(float(np.mean(abs_deltas)), 6),
        "max_abs_delta_G": round(float(np.max(abs_deltas)), 6),
        "min_abs_delta_G": round(float(np.min(abs_deltas)), 6),
        "mean_relative_error_pct": round(float(np.mean(rel_errs)), 2),
        "max_relative_error_pct": round(float(np.max(rel_errs)), 2),
    }

    output = {
        "method": "D-study forward prediction: 4-model variance components -> 8-model G coefficient",
        "source_models": sorted(SOURCE_MODELS),
        "description": "Variance components estimated from 4 exp-001 models, then D-study formula projects G_item at n_model=8. Compared with actual 8-model crossed G-study.",
        "benchmarks": results,
        "summary": summary,
    }

    print(f"\n{'='*80}", flush=True)
    print("FORWARD PREDICTION SUMMARY", flush=True)
    print(f"{'='*80}", flush=True)
    hdr = f"{'Benchmark':<12} {'n_src':>5} {'n_tgt':>5} {'G_4m':>8} {'G_pred':>8} {'G_actual':>8} {'dG':>8} {'Err%':>8}"
    print(hdr, flush=True)
    print("-" * len(hdr), flush=True)
    for bm, r in results.items():
        print(f"{bm:<12} {r['n_models_source']:>5} {r['n_models_target']:>5} "
              f"{r['G_source_4model']:>8.4f} {r['G_predicted']:>8.4f} {r['G_actual']:>8.4f} "
              f"{r['delta_G']:>+8.4f} {r['relative_error_pct']:>7.2f}%", flush=True)
    print("-" * len(hdr), flush=True)
    print(f"Mean |dG| = {summary['mean_abs_delta_G']:.4f}, "
          f"Max |dG| = {summary['max_abs_delta_G']:.4f}, "
          f"Mean Err = {summary['mean_relative_error_pct']:.2f}%", flush=True)

    return output


if __name__ == "__main__":
    data_dir = "results/exp002"
    output = run_forward_prediction(data_dir)

    out_dir = Path("results/exp004_8model_analysis/forward_prediction")
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / "forward_prediction_results.json"
    with open(out_path, "w") as f:
        json.dump(output, f, indent=2, default=str)
    print(f"\n=> Saved to {out_path}", flush=True)
