#!/usr/bin/env python3
"""Discordant pair failure mode analysis for Debate and Contrastive methods."""
import json, re, sys
from collections import Counter

def load(path):
    with open(path) as f:
        return json.load(f)

debate_data = load("results/exp076_debate_mistral_folio/results.json")
contrastive_data = load("results/exp075b_contrastive_mistral_folio/results.json")
folio_raw = load("data/folio_full.json")

debate_results = debate_data["results"]
contrastive_results = contrastive_data["results"]

folio_by_id = {item["id"]: item for item in folio_raw}

def premise_count(problem_id):
    if problem_id in folio_by_id:
        return len(folio_by_id[problem_id].get("premises_fol", []))
    return 0

def premise_bucket(n):
    if n <= 1: return "1"
    if n == 2: return "2"
    if n <= 4: return "3-4"
    if n <= 6: return "5-6"
    return "7+"

def text_features(problem_text):
    t = problem_text.lower()
    has_negation = bool(re.search(r"\b(not|never|no|neither|nor|cannot)\b", t))
    has_conditional = bool(re.search(r"\b(if|then|unless|provided that|given that|assuming)\b", t))
    has_quantifier = bool(re.search(r"\b(all|every|each|some|any|no one|nobody|none|most|few)\b", t))
    return has_negation, has_conditional, has_quantifier

# Identify discordant pairs
debate_disc_ids = set()
debate_disc = []
for r in debate_results:
    if r["sc_correct"] and not r["debate_correct"]:
        debate_disc.append(r)
        debate_disc_ids.add(r["problem_id"])

contrastive_disc_ids = set()
contrastive_disc = []
for r in contrastive_results:
    if r["sc_correct"] and not r["contrastive_correct"]:
        contrastive_disc.append(r)
        contrastive_disc_ids.add(r["problem_id"])

print(f"Debate discordant (SC correct, Debate wrong): {len(debate_disc)}")
print(f"Contrastive discordant (SC correct, Contrastive wrong): {len(contrastive_disc)}")

# Full dataset baseline
all_ids = [r["problem_id"] for r in debate_results]
full_premise_dist = Counter(premise_bucket(premise_count(pid)) for pid in all_ids)
full_answer_dist = Counter(r["ground_truth"] for r in debate_results)
full_n = len(debate_results)

# 1. Debate discordant analysis
deb_premise_dist = Counter(premise_bucket(premise_count(r["problem_id"])) for r in debate_disc)
deb_answer_dist = Counter(r["ground_truth"] for r in debate_disc)
deb_fallback_count = sum(1 for r in debate_disc if r.get("used_fallback", False))
deb_constraints = [r.get("constraints_from_debate", 0) for r in debate_disc]
deb_valid_debates = [r.get("n_valid_debates", 0) for r in debate_disc]

deb_neg, deb_cond, deb_quant = 0, 0, 0
for r in debate_disc:
    n, c, q = text_features(r["problem"])
    deb_neg += n; deb_cond += c; deb_quant += q

full_neg, full_cond, full_quant = 0, 0, 0
for r in debate_results:
    n, c, q = text_features(r["problem"])
    full_neg += n; full_cond += c; full_quant += q

full_constraints = [r.get("constraints_from_debate", 0) for r in debate_results]
full_fallback = sum(1 for r in debate_results if r.get("used_fallback", False))
full_valid_debates = [r.get("n_valid_debates", 0) for r in debate_results]

# 2. Contrastive discordant analysis
con_premise_dist = Counter(premise_bucket(premise_count(r["problem_id"])) for r in contrastive_disc)
con_answer_dist = Counter(r["ground_truth"] for r in contrastive_disc)
con_degenerate_count = sum(1 for r in contrastive_disc if r.get("degenerate", False))

con_disc_imbalance = [r.get("pro_constraints_count", 0) - r.get("con_constraints_count", 0) for r in contrastive_disc]
full_con_imbalance = [r.get("pro_constraints_count", 0) - r.get("con_constraints_count", 0) for r in contrastive_results]
full_degenerate = sum(1 for r in contrastive_results if r.get("degenerate", False))

