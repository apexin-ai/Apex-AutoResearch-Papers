"""Compute all metrics for gpt-5.5: SC, SICA, BR, Process-kappa, Answer Fleiss' kappa."""
import json, os, sys, numpy as np
from collections import Counter
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

BASE = "/root/symb_invariant_consensus/results/exp_d135_frontier_scb/gpt-5.5"
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
    has_constraints = sum(1 for r in results if r["constraints_stats"]["total_extracted"] > 0)
    return {
        "n": n,
        "sica_correct": sica_correct,
        "sica_acc": sica_correct / n if n else 0,
        "extraction_rate": has_constraints / n if n else 0,
    }

def compute_br(cross_model):
    results = cross_model["results"]
    br_values = []
    for r in results:
        if r["cross_model_correct"]:
            continue
        gold = r["ground_truth"]
        sica_ans = r["cross_model_answer"]
        scores = r["cross_model_scores"]
        weight_wrong = scores.get(sica_ans, 0.0)
        weight_gold = scores.get(gold, 0.0)
        if weight_gold > 0:
            br_values.append(weight_wrong / weight_gold)
        else:
            br_values.append(float('inf'))
    n_finite = sum(1 for v in br_values if v != float('inf'))
    n_inf = sum(1 for v in br_values if v == float('inf'))
    finite_vals = [v for v in br_values if v != float('inf')]
    return {
        "mean_br": round(np.mean(finite_vals), 4) if finite_vals else None,
        "median_br": round(np.median(finite_vals), 4) if finite_vals else None,
        "n_finite": n_finite,
        "n_inf": n_inf,
        "all_br": br_values,
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
    print("=== gpt-5.5 FOLIO-204 Full Metrics ===\n")
    frontier = load_frontier()

    sc_n, sc_total, sc_acc = compute_sc_accuracy(frontier)
    print(f"SC@12 accuracy: {sc_acc:.4f} ({sc_n}/{sc_total})")

    fk = compute_fleiss_kappa(frontier)
    print(f"Answer Fleiss' kappa: {fk:.4f}")

    pk = compute_process_kappa(frontier)
    print(f"Process-kappa (TF-IDF): {pk:.4f}")

    if not os.path.exists(CROSS_MODEL_RESULTS):
        print(f"\nCross-model results not found: {CROSS_MODEL_RESULTS}")
        return

    cross = load_cross_model()
    sica = compute_sica_metrics(cross)
    print(f"\nSICA accuracy: {sica['sica_acc']:.4f} ({sica['sica_correct']}/{sica['n']})")
    print(f"Delta (SICA-SC): {(sica['sica_acc'] - sc_acc)*100:+.2f}pp")
    print(f"Extraction rate: {sica['extraction_rate']:.4f}")

    br = compute_br(cross)
    wbr = compute_weighted_br(cross)
    print(f"\nMean BR: {br['mean_br']}")
    print(f"Median BR: {br['median_br']}")
    print(f"Weighted BR: {wbr}")
    print(f"n_br_finite: {br['n_finite']}")
    print(f"BR=inf: {br['n_inf']}")

    print("\n" + "="*50)
    print("| Metric                  | gpt-5.5          | gpt-4.1 (ref)   |")
    print("|" + "-"*25 + "|" + "-"*18 + "|" + "-"*17 + "|")
    print(f"| SC accuracy             | {sc_acc:.4f}           | 0.8284          |")
    print(f"| SICA accuracy           | {sica['sica_acc']:.4f}           | 0.8137          |")
    print(f"| Delta (SICA-SC)         | {(sica['sica_acc']-sc_acc)*100:+.2f}pp          | -1.47pp         |")
    print(f"| Mean BR                 | {br['mean_br']}           | 2.70            |")
    print(f"| Median BR               | {br['median_br']}           | 1.53            |")
    print(f"| Weighted BR             | {wbr}           | 3.21            |")
    print(f"| n_br_finite             | {br['n_finite']}                | 16              |")
    print(f"| BR=inf                  | {br['n_inf']}                | 22              |")
    print(f"| extraction_rate         | {sica['extraction_rate']:.4f}           | 1.0000          |")
    print(f"| Process-kappa           | {pk:.4f}           | 0.792           |")
    print(f"| Answer Fleiss' kappa    | {fk:.4f}           | 0.862           |")
    print("="*50)

    output = {
        "model": "gpt-5.5",
        "dataset": "FOLIO-204",
        "extraction_model": cross.get("summary", {}).get("extraction_model", "Mistral-7B"),
        "completed": sc_total,
        "sc_accuracy": round(sc_acc, 4),
        "sica_accuracy": round(sica["sica_acc"], 4),
        "delta_pp": round((sica["sica_acc"] - sc_acc) * 100, 2),
        "extraction_rate": round(sica["extraction_rate"], 4),
        "mean_br": br["mean_br"],
        "median_br": br["median_br"],
        "weighted_br": wbr,
        "n_br_finite": br["n_finite"],
        "n_br_inf": br["n_inf"],
        "process_kappa": round(pk, 4),
        "answer_fleiss_kappa": round(fk, 4),
    }
    out_path = os.path.join(BASE, "cross_model/gpt55_full_metrics.json")
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w") as f:
        json.dump(output, f, indent=2)
    print(f"\nSaved to {out_path}")

if __name__ == "__main__":
    main()
