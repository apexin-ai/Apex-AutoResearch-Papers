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

from data_utils import load_scierc, load_ace05, load_conll2003, load_wnut17, load_fewnerd
from sampling import (
    VLLMSampler,
    run_sampling_pipeline,
    save_sampled_results,
    load_sampled_results,
    realign_spans,
    SCIERC_SCHEMA_HINT,
    CONLL2003_SCHEMA_HINT,
    WNUT17_SCHEMA_HINT,
    FEWNERD_SCHEMA_HINT,
)
from consistency import compute_all_consistency_scores
from evaluation import (
    per_instance_f1,
    compute_ner_f1,
    compute_re_f1,
    compute_eae_f1,
    spearman_correlation,
    kendall_correlation,
    compute_auroc,
    compute_sample_f1_distribution,
)


def parse_args() -> argparse.Namespace:
    """Parse command-line arguments."""
    p = argparse.ArgumentParser(description="MVP pilot for structured self-consistency IE")
    p.add_argument("--model_path", type=str, required=True, help="Path to the fine-tuned model")
    p.add_argument("--data_dir", type=str, required=True, help="Dataset directory (SciERC or ACE05)")
    p.add_argument("--dataset", type=str, default="scierc", choices=["scierc", "ace05", "conll2003", "wnut17", "fewnerd"],
                   help="Dataset name (default: scierc)")
    p.add_argument("--subtask", type=str, default="ner", choices=["ner", "re", "eae", "joint"],
                   help="Subtask (default: ner)")
    p.add_argument("--schema_hint", type=str, default="",
                   help="Schema hint string (entity/relation types). Auto-set for scierc if empty")
    p.add_argument("--use_train_format", type=lambda x: x.lower() != "false", default=True,
                   help="Use train-aligned prompt template (default: True)")
    p.add_argument("--n_samples", type=int, default=8, help="Number of samples per instance (default: 8)")
    p.add_argument("--temperature", type=float, default=1.0, help="Sampling temperature (default: 1.0)")
    p.add_argument("--max_tokens", type=int, default=1024, help="Max generation tokens (default: 1024)")
    p.add_argument("--output_dir", type=str, default="output", help="Output directory (default: output)")
    p.add_argument("--num_test", type=int, default=99999, help="Max test instances (default: 99999, i.e. use all)")
    p.add_argument("--seed", type=int, default=42, help="Random seed (default: 42)")
    p.add_argument("--tensor_parallel", type=int, default=1, help="vLLM tensor parallel size (default: 1)")
    p.add_argument("--skip_sampling", action="store_true", help="Skip sampling, load from existing results")
    p.add_argument("--samples_path", type=str, default=None,
                   help="Path to existing sampling results (used with --skip_sampling)")
    p.add_argument("--no_realign", action="store_true",
                   help="Disable span realignment post-processing (default: realign enabled)")
    p.add_argument("--collect_logprobs", action="store_true",
                   help="Collect per-sample log-probabilities during generation")
    p.add_argument("--use_grammar", type=lambda x: x.lower() != "false", default=True,
                   help="Use XGrammar constrained decoding (default: True)")
    p.add_argument("--start_index", type=int, default=0, help="Start index for data sharding (inclusive)")
    p.add_argument("--end_index", type=int, default=None, help="End index for data sharding (exclusive)")
    return p.parse_args()