con_disc_pro = [r.get("pro_constraints_count", 0) for r in contrastive_disc]
con_disc_con = [r.get("con_constraints_count", 0) for r in contrastive_disc]
full_pro = [r.get("pro_constraints_count", 0) for r in contrastive_results]
full_con_c = [r.get("con_constraints_count", 0) for r in contrastive_results]

con_neg, con_cond, con_quant = 0, 0, 0
for r in contrastive_disc:
    n, c, q = text_features(r["problem"])
    con_neg += n; con_cond += c; con_quant += q

# 3. Overlap analysis
both_ids = debate_disc_ids & contrastive_disc_ids
debate_only_ids = debate_disc_ids - contrastive_disc_ids
contrastive_only_ids = contrastive_disc_ids - debate_disc_ids
union = debate_disc_ids | contrastive_disc_ids
jaccard = len(both_ids) / len(union) if union else 0

def group_stats(ids, results_list):
    subset = [r for r in results_list if r["problem_id"] in ids]
    if not subset:
        return {"n": 0}
    ans = Counter(r["ground_truth"] for r in subset)
    prem = Counter(premise_bucket(premise_count(r["problem_id"])) for r in subset)
    neg_r, cond_r, quant_r = 0, 0, 0
    for r in subset:
        n, c, q = text_features(r["problem"])
        neg_r += n; cond_r += c; quant_r += q
    return {
        "n": len(subset),
        "answer_dist": dict(ans),
        "premise_dist": dict(prem),
        "negation_rate": round(neg_r / len(subset), 3),
        "conditional_rate": round(cond_r / len(subset), 3),
        "quantifier_rate": round(quant_r / len(subset), 3)
    }

both_stats = group_stats(both_ids, debate_results)
debate_only_stats = group_stats(debate_only_ids, debate_results)
contrastive_only_stats = group_stats(contrastive_only_ids, contrastive_results)

mean = lambda x: sum(x)/len(x) if x else 0

output = {
    "debate_discordant": {
        "n": len(debate_disc),
        "premise_distribution": dict(deb_premise_dist),
        "answer_distribution": dict(deb_answer_dist),
        "fallback_rate": round(deb_fallback_count / len(debate_disc), 4) if debate_disc else 0,
        "mean_constraints_from_debate": round(mean(deb_constraints), 2),
        "mean_valid_debates": round(mean(deb_valid_debates), 2),
        "negation_rate": round(deb_neg / len(debate_disc), 3) if debate_disc else 0,
        "conditional_rate": round(deb_cond / len(debate_disc), 3) if debate_disc else 0,
        "quantifier_rate": round(deb_quant / len(debate_disc), 3) if debate_disc else 0,
        "discordant_ids": sorted(list(debate_disc_ids))
    },
    "contrastive_discordant": {
        "n": len(contrastive_disc),
        "premise_distribution": dict(con_premise_dist),
        "answer_distribution": dict(con_answer_dist),
        "degenerate_rate": round(con_degenerate_count / len(contrastive_disc), 4) if contrastive_disc else 0,
        "degenerate_count": con_degenerate_count,
        "mean_pro_con_imbalance": round(mean(con_disc_imbalance), 2),
        "mean_pro_constraints": round(mean(con_disc_pro), 2),
        "mean_con_constraints": round(mean(con_disc_con), 2),
        "negation_rate": round(con_neg / len(contrastive_disc), 3) if contrastive_disc else 0,
        "conditional_rate": round(con_cond / len(contrastive_disc), 3) if contrastive_disc else 0,
        "quantifier_rate": round(con_quant / len(contrastive_disc), 3) if contrastive_disc else 0,
        "discordant_ids": sorted(list(contrastive_disc_ids))
    },
    "overlap_analysis": {
        "debate_only": len(debate_only_ids),
        "contrastive_only": len(contrastive_only_ids),
        "both": len(both_ids),
        "jaccard": round(jaccard, 4),
        "both_ids": sorted(list(both_ids)),
        "debate_only_stats": debate_only_stats,
        "contrastive_only_stats": contrastive_only_stats,
        "both_stats": both_stats
    },
    "full_dataset_baseline": {
        "n": full_n,
        "premise_distribution": dict(full_premise_dist),
        "answer_distribution": dict(full_answer_dist),
        "mean_constraints_from_debate": round(mean(full_constraints), 2),
        "fallback_rate": round(full_fallback / full_n, 4),
        "mean_valid_debates": round(mean(full_valid_debates), 2),
        "degenerate_rate": round(full_degenerate / full_n, 4),
        "mean_pro_con_imbalance": round(mean(full_con_imbalance), 2),
        "mean_pro_constraints": round(mean(full_pro), 2),
        "mean_con_constraints": round(mean(full_con_c), 2),
        "negation_rate": round(full_neg / full_n, 3),
        "conditional_rate": round(full_cond / full_n, 3),
        "quantifier_rate": round(full_quant / full_n, 3)
    }
}

