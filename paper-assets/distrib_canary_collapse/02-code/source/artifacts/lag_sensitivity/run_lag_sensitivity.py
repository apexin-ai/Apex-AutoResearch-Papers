"""Lag sensitivity analysis for permutation Granger causality.

Runs permutation Granger test with lag=1,2,3 across all alpha-sweep experiments
and the alpha=1.00 generalize experiment, then applies per-alpha BH FDR correction.
"""

import json
import os
import csv
import sys
import numpy as np

sys.path.insert(0, "/root/autodl-tmp/distrib_canary_collapse")
from permutation_granger import permutation_granger_test

N_PERM = 5000
ALPHA_FDR = 0.05

CANARIES = ["token_entropy", "ece"]
DOWNSTREAMS = ["distinct_1", "distinct_2", "distinct_3", "perplexity"]
PAIRS = [(c, d) for c in CANARIES for d in DOWNSTREAMS]

EXPERIMENTS = {
    0.00: [
        ("a000_s42", 42, "results/alpha_sweep/a000_s42"),
        ("a000_s43", 43, "results/alpha_sweep/a000_s43"),
        ("a000_s44", 44, "results/alpha_sweep/a000_s44"),
    ],
    0.25: [
        ("a025_s43", 43, "results/alpha_sweep/a025_s43"),
        ("a025_s44", 44, "results/alpha_sweep/a025_s44"),
    ],
    0.50: [
        ("a050_s42", 42, "results/alpha_sweep/a050_s42"),
        ("a050_s43", 43, "results/alpha_sweep/a050_s43"),
        ("a050_s44", 44, "results/alpha_sweep/a050_s44"),
    ],
    0.75: [
        ("a075_s42", 42, "results/alpha_sweep/a075_s42"),
        ("a075_s43", 43, "results/alpha_sweep/a075_s43"),
        ("a075_s44", 44, "results/alpha_sweep/a075_s44"),
    ],
    1.00: [
        ("pythia410m_wiki_a100_s42", 42, "results/generalize/pythia410m_wiki_a100_s42"),
    ],
}

LAGS = [1, 2, 3]
BASE = "/root/autodl-tmp/distrib_canary_collapse"


def load_series(data_dir):
    all_path = os.path.join(data_dir, "all_metrics.json")
    with open(all_path) as f:
        data = json.load(f)
    data.sort(key=lambda x: x["generation"])
    out = {}
    for k in CANARIES + DOWNSTREAMS:
        out[k] = np.array([d[k] for d in data])
    return out, len(data)


def bh_fdr(p_values, alpha=0.05):
    pv = np.array(p_values, dtype=float)
    n = len(pv)
    valid = ~np.isnan(pv)
    adjusted = np.full(n, np.nan)
    if valid.sum() == 0:
        return adjusted.tolist(), [False] * n
    idx = np.where(valid)[0]
    p_valid = pv[idx]
    sorted_idx = np.argsort(p_valid)
    ranks = np.empty_like(sorted_idx)
    ranks[sorted_idx] = np.arange(1, len(p_valid) + 1)
    m = len(p_valid)
    adj = p_valid * m / ranks
    adj_sorted = adj[sorted_idx].copy()
    for i in range(m - 2, -1, -1):
        adj_sorted[i] = min(adj_sorted[i], adj_sorted[i + 1])
    adj_sorted = np.minimum(adj_sorted, 1.0)
    adj_final = np.empty(m)
    adj_final[sorted_idx] = adj_sorted
    for i, ix in enumerate(idx):
        adjusted[ix] = adj_final[i]
    significant = [(adjusted[i] < alpha if not np.isnan(adjusted[i]) else False) for i in range(n)]
    return adjusted.tolist(), significant


