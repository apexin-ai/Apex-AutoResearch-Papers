"""Compare exp4 T=1 vs exp-026 SICA predictions per-problem."""
import json
import sys
from pathlib import Path
from collections import Counter

sys.path.insert(0, "/root/symb_invariant_consensus")
from sica.z3_maxsat import ConstraintDeduplicator, MaxSATSolver
from sica.scorer import InvariantScorer

DATA_DIR = Path("/root/symb_invariant_consensus/results/folio_204_14b")
PER_TRACE_DIR = DATA_DIR / "per_trace_constraints"
INTERMEDIATES_DIR = DATA_DIR / "intermediates"
RESULTS_FILE = DATA_DIR / "folio_204_results.json"

def normalize_logic_answer(ans):
    a = ans.strip().lower()
    if a in ("true", "yes"): return "True"
    if a in ("false", "no"): return "False"
    if a in ("unknown", "uncertain", "undetermined"): return "Unknown"
    return a.capitalize()

# Load exp-026 per-problem results
with open(RESULTS_FILE) as f:
    exp026_data = json.load(f)

exp026_map = {}
for r in exp026_data["results"]:
    exp026_map[r["problem_id"]] = r

pids = sorted(exp026_map.keys(), key=lambda x: int(x.split("_")[1]))

# Re-run exp4 T=1 logic per problem and compare
diffs = []
exp4_correct = 0
exp026_correct = 0

for pid in pids:
    r026 = exp026_map[pid]
    gt = r026["ground_truth"]

    # exp-026 result
    e026_answer = r026["sica_answer"]
    e026_correct = r026["sica_correct"]

    # exp4 T=1: re-run from per_trace_constraints
    ptc_file = PER_TRACE_DIR / f"{pid}.json"
    if not ptc_file.exists():
        print(f"MISSING: {pid}")
        continue

    with open(ptc_file) as f:
        ptc = json.load(f)

    traces_raw = ptc["per_trace"]
    all_constraints = []
    traces_info = []
    for t in traces_raw:
        all_constraints.append(t.get("constraints", []))
        ans = normalize_logic_answer(t.get("answer") or t.get("extracted_answer") or "")
        traces_info.append({"answer": ans, "trace_idx": t["trace_idx"]})

    counts = Counter(t["answer"] for t in traces_info if t["answer"])
    candidates = list(set(t["answer"] for t in traces_info if t["answer"]))
    answer_counts = dict(counts)

    deduplicator = ConstraintDeduplicator()
    unique_constraints = deduplicator.deduplicate(all_constraints)

    solver = MaxSATSolver()
    maxsat_result = solver.solve(unique_constraints, timeout_ms=10000)

    scorer = InvariantScorer()
    scores = scorer.score(maxsat_result, traces_info, candidates)
    exp4_answer = scorer.select_answer(scores, answer_counts)

    exp4_is_correct = normalize_logic_answer(exp4_answer) == normalize_logic_answer(gt)
    exp4_correct += int(exp4_is_correct)
    exp026_correct += int(e026_correct)

    if exp4_answer != e026_answer:
        # Also get exp-026 constraint details from intermediates
        inter_file = INTERMEDIATES_DIR / f"{pid}.json"
        inter_data = json.load(open(inter_file))
        e026_stats = inter_data["sica_result"]["constraints_stats"]
        e026_scores = inter_data["sica_result"]["scores"]

        diffs.append({
            "pid": pid,
            "gt": gt,
            "exp4_answer": exp4_answer,
            "exp4_correct": exp4_is_correct,
            "exp4_scores": scores,
            "exp4_unique": len(unique_constraints),
            "exp4_satisfied": len(maxsat_result.satisfied),
            "exp4_excluded": len(maxsat_result.excluded),
            "exp4_ptc_total": sum(len(t.get("constraints",[])) for t in traces_raw),
            "exp026_answer": e026_answer,
            "exp026_correct": e026_correct,
            "exp026_scores": e026_scores,
            "exp026_unique": e026_stats["unique_after_dedup"],
            "exp026_total_extracted": e026_stats["total_extracted"],
            "exp026_maxsat_sat": r026["maxsat_stats"]["satisfied"],
            "exp026_maxsat_excl": r026["maxsat_stats"]["excluded"],
            "vote_distribution": r026["sc_vote_distribution"],
        })

print(f"\n=== SUMMARY ===")
print(f"exp4  T=1 correct: {exp4_correct}/204 = {exp4_correct/204:.4f}")
print(f"exp-026   correct: {exp026_correct}/204 = {exp026_correct/204:.4f}")
print(f"Differences: {len(diffs)} problems")

print(f"\n=== DIFF DETAILS ===")
for d in diffs:
    print(f"\n--- {d['pid']} (GT={d['gt']}) ---")
    print(f"  exp4:   {d['exp4_answer']} ({'CORRECT' if d['exp4_correct'] else 'WRONG'})  scores={d['exp4_scores']}")
    print(f"  exp026: {d['exp026_answer']} ({'CORRECT' if d['exp026_correct'] else 'WRONG'})  scores={d['exp026_scores']}")
    print(f"  exp4  constraints: ptc_total={d['exp4_ptc_total']} unique={d['exp4_unique']} sat={d['exp4_satisfied']} excl={d['exp4_excluded']}")
    print(f"  exp026 constraints: total={d['exp026_total_extracted']} unique={d['exp026_unique']} sat={d['exp026_maxsat_sat']} excl={d['exp026_maxsat_excl']}")
    print(f"  SC votes: {d['vote_distribution']}")
    # Determine which is better
    e4_c = d['exp4_correct']
    e026_c = d['exp026_correct']
    if e4_c and not e026_c: verdict = "exp4 WINS"
    elif e026_c and not e4_c: verdict = "exp026 WINS"
    elif e4_c and e026_c: verdict = "BOTH CORRECT (different answer)"
    else: verdict = "BOTH WRONG"
    print(f"  Verdict: {verdict}")

# Count wins
exp4_wins = sum(1 for d in diffs if d['exp4_correct'] and not d['exp026_correct'])
exp026_wins = sum(1 for d in diffs if d['exp026_correct'] and not d['exp4_correct'])
both_wrong = sum(1 for d in diffs if not d['exp4_correct'] and not d['exp026_correct'])
both_correct = sum(1 for d in diffs if d['exp4_correct'] and d['exp026_correct'])
print(f"\n=== WIN/LOSS ===")
print(f"exp4 wins: {exp4_wins}")
print(f"exp026 wins: {exp026_wins}")
print(f"Both correct (diff answer): {both_correct}")
print(f"Both wrong: {both_wrong}")
