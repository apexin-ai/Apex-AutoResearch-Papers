"""
Constraint Ablation + SICA K-Ablation on FOLIO 204.
Phase 1: Extract per-trace constraints from stored traces (needs LLM).
Phase 2: Run three aggregation comparisons + K ablation (CPU-only).

Usage:
  python analysis_constraint_ablation_folio204.py --extract   # Phase 1: extract constraints
  python analysis_constraint_ablation_folio204.py --analyze   # Phase 2: run ablations
  python analysis_constraint_ablation_folio204.py --all       # Both phases
"""
import json
import os
import sys
import time
import random
import argparse
from collections import Counter
from concurrent.futures import ThreadPoolExecutor, as_completed

sys.path.insert(0, "/root/symb_invariant_consensus")

random.seed(42)

INTERMEDIATES_DIR = "/root/symb_invariant_consensus/results/folio_204_14b/intermediates"
RESULTS_FILE = "/root/symb_invariant_consensus/results/folio_204_14b/folio_204_results.json"
CONSTRAINTS_DIR = "/root/symb_invariant_consensus/results/folio_204_14b/per_trace_constraints"
K_ABLATION_DIR = "/root/autodl-tmp/sica_project/results/k_ablation_folio204"
CONSTRAINT_ABLATION_DIR = "/root/autodl-tmp/sica_project/results/constraint_ablation_folio204"

API_BASE = "http://localhost:8001/v1"


def normalize_logic_answer(ans):
    ans = str(ans).strip().lower()
    if ans in ("true", "yes", "t"): return "True"
    elif ans in ("false", "no", "f"): return "False"
    elif ans in ("unknown", "uncertain", "u", "undetermined"): return "Unknown"
    return ans.capitalize()


def load_problems():
    with open(RESULTS_FILE) as f:
        data = json.load(f)
    problems = []
    for r in data["results"]:
        pid = r["problem_id"]
        with open(os.path.join(INTERMEDIATES_DIR, f"{pid}.json")) as f:
            intermed = json.load(f)
        problems.append({
            "pid": pid,
            "gt": normalize_logic_answer(r["ground_truth"]),
            "dataset": r["dataset"],
            "traces": intermed["sica_result"]["traces"],
            "sica_answer": normalize_logic_answer(r["sica_answer"]),
            "sica_correct": r["sica_correct"],
        })
    return problems


# ---- Phase 1: Extract per-trace constraints ----

def extract_constraints_for_trace(trace_text, api_base=API_BASE):
    """Extract constraints from a single trace using vLLM API."""
    from sica.constraint_extractor import LOGIC_EXTRACTION_PROMPT
    import httpx
    
    prompt = LOGIC_EXTRACTION_PROMPT.format(trace=trace_text)
    payload = {
        "model": "auto",
        "messages": [{"role": "user", "content": prompt}],
        "max_tokens": 2048,
        "temperature": 0.1,
    }
    try:
        resp = httpx.post(f"{api_base}/chat/completions", json=payload, timeout=60)
        resp.raise_for_status()
        raw = resp.json()["choices"][0]["message"]["content"]
        return parse_extraction_response(raw)
    except Exception as e:
        return {"error": str(e), "constraints": []}


def parse_extraction_response(raw):
    """Parse LLM extraction response into constraints list."""
    import re
    text = raw.strip()
    # Strip thinking tags if present
    text = re.sub(r'<think>.*?</think>', '', text, flags=re.DOTALL).strip()
    # Find JSON
    json_match = re.search(r'\{[\s\S]*\}', text)
    if not json_match:
        return {"error": "no JSON found", "constraints": []}
    try:
        data = json.loads(json_match.group())
        constraints = data.get("constraints", [])
        answer = data.get("answer", "")
        return {"constraints": constraints, "extracted_answer": answer}
    except json.JSONDecodeError:
        return {"error": "JSON parse failed", "constraints": []}


