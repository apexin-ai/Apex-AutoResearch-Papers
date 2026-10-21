"""
Constraint Ablation: MaxSAT vs Count-only vs Random-weight MaxSAT
"""
import json, os, glob, random
from collections import Counter, defaultdict

random.seed(42)

# ============ HELPERS ============

def load_intermediates(dir_path):
    """Load all intermediates JSONs from a directory."""
    results = []
    for f in sorted(glob.glob(os.path.join(dir_path, "*.json"))):
        with open(f) as fp:
            results.append(json.load(fp))
    return results

def count_only_answer(answer_counts):
    """Pick answer with highest count. Alphabetical tiebreak."""
    if not answer_counts:
        return None
    max_count = max(answer_counts.values())
    tied = sorted([a for a, c in answer_counts.items() if c == max_count])
    return tied[0]

def maxsat_answer_from_scores(scores):
    """Pick answer with highest MaxSAT score. Alphabetical tiebreak."""
    if not scores:
        return None
    max_score = max(scores.values())
    tied = sorted([a for a, s in scores.items() if s == max_score])
    return tied[0]

def normalize_answer(ans):
    """Normalize answer labels."""
    if ans is None:
        return None
    ans_lower = ans.strip().lower()
    if ans_lower in ("true", "proved", "yes"):
        return "True"
    if ans_lower in ("false", "disproved", "no"):
        return "False"
    if ans_lower in ("unknown", "uncertain", "undetermined"):
        return "Unknown"
    return ans

# ============ ANALYSIS 1: 14B Intermediates (MaxSAT vs Count-only) ============

def analyze_intermediates(dir_path, dataset_name):
    """Analyze MaxSAT vs Count-only from intermediates."""
    data = load_intermediates(dir_path)
    
    maxsat_correct = 0
    count_correct = 0
    maxsat_count_agree = 0
    total = 0
    
    # Track cases where they disagree
    disagree_cases = []
    
    for item in data:
        gt = normalize_answer(item["problem"]["answer"])
        sica = item.get("sica_result", {})
        
        # MaxSAT answer (as stored)
        maxsat_ans = normalize_answer(sica.get("answer"))
        
        # Count-only answer
        answer_counts = sica.get("answer_counts", {})
        # Normalize keys
        norm_counts = {}
        for k, v in answer_counts.items():
            nk = normalize_answer(k)
            norm_counts[nk] = norm_counts.get(nk, 0) + v
        count_ans = count_only_answer(norm_counts)
        
        if gt is None or maxsat_ans is None:
            continue
        
        total += 1
        if maxsat_ans == gt:
            maxsat_correct += 1
        if count_ans == gt:
            count_correct += 1
        if maxsat_ans == count_ans:
            maxsat_count_agree += 1
        else:
            disagree_cases.append({
                "pid": item["problem"]["id"],
                "gt": gt,
                "maxsat": maxsat_ans,
                "count": count_ans,
                "scores": sica.get("scores"),
                "counts": answer_counts,
            })
    
    return {
        "dataset": dataset_name,
        "total": total,
        "maxsat_acc": maxsat_correct / total if total > 0 else 0,
        "count_acc": count_correct / total if total > 0 else 0,
        "agreement": maxsat_count_agree / total if total > 0 else 0,
        "maxsat_correct": maxsat_correct,
        "count_correct": count_correct,
        "disagree_cases": disagree_cases[:10],  # sample
    }

# ============ ANALYSIS 2: Random-weight MaxSAT using per_trace_constraints ============