def _print_subtask_block(report: dict, prefix: str = "") -> None:
    """Print metrics block for a single subtask."""
    p = prefix
    print(f"  Greedy F1:      {report[f'{p}greedy_f1']:.4f}")
    print(f"  Oracle F1:      {report[f'{p}oracle_f1']:.4f}")
    print(f"  Oracle headroom:{report[f'{p}oracle_headroom']:+.4f}")
    print("-" * 60)
    print(f"  Fleiss' kappa (mean):    {report[f'{p}fleiss_kappa_mean']:.4f}")
    print(f"  Soft Jaccard (mean):     {report[f'{p}soft_jaccard_mean']:.4f}")
    print("-" * 60)
    print(f"  Sample F1 (mean):        {report[f'{p}sample_f1_mean']:.4f}")
    print(f"  Sample F1 (std):         {report[f'{p}sample_f1_std']:.4f}")
    print(f"  Sample F1=0 (%):         {report[f'{p}sample_f1_pct_zero']:.1f}%")
    print("-" * 60)
    n_empty = report.get(f"{p}n_gold_empty_filtered", 0)
    n_zero = report.get(f"{p}n_greedy_f1_zero_filtered", 0)
    print(f"  Gold-empty filtered:     {n_empty}")
    print(f"  All-samples-F1=0 filtered: {n_zero}")
    print("-" * 60)
    fk_full = report[f"{p}correlation_fleiss_vs_f1_full"]
    sj_full = report[f"{p}correlation_softjaccard_vs_f1_full"]
    fk_cond = report[f"{p}correlation_fleiss_vs_f1_conditional"]
    sj_cond = report[f"{p}correlation_softjaccard_vs_f1_conditional"]
    print(f"  Full ρ(κ,F1):   {fk_full['rho']:+.4f}  p={fk_full['p_value']:.4e}  n={fk_full['n']}")
    print(f"  Full ρ(SJ,F1):  {sj_full['rho']:+.4f}  p={sj_full['p_value']:.4e}  n={sj_full['n']}")
    print(f"  Cond ρ(κ,F1):   {fk_cond['rho']:+.4f}  p={fk_cond['p_value']:.4e}  n={fk_cond['n']}")
    print(f"  Cond ρ(SJ,F1):  {sj_cond['rho']:+.4f}  p={sj_cond['p_value']:.4e}  n={sj_cond['n']}")
    if fk_cond['n'] < 30:
        print(f"  ⚠️ Conditional n={fk_cond['n']} < 30, ρ may be unreliable")
    beats = "YES" if report[f"{p}structural_beats_surface"] else "NO"
    print(f"  Structural > Surface:    {beats}  (delta={report[f'{p}rho_advantage']:+.4f})")
    lp = report.get(f"{p}logprob_baseline")
    if lp:
        print("-" * 60)
        print(f"  Logprob (full):  ρ={lp['full']['rho']:+.4f}  τ={lp['full']['tau']:+.4f}  AUROC={lp['full']['auroc']:.4f}")
        print(f"  Logprob (cond):  ρ={lp['conditional']['rho']:+.4f}  τ={lp['conditional']['tau']:+.4f}  AUROC={lp['conditional']['auroc']:.4f}")


def print_report(report: dict) -> None:
    """Pretty-print the experiment report to stdout."""
    print("\n" + "=" * 60)
    print("  Structured Self-Consistency IE — MVP Pilot Report")
    print("=" * 60)
    print(f"  Dataset:        {report['dataset']} / {report['subtask']}")
    print(f"  Instances:      {report['num_instances']}")
    print(f"  Samples/inst:   {report['n_samples']}")
    print(f"  Temperature:    {report['temperature']}")
    print(f"  Train format:   {report.get('use_train_format', 'N/A')}")
    print("-" * 60)

    if report["subtask"] == "joint":
        for st in ["ner", "re"]:
            print(f"\n  >>> {st.upper()} <<<")
            _print_subtask_block(report, prefix=f"{st}_")
            print()
    else:
        _print_subtask_block(report, prefix="")

    print("-" * 60)
    print(f"  Verdict:        {report['verdict']}")
    if "warning" in report:
        print(f"  {report['warning']}")
    print(f"  Note:           {report['verdict_note']}")
    print("=" * 60 + "\n")


