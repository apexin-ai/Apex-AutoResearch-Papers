"""Compute all metrics for gpt-4.1: SC, SICA, BR, Process-kappa, Answer Fleiss' kappa."""
import json, os, sys, glob
import numpy as np
from collections import Counter
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

BASE = "/root/symb_invariant_consensus/results/exp_d135_frontier_scb/gpt-4.1"
FRONTIER_RESULTS = os.path.join(BASE, "results.json")
CROSS_MODEL_RESULTS = os.path.join(BASE, "cross_model/cross_model_mistral.json")

def load_frontier():
    with open(FRONTIER_RESULTS) as f:
        return json.load(f)

def load_cross_model():
    with open(CROSS_MODEL_RESULTS) as f:
        return json.load(f)

def compute_sc_accuracy(frontier):
    pq = frontier["per_question"]
    correct = sum(1 for q in pq if q["sc_correct"])
    return correct, len(pq), correct / len(pq)

def compute_fleiss_kappa(frontier):
    pq = frontier["per_question"]
    categories = ["True", "False", "Unknown"]
    cat2idx = {c: i for i, c in enumerate(categories)}
    ratings = np.zeros((len(pq), len(categories)), dtype=int)
    for qi, q in enumerate(pq):
        dist = q["answer_distribution"]
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

def compute_process_kappa(frontier):
    pq = frontier["per_question"]
    sims = []
    for q in pq:
        texts = [t["trace"] for t in q["traces"]]
        sim = mean_pairwise_cosine(texts)
        sims.append(sim)
    return float(np.mean(sims))

def compute_sica_metrics(cross_model):
    results = cross_model["results"]
    n = len(results)
    sica_correct = sum(1 for r in results if r["cross_model_correct"])
    sc_correct = sum(1 for r in results if r["sc_correct"])
    
    # Extraction rate: problems with at least 1 constraint
    has_constraints = sum(1 for r in results if r["constraints_stats"]["total_extracted"] > 0)
    
    return {
        "n": n,
        "sica_correct": sica_correct,
        "sica_acc": sica_correct / n if n else 0,
        "sc_correct_crosscheck": sc_correct,
        "sc_acc_crosscheck": sc_correct / n if n else 0,
        "extraction_rate": has_constraints / n if n else 0,
    }

def compute_br(cross_model):
    results = cross_model["results"]
    br_values = []
    per_q = []
    
    for r in results:
        if r["cross_model_correct"]:
            continue
        
        gold = r["ground_truth"]
        sica_ans = r["cross_model_answer"]
        scores = r["cross_model_scores"]
        
        weight_wrong = scores.get(sica_ans, 0.0)
        weight_gold = scores.get(gold, 0.0)
        
        if weight_gold > 0:
            br = weight_wrong / weight_gold
            br_values.append(br)
            per_q.append({"pid": r["problem_id"], "br": round(br, 4), "w_wrong": weight_wrong, "w_gold": weight_gold})
        else:
            per_q.append({"pid": r["problem_id"], "br": None, "w_wrong": weight_wrong, "w_gold": weight_gold})
    
    finite_br = [x for x in br_values if np.isfinite(x)]
    n_inf = len(per_q) - len(finite_br)
    
    return {
        "mean_br": round(float(np.mean(finite_br)), 4) if finite_br else None,
        "median_br": round(float(np.median(finite_br)), 4) if finite_br else None,
        "n_finite": len(finite_br),
        "n_inf": n_inf,
        "per_q": per_q,
    }

def compute_weighted_br(cross_model):
    results = cross_model["results"]
    numerator = 0.0
    denominator = 0.0
    for r in results:
        if r["cross_model_correct"]:
            continue
        gold = r["ground_truth"]
        sica_ans = r["cross_model_answer"]
        scores = r["cross_model_scores"]
        weight_wrong = scores.get(sica_ans, 0.0)
        weight_gold = scores.get(gold, 0.0)
        total_w = r.get("maxsat_stats", {}).get("total_weight", 0)
        if weight_gold > 0 and total_w > 0:
            br = weight_wrong / weight_gold
            numerator += br * total_w
            denominator += total_w
    return round(numerator / denominator, 4) if denominator > 0 else None

