#!/usr/bin/env python3
"""
1.5B Pooled IRT Calibration (4PL+gamma) — per-benchmark independent fits.
Pools s42 + s123 seeds for all 4 dosages (8 respondent models).
Focus: coverage collapse, PPP, discrimination, gamma direction.
"""

import json
import logging
import os
import sys
import time
from pathlib import Path
from datetime import datetime

import numpy as np

sys.path.insert(0, "/root/contamcal-irt-calibration/exp006")
from run_irt_calibration import (
    load_eval_results,
    prepare_stan_data,
    fit_stan_model,
    check_convergence,
    posterior_predictive_check,
    extract_results,
    _summarize_vector,
    STAN_MODELS,
)

log = logging.getLogger(__name__)

BENCHMARKS = ["mmlu", "gsm8k", "arc_challenge", "humaneval"]
MODEL_TYPE = "4pl_gamma"
STAN_FILE = STAN_MODELS[MODEL_TYPE]
EVAL_DIR = "/root/autodl-tmp/exp001/eval_results"
OUTPUT_DIR = Path("/root/autodl-tmp/exp001/artifacts/pooled_irt_15B")
MAX_ITEMS = 2000

WARMUP = 2000
SAMPLES = 2000
CHAINS = 4
ADAPT_DELTA = 0.95
MAX_TREEDEPTH = 12


def build_oracle_exposure(dosages, n_items):
    max_d = dosages.max() if dosages.max() > 0 else 1.0
    fracs = dosages / max_d
    return np.outer(fracs, np.ones(n_items))


def compute_coverage(calibrated_scores, raw_accuracy):
    """Compute 90% CI coverage: fraction of models where raw_acc in [q05, q95]."""
    means = np.array(calibrated_scores["mean"])
    sds = np.array(calibrated_scores["sd"])
    q05 = np.array(calibrated_scores.get("q05", means - 1.645 * sds))
    q95 = np.array(calibrated_scores.get("q95", means + 1.645 * sds))
    q025 = np.array(calibrated_scores["q025"])
    q975 = np.array(calibrated_scores["q975"])
    raw = np.array(raw_accuracy)

    cov_90 = np.mean((raw >= q05) & (raw <= q95))
    cov_95 = np.mean((raw >= q025) & (raw <= q975))

    per_model = []
    for i in range(len(raw)):
        per_model.append({
            "raw_acc": round(float(raw[i]), 4),
            "cal_mean": round(float(means[i]), 4),
            "cal_sd": round(float(sds[i]), 4),
            "in_90ci": bool((raw[i] >= q05[i]) and (raw[i] <= q95[i])),
            "in_95ci": bool((raw[i] >= q025[i]) and (raw[i] <= q975[i])),
            "residual": round(float(raw[i] - means[i]), 4),
        })
    return {
        "coverage_90": round(float(cov_90) * 100, 1),
        "coverage_95": round(float(cov_95) * 100, 1),
        "per_model": per_model,
    }


def analyze_discrimination(a_params, models, dosages):
    """Analyze discrimination by dosage group."""
    a_means = np.array(a_params["mean"])
    groups = {}
    for i, m in enumerate(models):
        d = m["dosage"]
        key = f"d{d:03d}"
        if key not in groups:
            groups[key] = []
        groups[key].append(i)

    result = {
        "overall_mean": round(float(a_means.mean()), 4),
        "overall_std": round(float(a_means.std()), 4),
        "overall_median": round(float(np.median(a_means)), 4),
        "n_items": len(a_means),
        "low_disc_frac": round(float(np.mean(a_means < 0.5)), 4),
    }
    return result


