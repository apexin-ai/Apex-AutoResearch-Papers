#!/usr/bin/env python3
"""
Dir-H Constraint Provenance Analysis — FOLIO 204

Analyzes relationship between constraint source_step (which reasoning step
produced the constraint) and problem accuracy.

Hypothesis: late-step constraints more likely reference conclusion,
cross-validating Dir-C premise-only findings.

Outputs: results.json + provenance_report.md
"""
import json
import os
import re
import sys
import time
from collections import Counter, defaultdict

from scipy.stats import chi2_contingency, fisher_exact, mannwhitneyu

sys.path.insert(0, '/root/symb_invariant_consensus')
from sica.z3_maxsat import ConstraintDeduplicator, MaxSATSolver
from sica.scorer import InvariantScorer
from sica.pipeline import normalize_logic_answer

FOLIO_PATH = '/root/symb_invariant_consensus/data/folio_full.json'
CACHE_DIR = '/root/symb_invariant_consensus/results/exp033_mistral_7b_folio204/constraint_cache'
INTERMED_DIR = '/root/symb_invariant_consensus/results/exp033_mistral_7b_folio204/intermediates'
OUTPUT_DIR = '/root/symb_invariant_consensus/results/dir_h_provenance_analysis'

STOP_WORDS = {
    'the', 'a', 'an', 'is', 'are', 'was', 'were', 'be', 'been', 'being',
    'have', 'has', 'had', 'do', 'does', 'did', 'will', 'would', 'could',
    'should', 'may', 'might', 'shall', 'can', 'to', 'of', 'in', 'for',
    'on', 'with', 'at', 'by', 'from', 'up', 'about', 'into', 'over',
    'after', 'that', 'this', 'which', 'who', 'whom', 'and', 'or', 'but',
    'if', 'then', 'than', 'so', 'not', 'no', 'nor', 'as', 'both',
    'either', 'neither', 'each', 'every', 'all', 'any', 'few', 'more',
    'most', 'other', 'some', 'such', 'only', 'own', 'same', 'her', 'his',
    'its', 'our', 'their', 'it', 'he', 'she', 'they', 'them', 'we',
    'me', 'him', 'us', 'my', 'your',
    'whether', 'determine', 'following', 'conclusion', 'true', 'false',
    'uncertain', 'given', 'premises', 'case', 'also', 'still',
}

STEP_BINS = {
    'early': (1, 3),
    'mid': (4, 6),
    'late': (7, 999),
}


def extract_conclusion_text(problem_text):
    marker = "Determine whether the following conclusion is true, false, or uncertain:\n"
    idx = problem_text.find(marker)
    if idx == -1:
        return ""
    return problem_text[idx + len(marker):].strip()


def normalize_to_tokens(text):
    text = text.replace('_', ' ')
    text = re.sub(r'([a-z])([A-Z])', r'\1 \2', text)
    text = re.sub(r'[^a-zA-Z\s]', ' ', text)
    tokens = set(text.lower().split())
    tokens -= STOP_WORDS
    return {t for t in tokens if len(t) > 1}


def get_conclusion_keywords(conclusion_text):
    words = conclusion_text.split()
    entities = set()
    for w in words:
        clean = re.sub(r'[^a-zA-Z]', '', w)
        if clean and clean[0].isupper() and clean.lower() not in STOP_WORDS:
            entities.add(clean.lower())
    tokens = normalize_to_tokens(conclusion_text)
    content = tokens - entities
    return content, entities


def constraint_references_conclusion(constraint, conclusion_kw, entities,
                                     threshold=0.5, min_overlap=2):
    if not conclusion_kw:
        return False
    expr = constraint.get('expression', '')
    z3f = constraint.get('z3_formula', '')
    combined = expr + ' ' + z3f
    expr_tokens = normalize_to_tokens(combined)
    expr_content = expr_tokens - entities
    overlap = conclusion_kw & expr_content
    required_min = min(min_overlap, len(conclusion_kw))
    if len(overlap) < required_min:
        return False
    ratio = len(overlap) / len(conclusion_kw)
    return ratio >= threshold


def classify_step(step):
    for name, (lo, hi) in STEP_BINS.items():
        if lo <= step <= hi:
            return name
    return 'late'


