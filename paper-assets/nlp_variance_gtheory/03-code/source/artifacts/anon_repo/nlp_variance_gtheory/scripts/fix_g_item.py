"""Fix G_item in 3 JSON files using correct Henderson I + G-theory formula."""

import json
import sys
import numpy as np
import pandas as pd
from math import prod
from pathlib import Path

sys.path.insert(0, ".")
from src.analysis.variance_decomposition import (
    compute_ss, estimate_variance_components, compute_text_exact_match
)

FACETS_6 = ["precision", "temperature", "prompt_template", "seed", "ordering", "item_id"]
FACETS_5 = ["temperature", "prompt_template", "seed", "ordering", "item_id"]


def compute_g_item(vc, n_levels, facets, item_facet="item_id"):
    tau = vc.get(item_facet, 0)
    non_item = [f for f in facets if f != item_facet]
    n_non_item_product = prod(n_levels[f] for f in non_item)
    delta = 0.0
    for key, est in vc.items():
        if key == item_facet or est <= 0:
            continue
        parts = key.split(":")
        if item_facet in parts:
            other = [p for p in parts if p != item_facet]
            divisor = prod(n_levels[f] for f in other) if other else 1
            delta += est / divisor
        elif key == "residual":
            delta += est / n_non_item_product
    g = tau / (tau + delta) if (tau + delta) > 0 else 0
    return g, tau, delta


def dstudy_g(tau, delta, n_actual, n_target):
    return tau / (tau + delta * n_actual / n_target) if (tau + delta) > 0 else 0


def find_min_items_g80(tau, delta, n_actual, max_items=5000):
    for n in range(1, max_items + 1):
        if dstudy_g(tau, delta, n_actual, n) >= 0.80:
            return n
    return None


def vc_to_pct(vc):
    total = sum(v for v in vc.values() if v > 0)
    return {k: round(v / total * 100, 4) for k, v in sorted(vc.items(), key=lambda x: -x[1]) if v > 0}


# ====================================================================
# Load exp-001 data
# ====================================================================
print("Loading exp-001 data...", flush=True)
dfs = []
for i in range(4):
    dfs.append(pd.read_json(f"./results/exp001_llama/llama_shard_{i}.jsonl", lines=True))
df_001 = pd.concat(dfs, ignore_index=True)
for f in FACETS_6:
    df_001[f] = df_001[f].astype(str)
print(f"  {len(df_001)} records", flush=True)


# ====================================================================
# FILE 1: llama_single_model_gstudy.json
# ====================================================================
print("\n=== FILE 1: llama_single_model_gstudy.json ===", flush=True)
path1 = "./results/analysis/llama_single_model_gstudy.json"
with open(path1) as f:
    file1 = json.load(f)

# --- correct ---
eff_c, nl_c = compute_ss(df_001, "correct", FACETS_6)
vc_c = estimate_variance_components(eff_c, FACETS_6, nl_c)
g_c, tau_c, delta_c = compute_g_item(vc_c, nl_c, FACETS_6)
total_c = sum(v for v in vc_c.values() if v > 0)

old_g_c = file1["correct"]["G_coefficient"]
file1["correct"]["components_pct"] = vc_to_pct(vc_c)
file1["correct"]["G_coefficient"] = round(g_c, 4)
file1["correct"]["total_variance"] = round(total_c, 8)

n_items_c = nl_c["item_id"]
ds_c = {}
for ni in [25, 50, 75, 100, 150, 200, 300, 500]:
    ds_c[str(ni)] = round(dstudy_g(tau_c, delta_c, n_items_c, ni), 4)
file1["d_study_correct"] = ds_c

print(f"  correct: {old_g_c} -> {round(g_c, 4)}", flush=True)

# --- text_exact_match ---
df_tem = compute_text_exact_match(df_001)
eff_t, nl_t = compute_ss(df_tem, "text_exact_match", FACETS_6)
vc_t = estimate_variance_components(eff_t, FACETS_6, nl_t)
g_t, tau_t, delta_t = compute_g_item(vc_t, nl_t, FACETS_6)
total_t = sum(v for v in vc_t.values() if v > 0)

