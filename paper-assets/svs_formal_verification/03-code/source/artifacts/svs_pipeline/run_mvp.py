"""SVS MVP runner — end-to-end pipeline for the minimum viable experiment.

Loads config (YAML or defaults), runs 50 ProofWriter depth-5 problems × 8
chains each through the full SVS pipeline, computes pass/fail criteria,
and outputs a structured JSON report.

Usage:
    python -m svs_pipeline.run_mvp [--config config.yaml] [--output-dir outputs/]
"""

import argparse
import json
import logging
import os
import random
import sys
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from dataclasses import asdict
from pathlib import Path

import yaml
import numpy as np
from scipy import stats

from .config import PipelineConfig, APIConfig, SamplingConfig, VerificationConfig, MVPConfig
from .types import Problem, Chain, SVSResult
from .data import load_problems
from .generation import ChainSampler
from .formalization import ClaimDecomposer, AutoFormalizer, VocabNormalizer, PremiseFormalizer
from .verification import Z3Checker, CrossChainChecker, SVSScorer
from .cost_tracker import get_tracker, reset_tracker
from .evaluation import evaluate_results

logger = logging.getLogger(__name__)


def load_config(config_path: str | None = None) -> PipelineConfig:
    """Load config from YAML file, falling back to dataclass defaults."""
    cfg = PipelineConfig()
    if config_path and os.path.exists(config_path):
        with open(config_path) as f:
            raw = yaml.safe_load(f)

        if "api" in raw:
            for k, v in raw["api"].items():
                if isinstance(v, str) and v.startswith("${"):
                    continue
                if hasattr(cfg.api, k):
                    setattr(cfg.api, k, v)
        if "sampling" in raw:
            for k, v in raw["sampling"].items():
                if hasattr(cfg.sampling, k):
                    setattr(cfg.sampling, k, v)
        if "verification" in raw:
            for k, v in raw["verification"].items():
                if hasattr(cfg.verification, k):
                    setattr(cfg.verification, k, v)
        if "mvp" in raw:
            for k, v in raw["mvp"].items():
                if hasattr(cfg.mvp, k):
                    setattr(cfg.mvp, k, v)
        if "output_dir" in raw:
            cfg.output_dir = raw["output_dir"]
        if "verbose" in raw:
            cfg.verbose = raw["verbose"]

        logger.info("Loaded config from %s", config_path)
    else:
        logger.info("Using default config (no YAML provided or file missing)")

    return cfg


