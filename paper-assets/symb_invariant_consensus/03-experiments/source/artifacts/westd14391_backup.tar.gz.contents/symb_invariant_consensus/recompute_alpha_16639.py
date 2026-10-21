#!/usr/bin/env python3
"""Recompute NLI combo with alphabetical tiebreaking for LLaMA, Qwen2.5, Qwen3 on PW600."""
import json
from collections import Counter
from scipy.stats import binomtest

VALID = {"True", "False", "Unknown"}
WEIGHTS = [1, 3, 5]

def majority_alpha(vote_dist):
    filtered = {k: v for k, v in vote_dist.items() if k in VALID}
    if not filtered:
        return "Unknown"
    max_count = max(filtered.values())
    winners = sorted([k for k, v in filtered.items() if v == max_count])
    return winners[0]

def combo_alpha(vote_dist, nli_pred, w):
    combined = {}
    for k, v in vote_dist.items():
        if k in VALID:
            combined[k] = combined.get(k, 0) + v
    if nli_pred in VALID:
        combined[nli_pred] = combined.get(nli_pred, 0) + w
    if not combined:
        return "Unknown"
    max_count = max(combined.values())
    winners = sorted([k for k, v in combined.items() if v == max_count])
    return winners[0]

def mcnemar_exact(b, c):
    n = b + c
    if n == 0:
        return 1.0
    return binomtest(min(b, c), n, 0.5).pvalue

def process_generator(name, questions):
    """questions: list of {pid, gold, sc_vote_distribution, deberta_pred}"""
    n = len(questions)
    
    # SC baseline (alphabetical)
    sc_correct = 0
    sc_results = []
    for q in questions:
        sc_ans = majority_alpha(q["sc_vote_distribution"])
        correct = (sc_ans == q["gold"])
        sc_results.append(correct)
        if correct:
            sc_correct += 1
    sc_acc = sc_correct / n
    
    # Combo for each weight
    combo_data = {}
    for w in WEIGHTS:
        combo_correct_list = []
        b_count = 0
        c_count = 0
        for i, q in enumerate(questions):
            combo_ans = combo_alpha(q["sc_vote_distribution"], q["deberta_pred"], w)
            combo_ok = (combo_ans == q["gold"])
            combo_correct_list.append(combo_ok)
            sc_ok = sc_results[i]
            if combo_ok and not sc_ok:
                b_count += 1
            if not combo_ok and sc_ok:
                c_count += 1
        
        combo_n_correct = sum(combo_correct_list)
        combo_acc = combo_n_correct / n
        delta_pp = round((combo_acc - sc_acc) * 100, 2)
        p_val = mcnemar_exact(b_count, c_count)
        
        combo_data[f"w{w}"] = {
            "acc": round(combo_acc * 100, 2),
            "n_correct": combo_n_correct,
            "delta_pp": delta_pp,
            "mcnemar_p": p_val,
            "b": b_count,
            "c": c_count
        }
    
    return {
        "sc": {"acc": round(sc_acc * 100, 2), "n_correct": sc_correct},
        **combo_data
    }

# === LLaMA-3.1-8B ===
print("Loading LLaMA-3.1-8B...")
with open("/root/symb_invariant_consensus/results/exp092_llama8b_pw_nli_combo/results.json") as f:
    llama_data = json.load(f)
llama_questions = []
for pid, pq in llama_data["per_question"].items():
    llama_questions.append({
        "pid": pid,
        "gold": pq["gold"],
        "sc_vote_distribution": pq["sc_vote_distribution"],
        "deberta_pred": pq["deberta_pred"]
    })
llama_result = process_generator("LLaMA-3.1-8B", llama_questions)
print(f"  LLaMA SC: {llama_result['sc']}")
for w in WEIGHTS:
    print(f"  LLaMA w{w}: {llama_result[f'w{w}']}")

# === Qwen2.5-14B ===
print("\nLoading Qwen2.5-14B...")
with open("/root/symb_invariant_consensus/results/qwen14b_pw_nli_combo/results.json") as f:
    qwen25_data = json.load(f)
qwen25_questions = []
for pid, pq in qwen25_data["per_question"].items():
    qwen25_questions.append({
        "pid": pid,
        "gold": pq["gold"],
        "sc_vote_distribution": pq["sc_vote_distribution"],
        "deberta_pred": pq["deberta_pred"]
    })
qwen25_result = process_generator("Qwen2.5-14B", qwen25_questions)
print(f"  Qwen2.5 SC: {qwen25_result['sc']}")
for w in WEIGHTS:
    print(f"  Qwen2.5 w{w}: {qwen25_result[f'w{w}']}")

# === Qwen3-14B ===
print("\nLoading Qwen3-14B...")
with open("/root/symb_invariant_consensus/results/exp033_qwen3_14b_pw600_nonthinking/results.json") as f:
    qwen3_sc = json.load(f)
with open("/root/symb_invariant_consensus/results/d116_qwen3_pw_deberta_large/results.json") as f:
    d116 = json.load(f)

# Build SC vote dist from exp033
qwen3_sc_by_pid = {}
for r in qwen3_sc["results"]:
    qwen3_sc_by_pid[r["problem_id"]] = {
        "sc_vote_distribution": r["sc_vote_distribution"],
        "gold": r["ground_truth"]
    }

# Build DeBERTa preds from D116
d116_pq = d116["per_question"]

qwen3_questions = []
for pid in qwen3_sc_by_pid:
    if pid not in d116_pq:
        continue
    qwen3_questions.append({
        "pid": pid,
        "gold": qwen3_sc_by_pid[pid]["gold"],
        "sc_vote_distribution": qwen3_sc_by_pid[pid]["sc_vote_distribution"],
        "deberta_pred": d116_pq[pid]["deberta_pred"]
    })
print(f"  Qwen3 merged: {len(qwen3_questions)} questions")
qwen3_result = process_generator("Qwen3-14B", qwen3_questions)
print(f"  Qwen3 SC: {qwen3_result['sc']}")
for w in WEIGHTS:
    print(f"  Qwen3 w{w}: {qwen3_result[f'w{w}']}")

# Save
output = {
    "LLaMA-3.1-8B": llama_result,
    "Qwen2.5-14B": qwen25_result,
    "Qwen3-14B": qwen3_result
}
with open("/root/symb_invariant_consensus/results/alpha_recompute_16639.json", "w") as f:
    json.dump(output, f, indent=2)
print(f"\nSaved to /root/symb_invariant_consensus/results/alpha_recompute_16639.json")
