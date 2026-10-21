#!/usr/bin/env python3
"""
Cross-Trace UNSAT Analysis (exp-036b)

For each problem, groups K=12 traces by candidate answer, then checks whether
constraints from different answer groups are mutually contradictory (UNSAT).
If constraints_A ∪ constraints_B is UNSAT, the symbolic constraints genuinely
distinguish between answers A and B (discriminative signal).

Compares cross-trace UNSAT rate against within-trace baseline (0.9% from exp-001).
"""

import argparse
import json
import os
import re
import sys
import time
from collections import defaultdict
from itertools import combinations
from pathlib import Path

import z3

sys.path.insert(0, str(Path(__file__).resolve().parent))
from sica.z3_maxsat import parse_z3_formula

RESERVED_TOKENS = {
    "True", "False", "And", "Or", "Not", "Implies", "If",
    "Bool", "Real", "Int", "abs", "Abs", "sum", "Sum",
    "max", "min", "len", "int", "Mod", "pow",
}


def load_per_trace(data_dir):
    ptc_dir = os.path.join(data_dir, "per_trace_constraints")
    problems = {}
    for fname in sorted(os.listdir(ptc_dir)):
        if not fname.endswith(".json"):
            continue
        with open(os.path.join(ptc_dir, fname)) as f:
            data = json.load(f)
        problems[data["pid"]] = data
    return problems


def load_sica_results(data_dir):
    results_file = os.path.join(data_dir, "folio_204_results.json")
    with open(results_file) as f:
        data = json.load(f)
    gold = {}
    sica = {}
    for r in data["results"]:
        pid = r["problem_id"]
        sica[pid] = r
        gold[pid] = r["ground_truth"]
    return sica, gold


def extract_var_names(z3_strs):
    names = set()
    for s in z3_strs:
        tokens = set(re.findall(r"\b([a-zA-Z_]\w*)\b", s))
        names.update(tokens - RESERVED_TOKENS)
    return names


def collect_formulas(traces, type_filter=None):
    """Parse z3_formula strings from traces. Returns (z3_exprs, raw_strings)."""
    formulas = []
    raw = []
    for t in traces:
        for c in t.get("constraints", []):
            if type_filter and c.get("type") not in type_filter:
                continue
            z3_str = c.get("z3_formula", "")
            if not z3_str:
                continue
            f = parse_z3_formula(z3_str)
            if f is not None and z3.is_bool(f):
                formulas.append(f)
                raw.append(z3_str)
    return formulas, raw


def check_unsat(formulas_a, formulas_b, timeout_ms=5000):
    """Check if formulas_a ∪ formulas_b is UNSAT."""
    if not formulas_a or not formulas_b:
        return "empty"
    s = z3.Solver()
    s.set("timeout", timeout_ms)
    for f in formulas_a:
        s.add(f)
    for f in formulas_b:
        s.add(f)
    r = s.check()
    if r == z3.unsat:
        return "unsat"
    elif r == z3.sat:
        return "sat"
    return "unknown"


def analyze_problem(pid, pdata, timeout_ms=5000):
    per_trace = pdata.get("per_trace", [])
    gt = pdata.get("gt", "")

    groups = defaultdict(list)
    for t in per_trace:
        ans = t.get("answer", "").strip()
        if ans:
            groups[ans].append(t)
    groups = dict(groups)
    answers = sorted(groups.keys())

    answer_counts = {a: len(groups[a]) for a in answers}

    if len(answers) < 2:
        return {
            "pid": pid, "gt": gt, "n_answers": len(answers),
            "answers": answers, "answer_counts": answer_counts,
            "pairs": [], "has_unsat": False, "skipped": True,
        }

    answer_formulas = {}
    answer_raw = {}
    answer_derived = {}
    for ans in answers:
        answer_formulas[ans], answer_raw[ans] = collect_formulas(groups[ans])
        answer_derived[ans], _ = collect_formulas(groups[ans], type_filter={"derived"})

    pairs = []
    has_unsat = False
    for a, b in combinations(answers, 2):
        fa, fb = answer_formulas[a], answer_formulas[b]
        result = check_unsat(fa, fb, timeout_ms)

        shared_vars = extract_var_names(answer_raw[a]) & extract_var_names(answer_raw[b])

        result_derived = check_unsat(
            answer_derived[a], answer_derived[b], timeout_ms
        )

        pair_info = {
            "pair": [a, b],
            "result": result,
            "result_derived_only": result_derived,
            "n_formulas": [len(fa), len(fb)],
            "n_derived": [len(answer_derived[a]), len(answer_derived[b])],
            "n_shared_vars": len(shared_vars),
        }
        pairs.append(pair_info)
        if result == "unsat":
            has_unsat = True

    return {
        "pid": pid, "gt": gt, "n_answers": len(answers),
        "answers": answers, "answer_counts": answer_counts,
        "formula_counts": {a: len(answer_formulas[a]) for a in answers},
        "pairs": pairs, "has_unsat": has_unsat, "skipped": False,
    }


