"""
Triple-seed bootstrap CI analysis for MMLU dose-response patterns.

Reads MMLU accuracy data from multiple sources (JSON result files + CSV summaries),
computes bootstrap confidence intervals for contamination effects (Δ accuracy),
classifies dose-response patterns, and measures cross-seed pattern stability.

Inputs:
  - results/mmlu_eval/{family}/d{dosage}_s{seed}/mmlu_results.json
  - analysis/results/gsm8k/mmlu_summary.csv (legacy s42 data)
Outputs:
  - analysis/bootstrap_results.txt  (formatted tables)
  - analysis/bootstrap_table.tex    (LaTeX table for paper)

Dependencies: numpy, scipy
"""

import argparse
import csv
import json
import os
import sys
from collections import defaultdict
from itertools import combinations
from pathlib import Path

import numpy as np
from scipy.stats import spearmanr

# ── Constants ──────────────────────────────────────────────────────────────

FAMILIES = ["Phi-4", "Qwen2.5-14B", "Qwen2.5-7B", "Gemma-2-9B", "OLMo-2-7B"]
DOSAGES = ["d000", "d005", "d025", "d050", "d100"]
SEEDS = [42, 123, 0]

DISPLAY_TO_DIR = {
    "Phi-4": "phi4",
    "Qwen2.5-14B": "qwen14b",
    "Qwen2.5-7B": "qwen7b",
    "Gemma-2-9B": "gemma2",
    "OLMo-2-7B": "olmo2",
}
DIR_TO_DISPLAY = {v: k for k, v in DISPLAY_TO_DIR.items()}

N_BOOTSTRAP = 10000
CI_LEVEL = 0.95
RNG_SEED = 42


# ── Data loading ───────────────────────────────────────────────────────────

def load_json_results(results_dir: Path, seeds: list[int]) -> dict:
    """Discover and load MMLU results from JSON files.

    Returns: {(display_name, dosage, seed): accuracy}
    """
    data = {}
    mmlu_eval_dir = results_dir / "mmlu_eval"
    if not mmlu_eval_dir.exists():
        return data

    for family_dir in mmlu_eval_dir.iterdir():
        if not family_dir.is_dir():
            continue
        display = DIR_TO_DISPLAY.get(family_dir.name, family_dir.name)
        for dosage_dir in family_dir.iterdir():
            if not dosage_dir.is_dir():
                continue
            name = dosage_dir.name
            parts = name.split("_")
            if len(parts) != 2 or not parts[1].startswith("s"):
                continue
            dosage = parts[0]
            try:
                seed = int(parts[1][1:])
            except ValueError:
                continue
            if seed not in seeds or dosage not in DOSAGES:
                continue
            json_path = dosage_dir / "mmlu_results.json"
            if not json_path.exists():
                continue
            with open(json_path) as f:
                result = json.load(f)
            data[(display, dosage, seed)] = result["accuracy"]
    return data


def load_csv_summary(results_dir: Path, seeds: list[int]) -> dict:
    """Load MMLU data from legacy CSV summary files.

    Searches for mmlu_summary.csv in common locations.
    Returns: {(display_name, dosage, seed): accuracy}
    """
    data = {}
    candidates = [
        results_dir.parent / "analysis" / "results" / "gsm8k" / "mmlu_summary.csv",
        results_dir / "mmlu_summary.csv",
    ]
    for csv_path in candidates:
        if not csv_path.exists():
            continue
        with open(csv_path) as f:
            reader = csv.DictReader(f)
            for row in reader:
                seed = int(row["seed"])
                if seed not in seeds:
                    continue
                display = row["model_display"]
                dosage = row["dosage"]
                if dosage not in DOSAGES:
                    continue
                data[(display, dosage, seed)] = float(row["accuracy"])
    return data


def discover_data(results_dir: Path, seeds: list[int]) -> dict:
    """Merge data from all sources. Returns {(family, dosage, seed): accuracy}."""
    data = {}
    csv_data = load_csv_summary(results_dir, seeds)
    json_data = load_json_results(results_dir, seeds)
    data.update(csv_data)
    data.update(json_data)  # JSON takes precedence over CSV
    return data


