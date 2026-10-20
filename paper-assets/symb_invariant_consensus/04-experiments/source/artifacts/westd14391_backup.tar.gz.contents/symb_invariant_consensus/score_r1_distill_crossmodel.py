#!/usr/bin/env python3
"""Re-score R1-Distill-8B using cross-model (Mistral) extracted constraints from per_trace_constraints_v2/.

Computes: SC accuracy, SICA accuracy, Delta, BR, Process-kappa, Answer Fleiss' kappa.
"""
import json, os, glob, sys
import numpy as np
from collections import Counter
from pathlib import Path

sys.path.insert(0, '/root/symb_invariant_consensus')
from sica.z3_maxsat import ConstraintDeduplicator, MaxSATSolver
from sica.scorer import InvariantScorer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

RESULTS_DIR = Path("/root/symb_invariant_consensus/results/exp_r1_distill_8b_sica")
INTERMEDIATES_DIR = RESULTS_DIR / "intermediates"
CONSTRAINTS_V2_DIR = RESULTS_DIR / "per_trace_constraints_v2"

LOGIC_CANONICAL = {
    "true": "True", "yes": "True", "1": "True",
    "false": "False", "no": "False", "0": "False",
    "unknown": "Unknown", "uncertain": "Unknown", "undetermined": "Unknown",
}

def normalize_logic_answer(ans):
    s = ans.strip()
    if s.startswith("\\text{"):
        s = s[len("\\text{"):]
        if s.endswith("}"):
            s = s[:-1]
        s = s.strip()
    return LOGIC_CANONICAL.get(s.lower(), s)

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

def fleiss_kappa(ratings_matrix):
    """Compute Fleiss' kappa from an N x C matrix."""
    N, C = ratings_matrix.shape
    n = ratings_matrix.sum(axis=1)
    k = n[0]  # assume all subjects rated by same number
    P_i = (np.sum(ratings_matrix ** 2, axis=1) - k) / (k * (k - 1)) if k > 1 else np.zeros(N)
    P_bar = np.mean(P_i)
    p_j = np.sum(ratings_matrix, axis=0) / (N * k)
    P_e = np.sum(p_j ** 2)
    if P_e >= 1.0:
        return 1.0
    return float((P_bar - P_e) / (1 - P_e))

