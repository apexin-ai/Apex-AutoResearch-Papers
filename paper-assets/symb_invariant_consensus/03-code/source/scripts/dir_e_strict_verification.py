#!/usr/bin/env python3
"""Dir-E: Z3 Strict-Mode Verification — FOLIO 30-problem Pilot

Checks constraint set consistency using z3.Solver.check() (strict mode)
instead of MAX-SAT optimize(). Finds MUS for UNSAT sets, removes them,
and rescores.
"""
import json
import sys
import os
import time
from collections import Counter
from math import comb
from pathlib import Path

sys.path.insert(0, '/root/symb_invariant_consensus')
from sica.z3_maxsat import parse_z3_formula, ConstraintDeduplicator, UniqueConstraint

import z3

z3.set_param('smt.random_seed', 42)
z3.set_param('sat.random_seed', 42)

CONSTRAINT_CACHE_DIR = Path('/root/symb_invariant_consensus/results/exp033_mistral_7b_folio204/constraint_cache')
RESULTS_FILE = Path('/root/symb_invariant_consensus/results/exp033_mistral_7b_folio204/exp033_results.json')
SC_MATRIX_FILE = Path('/root/symb_invariant_consensus/results/exp033_mistral_7b_folio204/sc_answer_matrix.json')
OUTPUT_DIR = Path('/root/symb_invariant_consensus/results/dir_e_strict_verification')
N_PROBLEMS = 30
CANDIDATES = ['True', 'False', 'Unknown']
ALPHA = 0.5


def iterative_mus_removal(unique_constraints, max_rounds=20):
    """Iteratively find and remove unsat_core until remaining set is SAT.

    Returns (filtered_constraints, all_removed, n_rounds).
    """
    remaining = list(unique_constraints)
    all_removed = []
    rounds = 0

    for _ in range(max_rounds):
        valid = [(i, uc) for i, uc in enumerate(remaining)
                 if uc.z3_formula is not None and z3.is_bool(uc.z3_formula)]
        if not valid:
            break

        s = z3.Solver()
        s.set("timeout", 5000)
        tracker_map = {}
        for i, uc in valid:
            t = z3.Bool(f'__trk_{i}_{rounds}')
            tracker_map[str(t)] = i
            s.assert_and_track(uc.z3_formula, t)

        result = s.check()
        if result == z3.sat:
            break
        if result == z3.unknown:
            break

        core = s.unsat_core()
        if not core:
            break

        core_strs = {str(c) for c in core}
        to_remove = {tracker_map[tn] for tn in core_strs if tn in tracker_map}
        if not to_remove:
            break

        all_removed.extend(remaining[i] for i in sorted(to_remove))
        remaining = [uc for i, uc in enumerate(remaining) if i not in to_remove]
        rounds += 1

    return remaining, all_removed, rounds


def score_candidates(unique_constraints, traces):
    """Score each candidate by total weight of constraints from supporting traces."""
    answer_traces = {}
    for t in traces:
        ans = str(t.get('answer', '')).strip()
        if ans:
            answer_traces.setdefault(ans, set()).add(t['trace_idx'])

    scores = {}
    for cand in CANDIDATES:
        cand_traces = answer_traces.get(cand, set())
        scores[cand] = sum(
            uc.weight for uc in unique_constraints
            if set(uc.source_traces) & cand_traces
        )
    return scores


def select_answer(scores, answer_counts):
    """Select highest-scoring answer; tie-break by vote count."""
    if not scores or max(scores.values()) == 0:
        return ''
    max_score = max(scores.values())
    top = [a for a, s in scores.items() if s == max_score]
    if len(top) == 1:
        return top[0]
    return max(top, key=lambda a: answer_counts.get(a, 0))


