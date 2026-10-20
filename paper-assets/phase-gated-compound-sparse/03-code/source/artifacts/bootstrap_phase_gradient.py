#!/usr/bin/env python3
"""
M1' Bootstrap Phase Gradient Analysis for PACS

Quantifies statistical significance of the phase-dependent interaction pattern:
  gradient = median(II_low_sparsity) / median(II_high_sparsity)

Per-segment II distributions are reconstructed from aggregate profiling statistics
via log-normal fit (matching stored mean and median exactly), since raw per-segment
II values are not saved in profiling_results.json.

Usage:
  python bootstrap_phase_gradient.py \
    --inputs /path/s015.json:importance /path/s025.json:importance \
             /path/random_s015.json:random /path/random_s025.json:random \
    --output-dir ./analysis \
    --n-boot 1000
"""

import argparse
import json
import os
import sys
from collections import defaultdict
from typing import Any, Dict, List, Tuple

import numpy as np

try:
    from scipy import stats as sp_stats
    HAS_SCIPY = True
except ImportError:
    HAS_SCIPY = False

PHASES = ["high_sparsity", "mid_sparsity", "low_sparsity"]
PHASE_LABELS = {"high_sparsity": "high", "mid_sparsity": "mid", "low_sparsity": "low"}


def load_profiling(path: str) -> dict:
    with open(path) as f:
        return json.load(f)


def reconstruct_ii_samples(
    ii_stats: dict, n_segments: int, rng: np.random.RandomState
) -> np.ndarray:
    """Reconstruct per-segment II distribution from aggregate statistics.

    Primary: Log-normal fit matching stored mean and median exactly.
      mu = ln(median), sigma = sqrt(2 * ln(mean/median))
    Fallback: Gamma (skewness-based) or Normal for edge cases.
    """
    mean = ii_stats["mean"]
    median = ii_stats.get("median", mean)

    if mean > 0 and median > 0 and mean >= median:
        mu = np.log(median)
        sigma = np.sqrt(2.0 * np.log(mean / median))
        sigma = max(sigma, 1e-6)
        return rng.lognormal(mu, sigma, size=n_segments)
    elif mean > 0:
        skew = ii_stats.get("skewness", 1.0)
        k = max((2.0 / max(skew, 0.1)) ** 2, 0.01)
        theta = mean / k
        return rng.gamma(k, theta, size=n_segments)
    else:
        se = (ii_stats["ci_high"] - ii_stats["ci_low"]) / (2 * 1.96)
        sigma = se * np.sqrt(n_segments)
        return rng.normal(mean, max(sigma, 1e-8), size=n_segments)


def bootstrap_gradient(
    ii_low: np.ndarray,
    ii_high: np.ndarray,
    n_boot: int = 1000,
    seed: int = 42,
) -> Tuple[float, float, float, np.ndarray]:
    """Bootstrap CI for gradient = median(II_low) / median(II_high)."""
    rng = np.random.RandomState(seed)
    n_lo, n_hi = len(ii_low), len(ii_high)
    point = float(np.median(ii_low) / np.median(ii_high))

    boots = np.empty(n_boot)
    for i in range(n_boot):
        ml = np.median(ii_low[rng.randint(0, n_lo, n_lo)])
        mh = np.median(ii_high[rng.randint(0, n_hi, n_hi)])
        boots[i] = ml / mh if mh > 1e-12 else np.nan

    return (
        point,
        float(np.nanpercentile(boots, 2.5)),
        float(np.nanpercentile(boots, 97.5)),
        boots,
    )


def mann_whitney(x: np.ndarray, y: np.ndarray) -> Dict[str, Any]:
    """Mann-Whitney U test with rank-biserial effect size r_rb."""
    if not HAS_SCIPY:
        return {"U": None, "p": None, "r_rb": None, "note": "scipy unavailable"}
    u, p = sp_stats.mannwhitneyu(x, y, alternative="two-sided")
    n1, n2 = len(x), len(y)
    r_rb = 1 - 2 * u / (n1 * n2)
    return {"U": float(u), "p": float(p), "r_rb": round(float(r_rb), 4)}


def cohens_d(x: np.ndarray, y: np.ndarray) -> float:
    nx, ny = len(x), len(y)
    sp = np.sqrt(
        ((nx - 1) * np.var(x, ddof=1) + (ny - 1) * np.var(y, ddof=1))
        / (nx + ny - 2)
    )
    return float((np.mean(x) - np.mean(y)) / sp) if sp > 0 else 0.0


def parse_inputs(input_specs: List[str]) -> List[Tuple[str, str]]:
    """Parse 'path:strategy' input specifications."""
    pairs = []
    for spec in input_specs:
        if ":" not in spec:
            raise ValueError(f"Input must be 'path:strategy', got: {spec}")
        path, strategy = spec.rsplit(":", 1)
        if strategy not in ("importance", "random"):
            raise ValueError(
                f"Strategy must be 'importance' or 'random', got: {strategy}"
            )
        pairs.append((path, strategy))
    return pairs


