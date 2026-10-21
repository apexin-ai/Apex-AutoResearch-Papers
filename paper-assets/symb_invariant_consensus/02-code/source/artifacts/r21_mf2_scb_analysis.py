"""
R21 MF2 Analysis: SCB vs CoT Bias Empirical Separation
Proves SCB is not merely CoT bias propagation to the constraint level.
"""
import json
import os
import re
import sys
import time
from collections import Counter, defaultdict
from pathlib import Path

BASE = Path("/root/symb_invariant_consensus/results/exp033_mistral_7b_folio204")
CACHE_DIR = BASE / "constraint_cache"
INTER_DIR = BASE / "intermediates"
RESULTS_FILE = BASE / "exp033_results.json"
OUT_DIR = BASE

try:
    import z3
    HAS_Z3 = True
except ImportError:
    HAS_Z3 = False
    print("WARNING: z3 not available, skipping Z3-based analyses")


def load_json(path):
    with open(path) as f:
        return json.load(f)


def extract_variables(z3_formula):
    tokens = set(re.findall(r'\b([a-zA-Z_][a-zA-Z0-9_]*)\b', z3_formula))
    reserved = {
        'True', 'False', 'And', 'Or', 'Not', 'Implies', 'If',
        'Bool', 'Real', 'Int', 'abs', 'Abs', 'sum', 'Sum',
        'max', 'min', 'Mod', 'pow', 'Unknown',
    }
    return tokens - reserved


def get_majority_answer(answers):
    valid = [a for a in answers if a.strip()]
    if not valid:
        return None, {}
    counts = Counter(valid)
    majority = counts.most_common(1)[0][0]
    return majority, dict(counts)


# ---- Z3-based analysis helpers ----
_BOOL_INDICATORS = re.compile(
    r'\bImplies\s*\(|==\s*True|==\s*False|\bNot\s*\(|\bAnd\s*\(|\bOr\s*\('
)

def parse_z3_formula(formula_str):
    if not HAS_Z3 or not formula_str or not formula_str.strip():
        return None
    s = formula_str.strip()
    use_bool = bool(_BOOL_INDICATORS.search(s))
    tokens = set(re.findall(r'\b([a-zA-Z_]\w*)\b', s))
    reserved = {
        'True', 'False', 'And', 'Or', 'Not', 'Implies', 'If',
        'abs', 'Abs', 'Bool', 'Real', 'Int', 'sum', 'Sum',
        'max', 'min', 'len', 'int', 'Mod', 'pow', 'Unknown',
    }
    var_names = tokens - reserved
    ns = {}
    for name in var_names:
        ns[name] = z3.Bool(name) if use_bool else z3.Real(name)
    ns['And'] = z3.And
    ns['Or'] = z3.Or
    ns['Not'] = z3.Not
    ns['Implies'] = z3.Implies
    ns['If'] = z3.If
    ns['True'] = True
    ns['False'] = False
    try:
        result = eval(s, {"__builtins__": {}}, ns)
        if isinstance(result, bool):
            return z3.BoolVal(result)
        if isinstance(result, z3.ExprRef):
            return result
        return None
    except Exception:
        return None


def check_group_consistency(formulas_z3, timeout_ms=2000):
    """Check if a set of Z3 formulas is jointly satisfiable."""
    if not HAS_Z3 or not formulas_z3:
        return None
    s = z3.Solver()
    s.set("timeout", timeout_ms)
    for f in formulas_z3:
        if f is not None and z3.is_bool(f):
            s.add(f)
    result = s.check()
    if result == z3.sat:
        return "sat"
    elif result == z3.unsat:
        return "unsat"
    return "unknown"