old_g_t = file1["text_exact_match"]["G_coefficient"]
file1["text_exact_match"]["components_pct"] = vc_to_pct(vc_t)
file1["text_exact_match"]["G_coefficient"] = round(g_t, 4)
file1["text_exact_match"]["total_variance"] = round(total_t, 8)

print(f"  text_exact_match: {old_g_t} -> {round(g_t, 4)}", flush=True)

with open(path1, "w") as f:
    json.dump(file1, f, indent=2)
print("  SAVED", flush=True)


# ====================================================================
# FILE 2: exp001b_resampling_gstudy.json
# ====================================================================
print("\n=== FILE 2: exp001b_resampling_gstudy.json ===", flush=True)
path2 = "./results/analysis/exp001b_resampling_gstudy.json"
with open(path2) as f:
    file2 = json.load(f)

# baseline = same as exp-001 correct
file2["baseline"]["components_pct"] = file1["correct"]["components_pct"]
file2["baseline"]["G_coefficient"] = file1["correct"]["G_coefficient"]
file2["baseline"]["total_variance"] = file1["correct"]["total_variance"]
print(f"  baseline: -> {file1['correct']['G_coefficient']}", flush=True)

# 3 samples
sample_gs = []
sample_item_pcts = []
for sname in ["sample1", "sample2", "sample3"]:
    spath = f"./results/exp001b/{sname}/all_results.jsonl"
    df_s = pd.read_json(spath, lines=True)
    for f in FACETS_5:
        df_s[f] = df_s[f].astype(str)

    eff_s, nl_s = compute_ss(df_s, "correct", FACETS_5)
    vc_s = estimate_variance_components(eff_s, FACETS_5, nl_s)
    g_s, tau_s, delta_s = compute_g_item(vc_s, nl_s, FACETS_5)
    total_s = sum(v for v in vc_s.values() if v > 0)
    pct_s = vc_to_pct(vc_s)

    old_g_s = file2[sname]["G_item"]
    file2[sname]["components_pct"] = pct_s
    file2[sname]["G_item"] = round(g_s, 4)
    file2[sname]["total_variance"] = round(total_s, 8)
    file2[sname]["item_id_pct"] = pct_s.get("item_id", 0)

    n_items_s = nl_s["item_id"]
    ds_s = {}
    for ni in [25, 50, 75, 100, 150, 200, 300, 500]:
        ds_s[str(ni)] = round(dstudy_g(tau_s, delta_s, n_items_s, ni), 4)
    file2[sname]["d_study"] = ds_s
    file2[sname]["min_items_g80"] = find_min_items_g80(tau_s, delta_s, n_items_s)

    sample_gs.append(round(g_s, 4))
    sample_item_pcts.append(pct_s.get("item_id", 0))
    print(f"  {sname}: {old_g_s} -> {round(g_s, 4)}, min_g80={file2[sname]['min_items_g80']}", flush=True)

# stability
stability = {}
for stat_key, comp_key in [
    ("item_id_pct", "item_id"),
    ("prompt_template_item_id_pct", "prompt_template:item_id"),
    ("seed_item_id_pct", "seed:item_id"),
    ("temperature_item_id_pct", "temperature:item_id"),
    ("ordering_item_id_pct", "ordering:item_id"),
]:
    vals = [file2[s]["components_pct"].get(comp_key, 0) for s in ["sample1", "sample2", "sample3"]]
    mn = float(np.mean(vals))
    sd = float(np.std(vals))
    stability[stat_key] = {
        "values": [round(v, 4) for v in vals],
        "mean": round(mn, 4),
        "std": round(sd, 4),
        "cv": round(sd / mn * 100, 2) if mn > 0 else 0,
    }