def analyze_random_weight(constraints_dir, intermediates_dir):
    """
    For problems with raw per-trace constraints:
    - Original SICA: weight each constraint by trace count (dedup, then MaxSAT)
    - Random-weight: assign random weight to each constraint, sum per answer
    - Count-only: just count traces per answer
    """
    results = []
    
    constraint_files = sorted(glob.glob(os.path.join(constraints_dir, "*.json")))
    
    for cf in constraint_files:
        with open(cf) as fp:
            cdata = json.load(fp)
        
        pid = cdata.get("pid")
        if pid is None:
            continue
        gt = normalize_answer(cdata.get("gt"))
        per_trace = cdata.get("per_trace", [])
        
        if not per_trace or gt is None:
            continue
        
        # --- Count-only method ---
        vote_counts = Counter()
        for trace in per_trace:
            ans = normalize_answer(trace.get("answer"))
            if ans:
                vote_counts[ans] += 1
        count_ans = count_only_answer(dict(vote_counts))
        
        # --- Constraint-count method (total constraints per answer) ---
        constraint_counts = defaultdict(int)
        for trace in per_trace:
            ans = normalize_answer(trace.get("answer"))
            n_constraints = len(trace.get("constraints", []))
            if ans:
                constraint_counts[ans] += n_constraints
        cc_max = max(constraint_counts.values()) if constraint_counts else 0
        cc_tied = sorted([a for a, c in constraint_counts.items() if c == cc_max])
        constraint_count_ans = cc_tied[0] if cc_tied else None
        
        # --- Random-weight method ---
        # Assign random weight to each constraint, sum per answer
        random_scores = defaultdict(float)
        for trace in per_trace:
            ans = normalize_answer(trace.get("answer"))
            for _ in trace.get("constraints", []):
                random_scores[ans] += random.uniform(0, 1)
        rw_max = max(random_scores.values()) if random_scores else 0
        rw_tied = sorted([a for a, s in random_scores.items() if abs(s - rw_max) < 1e-9])
        random_ans = rw_tied[0] if rw_tied else None
        
        # --- Load original MaxSAT answer from intermediates ---
        inter_path = os.path.join(intermediates_dir, f"{pid}.json")
        maxsat_ans = None
        if os.path.exists(inter_path):
            with open(inter_path) as fp:
                idata = json.load(fp)
            maxsat_ans = normalize_answer(idata.get("sica_result", {}).get("answer"))
        
        results.append({
            "pid": pid,
            "gt": gt,
            "maxsat_ans": maxsat_ans,
            "count_ans": count_ans,
            "constraint_count_ans": constraint_count_ans,
            "random_ans": random_ans,
        })
    
    # Compute metrics
    total = len(results)
    if total == 0:
        return {"error": "No data"}
    
    maxsat_correct = sum(1 for r in results if r["maxsat_ans"] == r["gt"])
    count_correct = sum(1 for r in results if r["count_ans"] == r["gt"])
    cc_correct = sum(1 for r in results if r["constraint_count_ans"] == r["gt"])
    random_correct = sum(1 for r in results if r["random_ans"] == r["gt"])
    
    maxsat_count_agree = sum(1 for r in results if r["maxsat_ans"] == r["count_ans"])
    maxsat_random_agree = sum(1 for r in results if r["maxsat_ans"] == r["random_ans"])
    count_random_agree = sum(1 for r in results if r["count_ans"] == r["random_ans"])
    
    # Only count problems where maxsat_ans is available
    maxsat_available = sum(1 for r in results if r["maxsat_ans"] is not None)
    
    return {
        "total": total,
        "maxsat_available": maxsat_available,
        "maxsat_acc": maxsat_correct / maxsat_available if maxsat_available else None,
        "count_acc": count_correct / total,
        "constraint_count_acc": cc_correct / total,
        "random_weight_acc": random_correct / total,
        "maxsat_vs_count_agree": maxsat_count_agree / maxsat_available if maxsat_available else None,
        "maxsat_vs_random_agree": maxsat_random_agree / maxsat_available if maxsat_available else None,
        "count_vs_random_agree": count_random_agree / total,
    }

# ============ MAIN ============

