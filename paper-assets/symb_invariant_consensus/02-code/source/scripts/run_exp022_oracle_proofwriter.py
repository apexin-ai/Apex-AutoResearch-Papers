"""
Exp-022: Oracle-SICA on ProofWriter OWA-D5 (600 problems)
Uses gold DSL (raw_logic_programs) from ProofWriter + Z3 consistency checking
to weight Qwen2.5-14B K=12 traces via MAX-SAT aggregation.
Compares Oracle-SICA vs SC vs SICA(self-extracted).

Input:
  - /root/autodl-tmp/crdd/data/proofwriter/proofwriter-OWA-D5-validation.jsonl (gold DSL)
  - /root/symb_invariant_consensus/results/sica_expanded_14b.json (K=12 traces)

Output:
  - /root/symb_invariant_consensus/results/exp022_oracle_proofwriter.json
"""

import json
import re
import sys
import time
from collections import Counter
from pathlib import Path

import z3

PROJECT_ROOT = Path("/root/symb_invariant_consensus")
DATA_PATH = Path("/root/autodl-tmp/crdd/data/proofwriter/proofwriter-OWA-D5-validation.jsonl")
TRACES_PATH = PROJECT_ROOT / "results" / "sica_expanded_14b.json"
OUTPUT_PATH = PROJECT_ROOT / "results" / "exp022_oracle_proofwriter.json"


# ============================================================
# ProofWriter DSL -> Z3 Parser
# ============================================================

class DSLParseError(Exception):
    pass


