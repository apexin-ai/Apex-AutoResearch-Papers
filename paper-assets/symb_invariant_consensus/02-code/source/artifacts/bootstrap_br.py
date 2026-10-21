import json
import os
import numpy as np
from collections import defaultdict

def load_raw_counts_from_cache(cache_dir, pid):
    path = os.path.join(cache_dir, f"{pid}.json")
    if not os.path.exists(path):
        return None, 0
    with open(path) as f:
        data = json.load(f)
    answer_counts = defaultdict(int)
    total = 0
    for trace in data.get("per_trace", []):
        ans = trace.get("answer") or trace.get("extracted_answer", "")
        ans = ans.strip() if ans else ""
        if not ans:
            continue
        n = len(trace.get("constraints", []))
        answer_counts[ans] += n
        total += n
    return dict(answer_counts), total

def load_llama_constraints(path):
    with open(path) as f:
        data = json.load(f)
    result = {}
    for pid, pdata in data.items():
        answer_counts = defaultdict(int)
        total = 0
        for trace in pdata.get("per_trace", []):
            ans = trace.get("answer", "").strip()
            if not ans:
                continue
            n = len(trace.get("constraints", []))
            answer_counts[ans] += n
            total += n
        result[pid] = (dict(answer_counts), total)
    return result

def get_per_question_data(results_path, cache_dir):
    with open(results_path) as f:
        data = json.load(f)
    questions = []
    for r in data["results"]:
        gt = r["ground_truth"]
        sica_ans = r["sica_answer"]
        pid = r["problem_id"]
        if sica_ans == gt:
            continue
        if cache_dir:
            ans_counts, total_c = load_raw_counts_from_cache(cache_dir, pid)
        else:
            scores = r.get("sica_scores", {})
            total_c = sum(scores.values())
            ans_counts = scores
        if not ans_counts or total_c == 0:
            continue
        gold_c = ans_counts.get(gt, 0)
        wrong_c = total_c - gold_c
        questions.append((wrong_c, gold_c))
    return questions

def get_llama_per_question_data(llama_constraints_path, llama_answer_matrix_path):
    llama_c = load_llama_constraints(llama_constraints_path)
    with open(llama_answer_matrix_path) as f:
        answer_matrix = json.load(f)
    questions = []
    n_sica_wrong = 0
    n_total = 0
    for pid, pdata in answer_matrix.items():
        gt = pdata["ground_truth"]
        n_total += 1
        if pid not in llama_c:
            continue
        ans_counts, total_c = llama_c[pid]
        if total_c == 0:
            continue
        sica_answer = max(ans_counts, key=ans_counts.get) if ans_counts else None
        if sica_answer == gt:
            continue
        n_sica_wrong += 1
        gold_c = ans_counts.get(gt, 0)
        wrong_c = total_c - gold_c
        questions.append((wrong_c, gold_c))
    print(f"  LLaMA: {n_total} total, {n_sica_wrong} SICA-wrong, {len(questions)} with data")
    return questions

def bootstrap_br(questions, n_boot=10000, seed=42):
    rng = np.random.RandomState(seed)
    n = len(questions)
    gold_fracs = np.array([gold_c / (wrong_c + gold_c) if (wrong_c + gold_c) > 0 else 0
                           for wrong_c, gold_c in questions])
    avg_gold = np.mean(gold_fracs)
    point_br = (1 - avg_gold) / avg_gold if avg_gold > 0 else float('inf')
    br_samples = []
    for _ in range(n_boot):
        idx = rng.choice(n, size=n, replace=True)
        boot_gold = np.mean(gold_fracs[idx])
        if boot_gold > 0:
            br_samples.append((1 - boot_gold) / boot_gold)
    br_samples = np.array(br_samples)
    ci_low = float(np.percentile(br_samples, 2.5))
    ci_high = float(np.percentile(br_samples, 97.5))
    return round(point_br, 4), round(ci_low, 4), round(ci_high, 4)

