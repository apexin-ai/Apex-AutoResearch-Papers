"""N-scaling analysis for pretrained FewNERD: N=8/16/32 comparison.

Computes greedy F1, MV F1, LP-selection F1, oracle F1, degeneracy rate,
capture rate, and SJ rho on gold-nonempty instances (micro-averaged).

Usage:
    python analyze_n32.py --input samples.jsonl [--n_samples 32] [--compute_sj]
"""

import json
import argparse
import sys
import os
from collections import Counter

import numpy as np
from scipy.stats import spearmanr

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from unified_metrics import (
    compute_entity_f1, compute_sample_f1s,
    get_lp_selection_idx, bootstrap_delta_ci,
)

# N=8 and N=16 pretrained FewNERD reference values (gold-nonempty, micro-avg)
REF = {
    8:  {"greedy": 0.538, "mv_delta": 3.9, "degen": 11.7, "oracle_delta": 11.2, "capture": 36, "sj_rho": 0.436},
    16: {"greedy": 0.537, "mv_delta": 4.1, "degen": 7.6,  "oracle_delta": 14.1, "capture": 29, "sj_rho": 0.453},
}


def load_gold_nonempty(path):
    instances = []
    with open(path) as f:
        for line in f:
            if not line.strip():
                continue
            obj = json.loads(line)
            if obj["gold"].get("entities", []):
                instances.append(obj)
    return instances


def entity_strict_counts(pred_entities, gold_entities):
    pred_set = {(e["start"], e["end"], e["type"]) for e in pred_entities}
    gold_set = {(e["start"], e["end"], e["type"]) for e in gold_entities}
    tp = len(pred_set & gold_set)
    return tp, len(pred_set) - tp, len(gold_set) - tp


def micro_f1(tp, fp, fn):
    p = tp / (tp + fp) if (tp + fp) > 0 else 0
    r = tp / (tp + fn) if (tp + fn) > 0 else 0
    return 2 * p * r / (p + r) if (p + r) > 0 else 0


def majority_vote_entities(samples, threshold_frac=0.5):
    """Strict MV: vote on (start, end, type) to match entity_strict_counts evaluation."""
    N = len(samples)
    threshold = N * threshold_frac
    counter = Counter()
    key_to_entity = {}

    for s in samples:
        for e in s.get("entities", []):
            key = (e["start"], e["end"], e["type"])
            counter[key] += 1
            key_to_entity[key] = e

    consensus = []
    for key, count in counter.items():
        if count > threshold:
            consensus.append(key_to_entity[key])
    return consensus