def print_tables(results: dict):
    sep = "=" * 78

    # Table 1: Gradient estimates
    print(f"\n{sep}")
    print("Table 1: Phase Gradient = median(II_low) / median(II_high)")
    print(sep)
    print(
        f"{'Strategy':>12} {'Sparsity':>10} {'Gradient':>10}"
        f" {'95% CI':>22} {'p(MW)':>10} {'d':>8}"
    )
    print("-" * 78)

    for strategy in sorted(results["per_strategy"].keys()):
        for level_str in sorted(results["per_strategy"][strategy].keys()):
            r = results["per_strategy"][strategy][level_str]
            ci = r["gradient_95ci"]
            mwu_p = r["mann_whitney_U"].get("p")
            p_str = f"{mwu_p:.2e}" if mwu_p is not None else "n/a"
            print(
                f"{strategy:>12} {level_str:>10} {r['gradient']:>10.2f}"
                f"  [{ci[0]:>8.2f}, {ci[1]:>8.2f}]"
                f" {p_str:>10} {r['cohens_d']:>8.2f}"
            )

    # Table 2: Per-phase median II
    print(f"\n{sep}")
    print("Table 2: Per-Phase Median II (reconstructed)")
    print(sep)
    print(f"{'Strategy':>12} {'Sparsity':>10} {'high':>10} {'mid':>10} {'low':>10}")
    print("-" * 54)

    for strategy in sorted(results["per_strategy"].keys()):
        for level_str in sorted(results["per_strategy"][strategy].keys()):
            meds = results["per_strategy"][strategy][level_str]["phase_medians"]
            print(
                f"{strategy:>12} {level_str:>10}"
                f" {meds.get('high', 0):>10.4f}"
                f" {meds.get('mid', 0):>10.4f}"
                f" {meds.get('low', 0):>10.4f}"
            )

    # Table 3: Pairwise Mann-Whitney U between phases
    print(f"\n{sep}")
    print("Table 3: Pairwise Phase Comparisons (Mann-Whitney U)")
    print(sep)
    print(
        f"{'Strategy':>12} {'Sparsity':>10} {'Pair':>14}"
        f" {'U':>12} {'p':>12} {'r_rb':>8}"
    )
    print("-" * 72)

    for strategy in sorted(results["per_strategy"].keys()):
        for level_str in sorted(results["per_strategy"][strategy].keys()):
            r = results["per_strategy"][strategy][level_str]
            mwu = r["mann_whitney_U"]
            print(
                f"{strategy:>12} {level_str:>10} {'low vs high':>14}"
                f" {mwu.get('U', 0):>12.0f}"
                f" {mwu.get('p', 0):>12.2e}"
                f" {mwu.get('r_rb', 0):>8.4f}"
            )
            pw = r.get("pairwise_tests", {})
            for pair_name, pair_data in pw.items():
                print(
                    f"{'':>12} {'':>10} {pair_name:>14}"
                    f" {pair_data.get('U', 0):>12.0f}"
                    f" {pair_data.get('p', 0):>12.2e}"
                    f" {pair_data.get('r_rb', 0):>8.4f}"
                )

    # Table 4: Cross-strategy comparison
    if results["comparisons"]:
        print(f"\n{sep}")
        print("Table 4: Importance vs Random Gradient Comparison")
        print(sep)
        print(
            f"{'Sparsity':>10} {'Imp Grad':>10} {'Rnd Grad':>10}"
            f" {'Diff':>10} {'p(2s)':>10} {'Sig':>6}"
        )
        print("-" * 58)

        for level_str in sorted(results["comparisons"].keys()):
            c = results["comparisons"][level_str]
            sig = (
                "***"
                if c["p_value_two_sided"] < 0.001
                else "**"
                if c["p_value_two_sided"] < 0.01
                else "*"
                if c["p_value_two_sided"] < 0.05
                else "ns"
            )
            print(
                f"{level_str:>10}"
                f" {c['importance_gradient']:>10.2f}"
                f" {c['random_gradient']:>10.2f}"
                f" {c['gradient_diff']:>10.2f}"
                f" {c['p_value_two_sided']:>10.4f}"
                f" {sig:>6}"
            )

    print(f"\n{sep}")


