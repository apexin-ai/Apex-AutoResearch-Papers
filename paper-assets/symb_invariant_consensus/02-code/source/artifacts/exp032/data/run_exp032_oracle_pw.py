#!/usr/bin/env python3
"""
Oracle-SICA on ProofWriter OWA-D5 using exp032 (Qwen2.5-14B, K=12) traces.
Replicates exp-022 logic but sources data from exp032 intermediates.

Gold DSL (raw_logic_programs) -> Z3 consistency check per trace -> weighted aggregation.
"""
import json
import os
import re
import sys
import time
from collections import Counter
from pathlib import Path

import z3

INTERMEDIATES_DIR = Path("/root/symb_invariant_consensus/results/exp032_qwen25_14b_pw600/intermediates")
OUTPUT_DIR = Path("/root/symb_invariant_consensus/results/exp032_qwen14b_pw_oracle")


class DSLParseError(Exception):
    pass


class ProofWriterDSLToZ3:
    def __init__(self):
        self.entity_sort = z3.DeclareSort("Entity")
        self.predicates = {}
        self.constants = {}
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
        for line in text.strip().split("\n"):
            line = line.split(":::")[0].strip()
            if not line:
                continue
            m = re.match(r'(\w+)\((.+)\)', line)
            if not m:
                continue
            name = m.group(1)
            args = [a.strip() for a in m.group(2).split(",")]
            entity_args = [a for a in args if a != "bool"]
            arity = len(entity_args)
            self.declared_pred_names.add(name)
            self.get_predicate(name, arity)

    def _parse_atomic(self, text):
        text = text.strip()
        m = re.match(r'(\w+)\((.+)\)', text)
        if not m:
            raise DSLParseError(f"Cannot parse atomic: {text!r}")
        raw_name = m.group(1)
        raw_args = [a.strip() for a in m.group(2).split(",")]

        if raw_args[-1] not in ("True", "False"):
            raise DSLParseError(f"Expected True/False as last arg in: {text!r}")
        is_positive = raw_args[-1] == "True"
        entity_args_raw = raw_args[:-1]

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

        if negated_prefix:
            expr = z3.Not(expr)
            if not is_positive:
                expr = z3.Not(expr)
        else:
            if not is_positive:
                expr = z3.Not(expr)

        return expr, variables

    def _parse_facts(self, text):
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
            cond_parts = [c.strip() for c in cond_text.split("&&")]
            cond_exprs = []
            for cp in cond_parts:
                expr, vs = self._parse_atomic(cp)
                cond_exprs.append(expr)
                all_vars |= vs

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
        for line in text.strip().split("\n"):
            line = line.split(":::")[0].strip()
            if not line:
                continue
            expr, variables = self._parse_atomic(line)
            if variables:
                raise DSLParseError(f"Variables in query: {line!r}")
            return expr
        raise DSLParseError("Empty query section")


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
    ans = str(ans).strip()
    if ans in ('True', 'False', 'Unknown'):
        return ans
    cleaned = re.sub(r'\\+text\{(\w+)\}', r'\1', ans)
    if cleaned in ('True', 'False', 'Unknown'):
        return cleaned
    low = ans.lower()
    if low == 'true':
        return 'True'
    elif low == 'false':
        return 'False'
    elif low == 'unknown':
        return 'Unknown'
    return ans


def check_consistency_for_answer(premises_z3, conclusion_z3, candidate_answer, timeout_ms=5000):
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
    return Counter(trace_answers).most_common(1)[0][0]


def get_subtype(problem_id):
    m = re.match(r'ProofWriter_(\w+)-OWA', problem_id)
    return m.group(1) if m else "Unknown"


