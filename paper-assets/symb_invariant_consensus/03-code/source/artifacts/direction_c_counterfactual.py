"""
Direction C: Counterfactual Constraint Subtraction — Pilot 20 problems

Idea: Filter out "direction-agnostic" constraints (bias) that would appear
regardless of the hypothesis direction. Keep only "signal" constraints that
are specific to the current conclusion.

Strategies tested:
  1. full       — all constraints (SICA baseline)
  2. signal     — only constraints referencing conclusion predicates
  3. premise    — only constraints NOT referencing conclusion predicates
  4. rules_only — only "rule" type, drop "fact" type constraints
"""
import json
import os
import re
import sys
import time
from collections import Counter
from pathlib import Path

sys.path.insert(0, "/root/symb_invariant_consensus")
from sica.z3_maxsat import ConstraintDeduplicator, MaxSATSolver, UniqueConstraint
from sica.scorer import InvariantScorer

EXP_DIR = Path("/root/symb_invariant_consensus/results/exp033_mistral_7b_folio204")
DATA_PATH = Path("/root/symb_invariant_consensus/data/folio_full.json")
N_PILOT = 20


def load_folio_data():
    with open(DATA_PATH) as f:
        return {p["id"]: p for p in json.load(f)}


def load_constraint_cache(pid):
    path = EXP_DIR / "constraint_cache" / f"{pid}.json"
    with open(path) as f:
        return json.load(f)


def load_intermediate(pid):
    path = EXP_DIR / "intermediates" / f"{pid}.json"
    with open(path) as f:
        return json.load(f)


def extract_conclusion_keywords(conclusion_fol):
    """Extract predicate and entity names from conclusion FOL."""
    clean = conclusion_fol.replace("\\u2200", "").replace("\\u2203", "")
    clean = conclusion_fol
    # Remove unicode logical operators
    for ch in ["∀", "∃", "¬", "→", "∧", "∨", "⊕"]:
        clean = clean.replace(ch, " ")
    # Extract all identifiers (predicate and entity names)
    tokens = re.findall(r'[A-Za-z_][A-Za-z0-9_]*', clean)
    # Filter out single-char variables like x, y
    tokens = [t for t in tokens if len(t) > 1]
    return set(t.lower() for t in tokens)


def constraint_references_conclusion(constraint, conclusion_keywords):
    """Check if a constraint's expression or z3_formula mentions conclusion keywords."""
    expr = constraint.get("expression", "").lower()
    z3f = constraint.get("z3_formula", "").lower()
    text = expr + " " + z3f

    # Extract tokens from constraint text
    constraint_tokens = set(re.findall(r'[a-z_][a-z0-9_]*', text))

    # Check for overlap with conclusion keywords
    # Use fuzzy matching: keyword must appear as substring of some token
    for kw in conclusion_keywords:
        if len(kw) < 3:
            continue
        for ct in constraint_tokens:
            if kw in ct or ct in kw:
                return True
    return False


def filter_constraints_by_strategy(per_trace_constraints, strategy, conclusion_keywords):
    """Return filtered per-trace constraint lists based on strategy."""
    filtered = []
    for trace_constraints in per_trace_constraints:
        if strategy == "full":
            filtered.append(trace_constraints)
        elif strategy == "signal":
            filtered.append([
                c for c in trace_constraints
                if constraint_references_conclusion(c, conclusion_keywords)
            ])
        elif strategy == "premise":
            filtered.append([
                c for c in trace_constraints
                if not constraint_references_conclusion(c, conclusion_keywords)
            ])
        elif strategy == "rules_only":
            filtered.append([
                c for c in trace_constraints
                if c.get("type") == "rule"
            ])
        else:
            filtered.append(trace_constraints)
    return filtered


def run_maxsat_scoring(per_trace_constraints, traces, candidates, answer_counts):
    """Run dedup -> MAX-SAT -> scoring pipeline on constraint lists."""
    deduplicator = ConstraintDeduplicator()
    solver = MaxSATSolver()
    scorer = InvariantScorer()

    unique = deduplicator.deduplicate(per_trace_constraints)
    if not unique:
        return None, None, {"unique": 0, "satisfied": 0, "excluded": 0}

    result = solver.solve(unique, timeout_ms=10000)
    scores = scorer.score(result, traces, candidates)
    answer = scorer.select_answer(scores, answer_counts)

    stats = {
        "unique": len(unique),
        "satisfied": len(result.satisfied),
        "excluded": len(result.excluded),
        "total_weight": result.total_weight,
    }
    return answer, scores, stats


def normalize_logic_answer(ans):
    ans = str(ans).strip().lower()
    if ans in ("true", "yes", "correct", "entailment"):
        return "True"
    if ans in ("false", "no", "incorrect", "contradiction"):
        return "False"
    if ans in ("unknown", "uncertain", "undetermined", "neutral"):
        return "Unknown"
    return ans.capitalize()


