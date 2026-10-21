"""
Direction D — CEGIS Iterative Refinement of SICA
Compares 1-round vs 2-round vs 3-round constraint extraction on FOLIO-204.
Uses existing exp-033 traces (Mistral-7B), iterates with Z3 UNSAT core feedback.
"""

import argparse
import json
import os
import re
import sys
import time
import logging
from collections import Counter
from concurrent.futures import ThreadPoolExecutor, as_completed

sys.path.insert(0, '/root/symb_invariant_consensus')

from sica.constraint_extractor import LOGIC_EXTRACTION_PROMPT
from sica.z3_feedback import REFINEMENT_PROMPT
from sica.z3_maxsat import ConstraintDeduplicator, MaxSATSolver, parse_z3_formula
from sica.scorer import InvariantScorer

import httpx
import z3

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s",
    handlers=[logging.StreamHandler(sys.stdout)],
)
logger = logging.getLogger(__name__)
logging.getLogger("httpx").setLevel(logging.WARNING)

API_BASE = "http://localhost:8021/v1"
EXP_DIR = "/root/symb_invariant_consensus/results/exp033_mistral_7b_folio204"
OUTPUT_DIR = "/root/symb_invariant_consensus/results/direction_d_cegis"
MAX_ROUNDS = 3
T_EXTRACT = 0.1
T_REFINE = 0.3
MAX_TOKENS = 2048
CONCURRENCY = 12


def get_model_id():
    r = httpx.get(f"{API_BASE}/models", timeout=10)
    r.raise_for_status()
    return r.json()["data"][0]["id"]


def normalize(ans):
    ans = str(ans).strip().lower()
    if ans in ("true", "yes", "t"):
        return "True"
    if ans in ("false", "no", "f"):
        return "False"
    if ans in ("unknown", "uncertain", "u", "undetermined"):
        return "Unknown"
    return ans.capitalize()


def strip_thinking(text):
    return re.sub(r"<think>.*?</think>", "", text, flags=re.DOTALL).strip()


def llm_call(model_id, prompt, temperature):
    payload = {
        "model": model_id,
        "messages": [{"role": "user", "content": prompt}],
        "max_tokens": MAX_TOKENS,
        "temperature": temperature,
    }
    resp = httpx.post(f"{API_BASE}/chat/completions", json=payload, timeout=180)
    resp.raise_for_status()
    return strip_thinking(resp.json()["choices"][0]["message"]["content"])


def parse_json_response(text):
    m = re.search(r"\{[\s\S]*\}", text)
    if not m:
        return None
    s = m.group()
    try:
        return json.loads(s)
    except json.JSONDecodeError:
        s2 = re.sub(r",\s*}", "}", s)
        s2 = re.sub(r",\s*]", "]", s2)
        try:
            return json.loads(s2)
        except json.JSONDecodeError:
            return None


def extract_constraints(model_id, trace_text):
    prompt = LOGIC_EXTRACTION_PROMPT.format(trace=trace_text)
    try:
        raw = llm_call(model_id, prompt, T_EXTRACT)
        data = parse_json_response(raw)
        if data is None:
            return []
        return data.get("constraints", [])
    except Exception as e:
        logger.warning("Extraction error: %s", str(e)[:120])
        return []


def extract_all_traces(model_id, traces):
    results = [None] * len(traces)
    with ThreadPoolExecutor(max_workers=CONCURRENCY) as executor:
        futures = {}
        for i, t in enumerate(traces):
            future = executor.submit(extract_constraints, model_id, t["trace"])
            futures[future] = i
        for future in as_completed(futures):
            i = futures[future]
            try:
                results[i] = future.result()
            except Exception:
                results[i] = []
    return results


def z3_check(constraints):
    parsed = []
    valid_map = []
    for i, c in enumerate(constraints):
        f = parse_z3_formula(c.get("z3_formula", ""))
        if f is not None and z3.is_bool(f):
            parsed.append(f)
            valid_map.append(i)
    if len(parsed) < 2:
        return "trivial", []
    solver = z3.Solver()
    solver.set("timeout", 5000)
    trackers = []
    for j, f in enumerate(parsed):
        t = z3.Bool(f"__t{j}")
        solver.assert_and_track(f, t)
        trackers.append(t)
    r = solver.check()
    if r == z3.unsat:
        core = solver.unsat_core()
        core_c = []
        for item in core:
            name = str(item)
            if name.startswith("__t"):
                j = int(name[3:])
                if j < len(valid_map):
                    core_c.append(constraints[valid_map[j]])
        return "unsat", core_c
    if r == z3.sat:
        return "sat", []
    return "unknown", []


def refine_constraints(model_id, constraints, core_c, trace_text, problem_text):
    prompt = REFINEMENT_PROMPT.format(
        problem=problem_text,
        trace=trace_text,
        all_constraints=json.dumps(constraints, indent=2, ensure_ascii=False),
        unsat_core=json.dumps(core_c, indent=2, ensure_ascii=False),
    )
    try:
        raw = llm_call(model_id, prompt, T_REFINE)
        data = parse_json_response(raw)
        if data and data.get("constraints"):
            return data["constraints"]
        return constraints
    except Exception as e:
        logger.warning("Refinement error: %s", str(e)[:120])
        return constraints


