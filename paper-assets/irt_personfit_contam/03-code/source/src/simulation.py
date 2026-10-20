"""
Contamination simulation study: tests whether lz* person-fit statistic
can detect benchmark contamination under a 4PL IRT model.

For each benchmark, generates clean responses from θ ~ N(0,1), injects
contamination (forcing k% of items correct), estimates θ_hat via MLE,
computes lz*, and measures detection power at α = 0.05.
"""

import os
import sys
import json
import time
import warnings
from multiprocessing import Pool, cpu_count

import numpy as np
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.ticker import PercentFormatter

sys.path.insert(0, os.path.dirname(__file__))
from person_fit import (
    prob_4pl,
    generate_response,
    log_likelihood,
    estimate_theta_mle,
    compute_lz_star,
    compute_lz,
    compute_outfit,
    compute_infit,
    filter_valid_items,
)

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PARAMS_DIR = os.path.join(PROJECT_ROOT, "artifacts", "psn_irt_params")
OUTPUT_DIR = os.path.join(PROJECT_ROOT, "artifacts", "extended_simulation")
DETAIL_DIR = os.path.join(OUTPUT_DIR, "power_by_benchmark")

BENCHMARKS = ["mmlu", "hellaswag", "gsm8k", "arc_c", "humaneval"]
CONTAMINATION_LEVELS = [0, 3, 5, 10, 15, 25, 50, 60, 75, 90, 100]
N_SIMS = 2000
SEED = 42
ALPHA = 0.05
Z_CRIT = -1.6449  # norm.ppf(0.05), one-sided left

LARGE_THRESHOLD = 1000  # items >= this → "large" tier
PASS_LARGE = 0.80       # 15% contamination detection rate threshold for large benchmarks
PASS_SMALL = 0.50       # 15% contamination detection rate threshold for small benchmarks

BENCHMARK_COLORS = {
    "mmlu": "#1f77b4",
    "hellaswag": "#ff7f0e",
    "gsm8k": "#2ca02c",
    "arc_c": "#d62728",
    "humaneval": "#9467bd",
}
BENCHMARK_MARKERS = {
    "mmlu": "o",
    "hellaswag": "s",
    "gsm8k": "^",
    "arc_c": "D",
    "humaneval": "v",
}


# ---------------------------------------------------------------------------
# Data loading
# ---------------------------------------------------------------------------

def load_item_params(benchmark: str) -> dict:
    """Load and filter item parameters for a benchmark.

    Returns dict with keys: a, b, c, d (numpy arrays), n_items (int).
    """
    path = os.path.join(PARAMS_DIR, f"{benchmark}_params.csv")
    df = pd.read_csv(path)
    a = df["a_discrimination"].values.astype(np.float64)
    b = df["b_difficulty"].values.astype(np.float64)
    c = df["c_guessing"].values.astype(np.float64)
    d = df["d_feasibility"].values.astype(np.float64)

    mask = filter_valid_items(a, b, c, d, min_a=0.0)
    a, b, c, d = a[mask], b[mask], c[mask], d[mask]

    return {"a": a, "b": b, "c": c, "d": d, "n_items": len(a)}


# ---------------------------------------------------------------------------
# Single simulation run
# ---------------------------------------------------------------------------

def run_single_sim(args):
    """Run one simulation trial.

    Args:
        args: tuple of (a, b, c, d, contam_pct, seed_i)

    Returns:
        dict with theta_true, theta_hat, lz_star, lz, outfit, infit, rejected
    """
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
    lz = compute_lz(x, theta_hat, a, b, c, d)
    outfit = compute_outfit(x, theta_hat, a, b, c, d)
    infit = compute_infit(x, theta_hat, a, b, c, d)

    rejected = bool(lz_star < Z_CRIT)

    return {
        "theta_true": theta_true,
        "theta_hat": theta_hat,
        "lz_star": lz_star,
        "lz": lz,
        "outfit": outfit,
        "infit": infit,
        "rejected": rejected,
    }


# ---------------------------------------------------------------------------
# Batch simulation for one (benchmark, contamination_level)
# ---------------------------------------------------------------------------

def run_batch(benchmark: str, contam_pct: int, params: dict,
              base_seed: int, n_sims: int, pool: Pool = None):
    """Run n_sims simulations for a given benchmark and contamination level.

    Returns list of result dicts.
    """
    a, b, c, d = params["a"], params["b"], params["c"], params["d"]

    task_args = [
        (a, b, c, d, contam_pct, base_seed + i)
        for i in range(n_sims)
    ]

    if pool is not None:
        results = pool.map(run_single_sim, task_args, chunksize=50)
    else:
        results = [run_single_sim(arg) for arg in task_args]

    return results


