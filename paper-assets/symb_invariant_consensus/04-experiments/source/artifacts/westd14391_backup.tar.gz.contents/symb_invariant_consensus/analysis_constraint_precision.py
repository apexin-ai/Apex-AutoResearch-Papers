import json, os, glob
import numpy as np
from collections import Counter

def load_experiment(results_dir, results_file):
    # Load summary
    with open(results_file) as f:
        summary_data = json.load(f)
    
    # Load per-problem intermediates
    problems = {}
    for fpath in sorted(glob.glob(os.path.join(results_dir, "intermediates", "folio_*.json"))):
        with open(fpath) as f:
            data = json.load(f)
        pid = data["problem"]["id"]
        problems[pid] = data
    
    return summary_data, problems

def analyze_experiment(name, summary_data, problems):
    print(f"\n{'='*70}")
    print(f"  {name}")
    print(f"{'='*70}")
    
    summ = summary_data["summary"]
    results = summary_data["results"]
    
    # Build results lookup
    results_by_id = {r["problem_id"]: r for r in results}
    
    # Per-problem metrics
    total_extracted_list = []
    unique_constraints_list = []
    dedup_ratios = []
    sat_ratios = []
    majority_fractions = []
    entropy_list = []
    n_answer_types_list = []
    
    sica_wins = 0
    sc_wins = 0
    both_correct = 0
    both_wrong = 0
    discordant = 0
    sica_correct_total = 0
    sc_correct_total = 0
    
    # For confirmation bias
    constraint_majority_alignment = []
    
    for pid in sorted(problems.keys()):
        pdata = problems[pid]
        rdata = results_by_id.get(pid, {})
        sica = pdata["sica_result"]
        
        # Constraint stats
        cs = sica["constraints_stats"]
        total_ext = cs["total_extracted"]
        unique = cs["unique_after_dedup"]
        total_extracted_list.append(total_ext)
        unique_constraints_list.append(unique)
        dedup_ratios.append(unique / total_ext if total_ext > 0 else 0)
        
        # MaxSAT stats
        ms = sica["maxsat_stats"]
        sat_ratio = ms["satisfied"] / unique if unique > 0 else 0
        sat_ratios.append(sat_ratio)
        
        # Vote distribution (trace diversity)
        answer_counts = sica["answer_counts"]
        total_votes = sum(answer_counts.values())
        majority_count = max(answer_counts.values())
        majority_frac = majority_count / total_votes if total_votes > 0 else 0
        majority_fractions.append(majority_frac)
        n_answer_types_list.append(len(answer_counts))
        
        # Entropy of vote distribution
        probs = [v/total_votes for v in answer_counts.values()]
        entropy = -sum(p * np.log2(p) for p in probs if p > 0)
        entropy_list.append(entropy)
        
        # Correctness comparison
        gt = rdata.get("ground_truth", pdata["problem"]["answer"])
        sica_ans = sica["answer"]
        sc_ans = rdata.get("sc_answer", "")
        sica_ok = (sica_ans == gt)
        sc_ok = (sc_ans == gt)
        
        if sica_ok: sica_correct_total += 1
        if sc_ok: sc_correct_total += 1
        
        if sica_ok and sc_ok:
            both_correct += 1
        elif not sica_ok and not sc_ok:
            both_wrong += 1
        elif sica_ok and not sc_ok:
            sica_wins += 1
            discordant += 1
        elif not sica_ok and sc_ok:
            sc_wins += 1
            discordant += 1
        
        # Confirmation bias: majority answer's score fraction
        scores = sica.get("scores", {})
        if scores:
            majority_answer = max(answer_counts, key=answer_counts.get)
            total_score = sum(scores.values())
            maj_score = scores.get(majority_answer, 0)
            maj_score_frac = maj_score / total_score if total_score > 0 else 0
            constraint_majority_alignment.append(maj_score_frac)
    
    n = len(problems)
    
    print(f"\n--- Summary ---")
    print(f"N problems: {n}")
    print(f"SICA accuracy: {sica_correct_total/n*100:.2f}% ({sica_correct_total}/{n})")
    print(f"SC accuracy:   {sc_correct_total/n*100:.2f}% ({sc_correct_total}/{n})")
    print(f"Delta (SICA-SC): {(sica_correct_total-sc_correct_total)/n*100:+.2f}pp")
    
    print(f"\n--- Constraint Quantity ---")
    print(f"Total extracted per problem: mean={np.mean(total_extracted_list):.1f}, median={np.median(total_extracted_list):.1f}, std={np.std(total_extracted_list):.1f}")
    print(f"Unique after dedup per problem: mean={np.mean(unique_constraints_list):.1f}, median={np.median(unique_constraints_list):.1f}, std={np.std(unique_constraints_list):.1f}")
    print(f"Dedup ratio (unique/total): mean={np.mean(dedup_ratios):.3f}, median={np.median(dedup_ratios):.3f}")
    
    print(f"\n--- Contradiction Rate ---")
    print(f"Global contradiction rate: {summ['contradiction_rate']*100:.2f}%")
    print(f"Problems with contradictions: {summ['problems_with_contradictions']}/{n} ({summ['problems_with_contradictions']/n*100:.1f}%)")
    
    print(f"\n--- MaxSAT Satisfaction ---")
    print(f"Sat ratio (satisfied/unique): mean={np.mean(sat_ratios):.3f}, median={np.median(sat_ratios):.3f}")
    
    print(f"\n--- Trace Diversity (Vote Distribution) ---")
    print(f"Majority fraction: mean={np.mean(majority_fractions):.3f}, median={np.median(majority_fractions):.3f}")
    print(f"Distinct answer types: mean={np.mean(n_answer_types_list):.2f}")
    print(f"Vote entropy: mean={np.mean(entropy_list):.3f}, median={np.median(entropy_list):.3f}")
    
    # Categorize majority fraction
    unanimous = sum(1 for mf in majority_fractions if mf >= 1.0)
    strong_maj = sum(1 for mf in majority_fractions if 0.75 <= mf < 1.0)
    moderate_maj = sum(1 for mf in majority_fractions if 0.5 <= mf < 0.75)
    split = sum(1 for mf in majority_fractions if mf < 0.5)
    print(f"Unanimous (100%): {unanimous} ({unanimous/n*100:.1f}%)")
    print(f"Strong majority (75-99%): {strong_maj} ({strong_maj/n*100:.1f}%)")
    print(f"Moderate majority (50-74%): {moderate_maj} ({moderate_maj/n*100:.1f}%)")
    print(f"Split (<50%): {split} ({split/n*100:.1f}%)")
    
    print(f"\n--- Discriminative Analysis (SICA vs SC) ---")
    print(f"Both correct: {both_correct}")
    print(f"Both wrong: {both_wrong}")
    print(f"SICA wins (SICA correct, SC wrong): {sica_wins}")
    print(f"SC wins (SC correct, SICA wrong): {sc_wins}")
    print(f"Discordant total: {discordant} ({discordant/n*100:.1f}%)")
    if discordant > 0:
        print(f"SICA win rate in discordant: {sica_wins/discordant*100:.1f}%")
    
    print(f"\n--- Confirmation Bias (Constraint-Majority Alignment) ---")
    if constraint_majority_alignment:
        print(f"Majority answer's score fraction: mean={np.mean(constraint_majority_alignment):.3f}, median={np.median(constraint_majority_alignment):.3f}")
        high_confirm = sum(1 for x in constraint_majority_alignment if x > 0.8)
        print(f"High confirmation (maj_score > 80% of total): {high_confirm}/{n} ({high_confirm/n*100:.1f}%)")
    
    return {
        "total_extracted": total_extracted_list,
        "unique_constraints": unique_constraints_list,
        "dedup_ratios": dedup_ratios,
        "sat_ratios": sat_ratios,
        "majority_fractions": majority_fractions,
        "entropy": entropy_list,
        "sica_wins": sica_wins,
        "sc_wins": sc_wins,
        "both_correct": both_correct,
        "both_wrong": both_wrong,
        "constraint_majority_alignment": constraint_majority_alignment,
        "results_by_id": results_by_id,
        "problems": problems,
    }


