"""MATH 8-model Henderson I G-study + clean MC/FF permutation test.

Uses vectorized numpy for fast bootstrap on balanced design.
"""

import json
import sys
import time
from itertools import combinations
from math import comb
from pathlib import Path

import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from src.config.model_paths import normalize_model_name

FACET_NAMES = ["model", "temperature", "prompt_template", "seed", "ordering", "item_id"]
MATH_FILES = [
    "llama_math.jsonl", "mistral_math.jsonl", "qwen_math.jsonl",
    "gemma_math.jsonl", "internlm_math.jsonl", "deepseek_math.jsonl",
    "olmo_math.jsonl", "yi_math.jsonl",
]


def load_math_data(data_dir):
    frames = []
    for f in MATH_FILES:
        p = Path(data_dir) / f
        df = pd.read_json(p, lines=True)
        frames.append(df)
        print(f"  {f}: {len(df)} rows", flush=True)
    df = pd.concat(frames, ignore_index=True)
    if "top_logprobs" in df.columns:
        df.drop(columns=["top_logprobs"], inplace=True)
    df["model"] = df["model"].map(normalize_model_name).fillna(df["model"])
    return df


def build_tensor(df):
    """Convert balanced DataFrame to numpy array indexed by facet levels."""
    level_maps = {}
    for f in FACET_NAMES:
        levels = sorted(df[f].unique())
        level_maps[f] = {v: i for i, v in enumerate(levels)}

    shape = tuple(len(level_maps[f]) for f in FACET_NAMES)
    print(f"  Tensor shape: {dict(zip(FACET_NAMES, shape))}", flush=True)
    tensor = np.full(shape, np.nan)

    for _, row in df.iterrows():
        idx = tuple(level_maps[f][row[f]] for f in FACET_NAMES)
        tensor[idx] = row["correct"]

    n_nan = np.isnan(tensor).sum()
    if n_nan > 0:
        print(f"  WARNING: {n_nan} missing cells in tensor")
    return tensor, level_maps, shape


def henderson_i_from_tensor(data):
    """Henderson I on a balanced fully-crossed tensor. Fast vectorized version."""
    shape = data.shape
    n_facets = len(shape)
    N = data.size
    grand_mean = np.nanmean(data)

    effects = {}

    # Main effects
    for i in range(n_facets):
        axes = tuple(j for j in range(n_facets) if j != i)
        facet_means = np.nanmean(data, axis=axes)
        n_per = N // shape[i]
        ss = float(n_per * np.nansum((facet_means - grand_mean) ** 2))
        df_eff = shape[i] - 1
        effects[i] = {"ss": ss, "df": df_eff, "ms": ss / df_eff if df_eff > 0 else 0.0}

    # 2-way interactions
    for i, j in combinations(range(n_facets), 2):
        axes = tuple(k for k in range(n_facets) if k not in (i, j))
        cell_means = np.nanmean(data, axis=axes)  # shape (shape[i], shape[j])
        main_i = np.nanmean(data, axis=tuple(k for k in range(n_facets) if k != i))
        main_j = np.nanmean(data, axis=tuple(k for k in range(n_facets) if k != j))
        interaction = cell_means - main_i[:, None] - main_j[None, :] + grand_mean
        n_per = N // (shape[i] * shape[j])
        ss = float(n_per * np.nansum(interaction ** 2))
        df_eff = (shape[i] - 1) * (shape[j] - 1)
        effects[(i, j)] = {"ss": ss, "df": df_eff, "ms": ss / df_eff if df_eff > 0 else 0.0}

    ss_total = float(np.nansum((data - grand_mean) ** 2))
    ss_model = sum(e["ss"] for e in effects.values())
    ss_res = max(0.0, ss_total - ss_model)
    df_res = N - 1 - sum(e["df"] for e in effects.values())
    effects["residual"] = {"ss": ss_res, "df": df_res, "ms": ss_res / df_res if df_res > 0 else 0.0}

    ms_res = effects["residual"]["ms"]

    # Variance components for interactions
    vc = {}
    for i, j in combinations(range(n_facets), 2):
        coeff = 1
        for k in range(n_facets):
            if k not in (i, j):
                coeff *= shape[k]
        raw = (effects[(i, j)]["ms"] - ms_res) / coeff if coeff > 0 else 0.0
        vc[(i, j)] = max(0.0, raw)

    # Variance components for main effects
    for i in range(n_facets):
        coeff_main = 1
        for k in range(n_facets):
            if k != i:
                coeff_main *= shape[k]
        interaction_contrib = 0.0
        for j in range(n_facets):
            if j == i:
                continue
            int_key = (min(i, j), max(i, j))
            coeff_ij = 1
            for k in range(n_facets):
                if k not in (i, j):
                    coeff_ij *= shape[k]
            interaction_contrib += coeff_ij * vc[int_key]
        raw = (effects[i]["ms"] - interaction_contrib - ms_res) / coeff_main if coeff_main > 0 else 0.0
        vc[i] = max(0.0, raw)

    vc["residual"] = ms_res
    return vc, effects