class ProofWriterDSLToZ3:
    """Parse ProofWriter raw_logic_programs DSL into Z3 expressions.

    DSL format:
      Predicates: Pred($x, bool) or Pred($x, $y, bool)
      Facts: Pred(Entity, True/False) or NotPred(Entity, True)
      Rules: Cond1 && Cond2 >>> Conclusion
      Query: Pred(Entity, True/False)
    """

    def __init__(self):
        self.entity_sort = z3.DeclareSort("Entity")
        self.predicates = {}   # name -> (arity, z3.Function)
        self.constants = {}    # name -> z3.Const
        self.declared_pred_names = set()

    def get_constant(self, name):
        name = name.strip()
        if name not in self.constants:
            self.constants[name] = z3.Const(name, self.entity_sort)
        return self.constants[name]

    def get_predicate(self, name, arity):
        key = (name, arity)
        if key not in self.predicates:
            if arity == 1:
                self.predicates[key] = z3.Function(name, self.entity_sort, z3.BoolSort())
            elif arity == 2:
                self.predicates[key] = z3.Function(name, self.entity_sort, self.entity_sort, z3.BoolSort())
            else:
                sorts = [self.entity_sort] * arity + [z3.BoolSort()]
                self.predicates[key] = z3.Function(name, *sorts)
        return self.predicates[key]

    def parse_dsl(self, dsl_text):
        """Parse full DSL text. Returns (premises_z3, conclusion_z3)."""
        sections = self._split_sections(dsl_text)
        self._parse_predicates(sections.get("Predicates", ""))
        premises = []
        premises.extend(self._parse_facts(sections.get("Facts", "")))
        premises.extend(self._parse_rules(sections.get("Rules", "")))
        conclusion = self._parse_query(sections.get("Query", ""))
        return premises, conclusion

    def _split_sections(self, text):
        sections = {}
        current_section = None
        current_lines = []
        for line in text.split("\n"):
            stripped = line.strip()
            if stripped in ("Predicates:", "Facts:", "Rules:", "Query:"):
                if current_section is not None:
                    sections[current_section] = "\n".join(current_lines)
                current_section = stripped[:-1]
                current_lines = []
            elif stripped.endswith(":") and stripped[:-1] in ("Predicates", "Facts", "Rules", "Query"):
                if current_section is not None:
                    sections[current_section] = "\n".join(current_lines)
                current_section = stripped[:-1]
                current_lines = []
            else:
                if current_section is not None:
                    current_lines.append(line)
        if current_section is not None:
            sections[current_section] = "\n".join(current_lines)
        return sections

    def _parse_predicates(self, text):
        """Register declared predicate names and arities."""
        for line in text.strip().split("\n"):
            line = line.split(":::")[0].strip()
            if not line:
                continue
            m = re.match(r'(\w+)\((.+)\)', line)
            if not m:
                continue
            name = m.group(1)
            args = [a.strip() for a in m.group(2).split(",")]
            # Last arg is 'bool', entity args are $x, $y, etc.
            entity_args = [a for a in args if a != "bool"]
            arity = len(entity_args)
            self.declared_pred_names.add(name)
            self.get_predicate(name, arity)

    def _parse_atomic(self, text):
        """Parse an atomic formula like Pred(arg1, arg2, True/False) or NotPred(arg1, True).
        Returns (z3_expr, variables_used_set)."""
        text = text.strip()
        m = re.match(r'(\w+)\((.+)\)', text)
        if not m:
            raise DSLParseError(f"Cannot parse atomic: {text!r}")
        raw_name = m.group(1)
        raw_args = [a.strip() for a in m.group(2).split(",")]

        # Last arg is True/False
        if raw_args[-1] not in ("True", "False"):
            raise DSLParseError(f"Expected True/False as last arg in: {text!r}")
        is_positive = raw_args[-1] == "True"
        entity_args_raw = raw_args[:-1]

        # Handle NotPred pattern: if name starts with "Not" and remaining is a declared pred
        negated_prefix = False
        pred_name = raw_name
        if raw_name.startswith("Not") and len(raw_name) > 3:
            candidate = raw_name[3:]
            if candidate in self.declared_pred_names:
                pred_name = candidate
                negated_prefix = True

        arity = len(entity_args_raw)
        pred_func = self.get_predicate(pred_name, arity)

        variables = set()
        z3_args = []
        for arg in entity_args_raw:
            if arg.startswith("$"):
                var_name = arg[1:]
                variables.add(var_name)
                z3_args.append(z3.Const(var_name, self.entity_sort))
            else:
                z3_args.append(self.get_constant(arg))

        expr = pred_func(*z3_args)

        # Apply negation: NotPred(x, True) = Not(pred(x)), Pred(x, False) = Not(pred(x))
        if negated_prefix:
            expr = z3.Not(expr)
            if not is_positive:
                # NotPred(x, False) = Not(Not(pred(x))) = pred(x)
                expr = z3.Not(expr)
        else:
            if not is_positive:
                expr = z3.Not(expr)

        return expr, variables

    def _parse_facts(self, text):
        """Parse Facts section into Z3 assertions."""
        facts = []
        for line in text.strip().split("\n"):
            line = line.split(":::")[0].strip()
            if not line:
                continue
            expr, variables = self._parse_atomic(line)
            if variables:
                raise DSLParseError(f"Variables in fact: {line!r}")
            facts.append(expr)
        return facts

    def _parse_rules(self, text):
        """Parse Rules section into Z3 ForAll/Implies."""
        rules = []
        for line in text.strip().split("\n"):
            line = line.split(":::")[0].strip()
            if not line:
                continue
            if ">>>" not in line:
                raise DSLParseError(f"No >>> in rule: {line!r}")
            parts = line.split(">>>")
            cond_text = parts[0].strip()
            concl_text = parts[1].strip()

            all_vars = set()

            # Parse conditions (split by &&)
            cond_parts = [c.strip() for c in cond_text.split("&&")]
            cond_exprs = []
            for cp in cond_parts:
                expr, vs = self._parse_atomic(cp)
                cond_exprs.append(expr)
                all_vars |= vs

            # Parse conclusion
            concl_expr, vs = self._parse_atomic(concl_text)
            all_vars |= vs

            if len(cond_exprs) == 1:
                antecedent = cond_exprs[0]
            else:
                antecedent = z3.And(*cond_exprs)

            rule_expr = z3.Implies(antecedent, concl_expr)

            if all_vars:
                z3_vars = [z3.Const(v, self.entity_sort) for v in sorted(all_vars)]
                rule_expr = z3.ForAll(z3_vars, rule_expr)

            rules.append(rule_expr)
        return rules

    def _parse_query(self, text):
        """Parse Query section, return conclusion Z3 expression."""
        for line in text.strip().split("\n"):
            line = line.split(":::")[0].strip()
            if not line:
                continue
            expr, variables = self._parse_atomic(line)
            if variables:
                raise DSLParseError(f"Variables in query: {line!r}")
            return expr
        raise DSLParseError("Empty query section")


