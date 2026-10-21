#!/usr/bin/env python3
"""Wild 4: Process-level vs Answer-level consistency analysis.
Compares Fleiss' kappa (answer agreement) with TF-IDF cosine similarity (process similarity)
on Mistral-7B FOLIO-204 K=12 self-consistency traces.
"""

import json
import os
import glob
import numpy as np
from itertools import combinations
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from scipy import stats


def load_traces(intermediates_dir):
    """Load all traces from intermediate files. Returns dict {qid: [{trace, answer, trace_idx}]}."""
    data = {}
    for fpath in sorted(glob.glob(os.path.join(intermediates_dir, "folio_*.json"))):
        with open(fpath) as f:
            d = json.load(f)
        qid = d["problem"]["id"]
        data[qid] = d["sica_result"]["traces"]
    return data


def fleiss_kappa(ratings_matrix):
    """Compute Fleiss' kappa from an N x k matrix where N=items, k=categories,
    each cell = count of raters assigning that category."""
    N, k = ratings_matrix.shape
    n = ratings_matrix.sum(axis=1)[0]  # number of raters per item (assumed constant)

    p_j = ratings_matrix.sum(axis=0) / (N * n)
    P_e = np.sum(p_j ** 2)

    P_i = (np.sum(ratings_matrix ** 2, axis=1) - n) / (n * (n - 1))
    P_bar = np.mean(P_i)

    if P_e == 1.0:
        return 1.0
    return (P_bar - P_e) / (1 - P_e)


def per_question_answer_agreement(answers):
    """Proportion of agreeing pairs among n raters."""
    n = len(answers)
    from collections import Counter
    counts = Counter(answers)
    agree_pairs = sum(c * (c - 1) for c in counts.values())
    total_pairs = n * (n - 1)
    return agree_pairs / total_pairs if total_pairs > 0 else 0.0


def mean_pairwise_cosine(texts):
    """Mean pairwise cosine similarity of TF-IDF vectors."""
    if len(texts) < 2:
        return 0.0
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
    """Among pairs with the same non-empty answer, fraction with cosine < threshold."""
    answers = [t["answer"] for t in traces]
    texts = [t["trace"] for t in traces]

    non_empty_indices = [i for i, a in enumerate(answers) if a.strip()]
    if len(non_empty_indices) < 2:
        return None, 0, 0

    non_empty_texts = [texts[i] for i in non_empty_indices]
    non_empty_answers = [answers[i] for i in non_empty_indices]

    vectorizer = TfidfVectorizer(max_features=5000, stop_words="english")
    try:
        tfidf = vectorizer.fit_transform(non_empty_texts)
    except ValueError:
        return None, 0, 0
    sim = cosine_similarity(tfidf)

    same_ans_pairs = 0
    diff_process_pairs = 0
    for i, j in combinations(range(len(non_empty_indices)), 2):
        if non_empty_answers[i] == non_empty_answers[j]:
            same_ans_pairs += 1
            if sim[i, j] < cosine_threshold:
                diff_process_pairs += 1

    if same_ans_pairs == 0:
        return None, 0, 0
    return diff_process_pairs / same_ans_pairs, diff_process_pairs, same_ans_pairs


