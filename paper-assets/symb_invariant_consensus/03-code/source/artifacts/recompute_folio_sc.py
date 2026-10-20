import json
from math import comb

def mcnemar_exact_pvalue(b, c):
    n = b + c
    if n == 0:
        return 1.0
    k = min(b, c)
    p = sum(comb(n, i) * (0.5 ** n) for i in range(k + 1))
    return min(2.0 * p, 1.0)

def sc_answer_alphabetical(vote_dist):
    if not vote_dist:
        return None
    max_count = max(vote_dist.values())
    tied = [k for k, v in vote_dist.items() if v == max_count]
    return sorted(tied)[0]

with open("/root/symb_invariant_consensus/results/exp033_mistral_7b_folio204/exp033_results.json") as f:
    data = json.load(f)

results = data["results"]
print(f"Total results: {len(results)}")

corrected = []
for r in results:
    dist = r["sc_vote_distribution"]
    new_sc = sc_answer_alphabetical(dist)
    gold = r["ground_truth"]
    new_sc_correct = (new_sc == gold)
    old_sc = r["sc_answer"]
    old_sc_correct = r["sc_correct"]
    changed = (new_sc != old_sc)
    corrected.append({
        "problem_id": r["problem_id"],
        "ground_truth": gold,
        "old_sc_answer": old_sc,
        "new_sc_answer": new_sc,
        "sc_changed": changed,
        "old_sc_correct": old_sc_correct,
        "new_sc_correct": new_sc_correct,
        "sica_correct": r["sica_correct"],
        "sica_answer": r["sica_answer"],
        "constraint_count": r["constraints_stats"]["unique_after_dedup"],
        "vote_dist": dist,
    })

total = len(corrected)
new_sc_total = sum(1 for c in corrected if c["new_sc_correct"])
old_sc_total = sum(1 for c in corrected if c["old_sc_correct"])
sica_total = sum(1 for c in corrected if c["sica_correct"])
changed_count = sum(1 for c in corrected if c["sc_changed"])

print(f"Old SC correct: {old_sc_total}/{total} = {old_sc_total/total:.4f}")
print(f"New SC correct: {new_sc_total}/{total} = {new_sc_total/total:.4f}")
print(f"SICA correct:   {sica_total}/{total} = {sica_total/total:.4f}")
print(f"SC answers changed: {changed_count}")

# Show which ones changed
for c in corrected:
    if c["sc_changed"]:
        print(f"  {c['problem_id']}: {c['old_sc_answer']} -> {c['new_sc_answer']} (gold={c['ground_truth']}, dist={c['vote_dist']})")

# --- BY ANSWER TYPE ---
print("\n=== BY ANSWER TYPE (FOLIO-204) ===")
answer_type_results = []
for label in ["True", "False", "Unknown"]:
    subset = [c for c in corrected if c["ground_truth"] == label]
    n = len(subset)
    sc_corr = sum(1 for c in subset if c["new_sc_correct"])
    sica_corr = sum(1 for c in subset if c["sica_correct"])
    b = sum(1 for c in subset if c["sica_correct"] and not c["new_sc_correct"])
    c_val = sum(1 for c in subset if not c["sica_correct"] and c["new_sc_correct"])
    p = mcnemar_exact_pvalue(b, c_val)
    row = {
        "group": f"FOLIO-204/{label}",
        "n": n,
        "sc_correct": sc_corr,
        "sc_accuracy": round(sc_corr / n, 4),
        "sica_correct": sica_corr,
        "sica_accuracy": round(sica_corr / n, 4),
        "delta_pp": round((sica_corr - sc_corr) / n, 4),
        "mcnemar_b_sica_plus_sc_minus": b,
        "mcnemar_c_sica_minus_sc_plus": c_val,
        "mcnemar_exact_p": round(p, 6),
    }
    answer_type_results.append(row)
    print(f"  {label}: n={n}, SC={sc_corr}/{n}={sc_corr/n:.4f}, SICA={sica_corr}/{n}={sica_corr/n:.4f}, Δ={row['delta_pp']}, b={b}, c={c_val}, p={p:.6f}")