def vc_to_named(vc, facet_names):
    """Convert integer-keyed vc dict to named dict."""
    named = {}
    for k, v in vc.items():
        if k == "residual":
            named["residual"] = v
        elif isinstance(k, int):
            named[facet_names[k]] = v
        elif isinstance(k, tuple):
            named[f"{facet_names[k[0]]}:{facet_names[k[1]]}"] = v
    return named


def compute_g_item_from_vc(vc_named, n_levels):
    """G_item from named vc dict."""
    sigma_item = vc_named.get("item_id", 0.0)
    non_item_facets = [f for f in FACET_NAMES if f != "item_id"]
    sigma_delta = 0.0
    for comp, est in vc_named.items():
        if est == 0.0 or comp == "item_id":
            continue
        if comp == "residual":
            divisor = 1
            for f in non_item_facets:
                divisor *= n_levels[f]
            sigma_delta += est / divisor
            continue
        facets_in = set(comp.split(":"))
        if "item_id" not in facets_in:
            continue
        other = [f for f in facets_in if f != "item_id"]
        divisor = 1
        for f in other:
            divisor *= n_levels[f]
        sigma_delta += est / divisor
    g = sigma_item / (sigma_item + sigma_delta) if (sigma_item + sigma_delta) > 0 else 0.0
    return g, sigma_item, sigma_delta


def get_item_pct(data):
    """Compute item_id% from tensor. item_id is the last axis (index 5)."""
    vc, _ = henderson_i_from_tensor(data)
    total = sum(vc.values())
    item_idx = 5  # item_id
    return vc[item_idx] / total * 100 if total > 0 else 0.0


def bootstrap_item_pct(data, n_boot=2000, seed=42):
    """Bootstrap item_id% by resampling items (last axis)."""
    rng = np.random.RandomState(seed)
    n_items = data.shape[5]
    pcts = np.zeros(n_boot)
    for b in range(n_boot):
        idx = rng.randint(0, n_items, size=n_items)
        boot_data = data[:, :, :, :, :, idx]
        pcts[b] = get_item_pct(boot_data)
        if (b + 1) % 200 == 0:
            print(f"    bootstrap {b+1}/{n_boot}", flush=True)
    return pcts


