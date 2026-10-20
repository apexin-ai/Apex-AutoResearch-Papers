"""Direction K: Minority Report Amplification.

Analyze whether minority traces (disagreeing with majority) have more
self-consistent FOL constraints than majority traces. If so, flip the answer.
"""

import json
import os
import re
import sys
import time
from collections import Counter
from pathlib import Path

import z3

CONSTRAINT_DIR = Path("/root/symb_invariant_consensus/results/exp033_mistral_7b_folio204/constraint_cache")
ANSWER_MATRIX = Path("/root/symb_invariant_consensus/results/exp033_mistral_7b_folio204/sc_answer_matrix.json")
OUTPUT_DIR = Path("/root/symb_invariant_consensus/results/direction_k_minority_report")
N_PROBLEMS = 204
Z3_TIMEOUT_MS = 10_000

Z3_BUILTINS = {"Implies", "And", "Or", "Not", "Xor", "If", "Bool", "True", "False"}
IDENT_RE = re.compile(r"[A-Za-z_][A-Za-z0-9_]*")


def extract_variables(formula_str: str) -> set:
    tokens = set(IDENT_RE.findall(formula_str))
    return tokens - Z3_BUILTINS


def build_namespace(all_vars: set) -> dict:
    ns = {}
    for v in all_vars:
        ns[v] = z3.Bool(v)
    ns["Implies"] = z3.Implies
    ns["And"] = z3.And
    ns["Or"] = z3.Or
    ns["Not"] = z3.Not
    ns["Xor"] = z3.Xor
    ns["If"] = z3.If
    ns["True"] = z3.BoolVal(True)
    ns["False"] = z3.BoolVal(False)
    return ns


def parse_formulas(constraints: list) -> list:
    """Parse z3_formula strings into z3 expressions."""
    formulas_str = [c.get("z3_formula", "") for c in constraints]
    formulas_str = [f for f in formulas_str if f.strip()]
    if not formulas_str:
        return []

    all_vars = set()
    for f in formulas_str:
        all_vars |= extract_variables(f)
    ns = build_namespace(all_vars)

    parsed = []
    for f in formulas_str:
        try:
            expr = eval(f, {"__builtins__": {}}, ns)
            if z3.is_expr(expr):
                parsed.append(expr)
            elif isinstance(expr, bool):
                parsed.append(z3.BoolVal(expr))
        except Exception:
            pass
    return parsed


def check_sat(formulas: list, timeout_ms: int = Z3_TIMEOUT_MS) -> str:
    """Check satisfiability of conjunction. Returns SAT/UNSAT/TIMEOUT/EMPTY."""
    if not formulas:
        return "EMPTY"
    solver = z3.Solver()
    solver.set("timeout", timeout_ms)
    for f in formulas:
        solver.add(f)
    result = solver.check()
    if result == z3.sat:
        return "SAT"
    elif result == z3.unsat:
        return "UNSAT"
    return "TIMEOUT"