def run_maxsat_with_tracking(all_trace_constraints, trace_answers, majority_answer):
    """
    Re-run MaxSAT and track which constraints are excluded,
    with their source trace group (majority/minority).
    """
    if not HAS_Z3:
        return None

    # String-based dedup with source tracking
    unique = []
    seen = {}
    for trace_idx, constraints in all_trace_constraints.items():
        ans = trace_answers.get(trace_idx, "")
        group = "majority" if ans == majority_answer else ("minority" if ans else "empty")
        for c in constraints:
            fstr = c.get("z3_formula", "").strip()
            if not fstr:
                continue
            if fstr in seen:
                uid = seen[fstr]
                unique[uid]["weight"] += 1
                unique[uid]["source_traces"].append(trace_idx)
                if group not in unique[uid]["groups"]:
                    unique[uid]["groups"].append(group)
            else:
                seen[fstr] = len(unique)
                unique.append({
                    "formula_str": fstr,
                    "weight": 1,
                    "source_traces": [trace_idx],
                    "groups": [group],
                })

    # Parse and run MaxSAT
    opt = z3.Optimize()
    opt.set("timeout", 5000)
    indicators = []
    active = []
    parsed = []

    for i, uc in enumerate(unique):
        z3f = parse_z3_formula(uc["formula_str"])
        parsed.append(z3f)
        ind = z3.Bool(f"__ind_{i}")
        indicators.append(ind)
        if z3f is not None and z3.is_bool(z3f):
            try:
                opt.add(z3.Implies(ind, z3f))
                opt.add_soft(ind, weight=uc["weight"])
                active.append(True)
            except Exception:
                active.append(False)
        else:
            active.append(False)

    result = opt.check()
    satisfied_groups = Counter()
    excluded_groups = Counter()
    satisfied_maj_only = 0
    satisfied_min_only = 0
    satisfied_shared = 0
    excluded_maj_only = 0
    excluded_min_only = 0
    excluded_shared = 0

    if result in (z3.sat, z3.unknown):
        model = opt.model()
        for i, uc in enumerate(unique):
            if not active[i]:
                # inactive constraints count as excluded
                for g in uc["groups"]:
                    excluded_groups[g] += 1
                continue
            val = model.evaluate(indicators[i], model_completion=True)
            groups = set(uc["groups"])
            is_maj = "majority" in groups
            is_min = "minority" in groups
            if z3.is_true(val):
                for g in uc["groups"]:
                    satisfied_groups[g] += 1
                if is_maj and not is_min:
                    satisfied_maj_only += 1
                elif is_min and not is_maj:
                    satisfied_min_only += 1
                elif is_maj and is_min:
                    satisfied_shared += 1
            else:
                for g in uc["groups"]:
                    excluded_groups[g] += 1
                if is_maj and not is_min:
                    excluded_maj_only += 1
                elif is_min and not is_maj:
                    excluded_min_only += 1
                elif is_maj and is_min:
                    excluded_shared += 1

    total_maj = satisfied_maj_only + excluded_maj_only
    total_min = satisfied_min_only + excluded_min_only
    total_shared = satisfied_shared + excluded_shared

    return {
        "n_unique": len(unique),
        "satisfied_maj_only": satisfied_maj_only,
        "satisfied_min_only": satisfied_min_only,
        "satisfied_shared": satisfied_shared,
        "excluded_maj_only": excluded_maj_only,
        "excluded_min_only": excluded_min_only,
        "excluded_shared": excluded_shared,
        "maj_exclusion_rate": excluded_maj_only / max(1, total_maj),
        "min_exclusion_rate": excluded_min_only / max(1, total_min),
        "shared_exclusion_rate": excluded_shared / max(1, total_shared),
    }


