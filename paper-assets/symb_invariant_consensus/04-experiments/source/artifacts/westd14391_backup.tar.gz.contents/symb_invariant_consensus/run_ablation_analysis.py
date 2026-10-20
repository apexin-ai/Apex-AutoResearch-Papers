"""
Phase 2: K Ablation (SICA) + Constraint Ablation from pre-extracted constraints.
CPU-only: uses z3 for dedup/MaxSAT, no LLM needed.
"""
import json, os, sys, time, random
from collections import Counter

sys.path.insert(0, "/root/symb_invariant_consensus")
random.seed(42)

CONSTRAINTS_DIR = "/root/symb_invariant_consensus/results/folio_204_14b/per_trace_constraints"
RESULTS_FILE = "/root/symb_invariant_consensus/results/folio_204_14b/folio_204_results.json"
K_ABLATION_DIR = "/root/autodl-tmp/sica_project/results/k_ablation_folio204"
CONSTRAINT_ABLATION_DIR = "/root/autodl-tmp/sica_project/results/constraint_ablation_folio204"

from sica.z3_maxsat import ConstraintDeduplicator, MaxSATSolver, MaxSATResult
from sica.scorer import InvariantScorer
from sica.pipeline import _group_logic_answers

def normalize(ans):
    ans = str(ans).strip().lower()
    if ans in ('true', 'yes', 't'): return 'True'
    elif ans in ('false', 'no', 'f'): return 'False'
    elif ans in ('unknown', 'uncertain', 'u', 'undetermined'): return 'Unknown'
    return ans.capitalize()

def sc_vote(answers):
    valid = [a.strip() for a in answers if a.strip()]
    if not valid: return ""
    groups = _group_logic_answers(valid)
    return max(groups, key=lambda k: len(groups[k]))

def run_sica(per_trace, k, mode="maxsat"):
    """Run SICA from per-trace constraints. mode: maxsat, count_only, random_weight"""
    traces_k = per_trace[:k]
    all_constraints = [t.get("constraints", []) for t in traces_k]
    trace_dicts = [{"trace_idx": t["trace_idx"], "answer": t["answer"]} for t in traces_k]
    
    dedup = ConstraintDeduplicator()
    unique = dedup.deduplicate(all_constraints)
    
    if mode == "random_weight":
        for uc in unique:
            uc.weight = random.randint(1, 10)
    
    if mode == "count_only":
        maxsat_result = MaxSATResult(
            satisfied=unique, excluded=[],
            total_weight=sum(uc.weight for uc in unique),
            solve_time_ms=0.0,
        )
    else:
        solver = MaxSATSolver()
        maxsat_result = solver.solve(unique, timeout_ms=10000)
    
    candidates = list(set(t["answer"] for t in trace_dicts if t["answer"]))
    answer_counts = Counter(t["answer"] for t in trace_dicts if t["answer"])
    scorer = InvariantScorer()
    scores = scorer.score(maxsat_result, trace_dicts, candidates)
    selected = scorer.select_answer(scores, answer_counts)
    
    return {
        "answer": normalize(selected),
        "scores": scores,
        "n_unique": len(unique),
        "n_satisfied": len(maxsat_result.satisfied),
        "n_excluded": len(maxsat_result.excluded),
    }