def analyze(instances, n_samples=None, compute_sj=False):
    greedy_tp = greedy_fp = greedy_fn = 0
    mv_tp = mv_fp = mv_fn = 0
    lp_tp = lp_fp = lp_fn = 0
    oracle_tp = oracle_fp = oracle_fn = 0

    n_degen_keyset = 0
    per_inst_greedy = []
    per_inst_oracle = []
    per_inst_mv = []
    sj_scores = []

    for inst in instances:
        gold_ents = inst["gold"]["entities"]
        samples = inst["samples"][:n_samples] if n_samples else inst["samples"]

        # Greedy (use dedicated field if present, else sample 0)
        greedy = inst.get("greedy", samples[0])
        tp, fp, fn = entity_strict_counts(greedy.get("entities", []), gold_ents)
        greedy_tp += tp; greedy_fp += fp; greedy_fn += fn
        g_f1 = compute_entity_f1(greedy.get("entities", []), gold_ents)
        per_inst_greedy.append(g_f1)

        # Majority voting
        consensus = majority_vote_entities(samples)
        tp, fp, fn = entity_strict_counts(consensus, gold_ents)
        mv_tp += tp; mv_fp += fp; mv_fn += fn
        per_inst_mv.append(compute_entity_f1(consensus, gold_ents))

        # LP selection
        lp_idx = get_lp_selection_idx(inst, n_samples)
        lp_pred = samples[lp_idx]
        tp, fp, fn = entity_strict_counts(lp_pred.get("entities", []), gold_ents)
        lp_tp += tp; lp_fp += fp; lp_fn += fn

        # Oracle
        sample_f1s = compute_sample_f1s(inst, n_samples)
        best_idx = max(range(len(sample_f1s)), key=lambda i: sample_f1s[i])
        best_sample = samples[best_idx]
        tp, fp, fn = entity_strict_counts(best_sample.get("entities", []), gold_ents)
        oracle_tp += tp; oracle_fp += fp; oracle_fn += fn
        per_inst_oracle.append(max(sample_f1s))

        # Degeneracy: all samples produce identical (start, end, type) set
        entity_sets = [frozenset((e["start"], e["end"], e["type"])
                                 for e in s.get("entities", []))
                       for s in samples]
        if len(set(entity_sets)) == 1:
            n_degen_keyset += 1

        # SJ (expensive for large N)
        if compute_sj:
            from consistency import structural_consistency_soft_jaccard
            sj = structural_consistency_soft_jaccard(samples, subtask="ner")
            sj_scores.append(sj)

    n_inst = len(instances)
    greedy_f1 = micro_f1(greedy_tp, greedy_fp, greedy_fn)
    mv_f1_val = micro_f1(mv_tp, mv_fp, mv_fn)
    lp_f1_val = micro_f1(lp_tp, lp_fp, lp_fn)
    oracle_f1 = micro_f1(oracle_tp, oracle_fp, oracle_fn)

    mv_delta = (mv_f1_val - greedy_f1) * 100
    lp_delta = (lp_f1_val - greedy_f1) * 100
    oracle_delta = (oracle_f1 - greedy_f1) * 100
    degen_rate = n_degen_keyset / n_inst * 100

    # Instance-averaged deltas (alternative to micro)
    inst_mv_delta = np.mean([m - g for m, g in zip(per_inst_mv, per_inst_greedy)]) * 100
    inst_oracle_delta = np.mean([o - g for o, g in zip(per_inst_oracle, per_inst_greedy)]) * 100

    # Capture rate: MV gain / oracle gain on instances where oracle > greedy
    o_gains, m_gains = [], []
    for i in range(n_inst):
        if per_inst_oracle[i] > per_inst_greedy[i] + 1e-9:
            o_gains.append(per_inst_oracle[i] - per_inst_greedy[i])
            m_gains.append(per_inst_mv[i] - per_inst_greedy[i])
    capture = sum(m_gains) / sum(o_gains) * 100 if o_gains else 0

    # SJ rho
    sj_rho = float("nan")
    if compute_sj and sj_scores:
        rho, _ = spearmanr(sj_scores, per_inst_greedy)
        sj_rho = float(rho)

    # Bootstrap CI for MV delta (instance-level)
    mv_ci = bootstrap_delta_ci(per_inst_mv, per_inst_greedy)

    return {
        "n_inst": n_inst,
        "greedy_f1": greedy_f1,
        "mv_f1": mv_f1_val,
        "lp_f1": lp_f1_val,
        "oracle_f1": oracle_f1,
        "mv_delta_pp": mv_delta,
        "lp_delta_pp": lp_delta,
        "oracle_delta_pp": oracle_delta,
        "degen_rate": degen_rate,
        "capture_rate": capture,
        "sj_rho": sj_rho,
        "mv_ci": mv_ci,
        "inst_mv_delta_pp": inst_mv_delta,
        "inst_oracle_delta_pp": inst_oracle_delta,
    }


