"""
Z3 Feedback Refinement experiment on FOLIO 204.
Loads pre-computed traces and constraints, applies Z3 UNSAT core feedback
refinement, then re-runs dedup + MAX-SAT + scoring.
Compares z3fb_sica_accuracy vs vanilla_sica_accuracy vs sc_accuracy.
"""
from __future__ import annotations

import argparse
import json
import logging
import os
import sys
import time
from collections import Counter

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from sica.z3_feedback import Z3FeedbackRefiner
from sica.z3_maxsat import ConstraintDeduplicator, MaxSATSolver
from sica.scorer import InvariantScorer

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s",
    handlers=[logging.StreamHandler(sys.stdout)],
)
logger = logging.getLogger(__name__)


def normalize_logic_answer(ans: str) -> str:
    ans = str(ans).strip().lower()
    if ans in ('true', 'yes', 't'):
        return 'True'
    elif ans in ('false', 'no', 'f'):
        return 'False'
    elif ans in ('unknown', 'uncertain', 'u', 'undetermined'):
        return 'Unknown'
    return ans.capitalize()


def load_problem_data(traces_dir: str) -> tuple[dict, list[dict]]:
    """Load results summary and per-problem data (traces + constraints)."""
    results_file = os.path.join(traces_dir, 'folio_204_results.json')
    with open(results_file) as f:
        results_data = json.load(f)

    problems = []
    for r in results_data['results']:
        pid = r['problem_id']

        intermed_file = os.path.join(traces_dir, 'intermediates', f'{pid}.json')
        with open(intermed_file) as f:
            intermed = json.load(f)

        constraints_file = os.path.join(traces_dir, 'per_trace_constraints', f'{pid}.json')
        with open(constraints_file) as f:
            constraint_data = json.load(f)

        trace_texts = {}
        for t in intermed['sica_result']['traces']:
            trace_texts[t['trace_idx']] = t['trace']

        per_trace = []
        for ct in constraint_data['per_trace']:
            per_trace.append({
                'trace_idx': ct['trace_idx'],
                'answer': normalize_logic_answer(ct['answer']),
                'constraints': ct.get('constraints', []),
                'trace_text': trace_texts.get(ct['trace_idx'], ''),
            })

        problems.append({
            'problem_id': pid,
            'problem_idx': r['problem_idx'],
            'problem_text': r['problem'],
            'ground_truth': normalize_logic_answer(r['ground_truth']),
            'vanilla_sica_answer': normalize_logic_answer(r['sica_answer']),
            'vanilla_sica_correct': r['sica_correct'],
            'sc_answer': normalize_logic_answer(r['sc_answer']),
            'sc_correct': r['sc_correct'],
            'per_trace': per_trace,
        })

    return results_data['summary'], problems


def run_sica_scoring(per_trace: list[dict], dedup: ConstraintDeduplicator,
                     solver: MaxSATSolver, scorer: InvariantScorer) -> dict:
    """Run dedup + MAX-SAT + scoring on a set of per-trace constraints."""
    all_constraints = [t.get('constraints', []) for t in per_trace]
    unique = dedup.deduplicate(all_constraints)
    maxsat_result = solver.solve(unique, timeout_ms=10000)

    answers = [t['answer'] for t in per_trace]
    candidates = sorted(set(a for a in answers if a))
    answer_counts = Counter(answers)

    traces_for_scoring = [
        {'answer': t['answer'], 'trace_idx': t['trace_idx']}
        for t in per_trace
    ]

    scores = scorer.score(maxsat_result, traces_for_scoring, candidates)
    selected = scorer.select_answer(scores, answer_counts)

    return {
        'answer': selected,
        'scores': scores,
        'answer_counts': dict(answer_counts),
        'unique_constraints': len(unique),
        'satisfied': len(maxsat_result.satisfied),
        'excluded': len(maxsat_result.excluded),
        'total_weight': maxsat_result.total_weight,
    }


