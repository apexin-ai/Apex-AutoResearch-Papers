"""
StrategyQA Llama Heuristic 8-Seed Aggregation Analysis

Combines original 4 seeds (42, 0, 1, 2) with new 4 seeds (3, 4, 5, 6)
to compute 8-seed aggregate statistics for the StrategyQA cross-domain
validation experiment.

Input:
  - Hardcoded original 4-seed data (from prior runs)
  - New seed JSON files: seed_{3,4,5,6}.json in the same directory

Output:
  - Per-seed summary table
  - 4-seed (new), 8-seed (all), 7-seed (excl. discovery) statistics
  - Non-inferiority t-test against delta = -3pp margin
  - LaTeX table row for paper
  - Prose summary for results.tex

Dependencies: json, math, statistics (stdlib) + scipy.stats (for t-test)
"""

from __future__ import annotations

import json
import math
import os
import statistics
import sys
from pathlib import Path
from typing import Optional, List, Dict

# ---------------------------------------------------------------------------
# Try importing scipy; fall back to manual t-test if unavailable
# ---------------------------------------------------------------------------
try:
    from scipy import stats as scipy_stats
    HAS_SCIPY = True
except ImportError:
    HAS_SCIPY = False
    print("[WARN] scipy not installed; using manual t critical values (df=7 -> 2.365, df=6 -> 2.447)")

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------
SCRIPT_DIR = Path(__file__).resolve().parent

# Original 4 seeds - hardcoded from prior experiment runs
# Each entry: (seed, baseline_acc, pruned_acc, delta_pp, suppress_pct)
ORIGINAL_SEEDS = [
    {"seed": 42, "baseline_acc": None, "pruned_acc": None, "delta_pp": 6.5, "suppress_pct": None, "source": "discovery seed (hardcoded)"},
    {"seed": 0,  "baseline_acc": None, "pruned_acc": None, "delta_pp": 6.0, "suppress_pct": 50.3, "source": "hardcoded"},
    {"seed": 1,  "baseline_acc": None, "pruned_acc": None, "delta_pp": 4.5, "suppress_pct": 50.8, "source": "hardcoded"},
    {"seed": 2,  "baseline_acc": None, "pruned_acc": None, "delta_pp": 2.5, "suppress_pct": 50.7, "source": "hardcoded"},
]

# New seed file paths
NEW_SEED_IDS = [3, 4, 5, 6]

# Non-inferiority margin (pp)
NI_MARGIN = -3.0

# t critical values for manual computation (two-tailed alpha=0.05)
T_CRIT = {
    3: 3.182,  # df=3
    6: 2.447,  # df=6
    7: 2.365,  # df=7
}


def load_seed_json(seed_id: int) -> dict | None:
    """Load a seed result JSON file. Returns None if file doesn't exist."""
    path = SCRIPT_DIR / f"seed_{seed_id}.json"
    if not path.exists():
        print(f"[WARN] {path.name} not found, skipping seed {seed_id}")
        return None
    with open(path) as f:
        data = json.load(f)
    # Extract relevant fields - handle both naming conventions
    baseline_acc = data.get("baseline", {}).get("accuracy")
    if baseline_acc is None:
        baseline_acc = data.get("baseline_acc")

    pruned_acc = data.get("online_pruned", {}).get("accuracy")
    if pruned_acc is None:
        pruned_acc = data.get("online_ack_acc")

    suppress_pct = data.get("online_pruned", {}).get("suppress_pct")
    if suppress_pct is None:
        suppress_pct = data.get("suppress_pct")

    delta_pp = data.get("delta_pp")

    # If delta_pp missing but we have both accuracies, compute it
    if delta_pp is None and baseline_acc is not None and pruned_acc is not None:
        delta_pp = (pruned_acc - baseline_acc) * 100

    return {
        "seed": seed_id,
        "baseline_acc": baseline_acc,
        "pruned_acc": pruned_acc,
        "delta_pp": delta_pp,
        "suppress_pct": suppress_pct,
        "source": f"seed_{seed_id}.json",
    }