def report_coverage(data: dict, seeds: list[int]):
    """Print data coverage matrix."""
    print("=" * 72)
    print("DATA COVERAGE")
    print("=" * 72)

    total_found = 0
    total_expected = 0

    header = f"{'Family':<16}" + "".join(f"{'s' + str(s):>8}" for s in seeds)
    print(header)
    print("-" * len(header))

    for family in FAMILIES:
        row = f"{family:<16}"
        for seed in seeds:
            found = sum(1 for d in DOSAGES if (family, d, seed) in data)
            total_found += found
            total_expected += len(DOSAGES)
            if found == len(DOSAGES):
                row += f"{'✓ ' + str(found) + '/5':>8}"
            elif found == 0:
                row += f"{'— 0/5':>8}"
            else:
                row += f"{'△ ' + str(found) + '/5':>8}"
        print(row)

    print("-" * len(header))
    print(f"Total: {total_found}/{total_expected} cells found")
    print()
    return total_found


# ── Bootstrap CI ───────────────────────────────────────────────────────────

def bootstrap_mean_ci(values: np.ndarray, n_boot: int = N_BOOTSTRAP,
                      ci: float = CI_LEVEL, rng_seed: int = RNG_SEED) -> tuple:
    """CI for the mean: BCa bootstrap (n>=3), t-distribution (n=2), point estimate (n=1).

    Returns: (mean, ci_low, ci_high, method)
      method: 'boot' | 't' | 'pt'
    """
    from scipy.stats import t as t_dist

    n = len(values)
    mean = np.mean(values)

    if n <= 1:
        return (mean, mean, mean, "pt")

    if n == 2:
        alpha = 1 - ci
        se = np.std(values, ddof=1) / np.sqrt(n)
        t_crit = t_dist.ppf(1 - alpha / 2, df=n - 1)
        return (mean, mean - t_crit * se, mean + t_crit * se, "t")

    rng = np.random.RandomState(rng_seed)
    boot_means = np.array([
        np.mean(rng.choice(values, size=n, replace=True))
        for _ in range(n_boot)
    ])

    # BCa correction
    alpha = 1 - ci

    # Bias correction: z0
    z0 = _norm_ppf(np.mean(boot_means < mean))

    # Acceleration: a (jackknife estimate)
    jackknife_means = np.array([
        np.mean(np.delete(values, i)) for i in range(n)
    ])
    jk_mean = np.mean(jackknife_means)
    num = np.sum((jk_mean - jackknife_means) ** 3)
    denom = 6.0 * (np.sum((jk_mean - jackknife_means) ** 2) ** 1.5)
    a = num / denom if denom != 0 else 0.0

    # Adjusted quantiles
    z_alpha2 = _norm_ppf(alpha / 2)
    z_1alpha2 = _norm_ppf(1 - alpha / 2)

    a1 = _norm_cdf(z0 + (z0 + z_alpha2) / (1 - a * (z0 + z_alpha2)))
    a2 = _norm_cdf(z0 + (z0 + z_1alpha2) / (1 - a * (z0 + z_1alpha2)))

    a1 = np.clip(a1, 0.001, 0.999)
    a2 = np.clip(a2, 0.001, 0.999)

    ci_low = np.percentile(boot_means, 100 * a1)
    ci_high = np.percentile(boot_means, 100 * a2)

    return (mean, ci_low, ci_high, "boot")


def _norm_ppf(p):
    """Normal percent-point function (inverse CDF) using Rational approximation."""
    from scipy.stats import norm
    return norm.ppf(np.clip(p, 1e-10, 1 - 1e-10))


def _norm_cdf(z):
    """Standard normal CDF."""
    from scipy.stats import norm
    return norm.cdf(z)


# ── Pattern classification ─────────────────────────────────────────────────