def main():
    print("=== gpt-4.1 FOLIO-204 Full Metrics ===\n")
    
    # Load frontier data (always available)
    frontier = load_frontier()
    
    # SC accuracy
    sc_n, sc_total, sc_acc = compute_sc_accuracy(frontier)
    print(f"SC@12 accuracy: {sc_acc:.4f} ({sc_n}/{sc_total})")
    
    # Answer Fleiss' kappa
    fk = compute_fleiss_kappa(frontier)
    print(f"Answer Fleiss' κ: {fk:.4f}")
    
    # Process-kappa
    pk = compute_process_kappa(frontier)
    print(f"Process-κ (TF-IDF): {pk:.4f}")
    
    # SICA + BR (need cross-model results)
    if not os.path.exists(CROSS_MODEL_RESULTS):
        print(f"\nCross-model results not found: {CROSS_MODEL_RESULTS}")
        print("Run cross_model_extract.py first.")
        return
    
    cross = load_cross_model()
    sica = compute_sica_metrics(cross)
    print(f"\nSICA accuracy: {sica['sica_acc']:.4f} ({sica['sica_correct']}/{sica['n']})")
    print(f"Δ (SICA-SC): {(sica['sica_acc'] - sc_acc)*100:+.2f}pp")
    print(f"Extraction rate: {sica['extraction_rate']:.4f}")
    
    n_sica_wrong = sica['n'] - sica['sica_correct']
    print(f"SICA wrong: {n_sica_wrong}")
    
    br = compute_br(cross)
    wbr = compute_weighted_br(cross)
    print(f"\nMean BR: {br['mean_br']}")
    print(f"Median BR: {br['median_br']}")
    print(f"Weighted BR: {wbr}")
    print(f"BR=∞ count: {br['n_inf']}")
    
    # Summary table
    print("\n" + "="*50)
    print("| Metric                  | Value            |")
    print("|" + "-"*25 + "|" + "-"*18 + "|")
    print(f"| Completed               | {sc_total}/204           |")
    print(f"| SC accuracy             | {sc_acc:.4f}           |")
    print(f"| SICA accuracy           | {sica['sica_acc']:.4f}           |")
    print(f"| Δ (SICA-SC)             | {(sica['sica_acc']-sc_acc)*100:+.2f}pp          |")
    print(f"| Extraction rate         | {sica['extraction_rate']:.4f}           |")
    print(f"| SICA wrong count        | {n_sica_wrong}                |")
    print(f"| Mean BR                 | {br['mean_br']}           |")
    print(f"| Median BR               | {br['median_br']}           |")
    print(f"| Weighted BR             | {wbr}           |")
    print(f"| BR=∞ count              | {br['n_inf']}                |")
    print(f"| Process-κ (TF-IDF)      | {pk:.4f}           |")
    print(f"| Answer Fleiss' κ        | {fk:.4f}           |")
    print("="*50)
    
    # Save to file
    output = {
        "model": "gpt-4.1",
        "dataset": "FOLIO-204",
        "extraction_model": cross.get("summary", {}).get("extraction_model", "Mistral-7B"),
        "completed": sc_total,
        "sc_accuracy": round(sc_acc, 4),
        "sica_accuracy": round(sica["sica_acc"], 4),
        "delta_pp": round((sica["sica_acc"] - sc_acc) * 100, 2),
        "extraction_rate": round(sica["extraction_rate"], 4),
        "n_sica_wrong": n_sica_wrong,
        "mean_br": br["mean_br"],
        "median_br": br["median_br"],
        "weighted_br": wbr,
        "n_br_inf": br["n_inf"],
        "process_kappa": round(pk, 4),
        "answer_fleiss_kappa": round(fk, 4),
    }
    out_path = os.path.join(BASE, "cross_model/gpt41_full_metrics.json")
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w") as f:
        json.dump(output, f, indent=2)
    print(f"\nSaved to {out_path}")

if __name__ == "__main__":
    main()
