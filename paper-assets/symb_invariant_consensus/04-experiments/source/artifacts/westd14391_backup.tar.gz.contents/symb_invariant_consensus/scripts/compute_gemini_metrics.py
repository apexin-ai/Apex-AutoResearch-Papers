"""Compute all metrics for Gemini 2.5 Pro (95-question interim): SC, SICA, BR, Process-kappa, Answer Fleiss' kappa."""
import json, os, glob, numpy as np
from collections import Counter
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

BASE = "/root/symb_invariant_consensus/results/exp_d135_frontier_scb/google_gemini-2.5-pro"
INTERMEDIATES_DIR = os.path.join(BASE, "intermediates")
CROSS_MODEL_RESULTS = os.path.join(BASE, "cross_model/cross_model_mistral.json")

def load_intermediates():
    files = sorted(glob.glob(os.path.join(INTERMEDIATES_DIR, "folio_*.json")),
                   key=lambda x: int(os.path.basename(x).replace("folio_","").replace(".json","")))
    data = []
    for f in files:
        with open(f) as fh:
            data.append(json.load(fh))
    return data

def load_cross_model():
    with open(CROSS_MODEL_RESULTS) as f:
        return json.load(f)

def compute_sc_accuracy(cross_results):
    correct = sum(1 for r in cross_results if r["sc_correct"])
    n = len(cross_results)
    return correct, n, correct / n if n else 0

def compute_fleiss_kappa_from_cross(cross_results):
    categories = ["True", "False", "Unknown"]
    cat2idx = {c: i for i, c in enumerate(categories)}
    ratings = np.zeros((len(cross_results), len(categories)), dtype=int)
    for qi, r in enumerate(cross_results):
        dist = r["sc_vote_distribution"]
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

def compute_process_kappa(intermediates, cross_ids):
    id_to_inter = {d["problem"]["id"]: d for d in intermediates}
    sims = []
    for pid in cross_ids:
        if pid not in id_to_inter:
            continue
        d = id_to_inter[pid]
        texts = [t["trace"] for t in d["sica_result"]["traces"]]
        sim = mean_pairwise_cosine(texts)
        sims.append(sim)
    return float(np.mean(sims)) if sims else float('nan')

def compute_sica_metrics(cross_results):
    n = len(cross_results)
    sica_correct = sum(1 for r in cross_results if r["cross_model_correct"])
    has_constraints = sum(1 for r in cross_results if r["constraints_stats"]["total_extracted"] > 0)
    return {
        "n": n,
        "sica_correct": sica_correct,
        "sica_acc": sica_correct / n if n else 0,
        "extraction_rate": has_constraints / n if n else 0,
    }

def compute_br(cross_results):
    br_values = []
    for r in cross_results:
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

def compute_weighted_br(cross_results):
    numerator = 0.0
    denominator = 0.0
    for r in cross_results:
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
    print("=== Gemini 2.5 Pro 95-question Interim Metrics ===\n")

    cross = load_cross_model()
    cross_results = cross["results"]
    n_cross = len(cross_results)
    print(f"Cross-model extraction results: {n_cross}")

    if n_cross < 95:
        print(f"WARNING: Only {n_cross}/95 extraction results available!")

    intermediates = load_intermediates()
    print(f"Intermediate files loaded: {len(intermediates)}")

    cross_ids = [r["problem_id"] for r in cross_results]

    sc_n, sc_total, sc_acc = compute_sc_accuracy(cross_results)
    print(f"\nSC@12 accuracy: {sc_acc:.4f} ({sc_n}/{sc_total})")

    fk = compute_fleiss_kappa_from_cross(cross_results)
    print(f"Answer Fleiss' kappa: {fk:.4f}")

    pk = compute_process_kappa(intermediates, cross_ids)
    print(f"Process-kappa (TF-IDF): {pk:.4f}")

    sica = compute_sica_metrics(cross_results)
    print(f"\nSICA accuracy: {sica['sica_acc']:.4f} ({sica['sica_correct']}/{sica['n']})")
    delta = (sica['sica_acc'] - sc_acc) * 100
    print(f"Delta (SICA-SC): {delta:+.2f}pp")
    print(f"Extraction rate: {sica['extraction_rate']:.4f}")

    br = compute_br(cross_results)
    wbr = compute_weighted_br(cross_results)
    print(f"\nMean BR: {br['mean_br']}")
    print(f"Median BR: {br['median_br']}")
    print(f"Weighted BR: {wbr}")
    print(f"n_br_finite: {br['n_finite']}")
    print(f"BR=inf: {br['n_inf']}")

    n_sica_wrong = sica['n'] - sica['sica_correct']

    print("\n" + "="*60)
    print(f"| {'Metric':<25} | {'Gemini-2.5-Pro':<16} | {'o3 (ref)':<12} |")
    print("|" + "-"*27 + "|" + "-"*18 + "|" + "-"*14 + "|")
    print(f"| {'SC accuracy':<25} | {sc_acc:.4f}           | 0.8265       |")
    print(f"| {'SICA accuracy':<25} | {sica['sica_acc']:.4f}           | 0.8265       |")
    print(f"| {'Delta (SICA-SC)':<25} | {delta:+.2f}pp          | +0.00pp      |")
    print(f"| {'Mean BR':<25} | {br['mean_br']}           | 1.6565       |")
    print(f"| {'Weighted BR':<25} | {wbr}           | 1.812        |")
    print(f"| {'n_br_finite':<25} | {br['n_finite']:<16} | 6            |")
    print(f"| {'BR=inf':<25} | {br['n_inf']:<16} | 28           |")
    print(f"| {'Process-kappa':<25} | {pk:.4f}           | 0.5964       |")
    print(f"| {'Answer Fleiss kappa':<25} | {fk:.4f}           | 0.9221       |")
    print("="*60)

    output = {
        "model": "google_gemini-2.5-pro",
        "dataset": "FOLIO-95 (interim)",
        "n_questions": sc_total,
        "extraction_model": cross.get("summary", {}).get("extraction_model", "/root/autodl-tmp/models/Mistral-7B-Instruct-v0.3"),
        "sc_accuracy": round(sc_acc, 4),
        "sica_accuracy": round(sica["sica_acc"], 4),
        "delta_pp": round(delta, 2),
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
    out_path = os.path.join(BASE, "cross_model/gemini_interim_95_metrics.json")
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w") as f:
        json.dump(output, f, indent=2)
    print(f"\nSaved to {out_path}")

if __name__ == "__main__":
    main()
