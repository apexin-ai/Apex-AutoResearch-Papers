#!/usr/bin/env python3
"""Compute BR (bias ratio) and Process-kappa for gpt-4o FOLIO-204."""
import json, os, glob
import numpy as np
from itertools import combinations
from collections import Counter
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

RESULTS_DIR = "/root/symb_invariant_consensus/results/e6_gpt4o_folio204"

def load_results():
    with open(os.path.join(RESULTS_DIR, "results.json")) as f:
        return json.load(f)

def load_traces(intermediates_dir):
    data = {}
    for fpath in sorted(glob.glob(os.path.join(intermediates_dir, "folio_*.json"))):
        with open(fpath) as f:
            d = json.load(f)
        qid = d["problem"]["id"]
        data[qid] = d["sica_result"]["traces"]
    return data

# ── BR computation ──
def compute_br(results):
    """BR = weight_supporting_wrong / weight_supporting_gold for SICA-wrong questions."""
    br_values = []
    per_q_br = []
    
    for r in results:
        if r["sica_correct"]:
            continue
        
        gold = r["ground_truth"]
        sica_ans = r["sica_answer"]
        scores = r["sica_scores"]
        
        weight_wrong = scores.get(sica_ans, 0.0)
        weight_gold = scores.get(gold, 0.0)
        
        if weight_gold > 0:
            br = weight_wrong / weight_gold
            br_values.append(br)
            per_q_br.append({
                "problem_id": r["problem_id"],
                "gold": gold,
                "sica_answer": sica_ans,
                "weight_wrong": weight_wrong,
                "weight_gold": weight_gold,
                "br": round(br, 4)
            })
        else:
            # gold answer has zero weight -> infinite bias
            per_q_br.append({
                "problem_id": r["problem_id"],
                "gold": gold,
                "sica_answer": sica_ans,
                "weight_wrong": weight_wrong,
                "weight_gold": weight_gold,
                "br": None  # undefined (infinite)
            })
    
    finite_br = [x for x in br_values if np.isfinite(x)]
    n_undefined = len(per_q_br) - len(finite_br)
    
    return {
        "mean_br": round(float(np.mean(finite_br)), 4) if finite_br else None,
        "median_br": round(float(np.median(finite_br)), 4) if finite_br else None,
        "std_br": round(float(np.std(finite_br)), 4) if finite_br else None,
        "n_finite": len(finite_br),
        "n_undefined_inf": n_undefined,
        "per_question_br": per_q_br,
    }

# ── Weighted BR: weight by question's total constraint weight ──
def compute_weighted_br(results):
    """Weighted BR: each question's BR weighted by total MaxSAT weight."""
    numerator = 0.0
    denominator = 0.0
    for r in results:
        if r["sica_correct"]:
            continue
        gold = r["ground_truth"]
        sica_ans = r["sica_answer"]
        scores = r["sica_scores"]
        weight_wrong = scores.get(sica_ans, 0.0)
        weight_gold = scores.get(gold, 0.0)
        total_w = r.get("maxsat_stats", {}).get("total_weight", 0)
        if weight_gold > 0 and total_w > 0:
            br = weight_wrong / weight_gold
            numerator += br * total_w
            denominator += total_w
    return round(numerator / denominator, 4) if denominator > 0 else None

# ── Process-kappa (TF-IDF cosine similarity) ──
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
    n = len(non_empty)
    sims = [sim_matrix[i, j] for i in range(n) for j in range(i + 1, n)]
    return float(np.mean(sims))

def compute_process_kappa(traces_data, qids):
    per_q_sim = []
    for qid in qids:
        traces = traces_data[qid]
        texts = [t["trace"] for t in traces]
        sim = mean_pairwise_cosine(texts)
        per_q_sim.append(sim)
    return {
        "mean": round(float(np.mean(per_q_sim)), 4),
        "std": round(float(np.std(per_q_sim)), 4),
        "median": round(float(np.median(per_q_sim)), 4),
    }

# ── Fleiss' kappa ──
def fleiss_kappa_from_results(results):
    categories = ["True", "False", "Unknown"]
    cat2idx = {c: i for i, c in enumerate(categories)}
    ratings = np.zeros((len(results), len(categories)), dtype=int)
    for qi, r in enumerate(results):
        dist = r.get("sc_vote_distribution", {})
        for ans, cnt in dist.items():
            ans_norm = ans.strip()
            if ans_norm in cat2idx:
                ratings[qi, cat2idx[ans_norm]] += cnt
            else:
                ratings[qi, cat2idx["Unknown"]] += cnt
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
    return float((P_bar - P_e) / (1 - P_e))


if __name__ == "__main__":
    data = load_results()
    results_list = data["results"]
    summary = data["summary"]
    
    print(f"Loaded {len(results_list)} questions")
    print(f"SC={summary['sc_accuracy']:.4f}, SICA={summary['sica_accuracy']:.4f}")
    
    # BR
    br_result = compute_br(results_list)
    weighted_br = compute_weighted_br(results_list)
    n_sica_wrong = sum(1 for r in results_list if not r["sica_correct"])
    print(f"\nSICA wrong: {n_sica_wrong}")
    print(f"BR (finite only): mean={br_result['mean_br']}, median={br_result['median_br']}, n_finite={br_result['n_finite']}, n_inf={br_result['n_undefined_inf']}")
    print(f"Weighted BR: {weighted_br}")
    
    # Process-kappa
    intermediates_dir = os.path.join(RESULTS_DIR, "intermediates")
    traces_data = load_traces(intermediates_dir)
    qids = sorted(traces_data.keys(), key=lambda x: int(x.split("_")[1]))
    print(f"\nLoaded traces for {len(qids)} questions")
    
    pk = compute_process_kappa(traces_data, qids)
    print(f"Process-κ (TF-IDF cosine): mean={pk['mean']}, std={pk['std']}, median={pk['median']}")
    
    # Fleiss' kappa
    fk = fleiss_kappa_from_results(results_list)
    print(f"Answer Fleiss' κ: {fk:.4f}")
    
    # Output
    output = {
        "model": "gpt-4o",
        "dataset": f"FOLIO-204 ({len(results_list)}/204 completed)",
        "sc_accuracy": round(summary["sc_accuracy"], 4),
        "sica_accuracy": round(summary["sica_accuracy"], 4),
        "delta_pp": round((summary["sica_accuracy"] - summary["sc_accuracy"]) * 100, 2),
        "n_sica_wrong": n_sica_wrong,
        "mean_br": br_result["mean_br"],
        "median_br": br_result["median_br"],
        "std_br": br_result["std_br"],
        "weighted_br": weighted_br,
        "n_br_finite": br_result["n_finite"],
        "n_br_undefined": br_result["n_undefined_inf"],
        "process_kappa_tfidf": pk["mean"],
        "process_kappa_tfidf_std": pk["std"],
        "process_kappa_tfidf_median": pk["median"],
        "answer_fleiss_kappa": round(fk, 4),
        "per_question_br": br_result["per_question_br"],
    }
    
    out_path = "/tmp/gpt4o_br_process_kappa.json"
    with open(out_path, "w") as f:
        json.dump(output, f, indent=2)
    print(f"\nSaved to {out_path}")
    print(json.dumps({k:v for k,v in output.items() if k != "per_question_br"}, indent=2))
