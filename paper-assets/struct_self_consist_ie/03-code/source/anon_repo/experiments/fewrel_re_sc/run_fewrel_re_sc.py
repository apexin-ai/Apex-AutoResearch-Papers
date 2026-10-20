#!/usr/bin/env python3
"""FewRel RE Self-Consistency diagnostic experiment.

Adapted from SciERC run_re_sc.py for FewRel dataset.
"""

import argparse
import json
import os
import statistics
import sys
from collections import Counter, defaultdict

import numpy as np

_project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
sys.path.insert(0, _project_root)
sys.path.insert(0, os.path.join(_project_root, "code"))

from sampling import (
    VLLMSampler,
    run_sampling_pipeline,
    load_sampled_results,
    save_sampled_results,
)
from evaluation import (
    per_instance_f1,
    relation_strict_match,
    compute_re_f1,
    _prf,
)
from consistency import (
    fleiss_kappa_surface,
    structural_consistency_soft_jaccard,
    oracle_best_of_n,
    compute_all_consistency_scores,
)
from data_utils import load_uie_jsonl

SUBTASK = "re"

FEWREL_SCHEMA_HINT = (
    "Entity types: ENTITY\n"
    "Relation types: follows, crosses, located in or next to body of water, "
    "competition class, mother, spouse, part of, "
    "original language of film or TV show, child, military rank, "
    "voice type, position played on team / speciality, "
    "member of, constellation, sport, main subject"
)


def relation_key(r: dict) -> tuple:
    return (r["head_start"], r["head_end"], r["tail_start"], r["tail_end"], r["type"])


def consensus_construct_re(inst, high_thresh=0.5, medium_thresh=0.25):
    samples = inst["samples"]
    N = len(samples)
    rel_counts = Counter()
    rel_sample_indices = defaultdict(list)
    rel_repr = {}

    for i, s in enumerate(samples):
        seen = set()
        for r in s.get("relations", []):
            key = relation_key(r)
            if key not in seen:
                rel_counts[key] += 1
                rel_sample_indices[key].append(i)
                seen.add(key)
                if key not in rel_repr:
                    rel_repr[key] = r

    sample_lps = []
    for i, s in enumerate(samples):
        lp = s.get("mean_logprob")
        if lp is None and "logprobs" in inst and i < len(inst["logprobs"]):
            lp = inst["logprobs"][i]
        if lp is not None:
            sample_lps.append(lp)
    instance_median_lp = statistics.median(sample_lps) if sample_lps else 0.0

    consensus = []
    for key, count in rel_counts.items():
        freq = count / N
        if freq > high_thresh:
            consensus.append(rel_repr[key])
        elif freq > medium_thresh:
            contributing_lps = []
            for i in rel_sample_indices[key]:
                lp = samples[i].get("mean_logprob")
                if lp is None and "logprobs" in inst and i < len(inst["logprobs"]):
                    lp = inst["logprobs"][i]
                if lp is not None:
                    contributing_lps.append(lp)
            if contributing_lps:
                mean_lp = statistics.mean(contributing_lps)
                if mean_lp > instance_median_lp:
                    consensus.append(rel_repr[key])

    return consensus


def majority_vote_re(samples, threshold=0.5):
    N = len(samples)
    rel_counts = Counter()
    rel_repr = {}
    for s in samples:
        seen = set()
        for r in s.get("relations", []):
            key = relation_key(r)
            if key not in seen:
                rel_counts[key] += 1
                seen.add(key)
                if key not in rel_repr:
                    rel_repr[key] = r
    return [rel_repr[key] for key, count in rel_counts.items() if count / N >= threshold]


def is_degenerate_re(inst):
    key_sets = set()
    for s in inst["samples"]:
        ks = frozenset(relation_key(r) for r in s.get("relations", []))
        key_sets.add(ks)
    return len(key_sets) == 1


