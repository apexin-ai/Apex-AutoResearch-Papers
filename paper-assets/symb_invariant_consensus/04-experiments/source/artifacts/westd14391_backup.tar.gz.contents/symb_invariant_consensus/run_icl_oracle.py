#!/usr/bin/env python3
"""
Experiment 3: ICL with Oracle Examples for FOLIO constraint extraction.
Injects 5 gold FOL examples into the LOGIC_EXTRACTION_PROMPT to improve
constraint quality. Evaluates SICA vs SC on the remaining 199 FOLIO problems.
"""
from __future__ import annotations

import argparse
import json
import logging
import os
import sys
import time
from collections import Counter

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from sica.constraint_extractor import (
    ConstraintExtractor, VLLMBackend, APIBasedLLM, MockLLM,
    LOGIC_EXTRACTION_PROMPT,
)
from sica.trace_generator import VLLMGenerator, MockGenerator
from sica.pipeline import SICAPipeline, normalize_logic_answer
from baselines.self_consistency import SelfConsistency
from utils.math_equiv import is_equiv

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s",
    handlers=[logging.StreamHandler(sys.stdout)],
)
logger = logging.getLogger(__name__)

# ---------------------------------------------------------------------------
# ICL example selection: 5 diverse FOLIO problems with gold FOL
# Indices into folio_full.json; excluded from evaluation.
# True: idx 15 (universal quantification chain), idx 6 (existential + conditional)
# False: idx 79 (negation chain), idx 52 (negation via relation)
# Unknown: idx 3 (XOR / insufficient info)
# ---------------------------------------------------------------------------
ICL_INDICES = [15, 6, 79, 52, 3]


def build_icl_block(folio_data: list[dict]) -> str:
    """Build the few-shot ICL block from gold FOL annotations."""
    examples = []
    for rank, idx in enumerate(ICL_INDICES, 1):
        d = folio_data[idx]
        problem = d["problem"]
        parts = problem.split("Determine whether")
        if len(parts) >= 2:
            premises_nl = parts[0].replace("Given the following premises:\n", "").strip()
            conclusion_nl = "Determine whether" + parts[1]
        else:
            premises_nl = problem[:500]
            conclusion_nl = ""

        premises_fol = d["premises_fol"]
        conclusion_fol = d["conclusion_fol"]
        answer = d["answer"]

        fol_constraints = []
        variables = set()
        for step_i, fol in enumerate(premises_fol, 1):
            ctype = "rule" if "∀" in fol or "∃" in fol or "→" in fol else "fact"
            fol_constraints.append({
                "type": ctype,
                "expression": fol,
                "z3_formula": _fol_to_z3_hint(fol),
                "source_step": step_i,
            })
            variables.update(_extract_var_names(fol))

        fol_constraints.append({
            "type": "derived",
            "expression": conclusion_fol,
            "z3_formula": _fol_to_z3_hint(conclusion_fol),
            "source_step": len(premises_fol) + 1,
        })
        variables.update(_extract_var_names(conclusion_fol))

        gold_json = json.dumps({
            "constraints": fol_constraints,
            "answer": answer,
            "variables": sorted(variables),
        }, indent=2, ensure_ascii=False)

        ex_text = (
            f"FOLIO Example {rank}:\n"
            f"Premises: {premises_nl}\n"
            f"Conclusion: {conclusion_nl}\n"
            f"Gold Answer: {answer}\n"
            f"Gold FOL Constraints:\n{gold_json}"
        )
        examples.append(ex_text)

    return "\n\n".join(examples)


def _fol_to_z3_hint(fol: str) -> str:
    """Best-effort conversion of FOL notation to Z3-style hint."""
    s = fol
    s = s.replace("∀x ", "ForAll(x, ").replace("∀x(", "ForAll(x, (")
    s = s.replace("∀y ", "ForAll(y, ").replace("∀y(", "ForAll(y, (")
    s = s.replace("∀z ", "ForAll(z, ").replace("∀z(", "ForAll(z, (")
    s = s.replace("∃x ", "Exists(x, ").replace("∃x(", "Exists(x, (")
    s = s.replace("∃y ", "Exists(y, ").replace("∃y(", "Exists(y, (")
    s = s.replace("→", ">>")
    s = s.replace("∧", "&")
    s = s.replace("∨", "|")
    s = s.replace("¬", "~")
    s = s.replace("⊕", "^")
    s = s.replace("↔", "==")
    if s.startswith("ForAll(") or s.startswith("Exists("):
        s = s + ")"
    return s