def run_pipeline(cfg: PipelineConfig) -> dict:
    """Execute the full MVP pipeline and return a results dict."""
    reset_tracker()
    random.seed(cfg.mvp.seed)
    np.random.seed(cfg.mvp.seed)

    out_dir = Path(cfg.output_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    # --- Step 1: Load data ---
    logger.info("Loading %d %s %s problems...", cfg.mvp.num_problems, cfg.mvp.dataset, cfg.mvp.subset)
    problems = load_problems(
        dataset=cfg.mvp.dataset,
        subset=cfg.mvp.subset,
        num_problems=cfg.mvp.num_problems,
        seed=cfg.mvp.seed,
    )
    logger.info("Loaded %d problems", len(problems))

    # --- Step 2: Initialize pipeline components ---
    sampler = ChainSampler(cfg.api, cfg.sampling)
    decomposer = ClaimDecomposer(cfg.api)
    vocab_norm = VocabNormalizer(cfg.api)
    formalizer = AutoFormalizer(cfg.api)
    premise_formalizer = PremiseFormalizer(cfg.api)
    z3_checker = Z3Checker(cfg.verification)
    cross_checker = CrossChainChecker(cfg.verification)
    scorer = SVSScorer(cfg.verification)

    # --- Step 3: Resume support ---
    results: list[SVSResult] = []
    all_chain_details = {}
    formalization_stats = {"total_claims": 0, "formalized_claims": 0}
    partial_path = out_dir / "results_partial.json"
    completed_ids: set[str] = set()

    if partial_path.exists():
        try:
            with open(partial_path) as f:
                existing = json.load(f)
            completed_ids = {r["problem_id"] for r in existing}
            logger.info("Resuming: %d problems already completed", len(completed_ids))
        except Exception as e:
            logger.warning("Could not load partial results: %s", e)

    # --- Step 4: Process each problem ---
    for i, problem in enumerate(problems):
        if problem.id in completed_ids:
            logger.info("Skipping completed problem %s (%d/%d)", problem.id, i + 1, len(problems))
            continue

        t0 = time.time()
        logger.info("--- Problem %d/%d: %s ---", i + 1, len(problems), problem.id)

        chains = sampler.sample(problem, cfg.sampling.num_chains)
        logger.info("Sampled %d chains", len(chains))

        vocab = vocab_norm.extract_vocab(problem)

        premise_fols = premise_formalizer.formalize_premises(problem, vocab)
        logger.info("Formalized %d/%d premises", len(premise_fols), len(problem.premises))
        formalization_stats["total_premises"] = formalization_stats.get("total_premises", 0) + len(problem.premises)
        formalization_stats["formalized_premises"] = formalization_stats.get("formalized_premises", 0) + len(premise_fols)

        chain_claims = {}

        def _process_chain(chain, _problem=problem, _vocab=vocab):
            claims = decomposer.decompose(chain, _problem)
            claims = formalizer.formalize_batch(claims, _vocab)
            return chain.chain_id, claims

        with ThreadPoolExecutor(max_workers=min(len(chains), 4)) as executor:
            futures = [executor.submit(_process_chain, c) for c in chains]
            for future in as_completed(futures):
                chain_id, claims = future.result()
                chain_claims[chain_id] = claims
                formalization_stats["total_claims"] += len(claims)
                formalization_stats["formalized_claims"] += sum(1 for c in claims if c.z3_parseable)

        result = scorer.select_answer(chains, chain_claims, vocab, z3_checker, cross_checker, premise_fols=premise_fols)
        result.gold_label = problem.label
        result.correct_svs = result.selected_answer == problem.label
        result.correct_sc = result.sc_answer == problem.label
        results.append(result)

        elapsed = time.time() - t0
        logger.info(
            "Problem %s: SVS=%s (correct=%s), SC=%s (correct=%s) [%.1fs]",
            problem.id, result.selected_answer, result.correct_svs,
            result.sc_answer, result.correct_sc, elapsed,
        )

        all_chain_details[problem.id] = {
            "chains": len(chains),
            "vocab_predicates": len(vocab.get("predicates", {})),
            "vocab_constants": len(vocab.get("constants", {})),
            "group_scores": result.group_scores,
        }

        # Save partial results after each problem
        try:
            partial_data = [asdict(r) for r in results]
            with open(partial_path, "w") as f:
                json.dump(partial_data, f, indent=2, default=str)
        except Exception as e:
            logger.warning("Failed to save partial results: %s", e)

    # --- Step 4: Compute metrics and pass/fail ---
    report = evaluate_and_judge(results, formalization_stats, cfg)

    # --- Cost summary ---
    cost_summary = get_tracker().summary()
    report["cost"] = cost_summary
    logger.info(
        "API Cost: %d calls, %d tokens (in=%d, out=%d), est. $%.4f",
        cost_summary["total_calls"],
        cost_summary["total_tokens"],
        cost_summary["total_input_tokens"],
        cost_summary["total_output_tokens"],
        cost_summary["estimated_cost_usd"],
    )

    # --- Step 5: Save outputs ---
    report_path = out_dir / "mvp_report.json"
    with open(report_path, "w") as f:
        json.dump(report, f, indent=2, default=str)
    logger.info("Report saved to %s", report_path)

    details_path = out_dir / "chain_details.json"
    with open(details_path, "w") as f:
        json.dump(all_chain_details, f, indent=2, default=str)

    results_path = out_dir / "results.json"
    with open(results_path, "w") as f:
        json.dump([asdict(r) for r in results], f, indent=2, default=str)

    return report


def evaluate_and_judge(
    results: list[SVSResult],
    form_stats: dict,
    cfg: PipelineConfig,
) -> dict:
    """Compute MVP pass criteria from results."""
    n = len(results)
    svs_correct = sum(1 for r in results if r.correct_svs)
    sc_correct = sum(1 for r in results if r.correct_sc)
    svs_acc = svs_correct / n if n else 0
    sc_acc = sc_correct / n if n else 0

    form_rate = (
        form_stats["formalized_claims"] / form_stats["total_claims"]
        if form_stats["total_claims"] > 0 else 0
    )

    # P1: Autoformalization success rate > 50%
    p1_pass = form_rate > 0.5

    # P2: Chains producing the correct answer have higher IC than those producing wrong answers
    correct_ic_scores = []
    incorrect_ic_scores = []
    for result in results:
        for cv in result.chain_verifications:
            if cv.answer == result.gold_label:
                correct_ic_scores.append(cv.ic_score)
            else:
                incorrect_ic_scores.append(cv.ic_score)

    p2_cohens_d = None
    p2_ci_lower = None
    p2_ci_upper = None
    p2_ttest_p = None
    p2_mannwhitney_p = None
    p2_pass = False
    p2_mean_correct = None
    p2_mean_incorrect = None

    if len(correct_ic_scores) >= 2 and len(incorrect_ic_scores) >= 2:
        correct_arr = np.array(correct_ic_scores)
        incorrect_arr = np.array(incorrect_ic_scores)
        p2_mean_correct = float(correct_arr.mean())
        p2_mean_incorrect = float(incorrect_arr.mean())

        mean_diff = p2_mean_correct - p2_mean_incorrect
        n_c, n_i = len(correct_arr), len(incorrect_arr)
        pooled_std = np.sqrt(
            ((n_c - 1) * correct_arr.std(ddof=1)**2
             + (n_i - 1) * incorrect_arr.std(ddof=1)**2)
            / (n_c + n_i - 2)
        )
        p2_cohens_d = mean_diff / pooled_std if pooled_std > 0 else 0.0

        _, p2_ttest_p = stats.ttest_ind(correct_arr, incorrect_arr, alternative="greater")
        _, p2_mannwhitney_p = stats.mannwhitneyu(
            correct_arr, incorrect_arr, alternative="greater"
        )

        rng = np.random.default_rng(cfg.mvp.seed)
        n_boot = 1000
        boot_diffs = np.empty(n_boot)
        for b in range(n_boot):
            bc = rng.choice(correct_arr, size=n_c, replace=True)
            bi = rng.choice(incorrect_arr, size=n_i, replace=True)
            boot_diffs[b] = bc.mean() - bi.mean()
        p2_ci_lower = float(np.percentile(boot_diffs, 2.5))
        p2_ci_upper = float(np.percentile(boot_diffs, 97.5))

        ci_excludes_zero = p2_ci_lower > 0
        d_threshold = cfg.mvp.cohens_d_threshold
        p_threshold = cfg.mvp.p_value_threshold
        p2_pass = (p2_cohens_d > d_threshold and ci_excludes_zero) or (p2_ttest_p < p_threshold)

    # Per-problem paired analysis
    per_problem_pairs = []
    for result in results:
        correct_chains = [cv for cv in result.chain_verifications if cv.answer == result.gold_label]
        incorrect_chains = [cv for cv in result.chain_verifications if cv.answer != result.gold_label]
        if correct_chains and incorrect_chains:
            mean_c = np.mean([cv.ic_score for cv in correct_chains])
            mean_i = np.mean([cv.ic_score for cv in incorrect_chains])
            per_problem_pairs.append({
                "problem_id": result.problem_id,
                "correct_ic_mean": float(mean_c),
                "incorrect_ic_mean": float(mean_i),
                "diff": float(mean_c - mean_i),
            })

    paired_analysis = {"n_problems_with_both": len(per_problem_pairs)}
    if len(per_problem_pairs) >= 2:
        diffs = np.array([p["diff"] for p in per_problem_pairs])
        paired_analysis["mean_diff"] = float(diffs.mean())
        _, paired_ttest_p = stats.ttest_1samp(diffs, 0, alternative="greater")
        paired_analysis["paired_ttest_p"] = float(paired_ttest_p)
        try:
            _, wilcoxon_p = stats.wilcoxon(diffs, alternative="greater")
            paired_analysis["wilcoxon_p"] = float(wilcoxon_p)
        except ValueError:
            paired_analysis["wilcoxon_p"] = None

    report = {
        "config": {
            "num_problems": cfg.mvp.num_problems,
            "num_chains": cfg.sampling.num_chains,
            "total_chains": cfg.mvp.num_problems * cfg.sampling.num_chains,
            "dataset": f"{cfg.mvp.dataset}/{cfg.mvp.subset}",
            "seed": cfg.mvp.seed,
        },
        "accuracy": {
            "svs": {"correct": svs_correct, "total": n, "accuracy": round(svs_acc, 4)},
            "sc": {"correct": sc_correct, "total": n, "accuracy": round(sc_acc, 4)},
            "delta": round(svs_acc - sc_acc, 4),
        },
        "formalization": {
            "total_claims": form_stats["total_claims"],
            "formalized_claims": form_stats["formalized_claims"],
            "rate": round(form_rate, 4),
        },
        "p1_autoformalization": {
            "threshold": 0.5,
            "actual": round(form_rate, 4),
            "pass": p1_pass,
        },
        "p2_ic_discrimination": {
            "method": "chain-level IC by gold answer",
            "n_correct_chains": len(correct_ic_scores),
            "n_incorrect_chains": len(incorrect_ic_scores),
            "mean_correct_ic": round(p2_mean_correct, 4) if p2_mean_correct is not None else None,
            "mean_incorrect_ic": round(p2_mean_incorrect, 4) if p2_mean_incorrect is not None else None,
            "cohens_d": round(p2_cohens_d, 4) if p2_cohens_d is not None else None,
            "cohens_d_threshold": cfg.mvp.cohens_d_threshold,
            "ci_95": [round(p2_ci_lower, 4), round(p2_ci_upper, 4)] if p2_ci_lower is not None else None,
            "ci_excludes_zero": p2_ci_lower > 0 if p2_ci_lower is not None else None,
            "ttest_p_value": round(p2_ttest_p, 6) if p2_ttest_p is not None else None,
            "mannwhitney_p_value": round(p2_mannwhitney_p, 6) if p2_mannwhitney_p is not None else None,
            "p_value_threshold": cfg.mvp.p_value_threshold,
            "pass": p2_pass,
            "paired_analysis": paired_analysis,
        },
        "verdict": {
            "p1": "PASS" if p1_pass else "FAIL",
            "p2": "PASS" if p2_pass else "FAIL",
            "overall": "PASS" if (p1_pass and p2_pass) else "FAIL",
        },
    }
    return report


def main():
    parser = argparse.ArgumentParser(description="Run SVS MVP experiment")
    parser.add_argument("--config", type=str, default="config.yaml", help="Path to config YAML")
    parser.add_argument("--output-dir", type=str, default=None, help="Override output directory")
    parser.add_argument("--verbose", action="store_true", default=True)
    args = parser.parse_args()

    log_level = logging.DEBUG if args.verbose else logging.INFO
    logging.basicConfig(
        level=log_level,
        format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
        datefmt="%H:%M:%S",
    )

    cfg = load_config(args.config)
    if args.output_dir:
        cfg.output_dir = args.output_dir

    logger.info(
        "MVP config: %d problems × %d chains = %d total chains",
        cfg.mvp.num_problems, cfg.sampling.num_chains,
        cfg.mvp.num_problems * cfg.sampling.num_chains,
    )

    report = run_pipeline(cfg)

    print("\n" + "=" * 60)
    print("MVP VERDICT")
    print("=" * 60)
    print(f"  P1 (formalization > 50%):  {report['verdict']['p1']}")
    print(f"  P2 (IC discrimination):    {report['verdict']['p2']}")
    print(f"  Overall:                   {report['verdict']['overall']}")
    print("=" * 60)
    print(f"  SVS accuracy: {report['accuracy']['svs']['accuracy']:.1%}")
    print(f"  SC  accuracy: {report['accuracy']['sc']['accuracy']:.1%}")
    print(f"  Delta:        {report['accuracy']['delta']:+.1%}")
    if "cost" in report:
        cost = report["cost"]
        print(f"  API calls:    {cost['total_calls']}")
        print(f"  Total tokens: {cost['total_tokens']:,} (in={cost['total_input_tokens']:,}, out={cost['total_output_tokens']:,})")
        print(f"  Est. cost:    ${cost['estimated_cost_usd']:.4f}")
    p2 = report["p2_ic_discrimination"]
    if p2["cohens_d"] is not None:
        print(f"  Cohen's d:    {p2['cohens_d']:.4f}")
        print(f"  t-test p:     {p2['ttest_p_value']:.6f}")
        print(f"  M-W p:        {p2['mannwhitney_p_value']:.6f}")
        ci = p2["ci_95"]
        print(f"  95% CI:       [{ci[0]:.4f}, {ci[1]:.4f}]")
        print(f"  Chains:       {p2['n_correct_chains']} correct, {p2['n_incorrect_chains']} incorrect")
    print("=" * 60)


if __name__ == "__main__":
    main()