def compute_adjusted_scores(analysis, sica_result, bonus=5.0):
    """Adjust SICA scores based on cross-trace UNSAT results."""
    original_scores = dict(sica_result.get("sica_scores", {}))
    original_answer = sica_result.get("sica_answer", "")

    if analysis["skipped"] or not analysis["has_unsat"]:
        return {
            "original_scores": original_scores,
            "adjusted_scores": original_scores,
            "original_answer": original_answer,
            "adjusted_answer": original_answer,
            "adjustment_applied": False,
        }

    adjusted = dict(original_scores)
    answer_counts = analysis["answer_counts"]

    for pair_info in analysis["pairs"]:
        if pair_info["result"] != "unsat":
            continue
        a, b = pair_info["pair"]
        ca = answer_counts.get(a, 0)
        cb = answer_counts.get(b, 0)
        if ca > cb:
            adjusted[a] = adjusted.get(a, 0) + bonus
            adjusted[b] = adjusted.get(b, 0) - bonus
        elif cb > ca:
            adjusted[b] = adjusted.get(b, 0) + bonus
            adjusted[a] = adjusted.get(a, 0) - bonus

    adjusted_answer = max(adjusted, key=lambda x: adjusted[x]) if adjusted else original_answer

    return {
        "original_scores": original_scores,
        "adjusted_scores": adjusted,
        "original_answer": original_answer,
        "adjusted_answer": adjusted_answer,
        "adjustment_applied": True,
    }


