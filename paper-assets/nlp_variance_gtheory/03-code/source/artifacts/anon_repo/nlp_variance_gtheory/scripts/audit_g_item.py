"""Audit G_item calculations across exp-001, exp-001b, and within-MMLU scripts.

Recomputes correct G_item using Henderson I variance components and
proper G-theory formula, then compares with stored values.
"""

import json
import sys
from itertools import combinations
from math import prod
from pathlib import Path

import numpy as np
import pandas as pd

sys.path.insert(0, ".")
from src.analysis.variance_decomposition import compute_ss, estimate_variance_components


def compute_g_item_correct(vc, n_levels, facets, item_facet="item_id"):
    """Correct G_item: tau = sigma2(item), delta = item-interacting errors / n_levels."""
    tau = vc.get(item_facet, 0)
    
    non_item = [f for f in facets if f != item_facet]
    n_non_item_product = prod(n_levels[f] for f in non_item)
    
    delta = 0.0
    delta_detail = {}
    
    for key, est in vc.items():
        if key == item_facet or est <= 0:
            continue
        parts = key.split(":")
        if item_facet in parts:
            other = [p for p in parts if p != item_facet]
            divisor = prod(n_levels[f] for f in other) if other else 1
            contrib = est / divisor
            delta_detail[key] = {"est": est, "divisor": divisor, "contrib": contrib}
            delta += contrib
        elif key == "residual":
            contrib = est / n_non_item_product
            delta_detail["residual"] = {"est": est, "divisor": n_non_item_product, "contrib": contrib}
            delta += contrib
    
    g = tau / (tau + delta) if (tau + delta) > 0 else 0
    return g, tau, delta, delta_detail


def compute_icc(vc, item_facet="item_id"):
    """ICC = sigma2(item) / sigma2(total) — what gstudy_full.py computes."""
    total = sum(v for v in vc.values() if v > 0)
    return vc.get(item_facet, 0) / total if total > 0 else 0


# ====================================================================
# Part 1: exp-001 single-model (llama)
# ====================================================================
print("=" * 70)
print("PART 1: exp-001 Single-Model (Llama) — gstudy_full.py")
print("=" * 70)

csv_path = "./results/analysis/llama_full.csv"
if Path(csv_path).exists():
    df = pd.read_csv(csv_path, low_memory=False)
    facets_1 = ["precision", "temperature", "prompt_template", "seed", "ordering", "item_id"]
    for f in facets_1:
        df[f] = df[f].astype(str)
    
    effects_1, n_levels_1 = compute_ss(df, "correct", facets_1)
    vc_1 = estimate_variance_components(effects_1, facets_1, n_levels_1)
    
    print(f"n_levels: {n_levels_1}")
    print(f"N = {len(df)}")
    
    # Correct G_item
    g_correct, tau, delta, detail = compute_g_item_correct(vc_1, n_levels_1, facets_1)
    icc = compute_icc(vc_1)
    
    print(f"\nHenderson I variance components:")
    total_vc = sum(v for v in vc_1.values() if v > 0)
    for k, v in sorted(vc_1.items(), key=lambda x: -x[1]):
        if v > 0.0001:
            print(f"  {k:30s}: {v:.8f} ({v/total_vc*100:.2f}%)")
    
    print(f"\nStored G_coefficient (ICC from SS):  0.6108")
    print(f"Recomputed ICC (from Henderson VC): {icc:.4f}")
    print(f"Correct G_item (G-theory):          {g_correct:.4f}")
    print(f"  tau = sigma2(item_id) = {tau:.8f}")
    print(f"  delta = {delta:.8f}")
    print(f"\nDelta breakdown:")
    for k, v in sorted(detail.items(), key=lambda x: -x[1]["contrib"]):
        print(f"  {k:30s}: {v['est']:.8f} / {v['divisor']:>5d} = {v['contrib']:.8f}")
else:
    print(f"  [SKIP] {csv_path} not found")

# ====================================================================
# Part 2: exp-001b resampling
# ====================================================================
print("\n" + "=" * 70)
print("PART 2: exp-001b Resampling — exp001b_gstudy.py")
print("=" * 70)

facets_b = ["temperature", "prompt_template", "seed", "ordering", "item_id"]
sample_paths = {
    "sample1": "./results/exp001b/sample1/all_results.jsonl",
    "sample2": "./results/exp001b/sample2/all_results.jsonl",
    "sample3": "./results/exp001b/sample3/all_results.jsonl",
}

stored_g = {"sample1": 0.7588, "sample2": 0.7538, "sample3": 0.7218}

for name, path in sample_paths.items():
    if not Path(path).exists():
        print(f"  [{name}] SKIP — {path} not found")
        continue
    
    df_b = pd.read_json(path, lines=True)
    for f in facets_b:
        df_b[f] = df_b[f].astype(str)
    
    effects_b, n_levels_b = compute_ss(df_b, "correct", facets_b)
    vc_b = estimate_variance_components(effects_b, facets_b, n_levels_b)
    
    g_correct_b, tau_b, delta_b, detail_b = compute_g_item_correct(vc_b, n_levels_b, facets_b)
    icc_b = compute_icc(vc_b)
    
    print(f"\n--- {name} ({len(df_b)} obs, n_levels={n_levels_b}) ---")
    print(f"  Stored G_item (ICC from SS):  {stored_g[name]:.4f}")
    print(f"  Recomputed ICC (Henderson VC): {icc_b:.4f}")
    print(f"  Correct G_item (G-theory):     {g_correct_b:.4f}")
    print(f"  tau={tau_b:.8f}, delta={delta_b:.8f}")

# ====================================================================
# Part 3: within-MMLU old (task8) vs new (4model)
# ====================================================================
print("\n" + "=" * 70)
print("PART 3: Within-MMLU — task8 (old) vs 4model (new)")
print("=" * 70)

# Read stored results
old_path = "./results/analysis/within_mmlu_subject_gradient.json"
new_path = "./results/exp001_analysis/within_mmlu_subject_gradient_4model.json"

with open(old_path) as f:
    old = json.load(f)
with open(new_path) as f:
    new = json.load(f)

print(f"\n{'Subject':<25} {'Old G_item':>10} {'New G_item':>10} {'Delta':>8}")
print("-" * 60)

old_subjects = old["subjects"]
new_subjects = new["subjects"]
for subj in sorted(old_subjects.keys()):
    old_g = old_subjects[subj]["G_item"]
    new_g = new_subjects.get(subj, {}).get("g_item", "N/A")
    if isinstance(new_g, (int, float)):
        delta_str = f"{new_g - old_g:+.4f}"
    else:
        delta_str = "N/A"
    print(f"{subj:<25} {old_g:>10.4f} {new_g:>10.4f} {delta_str:>8}")

# ====================================================================
# Part 4: Summary
# ====================================================================
print("\n" + "=" * 70)
print("SUMMARY: Bug Audit Results")
print("=" * 70)

print("""
FILE                              | BUG? | TYPE                           | IMPACT
----------------------------------+------+--------------------------------+------------------
gstudy_full.py (exp-001)          | YES  | ICC from SS, not G coefficient | G underestimated
exp001b_gstudy.py (exp-001b)      | YES  | ICC from SS, not G coefficient | G underestimated
task8_subject_gradient.py         | YES  | tau=fixed facets, not item     | G ≈ 0 (wrong tau)
compute_g_coefficients.py         | NO   | Correct G_item formula         | —
within_mmlu_gradient_4model.py    | NO   | Correct G_item formula         | —
src/analysis/variance_decomp.py   | N/A  | Correct VC estimation          | —
""")

print("DONE")
