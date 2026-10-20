#!/usr/bin/env python3
"""
Generate Appendix app:4pl_ablation — Per-benchmark power curves (3PL vs 4PL).

For each benchmark, computes detection power of lz* (Snijders 2001) under:
  - 4PL model (original PSN-IRT parameters)
  - 3PL model (d forced to 1.0)

Two-sided test at α = 0.05 (reject if |lz*| > 1.96).
"""

import os
import sys
import json
import time
import csv
from multiprocessing import Pool, cpu_count

import numpy as np

sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "src"))
from person_fit import (
    prob_4pl,
    generate_response,
    estimate_theta_mle,
    compute_lz_star,
    filter_valid_items,
)

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PARAMS_DIR = os.path.join(PROJECT_ROOT, "params")
RESULTS_DIR = os.path.join(PROJECT_ROOT, "results")

BENCHMARKS = ["mmlu", "hellaswag", "gsm8k", "arc_c", "humaneval"]
CONTAMINATION_LEVELS = [5, 10, 15, 25, 50, 75, 100]
N_SIMS = 2000
SEED = 12345
ALPHA = 0.05
Z_CRIT = 1.96  # two-sided: reject if |lz*| > 1.96
BATCH_SIZE = 500  # for memory safety on large benchmarks


def load_item_params(benchmark):
    path = os.path.join(PARAMS_DIR, f"{benchmark}_params.csv")
    rows = []
    with open(path) as f:
        reader = csv.DictReader(f)
        for row in reader:
            rows.append(row)

    a = np.array([float(r["a_discrimination"]) for r in rows], dtype=np.float64)
    b = np.array([float(r["b_difficulty"]) for r in rows], dtype=np.float64)
    c = np.array([float(r["c_guessing"]) for r in rows], dtype=np.float64)
    d = np.array([float(r["d_feasibility"]) for r in rows], dtype=np.float64)

    mask = filter_valid_items(a, b, c, d, min_a=0.0)
    return a[mask], b[mask], c[mask], d[mask]


def run_single_sim(args):
    a, b, c, d, contam_pct, seed_i = args
    rng = np.random.RandomState(seed_i)
    n_items = len(a)

    theta_true = rng.randn()
    x = generate_response(theta_true, a, b, c, d, rng=rng)

    if contam_pct > 0:
        n_contam = max(1, int(round(n_items * contam_pct / 100.0)))
        contam_idx = rng.choice(n_items, size=n_contam, replace=False)
        x[contam_idx] = 1

    theta_hat = estimate_theta_mle(x, a, b, c, d, theta_init=0.0, bounds=(-4, 4))
    lz_star = compute_lz_star(x, theta_hat, a, b, c, d)

    return {
        "lz_star": float(lz_star),
        "rejected": bool(abs(lz_star) > Z_CRIT),
    }


def run_batch_pooled(a, b, c, d, contam_pct, base_seed, n_sims, pool):
    task_args = [
        (a, b, c, d, contam_pct, base_seed + i)
        for i in range(n_sims)
    ]
    results = pool.map(run_single_sim, task_args, chunksize=50)
    return results


def run_batch_chunked(a, b, c, d, contam_pct, base_seed, n_sims, pool):
    """Run simulations in memory-safe chunks for large benchmarks."""
    all_results = []
    for chunk_start in range(0, n_sims, BATCH_SIZE):
        chunk_end = min(chunk_start + BATCH_SIZE, n_sims)
        chunk_size = chunk_end - chunk_start
        chunk_seed = base_seed + chunk_start
        results = run_batch_pooled(a, b, c, d, contam_pct, chunk_seed, chunk_size, pool)
        all_results.extend(results)
    return all_results


def summarize_results(results):
    valid = [r for r in results if not np.isnan(r["lz_star"])]
    n_valid = len(valid)
    if n_valid == 0:
        return {
            "n_sims": 0,
            "n_excluded": len(results),
            "power": 0.0,
            "mean_lz_star": float("nan"),
            "std_lz_star": float("nan"),
        }

    n_rejected = sum(1 for r in valid if r["rejected"])
    lz_vals = [r["lz_star"] for r in valid]
    return {
        "n_sims": n_valid,
        "n_excluded": len(results) - n_valid,
        "power": round(n_rejected / n_valid, 4),
        "mean_lz_star": round(float(np.mean(lz_vals)), 4),
        "std_lz_star": round(float(np.std(lz_vals)), 4),
    }


