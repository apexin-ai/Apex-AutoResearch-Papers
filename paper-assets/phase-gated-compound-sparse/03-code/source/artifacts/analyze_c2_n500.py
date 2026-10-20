"""
C2 n=500 Analysis: Phase-gated compound sparsity interaction.

Input:  profiling_output_n500_bf16_{ds,qw}_{imp,rand}_s{015,020,025,030}/profiling_results.json
        profiling_output_bf16_{ds,qw}_{imp,rand}_s{015,020,025,030}/profiling_results.json  (n=50 reference)
Output: analysis_output/c2_n500_results.json       — full analysis results
        analysis_output/cohens_d_n500.json          — paired d_z for paper figures
        analysis_output/c2_n500_report.md           — markdown report
        stdout                                      — formatted report

Usage:  python analyze_c2_n500.py [--n50-only]    # --n50-only: dry-run with n=50 data
"""

import json
import argparse
import sys
import os
from pathlib import Path
import numpy as np
from scipy import stats

BASE = Path("/root/autodl-tmp/pacs")

MODELS = {"deepseek": "ds", "qwen": "qw"}
MASKING_TYPES = ["imp", "rand"]
SPARSITY_LABELS = ["s015", "s020", "s025", "s030"]
SPARSITY_KEY_MAP = {"s015": "0.15", "s020": "0.2", "s025": "0.25", "s030": "0.3"}
PHASES = ["high", "mid", "low"]

B_BOOTSTRAP = 10000
SEED = 42


def output_dir_name(model_short, masking, slabel, prefix="n500"):
    if prefix == "n500":
        return f"profiling_output_n500_bf16_{model_short}_{masking}_{slabel}"
    else:
        return f"profiling_output_bf16_{model_short}_{masking}_{slabel}"


def load_profiling(dirpath):
    fpath = Path(dirpath) / "profiling_results.json"
    if not fpath.exists():
        return None
    with open(fpath) as f:
        return json.load(f)


def extract_per_problem_ii(data):
    ppi = data.get("per_problem_ii", {})
    keys = list(ppi.keys())
    if not keys:
        return None
    return ppi[keys[0]]


def compute_phase_diffs(problems, phase_a="low", phase_b="high"):
    """D = ii_{phase_a} - ii_{phase_b} per problem (paired)."""
    diffs = []
    indices = []
    for i, p in enumerate(problems):
        va = p.get(f"ii_{phase_a}")
        vb = p.get(f"ii_{phase_b}")
        if va is not None and vb is not None:
            diffs.append(va - vb)
            indices.append(i)
    return np.array(diffs), indices


def paired_cohens_dz(diffs):
    if len(diffs) < 2:
        return float("nan")
    s = np.std(diffs, ddof=1)
    if s == 0:
        return float("nan")
    return float(np.mean(diffs) / s)


def bootstrap_ci_dz(diffs, B=B_BOOTSTRAP, alpha=0.05, seed=SEED):
    rng = np.random.RandomState(seed)
    n = len(diffs)
    boot = np.empty(B)
    for i in range(B):
        sample = diffs[rng.randint(0, n, size=n)]
        s = sample.std(ddof=1)
        boot[i] = sample.mean() / s if s > 0 else np.nan
    boot = boot[~np.isnan(boot)]
    if len(boot) == 0:
        return float("nan"), float("nan")
    return float(np.percentile(boot, 100 * alpha / 2)), float(np.percentile(boot, 100 * (1 - alpha / 2)))


def bootstrap_ci_median(diffs, B=B_BOOTSTRAP, alpha=0.05, seed=SEED):
    rng = np.random.RandomState(seed)
    n = len(diffs)
    boot = np.array([np.median(diffs[rng.randint(0, n, size=n)]) for _ in range(B)])
    return float(np.percentile(boot, 100 * alpha / 2)), float(np.percentile(boot, 100 * (1 - alpha / 2)))


def bootstrap_ci_mean(diffs, B=B_BOOTSTRAP, alpha=0.05, seed=SEED):
    rng = np.random.RandomState(seed)
    n = len(diffs)
    boot = np.array([np.mean(diffs[rng.randint(0, n, size=n)]) for _ in range(B)])
    return float(np.percentile(boot, 100 * alpha / 2)), float(np.percentile(boot, 100 * (1 - alpha / 2)))


def wilcoxon_signed_rank(diffs):
    nonzero = diffs[diffs != 0]
    if len(nonzero) < 10:
        return float("nan"), float("nan")
    stat, p = stats.wilcoxon(nonzero, alternative="greater")
    return float(stat), float(p)