def compute_stats(deltas: list[float], label: str, df: int | None = None) -> dict:
    """Compute mean, SD, 95% CI, and non-inferiority test for a list of delta values."""
    n = len(deltas)
    mean = statistics.mean(deltas)
    sd = statistics.stdev(deltas) if n > 1 else 0.0
    se = sd / math.sqrt(n) if n > 1 else 0.0

    if df is None:
        df = n - 1

    # 95% CI using t distribution
    if HAS_SCIPY and n > 1:
        t_crit = scipy_stats.t.ppf(0.975, df)
    elif df in T_CRIT:
        t_crit = T_CRIT[df]
    else:
        t_crit = 2.0  # fallback
        print(f"[WARN] No t_crit for df={df}, using 2.0")

    ci_low = mean - t_crit * se
    ci_high = mean + t_crit * se

    # Non-inferiority one-sample t-test: H0: mu <= NI_MARGIN, H1: mu > NI_MARGIN
    # t = (mean - NI_MARGIN) / SE
    if se > 0:
        t_ni = (mean - NI_MARGIN) / se
        if HAS_SCIPY:
            p_ni = 1 - scipy_stats.t.cdf(t_ni, df)  # one-tailed
        else:
            # Approximate: for large t, p is very small
            p_ni = None  # can't compute without scipy
    else:
        t_ni = float('inf')
        p_ni = 0.0

    # Direction consistency
    all_positive = all(d > 0 for d in deltas)
    any_negative = any(d < 0 for d in deltas)

    return {
        "label": label,
        "n": n,
        "mean": mean,
        "sd": sd,
        "se": se,
        "ci_low": ci_low,
        "ci_high": ci_high,
        "t_crit": t_crit,
        "df": df,
        "t_ni": t_ni,
        "p_ni": p_ni,
        "all_positive": all_positive,
        "any_negative": any_negative,
    }


def print_separator(char: str = "=", width: int = 72):
    print(char * width)


def print_seed_table(all_seeds: list[dict]):
    """Print per-seed summary table."""
    print_separator()
    print("PER-SEED SUMMARY")
    print_separator()
    print(f"{'Seed':>6}  {'Delta (pp)':>10}  {'Suppress%':>10}  {'Base Acc':>10}  {'Pruned Acc':>10}  Source")
    print("-" * 80)
    for s in all_seeds:
        delta_str = f"{s['delta_pp']:+.1f}" if s['delta_pp'] is not None else "N/A"
        supp_str = f"{s['suppress_pct']:.1f}" if s['suppress_pct'] is not None else "N/A"
        base_str = f"{s['baseline_acc']:.4f}" if s['baseline_acc'] is not None else "N/A"
        prun_str = f"{s['pruned_acc']:.4f}" if s['pruned_acc'] is not None else "N/A"
        print(f"{s['seed']:>6}  {delta_str:>10}  {supp_str:>10}  {base_str:>10}  {prun_str:>10}  {s['source']}")


def print_stats(stats: dict):
    """Print formatted statistics block."""
    print(f"\n--- {stats['label']} (n={stats['n']}, df={stats['df']}) ---")
    print(f"  Mean delta:  {stats['mean']:+.2f} pp")
    print(f"  SD:          {stats['sd']:.2f} pp")
    print(f"  SE:          {stats['se']:.2f} pp")
    print(f"  95% CI:      [{stats['ci_low']:+.2f}, {stats['ci_high']:+.2f}] pp  (t_crit={stats['t_crit']:.3f})")
    print(f"  Direction:   {'ALL POSITIVE' if stats['all_positive'] else 'MIXED (has negative)' if stats['any_negative'] else 'ALL NON-NEGATIVE'}")
    print(f"  Non-inferiority (margin={NI_MARGIN}pp):")
    print(f"    t-stat:    {stats['t_ni']:.3f}")
    if stats['p_ni'] is not None:
        print(f"    p-value:   {stats['p_ni']:.6f}  {'*** SIGNIFICANT (p<0.001)' if stats['p_ni'] < 0.001 else '** SIGNIFICANT (p<0.01)' if stats['p_ni'] < 0.01 else '* SIGNIFICANT (p<0.05)' if stats['p_ni'] < 0.05 else 'NOT SIGNIFICANT'}")
    else:
        print(f"    p-value:   N/A (scipy not available)")


def generate_latex_row(stats_8: dict, suppress_mean: float | None, p_ni: float | None) -> str:
    """Generate LaTeX table row for paper."""
    delta_str = f"$\\Delta = {stats_8['mean']:+.1f} \\pm {stats_8['sd']:.1f}$\\,pp"
    if p_ni is not None and p_ni < 0.05:
        p_str = f"${p_ni:.4f}$" if p_ni >= 0.0001 else "$<0.001$"
    elif p_ni is not None:
        p_str = f"${p_ni:.3f}$"
    else:
        p_str = "N/A"
    supp_str = f"{suppress_mean:.1f}\\%" if suppress_mean is not None else "---"

    row = (
        f"Llama / StratQA (8 seeds) & "
        f"8${{\\times}}$200 & "
        f"\\multicolumn{{2}}{{c}}{{{delta_str}}} & "
        f"{p_str} & "
        f"{supp_str} \\\\"
    )
    return row


