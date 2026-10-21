#!/usr/bin/env python3
"""
MMLU domain-stratified gamma analysis via 2PL+gamma IRT.

Splits MMLU 14042 items into 7 knowledge domains (+ Other), fits per-domain
2PL+gamma IRT models on 1.5B eval data, and outputs a summary table of
per-domain contamination sensitivity (gamma).

Input:
  - 1.5B eval results in EVAL_DIR (correctness per item per model)
  - MMLU subject-to-domain mapping (hardcoded)
  - Stan 2PL+gamma model

Output:
  - per_domain_gamma_summary.json: structured results
  - per_domain_gamma_summary.md: human-readable table
  - per-domain fit JSONs in subdirectories

Dependencies: cmdstanpy, numpy, pyarrow (for MMLU subject index mapping)
"""

import argparse
import json
import logging
import os
import sys
import time
from pathlib import Path

import numpy as np

sys.path.insert(0, "/root/contamcal-irt-calibration/exp006")
from run_irt_calibration import (
    load_eval_results,
    prepare_stan_data,
    fit_stan_model,
    check_convergence,
    posterior_predictive_check,
    extract_results,
    STAN_MODELS,
)

log = logging.getLogger(__name__)

# ── MMLU Domain Mapping ──
# 57 subjects -> 7 domains + Other

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
OUTPUT_DIR = Path("/root/autodl-tmp/exp006/results_mmlu_domain_gamma")
MODEL_TYPE = "2pl_gamma"
STAN_FILE = STAN_MODELS[MODEL_TYPE]
MAX_ITEMS = 2000


def build_subject_index_map(arrow_path):
    """Read MMLU arrow cache to get subject for each item index."""
    import pyarrow as pa
    reader = pa.ipc.open_stream(arrow_path)
    table = reader.read_all()
    subjects = table.column("subject").to_pylist()
    return subjects


def build_domain_indices(subject_list):
    """Map each domain to a list of item indices in the MMLU response array."""
    # Invert DOMAIN_MAP: subject -> domain
    subj_to_domain = {}
    for domain, subjects in DOMAIN_MAP.items():
        for s in subjects:
            subj_to_domain[s] = domain

    domain_indices = {d: [] for d in DOMAIN_MAP}
    unmapped = []
    for i, subj in enumerate(subject_list):
        domain = subj_to_domain.get(subj)
        if domain:
            domain_indices[domain].append(i)
        else:
            unmapped.append((i, subj))

    if unmapped:
        log.warning("Unmapped subjects: %s", set(s for _, s in unmapped))

    return domain_indices


def build_oracle_exposure(dosages, n_items):
    """Oracle exposure: dosage_fraction (dosage/100) * uniform tau=1."""
    fracs = dosages / 100.0
    return np.outer(fracs, np.ones(n_items))


def load_1_5b_mmlu_data(eval_dir, skip_para=True, aligned_only=True):
    """Load 1.5B MMLU eval results with proper item-index alignment.

    Para models may evaluate a subset of items. This function finds the
    intersection of item indices across all models and builds a properly
    aligned response matrix.
    """
    from run_irt_calibration import parse_model_dir_name
    eval_path = Path(eval_dir)
    model_dirs = sorted([
        d for d in eval_path.iterdir()
        if d.is_dir() and (d / "eval_results.json").exists()
    ])

    models = []
    for d in model_dirs:
        info = parse_model_dir_name(d.name)
        if info is None:
            log.warning("Skipping unrecognized dir: %s", d.name)
            continue
        if skip_para and info["is_para"]:
            continue
        if aligned_only and not info.get("is_aligned", False):
            log.info("Skipping non-aligned dir: %s", d.name)
            continue
        if "1.5B" not in d.name:
            log.info("Skipping dir (scale mismatch): %s", d.name)
            continue
        info["path"] = str(d)
        models.append(info)

    # Dedup: prefer alpha=32 variants
    seen = {}
    for m in models:
        key = (m["model_name"], m["dosage"], m["seed"], m["is_para"])
        if key not in seen:
            seen[key] = m
        elif m.get("has_alpha") and not seen[key].get("has_alpha"):
            seen[key] = m
    models = list(seen.values())

    if not models:
        raise ValueError(f"No valid 1.5B eval results in {eval_dir}")
    log.info("Found %d model evaluations", len(models))

    # Load per_item with indices for each model
    all_item_indices = []
    all_per_item = []
    for m in models:
        with open(Path(m["path"]) / "eval_results.json") as f:
            data = json.load(f)
        per_item = data["benchmarks"]["mmlu"]["per_item"]
        indices = [it["index"] for it in per_item]
        all_item_indices.append(set(indices))
        all_per_item.append({it["index"]: int(it["correct"]) for it in per_item})

    # Find intersection of item indices
    common_indices = sorted(set.intersection(*all_item_indices))
    n_items = len(common_indices)
    log.info("Item alignment: intersection of %d models -> %d common items", len(models), n_items)

    # Build aligned response matrix
    matrix = np.zeros((len(models), n_items), dtype=int)
    for j, item_map in enumerate(all_per_item):
        for col, idx in enumerate(common_indices):
            matrix[j, col] = item_map[idx]

    dosages = np.array([m["dosage"] for m in models])

    return {
        "models": models,
        "benchmarks": {"mmlu": {"responses": matrix, "n_items": n_items}},
        "dosages": dosages,
        "item_indices": common_indices,
    }


