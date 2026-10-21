#!/usr/bin/env python3
"""MMLU domain-stratified gamma analysis: Qwen 1.5B×8 + Qwen 3B×8. J=16 models."""

import argparse
import json
import logging
import os
import re
import sys
import time
from pathlib import Path

import numpy as np

sys.path.insert(0, "/root/contamcal-irt-calibration/exp006")
from run_irt_calibration import (
    load_pooled_eval_results,
    prepare_stan_data,
    fit_stan_model,
    check_convergence,
    posterior_predictive_check,
    extract_results,
    STAN_MODELS,
)

log = logging.getLogger(__name__)

DOMAIN_MAP = {
    "STEM_Math": [
        "abstract_algebra", "college_mathematics", "elementary_mathematics",
        "high_school_mathematics", "high_school_statistics", "formal_logic",
    ],
    "STEM_Science": [
        "astronomy", "college_biology", "college_chemistry", "college_physics",
        "conceptual_physics", "high_school_biology", "high_school_chemistry",
        "high_school_physics",
    ],
    "STEM_CS_Eng": [
        "college_computer_science", "computer_security", "electrical_engineering",
        "high_school_computer_science", "machine_learning",
    ],
    "Medical": [
        "anatomy", "clinical_knowledge", "college_medicine", "human_aging",
        "medical_genetics", "nutrition", "professional_medicine", "virology",
    ],
    "Humanities": [
        "high_school_european_history", "high_school_us_history",
        "high_school_world_history", "logical_fallacies", "moral_disputes",
        "moral_scenarios", "philosophy", "prehistory", "world_religions",
    ],
    "Social_Sciences": [
        "econometrics", "high_school_geography",
        "high_school_government_and_politics", "high_school_macroeconomics",
        "high_school_microeconomics", "high_school_psychology",
        "human_sexuality", "professional_psychology", "public_relations",
        "security_studies", "sociology", "us_foreign_policy",
    ],
    "Business_Law": [
        "business_ethics", "international_law", "jurisprudence", "management",
        "marketing", "professional_accounting", "professional_law",
    ],
    "Other": [
        "global_facts", "miscellaneous",
    ],
}

MODEL_WHITELIST = {
    # Qwen 1.5B (8)
    "Qwen2.5-1.5B_d000_s123",
    "Qwen2.5-1.5B_d000_s42",
    "Qwen2.5-1.5B_d005_s123",
    "Qwen2.5-1.5B_d005_s42",
    "Qwen2.5-1.5B_d025_s123",
    "Qwen2.5-1.5B_d025_s42",
    "Qwen2.5-1.5B_d100_s123",
    "Qwen2.5-1.5B_d100_s42",
    # Qwen 3B (8)
    "Qwen2.5-3B_d000_s123",
    "Qwen2.5-3B_d000_s42_a32",
    "Qwen2.5-3B_d005_s123",
    "Qwen2.5-3B_d005_s42_a32",
    "Qwen2.5-3B_d025_s123",
    "Qwen2.5-3B_d025_v3_s42",
    "Qwen2.5-3B_d100_a32_s123",
    "Qwen2.5-3B_d100_a32_s42",
}

# Eval dir names (after strip_aligned) that differ from RRF keys
DIR_TO_RRF_KEY = {
    "Qwen2.5-3B_d000_s42_a32": "Qwen2.5-3B_d000_a32_s42",
    "Qwen2.5-3B_d005_s42_a32": "Qwen2.5-3B_d005_a32_s42",
}

EVAL_DIR = "/root/autodl-tmp/exp001/eval_results"
MMLU_ARROW = "/root/autodl-tmp/.hf_cache/cais___mmlu/all/0.0.0/c30699e8356da336a370243923dbaf21066bb9fe/mmlu-test.arrow"
RRF_PATH = "/root/autodl-tmp/exp003/rrf_all_scales/exposure_scores.json"
OUTPUT_DIR = "/root/autodl-tmp/exp006/mmlu_domain_irt_j16_qwen"
MODEL_TYPE = "2pl_gamma"
STAN_FILE = STAN_MODELS[MODEL_TYPE]
MAX_ITEMS = 2000


