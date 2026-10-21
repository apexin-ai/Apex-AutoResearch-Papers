"""Discriminative Constraint Filtering for SICA pipeline.

Filters out non-discriminative constraints before MAX-SAT scoring.
A constraint is non-discriminative if its source traces cover ALL candidate
answers, meaning it adds equal weight to every candidate during scoring.

Input:  SICA experiment results directory with intermediates/
Output: JSON report comparing original vs filtered SICA accuracy

Dependencies: z3-solver, openai (for constraint re-extraction when not cached)
"""
from __future__ import annotations

import argparse
import json
import logging
import os
import sys
import time
from collections import Counter

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from sica.z3_maxsat import ConstraintDeduplicator, MaxSATSolver
from sica.scorer import InvariantScorer
from sica.pipeline import normalize_logic_answer

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s",
)
logger = logging.getLogger(__name__)


def load_intermediates(input_dir: str) -> list[dict]:
    """Load all intermediate JSON files from the experiment directory."""
    intermed_dir = os.path.join(input_dir, "intermediates")
    if not os.path.isdir(intermed_dir):
        raise FileNotFoundError(f"No intermediates directory: {intermed_dir}")
    problems = []
    for fname in sorted(os.listdir(intermed_dir)):
        if not fname.endswith(".json"):
            continue
        with open(os.path.join(intermed_dir, fname)) as f:
            problems.append(json.load(f))
    return problems


def load_or_extract_constraints(problem_data, cache_dir, extractor):
    """Return per-trace constraint lists. Use cache or sica_result; re-extract as fallback."""
    pid = problem_data["problem"]["id"]
    sr = problem_data.get("sica_result", {})

    if cache_dir:
        cache_path = os.path.join(cache_dir, f"{pid}.json")
        if os.path.exists(cache_path):
            with open(cache_path) as f:
                return [t["constraints"] for t in json.load(f)["per_trace"]]

    if "per_trace_constraints" in sr:
        ptc = sr["per_trace_constraints"]
        if cache_dir:
            _save_cache(pid, sr["traces"], ptc, problem_data["problem"].get("answer", ""), cache_dir)
        return ptc

    if extractor is None:
        raise RuntimeError(f"No cached constraints for {pid} and no extractor provided")

    traces = sr.get("traces", [])
    ptc = extractor.extract_batch([t["trace"] for t in traces])
    if cache_dir:
        _save_cache(pid, traces, ptc, problem_data["problem"].get("answer", ""), cache_dir)
    return ptc


def _save_cache(pid, traces, ptc, gt, cache_dir):
    os.makedirs(cache_dir, exist_ok=True)
    per_trace = []
    for i, t in enumerate(traces):
        per_trace.append({
            "trace_idx": t.get("trace_idx", i),
            "answer": t.get("answer", ""),
            "constraints": ptc[i] if i < len(ptc) else [],
        })
    with open(os.path.join(cache_dir, f"{pid}.json"), "w") as f:
        json.dump({"pid": pid, "gt": gt, "per_trace": per_trace}, f, indent=2, default=str)


def filter_discriminative(unique_constraints, traces, candidates):
    """Split constraints into discriminative and non-discriminative.

    Non-discriminative: source_traces intersects with trace sets of ALL candidates.
    These add equal weight to every candidate and don't help distinguish answers.
    """
    answer_traces = {}
    for t in traces:
        ans = str(t.get("answer", "")).strip()
        idx = t.get("trace_idx", 0)
        answer_traces.setdefault(ans, set()).add(idx)

    discriminative = []
    non_discriminative = []

    for uc in unique_constraints:
        src = set(uc.source_traces)
        covers_all = all(
            bool(src & answer_traces.get(cand, set()))
            for cand in candidates
        )
        if covers_all:
            non_discriminative.append(uc)
        else:
            discriminative.append(uc)

    return discriminative, non_discriminative


