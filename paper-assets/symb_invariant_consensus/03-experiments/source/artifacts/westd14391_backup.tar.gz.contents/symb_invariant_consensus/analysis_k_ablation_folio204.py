"""
K Ablation on FOLIO 204 (exp-026 data).
Computes SC at different K values using the project's actual SC implementation.
Reports SICA@K=12 from stored results.
"""
import json
import os
import sys
import random
from collections import Counter

sys.path.insert(0, "/root/symb_invariant_consensus")
from sica.pipeline import _group_logic_answers

random.seed(42)

INTERMEDIATES_DIR = "/root/symb_invariant_consensus/results/folio_204_14b/intermediates"
RESULTS_FILE = "/root/symb_invariant_consensus/results/folio_204_14b/folio_204_results.json"
OUTPUT_DIR = "/root/autodl-tmp/sica_project/results/k_ablation_folio204"
os.makedirs(OUTPUT_DIR, exist_ok=True)

K_VALUES = [3, 4, 6, 8, 11, 12]

def normalize(ans):
    ans = str(ans).strip().lower()
    if ans in ("true", "yes", "t"): return "True"
    elif ans in ("false", "no", "f"): return "False"
    elif ans in ("unknown", "uncertain", "u", "undetermined"): return "Unknown"
    return ans.capitalize()

def sc_vote(answers):
    """Majority vote using project's _group_logic_answers (matches stored SC)."""
    valid = [a.strip() for a in answers if a.strip()]
    if not valid:
        return "", {}
    groups = _group_logic_answers(valid)
    best = max(groups, key=lambda k: len(groups[k]))
    vote_dist = {k: len(v) for k, v in groups.items()}
    return best, vote_dist

def load_problems():
    with open(RESULTS_FILE) as f:
        data = json.load(f)
    problems = []
    for r in data["results"]:
        pid = r["problem_id"]
        with open(os.path.join(INTERMEDIATES_DIR, f"{pid}.json")) as f:
            intermed = json.load(f)
        traces = intermed["sica_result"]["traces"]
        problems.append({
            "pid": pid,
            "gt": normalize(r["ground_truth"]),
            "traces": traces,
            "sica_answer": normalize(r["sica_answer"]),
            "sica_correct": r["sica_correct"],
            "sica_scores": r["sica_scores"],
            "stored_sc_answer": normalize(r["sc_answer"]),
            "stored_sc_correct": r["sc_correct"],
        })
    return problems

def compute_sc_at_k(problems, k):
    correct = 0
    per_problem = []
    for p in problems:
        traces_k = p["traces"][:k]
        answers = [normalize(t["answer"]) for t in traces_k if t.get("answer")]
        sc_ans, vote_dist = sc_vote(answers)
        sc_correct = (sc_ans == p["gt"])
        if sc_correct:
            correct += 1
        per_problem.append({"pid": p["pid"], "sc_answer": sc_ans, "sc_correct": sc_correct, "votes": vote_dist})
    return correct, per_problem