def maxsat_satisfaction_ratio(constraints: list, timeout_ms: int = Z3_TIMEOUT_MS) -> dict:
    """Compute MAX-SAT satisfaction ratio for a set of constraints.

    Returns dict with: n_total, n_parsed, n_satisfied, ratio, sat_status.
    """
    formulas_str = [c.get("z3_formula", "") for c in constraints]
    formulas_str = [f for f in formulas_str if f.strip()]

    if not formulas_str:
        return {"n_total": 0, "n_parsed": 0, "n_satisfied": 0, "ratio": 0.0, "sat_status": "EMPTY"}

    all_vars = set()
    for f in formulas_str:
        all_vars |= extract_variables(f)
    ns = build_namespace(all_vars)

    parsed = []
    for f in formulas_str:
        try:
            expr = eval(f, {"__builtins__": {}}, ns)
            if z3.is_expr(expr):
                parsed.append(expr)
            elif isinstance(expr, bool):
                parsed.append(z3.BoolVal(expr))
        except Exception:
            pass

    if not parsed:
        return {"n_total": len(formulas_str), "n_parsed": 0, "n_satisfied": 0, "ratio": 0.0, "sat_status": "PARSE_ERROR"}

    # First check simple SAT
    sat_status = check_sat(parsed, timeout_ms)

    if sat_status == "SAT":
        return {
            "n_total": len(formulas_str),
            "n_parsed": len(parsed),
            "n_satisfied": len(parsed),
            "ratio": 1.0,
            "sat_status": "SAT",
        }

    # UNSAT or TIMEOUT -> use MAX-SAT to find max satisfiable subset
    opt = z3.Optimize()
    opt.set("timeout", timeout_ms)

    indicators = []
    for i, f in enumerate(parsed):
        ind = z3.Bool(f"__mk_ind_{i}")
        indicators.append(ind)
        try:
            opt.add(z3.Implies(ind, f))
            opt.add_soft(ind, weight=1)
        except Exception:
            pass

    result = opt.check()
    n_satisfied = 0
    if result in (z3.sat, z3.unknown):
        model = opt.model()
        for ind in indicators:
            val = model.evaluate(ind, model_completion=True)
            if z3.is_true(val):
                n_satisfied += 1

    ratio = n_satisfied / len(parsed) if parsed else 0.0
    return {
        "n_total": len(formulas_str),
        "n_parsed": len(parsed),
        "n_satisfied": n_satisfied,
        "ratio": ratio,
        "sat_status": sat_status,
    }


def compute_group_consistency(trace_indices: list, per_trace: list) -> dict:
    """Compute consistency metrics for a group of traces."""
    group_constraints = []
    per_trace_results = []

    for tidx in trace_indices:
        tc = None
        for t in per_trace:
            if t["trace_idx"] == tidx:
                tc = t
                break
        if tc is None:
            continue
        constraints = tc.get("constraints", [])
        group_constraints.extend(constraints)

        # Per-trace SAT check
        formulas = parse_formulas(constraints)
        status = check_sat(formulas)
        per_trace_results.append({
            "trace_idx": tidx,
            "n_constraints": len(constraints),
            "n_parsed": len(formulas),
            "sat_status": status,
        })

    # Group-level MAX-SAT
    group_maxsat = maxsat_satisfaction_ratio(group_constraints)

    n_sat_traces = sum(1 for r in per_trace_results if r["sat_status"] == "SAT")
    n_traces = len(per_trace_results)

    return {
        "n_traces": n_traces,
        "n_constraints_total": len(group_constraints),
        "n_sat_traces": n_sat_traces,
        "trace_sat_ratio": n_sat_traces / n_traces if n_traces > 0 else 0.0,
        "maxsat": group_maxsat,
        "per_trace": per_trace_results,
    }