def main():
    all_rows = []

    for alpha_val, exps in EXPERIMENTS.items():
        for exp_name, seed, rel_path in exps:
            data_dir = os.path.join(BASE, rel_path)
            if not os.path.exists(os.path.join(data_dir, "all_metrics.json")):
                print(f"SKIP {exp_name}: no all_metrics.json")
                continue

            series, n_gens = load_series(data_dir)
            print(f"Processing {exp_name} (alpha={alpha_val}, seed={seed}, T={n_gens})")

            for lag in LAGS:
                for c_name, d_name in PAIRS:
                    pair_label = f"{c_name}->{d_name}"
                    try:
                        result = permutation_granger_test(
                            series[c_name], series[d_name],
                            max_lag=lag, n_perm=N_PERM, seed=seed,
                            difference=True
                        )
                        raw_p = result.get("p_value")
                    except (AssertionError, Exception) as e:
                        raw_p = None
                        print(f"  WARN {pair_label} lag={lag}: {e}")

                    all_rows.append({
                        "alpha": alpha_val,
                        "seed": seed,
                        "exp_name": exp_name,
                        "lag": lag,
                        "pair": pair_label,
                        "raw_p": raw_p,
                        "fdr_sig": None,
                        "n_perm": N_PERM,
                        "n_gens": n_gens,
                    })

    # Per-alpha BH FDR correction (pool all seeds within same alpha)
    for alpha_val in EXPERIMENTS:
        for lag in LAGS:
            subset_idx = [i for i, r in enumerate(all_rows)
                          if r["alpha"] == alpha_val and r["lag"] == lag]
            p_vals = [all_rows[i]["raw_p"] if all_rows[i]["raw_p"] is not None else np.nan
                      for i in subset_idx]
            if not p_vals:
                continue
            _, sig_list = bh_fdr(p_vals, ALPHA_FDR)
            for j, idx in enumerate(subset_idx):
                all_rows[idx]["fdr_sig"] = sig_list[j]

    # Write detailed CSV
    out_dir = "/root/autodl-tmp/distrib_canary_collapse/results/lag_sensitivity"
    os.makedirs(out_dir, exist_ok=True)

    detail_path = os.path.join(out_dir, "lag_sensitivity.csv")
    with open(detail_path, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["alpha", "seed", "lag", "pair", "raw_p", "fdr_sig", "n_perm"])
        w.writeheader()
        for r in all_rows:
            w.writerow({
                "alpha": r["alpha"],
                "seed": r["seed"],
                "lag": r["lag"],
                "pair": r["pair"],
                "raw_p": f"{r['raw_p']:.6f}" if r["raw_p"] is not None else "",
                "fdr_sig": r["fdr_sig"] if r["fdr_sig"] is not None else "",
                "n_perm": r["n_perm"],
            })
    print(f"\nSaved: {detail_path}")

    # Summary CSV: per alpha x lag
    summary_path = os.path.join(out_dir, "lag_sensitivity_summary.csv")
    summary_rows = []
    for alpha_val in sorted(EXPERIMENTS.keys()):
        for lag in LAGS:
            subset = [r for r in all_rows if r["alpha"] == alpha_val and r["lag"] == lag]
            if not subset:
                continue
            seeds = set(r["seed"] for r in subset)
            n_tests = len(subset)
            n_sig = sum(1 for r in subset if r["fdr_sig"] is True)
            sig_per_seed = {}
            for s in seeds:
                seed_tests = [r for r in subset if r["seed"] == s]
                sig_per_seed[s] = sum(1 for r in seed_tests if r["fdr_sig"] is True)
            mean_sig = np.mean(list(sig_per_seed.values()))
            sig_rate = n_sig / n_tests if n_tests > 0 else 0.0
            summary_rows.append({
                "alpha": alpha_val,
                "lag": lag,
                "n_seeds": len(seeds),
                "n_tests": n_tests,
                "n_sig": n_sig,
                "sig_rate": round(sig_rate, 4),
                "mean_sig_per_seed": round(mean_sig, 2),
            })

    with open(summary_path, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["alpha", "lag", "n_seeds", "n_tests", "n_sig", "sig_rate", "mean_sig_per_seed"])
        w.writeheader()
        for r in summary_rows:
            w.writerow(r)
    print(f"Saved: {summary_path}")

    # Print summary table
    print("\n" + "=" * 80)
    print("LAG SENSITIVITY SUMMARY: sig_rate (FDR-corrected) by alpha x lag")
    print("=" * 80)
    print(f"{'alpha':<8} {'lag=1':>12} {'lag=2':>12} {'lag=3':>12}")
    print("-" * 50)
    for alpha_val in sorted(EXPERIMENTS.keys()):
        line = f"{alpha_val:<8}"
        for lag in LAGS:
            match = [r for r in summary_rows if r["alpha"] == alpha_val and r["lag"] == lag]
            if match:
                sr = match[0]["sig_rate"]
                ns = match[0]["n_sig"]
                nt = match[0]["n_tests"]
                line += f" {sr:>5.1%} ({ns}/{nt})"
            else:
                line += f" {'N/A':>12}"
        print(line)
    print("=" * 80)

    # Also dump raw JSON for debugging
    json_path = os.path.join(out_dir, "lag_sensitivity_full.json")
    with open(json_path, "w") as f:
        json.dump(all_rows, f, indent=2, default=str)
    print(f"Saved: {json_path}")


if __name__ == "__main__":
    main()