def cross_model_comparison(mistral_data, qwen_data, mistral_problems, qwen_problems):
    print(f"\n{'='*70}")
    print(f"  CROSS-MODEL COMPARISON")
    print(f"{'='*70}")
    
    # Per-problem paired comparison
    common_pids = sorted(set(mistral_problems.keys()) & set(qwen_problems.keys()))
    print(f"\nCommon problems: {len(common_pids)}")
    
    # Regime analysis: group by Qwen's SC correctness
    qwen_sc_correct_pids = []
    qwen_sc_wrong_pids = []
    for pid in common_pids:
        qr = qwen_data["results_by_id"].get(pid, {})
        gt = qr.get("ground_truth", qwen_problems[pid]["problem"]["answer"])
        if qr.get("sc_answer") == gt:
            qwen_sc_correct_pids.append(pid)
        else:
            qwen_sc_wrong_pids.append(pid)
    
    print(f"\nQwen SC correct: {len(qwen_sc_correct_pids)}, Qwen SC wrong: {len(qwen_sc_wrong_pids)}")
    
    # For problems where Qwen SC is correct (high confidence regime)
    print(f"\n--- On Qwen-SC-correct problems ({len(qwen_sc_correct_pids)}) ---")
    m_maj_correct = [mistral_problems[pid]["sica_result"]["answer_counts"] for pid in qwen_sc_correct_pids]
    m_maj_frac_correct = []
    for ac in m_maj_correct:
        total = sum(ac.values())
        m_maj_frac_correct.append(max(ac.values()) / total)
    q_maj_frac_correct = []
    for pid in qwen_sc_correct_pids:
        ac = qwen_problems[pid]["sica_result"]["answer_counts"]
        total = sum(ac.values())
        q_maj_frac_correct.append(max(ac.values()) / total)
    print(f"  Mistral majority fraction: {np.mean(m_maj_frac_correct):.3f}")
    print(f"  Qwen majority fraction:    {np.mean(q_maj_frac_correct):.3f}")
    
    # For problems where Qwen SC is wrong (challenging regime)
    if qwen_sc_wrong_pids:
        print(f"\n--- On Qwen-SC-wrong problems ({len(qwen_sc_wrong_pids)}) ---")
        m_maj_frac_wrong = []
        for pid in qwen_sc_wrong_pids:
            ac = mistral_problems[pid]["sica_result"]["answer_counts"]
            total = sum(ac.values())
            m_maj_frac_wrong.append(max(ac.values()) / total)
        q_maj_frac_wrong = []
        for pid in qwen_sc_wrong_pids:
            ac = qwen_problems[pid]["sica_result"]["answer_counts"]
            total = sum(ac.values())
            q_maj_frac_wrong.append(max(ac.values()) / total)
        print(f"  Mistral majority fraction: {np.mean(m_maj_frac_wrong):.3f}")
        print(f"  Qwen majority fraction:    {np.mean(q_maj_frac_wrong):.3f}")
    
    # Detailed: per-problem constraint comparison
    print(f"\n--- Per-Problem Constraint Comparison ---")
    m_more_unique = 0
    q_more_unique = 0
    m_higher_dedup = 0
    q_higher_dedup = 0
    
    # Score spread analysis
    m_score_spreads = []
    q_score_spreads = []
    
    for pid in common_pids:
        m_cs = mistral_problems[pid]["sica_result"]["constraints_stats"]
        q_cs = qwen_problems[pid]["sica_result"]["constraints_stats"]
        
        if m_cs["unique_after_dedup"] > q_cs["unique_after_dedup"]:
            m_more_unique += 1
        elif q_cs["unique_after_dedup"] > m_cs["unique_after_dedup"]:
            q_more_unique += 1
        
        m_dr = m_cs["unique_after_dedup"] / m_cs["total_extracted"] if m_cs["total_extracted"] > 0 else 0
        q_dr = q_cs["unique_after_dedup"] / q_cs["total_extracted"] if q_cs["total_extracted"] > 0 else 0
        if m_dr > q_dr:
            m_higher_dedup += 1
        elif q_dr > m_dr:
            q_higher_dedup += 1
        
        # Score spread (range of SICA scores)
        m_scores = mistral_problems[pid]["sica_result"].get("scores", {})
        q_scores = qwen_problems[pid]["sica_result"].get("scores", {})
        if len(m_scores) > 1:
            m_score_spreads.append(max(m_scores.values()) - min(m_scores.values()))
        if len(q_scores) > 1:
            q_score_spreads.append(max(q_scores.values()) - min(q_scores.values()))
    
    print(f"Mistral has more unique constraints: {m_more_unique}")
    print(f"Qwen has more unique constraints:    {q_more_unique}")
    print(f"Mistral higher dedup ratio:          {m_higher_dedup}")
    print(f"Qwen higher dedup ratio:             {q_higher_dedup}")
    
    print(f"\n--- SICA Score Spread ---")
    print(f"Mistral score spread (multi-answer): mean={np.mean(m_score_spreads):.1f}, n={len(m_score_spreads)}")
    print(f"Qwen score spread (multi-answer):    mean={np.mean(q_score_spreads):.1f}, n={len(q_score_spreads)}")
    
    # Key analysis: on problems where SICA flipped the answer vs SC
    print(f"\n--- SICA Flip Analysis ---")
    for model_name, probs, res_by_id in [("Mistral", mistral_problems, mistral_data["results_by_id"]),
                                           ("Qwen", qwen_problems, qwen_data["results_by_id"])]:
        flips = 0
        flip_correct = 0
        flip_wrong = 0
        flip_entropies = []
        flip_unique_constraints = []
        for pid in common_pids:
            r = res_by_id.get(pid, {})
            gt = r.get("ground_truth", probs[pid]["problem"]["answer"])
            sica_ans = r.get("sica_answer", probs[pid]["sica_result"]["answer"])
            sc_ans = r.get("sc_answer", "")
            if sica_ans != sc_ans:
                flips += 1
                ac = probs[pid]["sica_result"]["answer_counts"]
                total = sum(ac.values())
                p_list = [v/total for v in ac.values()]
                ent = -sum(p * np.log2(p) for p in p_list if p > 0)
                flip_entropies.append(ent)
                flip_unique_constraints.append(probs[pid]["sica_result"]["constraints_stats"]["unique_after_dedup"])
                if sica_ans == gt:
                    flip_correct += 1
                else:
                    flip_wrong += 1
        print(f"\n  {model_name}:")
        print(f"    Total flips (SICA != SC): {flips}")
        print(f"    Flip -> correct: {flip_correct}")
        print(f"    Flip -> wrong: {flip_wrong}")
        if flips > 0:
            print(f"    Flip precision: {flip_correct/flips*100:.1f}%")
            print(f"    Mean entropy on flip problems: {np.mean(flip_entropies):.3f}")
            print(f"    Mean unique constraints on flip problems: {np.mean(flip_unique_constraints):.1f}")