def _extract_var_names(fol: str) -> list[str]:
    """Extract predicate-like identifiers from FOL string."""
    import re
    names = re.findall(r'[A-Z][a-zA-Z]*\([^)]*\)', fol)
    result = []
    for n in names:
        pred = n.split("(")[0]
        args_str = n.split("(")[1].rstrip(")")
        args = [a.strip() for a in args_str.split(",")]
        for arg in args:
            if arg and arg[0].islower() and len(arg) > 1:
                var_name = f"{pred.lower()}_{arg}"
                result.append(var_name)
    return result


ICL_ENHANCED_PROMPT_TEMPLATE = '''Extract logical constraints from this reasoning trace about a logic problem.

The problem has facts (base assertions), rules (grounded implications), and derived conclusions.
Convert each into a Z3 boolean formula.

Variable naming:
- Unary property: property_entity (e.g., kind_anne, red_charlie, round_fiona)
- Binary relation: relation_subject_object (e.g., eats_bear_squirrel, likes_lion_cat)
- Use lowercase with underscores only, no spaces or special characters

Constraint types:
- "fact": a given assertion, e.g., kind_anne == True
- "rule": a grounded implication over specific entities, e.g., Implies(kind_anne, nice_anne)
- "derived": an inferred conclusion from facts + rules, e.g., nice_anne == True

Z3 operators:
- Implies(a, b) for if-then rules
- And(a, b, ...) for conjunctive conditions
- Or(a, b, ...) for disjunctive conditions
- Not(a) for negation
- == True / == False for boolean assertions

Below are examples with gold first-order logic (FOL) annotations showing ideal constraint extraction for FOLIO-style problems. Use these as reference for the quality and granularity of constraints you should extract.

{icl_block}

Now extract constraints from the following trace. Output ONLY the JSON, nothing else:
{{"constraints": [{{"type": "fact", "expression": "kind(anne)", "z3_formula": "kind_anne == True", "source_step": 1}}], "answer": "True or False or Unknown", "variables": ["kind_anne"]}}

Trace:
{trace}'''


class ICLConstraintExtractor(ConstraintExtractor):
    """ConstraintExtractor with ICL oracle examples injected into logic prompt."""

    def __init__(self, llm, icl_block: str, parse_retries: int = 1,
                 domain: str = "logic"):
        super().__init__(llm=llm, parse_retries=parse_retries, domain=domain)
        self.icl_block = icl_block
        self._icl_prompt = ICL_ENHANCED_PROMPT_TEMPLATE.replace(
            "{icl_block}", icl_block
        )

    def _build_prompt(self, trace: str) -> str:
        if self.domain == "logic":
            return self._icl_prompt.replace("{trace}", trace)
        return super()._build_prompt(trace)


def build_generator(args):
    if args.mode == "mock":
        return MockGenerator()
    return VLLMGenerator(
        base_url=args.api_base,
        api_key="[REDACTED]",
        model=args.model if args.model != "auto" else None,
        temperature=args.temperature,
        max_tokens=args.max_tokens,
    )


def build_extractor(args, icl_block: str):
    if args.mode == "mock":
        return ICLConstraintExtractor(
            llm=MockLLM(domain="logic"), icl_block=icl_block, domain="logic"
        )
    return ICLConstraintExtractor(
        llm=VLLMBackend(
            base_url=args.api_base,
            model=args.model if args.model != "auto" else None,
        ),
        icl_block=icl_block,
        domain="logic",
    )


