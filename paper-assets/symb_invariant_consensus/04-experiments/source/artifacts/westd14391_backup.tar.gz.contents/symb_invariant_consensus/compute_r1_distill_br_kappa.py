#!/usr/bin/env python3
"""Compute BR, Process-kappa, Fleiss' kappa for R1-Distill-8B FOLIO-204."""
import json, os, glob, sys
import numpy as np
from collections import Counter
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

RESULTS_DIR = "/root/symb_invariant_consensus/results/exp_r1_distill_8b_sica"

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

def compute_br(results):
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
            per_q_br.append({"problem_id": r["problem_id"], "gold": gold, "sica_answer": sica_ans,
                             "weight_wrong": weight_wrong, "weight_gold": weight_gold, "br": round(br, 4)})
        else:
            per_q_br.append({"problem_id": r["problem_id"], "gold": gold, "sica_answer": sica_ans,
                             "weight_wrong": weight_wrong, "weight_gold": weight_gold, "br": None})
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

def compute_weighted_br(results):
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

def fleiss_kappa_from_traces(traces_data, qids):
    categories = ["True", "False", "Unknown"]
    cat2idx = {c: i for i, c in enumerate(categories)}
    ratings = np.zeros((len(qids), len(categories)), dtype=int)
    for qi, qid in enumerate(qids):
        for trace in traces_data[qid]:
            ans = trace.get("answer", "").strip()
            if ans in cat2idx:
                ratings[qi, cat2idx[ans]] += 1
            elif ans:
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
    return float((P_bar - P_e) / (1 - P_e))

if __name__ == "__main__":
    data = load_results()
    results_list = data["results"]
    summary = data["summary"]

    n = len(results_list)
    print(f"Loaded {n} questions")
    print(f"SC={summary['sc_accuracy']:.4f}, SICA={summary['sica_accuracy']:.4f}")
    print(f"Delta (SICA-SC) = {(summary['sica_accuracy'] - summary['sc_accuracy'])*100:+.2f}pp")
    print(f"Extraction rate: {summary.get('extraction_rate', 0):.4f}")
    print(f"Total constraints: {summary.get('total_constraints_extracted', 0)}, Unique: {summary.get('total_unique_constraints', 0)}")

    br_result = compute_br(results_list)
    weighted_br = compute_weighted_br(results_list)
    n_sica_wrong = sum(1 for r in results_list if not r["sica_correct"])
    print(f"\nSICA wrong: {n_sica_wrong}")
    print(f"BR (finite only): mean={br_result['mean_br']}, median={br_result['median_br']}, n_finite={br_result['n_finite']}, n_inf={br_result['n_undefined_inf']}")
    print(f"Weighted BR: {weighted_br}")

    intermediates_dir = os.path.join(RESULTS_DIR, "intermediates")
    traces_data = load_traces(intermediates_dir)
    qids = sorted(traces_data.keys(), key=lambda x: int(x.split("_")[1]))
    print(f"\nLoaded traces for {len(qids)} questions")

    pk = compute_process_kappa(traces_data, qids)
    print(f"Process-kappa (TF-IDF cosine): mean={pk['mean']}, std={pk['std']}, median={pk['median']}")

    fk = fleiss_kappa_from_traces(traces_data, qids)
    print(f"Answer Fleiss' kappa: {fk:.4f}")

    empty_answers = 0
    total_traces = 0
    for qid in qids:
        for t in traces_data[qid]:
            total_traces += 1
            if not t.get("answer", "").strip():
                empty_answers += 1
    print(f"\nEmpty answers: {empty_answers}/{total_traces} ({empty_answers/total_traces*100:.1f}%)")

    print("\n" + "="*60)
    print("FULL METRICS TABLE: R1-Distill-LLaMA-8B on FOLIO-204")
    print("="*60)
    print(f"| {'Metric':<25} | {'Value':>15} |")
    print(f"|{'-'*27}|{'-'*17}|")
    print(f"| {'Completed questions':<25} | {f'{n}/204':>15} |")
    print(f"| {'SC accuracy':<25} | {summary['sc_accuracy']:>15.4f} |")
    print(f"| {'SICA accuracy':<25} | {summary['sica_accuracy']:>15.4f} |")
    delta = (summary['sica_accuracy'] - summary['sc_accuracy']) * 100
    print(f"| {'Delta (SICA-SC) pp':<25} | {f'{delta:+.2f}':>15} |")
    print(f"| {'SICA wrong count':<25} | {n_sica_wrong:>15} |")
    print(f"| {'Extraction rate':<25} | {summary.get('extraction_rate',0):>15.4f} |")
    print(f"| {'Mean BR':<25} | {str(br_result['mean_br']):>15} |")
    print(f"| {'Median BR':<25} | {str(br_result['median_br']):>15} |")
    print(f"| {'Weighted BR':<25} | {str(weighted_br):>15} |")
    print(f"| {'BR=inf count':<25} | {br_result['n_undefined_inf']:>15} |")
    print(f"| {'Process-kappa (TF-IDF)':<25} | {pk['mean']:>15.4f} |")
    print(f"| {'Answer Fleiss kappa':<25} | {fk:>15.4f} |")
    print(f"| {'Empty answer rate':<25} | {f'{empty_answers/total_traces*100:.1f}%':>15} |")

    output = {
        "model": "DeepSeek-R1-Distill-LLaMA-8B",
        "dataset": f"FOLIO-204 ({n}/204 completed)",
        "sc_accuracy": round(summary["sc_accuracy"], 4),
        "sica_accuracy": round(summary["sica_accuracy"], 4),
        "delta_pp": round(delta, 2),
        "n_sica_wrong": n_sica_wrong,
        "extraction_rate": round(summary.get("extraction_rate", 0), 4),
        "mean_br": br_result["mean_br"],
        "median_br": br_result["median_br"],
        "weighted_br": weighted_br,
        "n_br_finite": br_result["n_finite"],
        "n_br_undefined": br_result["n_undefined_inf"],
        "process_kappa_tfidf": pk["mean"],
        "process_kappa_tfidf_std": pk["std"],
        "answer_fleiss_kappa": round(fk, 4),
        "empty_answer_rate": round(empty_answers / total_traces, 4),
    }

    out_path = os.path.join(RESULTS_DIR, "br_kappa_metrics.json")
    with open(out_path, "w") as f:
        json.dump(output, f, indent=2)
    print(f"\nSaved to {out_path}")
