import json
import math
import os

RESULTS_PATH = "/root/symb_invariant_consensus/results/exp033_mistral_7b_folio204/exp033_results.json"
OUTPUT_PATH = "/root/symb_invariant_consensus/results/exp033_per_problem_analysis.json"

with open(RESULTS_PATH) as f:
    data = json.load(f)

k = data["summary"]["k"]
results = data["results"]

def compute_entropy(vote_dist, k):
    total = sum(vote_dist.values())
    if total == 0:
        return 0.0
    probs = [c / total for c in vote_dist.values() if c > 0]
    return -sum(p * math.log2(p) for p in probs)

per_problem = []
for r in results:
    vote_dist = r["sc_vote_distribution"]
    total_votes = sum(vote_dist.values())
    entropy = compute_entropy(vote_dist, k)
    
    cs = r["constraints_stats"]
    extraction_rate = cs["traces_with_constraints"] / k if k > 0 else 0.0
    
    is_override = r["sica_answer"] != r["sc_answer"]
    override_correct = None
    if is_override:
        override_correct = r["sica_correct"]
    
    entry = {
        "problem_id": r["problem_id"],
        "gold_answer": r["ground_truth"],
        "sc_answer": r["sc_answer"],
        "sica_answer": r["sica_answer"],
        "sc_vote_distribution": vote_dist,
        "sc_vote_entropy": round(entropy, 4),
        "sc_majority_votes": r["sc_vote_count"],
        "sc_total_votes": total_votes,
        "sica_scores": r["sica_scores"],
        "unique_constraints": cs["unique_after_dedup"],
        "total_constraints": cs["total_extracted"],
        "constraint_extraction_rate": round(extraction_rate, 4),
        "sc_correct": r["sc_correct"],
        "sica_correct": r["sica_correct"],
        "is_override": is_override,
        "override_correct": override_correct,
    }
    per_problem.append(entry)

# --- Aggregate stats ---
n = len(per_problem)
overrides = [p for p in per_problem if p["is_override"]]
n_override = len(overrides)
override_correct_count = sum(1 for p in overrides if p["override_correct"])
override_wrong_count = sum(1 for p in overrides if not p["override_correct"])
# Override precision: when SICA overrides SC, how often is SICA right?
override_precision = override_correct_count / n_override if n_override > 0 else 0.0
# SC was correct but SICA overrode (damage)
override_damage = sum(1 for p in overrides if not p["sica_correct"] and p["problem_id"] in 
                      {pp["problem_id"] for pp in per_problem if pp["sc_correct"] and pp["is_override"]})

entropies = sorted([p["sc_vote_entropy"] for p in per_problem])
q25 = entropies[n // 4]
q50 = entropies[n // 2]
q75 = entropies[3 * n // 4]

# Entropy bins: low [0, 0.5), medium [0.5, 1.2), high [1.2, inf)
bins = {"low (H<0.5)": [], "medium (0.5<=H<1.2)": [], "high (H>=1.2)": []}
for p in per_problem:
    h = p["sc_vote_entropy"]
    if h < 0.5:
        bins["low (H<0.5)"].append(p)
    elif h < 1.2:
        bins["medium (0.5<=H<1.2)"].append(p)
    else:
        bins["high (H>=1.2)"].append(p)

bin_stats = {}
for bname, bprobs in bins.items():
    bn = len(bprobs)
    if bn == 0:
        bin_stats[bname] = {"n": 0, "sc_acc": 0, "sica_acc": 0, "overrides": 0, "override_precision": 0}
        continue
    sc_c = sum(1 for p in bprobs if p["sc_correct"])
    sica_c = sum(1 for p in bprobs if p["sica_correct"])
    ov = [p for p in bprobs if p["is_override"]]
    ov_c = sum(1 for p in ov if p["override_correct"])
    bin_stats[bname] = {
        "n": bn,
        "sc_acc": round(sc_c / bn, 4),
        "sica_acc": round(sica_c / bn, 4),
        "overrides": len(ov),
        "override_correct": ov_c,
        "override_precision": round(ov_c / len(ov), 4) if len(ov) > 0 else None,
    }

output = {
    "metadata": {
        "experiment": "exp-033",
        "model": "Mistral-7B",
        "dataset": "FOLIO-204",
        "k": k,
        "n_problems": n,
    },
    "aggregate": {
        "sc_accuracy": round(sum(1 for p in per_problem if p["sc_correct"]) / n, 4),
        "sica_accuracy": round(sum(1 for p in per_problem if p["sica_correct"]) / n, 4),
        "n_overrides": n_override,
        "override_precision": round(override_precision, 4),
        "override_correct": override_correct_count,
        "override_wrong": override_wrong_count,
        "entropy_quartiles": {"q25": round(q25, 4), "q50": round(q50, 4), "q75": round(q75, 4)},
        "entropy_min": round(entropies[0], 4),
        "entropy_max": round(entropies[-1], 4),
        "by_entropy_bin": bin_stats,
    },
    "per_problem": per_problem,
}

with open(OUTPUT_PATH, "w") as f:
    json.dump(output, f, indent=2)

print(f"Written {n} problems to {OUTPUT_PATH}")
print(f"\n=== Aggregate Stats ===")
print(f"SC accuracy:   {output['aggregate']['sc_accuracy']}")
print(f"SICA accuracy: {output['aggregate']['sica_accuracy']}")
print(f"Overrides:     {n_override} / {n} ({round(100*n_override/n,1)}%)")
print(f"Override precision: {override_correct_count}/{n_override} = {round(override_precision, 4)}")
print(f"Override correct: {override_correct_count}, wrong: {override_wrong_count}")
print(f"\nEntropy quartiles: Q25={q25:.4f}, Q50={q50:.4f}, Q75={q75:.4f}")
print(f"Entropy range: [{entropies[0]:.4f}, {entropies[-1]:.4f}]")
print(f"\n=== By Entropy Bin ===")
for bname, bs in bin_stats.items():
    print(f"  {bname}: n={bs['n']}, SC={bs['sc_acc']}, SICA={bs['sica_acc']}, overrides={bs['overrides']}, override_prec={bs.get('override_precision', 'N/A')}")