def main():
    print("=" * 60)
    print("Oracle-SICA on PW600 using exp032 traces")
    print("=" * 60)

    files = sorted(INTERMEDIATES_DIR.glob("*.json"))
    print(f"Found {len(files)} intermediate files.")
    assert len(files) == 600, f"Expected 600, got {len(files)}"

    results = []
    parse_errors = 0
    z3_vs_gold_match = 0
    z3_parsed_count = 0
    total_consistency_checks = 0
    total_solver_errors = 0
    t_start = time.time()

    for idx, fpath in enumerate(files):
        with open(fpath) as f:
            data = json.load(f)

        prob = data["problem"]
        sica = data["sica_result"]
        pid = prob["id"]
        gold_answer = normalize_answer(prob["answer"])
        subtype = get_subtype(pid)
        trace_answers = [normalize_answer(t["answer"]) for t in sica["traces"]]
        sc_answer = sc_aggregate(trace_answers)
        sica_answer = normalize_answer(sica["answer"])

        dsl_text = prob["raw_logic_programs"][0] if prob.get("raw_logic_programs") else None

        if not dsl_text:
            parse_errors += 1
            results.append({
                "problem_id": pid,
                "subtype": subtype,
                "ground_truth": gold_answer,
                "oracle_answer": sc_answer,
                "sc_answer": sc_answer,
                "sica_answer": sica_answer,
                "consistency_scores": [-1] * len(trace_answers),
                "parse_error": "no DSL available",
            })
            continue

        parser = ProofWriterDSLToZ3()
        try:
            premises, conclusion = parser.parse_dsl(dsl_text)
        except (DSLParseError, Exception) as e:
            parse_errors += 1
            results.append({
                "problem_id": pid,
                "subtype": subtype,
                "ground_truth": gold_answer,
                "oracle_answer": sc_answer,
                "sc_answer": sc_answer,
                "sica_answer": sica_answer,
                "consistency_scores": [-1] * len(trace_answers),
                "parse_error": str(e),
            })
            continue

        z3_parsed_count += 1

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

        consistency_scores = []
        for t_ans in trace_answers:
            score = check_consistency_for_answer(premises, conclusion, t_ans)
            consistency_scores.append(score)
            total_consistency_checks += 1
            if score == -1:
                total_solver_errors += 1

        oracle_answer = maxsat_aggregate(trace_answers, consistency_scores)

        results.append({
            "problem_id": pid,
            "subtype": subtype,
            "ground_truth": gold_answer,
            "oracle_answer": oracle_answer,
            "sc_answer": sc_answer,
            "sica_answer": sica_answer,
            "z3_answer": z3_answer,
            "z3_matches_gold": z3_answer == gold_answer,
            "consistency_scores": consistency_scores,
            "trace_answers": trace_answers,
        })

        if (idx + 1) % 100 == 0:
            elapsed = time.time() - t_start
            print(f"  Processed {idx + 1}/600... ({elapsed:.1f}s)")

    elapsed_total = time.time() - t_start

    oracle_correct = [r["oracle_answer"] == r["ground_truth"] for r in results]
    sc_correct = [r["sc_answer"] == r["ground_truth"] for r in results]
    sica_correct = [r["sica_answer"] == r["ground_truth"] for r in results]

    n = len(results)
    oracle_acc = sum(oracle_correct) / n
    sc_acc = sum(sc_correct) / n
    sica_acc = sum(sica_correct) / n
    z3_match_rate = z3_vs_gold_match / z3_parsed_count if z3_parsed_count > 0 else 0

    print(f"\n{'='*60}")
    print("Results")
    print(f"{'='*60}")
    print(f"N = {n}, K = 12")
    print(f"Oracle-SICA accuracy: {oracle_acc:.4f} ({sum(oracle_correct)}/{n})")
    print(f"SC accuracy:          {sc_acc:.4f} ({sum(sc_correct)}/{n})")
    print(f"SICA(self) accuracy:  {sica_acc:.4f} ({sum(sica_correct)}/{n})")
    print(f"Delta (Oracle vs SC):   {(oracle_acc - sc_acc)*100:+.2f} pp")
    print(f"Delta (Oracle vs SICA): {(oracle_acc - sica_acc)*100:+.2f} pp")
    print(f"Z3 vs gold match rate:  {z3_vs_gold_match}/{z3_parsed_count} = {z3_match_rate:.4f}")
    print(f"Parse errors: {parse_errors}/{n}")
    print(f"Solver errors: {total_solver_errors}/{total_consistency_checks}")

    subtypes = ["AttNoneg", "AttNeg", "RelNoneg", "RelNeg"]
    print(f"\nPer-subtype:")
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
        subtype_metrics[st] = {"n": st_n, "oracle_acc": st_oracle, "sc_acc": st_sc, "sica_acc": st_sica}

    per_gt = {}
    for gt in ["True", "False", "Unknown"]:
        sub = [r for r in results if r["ground_truth"] == gt]
        if sub:
            per_gt[gt] = {
                "n": len(sub),
                "oracle_acc": round(sum(1 for r in sub if r["oracle_answer"] == r["ground_truth"]) / len(sub), 4),
                "sc_acc": round(sum(1 for r in sub if r["sc_answer"] == r["ground_truth"]) / len(sub), 4),
            }
            print(f"\n  GT={gt}: n={per_gt[gt]['n']}, oracle={per_gt[gt]['oracle_acc']:.4f}, sc={per_gt[gt]['sc_acc']:.4f}")

    output = {
        "experiment": "exp032-oracle-proofwriter",
        "description": "Oracle DSL Extraction on exp032 Qwen2.5-14B PW600 traces",
        "traces_source": "exp032_qwen25_14b_pw600",
        "n_problems": n,
        "k_traces": 12,
        "processing_time_s": round(elapsed_total, 1),
        "metrics": {
            "oracle_sica_accuracy": round(oracle_acc, 4),
            "oracle_correct_count": sum(oracle_correct),
            "sc_accuracy": round(sc_acc, 4),
            "sc_correct_count": sum(sc_correct),
            "sica_self_accuracy": round(sica_acc, 4),
            "sica_correct_count": sum(sica_correct),
            "delta_oracle_vs_sc_pp": round((oracle_acc - sc_acc) * 100, 2),
            "delta_oracle_vs_sica_pp": round((oracle_acc - sica_acc) * 100, 2),
            "z3_gold_match_rate": round(z3_match_rate, 4),
            "z3_parsed_count": z3_parsed_count,
            "parse_error_count": parse_errors,
            "solver_error_count": total_solver_errors,
            "total_consistency_checks": total_consistency_checks,
        },
        "comparison_exp022": {
            "exp022_oracle_accuracy": 0.8667,
            "exp022_traces_source": "sica_expanded_14b.json (pre-exp032)",
            "note": "exp032 uses canonical trace generation run",
        },
        "per_subtype": subtype_metrics,
        "per_ground_truth": per_gt,
        "per_problem": results,
    }

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    out_path = OUTPUT_DIR / "results.json"
    with open(out_path, "w") as f:
        json.dump(output, f, indent=2)

    summary = {k: v for k, v in output.items() if k != "per_problem"}
    with open(OUTPUT_DIR / "summary.json", "w") as f:
        json.dump(summary, f, indent=2)

    print(f"\nResults saved to {out_path}")
    print(f"Wall time: {elapsed_total:.1f}s")
    print("EXP032_ORACLE_DONE")


if __name__ == "__main__":
    main()