# Main
base = "/root/symb_invariant_consensus/results"

mistral_summary, mistral_problems = load_experiment(
    os.path.join(base, "exp033_mistral_7b_folio204"),
    os.path.join(base, "exp033_mistral_7b_folio204", "exp033_results.json")
)

qwen_summary, qwen_problems = load_experiment(
    os.path.join(base, "folio_204_14b"),
    os.path.join(base, "folio_204_14b", "folio_204_results.json")
)

mistral_data = analyze_experiment("Mistral-7B (exp033)", mistral_summary, mistral_problems)
qwen_data = analyze_experiment("Qwen2.5-14B (exp026/folio_204_14b)", qwen_summary, qwen_problems)

cross_model_comparison(mistral_data, qwen_data, mistral_problems, qwen_problems)

# Additional: Confirmation Bias Deep Dive
print(f"\n{'='*70}")
print(f"  CONFIRMATION BIAS DEEP DIVE")
print(f"{'='*70}")

common_pids = sorted(set(mistral_problems.keys()) & set(qwen_problems.keys()))

# For each problem, compute: does the constraint weighting just confirm majority vote?
# Or does it add new information?
m_confirm_count = 0
q_confirm_count = 0
m_override_count = 0
q_override_count = 0

for pid in common_pids:
    for label, probs_dict, confirm_count_ref, override_count_ref in [
        ("mistral", mistral_problems, "m", None),
        ("qwen", qwen_problems, "q", None)
    ]:
        sica = probs_dict[pid]["sica_result"]
        ac = sica["answer_counts"]
        scores = sica.get("scores", {})
        
        sc_winner = max(ac, key=ac.get)
        sica_winner = sica["answer"]
        
        if sica_winner == sc_winner:
            if label == "mistral": m_confirm_count += 1
            else: q_confirm_count += 1
        else:
            if label == "mistral": m_override_count += 1
            else: q_override_count += 1

