"""MVP pilot experiment script for structured self-consistency IE.

Integrates data loading, vLLM sampling, consistency scoring, and evaluation
into a single CLI-driven pipeline. Outputs a verdict (PASS/MARGINAL/FAIL)
based on the correlation between structural consistency and per-instance F1.
"""

from __future__ import annotations

import argparse
import json
import os
import random
import sys

import numpy as np

from data_utils import load_scierc, load_ace05
from sampling import (
    VLLMSampler,
    run_sampling_pipeline,
    save_sampled_results,
    load_sampled_results,
)
from consistency import compute_all_consistency_scores
from evaluation import (
    per_instance_f1,
    compute_ner_f1,
    compute_eae_f1,
    spearman_correlation,
)


def parse_args() -> argparse.Namespace:
    """Parse command-line arguments."""
    p = argparse.ArgumentParser(description="MVP pilot for structured self-consistency IE")
    p.add_argument("--model_path", type=str, required=True, help="Path to the fine-tuned model")
    p.add_argument("--data_dir", type=str, required=True, help="Dataset directory (SciERC or ACE05)")
    p.add_argument("--dataset", type=str, default="scierc", choices=["scierc", "ace05"],
                   help="Dataset name (default: scierc)")
    p.add_argument("--subtask", type=str, default="ner", choices=["ner", "eae"],
                   help="Subtask (default: ner)")
    p.add_argument("--n_samples", type=int, default=8, help="Number of samples per instance (default: 8)")
    p.add_argument("--temperature", type=float, default=1.0, help="Sampling temperature (default: 1.0)")
    p.add_argument("--max_tokens", type=int, default=512, help="Max generation tokens (default: 512)")
    p.add_argument("--output_dir", type=str, default="output", help="Output directory (default: output)")
    p.add_argument("--num_test", type=int, default=200, help="Max test instances (default: 200)")
    p.add_argument("--seed", type=int, default=42, help="Random seed (default: 42)")
    p.add_argument("--tensor_parallel", type=int, default=1, help="vLLM tensor parallel size (default: 1)")
    p.add_argument("--skip_sampling", action="store_true", help="Skip sampling, load from existing results")
    p.add_argument("--samples_path", type=str, default=None,
                   help="Path to existing sampling results (used with --skip_sampling)")
    return p.parse_args()


def print_report(report: dict) -> None:
    """Pretty-print the experiment report to stdout.

    Args:
        report: Report dict produced by main().
    """
    print("\n" + "=" * 60)
    print("  Structured Self-Consistency IE — MVP Pilot Report")
    print("=" * 60)
    print(f"  Dataset:        {report['dataset']} / {report['subtask']}")
    print(f"  Instances:      {report['num_instances']}")
    print(f"  Samples/inst:   {report['n_samples']}")
    print(f"  Temperature:    {report['temperature']}")
    print("-" * 60)
    print(f"  Greedy F1:      {report['greedy_f1']:.4f}")
    print(f"  Oracle F1:      {report['oracle_f1']:.4f}")
    print(f"  Oracle headroom:{report['oracle_headroom']:+.4f}")
    print("-" * 60)
    print(f"  Fleiss' kappa (mean):    {report['fleiss_kappa_mean']:.4f}")
    print(f"  Soft Jaccard (mean):     {report['soft_jaccard_mean']:.4f}")
    print("-" * 60)

    corr_fk = report["correlation_fleiss_vs_f1"]
    corr_sj = report["correlation_softjaccard_vs_f1"]
    print(f"  Corr(fleiss_kappa, F1):  rho={corr_fk['rho']:+.4f}  p={corr_fk['p_value']:.4e}")
    print(f"  Corr(soft_jaccard, F1):  rho={corr_sj['rho']:+.4f}  p={corr_sj['p_value']:.4e}")
    print("-" * 60)
    print(f"  Verdict:        {report['verdict']}")
    print("=" * 60 + "\n")


