"""Henderson I bootstrap CI for all 5 benchmarks (1000 resamples, item-level).

Outputs one JSON per benchmark to:
  results/exp004_8model_analysis/bootstrap_ci_{benchmark}.json

Usage:
  cd .
  python scripts/exp004_bootstrap_ci_all.py
"""

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
LOCAL_MODELS = ["llama", "mistral", "qwen", "gemma", "internlm", "deepseek"]
N_BOOT = 1000
SEED = 42

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
                        rows.append({"model": model_name, "temperature": temp,
                                     "prompt_template": pt, "seed": seed,
                                     "ordering": ordering, "item_id": item_id,
                                     "correct": correct_bits[idx], "benchmark": "hellaswag"})
                        idx += 1
    return pd.DataFrame(rows)


def load_benchmark_data(data_dir, benchmark):
    data_path = Path(data_dir)
    frames = []

    if benchmark == "hellaswag":
        for m in LOCAL_MODELS:
            path = data_path / f"{m}_hellaswag.jsonl"
            if not path.exists():
                print(f"  WARNING: missing {path}", flush=True)
                continue
            df = pd.read_json(path, lines=True)
            if "top_logprobs" in df.columns:
                df.drop(columns=["top_logprobs"], inplace=True)
            df["model"] = df["model"].map(normalize_model_name).fillna(df["model"])
            df["temperature"] = df["temperature"].round(1)
            df = df[df["temperature"].isin([0.0, 0.7])]
            frames.append(df[["model", "temperature", "prompt_template", "seed",
                              "ordering", "item_id", "correct", "benchmark"]])

        item_ids = sorted(frames[0]["item_id"].unique().tolist()) if frames else []
        n_bits = len(HS_TEMPERATURES) * len(HS_PROMPTS) * len(HS_SEEDS) * len(HS_ORDERINGS) * HS_N_ITEMS
        olmo_bits = decode_binary(OLMO_B64, n_bits, OLMO_SUM, OLMO_MD5)
        yi_bits = decode_binary(YI_B64, n_bits, YI_SUM, YI_MD5)
        df_olmo = reconstruct_hellaswag_df(OLMO_MODEL, olmo_bits, item_ids)
        df_yi = reconstruct_hellaswag_df(YI_MODEL, yi_bits, item_ids)
        for d in [df_olmo, df_yi]:
            d["model"] = d["model"].map(normalize_model_name).fillna(d["model"])
        frames.extend([df_olmo, df_yi])
    else:
        all_models = LOCAL_MODELS + ["olmo", "yi"]
        for m in all_models:
            path = data_path / f"{m}_{benchmark}.jsonl"
            if not path.exists():
                print(f"  WARNING: missing {path}", flush=True)
                continue
            df = pd.read_json(path, lines=True)
            if "top_logprobs" in df.columns:
                df.drop(columns=["top_logprobs"], inplace=True)
            df["model"] = df["model"].map(normalize_model_name).fillna(df["model"])
            frames.append(df[["model", "temperature", "prompt_template", "seed",
                              "ordering", "item_id", "correct", "benchmark"]])

    df = pd.concat(frames, ignore_index=True)
    for f in FACETS:
        df[f] = df[f].astype(str)
    return df


def build_tensor(df, dim_levels):
    shape = [len(v) for v in dim_levels.values()]
    Y = np.full(shape, np.nan, dtype=np.float64)
    idx_maps = {name: {v: i for i, v in enumerate(vals)} for name, vals in dim_levels.items()}
    for _, row in df.iterrows():
        indices = tuple(idx_maps[name][row[name]] for name in dim_levels.keys())
        Y[indices] = row["correct"]
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