print(f"\nMistral-7B: SICA confirms SC = {m_confirm_count}, SICA overrides SC = {m_override_count}")
print(f"Qwen-14B:   SICA confirms SC = {q_confirm_count}, SICA overrides SC = {q_override_count}")
print(f"Mistral override rate: {m_override_count/len(common_pids)*100:.1f}%")
print(f"Qwen override rate:   {q_override_count/len(common_pids)*100:.1f}%")

# When SICA overrides, is it correct?
m_override_correct = 0
m_override_wrong = 0
q_override_correct = 0
q_override_wrong = 0

for pid in common_pids:
    for label, probs_dict, res_by_id in [
        ("mistral", mistral_problems, mistral_data["results_by_id"]),
        ("qwen", qwen_problems, qwen_data["results_by_id"])
    ]:
        sica = probs_dict[pid]["sica_result"]
        ac = sica["answer_counts"]
        sc_winner = max(ac, key=ac.get)
        sica_winner = sica["answer"]
        r = res_by_id.get(pid, {})
        gt = r.get("ground_truth", probs_dict[pid]["problem"]["answer"])
        
        if sica_winner != sc_winner:
            if sica_winner == gt:
                if label == "mistral": m_override_correct += 1
                else: q_override_correct += 1
            else:
                if label == "mistral": m_override_wrong += 1
                else: q_override_wrong += 1