def extract_all_constraints(problems, max_workers=2):
    """Extract constraints from all traces of all problems."""
    os.makedirs(CONSTRAINTS_DIR, exist_ok=True)
    
    total = sum(len(p["traces"]) for p in problems)
    done = 0
    skipped = 0
    t_start = time.time()
    
    for pi, p in enumerate(problems):
        pid = p["pid"]
        out_file = os.path.join(CONSTRAINTS_DIR, f"{pid}.json")
        
        # Skip if already extracted
        if os.path.exists(out_file):
            with open(out_file) as f:
                existing = json.load(f)
            if len(existing.get("per_trace", [])) == len(p["traces"]):
                skipped += len(p["traces"])
                done += len(p["traces"])
                continue
        
        per_trace = []
        for ti, trace in enumerate(p["traces"]):
            result = extract_constraints_for_trace(trace["trace"])
            per_trace.append({
                "trace_idx": trace["trace_idx"],
                "answer": normalize_logic_answer(trace["answer"]),
                "constraints": result.get("constraints", []),
                "extracted_answer": result.get("extracted_answer", ""),
                "error": result.get("error"),
            })
            done += 1
            
            if done % 24 == 0:
                elapsed = time.time() - t_start
                rate = (done - skipped) / elapsed if elapsed > 0 else 0
                eta = (total - done) / rate / 60 if rate > 0 else 0
                print(f"  [{done}/{total}] {pid} trace {ti}  rate={rate:.1f}/s  ETA={eta:.1f}min")
        
        with open(out_file, "w") as f:
            json.dump({"pid": pid, "gt": p["gt"], "per_trace": per_trace}, f, indent=2)
    
    elapsed = time.time() - t_start
    print(f"Extraction done: {done} traces ({skipped} skipped), {elapsed:.1f}s")


# ---- Phase 2: Analysis (CPU-only) ----

def load_constraints(pid):
    """Load per-trace constraints for a problem."""
    path = os.path.join(CONSTRAINTS_DIR, f"{pid}.json")
    if not os.path.exists(path):
        return None
    with open(path) as f:
        return json.load(f)


def run_sica_from_constraints(per_trace_data, k, mode="maxsat"):
    """
    Run SICA scoring from stored per-trace constraints.
    mode: "maxsat" (original), "count_only", "random_weight"
    Uses first k traces.
    """
    from sica.z3_maxsat import ConstraintDeduplicator, MaxSATSolver, UniqueConstraint
    from sica.scorer import InvariantScorer
    
    traces_k = per_trace_data[:k]
    
    # Build raw constraint lists (one per trace)
    all_constraints = []
    trace_dicts = []
    for t in traces_k:
        constraints = t.get("constraints", [])
        all_constraints.append(constraints)
        trace_dicts.append({"trace_idx": t["trace_idx"], "answer": t["answer"]})
    
    # Deduplicate
    deduplicator = ConstraintDeduplicator()
    unique_constraints = deduplicator.deduplicate(all_constraints)
    
    if mode == "random_weight":
        for uc in unique_constraints:
            uc.weight = random.randint(1, 10)
    
    # MaxSAT or count-only
    if mode == "count_only":
        # Skip MaxSAT: treat all parseable constraints as "satisfied"
        from sica.z3_maxsat import MaxSATResult
        satisfied = unique_constraints
        excluded = []
        maxsat_result = MaxSATResult(
            satisfied=satisfied, excluded=excluded,
            total_weight=sum(uc.weight for uc in satisfied),
            solve_time_ms=0.0,
        )
    else:
        solver = MaxSATSolver()
        maxsat_result = solver.solve(unique_constraints, timeout_ms=10000)
    
    # Score
    candidates = list(set(t["answer"] for t in trace_dicts if t["answer"]))
    answer_counts = Counter(t["answer"] for t in trace_dicts if t["answer"])
    scorer = InvariantScorer()
    scores = scorer.score(maxsat_result, trace_dicts, candidates)
    selected = scorer.select_answer(scores, answer_counts)
    
    return {
        "answer": selected,
        "scores": scores,
        "answer_counts": dict(answer_counts),
        "n_unique": len(unique_constraints),
        "n_satisfied": len(maxsat_result.satisfied),
        "n_excluded": len(maxsat_result.excluded),
    }


def sc_vote(answers):
    from sica.pipeline import _group_logic_answers
    valid = [a.strip() for a in answers if a.strip()]
    if not valid:
        return ""
    groups = _group_logic_answers(valid)
    return max(groups, key=lambda k: len(groups[k]))


