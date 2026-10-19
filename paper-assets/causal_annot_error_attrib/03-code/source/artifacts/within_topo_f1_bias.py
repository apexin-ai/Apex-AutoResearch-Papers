#!/usr/bin/env python3
"""
Within-topology Spearman ρ(macro_F1, |bias|) analysis.

Uses updated_empirical_results.json (23 configs × 7 topologies = 161 scenarios)
across HumAID, CivilComments, and VAST. Computes macro F1 from confusion matrices
using the same p_A priors as the main pipeline.
"""
import json
import os
from collections import defaultdict

import numpy as np
from scipy.stats import spearmanr

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "updated_empirical_results.json")
OUT = os.path.join(HERE, "within_topo_f1_bias_results.json")

TOPOS = ["confounding", "mediation", "collider", "exposure",
         "mbias", "frontdoor", "iv"]


def make_p_A(K):
    if K == 2:
        return np.array([0.55, 0.45])
    elif K == 3:
        return np.array([0.40, 0.35, 0.25])
    else:
        raw = np.array([1.0 / (i + 1) for i in range(K)])
        return raw / raw.sum()


def compute_f1_from_C(C, K, p_A):
    C = np.asarray(C)
    f1 = np.zeros(K)
    for i in range(K):
        recall_i = C[i, i]
        denom = sum(C[i, j] * p_A[j] for j in range(K))
        prec_i = C[i, i] * p_A[i] / denom if denom > 1e-12 else 0.0
        if prec_i + recall_i > 1e-12:
            f1[i] = 2 * prec_i * recall_i / (prec_i + recall_i)
    return float(f1.mean())


def _spearman(f1_list, bias_list):
    if len(f1_list) < 3:
        return None, None
    rho, p = spearmanr(f1_list, bias_list)
    return float(rho), float(p)


def main():
    with open(SRC) as f:
        data = json.load(f)

    cms = data["confusion_matrices"]
    biases_raw = data["biases"]

    config_f1 = {}
    for config_name, C_list in cms.items():
        K = len(C_list)
        mf1 = compute_f1_from_C(C_list, K, make_p_A(K))
        config_f1[config_name] = mf1

    rows = []
    for b in biases_raw:
        cname = f"{b['dataset']}_{b['model']}_{b['prompt']}"
        if cname not in config_f1:
            continue
        if b["bias"] is None:
            continue
        mf1 = config_f1[cname]
        if mf1 < 1e-6:
            continue
        rows.append({
            "config": cname,
            "dataset": b["dataset"],
            "topology": b["topology"],
            "macro_f1": mf1,
            "abs_bias": abs(b["bias"]),
        })

    # ── Per-topology (all datasets pooled) ──
    per_topo = {}
    for topo in TOPOS:
        sub = [r for r in rows if r["topology"] == topo]
        f1s = [r["macro_f1"] for r in sub]
        biases = [r["abs_bias"] for r in sub]
        rho, p = _spearman(f1s, biases)
        per_topo[topo] = {
            "n": len(sub),
            "spearman_rho": round(rho, 4) if rho is not None else None,
            "p_value": round(p, 4) if p is not None else None,
        }

    # ── Per-dataset × per-topology ──
    datasets = sorted(set(r["dataset"] for r in rows))
    per_ds_topo = {}
    for ds in datasets:
        per_ds_topo[ds] = {}
        for topo in TOPOS:
            sub = [r for r in rows if r["dataset"] == ds and r["topology"] == topo]
            f1s = [r["macro_f1"] for r in sub]
            biases = [r["abs_bias"] for r in sub]
            rho, p = _spearman(f1s, biases)
            per_ds_topo[ds][topo] = {
                "n": len(sub),
                "spearman_rho": round(rho, 4) if rho is not None else None,
                "p_value": round(p, 4) if p is not None else None,
            }

    # ── Overall ──
    all_f1 = [r["macro_f1"] for r in rows]
    all_bias = [r["abs_bias"] for r in rows]
    rho_all, p_all = _spearman(all_f1, all_bias)

    # ── Per-dataset overall ──
    per_ds_overall = {}
    for ds in datasets:
        sub = [r for r in rows if r["dataset"] == ds]
        f1s = [r["macro_f1"] for r in sub]
        biases = [r["abs_bias"] for r in sub]
        rho, p = _spearman(f1s, biases)
        per_ds_overall[ds] = {
            "n": len(sub),
            "spearman_rho": round(rho, 4) if rho is not None else None,
            "p_value": round(p, 4) if p is not None else None,
        }

    # ── Print ──
    print(f"Total scenarios: {len(rows)} "
          f"({len(config_f1)} configs × {len(TOPOS)} topologies)")
    for ds in datasets:
        n = sum(1 for r in rows if r["dataset"] == ds)
        print(f"  {ds}: {n}")
    print()

    print(f"Overall: ρ = {rho_all:.4f}, p = {p_all:.4f}, n = {len(rows)}")
    print()
    for ds in datasets:
        v = per_ds_overall[ds]
        print(f"  {ds}: ρ = {v['spearman_rho']:.4f}, p = {v['p_value']:.4f}, n = {v['n']}")
    print()

    fmt = f"{'topology':<14} {'n':>3}  {'ρ':>8}  {'p':>10}"
    print(fmt)
    print("-" * 40)
    for topo in TOPOS:
        t = per_topo[topo]
        rho_s = f"{t['spearman_rho']:+.4f}" if t["spearman_rho"] is not None else "   n/a"
        p_s = f"{t['p_value']:.4f}" if t["p_value"] is not None else "   n/a"
        print(f"  {topo:<12} {t['n']:>3}  {rho_s:>8}  {p_s:>10}")
    print("-" * 40)
    print(f"  {'overall':<12} {len(rows):>3}  {rho_all:+.4f}  {p_all:>10.4f}")
    print()

    print("Per-dataset × per-topology:")
    for ds in datasets:
        print(f"  {ds}:")
        for topo in TOPOS:
            t = per_ds_topo[ds][topo]
            if t["spearman_rho"] is not None:
                print(f"    {topo:<12} n={t['n']:>2}  ρ={t['spearman_rho']:+.4f}  p={t['p_value']:.4f}")
            else:
                print(f"    {topo:<12} n={t['n']:>2}  insufficient data")

    # ── Save ──
    results = {
        "description": ("Within-topology Spearman ρ(macro_F1, |bias|). "
                        "23 configs × 7 topologies across HumAID/CivilComments/VAST. "
                        "Configs with macro_F1 ≈ 0 excluded."),
        "source": "artifacts/updated_empirical_results.json",
        "overall": {
            "n": len(rows),
            "spearman_rho": round(rho_all, 4),
            "p_value": round(p_all, 4),
        },
        "per_dataset_overall": per_ds_overall,
        "per_topology": per_topo,
        "per_dataset_topology": per_ds_topo,
    }
    with open(OUT, "w") as f:
        json.dump(results, f, indent=2)
    print(f"\nSaved: {OUT}")


if __name__ == "__main__":
    main()