def classify_failure_mode(inst, greedy_f1, construction_f1, kappa):
    degenerate = is_degenerate_re(inst)
    if degenerate:
        return "F1_degeneracy"
    if kappa < 0.3:
        return "F2_low_agreement"
    if kappa >= 0.3 and greedy_f1 < 0.3:
        return "F3_high_agreement_low_quality"
    if construction_f1 - greedy_f1 < -0.05:
        return "F4_lp_quality_gap"
    return None


def evaluate_re_sc(sampled_instances, output_dir, high_thresh=0.5, medium_thresh=0.25):
    N_samples = len(sampled_instances[0]["samples"]) if sampled_instances else 0
    theta = 2 / N_samples if N_samples > 0 else 0.25
    if medium_thresh is None:
        medium_thresh = theta

    results = {
        "n_instances": len(sampled_instances),
        "n_samples": N_samples,
        "high_thresh": high_thresh,
        "medium_thresh": medium_thresh,
        "dataset": "fewrel",
    }

    greedy_f1s, construction_f1s, majority_f1s, oracle_f1s = [], [], [], []
    kappas, soft_jaccards, degen_flags = [], [], []
    failure_modes = []

    for inst in sampled_instances:
        gold = inst["gold"]
        samples = inst["samples"]
        greedy = inst.get("greedy", samples[0])

        g_f1 = per_instance_f1(greedy, gold, subtask=SUBTASK)
        greedy_f1s.append(g_f1)

        c_rels = consensus_construct_re(inst, high_thresh, medium_thresh)
        c_f1 = per_instance_f1({"relations": c_rels}, gold, subtask=SUBTASK)
        construction_f1s.append(c_f1)

        mv_rels = majority_vote_re(samples, threshold=0.5)
        mv_f1 = per_instance_f1({"relations": mv_rels}, gold, subtask=SUBTASK)
        majority_f1s.append(mv_f1)

        _, o_f1 = oracle_best_of_n(samples, gold, subtask=SUBTASK)
        oracle_f1s.append(o_f1)

        kappa = fleiss_kappa_surface(samples, subtask=SUBTASK)
        kappas.append(kappa)

        sj = structural_consistency_soft_jaccard(samples, subtask=SUBTASK)
        soft_jaccards.append(sj)

        degen = is_degenerate_re(inst)
        degen_flags.append(degen)

        fm = classify_failure_mode(inst, g_f1, c_f1, kappa)
        failure_modes.append(fm)

    n = len(sampled_instances)
    results["greedy_f1_mean"] = float(np.mean(greedy_f1s))
    results["construction_f1_mean"] = float(np.mean(construction_f1s))
    results["majority_vote_f1_mean"] = float(np.mean(majority_f1s))
    results["oracle_f1_mean"] = float(np.mean(oracle_f1s))
    results["fleiss_kappa_mean"] = float(np.mean(kappas))
    results["soft_jaccard_mean"] = float(np.mean(soft_jaccards))

    n_degen = sum(degen_flags)
    results["degeneracy_rate"] = n_degen / n if n > 0 else 0.0
    results["n_degenerate"] = n_degen
    results["n_nondegenerate"] = n - n_degen

    greedy_preds = [inst.get("greedy", inst["samples"][0]) for inst in sampled_instances]
    golds = [inst["gold"] for inst in sampled_instances]
    results["greedy_micro_f1"] = compute_re_f1(greedy_preds, golds)

    construction_preds = []
    for inst in sampled_instances:
        construction_preds.append({"relations": consensus_construct_re(inst, high_thresh, medium_thresh)})
    results["construction_micro_f1"] = compute_re_f1(construction_preds, golds)

    fm_counts = Counter()
    for fm in failure_modes:
        fm_counts[fm or "none"] += 1
    results["failure_modes"] = dict(fm_counts)
    results["failure_mode_pcts"] = {k: v / n * 100 for k, v in fm_counts.items()} if n > 0 else {}

    if n - n_degen > 0:
        nd_mask = [not d for d in degen_flags]
        nd_greedy = [f for f, m in zip(greedy_f1s, nd_mask) if m]
        nd_construction = [f for f, m in zip(construction_f1s, nd_mask) if m]
        results["nondegen_greedy_f1_mean"] = float(np.mean(nd_greedy))
        results["nondegen_construction_f1_mean"] = float(np.mean(nd_construction))
        results["nondegen_diff"] = results["nondegen_construction_f1_mean"] - results["nondegen_greedy_f1_mean"]

    results["bootstrap"] = run_bootstrap_re(greedy_f1s, construction_f1s, degen_flags)

    per_instance = []
    for i, inst in enumerate(sampled_instances):
        per_instance.append({
            "id": inst["id"],
            "greedy_f1": greedy_f1s[i],
            "construction_f1": construction_f1s[i],
            "majority_vote_f1": majority_f1s[i],
            "oracle_f1": oracle_f1s[i],
            "fleiss_kappa": kappas[i],
            "soft_jaccard": soft_jaccards[i],
            "degenerate": degen_flags[i],
            "failure_mode": failure_modes[i],
            "n_gold_relations": len(inst["gold"].get("relations", [])),
        })

    os.makedirs(output_dir, exist_ok=True)
    with open(os.path.join(output_dir, "re_sc_results.json"), "w") as f:
        json.dump(results, f, indent=2)
    with open(os.path.join(output_dir, "re_per_instance.json"), "w") as f:
        json.dump(per_instance, f, indent=2)

    print_summary(results)
    return results