def main():
    parser = argparse.ArgumentParser(description="ICL Oracle FOLIO Experiment")
    parser.add_argument("--api-base", default="http://localhost:8000/v1")
    parser.add_argument("--model", default="auto")
    parser.add_argument("--k", type=int, default=12)
    parser.add_argument("--data", default="data/folio_full.json")
    parser.add_argument("--output", default="results/icl_oracle_folio/results.json")
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--save-intermediates", action="store_true")
    parser.add_argument("--mode", default="vllm", choices=["vllm", "mock"])
    parser.add_argument("--temperature", type=float, default=0.7)
    parser.add_argument("--max-tokens", type=int, default=4096)
    parser.add_argument("--resume", action="store_true")
    args = parser.parse_args()

    import random
    random.seed(args.seed)

    logger.info("Loading FOLIO data from %s", args.data)
    with open(args.data) as f:
        folio_data = json.load(f)
    logger.info("Total FOLIO problems: %d", len(folio_data))

    icl_block = build_icl_block(folio_data)
    logger.info("ICL block built with %d examples (indices: %s)", len(ICL_INDICES), ICL_INDICES)
    logger.info("ICL block length: %d chars", len(icl_block))

    eval_indices = [i for i in range(len(folio_data)) if i not in ICL_INDICES]
    eval_problems = []
    for i in eval_indices:
        p = folio_data[i].copy()
        p["_orig_idx"] = i
        p.setdefault("dataset", "folio")
        eval_problems.append(p)
    logger.info("Evaluation problems: %d (excluded %d ICL examples)", len(eval_problems), len(ICL_INDICES))

    generator = build_generator(args)
    generator.domain = "math"
    extractor = build_extractor(args, icl_block)
    pipeline = SICAPipeline(
        trace_generator=generator,
        constraint_extractor=extractor,
        k=args.k,
    )
    sc_baseline = SelfConsistency()

    checkpoint = {}
    if args.resume and os.path.exists(args.output):
        with open(args.output) as f:
            checkpoint = json.load(f)
        logger.info("Resumed from checkpoint with %d results", len(checkpoint.get("results", [])))

    completed_ids = {r["problem_id"] for r in checkpoint.get("results", [])}
    all_results = list(checkpoint.get("results", []))
    remaining = [(i, p) for i, p in enumerate(eval_problems) if p.get("id", f"folio_{p['_orig_idx']}") not in completed_ids]

    total_start = time.time()
    elapsed_times = []

    for progress_idx, (eval_i, prob) in enumerate(remaining):
        prob_id = prob.get("id", f"folio_{prob['_orig_idx']}")
        t0 = time.time()

        print(f"\n--- [{progress_idx+1}/{len(remaining)}] (eval {eval_i+1}/{len(eval_problems)}) ---")
        print(f"ID: {prob_id} | GT: {prob['answer']}")
        print(f"Q: {prob['problem'][:120]}...")
        sys.stdout.flush()

        extractor.domain = "logic"
        pipeline.trace_generator.domain = "math"

        try:
            sica_result = pipeline.run_single(prob)
            sica_answer = sica_result.get("answer", "")
            sica_correct = is_equiv(sica_answer, prob["answer"])
            print(f"SICA: {sica_answer} ({'V' if sica_correct else 'X'})")
        except Exception as e:
            logger.error("SICA error on %s: %s", prob_id, e)
            import traceback; traceback.print_exc()
            sica_result = {"answer": "", "traces": [], "scores": {},
                           "constraints_stats": {"total_extracted": 0, "traces_with_constraints": 0, "unique_after_dedup": 0},
                           "maxsat_stats": {"satisfied": 0, "excluded": 0, "total_weight": 0, "solve_time_ms": 0},
                           "timing": {}}
            sica_answer = ""
            sica_correct = False

        try:
            traces = sica_result.get("traces", [])
            for t in traces:
                if t.get("answer"):
                    t["answer"] = normalize_logic_answer(t["answer"])
            answers = [t.get("answer", "") for t in traces]
            sc_result = sc_baseline.run(prob, traces=[t.get("trace", "") for t in traces], answers=answers)
            sc_answer = sc_result.get("answer", "")
            sc_correct = is_equiv(sc_answer, prob["answer"])
            print(f"SC:   {sc_answer} ({'V' if sc_correct else 'X'}) -- votes: {sc_result.get('vote_count','?')}/{len(traces)}")
        except Exception as e:
            logger.error("SC error on %s: %s", prob_id, e)
            sc_answer = ""
            sc_correct = False
            sc_result = {"vote_count": 0, "vote_distribution": {}}

        elapsed = time.time() - t0
        elapsed_times.append(elapsed)
        print(f"Time: {elapsed:.1f}s")

        avg_time = sum(elapsed_times) / len(elapsed_times)
        remaining_count = len(remaining) - (progress_idx + 1)
        if remaining_count > 0:
            eta_min = avg_time * remaining_count / 60
            print(f"ETA: {eta_min:.1f} min ({remaining_count} remaining, avg {avg_time:.1f}s/prob)")

        sys.stdout.flush()

        result_entry = {
            "problem_idx": eval_i,
            "problem_id": prob_id,
            "orig_folio_idx": prob["_orig_idx"],
            "problem": prob["problem"],
            "dataset": "folio",
            "ground_truth": prob["answer"],
            "sica_answer": sica_answer,
            "sica_scores": sica_result.get("scores", {}),
            "sica_correct": sica_correct,
            "sc_answer": sc_answer,
            "sc_vote_count": sc_result.get("vote_count", 0),
            "sc_vote_distribution": sc_result.get("vote_distribution", {}),
            "sc_correct": sc_correct,
            "constraints_stats": sica_result.get("constraints_stats", {}),
            "maxsat_stats": sica_result.get("maxsat_stats", {}),
            "timing": sica_result.get("timing", {}),
            "wall_time_s": round(elapsed, 2),
        }
        all_results.append(result_entry)

        if args.save_intermediates:
            intermed_dir = os.path.join(os.path.dirname(args.output) or ".", "intermediates")
            os.makedirs(intermed_dir, exist_ok=True)
            with open(os.path.join(intermed_dir, f"{prob_id}.json"), "w") as f:
                json.dump({"problem": prob, "sica_result": sica_result}, f, indent=2, default=str)

        summary = compute_summary(all_results, extractor.stats)
        summary["k"] = args.k
        summary["mode"] = args.mode
        summary["icl_indices"] = ICL_INDICES
        summary["n_eval"] = len(eval_problems)
        summary["total_wall_time_s"] = round(time.time() - total_start, 1)
        output = {"summary": summary, "results": all_results}
        os.makedirs(os.path.dirname(args.output) or ".", exist_ok=True)
        with open(args.output, "w") as f:
            json.dump(output, f, indent=2, default=str)

    total_wall = time.time() - total_start
    summary = compute_summary(all_results, extractor.stats)
    summary["k"] = args.k
    summary["mode"] = args.mode
    summary["icl_indices"] = ICL_INDICES
    summary["n_eval"] = len(eval_problems)
    summary["total_wall_time_s"] = round(total_wall, 1)

    output = {"summary": summary, "results": all_results}
    with open(args.output, "w") as f:
        json.dump(output, f, indent=2, default=str)

    print_summary(summary)
    print(f"\nTotal wall time: {total_wall/60:.1f} min")
    print(f"Results saved to {args.output}")
    print("ICL_ORACLE_DONE")


