"""Compute all metrics for o3: SC, SICA, BR, Process-kappa, Answer Fleiss' kappa."""
import json, os, numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

BASE = "/root/symb_invariant_consensus/results/exp_d135_frontier_scb/o3"
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
    # o3 has 204 questions but only 196 valid (8 have all-empty traces)
    valid_pq = [q for q in pq if q["n_valid_answers"] > 0]
    correct = sum(1 for q in valid_pq if q["sc_correct"])
    return correct, len(valid_pq), correct / len(valid_pq)

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
    print("=== o3 FOLIO Full Metrics ===\n")
    frontier = load_frontier()

    sc_n, sc_total, sc_acc = compute_sc_accuracy(frontier)
    print(f"SC accuracy: {sc_acc:.4f} ({sc_n}/{sc_total})")

    fk = compute_fleiss_kappa(frontier)
    print(f"Answer Fleiss' kappa: {fk:.4f}")

    pk = compute_process_kappa(frontier)
    print(f"Process-kappa (TF-IDF): {pk:.4f}")

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

    n_sica_wrong = sica['n'] - sica['sica_correct']

    print("\n" + "="*55)
    print(f"| {'Metric':<25} | {'o3':<12} | {'gpt-5.5 (ref)':<14} |")
    print("|" + "-"*27 + "|" + "-"*14 + "|" + "-"*16 + "|")
    print(f"| {'SC accuracy':<25} | {sc_acc:.4f}       | 0.8431         |")
    print(f"| {'SICA accuracy':<25} | {sica['sica_acc']:.4f}       | 0.8480         |")
    print(f"| {'Delta (SICA-SC)':<25} | {(sica['sica_acc']-sc_acc)*100:+.2f}pp     | +0.49pp        |")
    print(f"| {'Mean BR':<25} | {br['mean_br']}       | 3.4806         |")
    print(f"| {'Median BR':<25} | {br['median_br']}       | 3.4935         |")
    print(f"| {'Weighted BR':<25} | {wbr}       | 3.5735         |")
    print(f"| {'n_br_finite':<25} | {br['n_finite']:<12} | 4              |")
    print(f"| {'BR=inf':<25} | {br['n_inf']:<12} | 27             |")
    print(f"| {'Extraction rate':<25} | {sica['extraction_rate']:.4f}       | 1.0000         |")
    print(f"| {'Process-kappa':<25} | {pk:.4f}       | 0.5625         |")
    print(f"| {'Answer Fleiss kappa':<25} | {fk:.4f}       | 0.9581         |")
    print("="*55)

    output = {
        "model": "o3",
        "dataset": "FOLIO-204",
        "n_total": 204,
        "n_valid": sc_total,
        "extraction_model": cross.get("summary", {}).get("extraction_model", "Mistral-7B"),
        "sc_accuracy": round(sc_acc, 4),
        "sica_accuracy": round(sica["sica_acc"], 4),
        "delta_pp": round((sica["sica_acc"] - sc_acc) * 100, 2),
        "extraction_rate": round(sica["extraction_rate"], 4),
        "n_sica_wrong": n_sica_wrong,
        "mean_br": br["mean_br"],
        "median_br": br["median_br"],
        "weighted_br": wbr,
        "n_br_finite": br["n_finite"],
        "n_br_inf": br["n_inf"],
        "process_kappa": round(pk, 4),
        "answer_fleiss_kappa": round(fk, 4),
    }
    out_path = os.path.join(BASE, "cross_model/o3_full_metrics.json")
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w") as f:
        json.dump(output, f, indent=2)
    print(f"\nSaved to {out_path}")

if __name__ == "__main__":
    main()