with open("/tmp/error_categorization_discordant.json", "w") as f:
    json.dump(output, f, indent=2)

print(f"\n=== DEBATE DISCORDANT ({len(debate_disc)} items) ===")
print(f"Premise dist: {dict(deb_premise_dist)}")
print(f"  Baseline:   {dict(full_premise_dist)}")
print(f"Answer dist:  {dict(deb_answer_dist)}")
print(f"  Baseline:   {dict(full_answer_dist)}")
print(f"Fallback rate: {deb_fallback_count}/{len(debate_disc)} = {deb_fallback_count/len(debate_disc):.3f} (baseline: {full_fallback}/{full_n} = {full_fallback/full_n:.3f})")
print(f"Mean constraints: {mean(deb_constraints):.1f} (baseline: {mean(full_constraints):.1f})")
print(f"Mean valid debates: {mean(deb_valid_debates):.2f} (baseline: {mean(full_valid_debates):.2f})")
print(f"Negation: {deb_neg/len(debate_disc):.3f}, Conditional: {deb_cond/len(debate_disc):.3f}, Quantifier: {deb_quant/len(debate_disc):.3f}")
print(f"  Baseline: Neg={full_neg/full_n:.3f}, Cond={full_cond/full_n:.3f}, Quant={full_quant/full_n:.3f}")

print(f"\n=== CONTRASTIVE DISCORDANT ({len(contrastive_disc)} items) ===")
print(f"Premise dist: {dict(con_premise_dist)}")
print(f"Answer dist:  {dict(con_answer_dist)}")
print(f"Degenerate: {con_degenerate_count}/{len(contrastive_disc)} = {con_degenerate_count/len(contrastive_disc):.3f} (baseline: {full_degenerate}/{full_n} = {full_degenerate/full_n:.3f})")
print(f"Mean pro-con imbalance: {mean(con_disc_imbalance):.2f} (baseline: {mean(full_con_imbalance):.2f})")
print(f"Mean pro: {mean(con_disc_pro):.2f}, Mean con: {mean(con_disc_con):.2f}")
print(f"  Baseline pro: {mean(full_pro):.2f}, Baseline con: {mean(full_con_c):.2f}")

print(f"\n=== OVERLAP ===")
print(f"Debate-only: {len(debate_only_ids)}, Contrastive-only: {len(contrastive_only_ids)}, Both: {len(both_ids)}")
print(f"Jaccard: {jaccard:.4f}")
if both_stats.get("n", 0) > 0:
    print(f"Both group answer dist: {both_stats.get('answer_dist', {})}")
print(f"Debate-only answer dist: {debate_only_stats.get('answer_dist', {})}")
print(f"Contrastive-only answer dist: {contrastive_only_stats.get('answer_dist', {})}")

print(f"\n=== ANSWER-TYPE FLIP RATES ===")
for ans_type in ["True", "False", "Unknown"]:
    n_total = sum(1 for r in debate_results if r["ground_truth"] == ans_type)
    n_deb_flip = sum(1 for r in debate_disc if r["ground_truth"] == ans_type)
    n_con_flip = sum(1 for r in contrastive_disc if r["ground_truth"] == ans_type)
    n_sc_correct = sum(1 for r in debate_results if r["ground_truth"] == ans_type and r["sc_correct"])
    if n_sc_correct > 0:
        print(f"  {ans_type}: total={n_total}, SC_correct={n_sc_correct}, Debate_flipped={n_deb_flip} ({n_deb_flip/n_sc_correct:.1%}), Contrastive_flipped={n_con_flip} ({n_con_flip/n_sc_correct:.1%})")

print("\nJSON saved to /tmp/error_categorization_discordant.json")