def fit_domain(domain_name, responses_domain, dosages, args_dict, output_dir):
    """Fit 2PL+gamma for a single MMLU domain."""
    n_models, n_items = responses_domain.shape
    original_n_items = n_items
    subsampled = False

    if n_items > MAX_ITEMS:
        np.random.seed(42)
        indices = np.random.choice(n_items, MAX_ITEMS, replace=False)
        indices.sort()
        responses_domain = responses_domain[:, indices]
        n_items = MAX_ITEMS
        subsampled = True
        log.info("[%s] Subsampled: %d -> %d items", domain_name, original_n_items, n_items)

    log.info("[%s] N_models=%d, N_items=%d", domain_name, n_models, n_items)

    exposure = build_oracle_exposure(dosages, n_items)
    stan_data = prepare_stan_data(responses_domain, exposure, MODEL_TYPE)

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
    ppc = posterior_predictive_check(fit, responses_domain)
    results = extract_results(fit, responses_domain, MODEL_TYPE)

    domain_dir = output_dir / domain_name
    domain_dir.mkdir(parents=True, exist_ok=True)
    result_dict = {
        "domain": domain_name,
        "n_models": n_models,
        "n_items": n_items,
        "original_n_items": original_n_items,
        "subsampled": subsampled,
        "dosages": dosages.tolist(),
        "fit_time_sec": round(elapsed, 1),
        "diagnostics": diagnostics,
        "posterior_predictive": ppc,
        "gamma": results.get("gamma", {}),
        "calibrated_scores": results.get("calibrated_scores", {}),
        "mean_accuracy": round(float(responses_domain.mean()), 4),
    }
    with open(domain_dir / "irt_results.json", "w") as f:
        json.dump(result_dict, f, indent=2)

    return result_dict