def print_comparison(N, res):
    print(f"\n{'=' * 72}")
    print(f"  N={N} Pretrained FewNERD Analysis (gold-nonempty, micro-avg)")
    print(f"  {res['n_inst']} instances")
    print(f"{'=' * 72}")
    print(f"  Greedy F1:          {res['greedy_f1']:.3f}")
    print(f"  MV F1:              {res['mv_f1']:.3f}  (Δ = {res['mv_delta_pp']:+.1f} pp)")
    ci = res["mv_ci"]
    ci_lo = ci["ci_lo"] * 100
    ci_hi = ci["ci_hi"] * 100
    print(f"  MV Δ 95% CI:        [{ci_lo:+.1f}, {ci_hi:+.1f}] pp")
    print(f"  LP F1:              {res['lp_f1']:.3f}  (Δ = {res['lp_delta_pp']:+.1f} pp)")
    print(f"  Oracle F1:          {res['oracle_f1']:.3f}  (Δ = {res['oracle_delta_pp']:+.1f} pp)")
    print(f"  Degeneracy rate:    {res['degen_rate']:.1f}%  (keyset_surface)")
    print(f"  Capture rate:       {res['capture_rate']:.0f}%")
    print(f"  --- Instance-averaged ---")
    print(f"  MV Δ (inst-avg):    {res['inst_mv_delta_pp']:+.1f} pp")
    print(f"  Oracle Δ (inst-avg):{res['inst_oracle_delta_pp']:+.1f} pp")
    if not np.isnan(res["sj_rho"]):
        print(f"  SJ ρ:               {res['sj_rho']:.3f}")
    else:
        print(f"  SJ ρ:               (skipped, use --compute_sj)")

    # Comparison table
    print(f"\n{'=' * 72}")
    print(f"  N-scaling comparison")
    print(f"{'=' * 72}")
    header = f"  {'N':>4} | {'Greedy':>7} | {'MV Δ(pp)':>9} | {'Degen%':>7} | {'Oracle Δ':>9} | {'Capture':>8} | {'ρ_SJ':>6}"
    print(header)
    print(f"  {'-' * 4}-+-{'-' * 7}-+-{'-' * 9}-+-{'-' * 7}-+-{'-' * 9}-+-{'-' * 8}-+-{'-' * 6}")
    for n_ref, ref in sorted(REF.items()):
        sj_str = f"{ref['sj_rho']:.3f}" if ref.get("sj_rho") else "  N/A"
        print(f"  {n_ref:>4} | {ref['greedy']:>7.3f} | {ref['mv_delta']:>+8.1f} | {ref['degen']:>6.1f} | {ref['oracle_delta']:>+8.1f} | {ref['capture']:>7.0f}% | {sj_str}")
    sj_str = f"{res['sj_rho']:.3f}" if not np.isnan(res["sj_rho"]) else "  N/A"
    print(f"  {N:>4} | {res['greedy_f1']:>7.3f} | {res['mv_delta_pp']:>+8.1f} | {res['degen_rate']:>6.1f} | {res['oracle_delta_pp']:>+8.1f} | {res['capture_rate']:>7.0f}% | {sj_str}")

    # Scenario determination
    print(f"\n  Scenario:")
    if res["mv_delta_pp"] >= 5.0:
        print(f"    → B (growth): MV Δ = {res['mv_delta_pp']:+.1f} pp > 5 → update Discussion")
    elif res["mv_delta_pp"] < 3.0:
        print(f"    → C (decline): MV Δ = {res['mv_delta_pp']:+.1f} pp < 3 → update Discussion")
    else:
        print(f"    → A (plateau): MV Δ = {res['mv_delta_pp']:+.1f} pp in [3, 5) → no Discussion change")

    # LaTeX table row
    print(f"\n  LaTeX row for Table 4:")
    print(f"         & Pretrained ($N{{=}}{N}$) & .{res['greedy_f1']*1000:.0f} & $+${res['mv_delta_pp']:.1f} & {res['degen_rate']:.1f} & {res['capture_rate']:.0f}\\% & .{res['oracle_f1']*1000:.0f} \\\\")


def main():
    parser = argparse.ArgumentParser(description="N-scaling pretrained FewNERD analysis")
    parser.add_argument("--input", required=True, help="Path to samples.jsonl")
    parser.add_argument("--n_samples", type=int, default=None, help="Truncate to first N samples per instance")
    parser.add_argument("--compute_sj", action="store_true", help="Compute SJ rho (slow for large N)")
    args = parser.parse_args()

    N = args.n_samples or "auto"
    print(f"Loading {args.input} ...")
    instances = load_gold_nonempty(args.input)
    print(f"  {len(instances)} gold-nonempty instances")

    actual_n = len(instances[0]["samples"]) if instances else 0
    if args.n_samples:
        actual_n = min(args.n_samples, actual_n)
    print(f"  Using N={actual_n} samples per instance")

    if args.compute_sj:
        print(f"  SJ computation enabled (N={actual_n}: {actual_n*(actual_n-1)//2} pairs/instance, may be slow)")

    res = analyze(instances, n_samples=args.n_samples, compute_sj=args.compute_sj)
    print_comparison(actual_n, res)

    # Save JSON results
    out_dir = os.path.dirname(args.input)
    out_path = os.path.join(out_dir, f"n{actual_n}_analysis.json")
    save = {k: v for k, v in res.items() if k != "mv_ci"}
    save["mv_ci_lo"] = res["mv_ci"]["ci_lo"] * 100
    save["mv_ci_hi"] = res["mv_ci"]["ci_hi"] * 100
    with open(out_path, "w") as f:
        json.dump(save, f, indent=2, default=str)
    print(f"\n  Results saved to {out_path}")


if __name__ == "__main__":
    main()