def interpret_d(d):
    ad = abs(d)
    if ad < 0.2:
        return "negligible"
    elif ad < 0.5:
        return "small"
    elif ad < 0.8:
        return "medium"
    else:
        return "large"


def analyze_condition(problems):
    """Full analysis for one condition's per-problem II data."""
    diffs, valid_idx = compute_phase_diffs(problems, "low", "high")
    n_total = len(problems)
    n_valid = len(diffs)
    n_skipped = n_total - n_valid

    if n_valid < 5:
        return {"error": f"Too few valid problems: {n_valid}", "n_total": n_total}

    d_z = paired_cohens_dz(diffs)
    dz_ci_lo, dz_ci_hi = bootstrap_ci_dz(diffs)
    med = float(np.median(diffs))
    med_ci_lo, med_ci_hi = bootstrap_ci_median(diffs)
    mean_val = float(np.mean(diffs))
    mean_ci_lo, mean_ci_hi = bootstrap_ci_mean(diffs)
    std_val = float(np.std(diffs, ddof=1))
    w_stat, w_p = wilcoxon_signed_rank(diffs)

    # Per-phase aggregate II
    phase_stats = {}
    for ph in PHASES:
        vals = [p[f"ii_{ph}"] for p in problems if p.get(f"ii_{ph}") is not None]
        if vals:
            arr = np.array(vals)
            phase_stats[ph] = {
                "n": len(arr),
                "mean": float(np.mean(arr)),
                "median": float(np.median(arr)),
                "std": float(np.std(arr, ddof=1)),
            }

    # CI-crosses-zero check for median
    median_ci_crosses_zero = (med_ci_lo <= 0 <= med_ci_hi)
    # CI-crosses-zero check for d_z
    dz_ci_crosses_zero = (dz_ci_lo <= 0 <= dz_ci_hi)

    return {
        "n_total": n_total,
        "n_valid": n_valid,
        "n_skipped": n_skipped,
        "phase_gradient": {
            "d_z": round(d_z, 6),
            "d_z_ci": [round(dz_ci_lo, 4), round(dz_ci_hi, 4)],
            "d_z_interpretation": interpret_d(d_z),
            "d_z_ci_crosses_zero": dz_ci_crosses_zero,
        },
        "median_diff": {
            "value": round(med, 6),
            "ci": [round(med_ci_lo, 4), round(med_ci_hi, 4)],
            "ci_crosses_zero": median_ci_crosses_zero,
        },
        "mean_diff": {
            "value": round(mean_val, 6),
            "ci": [round(mean_ci_lo, 4), round(mean_ci_hi, 4)],
            "std": round(std_val, 6),
        },
        "wilcoxon": {
            "statistic": round(w_stat, 2) if not np.isnan(w_stat) else None,
            "p_value": w_p if not np.isnan(w_p) else None,
            "significant_005": w_p < 0.05 if not np.isnan(w_p) else None,
        },
        "phase_stats": phase_stats,
    }


def compare_n50_n500(r50, r500):
    """Compare n=50 and n=500 results."""
    if "error" in r50 or "error" in r500:
        return None
    pg50 = r50["phase_gradient"]
    pg500 = r500["phase_gradient"]
    ci50_width = pg50["d_z_ci"][1] - pg50["d_z_ci"][0]
    ci500_width = pg500["d_z_ci"][1] - pg500["d_z_ci"][0]

    med50 = r50["median_diff"]
    med500 = r500["median_diff"]
    med_ci50_width = med50["ci"][1] - med50["ci"][0]
    med_ci500_width = med500["ci"][1] - med500["ci"][0]

    return {
        "d_z_n50": pg50["d_z"],
        "d_z_n500": pg500["d_z"],
        "d_z_change": round(pg500["d_z"] - pg50["d_z"], 4),
        "ci_width_n50": round(ci50_width, 4),
        "ci_width_n500": round(ci500_width, 4),
        "ci_width_reduction_pct": round((1 - ci500_width / ci50_width) * 100, 1) if ci50_width > 0 else None,
        "median_ci_width_n50": round(med_ci50_width, 4),
        "median_ci_width_n500": round(med_ci500_width, 4),
        "median_ci_reduction_pct": round((1 - med_ci500_width / med_ci50_width) * 100, 1) if med_ci50_width > 0 else None,
    }