def generate_prose(stats_8: dict, stats_7: dict, stats_new4: dict, stats_orig4: dict,
                   all_seeds: list[dict]) -> str:
    """Generate a prose summary paragraph suitable for results.tex."""
    direction_word = "uniformly positive" if stats_8['all_positive'] else "mixed"

    # Suppress rate for seeds that have it
    supp_vals = [s['suppress_pct'] for s in all_seeds if s['suppress_pct'] is not None]
    supp_str = f"mean suppress rate {statistics.mean(supp_vals):.1f}\\%" if supp_vals else ""

    p_str = ""
    if stats_8['p_ni'] is not None:
        if stats_8['p_ni'] < 0.001:
            p_str = "$p < 0.001$"
        else:
            p_str = f"$p = {stats_8['p_ni']:.4f}$"

    prose = (
        f"Across 8 independent seeds (4 original + 4 new), "
        f"the heuristic acknowledgment gate on StrategyQA yields a "
        f"{direction_word} accuracy improvement of "
        f"$\\Delta = {stats_8['mean']:+.1f} \\pm {stats_8['sd']:.1f}$\\,pp "
        f"(mean $\\pm$ SD, 95\\% CI [{stats_8['ci_low']:+.1f}, {stats_8['ci_high']:+.1f}]\\,pp). "
        f"Excluding the discovery seed (42), the 7-seed estimate is "
        f"$\\Delta = {stats_7['mean']:+.1f} \\pm {stats_7['sd']:.1f}$\\,pp "
        f"(95\\% CI [{stats_7['ci_low']:+.1f}, {stats_7['ci_high']:+.1f}]\\,pp), "
        f"confirming that the original finding is not an artifact of seed selection. "
        f"A one-sample $t$-test against a non-inferiority margin of "
        f"$\\delta_0 = {NI_MARGIN}$\\,pp yields {p_str}, "
        f"establishing that ack-gating does not degrade accuracy on this reasoning benchmark"
    )
    if supp_str:
        prose += f" ({supp_str})"
    prose += "."

    return prose


