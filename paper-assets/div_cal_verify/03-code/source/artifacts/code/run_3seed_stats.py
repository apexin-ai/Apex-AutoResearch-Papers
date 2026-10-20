#!/usr/bin/env python3
"""
3-seed statistical analysis for div_cal_verify phase2 experiments.

Reads gen0-gen7 metrics from all_results.json across 4 methods × 3 seeds,
outputs summary CSV and paired t-test results with Cohen's d.

Input:  /root/autodl-tmp/div_cal_verify/results_*/*/all_results.json
Output: artifacts/3seed_summary.csv, artifacts/3seed_ttest_results.csv
Deps:   numpy, scipy (stdlib json/os/csv/sys)
"""

import json
import os
import csv
import sys
from pathlib import Path

import numpy as np

try:
    from scipy import stats
except ImportError:
    print("ERROR: scipy not installed. Run: pip install scipy")
    sys.exit(1)

BASE = "/root/autodl-tmp/div_cal_verify"
OUT_DIR = Path(os.environ.get("OUT_DIR", "/root/div_cal_verify/artifacts"))

SEED_DIR_MAP = {
    42: {
        "uncurated":     f"{BASE}/results_phase2/uncurated/all_results.json",
        "external_only": f"{BASE}/results_phase2/external_only/all_results.json",
        "rgds":          f"{BASE}/results_phase2/rgds/all_results.json",
        "random_50":     f"{BASE}/results_random50/random_50/all_results.json",
    },
    123: {
        "uncurated":     f"{BASE}/results_phase2_seed123/uncurated/uncurated/all_results.json",
        "external_only": f"{BASE}/results_phase2_seed123/external_only/external_only/all_results.json",
        "rgds":          f"{BASE}/results_phase2_seed123/rgds/rgds/all_results.json",
        "random_50":     f"{BASE}/results_random50_seed123/random_50/all_results.json",
    },
    456: {
        "uncurated":     f"{BASE}/results_seed456/uncurated/uncurated/all_results.json",
        "external_only": f"{BASE}/results_seed456/external_only/external_only/all_results.json",
        "rgds":          f"{BASE}/results_seed456/rgds/rgds/all_results.json",
        "random_50":     f"{BASE}/results_random50_seed456/random_50/all_results.json",
    },
}

METRICS = ["ppl", "rare", "rankme", "knn", "corr", "ratio"]
FIELD_MAP = {
    "ppl":    "held_out_perplexity",
    "rare":   "rare_ngram_survival",
    "rankme": "rankme",
    "knn":    "knn_probe_accuracy",
    "corr":   "rank_correlation",
    "ratio":  "selection_rare_ngram_ratio",
}

COMPARISONS = [
    ("rgds_vs_uncurated",  "rgds",          "uncurated",     "C1/C3: RGDS accelerates collapse"),
    ("ext_vs_random50",    "external_only",  "random_50",     "C2-revised: external ~ random"),
    ("rgds_vs_random50",   "rgds",          "random_50",     "C3: RGDS worse than random"),
]


def load_results(path):
    if not os.path.exists(path):
        return None
    with open(path) as f:
        text = f.read().replace("NaN", "null")
        data = json.loads(text)
    return data


def extract_gen_metrics(data):
    rows = []
    for g in data["generations"]:
        row = {"gen": g["generation"]}
        for short, full in FIELD_MAP.items():
            row[short] = g.get(full)
        rows.append(row)
    return rows


def cohens_d(x, y):
    diff = np.array(x, dtype=float) - np.array(y, dtype=float)
    sd = np.std(diff, ddof=1)
    if sd == 0:
        return float("inf") if np.mean(diff) != 0 else 0.0
    return float(np.mean(diff) / sd)