def classify_pattern(accs: dict) -> str:
    """Classify dose-response pattern from a single seed's accuracy dict.

    Args:
        accs: {dosage: accuracy} for one family/seed, must have d000 and d100.

    Returns: pattern label string.
    """
    if "d000" not in accs or "d100" not in accs:
        return "Incomplete"

    baseline = accs["d000"]
    delta_100 = (accs["d100"] - baseline) * 100  # in percentage points

    deltas = {}
    for d in DOSAGES:
        if d in accs:
            deltas[d] = (accs[d] - baseline) * 100

    # V-recovery: >=2pp dip in middle dosages with >=50% recovery at d100
    mid_deltas = [deltas[d] for d in ["d005", "d025", "d050"] if d in deltas]
    if mid_deltas:
        min_mid = min(mid_deltas)
        if min_mid < -2.0:
            recovery = delta_100 - min_mid
            dip_depth = abs(min_mid)
            if recovery >= 0.5 * dip_depth:
                if delta_100 < 1.0:
                    return "V-recovery"
                else:
                    return "Benefit"

    min_delta = min(deltas.values())

    # Immune
    if abs(delta_100) < 1.0:
        return "Immune"

    # Collapse
    if delta_100 < -3.0:
        return "Collapse"

    # V-recovery: dipped but recovered
    if min_delta < -1.0 and delta_100 > min_delta + 1.0:
        return "V-recovery"

    # Benefit patterns
    if delta_100 > 1.0:
        ordered_dosages = [d for d in DOSAGES if d in accs]
        vals = [accs[d] for d in ordered_dosages]
        # Check monotonicity (loosely: no decrease > 0.5pp)
        monotonic = all(
            vals[i + 1] >= vals[i] - 0.005 for i in range(len(vals) - 1)
        )
        # Check plateau: d050 ≈ d100 (within 1pp)
        if "d050" in accs and abs(accs["d100"] - accs["d050"]) * 100 < 1.0:
            return "Benefit-sat"
        if monotonic:
            return "Benefit"
        return "Benefit-sat"

    # Mild negative not reaching Collapse
    if delta_100 < -1.0:
        # Check if V-recovery shape
        return "Collapse" if min_delta < -3.0 else "V-recovery" if min_delta < -1.0 and delta_100 > min_delta + 1.0 else "Collapse"

    return "Immune"


# ── Spearman ρ ─────────────────────────────────────────────────────────────

def compute_pairwise_spearman(family_data: dict, seeds: list[int]) -> tuple:
    """Compute pairwise Spearman ρ between seeds for a family.

    Args:
        family_data: {(dosage, seed): accuracy}
        seeds: list of seeds to compare

    Returns: (mean_rho, min_rho, max_rho, n_pairs) or (None, None, None, 0)
    """
    seed_curves = {}
    for seed in seeds:
        curve = [family_data.get((d, seed)) for d in DOSAGES]
        if all(v is not None for v in curve):
            seed_curves[seed] = curve

    if len(seed_curves) < 2:
        return (None, None, None, 0)

    rhos = []
    for s1, s2 in combinations(seed_curves.keys(), 2):
        rho, _ = spearmanr(seed_curves[s1], seed_curves[s2])
        rhos.append(rho)

    return (np.mean(rhos), np.min(rhos), np.max(rhos), len(rhos))


# ── Main analysis ──────────────────────────────────────────────────────────

