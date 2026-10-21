"""Compute all 6 metrics for Gemini 2.5-pro interim (95 questions)."""
import json, os, glob, sys
import numpy as np
from collections import Counter
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

BASE = "/root/symb_invariant_consensus/results/exp_d135_frontier_scb/google_gemini-2.5-pro"
INTERMEDIATES = os.path.join(BASE, "intermediates")
CROSS_MODEL = os.path.join(BASE, "cross_model/cross_model_mistral.json")
OUTPUT = os.path.join(BASE, "cross_model/gemini_interim_95_metrics.json")


def load_intermediates():
    """Load all 95 intermediate files to get SC data."""
    files = sorted(glob.glob(os.path.join(INTERMEDIATES, "folio_*.json")))
    data = []
    for f in files:
        with open(f) as fh:
            d = json.load(fh)
        problem = d["problem"]
        sica = d["sica_result"]
        answers = [t["answer"] for t in sica["traces"]]
        dist = dict(Counter(answers))
        sc_answer = max(dist, key=dist.get)
        gt = problem["answer"]
        data.append({
            "problem_id": problem["id"],
            "ground_truth": gt,
            "traces": [t["trace"] for t in sica["traces"]],
            "answer_distribution": dist,
            "sc_answer": sc_answer,
            "sc_correct": sc_answer == gt,
        })
    return data


def load_cross_model():
    with open(CROSS_MODEL) as f:
        return json.load(f)


def compute_sc_accuracy(data):
    correct = sum(1 for q in data if q["sc_correct"])
    return correct, len(data), correct / len(data)


def compute_fleiss_kappa(data):
    categories = ["True", "False", "Unknown"]
    cat2idx = {c: i for i, c in enumerate(categories)}
    ratings = np.zeros((len(data), len(categories)), dtype=int)
    for qi, q in enumerate(data):
        for ans, cnt in q["answer_distribution"].items():
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


def compute_process_kappa(data):
    sims = []
    for q in data:
        sim = mean_pairwise_cosine(q["traces"])
        sims.append(sim)
    return float(np.mean(sims))


def compute_sica_metrics(cross_model, n_expected):
    results = cross_model["results"]
    assert len(results) == n_expected, f"Expected {n_expected} results, got {len(results)}"
    sica_correct = sum(1 for r in results if r["cross_model_correct"])
    has_constraints = sum(1 for r in results if r["constraints_stats"]["total_extracted"] > 0)
    return {
        "n": len(results),
        "sica_correct": sica_correct,
        "sica_acc": sica_correct / len(results),
        "extraction_rate": has_constraints / len(results),
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
    print("=== Gemini 2.5-pro Interim (95 questions) Full Metrics ===\n")

    data = load_intermediates()
    n = len(data)
    print(f"Loaded {n} questions from intermediates")

    sc_n, sc_total, sc_acc = compute_sc_accuracy(data)
    print(f"SC@12 accuracy: {sc_acc:.4f} ({sc_n}/{sc_total})")

    fk = compute_fleiss_kappa(data)
    print(f"Answer Fleiss' kappa: {fk:.4f}")

    pk = compute_process_kappa(data)
    print(f"Process-kappa (TF-IDF): {pk:.4f}")

    cross = load_cross_model()
    sica = compute_sica_metrics(cross, n)
    print(f"\nSICA accuracy: {sica['sica_acc']:.4f} ({sica['sica_correct']}/{sica['n']})")
    delta = (sica['sica_acc'] - sc_acc) * 100
    print(f"Delta (SICA-SC): {delta:+.2f}pp")
    print(f"Extraction rate: {sica['extraction_rate']:.4f}")

    br = compute_br(cross)
    wbr = compute_weighted_br(cross)
    print(f"\nMean BR: {br['mean_br']}")
    print(f"Median BR: {br['median_br']}")
    print(f"Weighted BR: {wbr}")
    print(f"n_br_finite: {br['n_finite']}")
    print(f"BR=inf: {br['n_inf']}")

    print("\n" + "=" * 70)
    print(f"| {'Metric':<25} | {'Gemini (n=95)':<16} | {'o3 (n=204)':<14} | {'gpt-5.5 (n=204)':<16} |")
    print("|" + "-"*27 + "|" + "-"*18 + "|" + "-"*16 + "|" + "-"*18 + "|")
    print(f"| {'SC accuracy':<25} | {sc_acc:<16.4f} | {'0.8265':<14} | {'0.8431':<16} |")
    print(f"| {'SICA accuracy':<25} | {sica['sica_acc']:<16.4f} | {'0.8265':<14} | {'0.8480':<16} |")
    print(f"| {'Delta (SICA-SC)':<25} | {delta:<+16.2f} | {'0.00pp':<14} | {'+0.49pp':<16} |")
    print(f"| {'Mean BR':<25} | {str(br['mean_br']):<16} | {'1.6565':<14} | {'3.4806':<16} |")
    print(f"| {'Median BR':<25} | {str(br['median_br']):<16} | {'1.2902':<14} | {'3.4935':<16} |")
    print(f"| {'Weighted BR':<25} | {str(wbr):<16} | {'1.8120':<14} | {'3.5735':<16} |")
    print(f"| {'n_br_finite':<25} | {br['n_finite']:<16} | {'6':<14} | {'4':<16} |")
    print(f"| {'BR=inf':<25} | {br['n_inf']:<16} | {'28':<14} | {'27':<16} |")
    print(f"| {'Extraction rate':<25} | {sica['extraction_rate']:<16.4f} | {'1.0000':<14} | {'1.0000':<16} |")
    print(f"| {'Process-kappa':<25} | {pk:<16.4f} | {'0.5964':<14} | {'0.5625':<16} |")
    print(f"| {'Answer Fleiss kappa':<25} | {fk:<16.4f} | {'0.9221':<14} | {'0.9581':<16} |")
    print("=" * 70)

    output = {
        "model": "gemini-2.5-pro",
        "dataset": "FOLIO-95-interim",
        "n_questions": n,
        "note": "95/204 interim results, not final",
        "extraction_model": "Mistral-7B-Instruct-v0.3",
        "sc_accuracy": round(sc_acc, 4),
        "sica_accuracy": round(sica["sica_acc"], 4),
        "delta_pp": round(delta, 2),
        "extraction_rate": round(sica["extraction_rate"], 4),
        "n_sica_wrong": sica["n"] - sica["sica_correct"],
        "mean_br": br["mean_br"],
        "median_br": br["median_br"],
        "weighted_br": wbr,
        "n_br_finite": br["n_finite"],
        "n_br_inf": br["n_inf"],
        "process_kappa": round(pk, 4),
        "answer_fleiss_kappa": round(fk, 4),
    }
    os.makedirs(os.path.dirname(OUTPUT), exist_ok=True)
    with open(OUTPUT, "w") as f:
        json.dump(output, f, indent=2)
    print(f"\nSaved to {OUTPUT}")


if __name__ == "__main__":
    main()