def main():
    parser = argparse.ArgumentParser(description="Cross-Trace UNSAT Analysis (exp-036b)")
    parser.add_argument("--data-dir", required=True)
    parser.add_argument("--output", default="results/cross_trace_unsat_results.json")
    parser.add_argument("--timeout-ms", type=int, default=5000)
    parser.add_argument("--bonus", type=float, default=5.0)
    parser.add_argument("--limit", type=int, default=0, help="Limit to N problems (0=all)")
    args = parser.parse_args()

    print("Loading data...")
    problems = load_per_trace(args.data_dir)
    sica_results, gold = load_sica_results(args.data_dir)
    print(f"Loaded {len(problems)} problems")

    items = sorted(problems.items())
    if args.limit > 0:
        items = items[:args.limit]
        print(f"Limited to {args.limit} problems")

    analyses = {}
    scoring = {}
    t0 = time.time()

    for i, (pid, pdata) in enumerate(items):
        analysis = analyze_problem(pid, pdata, args.timeout_ms)
        analyses[pid] = analysis

        if pid in sica_results:
            scoring[pid] = compute_adjusted_scores(analysis, sica_results[pid], args.bonus)

        if (i + 1) % 50 == 0:
            print(f"  Processed {i+1}/{len(items)}...")

    elapsed = time.time() - t0
    print(f"Analysis done in {elapsed:.1f}s")

    # --- Statistics ---
    total = len(analyses)
    skipped = sum(1 for a in analyses.values() if a["skipped"])
    checked = total - skipped
    n_with_unsat = sum(1 for a in analyses.values() if a["has_unsat"])

    all_pairs = []
    for a in analyses.values():
        all_pairs.extend(a["pairs"])

    pair_counts = defaultdict(int)
    pair_type_counts = defaultdict(lambda: defaultdict(int))
    derived_counts = defaultdict(int)
    shared_var_stats = []

    for p in all_pairs:
        pair_counts[p["result"]] += 1
        pair_key = "-".join(sorted(p["pair"]))
        pair_type_counts[pair_key][p["result"]] += 1
        derived_counts[p["result_derived_only"]] += 1
        shared_var_stats.append(p["n_shared_vars"])

    total_pairs = len(all_pairs)
    cross_unsat_rate = pair_counts.get("unsat", 0) / total_pairs if total_pairs > 0 else 0

    avg_shared = sum(shared_var_stats) / len(shared_var_stats) if shared_var_stats else 0
    zero_shared = sum(1 for x in shared_var_stats if x == 0)

    # --- Accuracy ---
    sica_correct = 0
    adjusted_correct = 0
    sc_correct = 0
    total_scored = 0
    flips = []

    for pid in sorted(scoring.keys()):
        gt = gold.get(pid, "")
        if not gt:
            continue
        total_scored += 1

        s = scoring[pid]
        sr = sica_results.get(pid, {})

        if s["original_answer"] == gt:
            sica_correct += 1
        if s["adjusted_answer"] == gt:
            adjusted_correct += 1
        if sr.get("sc_answer", "") == gt:
            sc_correct += 1

        if s["original_answer"] != s["adjusted_answer"]:
            flips.append({
                "pid": pid, "gt": gt,
                "original": s["original_answer"],
                "adjusted": s["adjusted_answer"],
                "original_correct": s["original_answer"] == gt,
                "adjusted_correct": s["adjusted_answer"] == gt,
            })

    summary = {
        "n_problems": total,
        "n_single_answer_skipped": skipped,
        "n_multi_answer_checked": checked,
        "n_problems_with_cross_unsat": n_with_unsat,
        "problem_cross_unsat_rate": round(n_with_unsat / checked, 4) if checked > 0 else 0,
        "total_pairs_checked": total_pairs,
        "pair_result_counts": dict(pair_counts),
        "cross_trace_unsat_rate": round(cross_unsat_rate, 4),
        "within_trace_unsat_rate_baseline": 0.009,
        "derived_only_result_counts": dict(derived_counts),
        "shared_var_stats": {
            "mean": round(avg_shared, 1),
            "zero_count": zero_shared,
            "zero_pct": round(zero_shared / total_pairs, 3) if total_pairs > 0 else 0,
        },
        "pair_type_breakdown": {k: dict(v) for k, v in pair_type_counts.items()},
        "accuracy": {
            "sc": round(sc_correct / total_scored, 4) if total_scored > 0 else 0,
            "sica": round(sica_correct / total_scored, 4) if total_scored > 0 else 0,
            "sica_cross_ut": round(adjusted_correct / total_scored, 4) if total_scored > 0 else 0,
            "n": total_scored,
        },
        "flips": {
            "total": len(flips),
            "improved": sum(1 for f in flips if f["adjusted_correct"] and not f["original_correct"]),
            "degraded": sum(1 for f in flips if not f["adjusted_correct"] and f["original_correct"]),
            "neutral": sum(1 for f in flips if f["adjusted_correct"] == f["original_correct"]),
        },
        "bonus": args.bonus,
        "elapsed_s": round(elapsed, 1),
    }

    output = {
        "summary": summary,
        "flips": flips,
        "per_problem": analyses,
    }

    os.makedirs(os.path.dirname(os.path.abspath(args.output)) or ".", exist_ok=True)
    with open(args.output, "w") as f:
        json.dump(output, f, indent=2)

    # --- Print ---
    print("\n" + "=" * 60)
    print("Cross-Trace UNSAT Results (exp-036b)")
    print("=" * 60)
    print(f"Problems: {total} total, {skipped} single-answer (skipped), {checked} multi-answer")
    print(f"Problems with cross-UNSAT: {n_with_unsat}/{checked} ({summary['problem_cross_unsat_rate']:.1%})")
    print(f"\nPair-level ({total_pairs} pairs):")
    for k in ["unsat", "sat", "empty", "unknown"]:
        v = pair_counts.get(k, 0)
        if v > 0:
            print(f"  {k:>8s}: {v:4d} ({v/total_pairs:.1%})")
    print(f"Cross-trace UNSAT rate: {cross_unsat_rate:.1%}  (within-trace baseline: 0.9%)")

    print(f"\nDerived-only pair results ({sum(derived_counts.values())} pairs):")
    for k in ["unsat", "sat", "empty", "unknown"]:
        v = derived_counts.get(k, 0)
        if v > 0:
            print(f"  {k:>8s}: {v:4d}")

    print(f"\nShared variables: mean={avg_shared:.1f}, {zero_shared}/{total_pairs} pairs share zero vars")

    print(f"\nPair type breakdown:")
    for pt in sorted(pair_type_counts.keys()):
        parts = []
        for k in ["unsat", "sat", "empty", "unknown"]:
            v = pair_type_counts[pt].get(k, 0)
            if v > 0:
                parts.append(f"{k}={v}")
        print(f"  {pt}: {', '.join(parts)}")

    print(f"\nAccuracy (n={total_scored}):")
    print(f"  SC baseline:       {sc_correct}/{total_scored} = {summary['accuracy']['sc']:.1%}")
    print(f"  SICA:              {sica_correct}/{total_scored} = {summary['accuracy']['sica']:.1%}")
    print(f"  SICA+CrossUT(b={args.bonus}): {adjusted_correct}/{total_scored} = {summary['accuracy']['sica_cross_ut']:.1%}")

    fl = summary["flips"]
    print(f"\nFlips: {fl['total']} total  (+{fl['improved']} improved, -{fl['degraded']} degraded, ={fl['neutral']} neutral)")
    if flips:
        for f in flips:
            mark = "+" if f["adjusted_correct"] and not f["original_correct"] else \
                   "-" if f["original_correct"] and not f["adjusted_correct"] else "="
            print(f"  [{mark}] {f['pid']}: {f['original']} -> {f['adjusted']} (gt={f['gt']})")

    print(f"\nSaved to {args.output}")


if __name__ == "__main__":
    main()
