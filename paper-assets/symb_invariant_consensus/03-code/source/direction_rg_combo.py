#!/usr/bin/env python3
"""Direction R+G Combo: SICA + NLI external verifier combination strategies.

Combines two architecturally independent signals:
- SICA: symbolic constraint aggregation from CoT traces (MAX-SAT)
- NLI: DeBERTa encoder-only model predicting entailment/contradiction/neutral

Since full G (decoupling) results are unavailable (only 5 test problems),
this uses standard SICA results. When G results become available,
swap in SICA-G per-problem answers.
"""
import argparse
import json
import os
import sys
from collections import Counter

import numpy as np


def normalize_answer(ans):
    ans = str(ans).strip().lower()
    if ans in ('true', 'yes', 't'):
        return 'True'
    elif ans in ('false', 'no', 'f'):
        return 'False'
    elif ans in ('unknown', 'uncertain', 'u', 'undetermined'):
        return 'Unknown'
    return ans.capitalize()


def sc_majority(answers):
    valid = [normalize_answer(a) for a in answers if normalize_answer(a) in ('True', 'False', 'Unknown')]
    if not valid:
        return 'Unknown'
    c = Counter(valid)
    return c.most_common(1)[0][0]


def mcnemar_test(correct_a, correct_b):
    """McNemar's test: are two classifiers significantly different?"""
    n = len(correct_a)
    b_count = sum(1 for i in range(n) if correct_a[i] and not correct_b[i])
    c_count = sum(1 for i in range(n) if not correct_a[i] and correct_b[i])

    if b_count + c_count == 0:
        return {'chi2': 0.0, 'p_value': 1.0, 'b': b_count, 'c': c_count}

    chi2 = (abs(b_count - c_count) - 1) ** 2 / (b_count + c_count)

    from scipy.stats import chi2 as chi2_dist
    p_value = 1 - chi2_dist.cdf(chi2, df=1)
    return {'chi2': round(chi2, 4), 'p_value': round(p_value, 6), 'b': b_count, 'c': c_count}


def load_data(r_results_path, exp033_path, sc_matrix_path):
    """Load R NLI results and exp033 SICA results."""
    with open(r_results_path) as f:
        r_data = json.load(f)

    with open(exp033_path) as f:
        exp033 = json.load(f)

    with open(sc_matrix_path) as f:
        sc_matrix = json.load(f)

    per_q = r_data['per_question']

    exp033_by_id = {}
    for prob in exp033['results']:
        exp033_by_id[prob['problem_id']] = prob

    problems = []
    for pid in sorted(per_q.keys(), key=lambda x: int(x.split('_')[1])):
        q = per_q[pid]
        e = exp033_by_id.get(pid, {})
        sc_answers = sc_matrix.get(pid, {}).get('answers', [])

        problems.append({
            'pid': pid,
            'gold': q['gold'],
            'sc_answer': q['sc_answer'],
            'sica_answer': q['sica_answer'],
            'deberta_pred': q['deberta_pred'],
            'deberta_probs': q['deberta_probs'],
            'sc_correct': q['sc_correct'],
            'sica_correct': q['sica_correct'],
            'deberta_correct': q['deberta_correct'],
            'sica_scores': e.get('sica_scores', {}),
            'sc_vote_distribution': e.get('sc_vote_distribution', {}),
            'sc_answers': sc_answers,
        })

    return problems


def strategy_intersection(problems):
    """When SICA and NLI agree, use that. When they disagree, fall back to SC."""
    results = []
    for p in problems:
        if p['sica_answer'] == p['deberta_pred']:
            answer = p['sica_answer']
            source = 'agree'
        else:
            answer = p['sc_answer']
            source = 'fallback_sc'
        correct = (answer == p['gold'])
        results.append({'pid': p['pid'], 'answer': answer, 'correct': correct, 'source': source})
    return results


def strategy_intersection_sica_fallback(problems):
    """When SICA and NLI agree, use that. When they disagree, fall back to SICA."""
    results = []
    for p in problems:
        if p['sica_answer'] == p['deberta_pred']:
            answer = p['sica_answer']
            source = 'agree'
        else:
            answer = p['sica_answer']
            source = 'fallback_sica'
        correct = (answer == p['gold'])
        results.append({'pid': p['pid'], 'answer': answer, 'correct': correct, 'source': source})
    return results