def main() -> None:
    args = parse_args()

    random.seed(args.seed)
    np.random.seed(args.seed)

    os.makedirs(args.output_dir, exist_ok=True)

    # --- 1. Load data ---
    if args.dataset == "scierc":
        data = load_scierc(args.data_dir)
    else:
        data = load_ace05(args.data_dir, subtask=args.subtask)

    test_instances = data["test"][:args.num_test]
    print(f"Loaded {len(test_instances)} test instances from {args.dataset}")

    # --- 2. Sampling (or load existing) ---
    if args.skip_sampling:
        if not args.samples_path:
            print("ERROR: --samples_path required when using --skip_sampling", file=sys.stderr)
            sys.exit(1)
        sampled = load_sampled_results(args.samples_path)
        print(f"Loaded {len(sampled)} sampled instances from {args.samples_path}")
    else:
        sampler = VLLMSampler(
            args.model_path,
            tensor_parallel_size=args.tensor_parallel,
        )
        samples_out = os.path.join(args.output_dir, "samples.jsonl")
        sampled = run_sampling_pipeline(
            sampler,
            test_instances,
            n_samples=args.n_samples,
            temperature=args.temperature,
            max_tokens=args.max_tokens,
            subtask=args.subtask,
            output_path=samples_out,
        )
        print(f"Sampling complete. Saved to {samples_out}")

    # --- 3. Consistency scores ---
    consistency = compute_all_consistency_scores(sampled, subtask=args.subtask)

    # --- 4. Evaluation metrics ---
    greedy_preds = [inst["greedy"] for inst in sampled]
    golds = [inst["gold"] for inst in sampled]

    if args.subtask == "ner":
        greedy_metrics = compute_ner_f1(greedy_preds, golds)
        oracle_preds = []
        for inst in sampled:
            best = max(inst["samples"], key=lambda s: per_instance_f1(s, inst["gold"], "ner"))
            oracle_preds.append(best)
        oracle_metrics = compute_ner_f1(oracle_preds, golds)
    else:
        greedy_metrics = compute_eae_f1(greedy_preds, golds)
        oracle_preds = []
        for inst in sampled:
            best = max(inst["samples"], key=lambda s: per_instance_f1(s, inst["gold"], "eae"))
            oracle_preds.append(best)
        oracle_metrics = compute_eae_f1(oracle_preds, golds)

    greedy_f1 = greedy_metrics["f1"]
    oracle_f1 = oracle_metrics["f1"]
    oracle_headroom = oracle_f1 - greedy_f1

    instance_f1s = [per_instance_f1(pred, gold, subtask=args.subtask)
                    for pred, gold in zip(greedy_preds, golds)]

    # --- 5. Correlation analysis ---
    rho_fk, p_fk = spearman_correlation(consistency["fleiss_kappa"], instance_f1s)
    rho_sj, p_sj = spearman_correlation(consistency["soft_jaccard"], instance_f1s)

    rho_structural = max(rho_fk, rho_sj)

    # --- 6. Pass/Fail verdict ---
    if rho_structural >= 0.40 and oracle_headroom >= 0.02:
        verdict = "PASS"
    elif rho_structural >= 0.30:
        verdict = "MARGINAL"
    else:
        verdict = "FAIL"

    # --- 7. Report ---
    report = {
        "dataset": args.dataset,
        "subtask": args.subtask,
        "n_samples": args.n_samples,
        "temperature": args.temperature,
        "num_instances": len(sampled),
        "greedy_f1": greedy_f1,
        "oracle_f1": oracle_f1,
        "oracle_headroom": oracle_headroom,
        "fleiss_kappa_mean": float(np.mean(consistency["fleiss_kappa"])),
        "soft_jaccard_mean": float(np.mean(consistency["soft_jaccard"])),
        "correlation_fleiss_vs_f1": {"rho": rho_fk, "p_value": p_fk},
        "correlation_softjaccard_vs_f1": {"rho": rho_sj, "p_value": p_sj},
        "verdict": verdict,
    }

    print_report(report)

    report_path = os.path.join(args.output_dir, "report.json")
    with open(report_path, "w", encoding="utf-8") as f:
        json.dump(report, f, indent=2, ensure_ascii=False)
    print(f"Report saved to {report_path}")


if __name__ == "__main__":
    main()