if __name__ == "__main__":
    base = "/root/symb_invariant_consensus/results"
    
    print("=" * 70)
    print("CONSTRAINT ABLATION ANALYSIS")
    print("=" * 70)
    
    # --- Part 1: Qwen2.5-14B on FOLIO-204 ---
    print("\n[1] Qwen2.5-14B FOLIO-204 (exp036)")
    folio_res = analyze_intermediates(
        f"{base}/exp036_qwen25_14b_folio204/intermediates", "FOLIO-204"
    )
    print(f"    Total problems: {folio_res['total']}")
    print(f"    MaxSAT accuracy: {folio_res['maxsat_acc']:.4f} ({folio_res['maxsat_correct']}/{folio_res['total']})")
    print(f"    Count-only accuracy: {folio_res['count_acc']:.4f} ({folio_res['count_correct']}/{folio_res['total']})")
    print(f"    MaxSAT vs Count-only agreement: {folio_res['agreement']:.4f}")
    
    # --- Part 2: Qwen2.5-14B on PW-600 ---
    print("\n[2] Qwen2.5-14B ProofWriter-600 (exp032)")
    pw_res = analyze_intermediates(
        f"{base}/exp032_qwen25_14b_pw600/intermediates", "PW-600"
    )
    print(f"    Total problems: {pw_res['total']}")
    print(f"    MaxSAT accuracy: {pw_res['maxsat_acc']:.4f} ({pw_res['maxsat_correct']}/{pw_res['total']})")
    print(f"    Count-only accuracy: {pw_res['count_acc']:.4f} ({pw_res['count_correct']}/{pw_res['total']})")
    print(f"    MaxSAT vs Count-only agreement: {pw_res['agreement']:.4f}")
    
    # --- Part 3: Combined 14B ---
    total_14b = folio_res['total'] + pw_res['total']
    maxsat_14b = folio_res['maxsat_correct'] + pw_res['maxsat_correct']
    count_14b = folio_res['count_correct'] + pw_res['count_correct']
    print(f"\n[3] Combined 14B (FOLIO-204 + PW-600)")
    print(f"    Total: {total_14b}")
    print(f"    MaxSAT overall: {maxsat_14b/total_14b:.4f} ({maxsat_14b}/{total_14b})")
    print(f"    Count-only overall: {count_14b/total_14b:.4f} ({count_14b}/{total_14b})")
    
    # --- Part 4: Random-weight using 8B raw constraints (FOLIO) ---
    print("\n[4] Random-weight ablation (DeepSeek-R1-Distill-8B, FOLIO)")
    print("    (Using per_trace_constraints_v2 for raw constraint data)")
    rw_res = analyze_random_weight(
        f"{base}/exp_r1_distill_8b_sica/per_trace_constraints_v2",
        f"{base}/exp_r1_distill_8b_sica/intermediates",
    )
    if "error" in rw_res:
        print(f"    ERROR: {rw_res['error']}")
    else:
        print(f"    Total problems: {rw_res['total']}")
        print(f"    MaxSAT available: {rw_res['maxsat_available']}")
        print(f"    MaxSAT accuracy: {rw_res['maxsat_acc']:.4f}" if rw_res['maxsat_acc'] else "    MaxSAT accuracy: N/A")
        print(f"    Count-only (trace vote) accuracy: {rw_res['count_acc']:.4f}")
        print(f"    Constraint-count accuracy: {rw_res['constraint_count_acc']:.4f}")
        print(f"    Random-weight accuracy: {rw_res['random_weight_acc']:.4f}")
        print(f"    MaxSAT vs Count-only agreement: {rw_res['maxsat_vs_count_agree']:.4f}" if rw_res['maxsat_vs_count_agree'] else "")
        print(f"    MaxSAT vs Random-weight agreement: {rw_res['maxsat_vs_random_agree']:.4f}" if rw_res['maxsat_vs_random_agree'] else "")
        print(f"    Count vs Random-weight agreement: {rw_res['count_vs_random_agree']:.4f}")
    
    # --- Summary Table ---
    print("\n" + "=" * 70)
    print("SUMMARY TABLE")
    print("=" * 70)
    print(f"\n{'Method':<25} {'FOLIO-204 Acc':<15} {'PW-600 Acc':<15} {'Overall Acc':<15}")
    print("-" * 70)
    print(f"{'MaxSAT (SICA)':<25} {folio_res['maxsat_acc']:.4f}         {pw_res['maxsat_acc']:.4f}         {maxsat_14b/total_14b:.4f}")
    print(f"{'Count-only':<25} {folio_res['count_acc']:.4f}         {pw_res['count_acc']:.4f}         {count_14b/total_14b:.4f}")
    
    print(f"\nMaxSAT vs Count-only agreement:")
    print(f"  FOLIO-204: {folio_res['agreement']:.4f}")
    print(f"  PW-600:    {pw_res['agreement']:.4f}")
    
    if "error" not in rw_res:
        print(f"\n{'Method':<25} {'8B FOLIO Acc':<15}")
        print("-" * 40)
        if rw_res['maxsat_acc']:
            print(f"{'MaxSAT (SICA)':<25} {rw_res['maxsat_acc']:.4f}")
        print(f"{'Count-only (trace vote)':<25} {rw_res['count_acc']:.4f}")
        print(f"{'Constraint-count':<25} {rw_res['constraint_count_acc']:.4f}")
        print(f"{'Random-weight':<25} {rw_res['random_weight_acc']:.4f}")
        if rw_res['maxsat_vs_count_agree']:
            print(f"\n  MaxSAT vs Count-only agreement: {rw_res['maxsat_vs_count_agree']:.4f}")
        if rw_res['maxsat_vs_random_agree']:
            print(f"  MaxSAT vs Random-weight agreement: {rw_res['maxsat_vs_random_agree']:.4f}")
    
    # --- Disagreement analysis ---
    print("\n" + "=" * 70)
    print("DISAGREEMENT ANALYSIS (MaxSAT vs Count-only, sample)")
    print("=" * 70)
    for case in folio_res['disagree_cases'][:5]:
        print(f"\n  {case['pid']}: gt={case['gt']}, maxsat={case['maxsat']}, count={case['count']}")
        print(f"    scores: {case['scores']}")
        print(f"    counts: {case['counts']}")
    for case in pw_res['disagree_cases'][:5]:
        print(f"\n  {case['pid']}: gt={case['gt']}, maxsat={case['maxsat']}, count={case['count']}")
        print(f"    scores: {case['scores']}")
        print(f"    counts: {case['counts']}")
