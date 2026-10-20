#!/usr/bin/env python3
"""Compute process-kappa for multiple models using TF-IDF cosine similarity."""
import json, os, glob, sys
import numpy as np
from itertools import combinations
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from scipy import stats
from collections import Counter

def load_traces(intermediates_dir):
    data = {}
    for fpath in sorted(glob.glob(os.path.join(intermediates_dir, "folio_*.json"))):
        with open(fpath) as f:
            d = json.load(f)
        qid = d["problem"]["id"]
        data[qid] = d["sica_result"]["traces"]
    return data

def per_question_answer_agreement(answers):
    n = len(answers)
    counts = Counter(answers)
    agree_pairs = sum(c * (c - 1) for c in counts.values())
    total_pairs = n * (n - 1)
    return agree_pairs / total_pairs if total_pairs > 0 else 0.0

def fleiss_kappa_from_traces(data, qids):
    categories = ["True", "False", "Unknown"]
    cat2idx = {c: i for i, c in enumerate(categories)}
    ratings = np.zeros((len(qids), len(categories)), dtype=int)
    for qi, qid in enumerate(qids):
        for trace in data[qid]:
            ans = trace["answer"]
            if ans in cat2idx:
                ratings[qi, cat2idx[ans]] += 1
            elif ans.strip():
                ratings[qi, cat2idx["Unknown"]] += 1
    n_per_q = ratings.sum(axis=1)
    valid = n_per_q >= 2
    ratings = ratings[valid]
    n_per_q = n_per_q[valid]
    N = ratings.shape[0]
    if N == 0:
        return float('nan')
    p_j = ratings.sum(axis=0) / ratings.sum()
    P_e = np.sum(p_j ** 2)
    P_i = (np.sum(ratings ** 2, axis=1) - n_per_q) / (n_per_q * (n_per_q - 1))
    P_bar = np.mean(P_i)
    if P_e >= 1.0:
        return 1.0
    return (P_bar - P_e) / (1 - P_e)

def mean_pairwise_cosine(texts):
    non_empty = [t for t in texts if t.strip()]
    if len(non_empty) < 2:
        return 0.0
    vectorizer = TfidfVectorizer(max_features=5000, stop_words="english")
    try:
        tfidf = vectorizer.fit_transform(non_empty)
    except ValueError:
        return 0.0
    sim_matrix = cosine_similarity(tfidf)
    n = sim_matrix.shape[0]
    upper_tri = sim_matrix[np.triu_indices(n, k=1)]
    return float(np.mean(upper_tri))

def same_answer_different_process(traces, cosine_threshold=0.5):
    answers = [t["answer"] for t in traces]
    texts = [t["trace"] for t in traces]
    non_empty_indices = [i for i, t in enumerate(texts) if t.strip()]
    if len(non_empty_indices) < 2:
        return None, 0, 0
    ne_texts = [texts[i] for i in non_empty_indices]
    ne_answers = [answers[i] for i in non_empty_indices]
    vectorizer = TfidfVectorizer(max_features=5000, stop_words="english")
    try:
        tfidf = vectorizer.fit_transform(ne_texts)
    except ValueError:
        return None, 0, 0
    sim = cosine_similarity(tfidf)
    sa_pairs = 0
    dp_pairs = 0
    for i, j in combinations(range(len(non_empty_indices)), 2):
        if ne_answers[i] == ne_answers[j]:
            sa_pairs += 1
            if sim[i, j] < cosine_threshold:
                dp_pairs += 1
    if sa_pairs == 0:
        return None, 0, 0
    return dp_pairs / sa_pairs, dp_pairs, sa_pairs

def compute_one(name, model, intermediates_dir):
    data = load_traces(intermediates_dir)
    qids = sorted(data.keys(), key=lambda x: int(x.split("_")[1]))
    K = len(data[qids[0]])
    kappa = fleiss_kappa_from_traces(data, qids)

    per_q = []
    for qid in qids:
        traces = data[qid]
        answers = [t["answer"] for t in traces]
        texts = [t["trace"] for t in traces]
        ans_agree = per_question_answer_agreement(answers)
        proc_sim = mean_pairwise_cosine(texts)
        sadp_ratio, sadp_count, sa_total = same_answer_different_process(traces)
        per_q.append({
            "qid": qid,
            "answer_agreement": round(ans_agree, 4),
            "process_similarity": round(proc_sim, 4),
            "same_ans_diff_proc_ratio": round(sadp_ratio, 4) if sadp_ratio is not None else None,
            "same_ans_diff_proc_count": sadp_count,
            "same_ans_total_pairs": sa_total,
        })

    ans_ag = [q["answer_agreement"] for q in per_q]
    proc_sim = [q["process_similarity"] for q in per_q]
    r_p, p_p = stats.pearsonr(ans_ag, proc_sim)
    r_s, p_s = stats.spearmanr(ans_ag, proc_sim)
    valid_sadp = [q for q in per_q if q["same_ans_diff_proc_ratio"] is not None]
    total_dp = sum(q["same_ans_diff_proc_count"] for q in valid_sadp)
    total_sa = sum(q["same_ans_total_pairs"] for q in valid_sadp)
    global_sadp = total_dp / total_sa if total_sa > 0 else 0.0

    return {
        "experiment": name,
        "model": model,
        "K": K,
        "n_questions": len(qids),
        "answer_kappa_3cat": round(kappa, 4),
        "mean_cosine_similarity": round(float(np.mean(proc_sim)), 4),
        "std_cosine_similarity": round(float(np.std(proc_sim)), 4),
        "pearson_r": round(r_p, 4),
        "pearson_p": round(p_p, 6),
        "spearman_rho": round(r_s, 4),
        "spearman_p": round(p_s, 6),
        "convergent_pairs_pct": round(global_sadp * 100, 1),
        "total_same_answer_pairs": total_sa,
        "total_different_process_pairs": total_dp,
    }

EXPERIMENTS = {
    "exp036": {
        "model": "Qwen2.5-14B",
        "dir": "/root/symb_invariant_consensus/results/exp036_qwen25_14b_folio204/intermediates",
    },
    "exp063": {
        "model": "LLaMA-3.1-8B",
        "dir": "/root/symb_invariant_consensus/results/exp-063-llama8b-folio204-16639/intermediates",
    },
}

if __name__ == "__main__":
    targets = sys.argv[1:] if len(sys.argv) > 1 else list(EXPERIMENTS.keys())
    results = []
    for exp_id in targets:
        if exp_id not in EXPERIMENTS:
            print(f"Unknown: {exp_id}")
            continue
        cfg = EXPERIMENTS[exp_id]
        if not os.path.isdir(cfg["dir"]):
            print(f"Skipping {exp_id}: dir not found")
            continue
        print(f"Computing {exp_id} ({cfg['model']})...")
        r = compute_one(exp_id, cfg["model"], cfg["dir"])
        results.append(r)
        print(f"  cosine={r['mean_cosine_similarity']}, kappa={r['answer_kappa_3cat']}, r={r['pearson_r']}, conv={r['convergent_pairs_pct']}%")

    out = "/root/symb_invariant_consensus/results/process_kappa_summary_16639.json"
    with open(out, "w") as f:
        json.dump(results, f, indent=2)
    print(f"\nSaved to {out}")