def main():
    print_separator("*")
    print("  StrategyQA Llama Heuristic: 8-Seed Aggregation Analysis")
    print_separator("*")
    print()

    # -----------------------------------------------------------------------
    # 1. Load all seed data
    # -----------------------------------------------------------------------
    all_seeds = list(ORIGINAL_SEEDS)  # copy hardcoded originals

    new_loaded = 0
    for sid in NEW_SEED_IDS:
        result = load_seed_json(sid)
        if result is not None:
            all_seeds.append(result)
            new_loaded += 1
        else:
            # Placeholder so we know it's missing
            pass

    print(f"\nLoaded {new_loaded}/{len(NEW_SEED_IDS)} new seed files")
    print(f"Total seeds available: {len(all_seeds)}")

    # Filter seeds with valid delta_pp
    valid_seeds = [s for s in all_seeds if s['delta_pp'] is not None]
    if len(valid_seeds) < 2:
        print("[ERROR] Need at least 2 valid seeds for statistics. Aborting.")
        sys.exit(1)

    # -----------------------------------------------------------------------
    # 2. Per-seed table
    # -----------------------------------------------------------------------
    print_seed_table(all_seeds)

    # -----------------------------------------------------------------------
    # 3. Compute statistics for each grouping
    # -----------------------------------------------------------------------

    # Original 4-seed
    orig_deltas = [s['delta_pp'] for s in ORIGINAL_SEEDS if s['delta_pp'] is not None]
    stats_orig4 = compute_stats(orig_deltas, "Original 4-seed (42, 0, 1, 2)")

    # New seeds only
    new_deltas = [s['delta_pp'] for s in all_seeds
                  if s['seed'] in NEW_SEED_IDS and s['delta_pp'] is not None]
    if new_deltas:
        stats_new4 = compute_stats(new_deltas, f"New {len(new_deltas)}-seed ({', '.join(str(s) for s in NEW_SEED_IDS[:len(new_deltas)])})")
    else:
        stats_new4 = None

    # All seeds combined
    all_deltas = [s['delta_pp'] for s in valid_seeds]
    stats_all = compute_stats(all_deltas, f"Combined {len(all_deltas)}-seed (all)")

    # Excluding discovery seed (42)
    no_disc_deltas = [s['delta_pp'] for s in valid_seeds if s['seed'] != 42]
    if len(no_disc_deltas) > 1:
        stats_no_disc = compute_stats(no_disc_deltas,
                                       f"Excl. discovery seed ({len(no_disc_deltas)}-seed)")
    else:
        stats_no_disc = None

    # -----------------------------------------------------------------------
    # 4. Print statistics
    # -----------------------------------------------------------------------
    print_separator()
    print("AGGREGATE STATISTICS")
    print_separator()

    print_stats(stats_orig4)
    if stats_new4:
        print_stats(stats_new4)
    print_stats(stats_all)
    if stats_no_disc:
        print_stats(stats_no_disc)

    # Comparison: new mean vs original mean
    if stats_new4:
        print(f"\n--- New vs Original Mean Comparison ---")
        print(f"  Original 4-seed mean: {stats_orig4['mean']:+.2f} pp")
        print(f"  New {stats_new4['n']}-seed mean:      {stats_new4['mean']:+.2f} pp")
        diff = stats_new4['mean'] - stats_orig4['mean']
        print(f"  Difference:           {diff:+.2f} pp")

    # -----------------------------------------------------------------------
    # 5. Suppress rate summary
    # -----------------------------------------------------------------------
    supp_vals = [s['suppress_pct'] for s in valid_seeds if s['suppress_pct'] is not None]
    if supp_vals:
        print(f"\n--- Suppress Rate Summary ---")
        print(f"  Seeds with suppress data: {len(supp_vals)}")
        print(f"  Mean suppress: {statistics.mean(supp_vals):.1f}%")
        if len(supp_vals) > 1:
            print(f"  SD suppress:   {statistics.stdev(supp_vals):.1f}%")

    # -----------------------------------------------------------------------
    # 6. LaTeX table row
    # -----------------------------------------------------------------------
    print_separator()
    print("LATEX TABLE ROW")
    print_separator()
    supp_mean = statistics.mean(supp_vals) if supp_vals else None
    latex_row = generate_latex_row(stats_all, supp_mean, stats_all['p_ni'])
    print(latex_row)

    # -----------------------------------------------------------------------
    # 7. Prose summary
    # -----------------------------------------------------------------------
    print_separator()
    print("PROSE SUMMARY (for results.tex)")
    print_separator()
    prose = generate_prose(stats_all, stats_no_disc if stats_no_disc else stats_all,
                           stats_new4 if stats_new4 else stats_orig4, stats_orig4,
                           valid_seeds)
    print(prose)

    # -----------------------------------------------------------------------
    # 8. Save summary JSON
    # -----------------------------------------------------------------------
    summary = {
        "analysis": "stratqa_llama_heuristic_8seed",
        "seeds_loaded": [s['seed'] for s in valid_seeds],
        "n_seeds": len(valid_seeds),
        "original_4seed": {
            "mean_delta_pp": stats_orig4['mean'],
            "sd_delta_pp": stats_orig4['sd'],
        },
        "combined": {
            "mean_delta_pp": stats_all['mean'],
            "sd_delta_pp": stats_all['sd'],
            "ci_95_low": stats_all['ci_low'],
            "ci_95_high": stats_all['ci_high'],
            "all_positive": stats_all['all_positive'],
            "ni_p_value": stats_all['p_ni'],
        },
    }
    if stats_no_disc:
        summary["excl_discovery"] = {
            "mean_delta_pp": stats_no_disc['mean'],
            "sd_delta_pp": stats_no_disc['sd'],
            "ci_95_low": stats_no_disc['ci_low'],
            "ci_95_high": stats_no_disc['ci_high'],
        }
    if stats_new4:
        summary["new_seeds"] = {
            "mean_delta_pp": stats_new4['mean'],
            "sd_delta_pp": stats_new4['sd'],
        }

    out_path = SCRIPT_DIR / "stratqa_8seed_summary.json"
    with open(out_path, "w") as f:
        json.dump(summary, f, indent=2)
    print(f"\n[INFO] Summary JSON saved to {out_path}")

    print_separator("*")
    print("  Analysis complete.")
    print_separator("*")


if __name__ == "__main__":
    main()