def run_analysis(data: dict, seeds: list[int], output_dir: Path):
    """Run full bootstrap analysis and output results."""

    lines = []

    def out(s=""):
        print(s)
        lines.append(s)

    # ── Per-dosage bootstrap table ──
    out("=" * 90)
    out("BOOTSTRAP CI: ACCURACY BY DOSAGE (mean ± 95% CI across seeds)")
    out("=" * 90)

    header = f"{'Family':<16}{'n':>3}"
    for d in DOSAGES:
        header += f"  {d:>18}"
    out(header)
    out("-" * len(header))

    family_summaries = {}

    for family in FAMILIES:
        available_seeds = [s for s in seeds if (family, "d000", s) in data]
        n_seeds = len(available_seeds)
        if n_seeds == 0:
            continue

        row = f"{family:<16}{n_seeds:>3}"
        family_summaries[family] = {"n_seeds": n_seeds, "seeds": available_seeds}

        for dosage in DOSAGES:
            vals = np.array([data[(family, dosage, s)] for s in available_seeds
                            if (family, dosage, s) in data])
            if len(vals) == 0:
                row += f"  {'—':>18}"
                continue
            mean, lo, hi, method = bootstrap_mean_ci(vals)
            if method == "pt":
                row += f"  {mean * 100:6.2f}pp (pt)      "
            else:
                row += f"  {mean * 100:5.2f} [{lo * 100:5.2f},{hi * 100:5.2f}]({method})"
            family_summaries[family][dosage] = (mean, lo, hi, len(vals))
        out(row)

    out()

    # ── Delta(d100) bootstrap ──
    out("=" * 90)
    out("BOOTSTRAP CI: Δ(d100) = acc(d100) - acc(d000)  [percentage points]")
    out("=" * 90)

    header2 = f"{'Family':<16}{'n':>3}{'Baseline':>10}{'Δ(d100) mean':>14}{'95% CI':>22}{'p(Δ=0)':>10}"
    out(header2)
    out("-" * len(header2))

    delta_results = {}

    for family in FAMILIES:
        info = family_summaries.get(family)
        if not info:
            continue
        available_seeds = info["seeds"]
        n_seeds = info["n_seeds"]

        baselines = np.array([data[(family, "d000", s)] for s in available_seeds
                              if (family, "d000", s) in data])
        d100s = np.array([data[(family, "d100", s)] for s in available_seeds
                          if (family, "d100", s) in data])

        if len(baselines) == 0 or len(d100s) == 0:
            continue

        # Paired deltas where both exist
        paired_seeds = [s for s in available_seeds
                        if (family, "d000", s) in data and (family, "d100", s) in data]
        deltas = np.array([data[(family, "d100", s)] - data[(family, "d000", s)]
                           for s in paired_seeds])

        baseline_mean = np.mean(baselines)
        delta_mean, delta_lo, delta_hi, delta_method = bootstrap_mean_ci(deltas)

        # Rough p-value: fraction of bootstrap samples crossing 0
        if len(deltas) > 1:
            rng = np.random.RandomState(RNG_SEED)
            boot_deltas = np.array([
                np.mean(rng.choice(deltas, size=len(deltas), replace=True))
                for _ in range(N_BOOTSTRAP)
            ])
            p_val = np.mean(boot_deltas * np.sign(-delta_mean) >= 0)
            p_str = f"{p_val:.3f}"
        else:
            p_str = "—"

        ci_str = f"[{delta_lo * 100:+.2f}, {delta_hi * 100:+.2f}]({delta_method})"
        out(f"{family:<16}{len(paired_seeds):>3}{baseline_mean * 100:>9.2f}%"
            f"{delta_mean * 100:>+13.2f}pp{ci_str:>28}{p_str:>10}")

        delta_results[family] = {
            "baseline": baseline_mean,
            "delta_mean": delta_mean,
            "delta_lo": delta_lo,
            "delta_hi": delta_hi,
            "n": len(paired_seeds),
            "method": delta_method,
        }

    out()

    # ── Per-dosage deltas ──
    out("=" * 90)
    out("BOOTSTRAP CI: Δ(d) by dosage [percentage points]")
    out("=" * 90)

    header3 = f"{'Family':<16}"
    for d in DOSAGES[1:]:  # skip d000
        header3 += f"  {'Δ(' + d + ')':>20}"
    out(header3)
    out("-" * len(header3))

    for family in FAMILIES:
        info = family_summaries.get(family)
        if not info:
            continue
        available_seeds = info["seeds"]
        row = f"{family:<16}"
        for dosage in DOSAGES[1:]:
            paired = [s for s in available_seeds
                      if (family, "d000", s) in data and (family, dosage, s) in data]
            if not paired:
                row += f"  {'—':>20}"
                continue
            deltas = np.array([data[(family, dosage, s)] - data[(family, "d000", s)]
                               for s in paired])
            mean, lo, hi, method = bootstrap_mean_ci(deltas)
            if method == "pt":
                row += f"  {mean * 100:+6.2f}pp (pt)       "
            else:
                row += f"  {mean * 100:+5.2f} [{lo * 100:+5.2f},{hi * 100:+5.2f}]({method})"
        out(row)

    out()

    # ── Pattern classification ──
    out("=" * 90)
    out("DOSE-RESPONSE PATTERN CLASSIFICATION (per seed)")
    out("=" * 90)

    header4 = f"{'Family':<16}" + "".join(f"{'s' + str(s):>14}" for s in seeds) + f"{'Consistent?':>14}" + f"{'Direction':>12}" + f"{'Dir-Con':>10}"
    out(header4)
    out("-" * len(header4))

    pattern_results = {}

    for family in FAMILIES:
        row = f"{family:<16}"
        patterns = []
        for seed in seeds:
            accs = {d: data[(family, d, seed)] for d in DOSAGES
                    if (family, d, seed) in data}
            if len(accs) < 2:
                row += f"{'—':>14}"
                continue
            pattern = classify_pattern(accs)
            patterns.append(pattern)
            row += f"{pattern:>14}"

        if patterns:
            consistent = len(set(patterns)) == 1
            row += f"{'Yes' if consistent else 'No':>14}"

            dr = delta_results.get(family)
            if dr:
                mean_delta_pp = dr["delta_mean"] * 100
                if abs(mean_delta_pp) < 1.0:
                    direction = "0"
                elif mean_delta_pp > 0:
                    direction = "+"
                else:
                    direction = "−"
            else:
                direction = "—"

            seed_dirs = []
            for seed in seeds:
                if (family, "d000", seed) in data and (family, "d100", seed) in data:
                    sd = (data[(family, "d100", seed)] - data[(family, "d000", seed)]) * 100
                    if abs(sd) < 1.0:
                        seed_dirs.append("0")
                    elif sd > 0:
                        seed_dirs.append("+")
                    else:
                        seed_dirs.append("−")
            dir_consistent = "✓" if len(set(seed_dirs)) == 1 and len(seed_dirs) > 0 else "✗"

            row += f"{direction:>12}"
            row += f"{dir_consistent:>10}"

            pattern_results[family] = {
                "patterns": patterns,
                "consistent": consistent,
                "majority": max(set(patterns), key=patterns.count),
                "direction": direction,
                "dir_consistent": dir_consistent,
            }
        else:
            row += f"{'—':>14}" + f"{'—':>12}" + f"{'—':>10}"
        out(row)

    out()

    # ── Spearman ρ ──
    out("=" * 90)
    out("CROSS-SEED PATTERN STABILITY (Spearman ρ of dose-response curves)")
    out("=" * 90)

    header5 = f"{'Family':<16}{'n_pairs':>8}{'ρ_mean':>10}{'ρ_min':>10}{'ρ_max':>10}"
    out(header5)
    out("-" * len(header5))

    rho_results = {}

    for family in FAMILIES:
        fam_data = {(d, s): data[(family, d, s)]
                    for d in DOSAGES for s in seeds
                    if (family, d, s) in data}
        mean_rho, min_rho, max_rho, n_pairs = compute_pairwise_spearman(fam_data, seeds)

        if n_pairs == 0:
            out(f"{family:<16}{'—':>8}{'—':>10}{'—':>10}{'—':>10}")
            continue

        out(f"{family:<16}{n_pairs:>8}{mean_rho:>10.3f}{min_rho:>10.3f}{max_rho:>10.3f}")
        rho_results[family] = {"mean": mean_rho, "min": min_rho, "max": max_rho, "n": n_pairs}

    out()

    # ── Save text output ──
    output_dir.mkdir(parents=True, exist_ok=True)
    txt_path = output_dir / "bootstrap_results.txt"
    with open(txt_path, "w") as f:
        f.write("\n".join(lines) + "\n")
    print(f"Results saved to {txt_path}")

    # ── Generate LaTeX table ──
    latex_lines = []
    latex_lines.append(r"\begin{table}[t]")
    latex_lines.append(r"\centering")
    latex_lines.append(r"\caption{Triple-seed bootstrap analysis of MMLU dose-response patterns.}")
    latex_lines.append(r"\label{tab:bootstrap-mmlu}")
    latex_lines.append(r"\small")
    latex_lines.append(r"\begin{tabular}{lccccccc}")
    latex_lines.append(r"\toprule")
    latex_lines.append(r"Family & Baseline (\%) & $\Delta$(d100) & 95\% CI & Pattern & Dir. & Dir-C & $\bar{\rho}$ \\")
    latex_lines.append(r"\midrule")

    for family in FAMILIES:
        dr = delta_results.get(family)
        pr = pattern_results.get(family)
        rr = rho_results.get(family)

        if not dr:
            continue

        baseline_str = f"{dr['baseline'] * 100:.2f}"
        delta_str = f"{dr['delta_mean'] * 100:+.2f}"
        method_suffix = r"$^t$" if dr.get("method") == "t" else ""
        ci_str = f"[{dr['delta_lo'] * 100:+.2f}, {dr['delta_hi'] * 100:+.2f}]{method_suffix}"

        pattern_str = pr["majority"] if pr else "---"
        if pr and not pr["consistent"]:
            pattern_str += r"$^\dagger$"

        rho_str = f"{rr['mean']:.2f}" if rr else "---"

        dir_str = pr.get("direction", "---") if pr else "---"
        dirc_raw = pr.get("dir_consistent", "---") if pr else "---"
        if dirc_raw == "✓":
            dirc_str = r"$\checkmark$"
        elif dirc_raw == "✗":
            dirc_str = r"$\times$"
        else:
            dirc_str = dirc_raw

        latex_lines.append(
            f"{family} & {baseline_str} & {delta_str} & {ci_str} & {pattern_str} & {dir_str} & {dirc_str} & {rho_str} \\\\"
        )

    latex_lines.append(r"\bottomrule")
    latex_lines.append(r"\end{tabular}")
    latex_lines.append(r"\vspace{1mm}")
    latex_lines.append(r"\raggedright\footnotesize")
    latex_lines.append(r"$\Delta$(d100) = acc(d100) $-$ acc(d000) in percentage points. "
                       r"CI via BCa bootstrap (10{,}000 resamples) for $n \geq 3$; "
                       r"$t$-distribution ($\mathrm{df}=1$) for $n=2$, marked $^t$. "
                       r"$\bar{\rho}$: mean pairwise Spearman $\rho$ across seeds. "
                       r"$^\dagger$Pattern inconsistent across seeds. Dir.: direction of mean $\Delta$(d100) ($+$/$-$/0 at 1pp threshold). Dir-C: $\checkmark$ if all seeds agree on direction.")
    latex_lines.append(r"\end{table}")

    tex_path = output_dir / "bootstrap_table.tex"
    with open(tex_path, "w") as f:
        f.write("\n".join(latex_lines) + "\n")
    print(f"LaTeX table saved to {tex_path}")