def refine_round(model_id, per_trace, trace_map, problem_text):
    unsat_jobs = []
    for i, td in enumerate(per_trace):
        c = td["constraints"]
        if len(c) < 2:
            continue
        status, core_c = z3_check(c)
        if status == "unsat":
            unsat_jobs.append((i, c, core_c))

    if not unsat_jobs:
        return per_trace, 0

    refined_map = {}
    with ThreadPoolExecutor(max_workers=CONCURRENCY) as executor:
        futures = {}
        for i, c, core_c in unsat_jobs:
            tidx = per_trace[i]["trace_idx"]
            future = executor.submit(
                refine_constraints, model_id, c, core_c,
                trace_map.get(tidx, ""), problem_text)
            futures[future] = i
        for future in as_completed(futures):
            i = futures[future]
            try:
                refined_map[i] = future.result()
            except Exception:
                refined_map[i] = per_trace[i]["constraints"]

    result = []
    for i, td in enumerate(per_trace):
        if i in refined_map:
            result.append({"trace_idx": td["trace_idx"], "answer": td["answer"],
                           "constraints": refined_map[i]})
        else:
            result.append(td)
    return result, len(unsat_jobs)


def sica_score(per_trace):
    dedup = ConstraintDeduplicator()
    solver = MaxSATSolver()
    scorer = InvariantScorer()
    all_c = [t.get("constraints", []) for t in per_trace]
    unique = dedup.deduplicate(all_c)
    maxsat = solver.solve(unique, timeout_ms=10000)
    answers = [t["answer"] for t in per_trace]
    candidates = sorted(set(a for a in answers if a))
    counts = Counter(answers)
    traces_for = [{"answer": t["answer"], "trace_idx": t["trace_idx"]} for t in per_trace]
    scores = scorer.score(maxsat, traces_for, candidates)
    return scorer.select_answer(scores, counts)


def sc_vote(traces):
    counts = Counter(t["answer"] for t in traces if t["answer"])
    return counts.most_common(1)[0][0] if counts else ""