def run_single_benchmark(bench, data, output_dir):
    """Run 4PL+gamma IRT fit for a single benchmark."""
    if bench not in data["benchmarks"]:
        log.warning("Benchmark %s not found, skipping", bench)
        return None

    bd = data["benchmarks"][bench]
    y = bd["responses"]
    valid = bd["valid_mask"]
    dosages = data["dosages"]

    if not valid.all():
        keep = valid.astype(bool)
        y = y[keep]
        dosages = dosages[keep]
        models = [m for m, k in zip(data["models"], keep) if k]
    else:
        models = data["models"]

    n_models, n_items_raw = y.shape
    n_items = min(n_items_raw, MAX_ITEMS)
    if n_items < n_items_raw:
        np.random.seed(42)
        idx = np.sort(np.random.choice(n_items_raw, n_items, replace=False))
        y = y[:, idx]

    exposure = build_oracle_exposure(dosages, n_items)
    stan_data = prepare_stan_data(y, exposure, MODEL_TYPE)

    class Args:
        chains = CHAINS
        warmup = WARMUP
        samples = SAMPLES
        adapt_delta = ADAPT_DELTA
        max_treedepth = MAX_TREEDEPTH
        seed = 42
        parallel_chains = 4

    args = Args()
    log.info("=== %s: %d models x %d items (original: %d) ===",
             bench, n_models, n_items, n_items_raw)
    log.info("Dosages: %s", dosages.tolist())
    log.info("Models: %s", [m["dirname"] for m in models])

    fit, elapsed = fit_stan_model(
        STAN_FILE, stan_data,
        chains=args.chains, iter_warmup=args.warmup,
        iter_sampling=args.samples, adapt_delta=args.adapt_delta,
        max_treedepth=args.max_treedepth, seed=args.seed,
        parallel_chains=args.parallel_chains,
    )

    diagnostics = check_convergence(fit)
    ppc = posterior_predictive_check(fit, y)
    results = extract_results(fit, y, MODEL_TYPE)

    # Coverage analysis
    cal_draws = fit.stan_variable("calibrated_score")
    cal_summary = _summarize_vector(cal_draws)
    # Add q05/q95 for 90% CI
    cal_summary["q05"] = np.round(np.percentile(cal_draws, 5, axis=0), 4).tolist()
    cal_summary["q95"] = np.round(np.percentile(cal_draws, 95, axis=0), 4).tolist()
    raw_acc = y.mean(axis=1).tolist()
    coverage = compute_coverage(cal_summary, raw_acc)

    # Discrimination analysis
    disc = analyze_discrimination(results["a"], models, dosages)

    # Gamma analysis
    gamma = results.get("gamma", {})

    bench_result = {
        "benchmark": bench,
        "model_type": MODEL_TYPE,
        "n_models": int(n_models),
        "n_items": int(n_items),
        "original_n_items": int(n_items_raw),
        "subsampled": n_items < n_items_raw,
        "models": [{"dirname": m["dirname"], "dosage": m["dosage"], "seed": m["seed"]}
                   for m in models],
        "dosages": dosages.tolist(),
        "fit_time_sec": round(elapsed, 1),
        "mcmc_config": {
            "warmup": WARMUP, "samples": SAMPLES,
            "chains": CHAINS, "adapt_delta": ADAPT_DELTA,
        },
        "diagnostics": diagnostics,
        "posterior_predictive": ppc,
        "gamma": gamma,
        "calibrated_scores": cal_summary,
        "raw_accuracy": raw_acc,
        "coverage": coverage,
        "discrimination": disc,
    }

    bench_dir = output_dir / bench
    bench_dir.mkdir(parents=True, exist_ok=True)
    with open(bench_dir / "irt_4pl_results.json", "w") as f:
        json.dump(bench_result, f, indent=2, default=str)

    # Save item params as CSV
    import csv
    with open(bench_dir / "item_params.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["item_idx", "a_mean", "a_sd", "b_mean", "b_sd",
                         "c_mean", "c_sd", "d_mean", "d_sd"])
        for j in range(n_items):
            writer.writerow([
                j,
                results["a"]["mean"][j], results["a"]["sd"][j],
                results["b"]["mean"][j], results["b"]["sd"][j],
                results["c"]["mean"][j], results["c"]["sd"][j],
                results["d"]["mean"][j], results["d"]["sd"][j],
            ])

    return bench_result


