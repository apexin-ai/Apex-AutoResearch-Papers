"""D-study bootstrap CI propagation for all 5 benchmarks.

Re-runs 1000 item-level bootstrap resamples, saves per-replicate
variance components, and propagates CIs to D-study n(G>=0.80).

Usage:
  cd .
  python scripts/dstudy_bootstrap_ci_propagation.py
"""

import json, sys, time, math, gzip, base64, hashlib
from itertools import combinations
from math import prod, ceil
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

# HellaSwag OLMo/Yi base64 data (2-temp version)
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
    cols = ["model", "temperature", "prompt_template", "seed",
            "ordering", "item_id", "correct", "benchmark"]

    if benchmark == "hellaswag":
        for m in LOCAL_MODELS:
            path = data_path / f"{m}_hellaswag.jsonl"
            if not path.exists():
                print(f"  WARNING: missing {path}", flush=True)
                continue
            df = pd.read_json(path, lines=True)
            df["model"] = df["model"].apply(normalize_model_name)
            df["temperature"] = df["temperature"].round(1)
            df = df[df["temperature"].isin([0.0, 0.7])]
            frames.append(df[cols])

        sample_df = frames[0] if frames else None
        if sample_df is not None:
            item_ids = sorted(sample_df["item_id"].unique())
            n_bits = len(HS_TEMPERATURES) * len(HS_PROMPTS) * len(HS_SEEDS) * len(HS_ORDERINGS) * len(item_ids)
            olmo_bits = decode_binary(OLMO_B64, n_bits, OLMO_SUM, OLMO_MD5)
            olmo_df = reconstruct_hellaswag_df(normalize_model_name(OLMO_MODEL), olmo_bits, item_ids)
            frames.append(olmo_df)
            yi_bits = decode_binary(YI_B64, n_bits, YI_SUM, YI_MD5)
            yi_df = reconstruct_hellaswag_df(normalize_model_name(YI_MODEL), yi_bits, item_ids)
            frames.append(yi_df)
    else:
        model_files = [f"{m}_{benchmark}.jsonl" for m in LOCAL_MODELS]
        model_files += [f"olmo_{benchmark}.jsonl", f"yi_{benchmark}.jsonl"]
        for mf in model_files:
            path = data_path / mf
            if not path.exists():
                print(f"  WARNING: missing {path}", flush=True)
                continue
            df = pd.read_json(path, lines=True)
            df["model"] = df["model"].apply(normalize_model_name)
            df["temperature"] = df["temperature"].round(1)
            frames.append(df[cols])

    combined = pd.concat(frames, ignore_index=True)
    for f in FACETS:
        combined[f] = combined[f].astype(str)
    return combined


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


def compute_dstudy(vc, n_levels, n_actual=200):
    """Compute multi-facet and single-condition D-study from variance components."""
    tau = vc.get("item_id", 0.0)
    if tau <= 0:
        return {"multi_n": 10000, "single_n": 10000, "ratio": 1.0}

    non_item_facets = [f for f in DIM_ORDER if f != "item_id" and f in n_levels]

    # Extract ×item interaction components
    item_interactions = {}
    for f in non_item_facets:
        key1 = f"{f}:item_id"
        key2 = f"item_id:{f}"
        item_interactions[f] = vc.get(key1, vc.get(key2, 0.0))
    residual = vc.get("residual", 0.0)

    # Multi-facet: divide each ×item by its facet level count
    delta_multi = sum(item_interactions[f] / n_levels[f] for f in non_item_facets)
    delta_multi += residual / prod(n_levels[f] for f in non_item_facets)

    # Single-condition: all facet levels = 1
    delta_single = sum(item_interactions[f] for f in non_item_facets)
    delta_single += residual

    # n(G>=0.80) = ceil(4 * delta * n_actual / tau)
    conditions = prod(n_levels[f] for f in non_item_facets)
    sigma2_Delta_multi = delta_multi * n_actual
    sigma2_Delta_single = delta_single * n_actual

    multi_n = ceil(4.0 * sigma2_Delta_multi / tau)
    single_n = ceil(4.0 * sigma2_Delta_single / tau)

    multi_n = min(multi_n, 10000)
    single_n = min(single_n, 10000)

    ratio = single_n / multi_n if multi_n > 0 else float('inf')

    return {
        "multi_n": multi_n,
        "single_n": single_n,
        "ratio": ratio,
        "conditions": conditions,
        "delta_multi": delta_multi,
        "delta_single": delta_single,
    }