def main():
    with open(RESULTS_FILE) as f:
        results_data = json.load(f)
    
    # Load problems with constraints
    problems = []
    for r in results_data["results"]:
        pid = r["problem_id"]
        cfile = os.path.join(CONSTRAINTS_DIR, f"{pid}.json")
        if not os.path.exists(cfile):
            continue
        cdata = json.load(open(cfile))
        if not any(len(t.get('constraints',[])) > 0 for t in cdata.get('per_trace',[])):
            continue
        problems.append({
            "pid": pid,
            "gt": normalize(r["ground_truth"]),
            "per_trace": cdata["per_trace"],
            "stored_sica_answer": normalize(r["sica_answer"]),
            "stored_sica_correct": r["sica_correct"],
        })
    
    print(f"Problems with constraints: {len(problems)}", flush=True)
    
    # ==================== K ABLATION ====================
    print("\n=== K ABLATION ===", flush=True)
    K_VALUES = [6, 8, 11, 12]
    k_results = {}
    
    for k in K_VALUES:
        corr = {"sica": 0, "count": 0, "sc": 0}
        per_prob = []
        t0 = time.time()
        
        for pi, p in enumerate(problems):
            answers_k = [t["answer"] for t in p["per_trace"][:k] if t["answer"]]
            sc_ans = sc_vote(answers_k)
            sc_ok = (sc_ans == p["gt"])
            if sc_ok: corr["sc"] += 1
            
            try:
                sica_res = run_sica(p["per_trace"], k, "maxsat")
                sica_ans = sica_res["answer"]
            except:
                sica_ans = sc_ans
            sica_ok = (sica_ans == p["gt"])
            if sica_ok: corr["sica"] += 1
            
            try:
                count_res = run_sica(p["per_trace"], k, "count_only")
                count_ans = count_res["answer"]
            except:
                count_ans = sc_ans
            count_ok = (count_ans == p["gt"])
            if count_ok: corr["count"] += 1
            
            per_prob.append({"pid": p["pid"], "gt": p["gt"],
                "sica": sica_ans, "sica_ok": sica_ok,
                "count": count_ans, "count_ok": count_ok,
                "sc": sc_ans, "sc_ok": sc_ok})
        
        n = len(problems)
        elapsed = time.time() - t0
        k_results[k] = {
            "sica_acc": corr["sica"]/n, "sica_correct": corr["sica"],
            "count_acc": corr["count"]/n, "count_correct": corr["count"],
            "sc_acc": corr["sc"]/n, "sc_correct": corr["sc"],
            "n": n, "time_s": round(elapsed, 1),
        }
        
        delta_sica_sc = (corr["sica"]/n - corr["sc"]/n) * 100
        agree_sica_count = sum(1 for pp in per_prob if pp["sica"] == pp["count"])
        print(f"K={k:2d}: SICA={corr['sica']/n:.4f} Count={corr['count']/n:.4f} SC={corr['sc']/n:.4f} "
              f"Δ(SICA-SC)={delta_sica_sc:+.2f}pp  SICA≡Count={agree_sica_count}/{n}  [{elapsed:.1f}s]", flush=True)
    
    # ==================== CONSTRAINT ABLATION @K=12 ====================
    print("\n=== CONSTRAINT ABLATION (K=12) ===", flush=True)
    n = len(problems)
    N_RANDOM = 5
    
    maxsat_corr = 0; count_corr = 0; sc_corr = 0
    random_corr = [0]*N_RANDOM
    agree_mc = 0; agree_mr = [0]*N_RANDOM
    
    per_prob_abl = []
    t0 = time.time()
    
    for p in problems:
        gt = p["gt"]
        answers = [t["answer"] for t in p["per_trace"] if t["answer"]]
        sc_ans = sc_vote(answers)
        sc_ok = (sc_ans == gt)
        if sc_ok: sc_corr += 1
        
        try:
            ms = run_sica(p["per_trace"], 12, "maxsat")
            ms_ans = ms["answer"]
        except:
            ms_ans = sc_ans
        ms_ok = (ms_ans == gt)
        if ms_ok: maxsat_corr += 1
        
        try:
            co = run_sica(p["per_trace"], 12, "count_only")
            co_ans = co["answer"]
        except:
            co_ans = sc_ans
        co_ok = (co_ans == gt)
        if co_ok: count_corr += 1
        
        if ms_ans == co_ans: agree_mc += 1
        
        rand_ans_list = []
        for trial in range(N_RANDOM):
            random.seed(42 + trial)
            try:
                rr = run_sica(p["per_trace"], 12, "random_weight")
                ra = rr["answer"]
            except:
                ra = sc_ans
            rand_ans_list.append(ra)
            if ra == gt: random_corr[trial] += 1
            if ra == ms_ans: agree_mr[trial] += 1
        
        per_prob_abl.append({"pid": p["pid"], "gt": gt,
            "maxsat": ms_ans, "count_only": co_ans, "sc": sc_ans,
            "random": rand_ans_list})
    
    elapsed = time.time() - t0
    rand_acc_mean = sum(c/n for c in random_corr) / N_RANDOM
    rand_agree_mean = sum(a for a in agree_mr) / N_RANDOM
    
    print(f"\n{'Method':>15} | {'Accuracy':>8} | {'Correct':>7} | vs MaxSAT agree")
    print("-"*60)
    print(f"{'MaxSAT (SICA)':>15} | {maxsat_corr/n:.4f}   | {maxsat_corr:>7} | -")
    print(f"{'Count-only':>15} | {count_corr/n:.4f}   | {count_corr:>7} | {agree_mc}/{n}")
    print(f"{'Random-weight':>15} | {rand_acc_mean:.4f}   | {'~':>7} | {rand_agree_mean:.0f}/{n}")
    print(f"{'SC baseline':>15} | {sc_corr/n:.4f}   | {sc_corr:>7} | -")
    print(f"[{elapsed:.1f}s]", flush=True)
    
    # Save results
    os.makedirs(K_ABLATION_DIR, exist_ok=True)
    os.makedirs(CONSTRAINT_ABLATION_DIR, exist_ok=True)
    
    k_output = {
        "experiment": "exp-036-k-ablation-folio204",
        "dataset": "FOLIO-204", "model": "Qwen2.5-14B-Instruct",
        "extraction_model": "Qwen3-14B",
        "n_problems": n,
        "k_ablation": {str(k): {kk: vv for kk, vv in v.items()} for k, v in k_results.items()},
    }
    with open(os.path.join(K_ABLATION_DIR, "k_ablation_sica_results.json"), "w") as f:
        json.dump(k_output, f, indent=2)
    
    abl_output = {
        "experiment": "exp-037-constraint-ablation-folio204",
        "dataset": "FOLIO-204", "model": "Qwen2.5-14B-Instruct",
        "extraction_model": "Qwen3-14B",
        "n_problems": n,
        "maxsat_accuracy": round(maxsat_corr/n, 4),
        "count_only_accuracy": round(count_corr/n, 4),
        "random_weight_mean_accuracy": round(rand_acc_mean, 4),
        "sc_accuracy": round(sc_corr/n, 4),
        "maxsat_correct": maxsat_corr,
        "count_only_correct": count_corr,
        "sc_correct": sc_corr,
        "agreement_maxsat_vs_countonly": f"{agree_mc}/{n}",
        "agreement_maxsat_vs_randomwt_mean": f"{rand_agree_mean:.0f}/{n}",
    }
    with open(os.path.join(CONSTRAINT_ABLATION_DIR, "constraint_ablation_results.json"), "w") as f:
        json.dump(abl_output, f, indent=2)
    
    print(f"\nSaved K ablation to {K_ABLATION_DIR}")
    print(f"Saved constraint ablation to {CONSTRAINT_ABLATION_DIR}")
    print("ANALYSIS_COMPLETE", flush=True)

if __name__ == "__main__":
    main()