def process_problem(problem_data, cache_dir, extractor, deduplicator, solver, scorer):
    """Process one problem: extract constraints, filter, re-score, compare."""
    pid = problem_data["problem"]["id"]
    gt = problem_data["problem"]["answer"]
    sr = problem_data["sica_result"]
    dataset = problem_data["problem"].get("dataset", "folio")
    is_logic = dataset in ("proofwriter", "folio", "strategyqa")

    traces = sr["traces"]
    if is_logic:
        for t in traces:
            if t.get("answer"):
                t["answer"] = normalize_logic_answer(t["answer"])

    candidates = sorted(set(t["answer"] for t in traces if t.get("answer")))
    answer_counts = Counter(t["answer"] for t in traces if t.get("answer"))

    ptc = load_or_extract_constraints(problem_data, cache_dir, extractor)
    unique_constraints = deduplicator.deduplicate(ptc)

    def check_correct(ans):
        if is_logic:
            return normalize_logic_answer(ans) == normalize_logic_answer(gt)
        return ans == gt

    # --- original (no filter) ---
    orig_maxsat = solver.solve(unique_constraints)
    orig_scores = scorer.score(orig_maxsat, traces, candidates)
    orig_answer = scorer.select_answer(orig_scores, answer_counts)

    # --- discriminative filter ---
    disc, non_disc = filter_discriminative(unique_constraints, traces, candidates)

    if disc:
        filt_maxsat = solver.solve(disc)
    else:
        filt_maxsat = solver.solve([])

    filt_scores = scorer.score(filt_maxsat, traces, candidates)
    filt_answer = scorer.select_answer(filt_scores, answer_counts)

    stored_answer = sr.get("answer", "")
    sc_answer = max(answer_counts, key=answer_counts.get) if answer_counts else ""

    return {
        "pid": pid,
        "ground_truth": gt,
        "candidates": candidates,
        "n_traces": len(traces),
        "answer_distribution": dict(answer_counts),
        "n_unique_constraints": len(unique_constraints),
        "n_discriminative": len(disc),
        "n_non_discriminative": len(non_disc),
        "filter_ratio": len(non_disc) / len(unique_constraints) if unique_constraints else 0,
        "stored_answer": stored_answer,
        "stored_correct": check_correct(stored_answer),
        "recomputed_answer": orig_answer,
        "recomputed_scores": {k: round(v, 2) for k, v in orig_scores.items()},
        "recomputed_correct": check_correct(orig_answer),
        "filtered_answer": filt_answer,
        "filtered_scores": {k: round(v, 2) for k, v in filt_scores.items()},
        "filtered_correct": check_correct(filt_answer),
        "answer_changed": orig_answer != filt_answer,
        "sc_answer": sc_answer,
        "sc_correct": check_correct(sc_answer),
        "orig_maxsat_satisfied": len(orig_maxsat.satisfied),
        "orig_maxsat_excluded": len(orig_maxsat.excluded),
        "filt_maxsat_satisfied": len(filt_maxsat.satisfied),
        "filt_maxsat_excluded": len(filt_maxsat.excluded),
    }