# Overall
b_all = sum(1 for c in corrected if c["sica_correct"] and not c["new_sc_correct"])
c_all = sum(1 for c in corrected if not c["sica_correct"] and c["new_sc_correct"])
p_all = mcnemar_exact_pvalue(b_all, c_all)
overall_row = {
    "group": "FOLIO-204/Overall",
    "n": total,
    "sc_correct": new_sc_total,
    "sc_accuracy": round(new_sc_total / total, 4),
    "sica_correct": sica_total,
    "sica_accuracy": round(sica_total / total, 4),
    "delta_pp": round((sica_total - new_sc_total) / total, 4),
    "mcnemar_b_sica_plus_sc_minus": b_all,
    "mcnemar_c_sica_minus_sc_plus": c_all,
    "mcnemar_exact_p": round(p_all, 6),
}
answer_type_results.append(overall_row)
print(f"  Overall: n={total}, SC={new_sc_total}/{total}={new_sc_total/total:.4f}, SICA={sica_total}/{total}={sica_total/total:.4f}, Δ={overall_row['delta_pp']}, b={b_all}, c={c_all}, p={p_all:.6f}")

# --- BY CONSTRAINT COUNT ---
print("\n=== BY CONSTRAINT COUNT (FOLIO-204) ===")
thresholds = [32, 47]
constraint_results = []

def get_tertile(count):
    if count <= thresholds[0]:
        return "Low"
    elif count <= thresholds[1]:
        return "Mid"
    else:
        return "High"

for tertile_name in ["Low", "Mid", "High"]:
    subset = [c for c in corrected if get_tertile(c["constraint_count"]) == tertile_name]
    n = len(subset)
    if n == 0:
        continue
    sc_corr = sum(1 for c in subset if c["new_sc_correct"])
    sica_corr = sum(1 for c in subset if c["sica_correct"])
    b = sum(1 for c in subset if c["sica_correct"] and not c["new_sc_correct"])
    c_val = sum(1 for c in subset if not c["sica_correct"] and c["new_sc_correct"])
    p = mcnemar_exact_pvalue(b, c_val)
    counts = [c["constraint_count"] for c in subset]
    mean_c = round(sum(counts) / len(counts), 1)
    min_c, max_c = min(counts), max(counts)
    row = {
        "group": f"FOLIO-204/constr_{tertile_name}",
        "n": n,
        "sc_correct": sc_corr,
        "sc_accuracy": round(sc_corr / n, 4),
        "sica_correct": sica_corr,
        "sica_accuracy": round(sica_corr / n, 4),
        "delta_pp": round((sica_corr - sc_corr) / n, 4),
        "mcnemar_b_sica_plus_sc_minus": b,
        "mcnemar_c_sica_minus_sc_plus": c_val,
        "mcnemar_exact_p": round(p, 6),
        "constraint_range": f"[{min_c}, {max_c}]",
        "mean_constraints": mean_c,
        "tertile_thresholds": thresholds,
    }
    constraint_results.append(row)
    print(f"  {tertile_name} [{min_c}-{max_c}]: n={n}, SC={sc_corr}/{n}={sc_corr/n:.4f}, SICA={sica_corr}/{n}={sica_corr/n:.4f}, Δ={row['delta_pp']}, b={b}, c={c_val}, p={p:.6f}")

# Output JSON
output = {
    "folio204_answer_type": answer_type_results,
    "folio204_constraint_count": constraint_results,
    "verification": {
        "old_sc_correct": old_sc_total,
        "new_sc_correct": new_sc_total,
        "sica_correct": sica_total,
        "total": total,
        "changed_answers": changed_count,
    }
}
print("\n=== JSON OUTPUT ===")
print(json.dumps(output, indent=2))
