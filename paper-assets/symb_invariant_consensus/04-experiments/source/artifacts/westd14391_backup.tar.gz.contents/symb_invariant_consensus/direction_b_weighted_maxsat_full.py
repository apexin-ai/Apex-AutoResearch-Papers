#!/usr/bin/env python3
"""
Direction B: Weighted MAX-SAT pilot (30 problems from exp-033).
Compares constraint weighting strategies against baseline SICA and SC.

Strategies tested:
  - sc:             Self-consistency majority vote
  - sica_stored:    Original SICA answer from exp-033
  - baseline:       Re-run SICA with weight = trace_count (validation)
  - quadratic:      weight = trace_count^2
  - log:            weight = 1 + log(trace_count)
  - sqrt:           weight = sqrt(trace_count)
  - thresh_3:       Only constraints from >= 3 traces
  - thresh_6:       Only constraints from >= 6 traces (majority)
  - answer_aligned: weight = trace_count * (1 + 0.5 * majority_ratio)
  - majority_only:  weight = count of source traces voting majority answer
"""
import json
import sys
import math
import time
import logging
from pathlib import Path
from collections import Counter

sys.path.insert(0, '/root/symb_invariant_consensus')
from sica.z3_maxsat import (
    parse_z3_formula, ConstraintDeduplicator, MaxSATSolver,
    UniqueConstraint,
)
from sica.scorer import InvariantScorer

logging.basicConfig(level=logging.WARNING)

RESULTS_DIR = Path('/root/symb_invariant_consensus/results/exp033_mistral_7b_folio204')
CACHE_DIR = RESULTS_DIR / 'constraint_cache'
INTER_DIR = RESULTS_DIR / 'intermediates'
N = 204
K = 12


def norm_ans(a):
    a = str(a).strip()
    al = a.lower()
    if al in ('true', 'yes'):
        return 'True'
    if al in ('false', 'no'):
        return 'False'
    if al in ('unknown', 'uncertain', 'undetermined', ''):
        return 'Unknown'
    return a


def sc_answer(traces):
    ans = [norm_ans(t.get('answer', '')) for t in traces]
    ans = [a for a in ans if a]
    if not ans:
        return 'Unknown'
    return Counter(ans).most_common(1)[0][0]


def apply_weights(ucs, weight_fn):
    out = []
    for uc in ucs:
        w = weight_fn(uc)
        if w > 0:
            new_uc = UniqueConstraint(
                expression=uc.expression,
                z3_formula=uc.z3_formula,
                weight=w,
                source_traces=list(uc.source_traces),
            )
            out.append(new_uc)
    return out


def solve_and_answer(ucs, traces, alpha=0.5, ft=0.2):
    if not ucs:
        return sc_answer(traces), {}

    solver = MaxSATSolver()
    mr = solver.solve(ucs, timeout_ms=10000)

    nt = []
    for t in traces:
        d = dict(t)
        d['answer'] = norm_ans(t.get('answer', ''))
        nt.append(d)

    cands = sorted(set(t['answer'] for t in nt if t['answer']))
    ac = Counter(t['answer'] for t in nt if t['answer'])

    scorer = InvariantScorer(alpha=alpha, fallback_threshold=ft)
    scores = scorer.score(mr, nt, cands)
    sel = scorer.select_answer(scores, ac)
    return sel, scores