def strip_aligned(dirname):
    return re.sub(r'(_para)?(_aligned)?$', '', dirname)


def build_subject_index_map(arrow_path):
    import pyarrow as pa
    reader = pa.ipc.open_stream(arrow_path)
    table = reader.read_all()
    return table.column("subject").to_pylist()


def build_domain_col_indices(subject_list, n_items):
    subj_to_domain = {}
    for domain, subjects in DOMAIN_MAP.items():
        for s in subjects:
            subj_to_domain[s] = domain
    domain_indices = {d: [] for d in DOMAIN_MAP}
    for i in range(min(len(subject_list), n_items)):
        domain = subj_to_domain.get(subject_list[i])
        if domain:
            domain_indices[domain].append(i)
    return domain_indices


def fit_domain(domain_name, responses, exposure, args_dict, output_dir):
    n_models, n_items = responses.shape
    original_n_items = n_items
    subsampled = False

    if n_items > MAX_ITEMS:
        np.random.seed(42)
        idx = np.sort(np.random.choice(n_items, MAX_ITEMS, replace=False))
        responses = responses[:, idx]
        exposure = exposure[:, idx]
        n_items = MAX_ITEMS
        subsampled = True
        log.info("[%s] Subsampled: %d -> %d items", domain_name, original_n_items, n_items)

    stan_data = prepare_stan_data(responses, exposure, MODEL_TYPE)
    fit, elapsed = fit_stan_model(
        STAN_FILE, stan_data,
        chains=args_dict["chains"],
        iter_warmup=args_dict["warmup"],
        iter_sampling=args_dict["samples"],
        adapt_delta=args_dict["adapt_delta"],
        max_treedepth=args_dict["max_treedepth"],
        seed=args_dict["seed"],
    )

    diag = check_convergence(fit)
    ppp = posterior_predictive_check(fit, responses)
    gamma_samples = fit.stan_variable("gamma")

    result = {
        "domain": domain_name,
        "n_items": n_items,
        "original_n_items": original_n_items,
        "subsampled": subsampled,
        "n_models": int(responses.shape[0]),
        "mean_acc": float(responses.mean()),
        "gamma": {
            "mean": float(np.mean(gamma_samples)),
            "median": float(np.median(gamma_samples)),
            "sd": float(np.std(gamma_samples)),
            "q025": float(np.percentile(gamma_samples, 2.5)),
            "q975": float(np.percentile(gamma_samples, 97.5)),
            "q05": float(np.percentile(gamma_samples, 5)),
            "q95": float(np.percentile(gamma_samples, 95)),
            "p_neg": float(np.mean(gamma_samples < 0)),
        },
        "diagnostics": diag,
        "ppp": ppp,
        "fit_time_sec": round(elapsed, 1),
    }

    theta_draws = fit.stan_variable("theta")
    result["theta"] = {
        "mean": np.round(np.mean(theta_draws, axis=0), 4).tolist(),
        "sd": np.round(np.std(theta_draws, axis=0), 4).tolist(),
        "q025": np.round(np.percentile(theta_draws, 2.5, axis=0), 4).tolist(),
        "q975": np.round(np.percentile(theta_draws, 97.5, axis=0), 4).tolist(),
    }

    domain_dir = output_dir / domain_name
    domain_dir.mkdir(parents=True, exist_ok=True)
    with open(domain_dir / "irt_results.json", "w") as f:
        json.dump(result, f, indent=2)

    return result