def run_benchmark(data_dir, benchmark):
    t0 = time.time()
    print(f"\n{'='*60}", flush=True)
    print(f"Benchmark: {benchmark}", flush=True)
    print(f"{'='*60}", flush=True)

    print("Loading data...", flush=True)
    df = load_benchmark_data(data_dir, benchmark)
    models = sorted(df["model"].unique().tolist())
    print(f"  {len(df)} records, {len(models)} models: {models}", flush=True)

    temps = sorted(df["temperature"].unique().tolist())
    prompts = sorted(df["prompt_template"].unique().tolist())
    seeds = sorted(df["seed"].unique().tolist())
    orderings = sorted(df["ordering"].unique().tolist())
    items = sorted(df["item_id"].unique().tolist())

    dim_levels = {"model": models, "temperature": temps, "prompt_template": prompts,
                  "seed": seeds, "ordering": orderings, "item_id": items}
    dim_sizes = [len(v) for v in dim_levels.values()]

    print(f"Building tensor {dim_sizes}...", flush=True)
    Y = build_tensor(df, dim_levels)
    n_levels = dict(zip(DIM_ORDER, dim_sizes))
    print(f"  shape={Y.shape}, mean={Y.mean():.6f}, size={Y.size}", flush=True)

    print("Henderson I (point estimate)...", flush=True)
    vc, _ = henderson_i_from_tensor(Y, dim_sizes)
    total_var = sum(vc.values())
    g_item, sigma_tau, sigma_delta = compute_g_item(vc, n_levels)

    print(f"  G_item={g_item:.6f}, total_var={total_var:.10f}", flush=True)
    for k in sorted(vc.keys(), key=lambda x: -vc[x]):
        pct = vc[k] / total_var * 100 if total_var > 0 else 0
        if pct >= 0.1:
            print(f"    {k:<30} {pct:>7.2f}%", flush=True)

    print(f"\nBootstrap ({N_BOOT} iterations)...", flush=True)
    rng = np.random.default_rng(SEED)
    n_items = len(items)
    boot_pcts = []
    boot_raws = []
    boot_g = []

    for b in range(N_BOOT):
        if b % 100 == 0:
            print(f"  iter {b}/{N_BOOT} ({time.time()-t0:.1f}s)", flush=True)
        idx = rng.choice(n_items, size=n_items, replace=True)
        Y_b = Y[:, :, :, :, :, idx]
        vc_b, nl_b = henderson_i_from_tensor(Y_b, dim_sizes)
        tot_b = sum(vc_b.values())
        pct_b = {k: v / tot_b * 100 if tot_b > 0 else 0 for k, v in vc_b.items()}
        g_b, _, _ = compute_g_item(vc_b, nl_b)
        boot_pcts.append(pct_b)
        boot_raws.append(vc_b)
        boot_g.append(g_b)

    print(f"  Done ({time.time()-t0:.1f}s)", flush=True)

    all_keys = set()
    for bp in boot_pcts:
        all_keys.update(bp.keys())

    components = {}
    for key in sorted(all_keys):
        pct_vals = np.array([bp.get(key, 0) for bp in boot_pcts])
        raw_vals = np.array([br.get(key, 0) for br in boot_raws])
        point_pct = vc[key] / total_var * 100 if total_var > 0 else 0
        components[key] = {
            "pct": round(point_pct, 4),
            "ci_lower": round(float(np.percentile(pct_vals, 2.5)), 4),
            "ci_upper": round(float(np.percentile(pct_vals, 97.5)), 4),
            "estimate": round(vc[key], 10),
            "raw_ci_lower": round(float(np.percentile(raw_vals, 2.5)), 10),
            "raw_ci_upper": round(float(np.percentile(raw_vals, 97.5)), 10),
        }

    g_arr = np.array(boot_g)
    g_item_out = {
        "value": round(g_item, 6),
        "ci_lower": round(float(np.percentile(g_arr, 2.5)), 6),
        "ci_upper": round(float(np.percentile(g_arr, 97.5)), 6),
    }

    output = {
        "benchmark": benchmark,
        "n_models": len(models),
        "models": models,
        "n_records": int(Y.size),
        "n_items": n_items,
        "n_bootstrap": N_BOOT,
        "n_levels": {k: int(v) for k, v in n_levels.items()},
        "grand_mean": round(float(Y.mean()), 6),
        "total_variance": round(total_var, 10),
        "components": {k: v for k, v in sorted(components.items(), key=lambda x: -x[1]["pct"])},
        "g_item": g_item_out,
        "sigma_tau": round(sigma_tau, 10),
        "sigma_delta": round(sigma_delta, 10),
        "runtime_seconds": round(time.time() - t0, 1),
    }

    print(f"\n{'Component':<30} {'%':>8} {'95% CI':>22}", flush=True)
    print("-" * 62, flush=True)
    for k in sorted(components.keys(), key=lambda x: -components[x]["pct"]):
        c = components[k]
        print(f"{k:<30} {c['pct']:>7.2f}% [{c['ci_lower']:>7.2f}, {c['ci_upper']:>7.02f}]", flush=True)
    print(f"\nG_item = {g_item_out['value']:.6f} [{g_item_out['ci_lower']:.6f}, {g_item_out['ci_upper']:.6f}]", flush=True)

    return output


def main():
    data_dir = "results/exp002"
    out_dir = Path("results/exp004_8model_analysis")
    out_dir.mkdir(parents=True, exist_ok=True)

    t_total = time.time()
    for bm in BENCHMARKS:
        result = run_benchmark(data_dir, bm)
        out_path = out_dir / f"bootstrap_ci_{bm}.json"
        with open(out_path, "w") as f:
            json.dump(result, f, indent=2, default=str)
        print(f"\n=> {out_path}", flush=True)

    print(f"\nAll done. Total: {time.time()-t_total:.1f}s", flush=True)


if __name__ == "__main__":
    main()