def run_bootstrap_re(greedy_f1s, construction_f1s, degen_flags, B=10000, seed=42):
    rng = np.random.RandomState(seed)
    n = len(greedy_f1s)
    greedy_arr = np.array(greedy_f1s)
    construction_arr = np.array(construction_f1s)
    diffs = construction_arr - greedy_arr
    obs_diff = float(diffs.mean())

    boot_diffs = np.zeros(B)
    for b in range(B):
        idx = rng.randint(0, n, n)
        boot_diffs[b] = diffs[idx].mean()
    boot_diffs.sort()

    ci_lo = float(boot_diffs[int(0.025 * B)])
    ci_hi = float(boot_diffs[int(0.975 * B)])
    p_value = float(np.mean(boot_diffs <= 0))

    std_diff = float(diffs.std(ddof=1))
    cohens_d = obs_diff / std_diff if std_diff > 0 else float("inf")

    result = {
        "observed_diff": obs_diff,
        "ci_95": [ci_lo, ci_hi],
        "p_value": p_value,
        "cohens_d": cohens_d,
        "B": B,
        "n_positive": int(np.sum(diffs > 0)),
        "n_negative": int(np.sum(diffs < 0)),
        "n_tied": int(np.sum(diffs == 0)),
    }

    degen_arr = np.array(degen_flags, dtype=bool)
    nd_mask = ~degen_arr
    if nd_mask.sum() > 0:
        nd_diffs = diffs[nd_mask]
        nd_n = nd_diffs.shape[0]
        nd_boot = np.zeros(B)
        for b in range(B):
            idx = rng.randint(0, nd_n, nd_n)
            nd_boot[b] = nd_diffs[idx].mean()
        nd_boot.sort()
        result["nondegen_observed_diff"] = float(nd_diffs.mean())
        result["nondegen_ci_95"] = [float(nd_boot[int(0.025 * B)]), float(nd_boot[int(0.975 * B)])]
        result["nondegen_p_value"] = float(np.mean(nd_boot <= 0))

    return result