# ── CLI ────────────────────────────────────────────────────────────────────

def main():
    global N_BOOTSTRAP
    parser = argparse.ArgumentParser(
        description="Triple-seed bootstrap CI analysis for MMLU dose-response patterns."
    )
    parser.add_argument(
        "--results-dir", type=str, default="results/",
        help="Root directory containing MMLU eval results (default: results/)"
    )
    parser.add_argument(
        "--output-dir", type=str, default="analysis/",
        help="Directory for output files (default: analysis/)"
    )
    parser.add_argument(
        "--seeds", type=str, default="42,123,0",
        help="Comma-separated list of seeds to include (default: 42,123,0)"
    )
    parser.add_argument(
        "--dry-run", action="store_true",
        help="Run with available data only, skip missing without error"
    )
    parser.add_argument(
        "--n-bootstrap", type=int, default=N_BOOTSTRAP,
        help=f"Number of bootstrap resamples (default: {N_BOOTSTRAP})"
    )
    args = parser.parse_args()

    N_BOOTSTRAP = args.n_bootstrap

    seeds = [int(s.strip()) for s in args.seeds.split(",")]
    results_dir = Path(args.results_dir).resolve()
    output_dir = Path(args.output_dir).resolve()

    print(f"Results dir: {results_dir}")
    print(f"Output dir:  {output_dir}")
    print(f"Seeds:       {seeds}")
    print(f"Dry-run:     {args.dry_run}")
    print(f"Bootstrap:   {N_BOOTSTRAP} resamples")
    print()

    data = discover_data(results_dir, seeds)
    n_found = report_coverage(data, seeds)

    if n_found == 0:
        print("ERROR: No data found. Check --results-dir path.")
        sys.exit(1)

    if not args.dry_run:
        expected = len(FAMILIES) * len(DOSAGES) * len(seeds)
        missing = expected - n_found
        if missing > 0:
            print(f"WARNING: {missing}/{expected} cells missing. Use --dry-run to proceed anyway.")
            print("Missing entries:")
            for family in FAMILIES:
                for seed in seeds:
                    for dosage in DOSAGES:
                        if (family, dosage, seed) not in data:
                            print(f"  {family} / {dosage} / s{seed}")
            sys.exit(1)

    run_analysis(data, seeds, output_dir)


if __name__ == "__main__":
    main()