def main():
    problems = load_problems()
    n = len(problems)
    print(f"FOLIO 204 K Ablation ({n} problems)\n")

    # Verify K=12 SC matches stored
    k12_correct, k12_pp = compute_sc_at_k(problems, 12)
    stored_sc_correct = sum(1 for p in problems if p["stored_sc_correct"])
    print(f"SC@K=12 verification: computed={k12_correct}/{n}, stored={stored_sc_correct}/{n}")
    
    sica_correct = sum(1 for p in problems if p["sica_correct"])
    sica_acc = sica_correct / n

    # Main K ablation table
    print(f"\n{'='*72}")
    print(f"{'K':>4} | {'SC Acc':>10} | {'SC Corr':>8} | {'SICA Acc':>10} | {'SICA Corr':>9} | {'Δ(pp)':>8}")
    print(f"{'-'*72}")
    
    k_results = {}
    for k in K_VALUES:
        sc_corr, pp = compute_sc_at_k(problems, k)
        sc_acc = sc_corr / n
        if k == 12:
            delta_pp = (sica_acc - sc_acc) * 100
            sica_str = f"{sica_acc:.4f}"
            sica_corr_str = str(sica_correct)
            delta_str = f"{delta_pp:+.2f}"
        else:
            sica_str = "-"
            sica_corr_str = "-"
            delta_str = "-"
        print(f"{k:>4} | {sc_acc:.4f}     | {sc_corr:>8} | {sica_str:>10} | {sica_corr_str:>9} | {delta_str:>8}")
        k_results[k] = {"sc_accuracy": sc_acc, "sc_correct": sc_corr, "per_problem": pp}
    print(f"{'='*72}")
    
    # SICA vs SC agreement at K=12
    agree = sum(1 for p in problems if p["sica_answer"] == p["stored_sc_answer"])
    sica_win = sum(1 for p in problems if p["sica_correct"] and not p["stored_sc_correct"])
    sc_win = sum(1 for p in problems if not p["sica_correct"] and p["stored_sc_correct"])
    both_ok = sum(1 for p in problems if p["sica_correct"] and p["stored_sc_correct"])
    both_bad = sum(1 for p in problems if not p["sica_correct"] and not p["stored_sc_correct"])
    
    print(f"\nSICA vs SC @K=12:")
    print(f"  Agreement: {agree}/{n} ({agree/n*100:.1f}%)")
    print(f"  Both correct: {both_ok}  |  SICA wins: {sica_win}  |  SC wins: {sc_win}  |  Both wrong: {both_bad}")
    
    # SC stability: answer flips vs K=12
    print(f"\nSC stability (answer changes vs K=12):")
    k12_map = {r["pid"]: r["sc_answer"] for r in k_results[12]["per_problem"]}
    for k in K_VALUES:
        if k == 12: continue
        k_map = {r["pid"]: r["sc_answer"] for r in k_results[k]["per_problem"]}
        flips = sum(1 for pid in k12_map if k_map[pid] != k12_map[pid])
        print(f"  K={k:2d} vs K=12: {flips:3d} flips ({flips/n*100:.1f}%)")
    
    # Random subsample variance
    print(f"\nSC variance (20 random subsamples):")
    for k in [4, 6, 8]:
        accs = []
        for _ in range(20):
            corr = 0
            for p in problems:
                idx = random.sample(range(len(p["traces"])), min(k, len(p["traces"])))
                answers = [normalize(p["traces"][i]["answer"]) for i in idx if p["traces"][i].get("answer")]
                ans, _ = sc_vote(answers)
                if ans == p["gt"]:
                    corr += 1
            accs.append(corr / n)
        mu = sum(accs)/len(accs)
        sigma = (sum((a-mu)**2 for a in accs)/len(accs))**0.5
        print(f"  K={k:2d}: mean={mu:.4f} ± {sigma:.4f}  range=[{min(accs):.4f}, {max(accs):.4f}]")
    
    # Save results
    output = {
        "experiment": "exp-036-k-ablation-folio204",
        "dataset": "FOLIO-204",
        "source_experiment": "exp-026",
        "model": "Qwen2.5-14B-Instruct",
        "n_problems": n,
        "sica_accuracy_k12": round(sica_acc, 4),
        "sica_correct_k12": sica_correct,
        "k_ablation": {str(k): {"sc_accuracy": round(r["sc_accuracy"], 4), "sc_correct": r["sc_correct"]} for k, r in k_results.items()},
        "agreement_k12": {
            "same_answer": agree,
            "both_correct": both_ok,
            "sica_only_correct": sica_win,
            "sc_only_correct": sc_win,
            "both_wrong": both_bad,
        },
        "note": "SICA at K<12 requires LLM-based constraint re-extraction (not available CPU-only). SC computed using first-K traces with project SC implementation.",
    }
    out_path = os.path.join(OUTPUT_DIR, "k_ablation_results.json")
    with open(out_path, "w") as f:
        json.dump(output, f, indent=2)
    print(f"\nSaved to {out_path}")

if __name__ == "__main__":
    main()
