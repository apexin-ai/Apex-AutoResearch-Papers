"""Tail-sensitive canary analysis: effective_rank, TTR, hapax vs downstream metrics.

Tests whether tail-sensitive indicators detect lead-lag signal in the blind zone (α=0.10).
"""

import json
import os
import sys
import numpy as np
from collections import Counter
from pathlib import Path

sys.path.insert(0, "/root/autodl-tmp/distrib_canary_collapse")
from permutation_granger import permutation_granger_test

N_PERM = 5000
FDR_Q = 0.05

EXPERIMENTS = {
    "a000": "results/alpha_sweep/a000_s42_fp32",
    "a010": "results/alpha_sweep/a010_s42_fp32",
    "a025": "results/alpha_sweep/a025_s42_fp32",
    "a050": "results/alpha_sweep/a050_s42_fp32",
}

CANARIES = ["effective_rank", "token_entropy", "ttr", "hapax_ratio"]
DOWNSTREAMS = ["distinct_1", "distinct_2", "distinct_3", "mauve"]


def compute_text_metrics(data_dir):
    """Compute TTR and hapax_legomena_ratio from synthetic_data for each generation."""
    gen_dirs = sorted(
        [d for d in Path(data_dir).iterdir() if d.name.startswith("gen_")],
        key=lambda d: int(d.name.split("_")[1])
    )
    ttr_series = []
    hapax_series = []

    for gd in gen_dirs:
        sd_path = gd / "synthetic_data"
        if not sd_path.exists():
            ttr_series.append(np.nan)
            hapax_series.append(np.nan)
            continue

        from datasets import load_from_disk
        ds = load_from_disk(str(sd_path))
        all_tokens = []
        for row in ds:
            all_tokens.extend(row["text"].split())

        total = len(all_tokens)
        if total == 0:
            ttr_series.append(np.nan)
            hapax_series.append(np.nan)
            continue

        counts = Counter(all_tokens)
        unique = len(counts)
        hapax = sum(1 for c in counts.values() if c == 1)

        ttr_series.append(unique / total)
        hapax_series.append(hapax / unique if unique > 0 else 0.0)

    return ttr_series, hapax_series


def load_metric_series(data_dir):
    """Load all metric time series including computed text metrics."""
    all_path = os.path.join(data_dir, "all_metrics.json")
    with open(all_path) as f:
        data = json.load(f)
    data.sort(key=lambda x: x["generation"])

    series = {}
    for k in ["token_entropy", "effective_rank", "distinct_1", "distinct_2", "distinct_3", "mauve"]:
        series[k] = np.array([d[k] for d in data])

    print(f"  Computing TTR/hapax from {len(data)} generations...")
    ttr, hapax = compute_text_metrics(data_dir)
    series["ttr"] = np.array(ttr)
    series["hapax_ratio"] = np.array(hapax)

    return series


def bh_fdr(pvals, q=FDR_Q):
    """Benjamini-Hochberg FDR correction."""
    pvals = np.array(pvals, dtype=float)
    n = len(pvals)
    valid = ~np.isnan(pvals)
    adjusted = np.full(n, np.nan)
    significant = np.full(n, False)

    if valid.sum() == 0:
        return adjusted, significant

    idx = np.where(valid)[0]
    p_sub = pvals[idx]
    order = np.argsort(p_sub)
    ranks = np.empty_like(order)
    ranks[order] = np.arange(1, len(p_sub) + 1)

    adj = p_sub * len(p_sub) / ranks
    adj = np.minimum.accumulate(adj[np.argsort(-ranks)])[np.argsort(np.argsort(-ranks))]
    adj = np.clip(adj, 0, 1)

    adjusted[idx] = adj
    significant[idx] = adj < q
    return adjusted, significant