def generate_summary_table(all_results, output_dir):
    """Generate markdown and JSON summary tables."""
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
            "rhat": d.get("max_rhat", None),
            "min_ess": d.get("min_ess", None),
            "divergences": d.get("divergent_count", None),
            "ppp": r["posterior_predictive"].get("overall_ppp", None),
            "fit_time_sec": r["fit_time_sec"],
        })

    # Sort by gamma descending
    rows.sort(key=lambda x: x["gamma_mean"], reverse=True)

    # JSON
    with open(output_dir / "per_domain_gamma_summary.json", "w") as f:
        json.dump(rows, f, indent=2)

    # Markdown
    lines = [
        "# MMLU Per-Domain Gamma Analysis (2PL+γ, 1.5B)",
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
    parser = argparse.ArgumentParser(
        description="MMLU domain-stratified gamma analysis (2PL+γ)")
    parser.add_argument("--eval-dir", type=str, default=EVAL_DIR)
    parser.add_argument("--output-dir", type=str, default=str(OUTPUT_DIR))
    parser.add_argument("--mmlu-arrow", type=str, default=MMLU_ARROW,
                        help="Path to cached MMLU test arrow file for subject mapping")
    parser.add_argument("--chains", type=int, default=4)
    parser.add_argument("--warmup", type=int, default=1000)
    parser.add_argument("--samples", type=int, default=1000)
    parser.add_argument("--adapt-delta", type=float, default=0.95)
    parser.add_argument("--max-treedepth", type=int, default=12)
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--domains", type=str, nargs="*", default=None,
                        help="Subset of domains to fit (default: all)")
    parser.add_argument("--include-para", action="store_true",
                        help="Include paraphrased training variants")
    parser.add_argument("--dry-run", action="store_true",
                        help="Load data and print domain stats without fitting")
    args = parser.parse_args()

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(message)s",
    )

    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    # Step 1: Load 1.5B MMLU eval data (with item-index alignment)
    log.info("Loading 1.5B MMLU eval data from %s", args.eval_dir)
    data = load_1_5b_mmlu_data(
        args.eval_dir,
        skip_para=not args.include_para,
        aligned_only=True,
    )
    mmlu_data = data["benchmarks"]["mmlu"]
    full_responses = mmlu_data["responses"]
    dosages = data["dosages"]
    n_total_items = mmlu_data["n_items"]
    item_indices = data.get("item_indices")

    log.info("Loaded: %d models x %d items", full_responses.shape[0], n_total_items)
    log.info("Models: %s", [m["dirname"] for m in data["models"]])
    log.info("Dosages: %s", dosages.tolist())

    # Step 2: Build domain indices mapped to response matrix columns
    log.info("Loading MMLU subject map from %s", args.mmlu_arrow)
    subject_list = build_subject_index_map(args.mmlu_arrow)

    if item_indices is not None:
        # Map arrow-file indices to response matrix column positions
        arrow_to_col = {arrow_idx: col for col, arrow_idx in enumerate(item_indices)}
        subj_to_domain = {}
        for domain, subjects in DOMAIN_MAP.items():
            for s in subjects:
                subj_to_domain[s] = domain
        domain_indices = {d: [] for d in DOMAIN_MAP}
        for arrow_idx, col in arrow_to_col.items():
            if arrow_idx < len(subject_list):
                subj = subject_list[arrow_idx]
                domain = subj_to_domain.get(subj)
                if domain:
                    domain_indices[domain].append(col)
    else:
        domain_indices = build_domain_indices(subject_list)

    for domain, indices in domain_indices.items():
        log.info("Domain %-15s: %4d items", domain, len(indices))

    total_mapped = sum(len(v) for v in domain_indices.values())
    log.info("Total mapped: %d / %d", total_mapped, n_total_items)

    domains_to_fit = args.domains if args.domains else list(DOMAIN_MAP.keys())

    if args.dry_run:
        print("\n=== DRY RUN: Domain Statistics ===\n")
        print(f"{'Domain':<18} {'N_items':>7} {'Mean_acc':>8} {'Subjects':>8}")
        print("-" * 55)
        for domain in domains_to_fit:
            indices = domain_indices[domain]
            if not indices:
                print(f"{domain:<18} {'0':>7} {'N/A':>8} {len(DOMAIN_MAP[domain]):>8}")
                continue
            domain_resp = full_responses[:, indices]
            acc = domain_resp.mean()
            print(f"{domain:<18} {len(indices):>7} {acc:>8.4f} {len(DOMAIN_MAP[domain]):>8}")
        print(f"\nTotal models: {full_responses.shape[0]}")
        print(f"Dosages: {dosages.tolist()}")
        print(f"Stan model: {MODEL_TYPE} ({STAN_FILE})")
        print(f"MCMC: {args.chains} chains x {args.warmup}w + {args.samples}s, "
              f"adapt_delta={args.adapt_delta}")

        # Rough time estimate: ~10-30s per 100 items with 8 models, 4 chains
        total_time = 0
        for domain in domains_to_fit:
            n = min(len(domain_indices[domain]), MAX_ITEMS)
            # Empirical: ~0.05-0.1s per item per chain
            est = n * 0.08 * args.chains
            total_time += est
            print(f"  {domain}: ~{est:.0f}s estimated")
        print(f"\nTotal estimated time: ~{total_time:.0f}s ({total_time/60:.1f} min)")
        return

    # Step 3: Fit per-domain IRT
    args_dict = {
        "chains": args.chains,
        "warmup": args.warmup,
        "samples": args.samples,
        "adapt_delta": args.adapt_delta,
        "max_treedepth": args.max_treedepth,
        "seed": args.seed,
    }

    all_results = {}
    for domain in domains_to_fit:
        indices = domain_indices[domain]
        if len(indices) < 10:
            log.warning("Skipping %s: only %d items", domain, len(indices))
            continue

        log.info("=" * 50)
        log.info("Fitting domain: %s (%d items)", domain, len(indices))
        log.info("=" * 50)

        domain_responses = full_responses[:, indices]
        result = fit_domain(domain, domain_responses, dosages, args_dict, output_dir)
        all_results[domain] = result

        g = result["gamma"]
        d = result["diagnostics"]
        log.info("[%s] gamma=%.4f [%.4f, %.4f], rhat=%.4f, ESS=%.0f, div=%d, time=%.0fs",
                 domain, g["mean"], g["q025"], g["q975"],
                 d.get("max_rhat", 0), d.get("min_ess", 0),
                 d.get("divergent_count", 0), result["fit_time_sec"])

    # Step 4: Summary
    if all_results:
        print("\n" + "=" * 70)
        generate_summary_table(all_results, output_dir)

        with open(output_dir / "all_domain_results.json", "w") as f:
            json.dump(all_results, f, indent=2)

        log.info("All results saved to %s", output_dir)


if __name__ == "__main__":
    main()