def run_benchmark(data_dir, benchmark):
    t0 = time.time()
    print(f"\n{'='*60}", flush=True)
    print(f"Benchmark: {benchmark}", flush=True)
    print(f"{'='*60}", flush=True)

    print("Loading data...", flush=True)
    df = load_benchmark_data(data_dir, benchmark)
    models = sorted(df["model"].unique())
    items = sorted(df["item_id"].unique())
    print(f"  {len(models)} models, {len(items)} items, {len(df)} records", flush=True)

    dim_levels = {}
    for f in DIM_ORDER:
        vals = sorted(df[f].unique())
        dim_levels[f] = vals
    dim_sizes = [len(v) for v in dim_levels.values()]
    n_levels = dict(zip(DIM_ORDER, dim_sizes))

    print("Building tensor...", flush=True)
    Y = build_tensor(df, dim_levels)
    print(f"  shape={Y.shape}, mean={Y.mean():.6f}, size={Y.size}", flush=True)

    # Point estimate
    print("Henderson I (point estimate)...", flush=True)
    vc, _ = henderson_i_from_tensor(Y, dim_sizes)
    total_var = sum(vc.values())
    dstudy_point = compute_dstudy(vc, n_levels)

    print(f"  tau={vc.get('item_id', 0):.10f}", flush=True)
    print(f"  multi_facet: n_G80={dstudy_point['multi_n']}, conditions={dstudy_point['conditions']}", flush=True)
    print(f"  single_cond: n_G80={dstudy_point['single_n']}", flush=True)
    print(f"  ratio: {dstudy_point['ratio']:.1f}x", flush=True)

    # Bootstrap
    print(f"\nBootstrap ({N_BOOT} iterations)...", flush=True)
    rng = np.random.default_rng(SEED)
    n_items = len(items)

    boot_multi_n = []
    boot_single_n = []
    boot_ratio = []
    boot_vc = []

    for b in range(N_BOOT):
        if b % 200 == 0:
            print(f"  iter {b}/{N_BOOT} ({time.time()-t0:.1f}s)", flush=True)
        idx = rng.choice(n_items, size=n_items, replace=True)
        Y_b = Y[:, :, :, :, :, idx]
        vc_b, nl_b = henderson_i_from_tensor(Y_b, dim_sizes)
        ds_b = compute_dstudy(vc_b, nl_b)
        boot_multi_n.append(ds_b["multi_n"])
        boot_single_n.append(ds_b["single_n"])
        boot_ratio.append(ds_b["ratio"])
        boot_vc.append(vc_b)

    print(f"  Done ({time.time()-t0:.1f}s)", flush=True)

    boot_multi_n = np.array(boot_multi_n)
    boot_single_n = np.array(boot_single_n)
    boot_ratio = np.array(boot_ratio)

    result = {
        "benchmark": benchmark,
        "n_models": len(models),
        "n_items": n_items,
        "n_levels": {k: int(v) for k, v in n_levels.items()},
        "multi_facet": {
            "point": int(dstudy_point["multi_n"]),
            "ci_lower": int(np.percentile(boot_multi_n, 2.5)),
            "ci_upper": int(np.percentile(boot_multi_n, 97.5)),
            "conditions": int(dstudy_point["conditions"]),
        },
        "single_condition": {
            "point": int(dstudy_point["single_n"]),
            "ci_lower": int(np.percentile(boot_single_n, 2.5)),
            "ci_upper": int(np.percentile(boot_single_n, 97.5)),
        },
        "ratio": {
            "point": round(dstudy_point["ratio"], 1),
            "ci_lower": round(float(np.percentile(boot_ratio, 2.5)), 1),
            "ci_upper": round(float(np.percentile(boot_ratio, 97.5)), 1),
        },
    }

    print(f"\n  Multi:   {result['multi_facet']['point']} [{result['multi_facet']['ci_lower']}, {result['multi_facet']['ci_upper']}]", flush=True)
    print(f"  Single:  {result['single_condition']['point']} [{result['single_condition']['ci_lower']}, {result['single_condition']['ci_upper']}]", flush=True)
    print(f"  Ratio:   {result['ratio']['point']}x [{result['ratio']['ci_lower']}, {result['ratio']['ci_upper']}]", flush=True)

    return result