def bootstrap_br_count(questions, n_boot=10000, seed=42):
    rng = np.random.RandomState(seed)
    n = len(questions)
    qa = np.array(questions)
    total_wrong = qa[:, 0].sum()
    total_gold = qa[:, 1].sum()
    point_br = total_wrong / total_gold if total_gold > 0 else float('inf')
    br_samples = []
    for _ in range(n_boot):
        idx = rng.choice(n, size=n, replace=True)
        bw = qa[idx, 0].sum()
        bg = qa[idx, 1].sum()
        if bg > 0:
            br_samples.append(bw / bg)
    br_samples = np.array(br_samples)
    ci_low = float(np.percentile(br_samples, 2.5))
    ci_high = float(np.percentile(br_samples, 97.5))
    return round(point_br, 4), round(ci_low, 4), round(ci_high, 4)

results = {}

# Mistral-7B
print("=== Mistral-7B ===")
mqs = get_per_question_data(
    "/root/symb_invariant_consensus/results/exp033_mistral_7b_folio204/exp033_results.json",
    "/root/symb_invariant_consensus/results/exp033_mistral_7b_folio204/constraint_cache")
print(f"  {len(mqs)} SICA-wrong questions")
br, lo, hi = bootstrap_br(mqs)
br2, lo2, hi2 = bootstrap_br_count(mqs)
print(f"  Frac-based: BR={br}, CI=[{lo}, {hi}]")
print(f"  Count-based: BR={br2}, CI=[{lo2}, {hi2}]")
results["Mistral-7B"] = {"br": br, "ci_low": lo, "ci_high": hi,
                          "br_count": br2, "ci_low_count": lo2, "ci_high_count": hi2,
                          "n_questions": len(mqs)}

# Qwen2.5-14B
print("\n=== Qwen2.5-14B ===")
qqs = get_per_question_data(
    "/root/symb_invariant_consensus/results/folio_204_14b/folio_204_results.json",
    "/root/symb_invariant_consensus/results/folio_204_14b/per_trace_constraints")
print(f"  {len(qqs)} SICA-wrong questions")
br, lo, hi = bootstrap_br(qqs)
br2, lo2, hi2 = bootstrap_br_count(qqs)
print(f"  Frac-based: BR={br}, CI=[{lo}, {hi}]")
print(f"  Count-based: BR={br2}, CI=[{lo2}, {hi2}]")
results["Qwen2.5-14B"] = {"br": br, "ci_low": lo, "ci_high": hi,
                           "br_count": br2, "ci_low_count": lo2, "ci_high_count": hi2,
                           "n_questions": len(qqs)}

# LLaMA-3.1-8B
print("\n=== LLaMA-3.1-8B ===")
lc = "/root/symb_invariant_consensus/results/cross_model_experiment/llama_constraints_t0t3.json"
la = "/root/symb_invariant_consensus/results/cross_model_experiment/llama_sc_answer_matrix.json"
if os.path.exists(lc) and os.path.exists(la):
    lqs = get_llama_per_question_data(lc, la)
    if lqs:
        br, lo, hi = bootstrap_br(lqs)
        br2, lo2, hi2 = bootstrap_br_count(lqs)
        print(f"  Frac-based: BR={br}, CI=[{lo}, {hi}]")
        print(f"  Count-based: BR={br2}, CI=[{lo2}, {hi2}]")
        results["LLaMA-3.1-8B"] = {
            "br": br, "ci_low": lo, "ci_high": hi,
            "br_count": br2, "ci_low_count": lo2, "ci_high_count": hi2,
            "n_questions": len(lqs),
            "note": "4 traces from cross-model experiment"
        }

print("\n" + json.dumps(results, indent=2))
with open("/tmp/br_bootstrap_ci.json", "w") as f:
    json.dump(results, f, indent=2)
print("\nSaved to /tmp/br_bootstrap_ci.json")