def print_summary(results):
    n = results["n_instances"]
    print(f"\n{'='*60}")
    print(f"  FewRel RE Self-Consistency Diagnostic — {n} instances")
    print(f"{'='*60}")
    print(f"Greedy F1 (mean):         {results['greedy_f1_mean']:.4f}")
    print(f"Construction F1 (mean):   {results['construction_f1_mean']:.4f}")
    print(f"Majority Vote F1 (mean):  {results['majority_vote_f1_mean']:.4f}")
    print(f"Oracle F1 (mean):         {results['oracle_f1_mean']:.4f}")
    print(f"Fleiss' kappa (mean):     {results['fleiss_kappa_mean']:.4f}")
    print(f"Soft Jaccard (mean):      {results['soft_jaccard_mean']:.4f}")
    print(f"Degeneracy rate:          {results['degeneracy_rate']:.2%} ({results['n_degenerate']}/{n})")

    micro = results.get("greedy_micro_f1", {})
    print(f"\nMicro-avg greedy:         P={micro.get('precision',0):.4f} R={micro.get('recall',0):.4f} F1={micro.get('f1',0):.4f}")
    micro_c = results.get("construction_micro_f1", {})
    print(f"Micro-avg construction:   P={micro_c.get('precision',0):.4f} R={micro_c.get('recall',0):.4f} F1={micro_c.get('f1',0):.4f}")

    if "nondegen_diff" in results:
        print(f"\nNon-degen greedy F1:      {results['nondegen_greedy_f1_mean']:.4f}")
        print(f"Non-degen construction:   {results['nondegen_construction_f1_mean']:.4f}")
        print(f"Non-degen diff:           {results['nondegen_diff']:+.4f}")

    print(f"\nFailure mode distribution:")
    for mode, pct in sorted(results.get("failure_mode_pcts", {}).items()):
        print(f"  {mode}: {pct:.1f}%")

    boot = results.get("bootstrap", {})
    if boot:
        print(f"\nBootstrap (B={boot.get('B', 10000)}):")
        print(f"  Diff: {boot.get('observed_diff', 0):+.4f}")
        ci = boot.get("ci_95", [0, 0])
        print(f"  95% CI: [{ci[0]:+.4f}, {ci[1]:+.4f}]")
        print(f"  p-value: {boot.get('p_value', 1):.4f}")


def main():
    parser = argparse.ArgumentParser(description="FewRel RE Self-Consistency Diagnostic")
    parser.add_argument("--model-path", default=None)
    parser.add_argument("--data", default=None)
    parser.add_argument("--samples", default=None)
    parser.add_argument("--output-dir", required=True)
    parser.add_argument("--eval-only", action="store_true")
    parser.add_argument("--n-samples", type=int, default=8)
    parser.add_argument("--temperature", type=float, default=1.0)
    parser.add_argument("--max-tokens", type=int, default=1024)
    parser.add_argument("--tensor-parallel", type=int, default=1)
    parser.add_argument("--high-thresh", type=float, default=0.5)
    parser.add_argument("--medium-thresh", type=float, default=None)
    args = parser.parse_args()

    if args.eval_only:
        if not args.samples:
            parser.error("--samples required when --eval-only is set")
        sampled = load_sampled_results(args.samples)
    else:
        if not args.model_path or not args.data:
            parser.error("--model-path and --data required for sampling")

        instances = load_uie_jsonl(args.data)
        print(f"Loaded {len(instances)} FewRel RE instances")

        sampler = VLLMSampler(
            model_path=args.model_path,
            tensor_parallel_size=args.tensor_parallel,
            max_model_len=4096,
            gpu_memory_utilization=0.90,
        )

        sampled = run_sampling_pipeline(
            sampler=sampler,
            instances=instances,
            n_samples=args.n_samples,
            temperature=args.temperature,
            max_tokens=args.max_tokens,
            subtask="re",
            schema_hint=FEWREL_SCHEMA_HINT,
            use_grammar=True,
            use_chat_template=True,
            use_train_format=False,
            output_path=os.path.join(args.output_dir, "re_samples.jsonl"),
            realign=True,
            collect_logprobs=True,
        )
        print(f"Sampled {len(sampled)} instances x {args.n_samples} samples")

    evaluate_re_sc(
        sampled,
        output_dir=args.output_dir,
        high_thresh=args.high_thresh,
        medium_thresh=args.medium_thresh,
    )


if __name__ == "__main__":
    main()