def run_sica_with_filter(cache, traces, step_filter=None):
    """Run dedup+maxsat+score with optional source_step filter.
    step_filter: None (all), or a bin name like 'early'/'mid'/'late'
    """
    deduplicator = ConstraintDeduplicator()
    solver = MaxSATSolver()
    scorer_obj = InvariantScorer()

    all_trace_constraints = []
    for trace_data in cache['per_trace']:
        constraints = trace_data['constraints']
        if step_filter is not None:
            lo, hi = STEP_BINS[step_filter]
            def _safe_step(c):
                try:
                    return int(c.get('source_step', 0))
                except (ValueError, TypeError):
                    return 0
            constraints = [c for c in constraints if lo <= _safe_step(c) <= hi]
        all_trace_constraints.append(constraints)

    unique = deduplicator.deduplicate(all_trace_constraints)
    if not unique:
        return "", {}, 0

    maxsat_result = solver.solve(unique)
    answer_counts = Counter(t['answer'] for t in traces if t.get('answer'))
    candidates = sorted(set(t['answer'] for t in traces if t.get('answer')))
    if not candidates:
        return "", {}, 0

    scores = scorer_obj.score(maxsat_result, traces, candidates)
    answer = scorer_obj.select_answer(scores, dict(answer_counts))
    return answer, scores, len(unique)