def compute_summary(results: list[dict], ext_stats) -> dict:
    n = len(results)
    if n == 0:
        return {}

    sica_correct = sum(1 for r in results if r["sica_correct"])
    sc_correct = sum(1 for r in results if r["sc_correct"])

    per_answer = {}
    for ans_type in ["True", "False", "Unknown"]:
        sub = [r for r in results if r["ground_truth"] == ans_type]
        if sub:
            per_answer[ans_type] = {
                "n": len(sub),
                "sica_acc": round(sum(1 for r in sub if r["sica_correct"]) / len(sub), 4),
                "sc_acc": round(sum(1 for r in sub if r["sc_correct"]) / len(sub), 4),
            }

    return {
        "n": n,
        "sica_accuracy": round(sica_correct / n, 4),
        "sc_accuracy": round(sc_correct / n, 4),
        "sica_correct": sica_correct,
        "sc_correct": sc_correct,
        "delta_pp": round((sica_correct / n - sc_correct / n) * 100, 2),
        "per_answer_type": per_answer,
        "extraction_stats": {
            "success": ext_stats.success,
            "fail_json_parse": ext_stats.fail_json_parse,
            "fail_empty": ext_stats.fail_empty,
            "fail_invalid_expr": ext_stats.fail_invalid_expr,
        },
    }


def print_summary(summary: dict):
    print("\n" + "=" * 60)
    print("ICL Oracle FOLIO Results")
    print("=" * 60)
    n = summary.get("n", 0)
    print(f"N = {n}, K = {summary.get('k', '?')}")
    print(f"ICL examples excluded: {summary.get('icl_indices', [])}")
    print(f"\nSICA accuracy:  {summary.get('sica_accuracy', 0):.4f} ({summary.get('sica_correct', 0)}/{n})")
    print(f"SC accuracy:    {summary.get('sc_accuracy', 0):.4f} ({summary.get('sc_correct', 0)}/{n})")
    print(f"Delta:          {summary.get('delta_pp', 0):+.2f}pp")

    per_ans = summary.get("per_answer_type", {})
    if per_ans:
        print(f"\n{'Type':8s}  {'n':>3s}  {'SICA':>7s}  {'SC':>7s}")
        for ans_type in ["True", "False", "Unknown"]:
            if ans_type in per_ans:
                st = per_ans[ans_type]
                print(f"{ans_type:8s}  {st['n']:3d}  {st['sica_acc']:7.4f}  {st['sc_acc']:7.4f}")

    ext = summary.get("extraction_stats", {})
    if ext:
        total_ext = ext.get("success", 0) + ext.get("fail_json_parse", 0) + ext.get("fail_empty", 0) + ext.get("fail_invalid_expr", 0)
        print(f"\nExtraction: {ext.get('success', 0)}/{total_ext} success, "
              f"{ext.get('fail_json_parse', 0)} json_fail, "
              f"{ext.get('fail_empty', 0)} empty, "
              f"{ext.get('fail_invalid_expr', 0)} invalid")


if __name__ == "__main__":
    main()