def format_report(all_results, comparisons, preregistration):
    """Generate markdown report."""
    lines = []
    lines.append("# C2 n=500 Analysis Report")
    lines.append("")

    # Pre-registration verdict
    lines.append("## Pre-registration Verdict")
    lines.append("")
    pr = preregistration
    if pr:
        qw_s015 = pr.get("qwen_s015", {})
        lines.append(f"- Qwen s015 median diff CI: [{qw_s015.get('median_ci_lo', '?')}, {qw_s015.get('median_ci_hi', '?')}]")
        lines.append(f"- CI crosses zero: **{qw_s015.get('crosses_zero', '?')}**")
        if qw_s015.get("crosses_zero"):
            lines.append(f"- → Narrative: compound effect emerges above threshold sparsity (~s020)")
        else:
            lines.append(f"- → Narrative: compound effect present at all tested sparsity levels")
        lines.append(f"- Qwen s015 d_z = {qw_s015.get('d_z', '?')} [{qw_s015.get('dz_ci_lo', '?')}, {qw_s015.get('dz_ci_hi', '?')}]")
        lines.append(f"- Wilcoxon p = {qw_s015.get('wilcoxon_p', '?')}")
    lines.append("")

    # Table 1: Phase gradient (d_z) — importance
    for model_name, model_short in MODELS.items():
        lines.append(f"## {model_name.title()} — Importance: Phase Gradient (ii_low - ii_high)")
        lines.append("")
        lines.append("| Sparsity | n | d_z | 95% CI | Interpretation | Median Δ | Median CI | Wilcoxon p | Sig? |")
        lines.append("|----------|---|-----|--------|----------------|----------|-----------|------------|------|")
        for sl in SPARSITY_LABELS:
            key = f"{model_short}_imp_{sl}"
            r = all_results.get(key)
            if r and "error" not in r:
                pg = r["phase_gradient"]
                md = r["median_diff"]
                w = r["wilcoxon"]
                p_str = f"{w['p_value']:.2e}" if w["p_value"] is not None else "N/A"
                sig = "YES" if w.get("significant_005") else "no"
                lines.append(
                    f"| {sl} | {r['n_valid']} | {pg['d_z']:.4f} | [{pg['d_z_ci'][0]:.4f}, {pg['d_z_ci'][1]:.4f}] | "
                    f"{pg['d_z_interpretation']} | {md['value']:.4f} | [{md['ci'][0]:.4f}, {md['ci'][1]:.4f}] | {p_str} | {sig} |"
                )
            else:
                lines.append(f"| {sl} | — | — | — | — | — | — | — | — |")
        lines.append("")

    # Table 2: Phase gradient — random
    for model_name, model_short in MODELS.items():
        lines.append(f"## {model_name.title()} — Random: Phase Gradient (ii_low - ii_high)")
        lines.append("")
        lines.append("| Sparsity | n | d_z | 95% CI | Interpretation | Median Δ | Median CI | Wilcoxon p | Sig? |")
        lines.append("|----------|---|-----|--------|----------------|----------|-----------|------------|------|")
        for sl in SPARSITY_LABELS:
            key = f"{model_short}_rand_{sl}"
            r = all_results.get(key)
            if r and "error" not in r:
                pg = r["phase_gradient"]
                md = r["median_diff"]
                w = r["wilcoxon"]
                p_str = f"{w['p_value']:.2e}" if w["p_value"] is not None else "N/A"
                sig = "YES" if w.get("significant_005") else "no"
                lines.append(
                    f"| {sl} | {r['n_valid']} | {pg['d_z']:.4f} | [{pg['d_z_ci'][0]:.4f}, {pg['d_z_ci'][1]:.4f}] | "
                    f"{pg['d_z_interpretation']} | {md['value']:.4f} | [{md['ci'][0]:.4f}, {md['ci'][1]:.4f}] | {p_str} | {sig} |"
                )
            else:
                lines.append(f"| {sl} | — | — | — | — | — | — | — | — |")
        lines.append("")

    # Table 3: Compound interaction severity (II_low) across sparsity — importance vs random
    for model_name, model_short in MODELS.items():
        lines.append(f"## {model_name.title()} — Compound Interaction Severity (II_low median)")
        lines.append("")
        lines.append("| Sparsity | Imp median | Imp mean | Rand median | Rand mean | Imp/Rand ratio |")
        lines.append("|----------|-----------|---------|------------|----------|----------------|")
        for sl in SPARSITY_LABELS:
            imp_key = f"{model_short}_imp_{sl}"
            rnd_key = f"{model_short}_rand_{sl}"
            ri = all_results.get(imp_key, {})
            rr = all_results.get(rnd_key, {})
            ps_i = ri.get("phase_stats", {}).get("low", {})
            ps_r = rr.get("phase_stats", {}).get("low", {})
            imp_med = ps_i.get("median", float("nan"))
            imp_mean = ps_i.get("mean", float("nan"))
            rnd_med = ps_r.get("median", float("nan"))
            rnd_mean = ps_r.get("mean", float("nan"))
            ratio = imp_med / rnd_med if rnd_med != 0 and not np.isnan(rnd_med) else float("nan")
            lines.append(
                f"| {sl} | {imp_med:.4f} | {imp_mean:.4f} | {rnd_med:.4f} | {rnd_mean:.4f} | {ratio:.3f} |"
            )
        lines.append("")

    # Table 4: Monotonicity check
    lines.append("## Monotonicity Check: Importance d_z vs Sparsity")
    lines.append("")
    lines.append("| Model | s015 d_z | s020 d_z | s025 d_z | s030 d_z | Monotonic? |")
    lines.append("|-------|----------|----------|----------|----------|------------|")
    for model_name, model_short in MODELS.items():
        ds = []
        for sl in SPARSITY_LABELS:
            key = f"{model_short}_imp_{sl}"
            r = all_results.get(key, {})
            d_z = r.get("phase_gradient", {}).get("d_z", float("nan"))
            ds.append(d_z)
        monotonic = all(ds[i] <= ds[i + 1] for i in range(len(ds) - 1) if not np.isnan(ds[i]) and not np.isnan(ds[i + 1]))
        d_strs = [f"{d:.4f}" for d in ds]
        lines.append(f"| {model_name} | {' | '.join(d_strs)} | {'YES' if monotonic else 'NO'} |")
    lines.append("")

    # Table 5: n=50 vs n=500 comparison
    if comparisons:
        lines.append("## Statistical Power: n=50 vs n=500")
        lines.append("")
        lines.append("| Condition | d_z (n=50) | d_z (n=500) | Δd_z | CI width n=50 | CI width n=500 | CI reduction |")
        lines.append("|-----------|-----------|------------|------|--------------|---------------|--------------|")
        for key, comp in sorted(comparisons.items()):
            if comp is None:
                continue
            lines.append(
                f"| {key} | {comp['d_z_n50']:.4f} | {comp['d_z_n500']:.4f} | "
                f"{comp['d_z_change']:+.4f} | {comp['ci_width_n50']:.4f} | "
                f"{comp['ci_width_n500']:.4f} | {comp['ci_width_reduction_pct']}% |"
            )
        lines.append("")

    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description="C2 n=500 analysis")
    parser.add_argument("--n50-only", action="store_true", help="Dry-run: analyze n=50 data only")
    args = parser.parse_args()

    prefix = "n50" if args.n50_only else "n500"
    print(f"=== C2 Analysis ({'n=50 dry-run' if args.n50_only else 'n=500'}) ===\n")

    # Load all conditions
    all_results = {}
    missing = []

    for model_name, model_short in MODELS.items():
        for masking in MASKING_TYPES:
            for sl in SPARSITY_LABELS:
                key = f"{model_short}_{masking}_{sl}"
                dirname = output_dir_name(model_short, masking, sl, prefix=prefix)
                dirpath = BASE / dirname

                data = load_profiling(dirpath)
                if data is None:
                    missing.append(key)
                    print(f"  MISSING: {dirname}")
                    continue

                problems = extract_per_problem_ii(data)
                if problems is None:
                    missing.append(key)
                    print(f"  NO per_problem_ii: {dirname}")
                    continue

                result = analyze_condition(problems)
                result["dirname"] = dirname
                result["model"] = model_name
                result["masking"] = masking
                result["sparsity"] = sl
                all_results[key] = result

                pg = result.get("phase_gradient", {})
                print(f"  {key}: n={result.get('n_valid','?')}, d_z={pg.get('d_z','?')}, "
                      f"CI=[{pg.get('d_z_ci',['?','?'])[0]}, {pg.get('d_z_ci',['?','?'])[1]}], "
                      f"{pg.get('d_z_interpretation','?')}")

    if missing:
        print(f"\nWARNING: {len(missing)} conditions missing: {missing}")
    print()

    # n=50 vs n=500 comparison (only if running n=500)
    comparisons = {}
    if not args.n50_only:
        print("=== n=50 vs n=500 Comparison ===\n")
        for model_name, model_short in MODELS.items():
            for masking in MASKING_TYPES:
                for sl in SPARSITY_LABELS:
                    key = f"{model_short}_{masking}_{sl}"
                    if key not in all_results:
                        continue

                    dirname_50 = output_dir_name(model_short, masking, sl, prefix="n50")
                    data_50 = load_profiling(BASE / dirname_50)
                    if data_50 is None:
                        continue
                    problems_50 = extract_per_problem_ii(data_50)
                    if problems_50 is None:
                        continue

                    r50 = analyze_condition(problems_50)
                    comp = compare_n50_n500(r50, all_results[key])
                    if comp:
                        comparisons[key] = comp
                        print(f"  {key}: CI width {comp['ci_width_n50']:.4f} → {comp['ci_width_n500']:.4f} "
                              f"(↓{comp['ci_width_reduction_pct']}%)")

        print()

    # Pre-registration check: Qwen s015
    preregistration = {}
    qw_s015 = all_results.get("qw_imp_s015")
    if qw_s015 and "error" not in qw_s015:
        pg = qw_s015["phase_gradient"]
        md = qw_s015["median_diff"]
        w = qw_s015["wilcoxon"]
        preregistration["qwen_s015"] = {
            "d_z": pg["d_z"],
            "dz_ci_lo": pg["d_z_ci"][0],
            "dz_ci_hi": pg["d_z_ci"][1],
            "median_diff": md["value"],
            "median_ci_lo": md["ci"][0],
            "median_ci_hi": md["ci"][1],
            "crosses_zero": md["ci_crosses_zero"],
            "wilcoxon_p": w["p_value"],
            "verdict": "threshold_s020" if md["ci_crosses_zero"] else "effect_at_s015",
        }
        print("=== Pre-registration Verdict ===")
        print(f"  Qwen s015 median diff = {md['value']:.6f}")
        print(f"  Median CI = [{md['ci'][0]:.4f}, {md['ci'][1]:.4f}]")
        print(f"  CI crosses zero: {md['ci_crosses_zero']}")
        if md["ci_crosses_zero"]:
            print("  → VERDICT: Change narrative to threshold ~s020")
        else:
            print("  → VERDICT: Compound effect confirmed at s015")
        print()

    # Generate markdown report
    report = format_report(all_results, comparisons, preregistration)
    print(report)

    # Build Cohen's d JSON for paper figures
    cohens_d_output = {
        "method": "paired d_z = mean(D)/SD(D), D = ii_low - ii_high, per-problem pairing",
        "n_bootstrap": B_BOOTSTRAP,
        "seed": SEED,
    }
    for model_name, model_short in MODELS.items():
        model_data = {}
        for sl in SPARSITY_LABELS:
            key = f"{model_short}_imp_{sl}"
            r = all_results.get(key, {})
            pg = r.get("phase_gradient", {})
            if pg:
                model_data[sl] = {
                    "d_z": pg.get("d_z"),
                    "ci_low": pg.get("d_z_ci", [None, None])[0],
                    "ci_high": pg.get("d_z_ci", [None, None])[1],
                    "n": r.get("n_valid"),
                    "interpretation": pg.get("d_z_interpretation"),
                    "mean_diff": r.get("mean_diff", {}).get("value"),
                    "std_diff": r.get("mean_diff", {}).get("std"),
                }
        cohens_d_output[model_name] = model_data

    # Save outputs
    out_dir = BASE / "analysis_output"
    out_dir.mkdir(exist_ok=True)

    suffix = "_dryrun" if args.n50_only else ""

    results_path = out_dir / f"c2_n500_results{suffix}.json"
    with open(results_path, "w") as f:
        json.dump({
            "conditions": {k: _sanitize(v) for k, v in all_results.items()},
            "comparisons": comparisons,
            "preregistration": preregistration,
            "metadata": {
                "data_source": "n=50" if args.n50_only else "n=500",
                "n_bootstrap": B_BOOTSTRAP,
                "seed": SEED,
                "missing_conditions": missing,
            },
        }, f, indent=2)
    print(f"\nSaved results: {results_path}")

    cohens_path = out_dir / f"cohens_d_n500{suffix}.json"
    with open(cohens_path, "w") as f:
        json.dump(cohens_d_output, f, indent=2)
    print(f"Saved Cohen's d: {cohens_path}")

    report_path = out_dir / f"c2_n500_report{suffix}.md"
    with open(report_path, "w") as f:
        f.write(report)
    print(f"Saved report: {report_path}")


def _sanitize(obj):
    """Convert numpy types to Python types for JSON serialization."""
    if isinstance(obj, dict):
        return {k: _sanitize(v) for k, v in obj.items()}
    elif isinstance(obj, list):
        return [_sanitize(v) for v in obj]
    elif isinstance(obj, (np.integer,)):
        return int(obj)
    elif isinstance(obj, (np.floating,)):
        return float(obj)
    elif isinstance(obj, np.ndarray):
        return obj.tolist()
    elif isinstance(obj, (np.bool_,)):
        return bool(obj)
    return obj


if __name__ == "__main__":
    main()