def main():
    parser = argparse.ArgumentParser(
        description="M1' Bootstrap Phase Gradient Analysis"
    )
    parser.add_argument(
        "--inputs",
        nargs="+",
        required=True,
        help="Profiling JSON paths as 'path:strategy' (strategy=importance|random)",
    )
    parser.add_argument("--output-dir", default=".", help="Output directory")
    parser.add_argument("--n-boot", type=int, default=1000, help="Bootstrap resamples")
    parser.add_argument("--seed", type=int, default=42, help="Random seed")
    args = parser.parse_args()

    input_pairs = parse_inputs(args.inputs)
    rng = np.random.RandomState(args.seed)

    # ── Load & reconstruct per-segment II distributions ───────────
    all_data: Dict[str, Dict[str, Dict[str, np.ndarray]]] = defaultdict(
        lambda: defaultdict(dict)
    )
    source_info: List[str] = []

    for path, strategy in input_pairs:
        data = load_profiling(path)
        ii_section = data["interaction_index"]
        phase_stats = data["phase_stats"]
        sparsity_str = ",".join(str(s) for s in data["config"]["sparsity_levels"])
        source_info.append(f"{os.path.basename(path)} [{strategy}, s={sparsity_str}]")

        for phase in PHASES:
            if phase not in ii_section:
                continue
            for level_str, ii_stats in ii_section[phase].items():
                n_seg = phase_stats[phase]["n_segments"]
                samples = reconstruct_ii_samples(ii_stats, n_seg, rng)
                all_data[strategy][level_str][phase] = samples

    print(f"Loaded {len(input_pairs)} profiling runs:")
    for s in source_info:
        print(f"  {s}")

    # ── Per-strategy gradient analysis ────────────────────────────
    results: Dict[str, Any] = {
        "per_strategy": {},
        "comparisons": {},
        "metadata": {
            "n_boot": args.n_boot,
            "seed": args.seed,
            "reconstruction_method": "lognormal_mean_median_match",
            "inputs": [f"{p}:{s}" for p, s in input_pairs],
        },
    }

    boot_dists: Dict[str, Dict[str, np.ndarray]] = defaultdict(dict)

    for strategy in sorted(all_data.keys()):
        results["per_strategy"][strategy] = {}
        for level_str in sorted(all_data[strategy].keys()):
            phase_data = all_data[strategy][level_str]
            if "low_sparsity" not in phase_data or "high_sparsity" not in phase_data:
                continue

            ii_lo = phase_data["low_sparsity"]
            ii_hi = phase_data["high_sparsity"]

            grad, ci_lo, ci_hi, boots = bootstrap_gradient(
                ii_lo, ii_hi, n_boot=args.n_boot, seed=rng.randint(0, 2 ** 31)
            )
            boot_dists[strategy][level_str] = boots

            mwu = mann_whitney(ii_lo, ii_hi)
            d = cohens_d(ii_lo, ii_hi)

            entry: Dict[str, Any] = {
                "gradient": round(grad, 4),
                "gradient_95ci": [round(ci_lo, 4), round(ci_hi, 4)],
                "mann_whitney_U": mwu,
                "cohens_d": round(d, 4),
                "phase_medians": {
                    PHASE_LABELS[p]: round(float(np.median(phase_data[p])), 6)
                    for p in PHASES
                    if p in phase_data
                },
                "phase_means": {
                    PHASE_LABELS[p]: round(float(np.mean(phase_data[p])), 6)
                    for p in PHASES
                    if p in phase_data
                },
            }

            if "mid_sparsity" in phase_data:
                ii_mid = phase_data["mid_sparsity"]
                entry["pairwise_tests"] = {
                    "low vs mid": mann_whitney(ii_lo, ii_mid),
                    "mid vs high": mann_whitney(ii_mid, ii_hi),
                    "low vs high": mwu,
                }
                entry["pairwise_cohens_d"] = {
                    "low vs mid": round(cohens_d(ii_lo, ii_mid), 4),
                    "mid vs high": round(cohens_d(ii_mid, ii_hi), 4),
                    "low vs high": round(d, 4),
                }

            results["per_strategy"][strategy][level_str] = entry

    # ── Cross-strategy comparison ─────────────────────────────────
    imp_levels = boot_dists.get("importance", {})
    rnd_levels = boot_dists.get("random", {})
    shared = sorted(set(imp_levels.keys()) & set(rnd_levels.keys()))

    for level_str in shared:
        b_imp = imp_levels[level_str]
        b_rnd = rnd_levels[level_str]
        diff = b_imp - b_rnd
        p_one = float(np.mean(diff <= 0))
        p_two = 2 * min(p_one, 1 - p_one)

        imp_grad = results["per_strategy"]["importance"][level_str]["gradient"]
        rnd_grad = results["per_strategy"]["random"][level_str]["gradient"]

        results["comparisons"][level_str] = {
            "importance_gradient": imp_grad,
            "random_gradient": rnd_grad,
            "gradient_diff": round(imp_grad - rnd_grad, 4),
            "p_value_two_sided": round(p_two, 6),
            "p_value_one_sided_imp_gt_rnd": round(p_one, 6),
        }

    # ── Output ────────────────────────────────────────────────────
    print_tables(results)

    os.makedirs(args.output_dir, exist_ok=True)
    out_path = os.path.join(args.output_dir, "bootstrap_gradient_results.json")
    with open(out_path, "w") as f:
        json.dump(results, f, indent=2, ensure_ascii=False)
    print(f"JSON saved to {out_path}")


if __name__ == "__main__":
    main()