def run_k_ablation_sica(problems):
    """K ablation: compute SICA at different K values."""
    K_VALUES = [6, 8, 11, 12]
    results = {}
    
    for k in K_VALUES:
        correct = {"maxsat": 0, "count_only": 0, "sc": 0}
        total = 0
        per_problem = []
        
        for p in problems:
            cdata = load_constraints(p["pid"])
            if not cdata:
                continue
            total += 1
            
            # SC
            answers_k = [t["answer"] for t in cdata["per_trace"][:k] if t["answer"]]
            sc_ans = sc_vote(answers_k)
            sc_correct = (sc_ans == p["gt"])
            if sc_correct:
                correct["sc"] += 1
            
            # SICA (MaxSAT)
            try:
                sica_res = run_sica_from_constraints(cdata["per_trace"], k, "maxsat")
                sica_ans = normalize_logic_answer(sica_res["answer"])
            except Exception as e:
                sica_ans = sc_ans  # fallback
            sica_correct = (sica_ans == p["gt"])
            if sica_correct:
                correct["maxsat"] += 1
            
            # Count-only
            try:
                count_res = run_sica_from_constraints(cdata["per_trace"], k, "count_only")
                count_ans = normalize_logic_answer(count_res["answer"])
            except Exception:
                count_ans = sc_ans
            count_correct = (count_ans == p["gt"])
            if count_correct:
                correct["count_only"] += 1
            
            per_problem.append({
                "pid": p["pid"],
                "gt": p["gt"],
                "sc": sc_ans, "sc_correct": sc_correct,
                "sica": sica_ans, "sica_correct": sica_correct,
                "count_only": count_ans, "count_correct": count_correct,
            })
        
        results[k] = {
            "k": k,
            "n": total,
            "sc_acc": correct["sc"] / total if total else 0,
            "sica_acc": correct["maxsat"] / total if total else 0,
            "count_only_acc": correct["count_only"] / total if total else 0,
            "sc_correct": correct["sc"],
            "sica_correct": correct["maxsat"],
            "count_only_correct": correct["count_only"],
            "per_problem": per_problem,
        }
    
    return results