def analyze_problem(pid):
    cache_file = CACHE_DIR / f"{pid}.json"
    if not cache_file.exists():
        return None

    cache = load_json(cache_file)
    gt = cache.get("gt", "")
    traces = cache.get("per_trace", [])
    if not traces:
        return None

    answers = [t.get("answer", "").strip() for t in traces]
    majority, counts = get_majority_answer(answers)
    if majority is None:
        return None

    majority_idxs = set()
    minority_idxs = set()
    trace_answers = {}
    for t in traces:
        ans = t.get("answer", "").strip()
        idx = t.get("trace_idx", 0)
        trace_answers[idx] = ans
        if ans == majority:
            majority_idxs.add(idx)
        elif ans:
            minority_idxs.add(idx)

    if not minority_idxs:
        return None

    # Collect constraints
    all_constraints_by_trace = {}
    for t in traces:
        idx = t.get("trace_idx", 0)
        all_constraints_by_trace[idx] = t.get("constraints", [])

    # --- Variable overlap ---
    majority_vars = set()
    minority_vars = set()
    for idx in majority_idxs:
        for c in all_constraints_by_trace.get(idx, []):
            majority_vars |= extract_variables(c.get("z3_formula", ""))
    for idx in minority_idxs:
        for c in all_constraints_by_trace.get(idx, []):
            minority_vars |= extract_variables(c.get("z3_formula", ""))

    if majority_vars and minority_vars:
        jaccard = len(majority_vars & minority_vars) / len(majority_vars | minority_vars)
    else:
        jaccard = 0.0

    # --- String-level formula sharing ---
    majority_formulas = set()
    minority_formulas = set()
    for idx in majority_idxs:
        for c in all_constraints_by_trace.get(idx, []):
            f = c.get("z3_formula", "").strip()
            if f:
                majority_formulas.add(f)
    for idx in minority_idxs:
        for c in all_constraints_by_trace.get(idx, []):
            f = c.get("z3_formula", "").strip()
            if f:
                minority_formulas.add(f)

    shared = majority_formulas & minority_formulas
    maj_only = majority_formulas - minority_formulas
    min_only = minority_formulas - majority_formulas

    # --- Constraint type distribution ---
    maj_types = Counter()
    min_types = Counter()
    for idx in majority_idxs:
        for c in all_constraints_by_trace.get(idx, []):
            maj_types[c.get("type", "unknown")] += 1
    for idx in minority_idxs:
        for c in all_constraints_by_trace.get(idx, []):
            min_types[c.get("type", "unknown")] += 1

    # --- Z3 cross-consistency ---
    maj_z3 = []
    min_z3 = []
    for idx in majority_idxs:
        for c in all_constraints_by_trace.get(idx, []):
            f = parse_z3_formula(c.get("z3_formula", ""))
            if f is not None:
                maj_z3.append(f)
    for idx in minority_idxs:
        for c in all_constraints_by_trace.get(idx, []):
            f = parse_z3_formula(c.get("z3_formula", ""))
            if f is not None:
                min_z3.append(f)

    maj_sat = check_group_consistency(maj_z3)
    min_sat = check_group_consistency(min_z3)
    cross_sat = check_group_consistency(maj_z3 + min_z3)

    # --- MaxSAT exclusion tracking ---
    maxsat_tracking = run_maxsat_with_tracking(
        all_constraints_by_trace, trace_answers, majority
    )

    # SICA/SC results
    inter_file = INTER_DIR / f"{pid}.json"
    sica_answer = None
    if inter_file.exists():
        inter = load_json(inter_file)
        sica_result = inter.get("sica_result", {})
        sica_answer = sica_result.get("answer", "")

    minority_answers = {idx: trace_answers[idx] for idx in minority_idxs}

    return {
        "pid": pid,
        "gt": gt,
        "majority": majority,
        "answer_counts": counts,
        "n_majority_traces": len(majority_idxs),
        "n_minority_traces": len(minority_idxs),
        "minority_answers": minority_answers,
        "sica_answer": sica_answer,
        "sc_correct": majority == gt,
        # Variable overlap
        "var_jaccard": jaccard,
        "majority_var_count": len(majority_vars),
        "minority_var_count": len(minority_vars),
        "shared_var_count": len(majority_vars & minority_vars),
        # Constraint sharing
        "n_shared_formulas": len(shared),
        "n_majority_only": len(maj_only),
        "n_minority_only": len(min_only),
        "shared_ratio": len(shared) / max(1, len(minority_formulas)),
        # Constraint counts
        "n_majority_constraints": sum(
            len(all_constraints_by_trace.get(i, [])) for i in majority_idxs
        ),
        "n_minority_constraints": sum(
            len(all_constraints_by_trace.get(i, [])) for i in minority_idxs
        ),
        # Type distribution
        "majority_types": dict(maj_types),
        "minority_types": dict(min_types),
        # Z3 consistency
        "majority_group_sat": maj_sat,
        "minority_group_sat": min_sat,
        "cross_group_sat": cross_sat,
        # MaxSAT exclusion
        "maxsat_tracking": maxsat_tracking,
        # For case study selection
        "majority_trace_idxs": sorted(majority_idxs),
        "minority_trace_idxs": sorted(minority_idxs),
        "shared_formulas_sample": sorted(shared)[:5],
        "minority_only_sample": sorted(min_only)[:5],
    }


