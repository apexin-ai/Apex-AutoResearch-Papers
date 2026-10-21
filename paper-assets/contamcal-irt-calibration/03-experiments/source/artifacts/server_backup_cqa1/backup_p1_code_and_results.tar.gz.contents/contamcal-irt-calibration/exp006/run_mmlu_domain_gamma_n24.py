#!/usr/bin/env python3
"""MMLU domain-stratified gamma analysis with all scales (0.5B+1.5B+3B) and RRF exposure."""

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

EVAL_DIR = "/root/autodl-tmp/exp001/eval_results"
MMLU_ARROW = "/root/autodl-tmp/.hf_cache/cais___mmlu/all/0.0.0/c30699e8356da336a370243923dbaf21066bb9fe/mmlu-test.arrow"
RRF_PATH = "/root/autodl-tmp/exp003/rrf_all_scales/exposure_scores.json"
OUTPUT_DIR = "/root/autodl-tmp/exp006/results_mmlu_domain_gamma_n24"
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
    """Map each domain to column indices (0..n_items-1) in the response matrix."""
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
    """Fit 2PL+gamma for a single MMLU domain."""
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

    diagnostics = check_convergence(fit)
    ppc = posterior_predictive_check(fit, responses)
    results = extract_results(fit, responses, MODEL_TYPE)

    domain_dir = output_dir / domain_name
    domain_dir.mkdir(parents=True, exist_ok=True)
    result_dict = {
        "domain": domain_name,
        "n_models": n_models,
        "n_items": n_items,
        "original_n_items": original_n_items,
        "subsampled": subsampled,
        "fit_time_sec": round(elapsed, 1),
        "diagnostics": diagnostics,
        "posterior_predictive": ppc,
        "gamma": results.get("gamma", {}),
        "mean_accuracy": round(float(responses.mean()), 4),
    }
    with open(domain_dir / "irt_results.json", "w") as f:
        json.dump(result_dict, f, indent=2)
    return result_dict


def generate_summary(all_results, output_dir, n_models_total):
    rows = []
    for domain in DOMAIN_MAP:
        if domain not in all_results:
            continue
        r = all_results[domain]
        g = r["gamma"]
        d = r["diagnostics"]
        rows.append({
            "domain": domain,
            "n_items": r["n_items"],
            "n_models": r["n_models"],
            "mean_acc": r["mean_accuracy"],
            "gamma_mean": g["mean"],
            "gamma_sd": g["sd"],
            "gamma_q025": g["q025"],
            "gamma_q975": g["q975"],
            "rhat": d.get("max_rhat"),
            "min_ess": d.get("min_ess"),
            "divergences": d.get("divergent_count"),
            "ppp": r["posterior_predictive"].get("overall_ppp"),
            "fit_time_sec": r["fit_time_sec"],
        })

    rows.sort(key=lambda x: x["gamma_mean"], reverse=True)

    with open(output_dir / "per_domain_gamma_summary.json", "w") as f:
        json.dump(rows, f, indent=2)

    lines = [
        f"# MMLU Per-Domain Gamma (2PL+γ, N={n_models_total}, 0.5B+1.5B+3B, RRF exposure)",
        "",
        "| Domain | N_items | N_models | Acc | γ̂ | SD | 95% CI | R̂ | ESS | Div | PPP | Time(s) |",
        "|--------|---------|----------|-----|------|------|--------|------|------|-----|------|---------|",
    ]
    for r in rows:
        ci = f"[{r['gamma_q025']:.3f}, {r['gamma_q975']:.3f}]"
        lines.append(
            f"| {r['domain']} | {r['n_items']} | {r['n_models']} | "
            f"{r['mean_acc']:.3f} | {r['gamma_mean']:.4f} | {r['gamma_sd']:.4f} | "
            f"{ci} | {r['rhat']:.3f} | {r['min_ess']:.0f} | "
            f"{r['divergences']} | {r['ppp']:.3f} | {r['fit_time_sec']:.0f} |"
        )
    lines.extend(["", f"Generated: {time.strftime('%Y-%m-%d %H:%M:%S')}"])
    md_text = "\n".join(lines)

    with open(output_dir / "per_domain_gamma_summary.md", "w") as f:
        f.write(md_text)
    print(md_text)
    return rows