def main():
    intermediates_dir = "/root/symb_invariant_consensus/results/exp033_mistral_7b_folio204/intermediates"
    output_dir = "/root/symb_invariant_consensus/results/wild4_process_kappa"
    os.makedirs(output_dir, exist_ok=True)

    data = load_traces(intermediates_dir)
    qids = sorted(data.keys(), key=lambda x: int(x.split("_")[1]))
    print(f"Loaded {len(qids)} questions, each with {len(data[qids[0]])} traces")

    # Kappa variant 1: 4 categories (True, False, Unknown, empty)
    categories_4 = ["True", "False", "Unknown", ""]
    cat2idx_4 = {c: i for i, c in enumerate(categories_4)}
    ratings_4 = np.zeros((len(qids), len(categories_4)), dtype=int)
    for qi, qid in enumerate(qids):
        for trace in data[qid]:
            ans = trace["answer"]
            if ans not in cat2idx_4:
                ans = ""
            ratings_4[qi, cat2idx_4[ans]] += 1
    kappa_4cat = fleiss_kappa(ratings_4)

    # Kappa variant 2: 3 categories, empty -> Unknown
    categories_3 = ["True", "False", "Unknown"]
    cat2idx_3 = {c: i for i, c in enumerate(categories_3)}
    ratings_3_merged = np.zeros((len(qids), 3), dtype=int)
    for qi, qid in enumerate(qids):
        for trace in data[qid]:
            ans = trace["answer"]
            if ans not in cat2idx_3:
                ans = "Unknown"
            ratings_3_merged[qi, cat2idx_3[ans]] += 1
    kappa_3cat_merged = fleiss_kappa(ratings_3_merged)

    # Kappa variant 3: 3 categories, empty excluded (variable n per item)
    ratings_3_excl = []
    ns_excl = []
    for qi, qid in enumerate(qids):
        answers = [t["answer"] for t in data[qid]]
        valid = [a for a in answers if a in cat2idx_3]
        if len(valid) < 2:
            continue
        row = [0] * 3
        for a in valid:
            row[cat2idx_3[a]] += 1
        ratings_3_excl.append(row)
        ns_excl.append(len(valid))
    ratings_3_excl = np.array(ratings_3_excl, dtype=float)
    ns_excl = np.array(ns_excl, dtype=float)
    p_j_excl = ratings_3_excl.sum(axis=0) / np.sum(ns_excl)
    P_e_excl = np.sum(p_j_excl ** 2)
    P_i_excl = (np.sum(ratings_3_excl ** 2, axis=1) - ns_excl) / (ns_excl * (ns_excl - 1))
    P_bar_excl = np.mean(P_i_excl)
    kappa_3cat_excl = (P_bar_excl - P_e_excl) / (1 - P_e_excl)

    overall_kappa = kappa_3cat_merged  # primary metric
    print(f"Fleiss' kappa (4-cat): {kappa_4cat:.4f}")
    print(f"Fleiss' kappa (3-cat, empty->Unknown): {kappa_3cat_merged:.4f}")
    print(f"Fleiss' kappa (3-cat, empty excluded): {kappa_3cat_excl:.4f}")

    per_q = []
    for qi, qid in enumerate(qids):
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

    ans_agreements = [q["answer_agreement"] for q in per_q]
    proc_similarities = [q["process_similarity"] for q in per_q]

    corr_pearson, p_pearson = stats.pearsonr(ans_agreements, proc_similarities)
    corr_spearman, p_spearman = stats.spearmanr(ans_agreements, proc_similarities)

    valid_sadp = [q for q in per_q if q["same_ans_diff_proc_ratio"] is not None]
    total_sadp_pairs = sum(q["same_ans_diff_proc_count"] for q in valid_sadp)
    total_sa_pairs = sum(q["same_ans_total_pairs"] for q in valid_sadp)
    global_sadp_ratio = total_sadp_pairs / total_sa_pairs if total_sa_pairs > 0 else 0.0

    results = {
        "experiment": "wild4_process_kappa",
        "source": "exp033_mistral_7b_folio204",
        "K": 12,
        "n_questions": len(qids),
        "answer_level": {
            "fleiss_kappa_4cat": round(kappa_4cat, 4),
            "fleiss_kappa_3cat_empty_as_unknown": round(kappa_3cat_merged, 4),
            "fleiss_kappa_3cat_empty_excluded": round(kappa_3cat_excl, 4),
            "fleiss_kappa_primary": round(overall_kappa, 4),
            "mean_agreement": round(float(np.mean(ans_agreements)), 4),
            "std_agreement": round(float(np.std(ans_agreements)), 4),
        },
        "process_level": {
            "mean_cosine_similarity": round(float(np.mean(proc_similarities)), 4),
            "std_cosine_similarity": round(float(np.std(proc_similarities)), 4),
        },
        "correlation": {
            "pearson_r": round(corr_pearson, 4),
            "pearson_p": round(p_pearson, 6),
            "spearman_rho": round(corr_spearman, 4),
            "spearman_p": round(p_spearman, 6),
        },
        "same_answer_different_process": {
            "cosine_threshold": 0.5,
            "global_ratio": round(global_sadp_ratio, 4),
            "total_same_answer_pairs": total_sa_pairs,
            "total_different_process_pairs": total_sadp_pairs,
            "questions_with_data": len(valid_sadp),
        },
        "per_question": per_q,
    }

    output_path = os.path.join(output_dir, "results.json")
    with open(output_path, "w") as f:
        json.dump(results, f, indent=2)
    print(f"\nResults saved to {output_path}")

    print(f"\n=== Summary ===")
    print(f"Fleiss' kappa (4-cat): {kappa_4cat:.4f}")
    print(f"Fleiss' kappa (3-cat, empty->Unknown): {kappa_3cat_merged:.4f}")
    print(f"Fleiss' kappa (3-cat, empty excluded): {kappa_3cat_excl:.4f}")
    print(f"Mean answer agreement (P_i): {np.mean(ans_agreements):.4f} +/- {np.std(ans_agreements):.4f}")
    print(f"Mean process similarity (cosine): {np.mean(proc_similarities):.4f} +/- {np.std(proc_similarities):.4f}")
    print(f"Pearson r(agreement, similarity): {corr_pearson:.4f} (p={p_pearson:.2e})")
    print(f"Spearman rho: {corr_spearman:.4f} (p={p_spearman:.2e})")
    print(f"Same answer, different process (cosine<0.5): {global_sadp_ratio:.1%} ({total_sadp_pairs}/{total_sa_pairs} pairs)")


if __name__ == "__main__":
    main()