def strategy_cascade(problems, threshold=0.7):
    """NLI high-confidence → use NLI, else → use SICA."""
    results = []
    for p in problems:
        probs = p['deberta_probs']
        max_prob = max(probs.values())
        if max_prob >= threshold:
            answer = p['deberta_pred']
            source = f'nli_conf_{max_prob:.2f}'
        else:
            answer = p['sica_answer']
            source = f'sica_lowconf_{max_prob:.2f}'
        correct = (answer == p['gold'])
        results.append({'pid': p['pid'], 'answer': answer, 'correct': correct, 'source': source})
    return results


def strategy_cascade_reverse(problems, threshold=0.7):
    """SICA high-confidence → use SICA, else → use NLI.

    SICA confidence = margin between top two SICA scores normalized.
    """
    results = []
    for p in problems:
        scores = p['sica_scores']
        if scores:
            sorted_scores = sorted(scores.values(), reverse=True)
            total = sum(sorted_scores)
            if total > 0:
                top_frac = sorted_scores[0] / total
            else:
                top_frac = 0
        else:
            top_frac = 0

        if top_frac >= threshold:
            answer = p['sica_answer']
            source = f'sica_conf_{top_frac:.2f}'
        else:
            answer = p['deberta_pred']
            source = f'nli_lowconf_{top_frac:.2f}'
        correct = (answer == p['gold'])
        results.append({'pid': p['pid'], 'answer': answer, 'correct': correct, 'source': source})
    return results


def strategy_nli_weighted_vote(problems, nli_weight=1):
    """Add NLI prediction as extra vote(s) to SC vote distribution, then majority vote."""
    results = []
    for p in problems:
        votes = Counter()
        for a in p['sc_answers']:
            na = normalize_answer(a)
            if na in ('True', 'False', 'Unknown'):
                votes[na] += 1

        votes[p['deberta_pred']] += nli_weight

        answer = votes.most_common(1)[0][0]
        correct = (answer == p['gold'])
        results.append({'pid': p['pid'], 'answer': answer, 'correct': correct, 'source': 'weighted_vote'})
    return results


def strategy_sica_nli_weighted_vote(problems, nli_weight=3):
    """Combine SICA MAX-SAT scores + NLI probability as weighted vote."""
    results = []
    for p in problems:
        combined = {'True': 0.0, 'False': 0.0, 'Unknown': 0.0}

        for label, score in p['sica_scores'].items():
            nl = normalize_answer(label)
            if nl in combined:
                combined[nl] += score

        probs = p['deberta_probs']
        combined['True'] += probs.get('True', 0) * nli_weight
        combined['False'] += probs.get('False', 0) * nli_weight
        combined['Unknown'] += probs.get('Unknown', 0) * nli_weight

        answer = max(combined, key=combined.get)
        correct = (answer == p['gold'])
        results.append({
            'pid': p['pid'], 'answer': answer, 'correct': correct,
            'source': 'sica_nli_weighted', 'combined_scores': {k: round(v, 3) for k, v in combined.items()},
        })
    return results


def strategy_oracle(problems):
    """Upper bound: pick whichever signal is correct when they disagree."""
    results = []
    for p in problems:
        if p['sica_answer'] == p['deberta_pred']:
            answer = p['sica_answer']
            source = 'agree'
        elif p['sica_correct']:
            answer = p['sica_answer']
            source = 'oracle_sica'
        elif p['deberta_correct']:
            answer = p['deberta_pred']
            source = 'oracle_nli'
        else:
            answer = p['sica_answer']
            source = 'both_wrong'
        correct = (answer == p['gold'])
        results.append({'pid': p['pid'], 'answer': answer, 'correct': correct, 'source': source})
    return results