def load_problems():
    d = os.path.join(EXP_DIR, "intermediates")
    problems = []
    for fname in sorted(os.listdir(d)):
        if not fname.endswith(".json"):
            continue
        with open(os.path.join(d, fname)) as f:
            data = json.load(f)
        prob = data["problem"]
        sica = data["sica_result"]
        traces = [
            {"trace_idx": t["trace_idx"], "trace": t["trace"],
             "answer": normalize(t["answer"])}
            for t in sica["traces"]
        ]
        problems.append({
            "pid": prob["id"], "text": prob["problem"],
            "gt": normalize(prob["answer"]), "traces": traces,
        })
    return problems


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    os.makedirs(OUTPUT_DIR, exist_ok=True)
    model_id = get_model_id()
    logger.info("Model: %s", model_id)

    problems = load_problems()
    if args.dry_run:
        problems = problems[:2]
        logger.info("DRY RUN: processing %d problems only", len(problems))

    n = len(problems)
    logger.info("Loaded %d problems", n)

    round_stats = {r: {"correct": 0, "constraints": [], "unsat_traces": 0,
                       "total_traces": 0}
                   for r in range(1, MAX_ROUNDS + 1)}
    sc_correct = 0
    n_extract = 0
    n_refine = 0
    per_problem = []
    t0 = time.time()

    for pi, prob in enumerate(problems):
        pid, gt, text = prob["pid"], prob["gt"], prob["text"]
        traces = prob["traces"]
        trace_map = {t["trace_idx"]: t["trace"] for t in traces}

        sc_ans = sc_vote(traces)
        if sc_ans == gt:
            sc_correct += 1

        detail_file = os.path.join(OUTPUT_DIR, f"{pid}.json")
        if not args.dry_run and os.path.exists(detail_file):
            try:
                with open(detail_file) as f:
                    cached = json.load(f)
                if cached.get("complete"):
                    pr = cached["result"]
                    per_problem.append(pr)
                    for r in range(1, MAX_ROUNDS + 1):
                        if pr[f"r{r}_correct"]:
                            round_stats[r]["correct"] += 1
                        round_stats[r]["constraints"].append(pr[f"r{r}_n_constraints"])
                        round_stats[r]["unsat_traces"] += pr[f"r{r}_unsat_traces"]
                        round_stats[r]["total_traces"] += len(traces)
                    n_extract += cached.get("n_extract", len(traces))
                    n_refine += cached.get("n_refine", 0)
                    if (pi + 1) % 20 == 0:
                        logger.info("[%d/%d] (cached)", pi + 1, n)
                    continue
            except (json.JSONDecodeError, KeyError):
                pass

        t_prob = time.time()
        constraint_lists = extract_all_traces(model_id, traces)
        n_extract += len(traces)
        r1 = [{"trace_idx": traces[i]["trace_idx"], "answer": traces[i]["answer"],
                "constraints": constraint_lists[i]}
               for i in range(len(traces))]

        rounds = {1: r1}
        local_refine = 0
        for rnd in range(2, MAX_ROUNDS + 1):
            refined, n_ref = refine_round(model_id, rounds[rnd - 1], trace_map, text)
            rounds[rnd] = refined
            local_refine += n_ref
            n_refine += n_ref

        prob_result = {"pid": pid, "gt": gt, "sc_answer": sc_ans,
                       "sc_correct": sc_ans == gt}
        for rnd in range(1, MAX_ROUNDS + 1):
            rd = rounds[rnd]
            ans = sica_score(rd)
            correct = ans == gt
            if correct:
                round_stats[rnd]["correct"] += 1
            nc = sum(len(t["constraints"]) for t in rd)
            round_stats[rnd]["constraints"].append(nc)
            round_stats[rnd]["total_traces"] += len(rd)

            unsat_count = 0
            for t in rd:
                if len(t["constraints"]) >= 2:
                    s, _ = z3_check(t["constraints"])
                    if s == "unsat":
                        unsat_count += 1
            round_stats[rnd]["unsat_traces"] += unsat_count

            prob_result[f"r{rnd}_answer"] = ans
            prob_result[f"r{rnd}_correct"] = correct
            prob_result[f"r{rnd}_n_constraints"] = nc
            prob_result[f"r{rnd}_unsat_traces"] = unsat_count

        per_problem.append(prob_result)
        prob_time = time.time() - t_prob

        with open(detail_file, "w") as f:
            json.dump({
                "complete": True,
                "result": prob_result,
                "n_extract": len(traces),
                "n_refine": local_refine,
                "rounds": {
                    str(r): [
                        {"trace_idx": t["trace_idx"], "answer": t["answer"],
                         "constraints": t["constraints"]}
                        for t in rounds[r]
                    ]
                    for r in range(1, MAX_ROUNDS + 1)
                },
            }, f, indent=2, ensure_ascii=False)

        if (pi + 1) % 10 == 0 or pi + 1 == n:
            elapsed = time.time() - t0
            rate = (pi + 1) / elapsed
            eta = (n - pi - 1) / rate if rate > 0 else 0
            accs = " ".join(
                f"R{r}={round_stats[r]['correct']/(pi+1):.3f}"
                for r in range(1, MAX_ROUNDS + 1)
            )
            logger.info(
                "[%d/%d] SC=%.3f %s  calls=%d+%d  %.1fs/prob ETA=%.0fs",
                pi + 1, n, sc_correct / (pi + 1), accs,
                n_extract, n_refine, prob_time, eta,
            )
            sys.stdout.flush()

    sc_acc = sc_correct / n
    r1_acc = round_stats[1]["correct"] / n

    summary = {
        "n": n, "model": model_id,
        "sc_accuracy": round(sc_acc, 4), "sc_correct": sc_correct,
        "rounds": {},
        "extraction_calls": n_extract,
        "refinement_calls": n_refine,
        "wall_s": round(time.time() - t0, 1),
    }
    for rnd in range(1, MAX_ROUNDS + 1):
        s = round_stats[rnd]
        avg_c = sum(s["constraints"]) / n if s["constraints"] else 0
        total_t = s["total_traces"]
        acc = s["correct"] / n
        summary["rounds"][str(rnd)] = {
            "accuracy": round(acc, 4),
            "correct": s["correct"],
            "avg_constraints_per_q": round(avg_c, 1),
            "unsat_traces": s["unsat_traces"],
            "unsat_rate": round(s["unsat_traces"] / total_t, 4) if total_t else 0,
            "delta_vs_sc": round(acc - sc_acc, 4),
            "delta_vs_r1": round(acc - r1_acc, 4),
        }

    output = {"summary": summary, "per_problem": per_problem}
    results_file = os.path.join(OUTPUT_DIR, "results.json")
    with open(results_file, "w") as f:
        json.dump(output, f, indent=2, ensure_ascii=False)

    print("\n" + "=" * 85)
    print("Direction D — CEGIS Iterative Refinement Results")
    print("=" * 85)
    print(f"{'Rounds':<10}{'Constr/Q':<12}{'UNSAT Rate':<14}{'Accuracy':<12}"
          f"{'dv SC':<12}{'dv R1':<12}")
    print("-" * 85)
    for rnd in range(1, MAX_ROUNDS + 1):
        rd = summary["rounds"][str(rnd)]
        ur = f"{rd['unsat_rate']:.1%}"
        d_sc = f"{rd['delta_vs_sc']:+.4f}"
        d_r1 = f"{rd['delta_vs_r1']:+.4f}" if rnd > 1 else "---"
        print(f"{rnd:<10}{rd['avg_constraints_per_q']:<12.1f}{ur:<14}"
              f"{rd['accuracy']:<12.4f}{d_sc:<12}{d_r1:<12}")

    print(f"\nSC baseline: {sc_acc:.4f} ({sc_correct}/{n})")
    print(f"LLM calls: {n_extract} extract + {n_refine} refine = "
          f"{n_extract + n_refine} total")
    print(f"Wall time: {summary['wall_s']:.0f}s")
    print(f"Results: {results_file}")
    sys.stdout.flush()


if __name__ == "__main__":
    main()