def main():
    pids = [f'folio_{i}' for i in range(N)]

    strategy_names = [
        'sc', 'sica_stored', 'baseline', 'quadratic', 'log', 'sqrt',
        'thresh_3', 'thresh_6', 'answer_aligned', 'majority_only',
    ]
    all_results = {s: [] for s in strategy_names}
    per_problem_detail = []

    t_start = time.time()

    for pi, pid in enumerate(pids):
        inter = json.loads((INTER_DIR / f'{pid}.json').read_text())
        cache = json.loads((CACHE_DIR / f'{pid}.json').read_text())

        traces = inter['sica_result']['traces']
        gt = norm_ans(inter['problem']['answer'])
        stored_sica = norm_ans(inter['sica_result']['answer'])

        # SC
        sc_ans = sc_answer(traces)
        all_results['sc'].append(sc_ans == gt)
        all_results['sica_stored'].append(stored_sica == gt)

        # Build trace answer map from cache
        trace_answers = {}
        for t_info in cache.get('per_trace', []):
            trace_answers[t_info['trace_idx']] = norm_ans(t_info.get('answer', ''))

        # Majority answer
        ta_counts = Counter(v for v in trace_answers.values() if v)
        majority_ans = ta_counts.most_common(1)[0][0] if ta_counts else None

        # Dedup
        all_c = [t_info.get('constraints', []) for t_info in cache.get('per_trace', [])]
        deduper = ConstraintDeduplicator()
        unique = deduper.deduplicate(all_c)

        # Static strategies (no closure issues)
        static_strategies = {
            'baseline': lambda uc: len(uc.source_traces),
            'quadratic': lambda uc: len(uc.source_traces) ** 2,
            'log': lambda uc: 1 + math.log(len(uc.source_traces)),
            'sqrt': lambda uc: math.sqrt(len(uc.source_traces)),
            'thresh_3': lambda uc: len(uc.source_traces) if len(uc.source_traces) >= 3 else 0,
            'thresh_6': lambda uc: len(uc.source_traces) if len(uc.source_traces) >= 6 else 0,
        }

        # Answer-aligned: bonus for constraints from traces agreeing with majority
        _maj = majority_ans
        _ta = dict(trace_answers)

        def _answer_aligned(uc, maj=_maj, ta=_ta):
            base = len(uc.source_traces)
            if maj is None:
                return base
            aligned = sum(1 for ti in uc.source_traces if ta.get(ti) == maj)
            ratio = aligned / len(uc.source_traces) if uc.source_traces else 0
            return base * (1 + 0.5 * ratio)

        def _majority_only(uc, maj=_maj, ta=_ta):
            if maj is None:
                return len(uc.source_traces)
            return sum(1 for ti in uc.source_traces if ta.get(ti) == maj)

        static_strategies['answer_aligned'] = _answer_aligned
        static_strategies['majority_only'] = _majority_only

        detail = {'pid': pid, 'gt': gt, 'sc': sc_ans, 'sica_stored': stored_sica}

        for sname, wfn in static_strategies.items():
            ucs = apply_weights(unique, wfn)
            ans, scores = solve_and_answer(ucs, traces)
            correct = (ans == gt)
            all_results[sname].append(correct)
            detail[sname] = ans

        per_problem_detail.append(detail)

        if (pi + 1) % 10 == 0:
            print(f"  processed {pi + 1}/{N} ...")

    elapsed = time.time() - t_start

    # Report
    print()
    print("=" * 70)
    print(f"Direction B: Weighted MAX-SAT Pilot  ({N} problems, {elapsed:.1f}s)")
    print("=" * 70)
    base_c = sum(all_results['baseline'])
    sc_c = sum(all_results['sc'])

    print(f"{'Strategy':<18} {'Correct':>8} {'Acc':>8} {'Δ vs base':>10} {'Δ vs SC':>10}")
    print("-" * 58)
    for sname in strategy_names:
        c = sum(all_results[sname])
        acc = c / N
        if sname in ('sc', 'sica_stored', 'baseline'):
            db_str = ''
        else:
            db_str = f"{(c - base_c) / N:+.1%}"
        ds_str = f"{(c - sc_c) / N:+.1%}"
        print(f"{sname:<18} {c:>5}/{N}   {acc:>6.1%}   {db_str:>10}   {ds_str:>10}")

    # Per-problem flips vs baseline
    print()
    print("=" * 70)
    print("Per-problem flips vs baseline")
    print("=" * 70)
    for sname in strategy_names:
        if sname in ('sc', 'sica_stored', 'baseline'):
            continue
        gains, losses = [], []
        for i in range(N):
            b = all_results['baseline'][i]
            s = all_results[sname][i]
            if not b and s:
                gains.append(f'folio_{i}')
            elif b and not s:
                losses.append(f'folio_{i}')
        if gains or losses:
            print(f"  {sname:<18} +{len(gains):>2} -{len(losses):>2}  "
                  f"gains={gains}  losses={losses}")

    # Validation: baseline vs stored SICA
    mismatches = []
    for i in range(N):
        d = per_problem_detail[i]
        if d['baseline'] != d['sica_stored']:
            mismatches.append(d['pid'])
    if mismatches:
        print(f"\nWARNING: baseline != sica_stored on: {mismatches}")
    else:
        print(f"\nValidation OK: baseline matches sica_stored on all {N} problems")

    # Save
    out = {
        'n_problems': N,
        'elapsed_s': round(elapsed, 1),
        'accuracy': {s: round(sum(all_results[s]) / N, 4) for s in strategy_names},
        'correct_counts': {s: sum(all_results[s]) for s in strategy_names},
        'per_problem': per_problem_detail,
    }
    out_path = RESULTS_DIR / 'direction_b_weighted_maxsat_pilot.json'
    with open(out_path, 'w') as f:
        json.dump(out, f, indent=2, ensure_ascii=False)
    print(f"\nSaved to {out_path}")


if __name__ == '__main__':
    main()