def main() -> None:
    args = parse_args()

    random.seed(args.seed)
    np.random.seed(args.seed)

    os.makedirs(args.output_dir, exist_ok=True)

    # Resolve schema hint
    if args.schema_hint:
        schema = args.schema_hint
    elif args.use_train_format:
        schema = {
            'scierc': SCIERC_SCHEMA_HINT,
            'conll2003': CONLL2003_SCHEMA_HINT,
            'wnut17': WNUT17_SCHEMA_HINT,
            'fewnerd': FEWNERD_SCHEMA_HINT,
        }.get(args.dataset, '')
    else:
        schema = ""

    # --- 1. Load data ---
    load_subtask = args.subtask if args.subtask != "joint" else "ner"
    if args.dataset == "scierc":
        data = load_scierc(args.data_dir)
    elif args.dataset == "conll2003":
        data = load_conll2003(args.data_dir)
    elif args.dataset == "wnut17":
        data = load_wnut17(args.data_dir)
    elif args.dataset == "fewnerd":
        data = load_fewnerd(args.data_dir)
    else:
        data = load_ace05(args.data_dir, subtask=load_subtask)

    test_instances = data["test"][:args.num_test]
    test_instances = test_instances[args.start_index:args.end_index]
    print(f"Loaded {len(test_instances)} test instances from {args.dataset} [index {args.start_index}:{args.end_index}]")

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
            subtask=args.subtask if args.subtask != "joint" else "full",
            schema_hint=schema,
            use_train_format=args.use_train_format,
            use_grammar=args.use_grammar,
            output_path=samples_out,
            realign=not args.no_realign,
            collect_logprobs=args.collect_logprobs,
            seed=args.seed,
        )
        print(f"Sampling complete. Saved to {samples_out}")

    greedy_preds = [inst["greedy"] for inst in sampled]
    golds = [inst["gold"] for inst in sampled]

    # Determine which subtasks to evaluate
    eval_subtasks = ["ner", "re"] if args.subtask == "joint" else [args.subtask]

    # --- Per-subtask evaluation ---
    subtask_reports = {}
    for st in eval_subtasks:
        consistency = compute_all_consistency_scores(sampled, subtask=st)

        # Filter gold-empty instances for sample F1 distribution
        if st == "ner":
            _nonempty = [inst for inst in sampled if len(inst["gold"].get("entities", [])) > 0]
        elif st == "re":
            _nonempty = [inst for inst in sampled if len(inst["gold"].get("relations", [])) > 0]
        else:
            _nonempty = sampled
        sample_f1_dist = compute_sample_f1_distribution(_nonempty, subtask=st)

        f1_fn = {"ner": compute_ner_f1, "re": compute_re_f1, "eae": compute_eae_f1}[st]
        greedy_metrics = f1_fn(greedy_preds, golds)
        oracle_preds = []
        for inst in sampled:
            best = max(inst["samples"], key=lambda s: per_instance_f1(s, inst["gold"], st))
            oracle_preds.append(best)
        oracle_metrics = f1_fn(oracle_preds, golds)

        greedy_f1 = greedy_metrics["f1"]
        oracle_f1 = oracle_metrics["f1"]
        oracle_headroom = oracle_f1 - greedy_f1

        instance_f1s = [per_instance_f1(pred, gold, subtask=st)
                        for pred, gold in zip(greedy_preds, golds)]

        # Filter gold-empty instances for correlation
        if st == "ner":
            nonempty_mask = [len(inst["gold"].get("entities", [])) > 0 for inst in sampled]
        elif st == "re":
            nonempty_mask = [len(inst["gold"].get("relations", [])) > 0 for inst in sampled]
        else:
            nonempty_mask = [True] * len(sampled)

        filtered_fk = [s for s, m in zip(consistency["fleiss_kappa"], nonempty_mask) if m]
        filtered_sj = [s for s, m in zip(consistency["soft_jaccard"], nonempty_mask) if m]
        filtered_f1s = [f for f, m in zip(instance_f1s, nonempty_mask) if m]
        n_gold_empty = sum(1 for m in nonempty_mask if not m)

        # Full ρ: on gold-nonempty instances
        rho_fk, p_fk = spearman_correlation(filtered_fk, filtered_f1s)
        rho_sj, p_sj = spearman_correlation(filtered_sj, filtered_f1s)

        # Conditional ρ: exclude greedy_F1=0 instances (knowledge-gap)
        cond_mask = [nonempty_mask[i] and instance_f1s[i] > 0 for i in range(len(sampled))]

        cond_fk = [s for s, m in zip(consistency["fleiss_kappa"], cond_mask) if m]
        cond_sj = [s for s, m in zip(consistency["soft_jaccard"], cond_mask) if m]
        cond_f1s = [f for f, m in zip(instance_f1s, cond_mask) if m]
        n_all_zero = sum(1 for ne, c in zip(nonempty_mask, cond_mask) if ne and not c)
        n_cond = len(cond_f1s)

        rho_fk_cond, p_fk_cond = spearman_correlation(cond_fk, cond_f1s) if n_cond >= 3 else (0.0, 1.0)
        rho_sj_cond, p_sj_cond = spearman_correlation(cond_sj, cond_f1s) if n_cond >= 3 else (0.0, 1.0)

        subtask_reports[st] = {
            "greedy_f1": greedy_f1,
            "oracle_f1": oracle_f1,
            "oracle_headroom": oracle_headroom,
            "fleiss_kappa_mean": float(np.mean(consistency["fleiss_kappa"])),
            "soft_jaccard_mean": float(np.mean(consistency["soft_jaccard"])),
            "correlation_fleiss_vs_f1_full": {"rho": rho_fk, "p_value": p_fk, "n": len(filtered_f1s)},
            "correlation_softjaccard_vs_f1_full": {"rho": rho_sj, "p_value": p_sj, "n": len(filtered_f1s)},
            "correlation_fleiss_vs_f1_conditional": {"rho": rho_fk_cond, "p_value": p_fk_cond, "n": n_cond},
            "correlation_softjaccard_vs_f1_conditional": {"rho": rho_sj_cond, "p_value": p_sj_cond, "n": n_cond},
            "n_gold_empty_filtered": n_gold_empty,
            "n_greedy_f1_zero_filtered": n_all_zero,
            "structural_beats_surface": rho_sj > rho_fk,
            "rho_advantage": rho_sj - rho_fk,
            "sample_f1_mean": sample_f1_dist["mean"],
            "sample_f1_std": sample_f1_dist["std"],
            "sample_f1_pct_zero": sample_f1_dist["pct_f1_zero"],
        }

        has_logprobs = sampled and "logprobs" in sampled[0]
        if has_logprobs:
            instance_mean_lps = [float(np.mean(inst["logprobs"])) for inst in sampled]
            filtered_lps = [lp for lp, m in zip(instance_mean_lps, nonempty_mask) if m]
            cond_lps = [lp for lp, m in zip(instance_mean_lps, cond_mask) if m]

            rho_lp, p_lp = spearman_correlation(filtered_lps, filtered_f1s)
            tau_lp, p_tau_lp = kendall_correlation(filtered_lps, filtered_f1s)
            auroc_lp = compute_auroc(filtered_lps, filtered_f1s)

            rho_lp_c, p_lp_c = spearman_correlation(cond_lps, cond_f1s) if n_cond >= 3 else (0.0, 1.0)
            tau_lp_c, p_tau_c = kendall_correlation(cond_lps, cond_f1s) if n_cond >= 3 else (0.0, 1.0)
            auroc_lp_c = compute_auroc(cond_lps, cond_f1s) if n_cond >= 3 else 0.5

            subtask_reports[st]["logprob_baseline"] = {
                "full": {"rho": rho_lp, "p_rho": p_lp, "tau": tau_lp, "p_tau": p_tau_lp, "auroc": auroc_lp, "n": len(filtered_lps)},
                "conditional": {"rho": rho_lp_c, "p_rho": p_lp_c, "tau": tau_lp_c, "p_tau": p_tau_c, "auroc": auroc_lp_c, "n": n_cond},
            }

    # --- Verdict: RE subtask's structural ρ is the primary signal ---
    re_report = subtask_reports.get("re", subtask_reports.get(args.subtask))
    re_rho = re_report["correlation_softjaccard_vs_f1_full"]["rho"]
    re_beats = re_report["structural_beats_surface"]
    any_headroom = any(sr["oracle_headroom"] >= 0.02 for sr in subtask_reports.values())

    if re_rho >= 0.40 and re_beats and any_headroom:
        verdict = "PASS"
    elif re_rho >= 0.30:
        verdict = "MARGINAL"
    else:
        verdict = "FAIL"

    # --- Build report ---
    if args.subtask == "joint":
        report = {
            "dataset": args.dataset,
            "subtask": "joint",
            "n_samples": args.n_samples,
            "temperature": args.temperature,
            "num_instances": len(sampled),
            "use_train_format": args.use_train_format,
        }
        for st, st_report in subtask_reports.items():
            for k, v in st_report.items():
                report[f"{st}_{k}"] = v
        report["verdict"] = verdict
        report["verdict_note"] = "Joint mode: verdict requires RE ρ_sj ≥ 0.40 AND ρ_sj > ρ_fk AND any subtask headroom ≥ 2pp"
    else:
        st_report = subtask_reports[args.subtask]
        report = {
            "dataset": args.dataset,
            "subtask": args.subtask,
            "n_samples": args.n_samples,
            "temperature": args.temperature,
            "num_instances": len(sampled),
            "use_train_format": args.use_train_format,
            **st_report,
            "verdict": verdict,
            "verdict_note": "MVP verdict on single subtask; final pass requires at least one of NER/RE/EAE to meet threshold",
        }

    worst_pct_zero = max(sr["sample_f1_pct_zero"] for sr in subtask_reports.values())
    if worst_pct_zero > 30:
        report["warning"] = "⚠️ >30% samples F1=0, recommend re-running at T=0.7"

    print_report(report)

    report_path = os.path.join(args.output_dir, "report.json")
    with open(report_path, "w", encoding="utf-8") as f:
        json.dump(report, f, indent=2, ensure_ascii=False)
    print(f"Report saved to {report_path}")


if __name__ == "__main__":
    main()