def main():
    parser = argparse.ArgumentParser(description='Z3 Feedback Refinement on FOLIO 204')
    parser.add_argument('--api-base', default='http://localhost:8000/v1')
    parser.add_argument('--model', default='Qwen2.5-14B-Instruct')
    parser.add_argument('--traces-dir', default='results/folio_204_14b/')
    parser.add_argument('--max-rounds', type=int, default=3)
    parser.add_argument('--output-dir', default='results/z3_feedback_folio204')
    parser.add_argument('--K', type=int, default=12)
    parser.add_argument('--T-ext', type=float, default=0.3,
                        help='Temperature for refinement LLM calls')
    args = parser.parse_args()

    os.makedirs(args.output_dir, exist_ok=True)

    logger.info("Loading problem data from %s", args.traces_dir)
    summary, problems = load_problem_data(args.traces_dir)
    logger.info("Loaded %d problems (vanilla SICA=%.3f, SC=%.3f)",
                len(problems), summary['sica_accuracy'], summary['sc_accuracy'])

    refiner = Z3FeedbackRefiner(
        api_base=args.api_base,
        model=args.model,
        max_rounds=args.max_rounds,
        temperature=args.T_ext,
    )
    dedup = ConstraintDeduplicator()
    solver = MaxSATSolver()
    scorer = InvariantScorer()

    results = []
    z3fb_correct = 0
    t_start = time.time()

    for i, prob in enumerate(problems):
        t0 = time.time()

        refined = refiner.refine_problem(prob['per_trace'], prob['problem_text'])
        scoring = run_sica_scoring(refined['per_trace'], dedup, solver, scorer)

        z3fb_answer = scoring['answer']
        z3fb_is_correct = (z3fb_answer == prob['ground_truth'])
        if z3fb_is_correct:
            z3fb_correct += 1

        elapsed = time.time() - t0
        result = {
            'problem_id': prob['problem_id'],
            'problem_idx': prob['problem_idx'],
            'ground_truth': prob['ground_truth'],
            'z3fb_answer': z3fb_answer,
            'z3fb_correct': z3fb_is_correct,
            'z3fb_scores': scoring['scores'],
            'vanilla_sica_answer': prob['vanilla_sica_answer'],
            'vanilla_sica_correct': prob['vanilla_sica_correct'],
            'sc_answer': prob['sc_answer'],
            'sc_correct': prob['sc_correct'],
            'refinement_stats': refined['problem_stats'],
            'constraints_stats': {
                'total_original': sum(len(t.get('constraints', []))
                                      for t in prob['per_trace']),
                'total_after_refinement': sum(
                    len(t.get('constraints', []))
                    for t in refined['per_trace']),
                'unique_after_dedup': scoring['unique_constraints'],
            },
            'maxsat_stats': {
                'satisfied': scoring['satisfied'],
                'excluded': scoring['excluded'],
                'total_weight': scoring['total_weight'],
            },
            'time_s': round(elapsed, 2),
        }
        results.append(result)

        # Save intermediate per-problem result
        per_prob_file = os.path.join(args.output_dir, f"{prob['problem_id']}.json")
        with open(per_prob_file, 'w') as f:
            json.dump(result, f, indent=2, ensure_ascii=False)

        if (i + 1) % 10 == 0 or (i + 1) == len(problems):
            total_elapsed = time.time() - t_start
            rate = (i + 1) / total_elapsed
            eta = (len(problems) - i - 1) / rate if rate > 0 else 0
            z3fb_acc = z3fb_correct / (i + 1)
            unsat_traces = refiner.stats.traces_initially_unsat
            resolved = refiner.stats.traces_resolved
            logger.info(
                "[%d/%d] z3fb_acc=%.3f  unsat_traces=%d  resolved=%d  "
                "rate=%.1f prob/s  ETA=%.0fs",
                i + 1, len(problems), z3fb_acc, unsat_traces, resolved, rate, eta,
            )

    # Final summary
    n = len(problems)
    z3fb_acc = z3fb_correct / n
    vanilla_correct = sum(1 for r in results if r['vanilla_sica_correct'])
    sc_correct_count = sum(1 for r in results if r['sc_correct'])

    z3fb_gains = [r['problem_id'] for r in results
                  if r['z3fb_correct'] and not r['vanilla_sica_correct']]
    z3fb_losses = [r['problem_id'] for r in results
                   if not r['z3fb_correct'] and r['vanilla_sica_correct']]

    output = {
        'summary': {
            'n_problems': n,
            'z3fb_sica_accuracy': z3fb_acc,
            'vanilla_sica_accuracy': vanilla_correct / n,
            'sc_accuracy': sc_correct_count / n,
            'z3fb_correct': z3fb_correct,
            'vanilla_sica_correct': vanilla_correct,
            'sc_correct': sc_correct_count,
            'z3fb_vs_vanilla': {
                'gains': len(z3fb_gains),
                'losses': len(z3fb_losses),
                'net': len(z3fb_gains) - len(z3fb_losses),
                'gain_ids': z3fb_gains,
                'loss_ids': z3fb_losses,
            },
            'refinement_global_stats': refiner.stats.to_dict(),
            'config': {
                'model': args.model,
                'max_rounds': args.max_rounds,
                'temperature': args.T_ext,
                'K': args.K,
            },
            'total_wall_time_s': round(time.time() - t_start, 1),
        },
        'per_problem': results,
    }

    output_file = os.path.join(args.output_dir, 'z3_feedback_results.json')
    with open(output_file, 'w') as f:
        json.dump(output, f, indent=2, ensure_ascii=False)

    logger.info("=" * 60)
    logger.info("RESULTS")
    logger.info("  Z3-Feedback SICA: %.3f (%d/%d)", z3fb_acc, z3fb_correct, n)
    logger.info("  Vanilla SICA:     %.3f (%d/%d)", vanilla_correct / n, vanilla_correct, n)
    logger.info("  Self-Consistency:  %.3f (%d/%d)", sc_correct_count / n, sc_correct_count, n)
    logger.info("  Z3FB vs Vanilla:   +%d -%d (net %+d)",
                len(z3fb_gains), len(z3fb_losses),
                len(z3fb_gains) - len(z3fb_losses))
    stats = refiner.stats.to_dict()
    logger.info("  UNSAT traces:      %d / %d (%.1f%%)",
                stats['traces_initially_unsat'], stats['total_traces_checked'],
                100 * stats['traces_initially_unsat'] / max(stats['total_traces_checked'], 1))
    logger.info("  UNSAT->SAT rate:   %.1f%% (%d/%d)",
                100 * stats['unsat_to_sat_rate'], stats['traces_resolved'],
                stats['traces_initially_unsat'])
    logger.info("Results saved to %s", output_file)


if __name__ == '__main__':
    main()