def fit_pooled(responses, exposure, args_dict, output_dir):
    n_models, n_items = responses.shape
    if n_items > MAX_ITEMS:
        np.random.seed(42)
        idx = np.sort(np.random.choice(n_items, MAX_ITEMS, replace=False))
        responses = responses[:, idx]
        exposure = exposure[:, idx]
        n_items = MAX_ITEMS
        log.info("[pooled] Subsampled to %d items", n_items)

    stan_data = prepare_stan_data(responses, exposure, MODEL_TYPE)
    fit, elapsed = fit_stan_model(
        STAN_FILE, stan_data,
        chains=args_dict["chains"],
        iter_warmup=args_dict["warmup"],
        iter_sampling=args_dict["samples"],
        adapt_delta=args_dict["adapt_delta"],
        max_treedepth=args_dict["max_treedepth"],
        seed=args_dict["seed"],
    )

    diag = check_convergence(fit)
    ppp = posterior_predictive_check(fit, responses)
    gamma_samples = fit.stan_variable("gamma")

    result = {
        "domain": "pooled",
        "n_items": n_items,
        "n_models": int(responses.shape[0]),
        "mean_acc": float(responses.mean()),
        "gamma": {
            "mean": float(np.mean(gamma_samples)),
            "median": float(np.median(gamma_samples)),
            "sd": float(np.std(gamma_samples)),
            "q025": float(np.percentile(gamma_samples, 2.5)),
            "q975": float(np.percentile(gamma_samples, 97.5)),
            "p_neg": float(np.mean(gamma_samples < 0)),
        },
        "diagnostics": diag,
        "ppp": ppp,
        "fit_time_sec": round(elapsed, 1),
    }

    pooled_dir = output_dir / "pooled"
    pooled_dir.mkdir(parents=True, exist_ok=True)
    with open(pooled_dir / "irt_results.json", "w") as f:
        json.dump(result, f, indent=2)

    return result


def _ppp_float(ppp):
    if isinstance(ppp, dict):
        return ppp.get("mean_ppp", ppp.get("ppp", 0.0))
    return float(ppp)


def generate_summary(all_results, output_dir, n_models):
    domains_ordered = [
        "STEM_Science", "STEM_Math", "STEM_CS_Eng", "Medical",
        "Other", "Business_Law", "Humanities", "Social_Sciences",
    ]

    lines = [f"# MMLU Domain IRT J=16 Qwen-only\n\nN_models = {n_models}\n"]
    lines.append("| Domain | N_items | γ_mean | γ_median | 95% CI | P(γ<0) | PPP | Rhat | ESS | Div |")
    lines.append("|--------|---------|--------|----------|--------|--------|-----|------|-----|-----|")

    summary_data = {}
    for domain in domains_ordered:
        r = all_results.get(domain)
        if not r:
            continue
        g = r["gamma"]
        d = r["diagnostics"]
        p_neg = g.get("p_neg", "N/A")
        p_neg_str = f"{p_neg:.3f}" if isinstance(p_neg, float) else str(p_neg)
        lines.append(
            f"| {domain} | {r['n_items']} | {g['mean']:.4f} | {g['median']:.4f} "
            f"| [{g['q025']:.3f}, {g['q975']:.3f}] | {p_neg_str} "
            f"| {_ppp_float(r['ppp']):.4f} | {d.get('max_rhat', 0):.4f} "
            f"| {d.get('min_ess', 0):.0f} | {d.get('divergent_count', 0)} |"
        )
        summary_data[domain] = {
            "gamma_mean": g["mean"], "gamma_median": g["median"],
            "ci95": [g["q025"], g["q975"]], "p_neg": p_neg,
            "n_items": r["n_items"], "ppp": _ppp_float(r["ppp"]),
        }

    if "pooled" in all_results:
        pg = all_results["pooled"]["gamma"]
        p_neg = pg.get("p_neg", "N/A")
        p_neg_str = f"{p_neg:.3f}" if isinstance(p_neg, float) else str(p_neg)
        lines.append(
            f"\n**Pooled**: γ={pg['mean']:.4f} [{pg['q025']:.3f}, {pg['q975']:.3f}], "
            f"P(γ<0)={p_neg_str}, PPP={_ppp_float(all_results['pooled']['ppp']):.4f}, "
            f"Rhat={all_results['pooled']['diagnostics'].get('max_rhat', 0):.4f}"
        )

    md_text = "\n".join(lines)
    print(md_text)

    with open(output_dir / "summary.md", "w") as f:
        f.write(md_text + "\n")
    with open(output_dir / "summary.json", "w") as f:
        json.dump(summary_data, f, indent=2)

    log.info("Summary saved to %s", output_dir / "summary.md")