def main():
    deduplicator = ConstraintDeduplicator()
    solver = MaxSATSolver()
    scorer = InvariantScorer(alpha=0.5)

    # Find problems that have both intermediates and v2 constraints
    v2_files = sorted(CONSTRAINTS_V2_DIR.glob("folio_*.json"))
    print(f"Found {len(v2_files)} v2 constraint files")

    all_results = []
    sc_correct_count = 0
    sica_correct_count = 0
    total_constraints_extracted = 0
    total_unique_constraints = 0
    traces_with_constraints_count = 0
    total_traces_count = 0
    process_kappas = []
    answer_ratings = []  # for Fleiss' kappa

    for vi, v2_path in enumerate(v2_files):
        fname = v2_path.name
        inter_path = INTERMEDIATES_DIR / fname
        if not inter_path.exists():
            print(f"SKIP {fname}: no intermediates")
            continue

        with open(inter_path) as f:
            inter = json.load(f)
        with open(v2_path) as f:
            v2 = json.load(f)

        pid = inter["problem"]["id"]
        gold = normalize_logic_answer(inter["problem"]["answer"])
        traces = inter["sica_result"]["traces"]  # original traces with CoT + answer
        v2_per_trace = v2["per_trace"]

        # SC: majority vote from original trace answers
        answers = [normalize_logic_answer(t["answer"]) for t in traces if t.get("answer", "").strip()]
        if not answers:
            continue
        answer_counts = Counter(answers)
        sc_answer = answer_counts.most_common(1)[0][0]
        sc_correct = (sc_answer == gold)
        if sc_correct:
            sc_correct_count += 1

        # Build constraint lists from v2
        all_constraints = []
        for t in v2_per_trace:
            all_constraints.append(t.get("constraints", []))
            n_c = len(t.get("constraints", []))
            total_constraints_extracted += n_c
            total_traces_count += 1
            if n_c > 0:
                traces_with_constraints_count += 1

        # Z3 dedup
        unique = deduplicator.deduplicate(all_constraints)
        total_unique_constraints += len(unique)

        # MaxSAT
        maxsat_result = solver.solve(unique, timeout_ms=10000)

        # Score candidates (use original trace answers, not v2 answers)
        candidates_set = sorted(set(normalize_logic_answer(t["answer"]) for t in traces if t.get("answer", "").strip()))
        trace_dicts = [{"answer": normalize_logic_answer(t["answer"]), "trace_idx": t.get("trace_idx", i)} for i, t in enumerate(traces)]
        scores = scorer.score(maxsat_result, trace_dicts, candidates_set)
        sica_answer = scorer.select_answer(scores, answer_counts)
        sica_correct = (sica_answer == gold)
        if sica_correct:
            sica_correct_count += 1

        # Process-kappa (TF-IDF cosine)
        cot_texts = [t["trace"] for t in traces]
        pk = mean_pairwise_cosine(cot_texts)
        process_kappas.append(pk)

        # Answer Fleiss' kappa prep
        cats = ["True", "False", "Unknown"]
        cat2idx = {c: i for i, c in enumerate(cats)}
        row = np.zeros(len(cats), dtype=int)
        for a in answers:
            if a in cat2idx:
                row[cat2idx[a]] += 1
        if row.sum() > 0:
            answer_ratings.append(row)

        result = {
            "problem_id": pid,
            "ground_truth": gold,
            "sc_answer": sc_answer,
            "sc_correct": sc_correct,
            "sica_answer": sica_answer,
            "sica_correct": sica_correct,
            "sica_scores": {k: round(v, 4) for k, v in scores.items()},
            "answer_counts": dict(answer_counts),
            "constraints_stats": {
                "total_extracted": sum(len(t.get("constraints", [])) for t in v2_per_trace),
                "traces_with_constraints": sum(1 for t in v2_per_trace if t.get("constraints")),
                "unique_after_dedup": len(unique),
            },
            "maxsat_stats": {
                "satisfied": len(maxsat_result.satisfied),
                "excluded": len(maxsat_result.excluded),
                "total_weight": maxsat_result.total_weight,
                "solve_time_ms": maxsat_result.solve_time_ms,
            },
        }
        all_results.append(result)

        if (vi + 1) % 20 == 0 or vi == len(v2_files) - 1:
            n = len(all_results)
            print(f"[{vi+1}/{len(v2_files)}] SC={sc_correct_count}/{n}={sc_correct_count/n:.4f}  SICA={sica_correct_count}/{n}={sica_correct_count/n:.4f}")

    # Final metrics
    n = len(all_results)
    if n == 0:
        print("No results!")
        return

    sc_acc = sc_correct_count / n
    sica_acc = sica_correct_count / n
    delta_pp = (sica_acc - sc_acc) * 100

    # BR
    br_values = []
    for r in all_results:
        if r["sica_correct"]:
            continue
        gold = r["ground_truth"]
        sica_ans = r["sica_answer"]
        scores = r["sica_scores"]
        w_wrong = scores.get(sica_ans, 0.0)
        w_gold = scores.get(gold, 0.0)
        if w_gold > 0:
            br_values.append(w_wrong / w_gold)

    mean_br = round(float(np.mean(br_values)), 4) if br_values else None
    median_br = round(float(np.median(br_values)), 4) if br_values else None

    # Process-kappa
    pk_mean = round(float(np.mean(process_kappas)), 4)
    pk_std = round(float(np.std(process_kappas)), 4)

    # Answer Fleiss' kappa
    if answer_ratings:
        ratings_mat = np.array(answer_ratings)
        fk = round(fleiss_kappa(ratings_mat), 4)
    else:
        fk = None

    extraction_rate = traces_with_constraints_count / max(total_traces_count, 1)

    print("\n" + "=" * 70)
    print("R1-Distill-LLaMA-8B FOLIO — Cross-Model Extraction (Mistral-7B)")
    print("=" * 70)
    print(f"| {'Metric':<30} | {'Value':>15} |")
    print(f"|{'-'*32}|{'-'*17}|")
    print(f"| {'N problems':<30} | {n:>15} |")
    print(f"| {'SC accuracy':<30} | {sc_acc:>15.4f} |")
    print(f"| {'SICA accuracy':<30} | {sica_acc:>15.4f} |")
    print(f"| {'Delta (SICA-SC) pp':<30} | {f'{delta_pp:+.2f}':>15} |")
    print(f"| {'Extraction rate':<30} | {extraction_rate:>15.4f} |")
    print(f"| {'Total constraints':<30} | {total_constraints_extracted:>15} |")
    print(f"| {'Unique constraints':<30} | {total_unique_constraints:>15} |")
    n_sica_wrong = sum(1 for r in all_results if not r["sica_correct"])
    print(f"| {'SICA wrong count':<30} | {n_sica_wrong:>15} |")
    print(f"| {'Mean BR':<30} | {str(mean_br):>15} |")
    print(f"| {'Median BR':<30} | {str(median_br):>15} |")
    print(f"| {'BR sample size':<30} | {len(br_values):>15} |")
    print(f"| {'Process-kappa (TF-IDF cos)':<30} | {pk_mean:>15.4f} |")
    print(f"| {'Process-kappa std':<30} | {pk_std:>15.4f} |")
    print(f"| {'Answer Fleiss kappa':<30} | {str(fk):>15} |")

    output = {
        "model": "DeepSeek-R1-Distill-LLaMA-8B",
        "extraction": "cross-model (Mistral-7B-Instruct-v0.3)",
        "dataset": f"FOLIO-204 ({n} completed)",
        "n_problems": n,
        "sc_accuracy": round(sc_acc, 4),
        "sica_accuracy": round(sica_acc, 4),
        "delta_pp": round(delta_pp, 2),
        "extraction_rate": round(extraction_rate, 4),
        "total_constraints": total_constraints_extracted,
        "unique_constraints": total_unique_constraints,
        "n_sica_wrong": n_sica_wrong,
        "mean_br": mean_br,
        "median_br": median_br,
        "n_br_samples": len(br_values),
        "process_kappa_tfidf": pk_mean,
        "process_kappa_tfidf_std": pk_std,
        "answer_fleiss_kappa": fk,
        "results": all_results,
    }

    summary = {k: v for k, v in output.items() if k != "results"}

    out_path = RESULTS_DIR / "crossmodel_metrics.json"
    with open(out_path, "w") as f:
        json.dump(output, f, indent=2, default=str)
    print(f"\nSaved to {out_path}")

    summary_path = RESULTS_DIR / "crossmodel_summary.json"
    with open(summary_path, "w") as f:
        json.dump(summary, f, indent=2)
    print(f"Summary saved to {summary_path}")

if __name__ == "__main__":
    import logging
    logging.basicConfig(level=logging.WARNING)
    main()