def main():
    os.makedirs(RESULTS_DIR, exist_ok=True)

    n_workers = max(1, cpu_count() - 1)
    print(f"Workers: {n_workers}, N_SIMS: {N_SIMS}, two-sided α={ALPHA}")

    all_params = {}
    for bm in BENCHMARKS:
        a, b, c, d = load_item_params(bm)
        all_params[bm] = {"a": a, "b": b, "c": c, "d": d, "n_items": len(a)}
        print(f"  {bm}: {len(a)} valid items")

    csv_rows = []
    summary = {}
    seed_offset = 0

    pool = Pool(processes=n_workers)

    try:
        for bm in BENCHMARKS:
            params = all_params[bm]
            a, b, c, d = params["a"], params["b"], params["c"], params["d"]
            n_items = params["n_items"]
            use_chunked = n_items > 5000

            d_3pl = np.ones_like(d)

            bm_summary = {"n_items": n_items, "levels": {}}
            print(f"\n{'='*60}")
            print(f"{bm} (n_items={n_items}, {'chunked' if use_chunked else 'pooled'})")
            print(f"{'='*60}")
            print(f"{'contam':>6} | {'model':>5} | {'power':>6} | {'mean_lz*':>9} | {'std_lz*':>8} | {'n_sim':>5} | {'time':>5}")

            for contam_pct in CONTAMINATION_LEVELS:
                level_summary = {}

                for model_name, d_use in [("4PL", d), ("3PL", d_3pl)]:
                    t0 = time.time()
                    base_seed = SEED + seed_offset
                    seed_offset += N_SIMS

                    if use_chunked:
                        results = run_batch_chunked(a, b, c, d_use, contam_pct, base_seed, N_SIMS, pool)
                    else:
                        results = run_batch_pooled(a, b, c, d_use, contam_pct, base_seed, N_SIMS, pool)

                    stats = summarize_results(results)
                    elapsed = time.time() - t0

                    level_summary[model_name] = stats

                    csv_rows.append({
                        "benchmark": bm,
                        "contamination_pct": contam_pct,
                        "model": model_name,
                        "power": stats["power"],
                        "mean_lz_star": stats["mean_lz_star"],
                        "std_lz_star": stats["std_lz_star"],
                        "n_sim": stats["n_sims"],
                    })

                    print(f"{contam_pct:>5}% | {model_name:>5} | {stats['power']:>6.3f} | "
                          f"{stats['mean_lz_star']:>+9.4f} | {stats['std_lz_star']:>8.4f} | "
                          f"{stats['n_sims']:>5} | {elapsed:>5.1f}s")

                bm_summary["levels"][contam_pct] = level_summary

            summary[bm] = bm_summary

    finally:
        pool.close()
        pool.join()

    # Write CSV
    csv_path = os.path.join(RESULTS_DIR, "appendix_4pl_ablation.csv")
    with open(csv_path, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=[
            "benchmark", "contamination_pct", "model", "power",
            "mean_lz_star", "std_lz_star", "n_sim",
        ])
        writer.writeheader()
        writer.writerows(csv_rows)
    print(f"\nCSV → {csv_path} ({len(csv_rows)} rows)")

    # Write JSON summary
    json_path = os.path.join(RESULTS_DIR, "appendix_4pl_ablation_summary.json")
    json_output = {
        "description": "3PL vs 4PL ablation: per-benchmark power curves",
        "test": "two-sided",
        "alpha": ALPHA,
        "z_crit": Z_CRIT,
        "n_sims": N_SIMS,
        "seed": SEED,
        "contamination_levels": CONTAMINATION_LEVELS,
        "benchmarks": summary,
    }
    with open(json_path, "w") as f:
        json.dump(json_output, f, indent=2)
    print(f"JSON → {json_path}")

    # Sanity check
    print(f"\n{'='*60}")
    print("SANITY CHECK")
    print(f"{'='*60}")
    has_nan = False
    for row in csv_rows:
        if row["power"] != row["power"] or row["mean_lz_star"] != row["mean_lz_star"]:
            print(f"  NaN detected: {row}")
            has_nan = True
    if not has_nan:
        print("  No NaN values detected.")


if __name__ == "__main__":
    main()