def main():
    parser = argparse.ArgumentParser(description="MMLU domain gamma analysis (J=16 Qwen)")
    parser.add_argument("--eval-dir", default=EVAL_DIR)
    parser.add_argument("--rrf-path", default=RRF_PATH)
    parser.add_argument("--mmlu-arrow", default=MMLU_ARROW)
    parser.add_argument("--output-dir", default=OUTPUT_DIR)
    parser.add_argument("--domains", nargs="*", default=None)
    parser.add_argument("--chains", type=int, default=4)
    parser.add_argument("--warmup", type=int, default=1000)
    parser.add_argument("--samples", type=int, default=1000)
    parser.add_argument("--adapt-delta", type=float, default=0.95)
    parser.add_argument("--max-treedepth", type=int, default=12)
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--skip-pooled", action="store_true")
    parser.add_argument("--pooled-only", action="store_true")
    args = parser.parse_args()

    logging.basicConfig(level=logging.INFO,
                        format="%(asctime)s [%(levelname)s] %(message)s")

    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    # Load eval results for both scales
    data = load_pooled_eval_results(
        args.eval_dir, scales=["1.5B", "3B"],
        benchmarks=["mmlu"], aligned_only=True, skip_para=True,
    )
    models = data["models"]
    dosages = data["dosages"]
    full_responses = data["benchmarks"]["mmlu"]["responses"]
    n_total_items = data["benchmarks"]["mmlu"]["n_items"]

    log.info("Loaded %d models x %d items", len(models), n_total_items)

    # Load RRF
    with open(args.rrf_path) as f:
        rrf_data = json.load(f)

    # Filter to whitelist + resolve RRF keys
    keep_idx = []
    for i, m in enumerate(models):
        key = strip_aligned(m["dirname"])
        if key not in MODEL_WHITELIST:
            log.info("Not in whitelist: %s, skipping", m["dirname"])
            continue
        rrf_key = DIR_TO_RRF_KEY.get(key, key)
        if rrf_key in rrf_data and "mmlu" in rrf_data[rrf_key]:
            keep_idx.append(i)
        elif m["dosage"] == 0:
            keep_idx.append(i)
            log.info("No RRF for %s (dosage=0), will use zero exposure", m["dirname"])
        else:
            log.warning("No RRF entry for %s (dosage=%d), skipping!", m["dirname"], m["dosage"])

    keep_idx = np.array(keep_idx)
    models = [models[i] for i in keep_idx]
    dosages = dosages[keep_idx]
    full_responses = full_responses[keep_idx]

    log.info("After whitelist + RRF filter: %d models x %d items", len(models), n_total_items)
    for m in models:
        log.info("  %s (scale=%s, dosage=%d)", m["dirname"], m.get("scale"), m["dosage"])

    if len(models) != 16:
        log.warning("Expected 16 models, got %d!", len(models))

    # Save model order
    model_meta = [{"dirname": m["dirname"], "scale": m.get("scale"), "dosage": m["dosage"]}
                  for m in models]
    with open(output_dir / "model_order.json", "w") as f:
        json.dump(model_meta, f, indent=2)

    # Build RRF exposure matrix
    rrf_exposure = np.zeros((len(models), n_total_items), dtype=float)
    for i, m in enumerate(models):
        key = strip_aligned(m["dirname"])
        rrf_key = DIR_TO_RRF_KEY.get(key, key)
        if rrf_key in rrf_data and "mmlu" in rrf_data[rrf_key]:
            scores = rrf_data[rrf_key]["mmlu"]["exposure_scores"]
            rrf_exposure[i, :] = scores[:n_total_items]
        # else: dosage=0, already zeros

    # Build domain indices
    subject_list = build_subject_index_map(args.mmlu_arrow)
    domain_indices = build_domain_col_indices(subject_list, n_total_items)

    domains_to_fit = args.domains if args.domains else list(DOMAIN_MAP.keys())

    if args.dry_run:
        print(f"\n=== DRY RUN: N_models={len(models)}, N_items={n_total_items} ===\n")
        print(f"{'Domain':<18} {'N_items':>7} {'Mean_acc':>8}")
        print("-" * 40)
        for domain in domains_to_fit:
            idx = domain_indices[domain]
            if not idx:
                print(f"{domain:<18} {'0':>7} {'N/A':>8}")
                continue
            acc = full_responses[:, idx].mean()
            print(f"{domain:<18} {len(idx):>7} {acc:>8.4f}")
        print(f"\nModels ({len(models)}):")
        for m in models:
            print(f"  {m['dirname']} (scale={m.get('scale')}, d={m['dosage']})")
        print(f"\nDosages: {dosages.tolist()}")
        return

    # Fit per-domain
    args_dict = {
        "chains": args.chains, "warmup": args.warmup,
        "samples": args.samples, "adapt_delta": args.adapt_delta,
        "max_treedepth": args.max_treedepth, "seed": args.seed,
    }

    all_results = {}

    if args.pooled_only:
        for domain in list(DOMAIN_MAP.keys()):
            result_path = output_dir / domain / "irt_results.json"
            if result_path.exists():
                with open(result_path) as f:
                    all_results[domain] = json.load(f)
                log.info("Loaded existing result for %s", domain)
        domains_to_fit = []

    for domain in domains_to_fit:
        idx = domain_indices[domain]
        if len(idx) < 10:
            log.warning("Skipping %s: only %d items", domain, len(idx))
            continue

        log.info("=" * 50)
        log.info("Fitting domain: %s (%d items)", domain, len(idx))

        domain_resp = full_responses[:, idx]
        domain_exp = rrf_exposure[:, idx]

        result = fit_domain(domain, domain_resp, domain_exp, args_dict, output_dir)
        all_results[domain] = result

        g = result["gamma"]
        d = result["diagnostics"]
        log.info("[%s] gamma=%.4f [%.4f, %.4f], P(γ<0)=%.3f, rhat=%.4f, ESS=%.0f, div=%d, time=%.0fs",
                 domain, g["mean"], g["q025"], g["q975"], g["p_neg"],
                 d.get("max_rhat", 0), d.get("min_ess", 0),
                 d.get("divergent_count", 0), result["fit_time_sec"])

    # Pooled fit
    if not args.skip_pooled or args.pooled_only:
        log.info("=" * 50)
        log.info("Fitting POOLED model (all domains combined)")
        pooled_result = fit_pooled(full_responses, rrf_exposure, args_dict, output_dir)
        all_results["pooled"] = pooled_result
        pg = pooled_result["gamma"]
        log.info("[pooled] gamma=%.4f [%.4f, %.4f], P(γ<0)=%.3f, PPP=%.4f",
                 pg["mean"], pg["q025"], pg["q975"], pg["p_neg"],
                 _ppp_float(pooled_result["ppp"]))

    if all_results:
        print("\n" + "=" * 70)
        generate_summary(all_results, output_dir, len(models))
        with open(output_dir / "all_domain_results.json", "w") as f:
            json.dump(all_results, f, indent=2)
        log.info("Done. Results in %s", output_dir)


if __name__ == "__main__":
    main()