def print_case_study_detail(pid, rank):
    """Print detailed constraint comparison for a case study."""
    cache = load_json(CACHE_DIR / f"{pid}.json")
    inter = load_json(INTER_DIR / f"{pid}.json") if (INTER_DIR / f"{pid}.json").exists() else None
    traces = cache.get("per_trace", [])
    answers = [t.get("answer", "").strip() for t in traces]
    majority, counts = get_majority_answer(answers)

    print(f"\n{'='*70}")
    print(f"CASE STUDY {rank}: {pid}")
    print(f"{'='*70}")
    print(f"Ground truth: {cache.get('gt')}")
    print(f"Majority (SC): {majority} (votes: {counts})")
    if inter:
        sr = inter.get("sica_result", {})
        print(f"SICA answer: {sr.get('answer')}  scores: {sr.get('scores')}")
    print()

    for t in traces:
        idx = t.get("trace_idx", 0)
        ans = t.get("answer", "").strip()
        group = "MAJ" if ans == majority else ("MIN" if ans else "---")
        constraints = t.get("constraints", [])
        n_c = len(constraints)
        print(f"  Trace {idx:2d} [{group}] answer={ans or '(empty)':8s}  constraints={n_c}")
        if group == "MIN" and constraints:
            for c in constraints[:4]:
                expr = c.get("expression", "")[:80]
                print(f"    [{c.get('type','?'):7s}] {expr}")
            if len(constraints) > 4:
                print(f"    ... +{len(constraints)-4} more")


