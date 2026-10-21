"""
Post-process case_study_constraints.json:
  1. Normalize answer formats (\\text{True} -> True, etc.)
  2. Recompute SC (majority vote) and SICA (invariant-weighted scoring)
  3. Analyze constraint count differences vs exp-001
"""
import json
import math
from collections import Counter
from pathlib import Path

ALPHA = 0.5
FALLBACK_THRESHOLD = 0.2

CANONICAL = {
    "true": "True", "yes": "True", "1": "True",
    "false": "False", "no": "False", "0": "False",
    "unknown": "Unknown", "uncertain": "Unknown", "undetermined": "Unknown",
}

def normalize_answer(raw: str) -> str:
    s = raw.strip()
    # Strip \text{...} and \\text{...} wrappers
    for prefix in (r"\\text{", r"\text{"):
        if s.startswith(prefix):
            s = s[len(prefix):]
            if s.endswith("}"):
                s = s[:-1]
            break
    return CANONICAL.get(s.strip().lower(), s.strip())


def compute_sc(normalized_answers: list[str]) -> dict:
    counts = Counter(a for a in normalized_answers if a)
    if not counts:
        return {"answer": "", "distribution": {}, "vote_entropy": 0.0}
    best = max(counts, key=lambda k: (counts[k], k))
    # Tiebreak: most votes, then alphabetical
    max_count = counts[best]
    tied = sorted([k for k, v in counts.items() if v == max_count])
    best = tied[0]  # alphabetical tiebreak

    total = sum(counts.values())
    entropy = -sum((c/total) * math.log2(c/total) for c in counts.values() if c > 0)
    max_entropy = math.log2(len(counts)) if len(counts) > 1 else 1.0
    normalized_entropy = entropy / max_entropy if max_entropy > 0 else 0.0

    return {
        "answer": best,
        "distribution": dict(counts),
        "vote_entropy": round(normalized_entropy, 4),
    }


def compute_sica(
    normalized_answers: list[str],
    trace_indices: list[int],
    satisfied: list[dict],
    excluded: list[dict],
) -> dict:
    # Build answer -> set of trace indices
    answer_traces: dict[str, set[int]] = {}
    for ans, idx in zip(normalized_answers, trace_indices):
        if ans:
            answer_traces.setdefault(ans, set()).add(idx)

    candidates = list(answer_traces.keys())
    n_sat = len(satisfied)
    n_exc = len(excluded)
    n_total = n_sat + n_exc

    if n_total == 0:
        return {"answer": "", "scores": {}, "mode": "EMPTY"}

    sat_ratio = n_sat / n_total
    fallback = sat_ratio < FALLBACK_THRESHOLD
    mode = "FALLBACK" if fallback else "NORMAL"

    answer_counts = Counter(normalized_answers)
    scores = {}

    for cand in candidates:
        cand_traces = answer_traces.get(cand, set())

        excluded_exposure = sum(
            c["weight"] for c in excluded
            if set(c["source_traces"]) & cand_traces
        )

        if fallback:
            scores[cand] = -excluded_exposure
        else:
            positive = sum(
                c["weight"] for c in satisfied
                if set(c["source_traces"]) & cand_traces
            )
            scores[cand] = positive - ALPHA * excluded_exposure

    # Select best
    if not scores:
        best = ""
    else:
        max_score = max(scores.values())
        top = [a for a, s in scores.items() if s == max_score]
        if len(top) == 1:
            best = top[0]
        else:
            best = max(top, key=lambda a: answer_counts.get(a, 0))

    return {"answer": best, "scores": scores, "mode": mode}


def analyze_constraint_counts(problem: dict) -> dict:
    """Analyze constraint count with different counting methods."""
    per_trace = problem["per_trace"]

    # Method 1: unique_after_dedup (current)
    unique_dedup = problem["stats"]["unique_after_dedup"]

    # Method 2: Count unique z3_formula strings across all traces (no Z3 equivalence)
    all_formulas = set()
    for t in per_trace:
        for c in t["constraints"]:
            all_formulas.add(c.get("z3_formula", ""))
    unique_formula_str = len(all_formulas - {""})

    # Method 3: Count unique expressions
    all_exprs = set()
    for t in per_trace:
        for c in t["constraints"]:
            all_exprs.add(c.get("expression", ""))
    unique_expr = len(all_exprs - {""})

    # Method 4: Exclude "derived" type (only count facts + rules)
    facts_rules_formulas = set()
    for t in per_trace:
        for c in t["constraints"]:
            if c.get("type") in ("fact", "rule"):
                facts_rules_formulas.add(c.get("z3_formula", ""))
    unique_facts_rules = len(facts_rules_formulas - {""})

    # Method 5: Only "fact" type
    facts_only = set()
    for t in per_trace:
        for c in t["constraints"]:
            if c.get("type") == "fact":
                facts_only.add(c.get("z3_formula", ""))
    unique_facts = len(facts_only - {""})

    # Method 6: Count from unique_constraints (with Z3 dedup), exclude derived
    unique_no_derived = 0
    for uc in problem.get("unique_constraints", []):
        # We don't have type info in unique_constraints, so try matching
        pass

    return {
        "unique_after_z3_dedup": unique_dedup,
        "unique_z3_formula_strings": unique_formula_str,
        "unique_expressions": unique_expr,
        "unique_facts_and_rules_only": unique_facts_rules,
        "unique_facts_only": unique_facts,
        "total_extracted": problem["stats"]["total_extracted"],
        "per_trace_counts": [t["num_constraints"] for t in per_trace],
    }