def part_a(data_dir):
    print("=" * 60)
    print("Part A: MATH 8-model Henderson I G-study")
    print("=" * 60)
    t0 = time.time()

    df = load_math_data(data_dir)
    print(f"\nTotal: {len(df)} records, {df['model'].nunique()} models", flush=True)
    print(f"Models: {sorted(df['model'].unique())}", flush=True)

    # Convert to string for consistency
    for f in FACET_NAMES:
        df[f] = df[f].astype(str)

    tensor, level_maps, shape = build_tensor(df)
    n_levels = {f: len(level_maps[f]) for f in FACET_NAMES}

    print(f"\n  Computing Henderson I...", flush=True)
    vc, effects = henderson_i_from_tensor(tensor)
    vc_named = vc_to_named(vc, FACET_NAMES)
    total_var = sum(vc_named.values())

    g_item, sigma_tau, sigma_delta = compute_g_item_from_vc(vc_named, n_levels)
    item_pct = vc_named.get("item_id", 0.0) / total_var * 100

    print(f"\n  item_id% = {item_pct:.2f}%")
    print(f"  G_item = {g_item:.6f}")
    print(f"  grand_mean = {np.nanmean(tensor):.6f}")
    print(f"\n  Variance components:")
    for k, v in sorted(vc_named.items(), key=lambda x: -x[1]):
        print(f"    {k:30s}: {v:.10f} ({v/total_var*100:.2f}%)")

    print(f"\n  Bootstrapping item_id% CI (2000 iterations)...", flush=True)
    boot_pcts = bootstrap_item_pct(tensor, n_boot=2000)
    ci_lo, ci_hi = np.percentile(boot_pcts, [2.5, 97.5])
    print(f"  item_id% 95% CI: [{ci_lo:.2f}%, {ci_hi:.2f}%]")

    prev_7model = 26.48
    print(f"\n  7-model item_id%: {prev_7model}%")
    print(f"  8-model item_id%: {item_pct:.2f}%")
    print(f"  Change: {item_pct - prev_7model:+.2f}pp")

    elapsed = time.time() - t0
    print(f"\n  Part A done in {elapsed:.1f}s")

    result = {
        "analysis": "math_8model_henderson_i",
        "n_models": 8,
        "n_observations": int(tensor.size),
        "models": sorted(level_maps["model"].keys()),
        "n_levels": {k: int(v) for k, v in n_levels.items()},
        "grand_mean_accuracy": round(float(np.nanmean(tensor)), 6),
        "variance_components": {
            k: {"estimate": round(v, 10), "pct": round(v / total_var * 100, 4)}
            for k, v in sorted(vc_named.items(), key=lambda x: -x[1])
        },
        "total_variance": round(total_var, 10),
        "item_id_pct": round(item_pct, 4),
        "item_id_pct_bootstrap_ci_95": [round(ci_lo, 4), round(ci_hi, 4)],
        "G_item": round(g_item, 6),
        "sigma_tau": round(sigma_tau, 10),
        "sigma_delta": round(sigma_delta, 10),
        "comparison_7model": {
            "prev_item_id_pct": prev_7model,
            "curr_item_id_pct": round(item_pct, 4),
            "change_pp": round(item_pct - prev_7model, 4),
        },
    }
    return result, item_pct