def generate_summary(all_results, output_dir):
    """Generate markdown summary report."""
    lines = [
        f"# 1.5B Pooled IRT Calibration (4PL+γ) — {datetime.now().strftime('%Y-%m-%d %H:%M')}",
        "",
        "## Configuration",
        f"- Model: {MODEL_TYPE}",
        f"- MCMC: {CHAINS} chains × {WARMUP} warmup + {SAMPLES} samples",
        f"- Adapt delta: {ADAPT_DELTA}",
        f"- Max items per benchmark: {MAX_ITEMS}",
        f"- Scale: 1.5B only, seeds s42+s123 pooled",
        "",
        "## Per-Benchmark Results",
        "",
    ]

    for bench in BENCHMARKS:
        if bench not in all_results:
            lines.append(f"### {bench}: SKIPPED\n")
            continue
        r = all_results[bench]
        d = r["diagnostics"]
        g = r.get("gamma", {})
        ppc = r["posterior_predictive"]
        cov = r["coverage"]
        disc = r["discrimination"]

        diag_status = "PASS" if d["all_ok"] else "FAIL"
        lines.extend([
            f"### {bench}",
            f"- **N**: {r['n_models']} models × {r['n_items']} items (of {r['original_n_items']})",
            f"- **Fit time**: {r['fit_time_sec']:.0f}s",
            f"- **Gamma**: mean={g.get('mean', 'N/A')}, CI95=[{g.get('q025', 'N/A')}, {g.get('q975', 'N/A')}], "
            f"excludes_zero={g.get('ci_excludes_zero', 'N/A')}",
            f"- **Diagnostics [{diag_status}]**: Rhat={d.get('max_rhat', 'N/A')}, "
            f"ESS={d.get('min_ess', 'N/A')}, divergences={d.get('divergent_count', 'N/A')} "
            f"({d.get('divergent_pct', 0):.2f}%)",
            f"- **PPP**: {ppc.get('overall_ppp', 'N/A')} "
            f"(obs={ppc.get('obs_mean_acc', 'N/A')}, pred={ppc.get('pred_mean_acc', 'N/A')})",
            f"- **Coverage**: C90={cov['coverage_90']}%, C95={cov['coverage_95']}%",
            f"- **Discrimination**: mean_a={disc['overall_mean']}, "
            f"median_a={disc['overall_median']}, low_disc(<0.5)={disc['low_disc_frac']*100:.1f}%",
            "",
            "| Model | Dosage | Raw Acc | Cal Mean | Cal SD | In 90%CI | Residual |",
            "|-------|--------|---------|----------|--------|----------|----------|",
        ])
        for i, m in enumerate(r["models"]):
            cm = cov["per_model"][i]
            lines.append(
                f"| {m['dirname']} | {m['dosage']} | {cm['raw_acc']:.4f} | "
                f"{cm['cal_mean']:.4f} | {cm['cal_sd']:.4f} | "
                f"{'YES' if cm['in_90ci'] else '**NO**'} | {cm['residual']:+.4f} |"
            )
        lines.append("")

    # Cross-benchmark comparison
    lines.extend(["## Cross-Benchmark Summary", "",
                   "| Benchmark | Gamma | CI95 | Excl.Zero | Coverage90 | PPP | Rhat | ESS | Divg |",
                   "|-----------|-------|------|-----------|------------|-----|------|-----|------|"])
    for bench in BENCHMARKS:
        if bench not in all_results:
            continue
        r = all_results[bench]
        g = r.get("gamma", {})
        d = r["diagnostics"]
        ppc = r["posterior_predictive"]
        cov = r["coverage"]
        lines.append(
            f"| {bench} | {g.get('mean', 'N/A'):.4f} | "
            f"[{g.get('q025', 'N/A'):.4f}, {g.get('q975', 'N/A'):.4f}] | "
            f"{'YES' if g.get('ci_excludes_zero') else 'no'} | "
            f"{cov['coverage_90']:.0f}% | {ppc.get('overall_ppp', 'N/A')} | "
            f"{d.get('max_rhat', 'N/A'):.4f} | {d.get('min_ess', 0):.0f} | "
            f"{d.get('divergent_count', 0)} |"
        )
    lines.append("")

    report = "\n".join(lines)
    with open(output_dir / "summary_report.md", "w") as f:
        f.write(report)
    return report


def main():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(message)s",
    )

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    log.info("Loading 1.5B eval results from %s", EVAL_DIR)
    data = load_eval_results(
        EVAL_DIR,
        benchmarks=BENCHMARKS,
        skip_para=True,
        model_scale="1.5B",
        aligned_only=True,
    )
    log.info("Loaded %d models: %s", len(data["models"]),
             [m["dirname"] for m in data["models"]])
    log.info("Dosages: %s", data["dosages"].tolist())

    all_results = {}
    for bench in BENCHMARKS:
        log.info("=" * 60)
        log.info("Fitting %s...", bench)
        result = run_single_benchmark(bench, data, OUTPUT_DIR)
        if result:
            all_results[bench] = result
            g = result.get("gamma", {})
            d = result["diagnostics"]
            cov = result["coverage"]
            log.info("[%s] gamma=%.4f [%.4f, %.4f], coverage90=%.0f%%, rhat=%.4f, ESS=%.0f",
                     bench, g.get("mean", 0), g.get("q025", 0), g.get("q975", 0),
                     cov["coverage_90"], d.get("max_rhat", 0), d.get("min_ess", 0))

    # Save combined results
    with open(OUTPUT_DIR / "all_benchmarks_results.json", "w") as f:
        json.dump(all_results, f, indent=2, default=str)

    report = generate_summary(all_results, OUTPUT_DIR)
    print("\n" + report)
    log.info("All results saved to %s", OUTPUT_DIR)


if __name__ == "__main__":
    main()