def main():
    folio_data = load_folio_data()

    # Load exp033 results for baseline comparison
    with open(EXP_DIR / "exp033_results.json") as f:
        exp033 = json.load(f)

    # Get first N problem IDs
    pilot_results = exp033["results"][:N_PILOT]
    pids = [r["problem_id"] for r in pilot_results]

    strategies = ["full", "signal", "premise", "rules_only"]
    results = {s: [] for s in strategies}
    detail_rows = []

    for i, pid in enumerate(pids):
        prob = folio_data[pid]
        gt = prob["answer"]
        conclusion_fol = prob.get("conclusion_fol", "")
        conclusion_kws = extract_conclusion_keywords(conclusion_fol)

        # Load constraint cache (per-trace constraints)
        cache = load_constraint_cache(pid)
        per_trace = [t["constraints"] for t in cache["per_trace"]]

        # Load intermediate for traces
        inter = load_intermediate(pid)
        traces = inter["sica_result"]["traces"]
        for t in traces:
            if t.get("answer"):
                t["answer"] = normalize_logic_answer(t["answer"])

        candidates = sorted(set(t["answer"] for t in traces if t["answer"]))
        answer_counts = Counter(t["answer"] for t in traces if t["answer"])

        # SC answer
        sc_answer = answer_counts.most_common(1)[0][0] if answer_counts else ""

        row = {
            "pid": pid,
            "gt": gt,
            "sc_answer": sc_answer,
            "sc_correct": sc_answer == gt,
            "conclusion_fol": conclusion_fol,
            "conclusion_keywords": sorted(conclusion_kws),
        }

        for strategy in strategies:
            filtered = filter_constraints_by_strategy(per_trace, strategy, conclusion_kws)
            n_constraints = sum(len(c) for c in filtered)

            answer, scores, stats = run_maxsat_scoring(
                filtered, traces, candidates, answer_counts
            )
            if answer is None:
                answer = sc_answer  # fallback to SC

            correct = answer == gt
            results[strategy].append(correct)

            row[f"{strategy}_answer"] = answer
            row[f"{strategy}_correct"] = correct
            row[f"{strategy}_n_constraints"] = n_constraints
            row[f"{strategy}_stats"] = stats

        detail_rows.append(row)
        print(f"  [{i+1:2d}/{N_PILOT}] {pid}: gt={gt}  sc={sc_answer}({'O' if row['sc_correct'] else 'X'})  "
              f"full={row['full_answer']}({'O' if row['full_correct'] else 'X'})  "
              f"signal={row['signal_answer']}({'O' if row['signal_correct'] else 'X'})  "
              f"premise={row['premise_answer']}({'O' if row['premise_correct'] else 'X'})  "
              f"rules={row['rules_only_answer']}({'O' if row['rules_only_correct'] else 'X'})")

    # Summary
    print("\n" + "=" * 60)
    print(f"Direction C Pilot Results — {N_PILOT} problems (exp033 Mistral-7B)")
    print("=" * 60)

    for strategy in strategies:
        correct = sum(results[strategy])
        total = len(results[strategy])
        acc = correct / total if total else 0
        print(f"  {strategy:12s}: {correct}/{total} = {acc:.1%}")

    sc_correct = sum(r["sc_correct"] for r in detail_rows)
    print(f"  {'SC':12s}: {sc_correct}/{N_PILOT} = {sc_correct/N_PILOT:.1%}")

    # Constraint retention ratio
    print("\nConstraint retention (avg |filtered| / |full|):")
    for strategy in strategies:
        if strategy == "full":
            continue
        ratios = []
        for row in detail_rows:
            full_n = row["full_n_constraints"]
            filt_n = row[f"{strategy}_n_constraints"]
            if full_n > 0:
                ratios.append(filt_n / full_n)
        avg_ratio = sum(ratios) / len(ratios) if ratios else 0
        print(f"  {strategy:12s}: {avg_ratio:.1%}")

    # Disagreement analysis: where strategies differ from full
    print("\nDisagreements with full SICA:")
    for strategy in ["signal", "premise", "rules_only"]:
        diffs = []
        for row in detail_rows:
            if row[f"{strategy}_answer"] != row["full_answer"]:
                diffs.append(row["pid"])
        print(f"  {strategy:12s}: {len(diffs)} disagreements — {diffs}")

    # Flip analysis: cases where filtered gets right but full gets wrong (or vice versa)
    print("\nFlip analysis (vs full baseline):")
    for strategy in ["signal", "premise", "rules_only"]:
        gained = []
        lost = []
        for row in detail_rows:
            fc = row["full_correct"]
            sc = row[f"{strategy}_correct"]
            if not fc and sc:
                gained.append(row["pid"])
            elif fc and not sc:
                lost.append(row["pid"])
        print(f"  {strategy:12s}: gained={gained}  lost={lost}  net={len(gained)-len(lost):+d}")

    # Save results
    output = {
        "summary": {
            "n_problems": N_PILOT,
            "strategies": {
                s: {
                    "accuracy": sum(results[s]) / len(results[s]),
                    "correct": sum(results[s]),
                }
                for s in strategies
            },
            "sc_accuracy": sc_correct / N_PILOT,
        },
        "details": detail_rows,
    }

    out_path = "/root/symb_invariant_consensus/results/direction_c_counterfactual_pilot.json"
    with open(out_path, "w") as f:
        json.dump(output, f, indent=2, default=str)
    print(f"\nResults saved to {out_path}")


if __name__ == "__main__":
    main()