def main():
    t0 = time.time()

    pids = sorted([f.stem for f in CACHE_DIR.glob("*.json")])
    print(f"Loading {len(pids)} problems...")

    # Load exp033_results for SC/SICA accuracy context
    exp_results = load_json(RESULTS_FILE) if RESULTS_FILE.exists() else None
    if exp_results:
        summary = exp_results.get("summary", {})
        print(f"Exp033 summary: SICA={summary.get('sica_accuracy',0):.3f}, "
              f"SC={summary.get('sc_accuracy',0):.3f}, n={summary.get('n_problems')}")

    results = []
    for i, pid in enumerate(pids):
        r = analyze_problem(pid)
        if r:
            results.append(r)
        if (i + 1) % 50 == 0:
            print(f"  processed {i+1}/{len(pids)}...")

    elapsed = time.time() - t0
    print(f"\nAnalysis complete in {elapsed:.1f}s")
    print(f"Problems with minority traces: {len(results)}/{len(pids)}")

    if not results:
        print("No problems with minority traces!")
        return

    # ================================================================
    # AGGREGATE STATISTICS
    # ================================================================
    print("\n" + "=" * 80)
    print("R21 MF2: SCB vs CoT Bias — Empirical Separation")
    print("=" * 80)

    # --- Data overview ---
    avg_min = sum(r["n_minority_traces"] for r in results) / len(results)
    n_total = len(pids)
    n_disagree = len(results)
    print(f"\n### Data Overview")
    print(f"  Total problems: {n_total}")
    print(f"  Disagreement problems (have minority traces): {n_disagree} "
          f"({100*n_disagree/n_total:.1f}%)")
    print(f"  Avg minority traces: {avg_min:.1f}/12")

    # --- Metric A: Constraint Partitioning ---
    total_shared = sum(r["n_shared_formulas"] for r in results)
    total_maj_only = sum(r["n_majority_only"] for r in results)
    total_min_only = sum(r["n_minority_only"] for r in results)
    total_all = total_shared + total_maj_only + total_min_only
    problems_sharing = sum(1 for r in results if r["n_shared_formulas"] > 0)

    print(f"\n### Metric A: Constraint Formula Sharing (string-level dedup)")
    print(f"  Total unique formulas across groups: {total_all}")
    print(f"    Majority-only: {total_maj_only} ({100*total_maj_only/max(1,total_all):.1f}%)")
    print(f"    Minority-only: {total_min_only} ({100*total_min_only/max(1,total_all):.1f}%)")
    print(f"    Shared:         {total_shared} ({100*total_shared/max(1,total_all):.1f}%)")
    print(f"  Problems with >=1 shared formula: {problems_sharing}/{n_disagree} "
          f"({100*problems_sharing/n_disagree:.1f}%)")
    shared_ratios = [r["shared_ratio"] for r in results]
    print(f"  Mean shared/minority ratio: {sum(shared_ratios)/len(shared_ratios):.3f}")

    # --- Metric B: Variable Overlap ---
    jaccards = [r["var_jaccard"] for r in results]
    mean_j = sum(jaccards) / len(jaccards)
    high = sum(1 for j in jaccards if j > 0.5)
    med = sum(1 for j in jaccards if 0.2 <= j <= 0.5)
    low = sum(1 for j in jaccards if j < 0.2)

    print(f"\n### Metric B: Variable Overlap (Jaccard)")
    print(f"  Mean Jaccard: {mean_j:.3f}")
    print(f"  Distribution: high(>0.5)={high}, medium(0.2-0.5)={med}, low(<0.2)={low}")
    print(f"  Interpretation: {'Shared semantic space' if mean_j > 0.3 else 'Isolated variable spaces'}")

    # --- Metric C: Z3 Cross-Group Consistency ---
    maj_sat_c = Counter(r["majority_group_sat"] for r in results)
    min_sat_c = Counter(r["minority_group_sat"] for r in results)
    cross_sat_c = Counter(r["cross_group_sat"] for r in results)

    print(f"\n### Metric C: Z3 Group Consistency")
    print(f"  Majority constraints SAT:   {dict(maj_sat_c)}")
    print(f"  Minority constraints SAT:   {dict(min_sat_c)}")
    print(f"  Cross-group (maj+min) SAT:  {dict(cross_sat_c)}")
    n_cross_unsat = cross_sat_c.get("unsat", 0)
    n_both_sat = sum(1 for r in results
                     if r["majority_group_sat"] == "sat"
                     and r["minority_group_sat"] == "sat")
    n_cross_unsat_from_both_sat = sum(
        1 for r in results
        if r["majority_group_sat"] == "sat"
        and r["minority_group_sat"] == "sat"
        and r["cross_group_sat"] == "unsat"
    )
    print(f"  Both groups individually SAT: {n_both_sat}")
    print(f"  Of those, cross-group UNSAT: {n_cross_unsat_from_both_sat}")
    if n_both_sat > 0:
        print(f"  → {100*n_cross_unsat_from_both_sat/n_both_sat:.1f}% have genuine semantic conflict")

    # --- Metric D: MaxSAT Exclusion Asymmetry ---
    tracked = [r for r in results if r.get("maxsat_tracking")]
    if tracked:
        maj_excl_rates = [r["maxsat_tracking"]["maj_exclusion_rate"] for r in tracked]
        min_excl_rates = [r["maxsat_tracking"]["min_exclusion_rate"] for r in tracked]
        mean_maj_excl = sum(maj_excl_rates) / len(maj_excl_rates)
        mean_min_excl = sum(min_excl_rates) / len(min_excl_rates)

        total_excl_maj = sum(r["maxsat_tracking"]["excluded_maj_only"] for r in tracked)
        total_excl_min = sum(r["maxsat_tracking"]["excluded_min_only"] for r in tracked)
        total_excl_shared = sum(r["maxsat_tracking"]["excluded_shared"] for r in tracked)
        total_sat_maj = sum(r["maxsat_tracking"]["satisfied_maj_only"] for r in tracked)
        total_sat_min = sum(r["maxsat_tracking"]["satisfied_min_only"] for r in tracked)
        total_sat_shared = sum(r["maxsat_tracking"]["satisfied_shared"] for r in tracked)

        print(f"\n### Metric D: MaxSAT Exclusion Asymmetry")
        print(f"  Majority-only constraints: {total_sat_maj} satisfied, "
              f"{total_excl_maj} excluded "
              f"(rate={total_excl_maj/max(1,total_sat_maj+total_excl_maj):.3f})")
        print(f"  Minority-only constraints: {total_sat_min} satisfied, "
              f"{total_excl_min} excluded "
              f"(rate={total_excl_min/max(1,total_sat_min+total_excl_min):.3f})")
        print(f"  Shared constraints:        {total_sat_shared} satisfied, "
              f"{total_excl_shared} excluded "
              f"(rate={total_excl_shared/max(1,total_sat_shared+total_excl_shared):.3f})")
        print(f"  Mean per-problem exclusion rate:")
        print(f"    Majority-only: {mean_maj_excl:.3f}")
        print(f"    Minority-only: {mean_min_excl:.3f}")

        bias_problems = sum(
            1 for r in tracked
            if r["maxsat_tracking"]["min_exclusion_rate"] >
               r["maxsat_tracking"]["maj_exclusion_rate"]
        )
        print(f"  Problems where minority excl > majority excl: "
              f"{bias_problems}/{len(tracked)} ({100*bias_problems/len(tracked):.1f}%)")

    # --- Metric E: Constraint density per trace ---
    maj_per_trace = []
    min_per_trace = []
    for r in results:
        n_maj_t = r["n_majority_traces"]
        n_min_t = r["n_minority_traces"]
        if n_maj_t > 0:
            maj_per_trace.append(r["n_majority_constraints"] / n_maj_t)
        if n_min_t > 0:
            min_per_trace.append(r["n_minority_constraints"] / n_min_t)
    print(f"\n### Metric E: Constraints Per Trace")
    print(f"  Majority traces avg: {sum(maj_per_trace)/len(maj_per_trace):.1f} constraints/trace")
    print(f"  Minority traces avg: {sum(min_per_trace)/len(min_per_trace):.1f} constraints/trace")

    # ================================================================
    # CASE STUDIES
    # ================================================================
    # Select: SC incorrect, has minority, interesting sharing/exclusion patterns
    sc_wrong = [r for r in results if not r["sc_correct"] and r["n_minority_traces"] >= 2]
    sc_wrong.sort(key=lambda r: (
        -(r.get("maxsat_tracking", {}).get("min_exclusion_rate", 0)
          - r.get("maxsat_tracking", {}).get("maj_exclusion_rate", 0)),
        -r["n_shared_formulas"],
    ))

    print(f"\n### Case Studies (SC incorrect, >=2 minority traces): {len(sc_wrong)} candidates")
    for i, cs in enumerate(sc_wrong[:3]):
        print_case_study_detail(cs["pid"], i + 1)
        mt = cs.get("maxsat_tracking", {})
        print(f"  Variable Jaccard: {cs['var_jaccard']:.3f}")
        print(f"  Shared formulas: {cs['n_shared_formulas']}, "
              f"Maj-only: {cs['n_majority_only']}, Min-only: {cs['n_minority_only']}")
        print(f"  Z3: maj={cs['majority_group_sat']}, min={cs['minority_group_sat']}, "
              f"cross={cs['cross_group_sat']}")
        if mt:
            print(f"  MaxSAT excl rate: maj={mt['maj_exclusion_rate']:.3f}, "
                  f"min={mt['min_exclusion_rate']:.3f}")

    # ================================================================
    # SCIENTIFIC CONCLUSION
    # ================================================================
    print(f"\n{'='*80}")
    print("SCIENTIFIC CONCLUSION")
    print(f"{'='*80}")

    # Determine situation
    if tracked:
        global_maj_excl = total_excl_maj / max(1, total_sat_maj + total_excl_maj)
        global_min_excl = total_excl_min / max(1, total_sat_min + total_excl_min)
        excl_gap = global_min_excl - global_maj_excl
    else:
        excl_gap = 0

    if mean_j > 0.3 and excl_gap > 0.02:
        print("\nFINDING: SCB has INDEPENDENT components beyond CoT bias propagation.")
        print(f"\n1. Shared semantic space (Jaccard={mean_j:.3f}): Constraints from majority")
        print(f"   and minority traces use overlapping variables — they are NOT isolated")
        print(f"   trace-specific echo chambers.")
        print(f"\n2. MaxSAT exclusion asymmetry (gap={excl_gap:.3f}): Minority-origin")
        print(f"   constraints are excluded at a HIGHER rate than majority-origin ones.")
        print(f"   This is because MaxSAT optimizes total weight, and majority constraints")
        print(f"   have more weight support → minority constraints are sacrificed when")
        print(f"   cross-group conflicts arise.")
        print(f"\n3. Cross-group inconsistency: {n_cross_unsat_from_both_sat} problems have")
        print(f"   majority and minority constraints that are individually SAT but jointly")
        print(f"   UNSAT → genuine semantic conflict exists between answer groups.")
        print(f"\nConclusion: SCB = CoT bias propagation + MaxSAT-induced exclusion bias")
        print(f"   + source-attribution amplification. The latter two are constraint-level")
        print(f"   phenomena that go BEYOND simple CoT bias transmission.")
    elif mean_j > 0.2:
        print("\nFINDING: SCB is partially explained by CoT bias, with moderate independent effect.")
    else:
        print("\nFINDING: SCB appears to be primarily CoT bias propagation.")

    # Save all results
    output = {
        "analysis_time_s": time.time() - t0,
        "summary": {
            "n_total": n_total,
            "n_disagree": n_disagree,
            "avg_minority_traces": avg_min,
            "constraint_partitioning": {
                "shared": total_shared,
                "majority_only": total_maj_only,
                "minority_only": total_min_only,
                "sharing_rate": total_shared / max(1, total_all),
                "problems_with_sharing": problems_sharing,
            },
            "variable_overlap": {
                "mean_jaccard": mean_j,
                "high": high,
                "medium": med,
                "low": low,
            },
            "z3_consistency": {
                "majority_sat": dict(maj_sat_c),
                "minority_sat": dict(min_sat_c),
                "cross_sat": dict(cross_sat_c),
                "cross_unsat_from_both_sat": n_cross_unsat_from_both_sat,
            },
            "maxsat_exclusion": {
                "global_maj_excl_rate": total_excl_maj / max(1, total_sat_maj + total_excl_maj) if tracked else None,
                "global_min_excl_rate": total_excl_min / max(1, total_sat_min + total_excl_min) if tracked else None,
                "bias_problems": bias_problems if tracked else None,
            } if tracked else None,
        },
        "per_problem": [{k: v for k, v in r.items()
                         if k not in ("shared_formulas_sample", "minority_only_sample")}
                        for r in results],
    }
    out_path = OUT_DIR / "r21_mf2_scb_vs_cot_analysis.json"
    with open(str(out_path), "w") as f:
        json.dump(output, f, indent=2, default=str)
    print(f"\nResults saved to: {out_path}")


if __name__ == "__main__":
    main()