mn_g = float(np.mean(sample_gs))
sd_g = float(np.std(sample_gs))
stability["G_item"] = {
    "values": sample_gs,
    "mean": round(mn_g, 4),
    "std": round(sd_g, 4),
    "cv": round(sd_g / mn_g * 100, 2),
}
file2["stability"] = stability

# comparison
pct_c_item = vc_to_pct(vc_c).get("item_id", 0)
file2["comparison_with_exp001"]["exp001_item_id_pct"] = pct_c_item
file2["comparison_with_exp001"]["resampling_mean_item_id_pct"] = stability["item_id_pct"]["mean"]
file2["comparison_with_exp001"]["delta"] = round(stability["item_id_pct"]["mean"] - pct_c_item, 4)

with open(path2, "w") as f:
    json.dump(file2, f, indent=2)
print("  SAVED", flush=True)


# ====================================================================
# FILE 3: dstudy_progressive_validation.json
# ====================================================================
print("\n=== FILE 3: dstudy_progressive_validation.json ===", flush=True)
path3 = "./results/analysis/dstudy_progressive_validation.json"
with open(path3) as f:
    file3 = json.load(f)

all_items = sorted(df_001["item_id"].unique())

for size_str, entries in file3["subsets"].items():
    size = int(size_str)
    for entry in entries:
        seed_val = entry["seed"]
        if seed_val == 0 and size == 200:
            sub_df = df_001
        else:
            rng = np.random.RandomState(seed_val)
            sampled = sorted(rng.choice(all_items, size=size, replace=False))
            sub_df = df_001[df_001["item_id"].isin(sampled)].copy()

        eff_sub, nl_sub = compute_ss(sub_df, "correct", FACETS_6)
        vc_sub = estimate_variance_components(eff_sub, FACETS_6, nl_sub)
        g_sub, tau_sub, delta_sub = compute_g_item(vc_sub, nl_sub, FACETS_6)
        pct_sub = vc_to_pct(vc_sub)

        old_g = entry["G_item"]
        entry["item_id_pct"] = round(pct_sub.get("item_id", 0), 4)
        entry["components_pct"] = pct_sub
        entry["G_item"] = round(g_sub, 4)

        n_actual = nl_sub["item_id"]
        min_g80 = find_min_items_g80(tau_sub, delta_sub, n_actual)
        entry["min_items_G80"] = min_g80

        print(f"  size={size}, seed={seed_val}: {old_g} -> {round(g_sub, 4)}, min_G80={min_g80}", flush=True)

# convergence
metrics_to_track = ["item_id_pct", "G_item", "min_items_G80"]
convergence = {}
for metric_name in metrics_to_track:
    conv = {}
    for size in [50, 100, 150]:
        vals = [e[metric_name] for e in file3["subsets"][str(size)] if e[metric_name] is not None]
        if vals:
            conv[f"{size}_mean"] = round(float(np.mean(vals)), 4)
            conv[f"{size}_std"] = round(float(np.std(vals)), 4)
            conv[f"{size}_cv"] = round(float(np.std(vals) / np.mean(vals) * 100), 2) if np.mean(vals) != 0 else None

    val_200 = file3["subsets"]["200"][0][metric_name]
    conv["200"] = round(float(val_200), 4) if isinstance(val_200, float) else val_200

    if "150_mean" in conv and val_200 is not None and conv["150_mean"] is not None:
        if conv["150_mean"] != 0:
            change = abs(float(val_200) - conv["150_mean"]) / conv["150_mean"] * 100
            conv["150_to_200_change_pct"] = round(change, 2)

    convergence[metric_name] = conv

file3["convergence"] = convergence
changes = [convergence[m].get("150_to_200_change_pct", 999) for m in metrics_to_track]
file3["conclusion"] = "converged" if all(c < 10 for c in changes) else "not converged"

with open(path3, "w") as f:
    json.dump(file3, f, indent=2)
print("  SAVED", flush=True)

print("\n=== ALL DONE ===", flush=True)