def main():
    os.makedirs(OUT_DIR, exist_ok=True)

    # --- Phase 1: Load all data ---
    all_rows = []
    method_seed_gen7 = {}
    method_availability = {}

    for seed, methods in SEED_DIR_MAP.items():
        for method, path in methods.items():
            data = load_results(path)
            if data is None:
                print(f"  SKIP {method} seed={seed}: file not found")
                continue

            gens = extract_gen_metrics(data)
            max_gen = max(r["gen"] for r in gens)
            print(f"  OK   {method} seed={seed}: {len(gens)} gens (0-{max_gen})")

            for r in gens:
                all_rows.append({
                    "method": method,
                    "seed": seed,
                    "gen": r["gen"],
                    **{m: r[m] for m in METRICS}
                })

            gen7 = [r for r in gens if r["gen"] == 7]
            if gen7:
                key = (method, seed)
                method_seed_gen7[key] = gen7[0]
                method_availability.setdefault(method, []).append(seed)

    # --- Phase 2: Write summary CSV ---
    summary_path = OUT_DIR / "3seed_summary.csv"
    with open(summary_path, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["method", "seed", "gen"] + METRICS)
        writer.writeheader()
        for row in sorted(all_rows, key=lambda r: (r["method"], r["seed"], r["gen"])):
            writer.writerow(row)
    print(f"\nSummary CSV: {summary_path} ({len(all_rows)} rows)")

    # --- Phase 3: Print gen7 summary per method ---
    print("\n=== Gen7 Summary (mean +/- std) ===")
    for method in ["uncurated", "external_only", "rgds", "random_50"]:
        seeds = method_availability.get(method, [])
        n = len(seeds)
        if n == 0:
            print(f"  {method}: no data")
            continue
        vals = {m: [] for m in ["ppl", "rare", "rankme"]}
        for s in seeds:
            g7 = method_seed_gen7[(method, s)]
            for m in vals:
                if g7[m] is not None:
                    vals[m].append(g7[m])
        parts = []
        for m in ["ppl", "rare", "rankme"]:
            v = vals[m]
            if len(v) >= 2:
                parts.append(f"{m}={np.mean(v):.2f}+/-{np.std(v, ddof=1):.2f}")
            elif len(v) == 1:
                parts.append(f"{m}={v[0]:.4f}")
        status = f"{n} seeds" + (" [COMPLETE]" if n == 3 else " [PARTIAL]")
        print(f"  {method} ({status}): {', '.join(parts)}")

    # --- Phase 4: Paired t-tests ---
    print("\n=== Paired t-tests (gen7, 3-seed) ===")
    ttest_rows = []
    test_metrics = ["ppl", "rare", "rankme"]

    for comp_name, method_a, method_b, hypothesis in COMPARISONS:
        seeds_a = set(method_availability.get(method_a, []))
        seeds_b = set(method_availability.get(method_b, []))
        common_seeds = sorted(seeds_a & seeds_b)

        if len(common_seeds) < 3:
            print(f"\n  {comp_name}: only {len(common_seeds)} common seeds, need 3 -- skipped")
            for m in test_metrics:
                if len(common_seeds) >= 2:
                    va = [method_seed_gen7[(method_a, s)][m] for s in common_seeds if method_seed_gen7[(method_a, s)][m] is not None]
                    vb = [method_seed_gen7[(method_b, s)][m] for s in common_seeds if method_seed_gen7[(method_b, s)][m] is not None]
                    if len(va) == len(vb) and len(va) >= 2:
                        ttest_rows.append({
                            "comparison": comp_name,
                            "metric": m,
                            "t_stat": "N/A",
                            "p_value": "N/A",
                            "cohens_d": "N/A",
                            "mean_diff": f"{np.mean(va) - np.mean(vb):.4f}",
                            "n_seeds": len(common_seeds),
                            "conclusion": f"PARTIAL ({len(common_seeds)} seeds): {method_a} mean={np.mean(va):.2f}, {method_b} mean={np.mean(vb):.2f}",
                        })
            continue

        print(f"\n  {comp_name} ({hypothesis})")
        for m in test_metrics:
            va = [method_seed_gen7[(method_a, s)][m] for s in common_seeds]
            vb = [method_seed_gen7[(method_b, s)][m] for s in common_seeds]

            if any(v is None for v in va + vb):
                print(f"    {m}: missing values, skipped")
                continue

            t_stat, p_val = stats.ttest_rel(va, vb)
            d = cohens_d(va, vb)
            mean_diff = np.mean(va) - np.mean(vb)

            sig = "***" if p_val < 0.001 else "**" if p_val < 0.01 else "*" if p_val < 0.05 else "ns"
            direction = f"{method_a} > {method_b}" if mean_diff > 0 else f"{method_a} < {method_b}"

            conclusion = f"{sig} {direction} (d={d:.2f})"
            print(f"    {m}: t={t_stat:.3f}, p={p_val:.4f}, d={d:.2f}, diff={mean_diff:.4f} -> {conclusion}")

            ttest_rows.append({
                "comparison": comp_name,
                "metric": m,
                "t_stat": f"{t_stat:.4f}",
                "p_value": f"{p_val:.6f}",
                "cohens_d": f"{d:.4f}",
                "mean_diff": f"{mean_diff:.4f}",
                "n_seeds": len(common_seeds),
                "conclusion": conclusion,
            })

    # --- Phase 5: Write t-test CSV ---
    ttest_path = OUT_DIR / "3seed_ttest_results.csv"
    with open(ttest_path, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["comparison", "metric", "t_stat", "p_value", "cohens_d", "mean_diff", "n_seeds", "conclusion"])
        writer.writeheader()
        for row in ttest_rows:
            writer.writerow(row)
    print(f"\nt-test CSV: {ttest_path} ({len(ttest_rows)} rows)")


if __name__ == "__main__":
    main()
