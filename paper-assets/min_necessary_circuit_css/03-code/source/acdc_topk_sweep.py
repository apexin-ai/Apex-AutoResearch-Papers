import os
os.environ["CUDA_VISIBLE_DEVICES"] = "5"

import json
import math
from collections import Counter

PYTHON = "/root/miniconda3/bin/python3.12"

def load_scores(path):
    with open(path) as f:
        return json.load(f)

def get_topk_edges(scores, k, use_abs=True):
    if use_abs:
        sorted_edges = sorted(
            scores.items(),
            key=lambda x: abs(x[1]) if not math.isinf(x[1]) else float('inf'),
            reverse=True
        )
    else:
        sorted_edges = sorted(
            scores.items(),
            key=lambda x: x[1] if not math.isinf(x[1]) else float('inf'),
            reverse=True
        )
    return set(e[0] for e in sorted_edges[:k])

def get_inf_edges(scores):
    return set(k for k, v in scores.items() if math.isinf(v))

def jaccard(a, b):
    if len(a | b) == 0:
        return 0.0
    return len(a & b) / len(a | b)

def analyze_score_distribution(scores, name):
    vals = list(scores.values())
    inf_count = sum(1 for v in vals if math.isinf(v))
    unique_vals = set(v for v in vals if not math.isinf(v))
    print(f"\n--- {name} ---")
    print(f"  Total edges: {len(vals)}")
    print(f"  Infinity edges: {inf_count}")
    print(f"  Unique non-inf values: {len(unique_vals)}")
    if len(unique_vals) <= 10:
        val_counts = Counter(v for v in vals if not math.isinf(v))
        for v, c in sorted(val_counts.items(), key=lambda x: x[0], reverse=True)[:10]:
            print(f"    {v:.6f}: {c} edges")
    else:
        non_inf = sorted([abs(v) for v in vals if not math.isinf(v)], reverse=True)
        print(f"  Top-5 abs values: {[f'{x:.4f}' for x in non_inf[:5]]}")
        print(f"  Median abs value: {non_inf[len(non_inf)//2]:.6f}")

def run_sweep(dataset_name, acdc_scores, eapig_scores, ep_scores):
    print(f"\n{'='*70}")
    print(f"  {dataset_name}")
    print(f"{'='*70}")

    analyze_score_distribution(acdc_scores, f"ACDC ({dataset_name})")
    analyze_score_distribution(eapig_scores, f"EAP-IG ({dataset_name})")
    analyze_score_distribution(ep_scores, f"EP ({dataset_name})")

    eapig_top100 = get_topk_edges(eapig_scores, 100, use_abs=True)
    ep_top100 = get_topk_edges(ep_scores, 100, use_abs=True)

    print(f"\n  EAP-IG top-100 edges (fixed)")
    print(f"  EP top-100 edges (fixed)")
    print(f"  J(eapig, ep) = {jaccard(eapig_top100, ep_top100):.4f}")

    acdc_inf = get_inf_edges(acdc_scores)
    print(f"  ACDC isinf edges: {len(acdc_inf)}")
    if len(acdc_inf) <= 20:
        print(f"  ACDC isinf edge list: {sorted(acdc_inf)}")

    ks = ["isinf", 20, 50, 75, 100, 150, 200]

    header = f"  {'k':>6} | {'ACDC':>5} | {'1/3':>5} | {'2/3':>5} | {'3/3':>5} | {'J(ei,ep)':>8} | {'J(ei,ac)':>8} | {'J(ep,ac)':>8}"
    sep = f"  {'-'*6}-+-{'-'*5}-+-{'-'*5}-+-{'-'*5}-+-{'-'*5}-+-{'-'*8}-+-{'-'*8}-+-{'-'*8}"
    print(f"\n{header}")
    print(sep)

    for k in ks:
        if k == "isinf":
            acdc_selected = acdc_inf
            k_label = "isinf"
        else:
            acdc_selected = get_topk_edges(acdc_scores, k, use_abs=True)
            k_label = str(k)

        all_edges = eapig_top100 | ep_top100 | acdc_selected

        css_1of3 = 0
        css_2of3 = 0
        css_3of3 = 0

        for edge in all_edges:
            count = (edge in eapig_top100) + (edge in ep_top100) + (edge in acdc_selected)
            if count == 1:
                css_1of3 += 1
            elif count == 2:
                css_2of3 += 1
            elif count == 3:
                css_3of3 += 1

        j_ei_ep = jaccard(eapig_top100, ep_top100)
        j_ei_ac = jaccard(eapig_top100, acdc_selected)
        j_ep_ac = jaccard(ep_top100, acdc_selected)

        print(f"  {k_label:>6} | {len(acdc_selected):>5} | {css_1of3:>5} | {css_2of3:>5} | {css_3of3:>5} | {j_ei_ep:>8.4f} | {j_ei_ac:>8.4f} | {j_ep_ac:>8.4f}")

    print(f"\n  --- Overlap details ---")
    for k in ["isinf", 50, 100]:
        if k == "isinf":
            acdc_selected = acdc_inf
            k_label = "isinf"
        else:
            acdc_selected = get_topk_edges(acdc_scores, k, use_abs=True)
            k_label = f"k={k}"

        overlap_all3 = eapig_top100 & ep_top100 & acdc_selected
        overlap_eapig_ep = (eapig_top100 & ep_top100) - acdc_selected
        overlap_eapig_acdc = (eapig_top100 & acdc_selected) - ep_top100
        overlap_ep_acdc = (ep_top100 & acdc_selected) - eapig_top100

        print(f"\n  [{k_label}] ACDC={len(acdc_selected)} edges")
        print(f"    All 3: {len(overlap_all3)}")
        print(f"    EAP-IG & EP only: {len(overlap_eapig_ep)}")
        print(f"    EAP-IG & ACDC only: {len(overlap_eapig_acdc)}")
        print(f"    EP & ACDC only: {len(overlap_ep_acdc)}")
        if len(overlap_all3) <= 30:
            print(f"    3/3 edges: {sorted(overlap_all3)}")


print("Loading scores...")
acdc_arith = load_scores("/root/structfuse-context/cache_acdc_arith.json")
eapig_arith = load_scores("/root/structfuse-context/cache_eap_ig_arith.json")
ep_arith = load_scores("/root/structfuse-context/cache_ep_arith.json")

acdc_ioi = load_scores("/root/structfuse-context/cache_acdc.json")
eapig_ioi = load_scores("/root/structfuse-context/cache_eap_ig.json")
ep_ioi = load_scores("/root/structfuse-context/cache_edge_pruning.json")

print(f"\nEdge key check:")
print(f"  Arith: ACDC={len(acdc_arith)}, EAP-IG={len(eapig_arith)}, EP={len(ep_arith)}")
print(f"  IOI:   ACDC={len(acdc_ioi)}, EAP-IG={len(eapig_ioi)}, EP={len(ep_ioi)}")

arith_keys_match = set(acdc_arith.keys()) == set(eapig_arith.keys()) == set(ep_arith.keys())
ioi_keys_match = set(acdc_ioi.keys()) == set(eapig_ioi.keys()) == set(ep_ioi.keys())
print(f"  Arith keys match: {arith_keys_match}")
print(f"  IOI keys match: {ioi_keys_match}")

run_sweep("Arithmetic", acdc_arith, eapig_arith, ep_arith)
run_sweep("IOI (baseline)", acdc_ioi, eapig_ioi, ep_ioi)

print(f"\n{'='*70}")
print("  DONE")
print(f"{'='*70}")