# ============================================================
# Z3 Entailment Checking (reused from exp-021)
# ============================================================

def check_entailment(premises_z3, conclusion_z3, timeout_ms=5000):
    solver = z3.Solver()
    solver.set("timeout", timeout_ms)
    for p in premises_z3:
        solver.add(p)
    solver.add(z3.Not(conclusion_z3))
    result = solver.check()
    if result == z3.unsat:
        return True
    elif result == z3.sat:
        return False
    else:
        return None


def normalize_answer(ans):
    ans = ans.strip()
    if ans in ('True', 'False', 'Unknown'):
        return ans
    cleaned = re.sub(r'\\+text\{(\w+)\}', r'\1', ans)
    if cleaned in ('True', 'False', 'Unknown'):
        return cleaned
    return ans


def check_consistency_for_answer(premises_z3, conclusion_z3, candidate_answer, timeout_ms=5000):
    """Check if candidate_answer is consistent with Z3 entailment result.
    Returns 1 (consistent), 0 (inconsistent), -1 (solver error)."""
    entails_true = check_entailment(premises_z3, conclusion_z3, timeout_ms)
    entails_false = check_entailment(premises_z3, z3.Not(conclusion_z3), timeout_ms)

    if entails_true is None and entails_false is None:
        return -1

    if candidate_answer == "True":
        return 1 if entails_true == True else 0
    elif candidate_answer == "False":
        return 1 if entails_false == True else 0
    elif candidate_answer == "Unknown":
        if entails_true == True or entails_false == True:
            return 0
        else:
            return 1
    else:
        return -1


# ============================================================
# Aggregation (reused from exp-021)
# ============================================================

def maxsat_aggregate(trace_answers, consistency_scores):
    weighted_votes = Counter()
    for ans, score in zip(trace_answers, consistency_scores):
        if score == 1:
            weighted_votes[ans] += 1.0
        elif score == 0:
            weighted_votes[ans] += 0.0
        else:
            weighted_votes[ans] += 0.5

    if not weighted_votes or max(weighted_votes.values()) == 0:
        return Counter(trace_answers).most_common(1)[0][0]

    max_weight = max(weighted_votes.values())
    candidates = [a for a, w in weighted_votes.items() if w == max_weight]

    if len(candidates) == 1:
        return candidates[0]
    raw_votes = Counter(trace_answers)
    candidates.sort(key=lambda a: raw_votes.get(a, 0), reverse=True)
    return candidates[0]


def sc_aggregate(trace_answers):
    votes = Counter(trace_answers)
    return votes.most_common(1)[0][0]


# ============================================================
# Statistics
# ============================================================

def mcnemar_test(correct_a, correct_b):
    b_count = sum(1 for a, b in zip(correct_a, correct_b) if a and not b)
    c_count = sum(1 for a, b in zip(correct_a, correct_b) if not a and b)
    if b_count + c_count == 0:
        return 1.0
    chi2_val = (abs(b_count - c_count) - 1) ** 2 / (b_count + c_count)
    from scipy.stats import chi2 as chi2_dist
    p_value = 1 - chi2_dist.cdf(chi2_val, df=1)
    return p_value


def bootstrap_ci(correct, n_bootstrap=10000, seed=42):
    import numpy as np
    rng = np.random.RandomState(seed)
    n = len(correct)
    accs = []
    for _ in range(n_bootstrap):
        idx = rng.choice(n, n, replace=True)
        accs.append(sum(correct[i] for i in idx) / n)
    accs.sort()
    lo = accs[int(0.025 * n_bootstrap)]
    hi = accs[int(0.975 * n_bootstrap)]
    return lo, hi