def main():
    parser = argparse.ArgumentParser(description="Discriminative constraint filtering for SICA")
    parser.add_argument("--input-dir", required=True, help="Experiment results directory")
    parser.add_argument("--output", required=True, help="Output JSON path")
    parser.add_argument("--cache-dir", default=None,
                        help="Cache dir for extracted constraints (avoids re-extraction)")
    parser.add_argument("--api-base", default="http://localhost:8000/v1")
    parser.add_argument("--model", default=None)
    parser.add_argument("--domain", default="logic",
                        help="Extraction domain: logic | math | commonsense")
    parser.add_argument("--limit", type=int, default=None)
    args = parser.parse_args()

    problems = load_intermediates(args.input_dir)
    logger.info("Loaded %d intermediates", len(problems))
    if args.limit:
        problems = problems[:args.limit]

    needs_extraction = False
    for p in problems:
        sr = p.get("sica_result", {})
        if "per_trace_constraints" not in sr:
            pid = p["problem"]["id"]
            if args.cache_dir:
                if not os.path.exists(os.path.join(args.cache_dir, f"{pid}.json")):
                    needs_extraction = True
                    break
            else:
                needs_extraction = True
                break

    extractor = None
    if needs_extraction:
        from sica.constraint_extractor import ConstraintExtractor, VLLMBackend
        logger.info("Initializing extractor (api_base=%s, domain=%s)...", args.api_base, args.domain)
        llm = VLLMBackend(base_url=args.api_base, model=args.model)
        extractor = ConstraintExtractor(llm=llm, domain=args.domain)

    deduplicator = ConstraintDeduplicator()
    solver = MaxSATSolver()
    scorer = InvariantScorer()

    results = []
    t_start = time.time()

    for i, prob in enumerate(problems):
        pid = prob["problem"]["id"]
        t0 = time.time()
        try:
            r = process_problem(prob, args.cache_dir, extractor, deduplicator, solver, scorer)
            results.append(r)
            elapsed = time.time() - t0
            tag = "CHANGED" if r["answer_changed"] else "same"
            logger.info(
                "[%d/%d] %s disc=%d/%d orig=%s filt=%s gt=%s %s (%.1fs)",
                i + 1, len(problems), pid,
                r["n_discriminative"], r["n_unique_constraints"],
                r["recomputed_answer"], r["filtered_answer"],
                r["ground_truth"], tag, elapsed,
            )
        except Exception as e:
            logger.error("[%d/%d] %s ERROR: %s", i + 1, len(problems), pid, e)
            results.append({"pid": pid, "error": str(e)})

    total_time = time.time() - t_start
    valid = [r for r in results if "error" not in r]
    n = len(valid)

    stored_c = sum(1 for r in valid if r["stored_correct"])
    recomp_c = sum(1 for r in valid if r["recomputed_correct"])
    filt_c = sum(1 for r in valid if r["filtered_correct"])
    sc_c = sum(1 for r in valid if r["sc_correct"])
    changed = [r for r in valid if r["answer_changed"]]

    total_uc = sum(r["n_unique_constraints"] for r in valid)
    total_disc = sum(r["n_discriminative"] for r in valid)
    total_ndisc = sum(r["n_non_discriminative"] for r in valid)

    changed_detail = []
    for r in changed:
        changed_detail.append({
            "pid": r["pid"],
            "ground_truth": r["ground_truth"],
            "original_answer": r["recomputed_answer"],
            "filtered_answer": r["filtered_answer"],
            "original_correct": r["recomputed_correct"],
            "filtered_correct": r["filtered_correct"],
            "n_constraints": r["n_unique_constraints"],
            "n_discriminative": r["n_discriminative"],
            "answer_distribution": r["answer_distribution"],
        })

    summary = {
        "n_problems": n,
        "n_errors": len(results) - n,
        "sc_accuracy": sc_c / n if n else 0,
        "stored_sica_accuracy": stored_c / n if n else 0,
        "recomputed_sica_accuracy": recomp_c / n if n else 0,
        "filtered_sica_accuracy": filt_c / n if n else 0,
        "delta_vs_stored": (filt_c - stored_c) / n if n else 0,
        "delta_vs_recomputed": (filt_c - recomp_c) / n if n else 0,
        "n_answer_changed": len(changed),
        "gained": sum(1 for c in changed_detail if c["filtered_correct"] and not c["original_correct"]),
        "lost": sum(1 for c in changed_detail if not c["filtered_correct"] and c["original_correct"]),
        "constraint_stats": {
            "total_unique": total_uc,
            "total_discriminative": total_disc,
            "total_non_discriminative": total_ndisc,
            "avg_per_problem": round(total_uc / n, 1) if n else 0,
            "avg_discriminative": round(total_disc / n, 1) if n else 0,
            "avg_filter_ratio": round(total_ndisc / total_uc, 4) if total_uc else 0,
        },
        "total_time_s": round(total_time, 1),
    }

    output = {"summary": summary, "changed_problems": changed_detail, "per_problem": results}
    os.makedirs(os.path.dirname(args.output) or ".", exist_ok=True)
    with open(args.output, "w") as f:
        json.dump(output, f, indent=2)

    print("\n" + "=" * 60)
    print("DISCRIMINATIVE FILTERING RESULTS")
    print("=" * 60)
    if n:
        print(f"Problems:          {n}")
        print(f"SC accuracy:       {sc_c}/{n} = {sc_c/n:.4f}")
        print(f"Stored SICA:       {stored_c}/{n} = {stored_c/n:.4f}")
        print(f"Recomputed SICA:   {recomp_c}/{n} = {recomp_c/n:.4f}")
        print(f"Filtered SICA:     {filt_c}/{n} = {filt_c/n:.4f}")
        print(f"Delta (vs stored): {(filt_c - stored_c)/n:+.4f}")
        print(f"Delta (vs recomp): {(filt_c - recomp_c)/n:+.4f}")
        print(f"Constraints:       {total_uc} total, {total_disc} disc, {total_ndisc} non-disc")
        if total_uc:
            print(f"Avg filter ratio:  {total_ndisc/total_uc:.1%}")
        print(f"Answer changed:    {len(changed)}/{n}")
        if changed_detail:
            gained = summary["gained"]
            lost = summary["lost"]
            neutral = len(changed_detail) - gained - lost
            print(f"  Gained: {gained}, Lost: {lost}, Neutral: {neutral}")
            for c in changed_detail:
                tag = ("GAIN" if c["filtered_correct"] and not c["original_correct"] else
                       "LOSS" if not c["filtered_correct"] and c["original_correct"] else
                       "NEUTRAL")
                print(f"  {c['pid']}: {c['original_answer']}->{c['filtered_answer']} "
                      f"(gt={c['ground_truth']}) [{tag}] disc={c['n_discriminative']}/{c['n_constraints']}")
    print(f"\nOutput: {args.output}")
    print(f"Time:   {total_time:.1f}s")


if __name__ == "__main__":
    main()