# ---------------------------------------------------------------------------
# Wilson score confidence interval for proportions
# ---------------------------------------------------------------------------

def wilson_ci(n_success: int, n_total: int, z: float = 1.96):
    """Wilson score interval for a binomial proportion."""
    if n_total == 0:
        return (0.0, 0.0)
    p_hat = n_success / n_total
    denom = 1 + z**2 / n_total
    center = (p_hat + z**2 / (2 * n_total)) / denom
    half_width = (z / denom) * np.sqrt(p_hat * (1 - p_hat) / n_total + z**2 / (4 * n_total**2))
    return (max(0.0, center - half_width), min(1.0, center + half_width))


# ---------------------------------------------------------------------------
# Inverted-U detection
# ---------------------------------------------------------------------------

def detect_inverted_u(detection_rates: dict) -> bool:
    """Check if detection rate shows inverted-U shape.

    Inverted-U: power peaks at 15-50% contamination and drops at 100%.
    """
    levels = sorted(detection_rates.keys())
    rates = {lvl: detection_rates[lvl] for lvl in levels}

    mid_levels = [lvl for lvl in levels if 15 <= lvl <= 50]
    if not mid_levels or 100 not in rates:
        return False

    max_mid_rate = max(rates[lvl] for lvl in mid_levels)
    rate_100 = rates[100]

    peak_level = max(mid_levels, key=lambda l: rates[l])
    return rate_100 < max_mid_rate and peak_level in mid_levels


# ---------------------------------------------------------------------------
# Plotting
# ---------------------------------------------------------------------------

def plot_power_curves(all_results: dict, output_path: str):
    """Plot combined power curves for all benchmarks."""
    fig, ax = plt.subplots(figsize=(10, 6))

    for bm in BENCHMARKS:
        if bm not in all_results:
            continue
        bm_data = all_results[bm]
        n_items = bm_data["n_items"]
        levels = sorted(bm_data["contamination_levels"].keys())
        rates = [bm_data["contamination_levels"][lvl]["detection_rate"] for lvl in levels]

        ax.plot(
            levels, rates,
            color=BENCHMARK_COLORS[bm],
            marker=BENCHMARK_MARKERS[bm],
            linewidth=2, markersize=7,
            label=f"{bm} (n={n_items})",
        )

    ax.axhline(y=PASS_LARGE, color="gray", linestyle="--", alpha=0.7, label=f"{PASS_LARGE:.0%} threshold (large)")
    ax.axhline(y=PASS_SMALL, color="gray", linestyle=":", alpha=0.7, label=f"{PASS_SMALL:.0%} threshold (small)")
    ax.axhline(y=ALPHA, color="red", linestyle=":", alpha=0.4, label=f"α = {ALPHA}")

    ax.set_xlabel("Contamination Level (%)", fontsize=12)
    ax.set_ylabel("Detection Rate (Power)", fontsize=12)
    ax.set_title("Detection Power of lz* across Contamination Levels", fontsize=14)
    ax.set_xticks(CONTAMINATION_LEVELS)
    ax.set_ylim(-0.02, 1.05)
    ax.legend(loc="upper left", fontsize=9)
    ax.grid(True, alpha=0.3)

    fig.tight_layout()
    fig.savefig(output_path, dpi=150, bbox_inches="tight")
    plt.close(fig)


