"""8-model Henderson I G-study for HellaSwag with bootstrap CI.
Optimized: pre-compute item-level tensor, vectorize bootstrap.
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

OLMO_B64 = "H4sIAPGID2oC/+3YsWsaURwH8O0gQ/NfODg4Brp0CIUMGQLlBiGbhFss5xGOIniEbgGhbuIWQoaAB7ktLekQQoeKBNNSiCEVtTnE6YI3Fant3et7v3fqndUQvV/scvOHy/d8Pt/7fVOuxtWcdZGSje09p6uUBNe1+gUifi9HEEEIaCZUrUNMee1ScmJvP1TctkVOiFiPIIIwUDVUzSJsw71xupnixn2bbjg7SXdiAg+MJUBiCU/819ddxheF91a3uprrUNAbkmPSg6xHN1zBFh0AK4IIFoNqYjdnHZryeUN2Ysq+0HMtYtjs5owggsWhSQEuyIZMPimnq3/ohsvb4rcIIggD1byaZgP9eWOPHmT7MNBf2clfE1AJCx0Gm+PS8BXaBCLEd3kx8YUXIPxBIHM8odNhIsfCjU0GpS23zctPALohIeHBtsw/IAUDG3SvxF3C5xDG4WjABnq6ut5Ar5Qq7oAeZET8CTsRDbJa5wKgRUvDF1Ya3pFXdVzwhxdnvdVUkB8NWW2H/6nW8ShcrKPCC1Xb6ZvK2oBC1t+8EIEt4rjEBd8KCWo6/9XqdKA3M9cCG+jhkKnF0YBuam0I3UyJlQbShNt5CrQWg9ro9KHhaR4OxQQRePkxR+WHDqn9AzgsA3A9Cx71BFQyUwFIFyH8xEIGX4kbflEHk+0uJNx6++ojDPQ3q73hZkAGX+dkQK7sl+jAwo/oRX+k3LBiwjaDgwuB7rwF5YeITwLHA4l0vYJFB+H6AxCf+4lAieNf1CgcCaorbKBPTZn0EeEZgOTBxpMAO2R+pOT3/4Qjwqj8SDy8DRckOrw+vKPhEg9v//aHzwRzAQgsIkGFMz5MwCKSdaXoDfTJ2fB87icCpWGdlgZ2CeeViTYRDs5aPFzxwoX7htWHt8KDcpMN2xAuQflh4SvQihCBDdvkTonRQ+azciqwRYzb/D/beOANkBBe5Is4bHc48BfEFh+fIBwAAA=="
YI_B64 = "H4sIAAeJD2oC/+3Yv2/TQBQH8Al1ZOyYP4GJdmumKlPFgBADgxWohdSSZKhCBivxX1AxMlUwWkVVgSFEtRqPDFA6FoX8ECptBpKYSpFR4p4fd74zaRJfHKfnoqKu/ej53dlX+32jNSBb0NGxXK4AUqE4B2CCCjlH44N5AxMg958s93L72K5B1jFBTu1WTZR7hCF10lNeHIJGAODJCJg+kKewPQYZHuR5PbiXYqsKguQUFXkeBC03xKryAaAFNE9Gcq/Cr2rm56HVzGxGR3LKqLfRom19BOiChFSDQg9DBYNiJShAECAGNgPgVUQBl2+OIuhxFbckwh4zPdrtLciu0XOF0KJqJRz8IovhV5kPAB8kH5ibWBETUvHvQbpZrh/s1QhAUjbqJnoOxQT5QMbhtzMC1g2MwdNrtdyiwA0GQwlDwUZJOY4PXE597/aQQO9zwGAAw9DgVTR4FYMe014qfPNIKiD0vQoPUW4w8EFdGuiq8EBvoO/yEhvoHTrQe3DMgxAVLFo2U+U6ixkqOdQqiATcXNX3T7xggjfYxH/esAUDbo6h7oWfJmnuB2ZoGLoU+bD4VgiE5Cj0BUJpy3Hz4MputYNy94u3nNazMzzQN9660BgAzAqvWOZ8TEMDmfouBpPpIBVQ8brmkGDCmm8Ul6G1ejYJGsOgEPjhUzEE/bvn5jd5ZafaaT/4ZS07n1ffKZufYgLBjWQ/cT7f8TYIF7LaECAewLTQpjDnXmrTD2BWKNU6bPD6igcvpZjooPOedKAYAuALhnsYyGEo6PYqSxOnR+adLsRwzGAgCwANN1/Xeycpo0pzrYm6SKopgqDnQdptXm0RODrc7/ZuH/AhTiATssLMpt/YXj4/fQlGlwzChj8gHkAgwF+YnwxoFiixgV42KoM8KJGvGoWkACChoaADfSFjmCehIc7ShCDQtkx6GMpkg27zphtMBIObtvcxLKjWwzCACExxKfKgyAZZxbyXz68Z7CF8GAxyGPCD8kKDBB8cHvTDA3nJqOOhAUAgkAFyfTzjTIC90ECaZ64SFqKDtD0OjkAgt33NG+hVlQ7bXpoQCAXanL4A6I/9IBboACkvYbgQfmwKwANcUeaBb8WgufePY/fFwWgPiwH0hQK7icB+dJoK0qHgDyeAYD4gHAAA"
OLMO_SUM, YI_SUM = 36500, 44242
OLMO_MD5, YI_MD5 = "46893fa2e0bd1bdc336ab86b97a2974f", "d6ec052ecc8bbbdf37b8e8836c9b88b6"
OLMO_MODEL = "allenai/OLMo-2-1124-7B-Instruct"
YI_MODEL = "01-ai/Yi-1.5-9B-Chat"
TEMPERATURES = [0.0, 0.7]
PROMPT_TEMPLATES = [1, 2, 3, 4, 5, 6]
SEEDS = [42, 123, 456, 789, 1024, 2048]
ORDERINGS = [1, 2, 3, 4]
N_ITEMS = 200


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


def reconstruct_df(model_name, correct_bits, item_ids):
    rows = []
    idx = 0
    for temp in TEMPERATURES:
        for pt in PROMPT_TEMPLATES:
            for seed in SEEDS:
                for ordering in ORDERINGS:
                    for item_id in item_ids:
                        rows.append({"model": model_name, "temperature": temp,
                                     "prompt_template": pt, "seed": seed,
                                     "ordering": ordering, "item_id": item_id,
                                     "correct": correct_bits[idx], "benchmark": "hellaswag"})
                        idx += 1
    return pd.DataFrame(rows)


def load_local_hellaswag(data_dir):
    models = ["llama", "mistral", "qwen", "gemma", "internlm", "deepseek"]
    frames = []
    for m in models:
        path = Path(data_dir) / f"{m}_hellaswag.jsonl"
        if not path.exists():
            continue
        df = pd.read_json(path, lines=True)
        if "top_logprobs" in df.columns:
            df.drop(columns=["top_logprobs"], inplace=True)
        df["model"] = df["model"].map(normalize_model_name).fillna(df["model"])
        frames.append(df[["model", "temperature", "prompt_template", "seed", "ordering", "item_id", "correct", "benchmark"]])
    return pd.concat(frames, ignore_index=True)


def henderson_i_from_tensor(Y, dim_sizes, dim_names=None):
    """Vectorized Henderson I on a pre-indexed tensor Y[m,t,p,s,o,i]."""
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
    tau = vc.get("item_id", 0)
    delta = 0.0
    for comp, est in vc.items():
        if comp == "item_id":
            continue
        if comp == "residual":
            delta += est / prod(n_levels[f] for f in FACETS if f != "item_id")
            continue
        parts = comp.split(":")
        if "item_id" not in parts:
            continue
        other = [f for f in parts if f != "item_id"]
        delta += est / (prod(n_levels[f] for f in other) if other else 1)
    g = tau / (tau + delta) if (tau + delta) > 0 else 0.0
    return g, tau, delta


def d_study_curve(vc, n_levels, item_counts):
    tau = vc.get("item_id", 0)
    n_actual = n_levels["item_id"]
    base_delta = 0.0
    for comp, est in vc.items():
        if comp == "item_id":
            continue
        if comp == "residual":
            base_delta += est / prod(n_levels[f] for f in FACETS if f != "item_id")
            continue
        parts = comp.split(":")
        if "item_id" not in parts:
            continue
        other = [f for f in parts if f != "item_id"]
        base_delta += est / (prod(n_levels[f] for f in other) if other else 1)
    curve = []
    for ni in item_counts:
        d = base_delta * (n_actual / ni)
        g = tau / (tau + d) if (tau + d) > 0 else 0.0
        curve.append({"n_items": ni, "G_item": round(g, 6)})
    return curve


def build_tensor(df, dim_levels):
    """Build a tensor from dataframe with known dimension levels."""
    shape = [len(v) for v in dim_levels.values()]
    Y = np.zeros(shape, dtype=np.float64)
    idx_maps = {name: {v: i for i, v in enumerate(vals)} for name, vals in dim_levels.items()}

    for _, row in df.iterrows():
        indices = tuple(idx_maps[name][row[name]] for name in dim_levels.keys())
        Y[indices] = row["correct"]
    return Y


def main():
    t0 = time.time()

    print("Loading 6 local models...", flush=True)
    df_local = load_local_hellaswag("results/exp002")
    df_local = df_local[df_local["benchmark"] == "hellaswag"].reset_index(drop=True)
    print(f"  {len(df_local)} records, models: {sorted(df_local['model'].unique())}", flush=True)

    item_ids = sorted(df_local["item_id"].unique().tolist())
    print(f"  {len(item_ids)} items", flush=True)

    print("Decoding OLMo/Yi...", flush=True)
    n_bits = len(TEMPERATURES) * len(PROMPT_TEMPLATES) * len(SEEDS) * len(ORDERINGS) * N_ITEMS
    olmo_bits = decode_binary(OLMO_B64, n_bits, OLMO_SUM, OLMO_MD5)
    yi_bits = decode_binary(YI_B64, n_bits, YI_SUM, YI_MD5)

    df_olmo = reconstruct_df(OLMO_MODEL, olmo_bits, item_ids)
    df_yi = reconstruct_df(YI_MODEL, yi_bits, item_ids)
    for d in [df_olmo, df_yi]:
        d["model"] = d["model"].map(normalize_model_name).fillna(d["model"])

    df = pd.concat([df_local, df_olmo, df_yi], ignore_index=True)
    df["temperature"] = df["temperature"].round(1)
    for f in FACETS:
        df[f] = df[f].astype(str)

    models = sorted(df["model"].unique().tolist())
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
    print(f"  Tensor shape={Y.shape}, mean={Y.mean():.6f}", flush=True)

    # Point estimate Henderson I
    print("Running Henderson I (point estimate)...", flush=True)
    vc, n_levels = henderson_i_from_tensor(Y, dim_sizes)
    total_var = sum(vc.values())
    g_item, sigma_tau, sigma_delta = compute_g_item(vc, n_levels)

    print(f"\n{'='*60}")
    print(f"HellaSwag 8-Model Henderson I")
    print(f"{'='*60}")
    print(f"N={Y.size}, Grand mean={Y.mean():.6f}, G_item={g_item:.6f}")
    print(f"\n{'Component':<30} {'Estimate':>12} {'%':>8}")
    print("-" * 52)
    for k, v in sorted(vc.items(), key=lambda x: -x[1]):
        print(f"{k:<30} {v:>12.8f} {v/total_var*100:>7.2f}%")

    # Bootstrap CI (item resampling on tensor)
    n_boot = 500
    print(f"\nBootstrap CI ({n_boot} iterations)...", flush=True)
    rng = np.random.default_rng(42)
    n_items = len(items)
    boot_vc_list = []
    boot_g_list = []

    for b in range(n_boot):
        if b % 50 == 0:
            print(f"  Bootstrap {b}/{n_boot} ({time.time()-t0:.1f}s)...", flush=True)
        idx = rng.choice(n_items, size=n_items, replace=True)
        Y_boot = Y[:, :, :, :, :, idx]
        vc_b, nl_b = henderson_i_from_tensor(Y_boot, dim_sizes)
        tot_b = sum(vc_b.values())
        pct_b = {k: v / tot_b * 100 if tot_b > 0 else 0 for k, v in vc_b.items()}
        g_b, _, _ = compute_g_item(vc_b, nl_b)
        boot_vc_list.append({"pct": pct_b, "raw": vc_b})
        boot_g_list.append(g_b)

    # Compute CIs
    ci = {}
    all_keys = set()
    for bv in boot_vc_list:
        all_keys.update(bv["pct"].keys())
    for key in all_keys:
        vals = [bv["pct"].get(key, 0) for bv in boot_vc_list]
        ci[key] = {"mean": round(float(np.mean(vals)), 4),
                    "ci_lo": round(float(np.percentile(vals, 2.5)), 4),
                    "ci_hi": round(float(np.percentile(vals, 97.5)), 4)}

    g_arr = np.array(boot_g_list)
    ci["G_item"] = {"mean": round(float(g_arr.mean()), 6),
                     "ci_lo": round(float(np.percentile(g_arr, 2.5)), 6),
                     "ci_hi": round(float(np.percentile(g_arr, 97.5)), 6)}

    oi_raw = [bv["raw"].get("ordering:item_id", 0) for bv in boot_vc_list]
    oi_pct = [bv["pct"].get("ordering:item_id", 0) for bv in boot_vc_list]
    oi_detail = {
        "raw_mean": round(float(np.mean(oi_raw)), 10),
        "raw_ci_lo": round(float(np.percentile(oi_raw, 2.5)), 10),
        "raw_ci_hi": round(float(np.percentile(oi_raw, 97.5)), 10),
        "pct_nonzero": round(sum(1 for v in oi_raw if v > 0) / len(oi_raw) * 100, 2),
    }

    print(f"\n{'Component':<30} {'%':>8} {'95% CI':>20}")
    print("-" * 60)
    for k in sorted(vc.keys(), key=lambda x: -vc[x]):
        if k in ci:
            print(f"{k:<30} {vc[k]/total_var*100:>7.2f}% [{ci[k]['ci_lo']:>6.2f}%, {ci[k]['ci_hi']:>6.2f}%]")

    print(f"\nG_item = {g_item:.6f} [{ci['G_item']['ci_lo']:.6f}, {ci['G_item']['ci_hi']:.6f}]")

    oi_pct_pt = vc.get("ordering:item_id", 0) / total_var * 100 if total_var > 0 else 0
    print(f"\n{'='*60}")
    print(f"ordering:item_id Analysis (R1-W4)")
    print(f"{'='*60}")
    print(f"  Point: {vc.get('ordering:item_id', 0):.10f} ({oi_pct_pt:.4f}%)")
    print(f"  Bootstrap: nonzero in {oi_detail['pct_nonzero']}% of samples")

    # Per-model analysis
    print(f"\nPer-model ordering:item_id:", flush=True)
    per_model = {}
    for mi, mname in enumerate(models):
        Ym = Y[mi:mi+1]
        ds = [1] + dim_sizes[1:]
        dn = ["model"] + list(dim_levels.keys())[1:]
        facets_nm = [f for f in FACETS if f != "model"]
        Ym_sq = Ym.squeeze(axis=0)
        ds_nm = dim_sizes[1:]
        vc_m, nl_m = henderson_i_from_tensor(Ym_sq, ds_nm, dim_names=DIM_ORDER[1:])
        tot_m = sum(vc_m.values())
        oi_m = vc_m.get("ordering:item_id", 0)
        per_model[mname] = {
            "ordering_item_pct": round(oi_m / tot_m * 100, 4) if tot_m > 0 else 0,
            "ordering_item_raw": round(oi_m, 10),
        }

    DIM_ORDER_NM = DIM_ORDER[1:]  # without model

    print(f"  {'Model':<20} {'o:i %':>10}")
    print("  " + "-" * 32)
    for m in sorted(per_model.keys()):
        print(f"  {m:<20} {per_model[m]['ordering_item_pct']:>9.4f}%")

    # D-study
    item_counts = [25, 50, 75, 100, 150, 200, 300, 500, 1000]
    d_curve = d_study_curve(vc, n_levels, item_counts)

    # Save
    output = {
        "experiment": "exp-004",
        "analysis": "per_benchmark_henderson_i_gstudy_8model",
        "benchmark": "hellaswag",
        "n_models": 8,
        "models": models,
        "facets": FACETS,
        "n_observations": int(Y.size),
        "n_levels": {k: int(v) for k, v in n_levels.items()},
        "grand_mean_accuracy": round(float(Y.mean()), 6),
        "variance_components": {
            k: {"estimate": round(v, 10), "pct": round(v / total_var * 100, 4) if total_var > 0 else 0.0}
            for k, v in sorted(vc.items(), key=lambda x: -x[1])
        },
        "total_variance": round(total_var, 10),
        "G_item": round(g_item, 6),
        "G_item_CI": ci.get("G_item", {}),
        "sigma_tau": round(sigma_tau, 10),
        "sigma_delta": round(sigma_delta, 10),
        "bootstrap_ci": {k: v for k, v in ci.items() if k != "G_item"},
        "ordering_item_id_analysis": {
            "point_estimate": round(vc.get("ordering:item_id", 0), 10),
            "point_pct": round(oi_pct_pt, 4),
            "bootstrap": oi_detail,
            "per_model": per_model,
            "conclusion": "nonzero" if vc.get("ordering:item_id", 0) > 0 else "zero (truncated to 0)",
        },
        "d_study_curve": d_curve,
        "runtime_seconds": round(time.time() - t0, 1),
    }

    out_path = Path("results/exp004_8model_analysis/per_benchmark_gstudy_hellaswag_2temp.json")
    out_path.parent.mkdir(parents=True, exist_ok=True)
    with open(out_path, "w") as f:
        json.dump(output, f, indent=2, default=str)

    print(f"\n=> {out_path}")
    print(f"Total runtime: {time.time()-t0:.1f}s")


# Patch DIM_ORDER for per-model analysis
DIM_ORDER_ORIG = list(DIM_ORDER)

if __name__ == "__main__":
    # For per-model Henderson I, temporarily adjust DIM_ORDER
    main()