def main():
    parser = argparse.ArgumentParser(description="MMLU domain gamma (all scales, RRF)")
    parser.add_argument("--eval-dir", type=str, default=EVAL_DIR)
    parser.add_argument("--output-dir", type=str, default=OUTPUT_DIR)
    parser.add_argument("--rrf-path", type=str, default=RRF_PATH)
    parser.add_argument("--mmlu-arrow", type=str, default=MMLU_ARROW)
    parser.add_argument("--include-para", action="store_true")
    parser.add_argument("--chains", type=int, default=4)
    parser.add_argument("--warmup", type=int, default=1000)
    parser.add_argument("--samples", type=int, default=1000)
    parser.add_argument("--adapt-delta", type=float, default=0.95)
    parser.add_argument("--max-treedepth", type=int, default=12)
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--domains", type=str, nargs="*", default=None)
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")

    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    # Load RRF exposure
    log.info("Loading RRF exposure from %s", args.rrf_path)
    with open(args.rrf_path) as f:
        rrf_data = json.load(f)

    # Load all scales
    scales = ["0.5B", "1.5B", "3B"]
    log.info("Loading pooled eval results: scales=%s", scales)
    data = load_pooled_eval_results(
        args.eval_dir, scales, benchmarks=["mmlu"],
        skip_para=not args.include_para, aligned_only=True,
    )

    mmlu = data["benchmarks"]["mmlu"]
    full_responses = mmlu["responses"]
    valid_mask = mmlu["valid_mask"]
    n_total_items = mmlu["n_items"]
    models = data["models"]
    dosages = data["dosages"]

    # Filter to models with RRF entries
    keep_idx = []
    for i, m in enumerate(models):
        if not valid_mask[i]:
            continue
        key = strip_aligned(m["dirname"])
        if key in rrf_data and "mmlu" in rrf_data[key]:
            keep_idx.append(i)
        else:
            log.info("No RRF entry for %s, skipping", m["dirname"])

    keep_idx = np.array(keep_idx)
    models = [models[i] for i in keep_idx]
    dosages = dosages[keep_idx]
    full_responses = full_responses[keep_idx]

    log.info("After RRF filter: %d models x %d items", len(models), n_total_items)
    for m in models:
        log.info("  %s (scale=%s, dosage=%d)", m["dirname"], m.get("scale"), m["dosage"])

    # Build RRF exposure matrix (N_models x N_items)
    rrf_exposure = np.zeros((len(models), n_total_items), dtype=float)
    for i, m in enumerate(models):
        key = strip_aligned(m["dirname"])
        scores = rrf_data[key]["mmlu"]["exposure_scores"]
        rrf_exposure[i, :] = scores[:n_total_items]

    # Build domain indices from MMLU arrow
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
        return

    # Fit per-domain
    args_dict = {
        "chains": args.chains, "warmup": args.warmup,
        "samples": args.samples, "adapt_delta": args.adapt_delta,
        "max_treedepth": args.max_treedepth, "seed": args.seed,
    }

    all_results = {}
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
        log.info("[%s] gamma=%.4f [%.4f, %.4f], rhat=%.4f, ESS=%.0f, div=%d, time=%.0fs",
                 domain, g["mean"], g["q025"], g["q975"],
                 d.get("max_rhat", 0), d.get("min_ess", 0),
                 d.get("divergent_count", 0), result["fit_time_sec"])

    if all_results:
        print("\n" + "=" * 70)
        generate_summary(all_results, output_dir, len(models))
        with open(output_dir / "all_domain_results.json", "w") as f:
            json.dump(all_results, f, indent=2)
        log.info("Done. Results in %s", output_dir)


if __name__ == "__main__":
    main()