def answer_label_to_text(label):
    """Convert ProofWriter answer label (A/B/C) to True/False/Unknown."""
    return {"A": "True", "B": "False", "C": "Unknown"}.get(label, label)


def get_subtype(problem_id):
    """Extract subtype from problem ID like ProofWriter_AttNoneg-OWA-D5-1041_Q1."""
    m = re.match(r'ProofWriter_(\w+)-OWA', problem_id)
    return m.group(1) if m else "Unknown"


# ============================================================
# Main
# ============================================================

def main():
    print("=" * 60)
    print("Exp-022: Oracle-SICA on ProofWriter OWA-D5")
    print("=" * 60)

    # Load gold DSL data
    gold_data = {}
    with open(DATA_PATH) as f:
        for line in f:
            item = json.loads(line)
            gold_data[item["id"]] = item
    print(f"Loaded {len(gold_data)} ProofWriter problems with gold DSL.")

    # Load traces
    with open(TRACES_PATH) as f:
        traces_data = json.load(f)
    pw_traces = [r for r in traces_data["results"] if r.get("dataset") == "proofwriter"]
    print(f"Loaded {len(pw_traces)} ProofWriter trace results (Qwen-14B, K=12).")

    trace_by_id = {r["problem_id"]: r for r in pw_traces}
    common_ids = set(trace_by_id.keys()) & set(gold_data.keys())
    print(f"Common problem IDs: {len(common_ids)}")

    if len(common_ids) != 600:
        print(f"WARNING: Expected 600, got {len(common_ids)}")

    # ---- Phase 1: Validation (2 per subtype = 8 problems) ----
    print("\n" + "-" * 40)
    print("Phase 1: Per-subtype validation")
    print("-" * 40)

    subtypes = ["AttNoneg", "AttNeg", "RelNoneg", "RelNeg"]
    subtype_ids = {st: [] for st in subtypes}
    for pid in sorted(common_ids):
        st = get_subtype(pid)
        if st in subtype_ids:
            subtype_ids[st].append(pid)

    val_ok = 0
    val_total = 0
    for st in subtypes:
        for pid in subtype_ids[st][:2]:
            gold = gold_data[pid]
            dsl_text = gold["raw_logic_programs"][0]
            gold_answer = answer_label_to_text(gold["answer"])
            parser = ProofWriterDSLToZ3()
            try:
                premises, conclusion = parser.parse_dsl(dsl_text)
                et = check_entailment(premises, conclusion)
                ef = check_entailment(premises, z3.Not(conclusion))
                if et:
                    z3_ans = "True"
                elif ef:
                    z3_ans = "False"
                else:
                    z3_ans = "Unknown"
                match = z3_ans == gold_answer
                val_ok += int(match)
                print(f"  [{st}] {pid}: gold={gold_answer}, z3={z3_ans}, match={match}")
            except Exception as e:
                print(f"  [{st}] {pid}: gold={gold_answer}, PARSE ERROR: {e}")
            val_total += 1

    print(f"\nValidation: {val_ok}/{val_total} correct")
    if val_ok < val_total // 2:
        print("WARNING: Validation accuracy below 50%. Check parser.")

    # ---- Phase 2: Full 600-problem run ----
    print("\n" + "-" * 40)
    print("Phase 2: Full evaluation")
    print("-" * 40)

    results = []
    parse_errors = 0
    z3_vs_gold_match = 0
    total_consistency_checks = 0
    total_solver_errors = 0
    n_total = len(common_ids)
    t_start = time.time()

    for idx, pid in enumerate(sorted(common_ids)):
        gold = gold_data[pid]
        trace_result = trace_by_id[pid]
        gold_answer = answer_label_to_text(gold["answer"])
        dsl_text = gold["raw_logic_programs"][0]
        trace_answers = [normalize_answer(t["answer"]) for t in trace_result["per_trace"]]
        subtype = get_subtype(pid)

        parser = ProofWriterDSLToZ3()
        try:
            premises, conclusion = parser.parse_dsl(dsl_text)
        except (DSLParseError, Exception) as e:
            parse_errors += 1
            sc_answer = sc_aggregate(trace_answers)
            results.append({
                "problem_id": pid,
                "subtype": subtype,
                "ground_truth": gold_answer,
                "oracle_answer": sc_answer,
                "sc_answer": sc_answer,
                "sica_answer": trace_result["sica_answer"],
                "consistency_scores": [-1] * len(trace_answers),
                "parse_error": str(e),
            })
            continue

        # Z3 entailment vs gold
        et = check_entailment(premises, conclusion, timeout_ms=30000)
        ef = check_entailment(premises, z3.Not(conclusion), timeout_ms=30000)
        if et:
            z3_answer = "True"
        elif ef:
            z3_answer = "False"
        else:
            z3_answer = "Unknown"
        if z3_answer == gold_answer:
            z3_vs_gold_match += 1

        # Consistency scoring for each trace
        consistency_scores = []
        for t_ans in trace_answers:
            score = check_consistency_for_answer(premises, conclusion, t_ans)
            consistency_scores.append(score)
            total_consistency_checks += 1
            if score == -1:
                total_solver_errors += 1

        oracle_answer = maxsat_aggregate(trace_answers, consistency_scores)
        sc_answer = sc_aggregate(trace_answers)

        results.append({
            "problem_id": pid,
            "subtype": subtype,
            "ground_truth": gold_answer,
            "oracle_answer": oracle_answer,
            "sc_answer": sc_answer,
            "sica_answer": trace_result["sica_answer"],
            "z3_answer": z3_answer,
            "z3_matches_gold": z3_answer == gold_answer,
            "consistency_scores": consistency_scores,
            "trace_answers": trace_answers,
        })

        if (idx + 1) % 100 == 0:
            elapsed = time.time() - t_start
            print(f"  Processed {idx + 1}/{n_total}... ({elapsed:.1f}s)")

    elapsed_total = time.time() - t_start
    print(f"\n  Total processing time: {elapsed_total:.1f}s")

    # ---- Phase 3: Results ----
    print("\n" + "-" * 40)
    print("Phase 3: Results")
    print("-" * 40)

    oracle_correct = [r["oracle_answer"] == r["ground_truth"] for r in results]
    sc_correct = [r["sc_answer"] == r["ground_truth"] for r in results]
    sica_correct = [r["sica_answer"] == r["ground_truth"] for r in results]

    oracle_acc = sum(oracle_correct) / len(results)
    sc_acc = sum(sc_correct) / len(results)
    sica_acc = sum(sica_correct) / len(results)
    n_parsed = n_total - parse_errors

    print(f"\n  Oracle-SICA accuracy: {oracle_acc:.4f} ({sum(oracle_correct)}/{n_total})")
    print(f"  SC accuracy:          {sc_acc:.4f} ({sum(sc_correct)}/{n_total})")
    print(f"  SICA(self) accuracy:  {sica_acc:.4f} ({sum(sica_correct)}/{n_total})")
    print(f"\n  Delta (Oracle vs SC):   {(oracle_acc - sc_acc)*100:+.2f} pp")
    print(f"  Delta (Oracle vs SICA): {(oracle_acc - sica_acc)*100:+.2f} pp")
    z3_match_rate = z3_vs_gold_match / n_parsed if n_parsed > 0 else 0
    print(f"\n  Z3 vs gold match rate: {z3_vs_gold_match}/{n_parsed} = {z3_match_rate:.4f}")
    print(f"  Parse errors: {parse_errors}/{n_total}")
    print(f"  Solver errors: {total_solver_errors}/{total_consistency_checks}")

    # Per-subtype breakdown
    print("\n  Per-subtype breakdown:")
    print(f"  {'Subtype':<12} {'N':>4} {'Oracle':>8} {'SC':>8} {'SICA':>8} {'Delta':>8}")
    subtype_metrics = {}
    for st in subtypes:
        st_results = [r for r in results if r.get("subtype") == st]
        if not st_results:
            continue
        st_n = len(st_results)
        st_oracle = sum(1 for r in st_results if r["oracle_answer"] == r["ground_truth"]) / st_n
        st_sc = sum(1 for r in st_results if r["sc_answer"] == r["ground_truth"]) / st_n
        st_sica = sum(1 for r in st_results if r["sica_answer"] == r["ground_truth"]) / st_n
        st_delta = (st_oracle - st_sc) * 100
        print(f"  {st:<12} {st_n:>4} {st_oracle:>8.4f} {st_sc:>8.4f} {st_sica:>8.4f} {st_delta:>+8.2f}")
        subtype_metrics[st] = {
            "n": st_n,
            "oracle_acc": st_oracle,
            "sc_acc": st_sc,
            "sica_acc": st_sica,
            "delta_pp": st_delta,
        }

    # McNemar test
    p_oracle_vs_sc = p_oracle_vs_sica = None
    try:
        p_oracle_vs_sc = mcnemar_test(oracle_correct, sc_correct)
        p_oracle_vs_sica = mcnemar_test(oracle_correct, sica_correct)
        print(f"\n  McNemar p (Oracle vs SC):   {p_oracle_vs_sc:.6f}")
        print(f"  McNemar p (Oracle vs SICA): {p_oracle_vs_sica:.6f}")
    except ImportError:
        print("\n  (scipy not available for McNemar test)")

    # Bootstrap CI
    oracle_ci = sc_ci = sica_ci = None
    try:
        oracle_ci = bootstrap_ci(oracle_correct)
        sc_ci = bootstrap_ci(sc_correct)
        sica_ci = bootstrap_ci(sica_correct)
        print(f"\n  Bootstrap 95% CI:")
        print(f"    Oracle-SICA: [{oracle_ci[0]:.4f}, {oracle_ci[1]:.4f}]")
        print(f"    SC:          [{sc_ci[0]:.4f}, {sc_ci[1]:.4f}]")
        print(f"    SICA(self):  [{sica_ci[0]:.4f}, {sica_ci[1]:.4f}]")
    except ImportError:
        print("\n  (numpy not available for bootstrap CI)")

    # ---- Save results ----
    output = {
        "experiment": "exp-022-oracle-proofwriter",
        "description": "Oracle DSL Extraction: gold ProofWriter DSL + Z3 verification + MAX-SAT aggregation",
        "model": "Qwen2.5-14B-Instruct (traces) + Z3 (oracle constraints)",
        "dataset": "ProofWriter-OWA-D5",
        "n_problems": n_total,
        "k_traces": 12,
        "processing_time_s": elapsed_total,
        "metrics": {
            "oracle_sica_accuracy": oracle_acc,
            "sc_accuracy": sc_acc,
            "sica_self_extracted_accuracy": sica_acc,
            "delta_oracle_vs_sc_pp": (oracle_acc - sc_acc) * 100,
            "delta_oracle_vs_sica_pp": (oracle_acc - sica_acc) * 100,
            "z3_gold_match_rate": z3_match_rate,
            "parse_error_count": parse_errors,
            "solver_error_count": total_solver_errors,
            "total_consistency_checks": total_consistency_checks,
        },
        "per_subtype": subtype_metrics,
        "statistical_tests": {
            "mcnemar_oracle_vs_sc": p_oracle_vs_sc,
            "mcnemar_oracle_vs_sica": p_oracle_vs_sica,
            "bootstrap_ci_oracle": list(oracle_ci) if oracle_ci else None,
            "bootstrap_ci_sc": list(sc_ci) if sc_ci else None,
            "bootstrap_ci_sica": list(sica_ci) if sica_ci else None,
        },
        "per_problem": results,
    }

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    with open(OUTPUT_PATH, "w") as f:
        json.dump(output, f, indent=2)
    print(f"\nResults saved to {OUTPUT_PATH}")

    # Summary without per_problem
    summary = {k: v for k, v in output.items() if k != "per_problem"}
    summary_path = OUTPUT_PATH.with_name("exp022_oracle_pw_summary.json")
    with open(summary_path, "w") as f:
        json.dump(summary, f, indent=2)
    print(f"Summary saved to {summary_path}")

    print("\n" + "=" * 60)
    print("DONE")
    print("=" * 60)


if __name__ == "__main__":
    main()
