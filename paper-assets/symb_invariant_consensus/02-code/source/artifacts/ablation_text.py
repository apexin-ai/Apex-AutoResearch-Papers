"""T_ext ablation: re-extract constraints at different temperatures from exp033 traces.
Uses existing Mistral-7B vLLM on ports 8001/8002.
"""
import json
import os
import sys
import time
import logging
from collections import Counter
from pathlib import Path
from scipy.stats import binomtest

sys.path.insert(0, "/root/symb_invariant_consensus")
from sica.constraint_extractor import ConstraintExtractor, VLLMBackend
from sica.z3_maxsat import ConstraintDeduplicator, MaxSATSolver
from sica.scorer import InvariantScorer
from sica.pipeline import normalize_logic_answer

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
logger = logging.getLogger(__name__)

INTERMEDIATES_DIR = "/root/symb_invariant_consensus/results/exp033_mistral_7b_folio204/intermediates"
EXP033_RESULTS = "/root/symb_invariant_consensus/results/exp033_mistral_7b_folio204/exp033_results.json"
OUTPUT_PATH = "/root/symb_invariant_consensus/results/text_ablation_results.json"
T_EXT_VALUES = [0.1, 0.3, 0.5, 0.7, 1.0]
VLLM_PORTS = [8001, 8002]
N_PROBLEMS = 204


def load_intermediates():
    problems = []
    for i in range(N_PROBLEMS):
        path = os.path.join(INTERMEDIATES_DIR, f"folio_{i}.json")
        with open(path) as f:
            data = json.load(f)
        problems.append(data)
    return problems


def get_sc_answer(traces):
    votes = Counter()
    for t in traces:
        ans = normalize_logic_answer(t.get("answer", ""))
        if ans:
            votes[ans] += 1
    if not votes:
        return "", {}
    winner = max(sorted(votes.keys()), key=lambda k: votes[k])
    return winner, dict(votes)


def check_correct(predicted, ground_truth):
    return normalize_logic_answer(predicted) == normalize_logic_answer(ground_truth)


def run_single_problem(problem_data, extractor, deduplicator, solver, scorer):
    traces = problem_data["sica_result"]["traces"]
    gt = problem_data["problem"]["answer"]
    trace_texts = [t["trace"] for t in traces]

    for t in traces:
        if t.get("answer"):
            t["answer"] = normalize_logic_answer(t["answer"])

    all_constraints = extractor.extract_batch(trace_texts)
    total_constraints = sum(len(c) for c in all_constraints)
    unique_constraints = deduplicator.deduplicate(all_constraints)
    maxsat_result = solver.solve(unique_constraints, timeout_ms=10000)

    candidates = sorted(set(t["answer"] for t in traces if t.get("answer")))
    answer_counts = Counter(t["answer"] for t in traces if t.get("answer"))
    scores = scorer.score(maxsat_result, traces, candidates)
    sica_answer = scorer.select_answer(scores, answer_counts)

    sc_answer, sc_votes = get_sc_answer(traces)

    return {
        "sica_answer": sica_answer,
        "sica_correct": check_correct(sica_answer, gt),
        "sc_answer": sc_answer,
        "sc_correct": check_correct(sc_answer, gt),
        "ground_truth": gt,
        "n_constraints_total": total_constraints,
        "n_constraints_unique": len(unique_constraints),
        "n_satisfied": len(maxsat_result.satisfied),
        "n_excluded": len(maxsat_result.excluded),
    }


def load_baseline_results():
    with open(EXP033_RESULTS) as f:
        data = json.load(f)
    per_problem = []
    for r in data["results"]:
        per_problem.append({
            "sica_answer": r["sica_answer"],
            "sica_correct": r["sica_correct"],
            "sc_answer": r["sc_answer"],
            "sc_correct": r["sc_correct"],
            "ground_truth": r["ground_truth"],
            "n_constraints_total": r["constraints_stats"]["total_extracted"],
            "n_constraints_unique": r["constraints_stats"]["unique_after_dedup"],
            "n_satisfied": r["maxsat_stats"]["satisfied"],
            "n_excluded": r["maxsat_stats"]["excluded"],
        })
    return per_problem


def compute_mcnemar(per_problem_results):
    b = 0  # SC correct, SICA wrong
    c = 0  # SC wrong, SICA correct
    for r in per_problem_results:
        sc_ok = r["sc_correct"]
        sica_ok = r["sica_correct"]
        if sc_ok and not sica_ok:
            b += 1
        elif not sc_ok and sica_ok:
            c += 1
    n_disc = b + c
    if n_disc == 0:
        return 1.0, b, c
    p_value = binomtest(min(b, c), n_disc, 0.5).pvalue
    return p_value, b, c