def part_b(math_item_pct):
    print("\n" + "=" * 60)
    print("Part B: Clean MC/FF Permutation Test")
    print("=" * 60)

    mc = {"MMLU": 37.88, "ARC": 37.88, "HellaSwag": 34.27}
    ff = {"GSM8K": 16.86, "MATH": round(math_item_pct, 2)}

    mc_vals = list(mc.values())
    ff_vals = list(ff.values())
    all_names = list(mc.keys()) + list(ff.keys())
    all_vals = np.array(mc_vals + ff_vals)
    n = len(all_vals)
    n_mc = len(mc_vals)

    mc_mean = np.mean(mc_vals)
    ff_mean = np.mean(ff_vals)
    obs_diff = mc_mean - ff_mean

    print(f"\n  MC: {mc} -> mean={mc_mean:.2f}%")
    print(f"  FF: {ff} -> mean={ff_mean:.2f}%")
    print(f"  Observed diff (MC-FF): {obs_diff:.2f}pp")

    perms = list(combinations(range(n), n_mc))
    n_perms = len(perms)
    print(f"\n  Exhaustive: C({n},{n_mc}) = {n_perms} permutations")

    count_ge = 0
    perm_diffs = []
    for perm in perms:
        ff_idx = [i for i in range(n) if i not in perm]
        d = np.mean(all_vals[list(perm)]) - np.mean(all_vals[ff_idx])
        perm_diffs.append(d)
        if d >= obs_diff:
            count_ge += 1

    p_val = count_ge / n_perms
    print(f"  Count >= observed: {count_ge}/{n_perms}")
    print(f"  p-value (one-sided): {p_val:.4f}")

    pooled_std = np.std(all_vals, ddof=1)
    cohens_d = obs_diff / pooled_std if pooled_std > 0 else 0.0
    print(f"\n  Cohen's d: {cohens_d:.4f}")

    rng = np.random.RandomState(42)
    n_boot = 10000
    mc_arr, ff_arr = np.array(mc_vals), np.array(ff_vals)
    boot_ds, boot_diffs = [], []
    for _ in range(n_boot):
        mc_b = rng.choice(mc_arr, size=len(mc_arr), replace=True)
        ff_b = rng.choice(ff_arr, size=len(ff_arr), replace=True)
        diff_b = np.mean(mc_b) - np.mean(ff_b)
        boot_diffs.append(diff_b)
        all_b = np.concatenate([mc_b, ff_b])
        std_b = np.std(all_b, ddof=1)
        boot_ds.append(diff_b / std_b if std_b > 0 else 0.0)

    d_ci = np.percentile(boot_ds, [2.5, 97.5])
    diff_ci = np.percentile(boot_diffs, [2.5, 97.5])
    print(f"  Cohen's d 95% CI: [{d_ci[0]:.4f}, {d_ci[1]:.4f}]")
    print(f"  Diff 95% CI: [{diff_ci[0]:.2f}, {diff_ci[1]:.2f}]pp")

    print(f"\n  All permutations:")
    for i, perm in enumerate(perms):
        ff_idx = [j for j in range(n) if j not in perm]
        mc_n = [all_names[j] for j in perm]
        ff_n = [all_names[j] for j in ff_idx]
        marker = " <-- observed" if sorted(perm) == [0, 1, 2] else ""
        print(f"    {mc_n} vs {ff_n}: diff={perm_diffs[i]:+.2f}pp{marker}")

    result = {
        "analysis": "clean_permutation_test_mc_vs_ff",
        "mc_benchmarks": mc,
        "ff_benchmarks": ff,
        "mc_mean_item_id_pct": round(float(mc_mean), 4),
        "ff_mean_item_id_pct": round(float(ff_mean), 4),
        "observed_difference_pp": round(float(obs_diff), 4),
        "permutation_test": {
            "type": "exhaustive",
            "n_permutations": n_perms,
            "count_ge_observed": count_ge,
            "p_value_one_sided": round(p_val, 4),
            "note": f"n=5, minimum possible p = 1/C(5,3) = {1/comb(5,3):.2f}; describes format-conditional variance structure, not statistical significance",
        },
        "effect_size": {
            "cohens_d": round(float(cohens_d), 4),
            "cohens_d_95_ci": [round(float(d_ci[0]), 4), round(float(d_ci[1]), 4)],
            "difference_95_ci_pp": [round(float(diff_ci[0]), 4), round(float(diff_ci[1]), 4)],
        },
        "all_permutation_diffs_sorted": sorted([round(float(d), 4) for d in perm_diffs], reverse=True),
    }
    return result


def main():
    data_dir = "./results/exp002"
    out_dir = Path("./results/exp004_8model_analysis")
    out_dir.mkdir(parents=True, exist_ok=True)

    result_a, math_pct = part_a(data_dir)
    with open(out_dir / "math_8model_verified.json", "w") as f:
        json.dump(result_a, f, indent=2, default=str)
    print(f"\n  -> {out_dir / 'math_8model_verified.json'}")

    result_b = part_b(math_pct)
    with open(out_dir / "clean_permutation_test.json", "w") as f:
        json.dump(result_b, f, indent=2, default=str)
    print(f"  -> {out_dir / 'clean_permutation_test.json'}")


if __name__ == "__main__":
    main()