def compute_per_class(results, problems):
    """Compute per-class accuracy."""
    by_class = {}
    for r, p in zip(results, problems):
        gold = p['gold']
        if gold not in by_class:
            by_class[gold] = {'total': 0, 'correct': 0}
        by_class[gold]['total'] += 1
        if r['correct']:
            by_class[gold]['correct'] += 1

    for label in by_class:
        s = by_class[label]
        s['accuracy'] = round(s['correct'] / s['total'], 4) if s['total'] > 0 else 0
    return by_class


def main():
    parser = argparse.ArgumentParser(description='R+G Combo: SICA + NLI combination strategies')
    parser.add_argument('--r-results', default='results/direction_r_nli_large/results.json')
    parser.add_argument('--exp033', default='results/exp033_mistral_7b_folio204/exp033_results.json')
    parser.add_argument('--sc-matrix', default='results/exp033_mistral_7b_folio204/sc_answer_matrix.json')
    parser.add_argument('--output-dir', default='results/direction_rg_combo')
    parser.add_argument('--dry-run', action='store_true')
    args = parser.parse_args()

    os.chdir('/root/symb_invariant_consensus')

    if args.dry_run:
        print('=== DRY RUN ===')
        for path in [args.r_results, args.exp033, args.sc_matrix]:
            exists = os.path.exists(path)
            print(f'  {path}: {"OK" if exists else "MISSING"}')
        try:
            import scipy.stats
            print('  scipy: OK')
        except ImportError:
            print('  scipy: MISSING (McNemar test will fail)')
        try:
            import numpy
            print(f'  numpy: OK ({numpy.__version__})')
        except ImportError:
            print('  numpy: MISSING')
        print('=== DRY RUN PASSED ===')
        return

    print('Loading data...', flush=True)
    problems = load_data(args.r_results, args.exp033, args.sc_matrix)
    n = len(problems)
    print(f'  {n} problems loaded', flush=True)

    sc_correct_list = [p['sc_correct'] for p in problems]
    sica_correct_list = [p['sica_correct'] for p in problems]
    nli_correct_list = [p['deberta_correct'] for p in problems]

    sc_acc = sum(sc_correct_list) / n
    sica_acc = sum(sica_correct_list) / n
    nli_acc = sum(nli_correct_list) / n

    strategies = {}

    # 1. Intersection: agree → use, disagree → SC fallback
    res = strategy_intersection(problems)
    agree_count = sum(1 for r in res if r['source'] == 'agree')
    strategies['intersection_sc_fallback'] = {
        'results': res,
        'description': 'SICA ∩ NLI agree → use, disagree → SC fallback',
        'agree_count': agree_count,
        'agree_pct': round(agree_count / n * 100, 1),
    }

    # 2. Intersection: agree → use, disagree → SICA fallback
    res = strategy_intersection_sica_fallback(problems)
    strategies['intersection_sica_fallback'] = {
        'results': res,
        'description': 'SICA ∩ NLI agree → use, disagree → SICA fallback',
    }

    # 3. Cascade NLI→SICA at various thresholds
    for thresh in [0.6, 0.7, 0.8, 0.9]:
        res = strategy_cascade(problems, threshold=thresh)
        nli_used = sum(1 for r in res if r['source'].startswith('nli'))
        strategies[f'cascade_nli_t{int(thresh*100)}'] = {
            'results': res,
            'description': f'NLI conf≥{thresh} → use NLI, else → SICA',
            'nli_used': nli_used,
            'nli_used_pct': round(nli_used / n * 100, 1),
        }

    # 4. Cascade SICA→NLI (reverse) at various thresholds
    for thresh in [0.6, 0.7, 0.8]:
        res = strategy_cascade_reverse(problems, threshold=thresh)
        sica_used = sum(1 for r in res if r['source'].startswith('sica'))
        strategies[f'cascade_sica_t{int(thresh*100)}'] = {
            'results': res,
            'description': f'SICA conf≥{thresh} → use SICA, else → NLI',
            'sica_used': sica_used,
            'sica_used_pct': round(sica_used / n * 100, 1),
        }

    # 5. NLI as extra vote in SC (w=1, w=3, w=5)
    for w in [1, 3, 5]:
        res = strategy_nli_weighted_vote(problems, nli_weight=w)
        strategies[f'nli_sc_vote_w{w}'] = {
            'results': res,
            'description': f'SC votes + NLI as {w} extra vote(s)',
        }

    # 6. SICA scores + NLI probability weighted combination
    for w in [5, 10, 20, 50]:
        res = strategy_sica_nli_weighted_vote(problems, nli_weight=w)
        strategies[f'sica_nli_weighted_w{w}'] = {
            'results': res,
            'description': f'SICA MAX-SAT scores + NLI probs × {w}',
        }

    # 7. Oracle upper bound
    res = strategy_oracle(problems)
    strategies['oracle'] = {
        'results': res,
        'description': 'Perfect arbitrator between SICA and NLI (upper bound)',
    }

    # Compute metrics
    print(f'\n{"="*70}')
    print(f'R+G COMBO RESULTS (n={n})')
    print(f'{"="*70}')
    print(f'{"Strategy":<35} {"Acc":>7} {"Correct":>8} {"Delta/SC":>9} {"Delta/SICA":>11}')
    print('-' * 70)
    print(f'{"SC baseline":<35} {sc_acc:>6.2%} {sum(sc_correct_list):>8}')
    print(f'{"SICA baseline":<35} {sica_acc:>6.2%} {sum(sica_correct_list):>8} {sica_acc-sc_acc:>+8.2%}')
    print(f'{"NLI standalone":<35} {nli_acc:>6.2%} {sum(nli_correct_list):>8} {nli_acc-sc_acc:>+8.2%}')
    print('-' * 70)

    output_strategies = {}
    best_acc = 0
    best_name = ''

    for name, strat in strategies.items():
        res = strat['results']
        correct_list = [r['correct'] for r in res]
        acc = sum(correct_list) / n
        correct_count = sum(correct_list)
        delta_sc = acc - sc_acc
        delta_sica = acc - sica_acc

        if name != 'oracle' and acc > best_acc:
            best_acc = acc
            best_name = name

        mcnemar_vs_sc = mcnemar_test(correct_list, sc_correct_list)
        mcnemar_vs_sica = mcnemar_test(correct_list, sica_correct_list)

        per_class = compute_per_class(res, problems)

        label = name[:35]
        sig_sc = '*' if mcnemar_vs_sc['p_value'] < 0.05 else ''
        print(f'{label:<35} {acc:>6.2%} {correct_count:>8} {delta_sc:>+8.2%}{sig_sc} {delta_sica:>+10.2%}')

        output_entry = {
            'description': strat['description'],
            'accuracy': round(acc, 4),
            'correct': correct_count,
            'delta_vs_sc': round(delta_sc, 4),
            'delta_vs_sica': round(delta_sica, 4),
            'mcnemar_vs_sc': mcnemar_vs_sc,
            'mcnemar_vs_sica': mcnemar_vs_sica,
            'per_class': per_class,
        }

        for k in ('agree_count', 'agree_pct', 'nli_used', 'nli_used_pct', 'sica_used', 'sica_used_pct'):
            if k in strat:
                output_entry[k] = strat[k]

        output_strategies[name] = output_entry

    print(f'{"="*70}')
    print(f'* = McNemar p<0.05 vs SC')
    print(f'\nBest non-oracle strategy: {best_name} ({best_acc:.2%})')

    # Agreement analysis
    agree_sica_nli = sum(1 for p in problems if p['sica_answer'] == p['deberta_pred'])
    agree_correct = sum(1 for p in problems if p['sica_answer'] == p['deberta_pred'] and p['sica_correct'])
    disagree_count = n - agree_sica_nli
    disagree_sica_right = sum(1 for p in problems if p['sica_answer'] != p['deberta_pred'] and p['sica_correct'])
    disagree_nli_right = sum(1 for p in problems if p['sica_answer'] != p['deberta_pred'] and p['deberta_correct'])
    disagree_both_wrong = disagree_count - disagree_sica_right - disagree_nli_right

    agreement_analysis = {
        'agree': agree_sica_nli,
        'agree_pct': round(agree_sica_nli / n * 100, 1),
        'agree_accuracy': round(agree_correct / agree_sica_nli, 4) if agree_sica_nli > 0 else 0,
        'disagree': disagree_count,
        'disagree_sica_correct': disagree_sica_right,
        'disagree_nli_correct': disagree_nli_right,
        'disagree_both_wrong': disagree_both_wrong,
    }

    print(f'\nAgreement analysis:')
    print(f'  SICA ∩ NLI agree: {agree_sica_nli}/{n} ({agree_sica_nli/n:.1%}), '
          f'accuracy when agree: {agree_correct}/{agree_sica_nli} ({agree_correct/agree_sica_nli:.2%})')
    print(f'  Disagree: {disagree_count}/{n}')
    print(f'    SICA correct: {disagree_sica_right}, NLI correct: {disagree_nli_right}, '
          f'Both wrong: {disagree_both_wrong}')

    # Correlation analysis: NLI confidence vs correctness
    nli_confs = [max(p['deberta_probs'].values()) for p in problems]
    nli_correct_when_high = sum(1 for p, c in zip(problems, nli_confs) if c >= 0.8 and p['deberta_correct'])
    nli_total_high = sum(1 for c in nli_confs if c >= 0.8)
    nli_correct_when_low = sum(1 for p, c in zip(problems, nli_confs) if c < 0.8 and p['deberta_correct'])
    nli_total_low = sum(1 for c in nli_confs if c < 0.8)

    confidence_analysis = {
        'nli_high_conf_ge80': {
            'count': nli_total_high,
            'correct': nli_correct_when_high,
            'accuracy': round(nli_correct_when_high / nli_total_high, 4) if nli_total_high > 0 else 0,
        },
        'nli_low_conf_lt80': {
            'count': nli_total_low,
            'correct': nli_correct_when_low,
            'accuracy': round(nli_correct_when_low / nli_total_low, 4) if nli_total_low > 0 else 0,
        },
    }

    print(f'\nNLI confidence analysis:')
    print(f'  High conf (≥0.8): {nli_total_high} problems, '
          f'acc={nli_correct_when_high}/{nli_total_high} '
          f'({nli_correct_when_high/nli_total_high:.2%})')
    print(f'  Low conf (<0.8):  {nli_total_low} problems, '
          f'acc={nli_correct_when_low}/{nli_total_low} '
          f'({nli_correct_when_low/nli_total_low:.2%})')

    # Per-question detail for best strategy
    best_results = strategies[best_name]['results']
    per_question_detail = {}
    for r, p in zip(best_results, problems):
        per_question_detail[p['pid']] = {
            'gold': p['gold'],
            'combo_answer': r['answer'],
            'combo_correct': r['correct'],
            'combo_source': r['source'],
            'sica_answer': p['sica_answer'],
            'sica_correct': p['sica_correct'],
            'deberta_pred': p['deberta_pred'],
            'deberta_correct': p['deberta_correct'],
            'sc_answer': p['sc_answer'],
            'sc_correct': p['sc_correct'],
        }

    # Save
    os.makedirs(args.output_dir, exist_ok=True)

    output = {
        'baselines': {
            'sc': {'accuracy': round(sc_acc, 4), 'correct': sum(sc_correct_list)},
            'sica': {'accuracy': round(sica_acc, 4), 'correct': sum(sica_correct_list)},
            'nli_standalone': {'accuracy': round(nli_acc, 4), 'correct': sum(nli_correct_list)},
        },
        'n_problems': n,
        'best_strategy': best_name,
        'best_accuracy': round(best_acc, 4),
        'strategies': output_strategies,
        'agreement_analysis': agreement_analysis,
        'confidence_analysis': confidence_analysis,
        'note': 'Using standard SICA (not SICA-G decoupling) since G only has 5 test problems. '
                'When full G results are available, re-run with --g-results flag.',
    }

    out_file = os.path.join(args.output_dir, 'results.json')
    with open(out_file, 'w') as f:
        json.dump(output, f, indent=2)
    print(f'\nSummary saved to {out_file}')

    detail_file = os.path.join(args.output_dir, 'per_question_best.json')
    with open(detail_file, 'w') as f:
        json.dump(per_question_detail, f, indent=2)
    print(f'Per-question detail saved to {detail_file}')


if __name__ == '__main__':
    main()