def run_ablation():
    logger.info("Loading intermediates...")
    problems = load_intermediates()
    logger.info("Loaded %d problems", len(problems))

    all_results = []

    for t_ext in T_EXT_VALUES:
        logger.info("=" * 60)
        logger.info("T_ext = %.1f", t_ext)
        logger.info("=" * 60)

        if t_ext == 0.3:
            logger.info("Using existing exp033 results for T_ext=0.3")
            per_problem = load_baseline_results()
        else:
            port = VLLM_PORTS[0]
            llm = VLLMBackend(
                base_url=f"http://localhost:{port}/v1",
                model=None,
                temperature=t_ext,
                max_tokens=2048,
            )
            extractor = ConstraintExtractor(llm=llm, domain="logic")
            deduplicator = ConstraintDeduplicator()
            solver = MaxSATSolver()
            scorer = InvariantScorer()

            per_problem = []
            t0 = time.time()
            for idx, prob_data in enumerate(problems):
                try:
                    result = run_single_problem(
                        prob_data, extractor, deduplicator, solver, scorer
                    )
                    per_problem.append(result)
                except Exception as e:
                    logger.error("Problem %d failed: %s", idx, e)
                    per_problem.append({
                        "sica_answer": "",
                        "sica_correct": False,
                        "sc_answer": "",
                        "sc_correct": False,
                        "ground_truth": prob_data["problem"]["answer"],
                        "n_constraints_total": 0,
                        "n_constraints_unique": 0,
                        "n_satisfied": 0,
                        "n_excluded": 0,
                    })

                if (idx + 1) % 20 == 0 or idx == 0:
                    elapsed = time.time() - t0
                    rate = (idx + 1) / elapsed
                    eta = (N_PROBLEMS - idx - 1) / rate
                    sica_so_far = sum(1 for r in per_problem if r["sica_correct"])
                    logger.info(
                        "[%d/%d] sica_acc=%.1f%% elapsed=%.0fs eta=%.0fs",
                        idx + 1, N_PROBLEMS,
                        100 * sica_so_far / len(per_problem),
                        elapsed, eta,
                    )

        sica_correct = sum(1 for r in per_problem if r["sica_correct"])
        sc_correct = sum(1 for r in per_problem if r["sc_correct"])
        n = len(per_problem)
        sica_acc = sica_correct / n
        sc_acc = sc_correct / n
        delta_pp = (sica_acc - sc_acc) * 100
        mcnemar_p, b, c = compute_mcnemar(per_problem)
        mean_constraints = sum(r["n_constraints_total"] for r in per_problem) / n

        entry = {
            "t_ext": t_ext,
            "sc_acc": round(sc_acc, 4),
            "sica_acc": round(sica_acc, 4),
            "delta_pp": round(delta_pp, 2),
            "mcnemar_p": round(mcnemar_p, 6),
            "mcnemar_b": b,
            "mcnemar_c": c,
            "n_constraints_mean": round(mean_constraints, 1),
            "sica_correct": sica_correct,
            "sc_correct": sc_correct,
            "n": n,
        }
        all_results.append(entry)
        logger.info(
            "T_ext=%.1f  SC=%.1f%%  SICA=%.1f%%  Δ=%.1fpp  p=%.4f  constraints_mean=%.1f",
            t_ext, sc_acc * 100, sica_acc * 100, delta_pp, mcnemar_p, mean_constraints,
        )

    output = {
        "metadata": {
            "experiment": "T_ext ablation (constraint extraction temperature)",
            "model": "Mistral-7B-Instruct-v0.3",
            "dataset": "FOLIO-204",
            "base_traces": "exp033 (T_sampling=0.7, K=12, seed=42)",
            "t_ext_values": T_EXT_VALUES,
            "timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        },
        "results": all_results,
    }

    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w") as f:
        json.dump(output, f, indent=2)
    logger.info("Results saved to %s", OUTPUT_PATH)

    print("\n" + "=" * 70)
    print("T_ext ABLATION RESULTS")
    print("=" * 70)
    print(f"{'T_ext':>6} {'SC%':>6} {'SICA%':>7} {'Δpp':>6} {'p-val':>8} {'#constr':>8}")
    print("-" * 70)
    for r in all_results:
        print(
            f"{r['t_ext']:6.1f} {r['sc_acc']*100:6.1f} {r['sica_acc']*100:7.1f} "
            f"{r['delta_pp']:+6.1f} {r['mcnemar_p']:8.4f} {r['n_constraints_mean']:8.1f}"
        )
    print("=" * 70)


if __name__ == "__main__":
    run_ablation()