def run_constraint_ablation(problems):
    """Constraint ablation: MaxSAT vs count-only vs random-weight at K=12."""
    n_random_trials = 5
    
    maxsat_correct = 0
    count_correct = 0
    random_correct_trials = [0] * n_random_trials
    sc_correct_count = 0
    total = 0
    
    agreement_maxsat_count = 0
    agreement_maxsat_random = [0] * n_random_trials
    
    per_problem = []
    
    for p in problems:
        cdata = load_constraints(p["pid"])
        if not cdata:
            continue
        total += 1
        
        # SC
        answers = [t["answer"] for t in cdata["per_trace"] if t["answer"]]
        sc_ans = sc_vote(answers)
        sc_ok = (sc_ans == p["gt"])
        if sc_ok:
            sc_correct_count += 1
        
        # MaxSAT
        try:
            maxsat_res = run_sica_from_constraints(cdata["per_trace"], 12, "maxsat")
            maxsat_ans = normalize_logic_answer(maxsat_res["answer"])
        except Exception:
            maxsat_ans = sc_ans
        maxsat_ok = (maxsat_ans == p["gt"])
        if maxsat_ok:
            maxsat_correct += 1
        
        # Count-only
        try:
            count_res = run_sica_from_constraints(cdata["per_trace"], 12, "count_only")
            count_ans = normalize_logic_answer(count_res["answer"])
        except Exception:
            count_ans = sc_ans
        count_ok = (count_ans == p["gt"])
        if count_ok:
            count_correct += 1
        
        if maxsat_ans == count_ans:
            agreement_maxsat_count += 1
        
        # Random-weight (multiple trials)
        random_answers = []
        for trial in range(n_random_trials):
            random.seed(42 + trial)
            try:
                rand_res = run_sica_from_constraints(cdata["per_trace"], 12, "random_weight")
                rand_ans = normalize_logic_answer(rand_res["answer"])
            except Exception:
                rand_ans = sc_ans
            random_answers.append(rand_ans)
            if rand_ans == p["gt"]:
                random_correct_trials[trial] += 1
            if rand_ans == maxsat_ans:
                agreement_maxsat_random[trial] += 1
        
        per_problem.append({
            "pid": p["pid"], "gt": p["gt"],
            "maxsat": maxsat_ans, "count_only": count_ans, "sc": sc_ans,
            "random_weights": random_answers,
        })
    
    random_accs = [c / total for c in random_correct_trials]
    random_agree = [a / total for a in agreement_maxsat_random]
    
    return {
        "n": total,
        "maxsat_accuracy": maxsat_correct / total if total else 0,
        "count_only_accuracy": count_correct / total if total else 0,
        "random_weight_mean_accuracy": sum(random_accs) / len(random_accs),
        "sc_accuracy": sc_correct_count / total if total else 0,
        "maxsat_correct": maxsat_correct,
        "count_only_correct": count_correct,
        "sc_correct": sc_correct_count,
        "agreement_maxsat_vs_countonly": f"{agreement_maxsat_count}/{total}",
        "agreement_maxsat_vs_randomwt_mean": f"{sum(agreement_maxsat_random)/len(agreement_maxsat_random):.0f}/{total}",
        "per_problem": per_problem,
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--extract", action="store_true", help="Phase 1: extract constraints")
    parser.add_argument("--analyze", action="store_true", help="Phase 2: run ablations")
    parser.add_argument("--all", action="store_true", help="Both phases")
    args = parser.parse_args()
    
    if not (args.extract or args.analyze or args.all):
        args.all = True
    
    problems = load_problems()
    print(f"Loaded {len(problems)} problems")
    
    if args.extract or args.all:
        print("\n=== Phase 1: Extracting per-trace constraints ===")
        extract_all_constraints(problems)
    
    if args.analyze or args.all:
        # Check if constraints are available
        available = sum(1 for p in problems if os.path.exists(os.path.join(CONSTRAINTS_DIR, f"{p['pid']}.json")))
        print(f"\n=== Phase 2: Analysis ({available}/{len(problems)} problems have constraints) ===")
        
        if available == 0:
            print("ERROR: No constraints extracted. Run --extract first.")
            return
        
        # K Ablation with SICA
        print("\n--- K Ablation (SICA + SC) ---")
        k_results = run_k_ablation_sica(problems)
        
        print(f"\n{'K':>4} | {'SICA':>8} | {'Count-only':>10} | {'SC':>8} | {'Δ(SICA-SC)':>10}")
        print("-" * 55)
        for k in sorted(k_results.keys()):
            r = k_results[k]
            delta = (r["sica_acc"] - r["sc_acc"]) * 100
            print(f"{k:>4} | {r['sica_acc']:.4f}   | {r['count_only_acc']:.4f}     | {r['sc_acc']:.4f}   | {delta:+.2f}pp")
        
        os.makedirs(K_ABLATION_DIR, exist_ok=True)
        k_out = {str(k): {kk: vv for kk, vv in v.items() if kk != "per_problem"} for k, v in k_results.items()}
        with open(os.path.join(K_ABLATION_DIR, "k_ablation_sica_results.json"), "w") as f:
            json.dump(k_out, f, indent=2)
        
        # Constraint Ablation
        print("\n--- Constraint Ablation (MaxSAT vs Count-only vs Random-weight) ---")
        ablation = run_constraint_ablation(problems)
        
        print(f"\n{'Method':>15} | {'Accuracy':>8} | {'Correct':>8}")
        print("-" * 40)
        print(f"{'MaxSAT (SICA)':>15} | {ablation['maxsat_accuracy']:.4f}   | {ablation['maxsat_correct']}")
        print(f"{'Count-only':>15} | {ablation['count_only_accuracy']:.4f}   | {ablation['count_only_correct']}")
        print(f"{'Random-weight':>15} | {ablation['random_weight_mean_accuracy']:.4f}   | -")
        print(f"{'SC baseline':>15} | {ablation['sc_accuracy']:.4f}   | {ablation['sc_correct']}")
        print(f"\nAgreement MaxSAT vs Count-only: {ablation['agreement_maxsat_vs_countonly']}")
        print(f"Agreement MaxSAT vs Random-wt:  {ablation['agreement_maxsat_vs_randomwt_mean']}")
        
        os.makedirs(CONSTRAINT_ABLATION_DIR, exist_ok=True)
        abl_out = {k: v for k, v in ablation.items() if k != "per_problem"}
        with open(os.path.join(CONSTRAINT_ABLATION_DIR, "constraint_ablation_results.json"), "w") as f:
            json.dump(abl_out, f, indent=2)
        
        print(f"\nResults saved to {K_ABLATION_DIR} and {CONSTRAINT_ABLATION_DIR}")


if __name__ == "__main__":
    main()