def plot_benchmark_detail(benchmark: str, bm_data: dict,
                          sim_records: list, output_path: str):
    """Plot detailed power curve + lz* distribution for one benchmark."""
    fig, (ax_top, ax_bot) = plt.subplots(2, 1, figsize=(10, 10),
                                          gridspec_kw={"height_ratios": [1, 1.2]})

    levels = sorted(bm_data["contamination_levels"].keys())
    rates = []
    ci_lo = []
    ci_hi = []
    for lvl in levels:
        info = bm_data["contamination_levels"][lvl]
        rate = info["detection_rate"]
        n_rej = int(round(rate * info["n_sims"]))
        lo, hi = wilson_ci(n_rej, info["n_sims"])
        rates.append(rate)
        ci_lo.append(lo)
        ci_hi.append(hi)

    rates = np.array(rates)
    ci_lo = np.array(ci_lo)
    ci_hi = np.array(ci_hi)

    ax_top.plot(levels, rates, "o-", color=BENCHMARK_COLORS.get(benchmark, "blue"),
                linewidth=2, markersize=7)
    ax_top.fill_between(levels, ci_lo, ci_hi, alpha=0.2,
                         color=BENCHMARK_COLORS.get(benchmark, "blue"))
    threshold = PASS_LARGE if bm_data["n_items"] >= LARGE_THRESHOLD else PASS_SMALL
    ax_top.axhline(y=threshold, color="gray", linestyle="--", alpha=0.7,
                    label=f"Threshold = {threshold:.0%}")
    ax_top.axhline(y=ALPHA, color="red", linestyle=":", alpha=0.4, label=f"α = {ALPHA}")
    ax_top.set_xlabel("Contamination Level (%)")
    ax_top.set_ylabel("Detection Rate (Power)")
    ax_top.set_title(f"{benchmark} — Power Curve with 95% CI (n_items={bm_data['n_items']})")
    ax_top.set_xticks(CONTAMINATION_LEVELS)
    ax_top.set_ylim(-0.02, 1.05)
    ax_top.legend(fontsize=9)
    ax_top.grid(True, alpha=0.3)

    # Bottom: lz* violin plot by contamination level
    lz_by_level = {}
    for rec in sim_records:
        if rec["benchmark"] != benchmark:
            continue
        lvl = rec["contamination_pct"]
        if lvl not in lz_by_level:
            lz_by_level[lvl] = []
        if not np.isnan(rec["lz_star"]):
            lz_by_level[lvl].append(rec["lz_star"])

    positions = list(range(len(levels)))
    violin_data = [lz_by_level.get(lvl, [0.0]) if lz_by_level.get(lvl) else [0.0] for lvl in levels]

    parts = ax_bot.violinplot(violin_data, positions=positions, showmeans=True,
                               showmedians=True, showextrema=False)
    for pc in parts["bodies"]:
        pc.set_facecolor(BENCHMARK_COLORS.get(benchmark, "blue"))
        pc.set_alpha(0.4)

    ax_bot.axhline(y=Z_CRIT, color="red", linestyle="--", alpha=0.7, label=f"z_crit = {Z_CRIT:.3f}")
    ax_bot.axhline(y=0, color="gray", linestyle="-", alpha=0.3)
    ax_bot.set_xticks(positions)
    ax_bot.set_xticklabels([f"{lvl}%" for lvl in levels])
    ax_bot.set_xlabel("Contamination Level (%)")
    ax_bot.set_ylabel("lz* statistic")
    ax_bot.set_title(f"{benchmark} — lz* Distribution by Contamination Level")
    ax_bot.legend(fontsize=9)
    ax_bot.grid(True, alpha=0.3)

    fig.tight_layout()
    fig.savefig(output_path, dpi=150, bbox_inches="tight")
    plt.close(fig)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    os.makedirs(DETAIL_DIR, exist_ok=True)

    n_workers = max(1, cpu_count() - 1)
    print(f"Using {n_workers} worker processes")

    # Load all benchmark params
    all_params = {}
    for bm in BENCHMARKS:
        params = load_item_params(bm)
        all_params[bm] = params
        print(f"Loaded {bm}: {params['n_items']} valid items")

    # Run simulations
    all_summary = {}
    all_records = []
    seed_offset = 0

    pool = Pool(processes=n_workers)

    try:
        for bm in BENCHMARKS:
            params = all_params[bm]
            n_items = params["n_items"]
            tier = "large" if n_items >= LARGE_THRESHOLD else "small"
            bm_summary = {
                "n_items": n_items,
                "tier": tier,
                "contamination_levels": {},
            }

            for contam_pct in CONTAMINATION_LEVELS:
                t0 = time.time()
                base_seed = SEED + seed_offset
                seed_offset += N_SIMS

                results = run_batch(bm, contam_pct, params, base_seed, N_SIMS, pool=pool)

                valid_results = [r for r in results if not np.isnan(r["lz_star"])]
                n_valid = len(valid_results)
                n_rejected = sum(1 for r in valid_results if r["rejected"])
                detection_rate = n_rejected / n_valid if n_valid > 0 else 0.0

                lz_stars = [r["lz_star"] for r in valid_results]
                mean_lz = np.mean(lz_stars) if lz_stars else np.nan
                std_lz = np.std(lz_stars) if lz_stars else np.nan

                bm_summary["contamination_levels"][contam_pct] = {
                    "n_sims": n_valid,
                    "n_excluded": N_SIMS - n_valid,
                    "detection_rate": round(detection_rate, 4),
                    "mean_lz_star": round(float(mean_lz), 4),
                    "std_lz_star": round(float(std_lz), 4),
                }

                for i, r in enumerate(results):
                    all_records.append({
                        "benchmark": bm,
                        "contamination_pct": contam_pct,
                        "sim_idx": i,
                        "theta_true": round(r["theta_true"], 6),
                        "theta_hat": round(r["theta_hat"], 6) if not np.isnan(r["theta_hat"]) else np.nan,
                        "lz_star": round(r["lz_star"], 6) if not np.isnan(r["lz_star"]) else np.nan,
                        "lz": round(r["lz"], 6) if not np.isnan(r["lz"]) else np.nan,
                        "outfit": round(r["outfit"], 6) if not np.isnan(r["outfit"]) else np.nan,
                        "infit": round(r["infit"], 6) if not np.isnan(r["infit"]) else np.nan,
                        "rejected": r["rejected"],
                    })

                elapsed = time.time() - t0
                print(f"  {bm} | contam={contam_pct:3d}% | "
                      f"power={detection_rate:.3f} | "
                      f"mean_lz*={mean_lz:+.3f} | "
                      f"n_valid={n_valid} | {elapsed:.1f}s")

            # Pass/fail and inverted-U
            det_rates = {lvl: info["detection_rate"]
                         for lvl, info in bm_summary["contamination_levels"].items()}
            threshold = PASS_LARGE if tier == "large" else PASS_SMALL
            bm_summary["pass_15pct"] = det_rates.get(15, 0.0) > threshold
            bm_summary["threshold"] = threshold
            bm_summary["inverted_u_detected"] = detect_inverted_u(det_rates)

            all_summary[bm] = bm_summary
            print(f"  → {bm} pass@15%: {bm_summary['pass_15pct']} "
                  f"(rate={det_rates.get(15, 0):.3f} vs {threshold:.2f}), "
                  f"inverted-U: {bm_summary['inverted_u_detected']}")
            print()

    finally:
        pool.close()
        pool.join()

    # Global pass
    large_bms = [bm for bm in all_summary if all_summary[bm]["tier"] == "large"]
    all_large_pass = all(all_summary[bm]["pass_15pct"] for bm in large_bms)
    any_inverted_u = any(all_summary[bm]["inverted_u_detected"] for bm in all_summary)
    global_pass = all_large_pass and any_inverted_u

    summary_output = {
        "global_pass": global_pass,
        "all_large_benchmarks_pass": all_large_pass,
        "inverted_u_observable": any_inverted_u,
        "benchmarks": all_summary,
    }

    # Save JSON summary
    json_path = os.path.join(OUTPUT_DIR, "simulation_summary.json")
    with open(json_path, "w") as f:
        json.dump(summary_output, f, indent=2)
    print(f"Saved summary → {json_path}")

    # Save detailed CSV
    csv_path = os.path.join(OUTPUT_DIR, "simulation_detailed.csv")
    df = pd.DataFrame(all_records)
    df.to_csv(csv_path, index=False)
    print(f"Saved detailed results → {csv_path} ({len(df)} rows)")

    # Plot combined power curves
    power_path = os.path.join(OUTPUT_DIR, "power_curves.png")
    plot_power_curves(all_summary, power_path)
    print(f"Saved power curves → {power_path}")

    # Plot per-benchmark details
    for bm in BENCHMARKS:
        if bm not in all_summary:
            continue
        detail_path = os.path.join(DETAIL_DIR, f"{bm}_power_detail.png")
        plot_benchmark_detail(bm, all_summary[bm], all_records, detail_path)
        print(f"Saved detail plot → {detail_path}")

    # Final verdict
    print()
    print("=" * 60)
    print(f"GLOBAL PASS: {global_pass}")
    print(f"  All large benchmarks pass @15%: {all_large_pass}")
    print(f"  Inverted-U observable: {any_inverted_u}")
    for bm in BENCHMARKS:
        if bm in all_summary:
            s = all_summary[bm]
            rate_15 = s["contamination_levels"].get(15, {}).get("detection_rate", "N/A")
            print(f"  {bm:12s} [{s['tier']:5s}] pass={s['pass_15pct']}  "
                  f"rate@15%={rate_15}  invU={s['inverted_u_detected']}")
    print("=" * 60)


if __name__ == "__main__":
    main()