def main():
    t_start = time.time()

    with open(FOLIO_PATH) as f:
        folio_data = json.load(f)
    folio_by_id = {p['id']: p for p in folio_data}

    pids = sorted(folio_by_id.keys(), key=lambda x: int(x.split('_')[1]))

    # Aggregation accumulators
    step_dist = Counter()  # global source_step distribution by bin
    step_dist_correct = Counter()
    step_dist_incorrect = Counter()
    leakage_by_step = defaultdict(lambda: {'total': 0, 'leaks': 0})
    cross_trace_by_step = defaultdict(lambda: {'total': 0, 'multi_trace': 0})

    acc_by_filter = {k: {'correct': 0, 'total': 0} for k in ['all', 'early', 'mid', 'late']}
    n_sc_correct = 0
    per_problem = []

    for i, pid in enumerate(pids):
        problem = folio_by_id[pid]
        gt = problem['answer']

        cache_path = os.path.join(CACHE_DIR, f"{pid}.json")
        intermed_path = os.path.join(INTERMED_DIR, f"{pid}.json")
        if not os.path.exists(cache_path) or not os.path.exists(intermed_path):
            continue

        with open(cache_path) as f:
            cache = json.load(f)
        with open(intermed_path) as f:
            intermed = json.load(f)

        traces = intermed['sica_result']['traces']
        sica_orig = intermed['sica_result']['answer']
        sica_orig_correct = (sica_orig == gt)

        answer_counts = Counter(t['answer'] for t in traces if t.get('answer'))
        sc_answer = answer_counts.most_common(1)[0][0] if answer_counts else ""
        sc_ok = (sc_answer == gt)
        n_sc_correct += sc_ok

        conclusion_text = extract_conclusion_text(problem['problem'])
        conclusion_kw, entities = get_conclusion_keywords(conclusion_text)

        # Per-constraint analysis
        prob_step_dist = Counter()
        prob_leakage = defaultdict(lambda: {'total': 0, 'leaks': 0})
        all_constraints_flat = []

        for trace_data in cache['per_trace']:
            trace_idx = trace_data['trace_idx']
            for c in trace_data['constraints']:
                try:
                    step = int(c.get('source_step', 0))
                except (ValueError, TypeError):
                    continue
                if step < 1:
                    continue
                bin_name = classify_step(step)
                prob_step_dist[bin_name] += 1
                step_dist[bin_name] += 1

                leaks = constraint_references_conclusion(c, conclusion_kw, entities)
                prob_leakage[bin_name]['total'] += 1
                prob_leakage[bin_name]['leaks'] += int(leaks)
                leakage_by_step[bin_name]['total'] += 1
                leakage_by_step[bin_name]['leaks'] += int(leaks)

                all_constraints_flat.append({
                    'trace_idx': trace_idx,
                    'step': step,
                    'bin': bin_name,
                    'expression': c.get('expression', ''),
                    'leaks': leaks,
                })

        if sica_orig_correct:
            step_dist_correct += prob_step_dist
        else:
            step_dist_incorrect += prob_step_dist

        # Cross-trace consistency by step bin
        expr_by_bin = defaultdict(lambda: defaultdict(set))
        for trace_data in cache['per_trace']:
            trace_idx = trace_data['trace_idx']
            for c in trace_data['constraints']:
                try:
                    step = int(c.get('source_step', 0))
                except (ValueError, TypeError):
                    continue
                if step < 1:
                    continue
                bin_name = classify_step(step)
                expr_norm = c.get('expression', '').strip().lower()
                if expr_norm:
                    expr_by_bin[bin_name][expr_norm].add(trace_idx)

        for bin_name, exprs in expr_by_bin.items():
            for expr, trace_set in exprs.items():
                cross_trace_by_step[bin_name]['total'] += 1
                if len(trace_set) > 1:
                    cross_trace_by_step[bin_name]['multi_trace'] += 1

        # Run SICA with different step filters
        prob_results = {'pid': pid, 'gt': gt, 'sica_orig_correct': sica_orig_correct}

        for filt in ['all', 'early', 'mid', 'late']:
            sf = None if filt == 'all' else filt
            ans, scores, n_unique = run_sica_with_filter(cache, traces, sf)
            ok = (ans == gt)
            acc_by_filter[filt]['correct'] += int(ok)
            acc_by_filter[filt]['total'] += 1
            prob_results[f'{filt}_answer'] = ans
            prob_results[f'{filt}_correct'] = ok
            prob_results[f'{filt}_n_unique'] = n_unique

        prob_results['step_distribution'] = dict(prob_step_dist)
        prob_results['leakage'] = {k: dict(v) for k, v in prob_leakage.items()}
        per_problem.append(prob_results)

        if (i + 1) % 50 == 0:
            print(f"  processed {i+1}/{len(pids)}...")

    n = acc_by_filter['all']['total']

    # Leakage rates
    leakage_rates = {}
    for bin_name in ['early', 'mid', 'late']:
        d = leakage_by_step[bin_name]
        rate = d['leaks'] / d['total'] if d['total'] > 0 else 0
        leakage_rates[bin_name] = {
            'rate': round(rate, 4),
            'leaks': d['leaks'],
            'total': d['total'],
        }

    # Chi-squared test for leakage independence
    leakage_table = []
    for bin_name in ['early', 'mid', 'late']:
        d = leakage_by_step[bin_name]
        leakage_table.append([d['leaks'], d['total'] - d['leaks']])
    if all(sum(row) > 0 for row in leakage_table):
        chi2, chi2_p, dof, _ = chi2_contingency(leakage_table)
    else:
        chi2, chi2_p, dof = 0, 1.0, 0

    # Fisher exact for early vs late leakage
    if leakage_by_step['early']['total'] > 0 and leakage_by_step['late']['total'] > 0:
        table_2x2 = [
            [leakage_by_step['early']['leaks'],
             leakage_by_step['early']['total'] - leakage_by_step['early']['leaks']],
            [leakage_by_step['late']['leaks'],
             leakage_by_step['late']['total'] - leakage_by_step['late']['leaks']],
        ]
        fisher_or, fisher_p = fisher_exact(table_2x2)
    else:
        fisher_or, fisher_p = 0, 1.0

    # Accuracy by filter
    accuracy_results = {}
    for filt in ['all', 'early', 'mid', 'late']:
        d = acc_by_filter[filt]
        acc = d['correct'] / d['total'] if d['total'] > 0 else 0
        accuracy_results[filt] = {
            'accuracy': round(acc, 4),
            'correct': d['correct'],
            'total': d['total'],
        }

    # Correct vs incorrect step distribution (normalized)
    total_correct_constraints = sum(step_dist_correct.values())
    total_incorrect_constraints = sum(step_dist_incorrect.values())
    correct_dist_norm = {}
    incorrect_dist_norm = {}
    for b in ['early', 'mid', 'late']:
        correct_dist_norm[b] = round(step_dist_correct[b] / total_correct_constraints, 4) if total_correct_constraints > 0 else 0
        incorrect_dist_norm[b] = round(step_dist_incorrect[b] / total_incorrect_constraints, 4) if total_incorrect_constraints > 0 else 0

    # Mann-Whitney U: compare source_step distributions between correct and incorrect
    correct_steps = []
    incorrect_steps = []
    for p in per_problem:
        pid = p['pid']
        cache_path = os.path.join(CACHE_DIR, f"{pid}.json")
        with open(cache_path) as f:
            cache = json.load(f)
        for trace_data in cache['per_trace']:
            for c in trace_data['constraints']:
                try:
                    step = int(c.get('source_step', 0))
                except (ValueError, TypeError):
                    continue
                if step < 1:
                    continue
                if p['sica_orig_correct']:
                    correct_steps.append(step)
                else:
                    incorrect_steps.append(step)

    if correct_steps and incorrect_steps:
        mwu_stat, mwu_p = mannwhitneyu(correct_steps, incorrect_steps, alternative='two-sided')
        mean_correct = sum(correct_steps) / len(correct_steps)
        mean_incorrect = sum(incorrect_steps) / len(incorrect_steps)
    else:
        mwu_stat, mwu_p = 0, 1.0
        mean_correct = mean_incorrect = 0

    # Cross-trace consistency
    cross_trace_rates = {}
    for bin_name in ['early', 'mid', 'late']:
        d = cross_trace_by_step[bin_name]
        rate = d['multi_trace'] / d['total'] if d['total'] > 0 else 0
        cross_trace_rates[bin_name] = {
            'rate': round(rate, 4),
            'multi_trace': d['multi_trace'],
            'total_unique_exprs': d['total'],
        }

    # Compile results
    results = {
        'summary': {
            'n_problems': n,
            'sc_accuracy': round(n_sc_correct / n, 4) if n else 0,
            'sc_correct': n_sc_correct,
        },
        'source_step_distribution': {
            'global': {b: step_dist[b] for b in ['early', 'mid', 'late']},
            'total': sum(step_dist.values()),
        },
        'correct_vs_incorrect_distribution': {
            'correct_problems': {
                'raw': {b: step_dist_correct[b] for b in ['early', 'mid', 'late']},
                'normalized': correct_dist_norm,
                'total_constraints': total_correct_constraints,
            },
            'incorrect_problems': {
                'raw': {b: step_dist_incorrect[b] for b in ['early', 'mid', 'late']},
                'normalized': incorrect_dist_norm,
                'total_constraints': total_incorrect_constraints,
            },
            'mann_whitney_u': {
                'statistic': round(mwu_stat, 2),
                'p_value': round(mwu_p, 6),
                'mean_step_correct': round(mean_correct, 3),
                'mean_step_incorrect': round(mean_incorrect, 3),
            },
        },
        'leakage_rate_by_step': leakage_rates,
        'leakage_tests': {
            'chi2_3way': {
                'chi2': round(chi2, 4),
                'p_value': round(chi2_p, 6),
                'dof': dof,
            },
            'fisher_early_vs_late': {
                'odds_ratio': round(fisher_or, 4),
                'p_value': round(fisher_p, 6),
            },
        },
        'accuracy_by_step_filter': accuracy_results,
        'cross_trace_consistency_by_step': cross_trace_rates,
        'per_problem': per_problem,
    }

    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(os.path.join(OUTPUT_DIR, 'results.json'), 'w') as f:
        json.dump(results, f, indent=2)

    # Generate report
    report = []
    report.append("# Dir-H: Constraint Provenance Analysis — FOLIO 204\n")
    report.append(f"**Date**: {time.strftime('%Y-%m-%d %H:%M')}")
    report.append(f"**Problems**: {n}")
    report.append(f"**SC baseline**: {n_sc_correct}/{n} = {n_sc_correct/n:.2%}\n")

    report.append("## 1. Source Step Distribution\n")
    report.append("| Bin | Range | Count | Proportion |")
    report.append("|-----|-------|-------|------------|")
    total_c = sum(step_dist.values())
    for b in ['early', 'mid', 'late']:
        lo, hi = STEP_BINS[b]
        hi_str = f"{hi}" if hi < 999 else "+"
        report.append(f"| {b} | {lo}-{hi_str} | {step_dist[b]} | {step_dist[b]/total_c:.2%} |")
    report.append(f"| **total** | | **{total_c}** | |")

    report.append("\n## 2. Correct vs Incorrect Problems\n")
    report.append("| Bin | Correct (norm) | Incorrect (norm) |")
    report.append("|-----|---------------|-----------------|")
    for b in ['early', 'mid', 'late']:
        report.append(f"| {b} | {correct_dist_norm[b]:.2%} | {incorrect_dist_norm[b]:.2%} |")
    report.append(f"\nMann-Whitney U: stat={mwu_stat:.2f}, p={mwu_p:.6f}")
    report.append(f"Mean source_step — correct: {mean_correct:.3f}, incorrect: {mean_incorrect:.3f}")

    report.append("\n## 3. Conclusion Leakage by Step\n")
    report.append("| Bin | Leakage Rate | Leaks / Total |")
    report.append("|-----|-------------|---------------|")
    for b in ['early', 'mid', 'late']:
        d = leakage_rates[b]
        report.append(f"| {b} | {d['rate']:.2%} | {d['leaks']}/{d['total']} |")
    report.append(f"\nChi-squared (3-way): χ²={chi2:.4f}, p={chi2_p:.6f}, dof={dof}")
    report.append(f"Fisher exact (early vs late): OR={fisher_or:.4f}, p={fisher_p:.6f}")

    report.append("\n## 4. Accuracy by Step Filter\n")
    report.append("Only constraints from the specified step bin are used for SICA scoring.\n")
    report.append("| Filter | Accuracy | Correct/Total | Δ vs SC |")
    report.append("|--------|----------|---------------|---------|")
    for filt in ['all', 'early', 'mid', 'late']:
        d = accuracy_results[filt]
        delta = (d['correct'] - n_sc_correct) / n if n else 0
        report.append(f"| {filt} | {d['accuracy']:.2%} | {d['correct']}/{d['total']} | {delta:+.2%} |")

    report.append("\n## 5. Cross-Trace Consistency by Step\n")
    report.append("Fraction of unique expressions appearing in >1 trace.\n")
    report.append("| Bin | Consistency Rate | Multi-trace / Total |")
    report.append("|-----|-----------------|---------------------|")
    for b in ['early', 'mid', 'late']:
        d = cross_trace_rates[b]
        report.append(f"| {b} | {d['rate']:.2%} | {d['multi_trace']}/{d['total_unique_exprs']} |")

    report.append("\n## 6. Key Findings\n")
    late_leak = leakage_rates['late']['rate']
    early_leak = leakage_rates['early']['rate']
    report.append(f"- Late-step leakage rate ({late_leak:.2%}) vs early-step ({early_leak:.2%}): "
                  f"Fisher p={fisher_p:.6f}")
    if fisher_p < 0.05:
        report.append("  → **Significant**: late-step constraints have higher conclusion leakage")
    else:
        report.append("  → Not significant at α=0.05")

    early_acc = accuracy_results['early']['accuracy']
    all_acc = accuracy_results['all']['accuracy']
    report.append(f"- Early-only SICA accuracy: {early_acc:.2%} vs full SICA: {all_acc:.2%}")
    report.append(f"- This {'supports' if late_leak > early_leak and fisher_p < 0.1 else 'does not clearly support'} "
                  "the Dir-C finding that conclusion-referencing constraints are more prevalent in later reasoning steps.")

    elapsed = time.time() - t_start
    report.append(f"\n---\n*Analysis completed in {elapsed:.1f}s*")

    with open(os.path.join(OUTPUT_DIR, 'provenance_report.md'), 'w') as f:
        f.write('\n'.join(report))

    print(f"\n{'='*60}")
    print("DIR-H CONSTRAINT PROVENANCE ANALYSIS (FOLIO 204)")
    print(f"{'='*60}")
    print(f"Problems:              {n}")
    print(f"SC Accuracy:           {n_sc_correct}/{n} = {n_sc_correct/n:.4f}")
    print(f"Step distribution:     early={step_dist['early']}, mid={step_dist['mid']}, late={step_dist['late']}")
    print(f"Leakage rates:         early={leakage_rates['early']['rate']:.4f}, mid={leakage_rates['mid']['rate']:.4f}, late={leakage_rates['late']['rate']:.4f}")
    print(f"Fisher (early v late): OR={fisher_or:.4f}, p={fisher_p:.6f}")
    print(f"Accuracy (all):        {accuracy_results['all']['correct']}/{n} = {accuracy_results['all']['accuracy']:.4f}")
    print(f"Accuracy (early):      {accuracy_results['early']['correct']}/{n} = {accuracy_results['early']['accuracy']:.4f}")
    print(f"Accuracy (mid):        {accuracy_results['mid']['correct']}/{n} = {accuracy_results['mid']['accuracy']:.4f}")
    print(f"Accuracy (late):       {accuracy_results['late']['correct']}/{n} = {accuracy_results['late']['accuracy']:.4f}")
    print(f"Cross-trace consist:   early={cross_trace_rates['early']['rate']:.4f}, mid={cross_trace_rates['mid']['rate']:.4f}, late={cross_trace_rates['late']['rate']:.4f}")
    print(f"Time:                  {elapsed:.1f}s")
    print(f"Output:                {OUTPUT_DIR}/")


if __name__ == '__main__':
    main()