def main():
    print("Direction K: Minority Report Amplification")
    print("=" * 60)

    with open(ANSWER_MATRIX) as f:
        answer_matrix = json.load(f)

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    per_problem_results = []
    n_unanimous = 0
    n_with_minority = 0
    n_meaningful_minority = 0  # >=2 minority traces

    flip_stats = {
        "strict": {"flipped": 0, "flip_correct": 0, "flip_wrong": 0},
        "moderate": {"flipped": 0, "flip_correct": 0, "flip_wrong": 0},
        "combined": {"flipped": 0, "flip_correct": 0, "flip_wrong": 0},
    }

    sc_correct = 0
    variant_correct = {"strict": 0, "moderate": 0, "combined": 0}
    total = 0

    t0 = time.time()

    for pid_idx in range(N_PROBLEMS):
        pid = f"folio_{pid_idx}"

        if pid not in answer_matrix:
            continue

        cache_file = CONSTRAINT_DIR / f"{pid}.json"
        if not cache_file.exists():
            continue

        answers = answer_matrix[pid]["answers"]
        gt = answer_matrix[pid]["ground_truth"]

        with open(cache_file) as f:
            cache = json.load(f)

        per_trace = cache.get("per_trace", [])

        # Filter out empty answers
        valid_answers = [(i, a) for i, a in enumerate(answers) if a.strip()]
        if not valid_answers:
            continue

        total += 1

        # Determine majority and minority
        answer_counts = Counter(a for _, a in valid_answers)
        sc_answer = answer_counts.most_common(1)[0][0]
        sc_is_correct = (sc_answer == gt)
        if sc_is_correct:
            sc_correct += 1

        # Check if unanimous
        if len(answer_counts) == 1:
            n_unanimous += 1
            # No minority -> all variants keep SC answer
            for v in variant_correct:
                if sc_is_correct:
                    variant_correct[v] += 1

            per_problem_results.append({
                "pid": pid,
                "gt": gt,
                "sc_answer": sc_answer,
                "sc_correct": sc_is_correct,
                "unanimous": True,
                "n_valid_traces": len(valid_answers),
            })
            continue

        n_with_minority += 1

        # Identify majority and minority trace groups
        majority_answer = sc_answer
        majority_traces = [i for i, a in valid_answers if a == majority_answer]
        minority_groups = {}
        for i, a in valid_answers:
            if a != majority_answer:
                minority_groups.setdefault(a, []).append(i)

        # Find the strongest minority (most votes)
        best_minority_answer = max(minority_groups, key=lambda a: len(minority_groups[a]))
        minority_traces = minority_groups[best_minority_answer]

        if len(minority_traces) >= 2:
            n_meaningful_minority += 1

        # Compute consistency for both groups
        maj_consistency = compute_group_consistency(majority_traces, per_trace)
        min_consistency = compute_group_consistency(minority_traces, per_trace)

        maj_ratio = maj_consistency["maxsat"]["ratio"]
        min_ratio = min_consistency["maxsat"]["ratio"]
        maj_trace_sat = maj_consistency["trace_sat_ratio"]
        min_trace_sat = min_consistency["trace_sat_ratio"]

        # Combined consistency score: average of maxsat ratio and trace-level sat ratio
        maj_combined = (maj_ratio + maj_trace_sat) / 2
        min_combined = (min_ratio + min_trace_sat) / 2

        # SC vote counts
        majority_count = len(majority_traces)
        minority_count = len(minority_traces)

        result = {
            "pid": pid,
            "gt": gt,
            "sc_answer": sc_answer,
            "sc_correct": sc_is_correct,
            "unanimous": False,
            "n_valid_traces": len(valid_answers),
            "majority_answer": majority_answer,
            "majority_count": majority_count,
            "minority_answer": best_minority_answer,
            "minority_count": minority_count,
            "majority_consistency": {
                "maxsat_ratio": maj_ratio,
                "trace_sat_ratio": maj_trace_sat,
                "combined": maj_combined,
                "n_constraints": maj_consistency["n_constraints_total"],
            },
            "minority_consistency": {
                "maxsat_ratio": min_ratio,
                "trace_sat_ratio": min_trace_sat,
                "combined": min_combined,
                "n_constraints": min_consistency["n_constraints_total"],
            },
        }

        # Variant decisions
        for variant_name in ["strict", "moderate", "combined"]:
            if variant_name == "strict":
                # Flip only if minority ratio > 1.5x majority ratio
                flip = (min_ratio > 1.5 * maj_ratio) if maj_ratio > 0 else (min_ratio > 0.5)
            elif variant_name == "moderate":
                # Flip if minority ratio > majority ratio
                flip = min_ratio > maj_ratio
            else:
                # Combined: weighted score = consistency * 0.6 + vote_share * 0.4
                maj_vote_share = majority_count / (majority_count + minority_count)
                min_vote_share = minority_count / (majority_count + minority_count)
                maj_score = maj_combined * 0.6 + maj_vote_share * 0.4
                min_score = min_combined * 0.6 + min_vote_share * 0.4
                flip = min_score > maj_score

            final_answer = best_minority_answer if flip else sc_answer
            correct = (final_answer == gt)

            if correct:
                variant_correct[variant_name] += 1

            if flip:
                flip_stats[variant_name]["flipped"] += 1
                if correct:
                    flip_stats[variant_name]["flip_correct"] += 1
                else:
                    flip_stats[variant_name]["flip_wrong"] += 1
            else:
                # Kept SC answer
                pass

            result[f"{variant_name}_flip"] = flip
            result[f"{variant_name}_answer"] = final_answer
            result[f"{variant_name}_correct"] = correct

        per_problem_results.append(result)

        if pid_idx % 50 == 0:
            print(f"  processed {pid_idx}/{N_PROBLEMS}...")

    elapsed = time.time() - t0

    # Summary
    sc_acc = sc_correct / total if total > 0 else 0
    summary = {
        "total_problems": total,
        "n_unanimous": n_unanimous,
        "n_with_minority": n_with_minority,
        "n_meaningful_minority_gte2": n_meaningful_minority,
        "sc_accuracy": sc_acc,
        "sc_correct": sc_correct,
        "elapsed_s": round(elapsed, 1),
    }

    for v in ["strict", "moderate", "combined"]:
        acc = variant_correct[v] / total if total > 0 else 0
        summary[f"{v}_accuracy"] = acc
        summary[f"{v}_correct"] = variant_correct[v]
        summary[f"{v}_delta_vs_sc"] = round(acc - sc_acc, 4)
        summary[f"{v}_flips"] = flip_stats[v]

    # Analyze minority correctness correlation
    minority_correct_gt = 0
    majority_correct_gt = 0
    for r in per_problem_results:
        if r.get("unanimous"):
            continue
        if r["minority_answer"] == r["gt"]:
            minority_correct_gt += 1
        if r["majority_answer"] == r["gt"]:
            majority_correct_gt += 1

    summary["minority_is_gt_count"] = minority_correct_gt
    summary["majority_is_gt_count"] = majority_correct_gt
    summary["minority_gt_rate"] = minority_correct_gt / n_with_minority if n_with_minority > 0 else 0
    summary["majority_gt_rate"] = majority_correct_gt / n_with_minority if n_with_minority > 0 else 0

    # Consistency vs correctness correlation
    min_more_consistent = 0
    min_more_consistent_and_correct = 0
    min_more_consistent_and_wrong = 0
    for r in per_problem_results:
        if r.get("unanimous"):
            continue
        min_r = r["minority_consistency"]["maxsat_ratio"]
        maj_r = r["majority_consistency"]["maxsat_ratio"]
        if min_r > maj_r:
            min_more_consistent += 1
            if r["minority_answer"] == r["gt"]:
                min_more_consistent_and_correct += 1
            else:
                min_more_consistent_and_wrong += 1

    summary["minority_more_consistent_count"] = min_more_consistent
    summary["minority_more_consistent_and_correct"] = min_more_consistent_and_correct
    summary["minority_more_consistent_and_wrong"] = min_more_consistent_and_wrong
    if min_more_consistent > 0:
        summary["minority_consistency_precision"] = min_more_consistent_and_correct / min_more_consistent
    else:
        summary["minority_consistency_precision"] = 0.0

    output = {
        "summary": summary,
        "per_problem": per_problem_results,
    }

    out_file = OUTPUT_DIR / "results.json"
    with open(out_file, "w") as f:
        json.dump(output, f, indent=2)

    print(f"\nResults saved to {out_file}")
    print(f"\n{'='*60}")
    print(f"Total: {total} problems, {n_unanimous} unanimous, {n_with_minority} with minority")
    print(f"Meaningful minority (>=2 traces): {n_meaningful_minority}")
    print(f"\nSC baseline:     {sc_acc:.4f} ({sc_correct}/{total})")
    for v in ["strict", "moderate", "combined"]:
        acc = summary[f"{v}_accuracy"]
        delta = summary[f"{v}_delta_vs_sc"]
        fs = flip_stats[v]
        print(f"{v:12s}:    {acc:.4f} ({variant_correct[v]}/{total}) delta={delta:+.4f}  "
              f"flips={fs['flipped']} (correct={fs['flip_correct']}, wrong={fs['flip_wrong']})")

    print(f"\nMinority is ground truth: {minority_correct_gt}/{n_with_minority} ({summary['minority_gt_rate']:.4f})")
    print(f"Majority is ground truth: {majority_correct_gt}/{n_with_minority} ({summary['majority_gt_rate']:.4f})")
    print(f"\nMinority more consistent: {min_more_consistent}")
    print(f"  -> correct: {min_more_consistent_and_correct}, wrong: {min_more_consistent_and_wrong}")
    print(f"  -> precision: {summary['minority_consistency_precision']:.4f}")
    print(f"\nElapsed: {elapsed:.1f}s")


if __name__ == "__main__":
    main()