def run_analysis():
    base = "/root/autodl-tmp/distrib_canary_collapse"
    all_results = {}

    for alpha_label, rel_path in EXPERIMENTS.items():
        data_dir = os.path.join(base, rel_path)
        print(f"\n{'='*60}")
        print(f"α={alpha_label}")
        print(f"{'='*60}")

        series = load_metric_series(data_dir)

        print(f"  Series lengths: {', '.join(f'{k}={len(v)}' for k,v in series.items())}")
        print(f"  effective_rank: {series['effective_rank']}")
        print(f"  ttr: {series['ttr']}")
        print(f"  hapax_ratio: {series['hapax_ratio']}")

        pairs = []
        raw_pvals = []

        for cn in CANARIES:
            for dn in DOWNSTREAMS:
                c = series[cn]
                d = series[dn]

                result = permutation_granger_test(c, d, max_lag=1, n_perm=N_PERM, seed=42, difference=True)
                pairs.append({
                    "canary": cn,
                    "downstream": dn,
                    "f_stat": result["f_stat"],
                    "p_value": result["p_value"],
                    "effect_size_f2": result["effect_size_f2"],
                    "significant_raw": result["significant"],
                })
                raw_pvals.append(result["p_value"] if result["p_value"] is not None else np.nan)

        adj_pvals, sig_fdr = bh_fdr(raw_pvals)
        for i, p in enumerate(pairs):
            p["p_fdr"] = round(float(adj_pvals[i]), 6) if not np.isnan(adj_pvals[i]) else None
            p["significant_fdr"] = bool(sig_fdr[i])

        all_results[alpha_label] = pairs

        print(f"\n  {'Canary':<18} {'Downstream':<12} {'F-stat':>8} {'p_raw':>8} {'p_FDR':>8} {'Sig':>4}")
        print(f"  {'-'*70}")
        for p in pairs:
            f_str = f"{p['f_stat']:.3f}" if p['f_stat'] is not None else "N/A"
            pr_str = f"{p['p_value']:.4f}" if p['p_value'] is not None else "N/A"
            pf_str = f"{p['p_fdr']:.4f}" if p['p_fdr'] is not None else "N/A"
            sig_str = "*" if p['significant_fdr'] else ""
            print(f"  {p['canary']:<18} {p['downstream']:<12} {f_str:>8} {pr_str:>8} {pf_str:>8} {sig_str:>4}")

    # Summary comparison
    print(f"\n\n{'='*70}")
    print("SUMMARY: FDR-significant pairs per canary × α")
    print(f"{'='*70}")
    print(f"  {'Canary':<18} {'α=0.00':>8} {'α=0.10':>8} {'α=0.25':>8} {'α=0.50':>8}")
    print(f"  {'-'*52}")
    for cn in CANARIES:
        counts = []
        for al in ["a000", "a010", "a025", "a050"]:
            c = sum(1 for p in all_results[al] if p["canary"] == cn and p["significant_fdr"])
            counts.append(f"{c}/4")
        print(f"  {cn:<18} {'  '.join(f'{c:>6}' for c in counts)}")

    # Detailed α=0.10 focus
    print(f"\n\nFOCUS: α=0.10 (blind zone)")
    print(f"{'='*70}")
    for p in all_results["a010"]:
        if p["significant_fdr"]:
            print(f"  SIGNAL: {p['canary']} → {p['downstream']} (F={p['f_stat']:.3f}, p_FDR={p['p_fdr']:.4f}, f²={p['effect_size_f2']})")
    nosig = [p for p in all_results["a010"] if not p["significant_fdr"]]
    if len(nosig) == len(all_results["a010"]):
        print("  No FDR-significant signals detected.")

    # Save JSON
    out_dir = os.path.join(base, "analysis", "tail_sensitive_canary")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "permg_results.json")
    with open(out_path, "w") as f:
        json.dump(all_results, f, indent=2, default=str)
    print(f"\nResults saved to {out_path}")

    return all_results


if __name__ == "__main__":
    run_analysis()