def main():
    base = Path("/root/symb_invariant_consensus")
    data = json.load(open(base / "results/case_study_constraints.json"))

    exp001_expected = {
        "folio_134": {"sc": "True", "sica": "Unknown", "constraint_count": 7},
        "ProofWriter_AttNoneg-OWA-D5-1066_Q6": {"sc": "False", "sica": "True", "constraint_count": 17},
        "ProofWriter_RelNeg-OWA-D5-903_Q6": {"sc": "False", "sica": "False", "constraint_count": 44},
    }

    results = []

    for problem in data:
        pid = problem["id"]
        gold = problem["gold"]
        print(f"\n{'='*60}")
        print(f"Problem: {pid}  (gold={gold})")
        print(f"{'='*60}")

        # --- Raw answers ---
        raw_answers = [t["answer"] for t in problem["per_trace"]]
        trace_indices = list(range(len(raw_answers)))
        print(f"\nRaw answers: {raw_answers}")
        print(f"Raw SC: {problem['sc_answer']}")
        print(f"Raw SICA: {problem['sica_answer']}")

        # --- Normalize ---
        norm_answers = [normalize_answer(a) for a in raw_answers]
        print(f"\nNormalized answers: {norm_answers}")

        # --- Recompute SC ---
        sc = compute_sc(norm_answers)
        print(f"\nSC after normalization:")
        print(f"  Answer: {sc['answer']}")
        print(f"  Distribution: {sc['distribution']}")
        print(f"  Vote entropy: {sc['vote_entropy']}")

        # --- Recompute SICA ---
        sica = compute_sica(
            norm_answers,
            trace_indices,
            problem["maxsat_satisfied"],
            problem["maxsat_excluded"],
        )
        print(f"\nSICA after normalization:")
        print(f"  Answer: {sica['answer']}")
        print(f"  Scores: {sica['scores']}")
        print(f"  Mode: {sica['mode']}")

        # --- Compare with exp-001 ---
        exp = exp001_expected.get(pid, {})
        print(f"\nComparison with exp-001:")
        print(f"  exp-001 SC={exp.get('sc')}, re-extract SC={sc['answer']}")
        print(f"  exp-001 SICA={exp.get('sica')}, re-extract SICA={sica['answer']}")
        sc_match = sc["answer"] == exp.get("sc")
        sica_match = sica["answer"] == exp.get("sica")
        print(f"  SC match: {sc_match}, SICA match: {sica_match}")

        # --- Constraint count analysis ---
        cc = analyze_constraint_counts(problem)
        print(f"\nConstraint count analysis:")
        print(f"  exp-001 constraint_count: {exp.get('constraint_count')}")
        print(f"  Re-extract unique_after_z3_dedup: {cc['unique_after_z3_dedup']}")
        print(f"  Re-extract unique z3_formula strings: {cc['unique_z3_formula_strings']}")
        print(f"  Re-extract unique expressions: {cc['unique_expressions']}")
        print(f"  Re-extract facts+rules only: {cc['unique_facts_and_rules_only']}")
        print(f"  Re-extract facts only: {cc['unique_facts_only']}")
        print(f"  Total extracted (pre-dedup): {cc['total_extracted']}")
        print(f"  Per-trace: {cc['per_trace_counts']}")

        results.append({
            "id": pid,
            "gold": gold,
            "raw_sc_answer": problem["sc_answer"],
            "raw_sica_answer": problem["sica_answer"],
            "normalized_answers": norm_answers,
            "sc_answer": sc["answer"],
            "sc_distribution": sc["distribution"],
            "sc_vote_entropy": sc["vote_entropy"],
            "sica_answer": sica["answer"],
            "sica_scores": sica["scores"],
            "sica_mode": sica["mode"],
            "sc_correct": sc["answer"].lower() == str(gold).lower(),
            "sica_correct": sica["answer"].lower() == str(gold).lower(),
            "exp001_sc": exp.get("sc"),
            "exp001_sica": exp.get("sica"),
            "sc_matches_exp001": sc_match,
            "sica_matches_exp001": sica_match,
            "constraint_analysis": cc,
            "exp001_constraint_count": exp.get("constraint_count"),
            "maxsat_satisfied_count": problem["stats"]["maxsat_satisfied"],
            "maxsat_excluded_count": problem["stats"]["maxsat_excluded"],
        })

    # Save
    out_path = base / "results/case_study_normalized.json"
    with open(out_path, "w") as f:
        json.dump(results, f, indent=2, ensure_ascii=False)
    print(f"\n\nResults saved to {out_path}")

    # Summary
    print(f"\n{'='*60}")
    print("SUMMARY")
    print(f"{'='*60}")
    for r in results:
        print(f"\n{r['id']}:")
        print(f"  Gold={r['gold']}")
        print(f"  SC={r['sc_answer']} (correct={r['sc_correct']}, matches_exp001={r['sc_matches_exp001']})")
        print(f"  SICA={r['sica_answer']} (correct={r['sica_correct']}, matches_exp001={r['sica_matches_exp001']})")
        print(f"  SC distribution: {r['sc_distribution']}, entropy={r['sc_vote_entropy']}")
        print(f"  SICA scores: {r['sica_scores']}")
        print(f"  Constraints: re-extract={r['constraint_analysis']['unique_after_z3_dedup']}, exp-001={r['exp001_constraint_count']}")


if __name__ == "__main__":
    main()