def main():
    data_dir = "results/exp002"
    out_dir = Path("results/exp004_8model_analysis")
    out_dir.mkdir(parents=True, exist_ok=True)

    t_total = time.time()
    all_results = {}

    for bm in BENCHMARKS:
        result = run_benchmark(data_dir, bm)
        all_results[bm] = result

    # Aggregate
    mc_benchmarks = ["mmlu", "arc", "hellaswag"]
    ff_benchmarks = ["gsm8k", "math"]

    mc_ratios = [all_results[b]["ratio"]["point"] for b in mc_benchmarks]
    ff_ratios = [all_results[b]["ratio"]["point"] for b in ff_benchmarks]

    # For aggregate CI, use per-benchmark CIs
    mc_ratio_lowers = [all_results[b]["ratio"]["ci_lower"] for b in mc_benchmarks]
    mc_ratio_uppers = [all_results[b]["ratio"]["ci_upper"] for b in mc_benchmarks]
    ff_ratio_lowers = [all_results[b]["ratio"]["ci_lower"] for b in ff_benchmarks]
    ff_ratio_uppers = [all_results[b]["ratio"]["ci_upper"] for b in ff_benchmarks]

    output = {
        "n_bootstrap": N_BOOT,
        "seed": SEED,
        "benchmarks": {bm: all_results[bm] for bm in BENCHMARKS},
        "aggregate": {
            "mc_ratio_mean": {
                "point": round(np.mean(mc_ratios), 1),
                "ci_lower": round(np.mean(mc_ratio_lowers), 1),
                "ci_upper": round(np.mean(mc_ratio_uppers), 1),
            },
            "ff_ratio_mean": {
                "point": round(np.mean(ff_ratios), 1),
                "ci_lower": round(np.mean(ff_ratio_lowers), 1),
                "ci_upper": round(np.mean(ff_ratio_uppers), 1),
            },
        },
    }

    out_path = out_dir / "dstudy_bootstrap_ci.json"
    with open(out_path, "w") as f:
        json.dump(output, f, indent=2)
    print(f"\n=> Saved: {out_path}", flush=True)

    # Verification table
    expected = {
        "arc": (98, 1078, 11.0),
        "hellaswag": (118, 1403, 11.9),
        "gsm8k": (128, 2768, 21.6),
        "math": (101, 2160, 21.4),
    }

    print(f"\n{'='*72}")
    print(f"{'Benchmark':<12} {'Multi':>6} {'expect':>7} {'Single':>7} {'expect':>7} {'Ratio':>6} {'expect':>7}")
    print("-" * 72)
    for bm in BENCHMARKS:
        r = all_results[bm]
        m = r["multi_facet"]["point"]
        s = r["single_condition"]["point"]
        rat = r["ratio"]["point"]
        if bm in expected:
            em, es, er = expected[bm]
            m_ok = "OK" if m == em else f"DIFF({em})"
            s_ok = "OK" if s == es else f"DIFF({es})"
            r_ok = "OK" if abs(rat - er) < 0.2 else f"DIFF({er})"
            print(f"{bm:<12} {m:>6} {m_ok:>7} {s:>7} {s_ok:>7} {rat:>5.1f}x {r_ok:>7}")
        else:
            print(f"{bm:<12} {m:>6}     N/A {s:>7}     N/A {rat:>5.1f}x     N/A")

    print(f"\n{'Benchmark':<12} {'Multi CI':>24} {'Single CI':>24} {'Ratio CI':>20}")
    print("-" * 82)
    for bm in BENCHMARKS:
        r = all_results[bm]
        mc = r["multi_facet"]
        sc = r["single_condition"]
        rc = r["ratio"]
        print(f"{bm:<12} {mc['point']:>5} [{mc['ci_lower']:>5}, {mc['ci_upper']:>5}]"
              f"  {sc['point']:>5} [{sc['ci_lower']:>5}, {sc['ci_upper']:>5}]"
              f"  {rc['point']:>5.1f}x [{rc['ci_lower']:>5.1f}, {rc['ci_upper']:>5.1f}]")

    print(f"\nTotal runtime: {time.time()-t_total:.1f}s", flush=True)


if __name__ == "__main__":
    main()