def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    with open(RESULTS_FILE) as f:
        orig_results = json.load(f)
    with open(SC_MATRIX_FILE) as f:
        sc_matrix = json.load(f)

    deduplicator = ConstraintDeduplicator()

    per_question = []
    n_unsat = 0
    mus_sizes = []
    sica_correct = 0
    strict_correct = 0
    sc_correct = 0

    t_start = time.time()

    for qi in range(N_PROBLEMS):
        pid = f'folio_{qi}'
        cache_path = CONSTRAINT_CACHE_DIR / f'{pid}.json'
        with open(cache_path) as f:
            cache = json.load(f)

        gt = cache['gt']
        all_trace_constraints = []
        traces = []
        for td in cache['per_trace']:
            traces.append({'trace_idx': td['trace_idx'], 'answer': td['answer']})
            all_trace_constraints.append(td['constraints'])

        # Deduplicate
        unique_constraints = deduplicator.deduplicate(all_trace_constraints)
        n_before = len(unique_constraints)

        # Strict check + MUS removal
        filtered, removed, n_rounds = iterative_mus_removal(unique_constraints)
        n_after = len(filtered)
        was_unsat = len(removed) > 0

        if was_unsat:
            n_unsat += 1
            mus_sizes.append(len(removed))

        # Answer counts for tie-breaking
        answer_counts = Counter(
            str(t['answer']).strip() for t in traces if str(t['answer']).strip()
        )

        # Strict-filtered scoring
        strict_scores = score_candidates(filtered, traces)
        strict_answer = select_answer(strict_scores, answer_counts)
        strict_is_correct = (strict_answer == gt)

        # Original SICA
        orig_entry = orig_results['results'][qi]
        orig_sica_correct = orig_entry['sica_correct']

        # SC
        sc_data = sc_matrix.get(pid, {})
        sc_answers = [a for a in sc_data.get('answers', []) if a.strip()]
        sc_answer = Counter(sc_answers).most_common(1)[0][0] if sc_answers else ''
        sc_is_correct = (sc_answer == gt)

        if orig_sica_correct:
            sica_correct += 1
        if strict_is_correct:
            strict_correct += 1
        if sc_is_correct:
            sc_correct += 1

        per_question.append({
            'pid': pid,
            'gt': gt,
            'orig_sica_answer': orig_entry['sica_answer'],
            'orig_sica_correct': orig_sica_correct,
            'strict_answer': strict_answer,
            'strict_scores': {k: round(v, 2) for k, v in strict_scores.items()},
            'strict_correct': strict_is_correct,
            'sc_answer': sc_answer,
            'sc_correct': sc_is_correct,
            'was_unsat': was_unsat,
            'mus_rounds': n_rounds,
            'n_constraints_before': n_before,
            'n_constraints_after': n_after,
            'mus_size': len(removed),
            'removed_expressions': [uc.expression for uc in removed],
        })

        status = "UNSAT" if was_unsat else "SAT"
        print(f'  {pid}: {status}  constraints {n_before}->{n_after}  '
              f'sica={orig_entry["sica_answer"]}  strict={strict_answer}  gt={gt}')

    elapsed = time.time() - t_start

    # McNemar exact test (SICA vs strict)
    a = b = c = d = 0
    for q in per_question:
        sc_ok = q['orig_sica_correct']
        st_ok = q['strict_correct']
        if sc_ok and st_ok: a += 1
        elif sc_ok and not st_ok: b += 1
        elif not sc_ok and st_ok: c += 1
        else: d += 1

    n_disc = b + c
    if n_disc > 0:
        k = min(b, c)
        p_val = sum(comb(n_disc, i) * 0.5**n_disc for i in range(k + 1)) * 2
        p_val = min(p_val, 1.0)
    else:
        p_val = 1.0

    avg_mus = sum(mus_sizes) / len(mus_sizes) if mus_sizes else 0.0

    summary = {
        'n_problems': N_PROBLEMS,
        'original_sica_acc': round(sica_correct / N_PROBLEMS, 4),
        'strict_filtered_acc': round(strict_correct / N_PROBLEMS, 4),
        'sc_acc': round(sc_correct / N_PROBLEMS, 4),
        'sica_correct': sica_correct,
        'strict_correct': strict_correct,
        'sc_correct': sc_correct,
        'unsat_count': n_unsat,
        'unsat_rate': round(n_unsat / N_PROBLEMS, 4),
        'avg_mus_size': round(avg_mus, 2),
        'total_mus_removed': sum(mus_sizes),
        'mcnemar_sica_vs_strict': {
            'both_correct': a,
            'sica_only': b,
            'strict_only': c,
            'both_wrong': d,
            'p_value': round(p_val, 6),
        },
        'elapsed_s': round(elapsed, 1),
    }

    output = {'summary': summary, 'per_question': per_question}
    output_path = OUTPUT_DIR / 'results.json'
    with open(output_path, 'w') as f:
        json.dump(output, f, indent=2, ensure_ascii=False)

    print(f'\n=== Dir-E Strict Verification (n={N_PROBLEMS}) ===')
    print(f'Original SICA acc: {summary["original_sica_acc"]:.4f} ({sica_correct}/{N_PROBLEMS})')
    print(f'Strict-filtered acc: {summary["strict_filtered_acc"]:.4f} ({strict_correct}/{N_PROBLEMS})')
    print(f'SC acc:             {summary["sc_acc"]:.4f} ({sc_correct}/{N_PROBLEMS})')
    print(f'UNSAT rate: {summary["unsat_rate"]:.4f} ({n_unsat}/{N_PROBLEMS})')
    print(f'Avg MUS size: {avg_mus:.2f}')
    print(f'McNemar p={p_val:.4f}  (b={b}, c={c})')
    print(f'Elapsed: {elapsed:.1f}s')
    print(f'Saved: {output_path}')


if __name__ == '__main__':
    main()