print(f"\nMistral overrides: {m_override_correct} correct, {m_override_wrong} wrong -> precision {m_override_correct/(m_override_correct+m_override_wrong)*100:.1f}%" if m_override_correct+m_override_wrong > 0 else "")
print(f"Qwen overrides:   {q_override_correct} correct, {q_override_wrong} wrong -> precision {q_override_correct/(q_override_correct+q_override_wrong)*100:.1f}%" if q_override_correct+q_override_wrong > 0 else "")

# Consensus concentration analysis
print(f"\n--- Consensus Concentration by Entropy Bucket ---")
for label, probs_dict, res_by_id in [
    ("Mistral-7B", mistral_problems, mistral_data["results_by_id"]),
    ("Qwen-14B", qwen_problems, qwen_data["results_by_id"])
]:
    print(f"\n  {label}:")
    buckets = {"low_ent (0-0.5)": [], "med_ent (0.5-1.0)": [], "high_ent (1.0+)": []}
    for pid in common_pids:
        sica = probs_dict[pid]["sica_result"]
        ac = sica["answer_counts"]
        total = sum(ac.values())
        p_list = [v/total for v in ac.values()]
        ent = -sum(p * np.log2(p) for p in p_list if p > 0)
        
        r = res_by_id.get(pid, {})
        gt = r.get("ground_truth", probs_dict[pid]["problem"]["answer"])
        sica_ok = (sica["answer"] == gt)
        sc_ans = r.get("sc_answer", max(ac, key=ac.get))
        sc_ok = (sc_ans == gt)
        
        if ent < 0.5:
            buckets["low_ent (0-0.5)"].append((sica_ok, sc_ok))
        elif ent < 1.0:
            buckets["med_ent (0.5-1.0)"].append((sica_ok, sc_ok))
        else:
            buckets["high_ent (1.0+)"].append((sica_ok, sc_ok))
    
    for bname, items in buckets.items():
        if items:
            sica_acc = sum(s for s, _ in items) / len(items)
            sc_acc = sum(s for _, s in items) / len(items)
            delta = sica_acc - sc_acc
            print(f"    {bname}: n={len(items)}, SICA={sica_acc*100:.1f}%, SC={sc_acc*100:.1f}%, delta={delta*100:+.1f}pp")

print("\n\nDone.")
