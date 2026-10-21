"""
Direction G+R Combo: Decoupling + NLI External Verifier
Combines G (truncation-based debiasing) with R (DeBERTa NLI verifier).

Inputs:
  --g-results: G per-problem JSON (e.g. per_problem_conservative.json)
  --r-results: R results JSON (supports both r_nli_small and r_nli_large formats)
  --baseline:  exp033 results JSON (for SC/SICA baselines)
Output:
  results/direction_gr_combo/results.json
"""
import json
import os
import argparse
from collections import Counter

OUTPUT_DIR = '/root/symb_invariant_consensus/results/direction_gr_combo'

NLI_TO_ANSWER = {
    'ENTAILMENT': 'True',
    'CONTRADICTION': 'False',
    'NEUTRAL': 'Unknown',
}


def normalize_answer(ans):
    ans = str(ans).strip().lower()
    if ans in ('true', 'yes', 't'):
        return 'True'
    elif ans in ('false', 'no', 'f'):
        return 'False'
    elif ans in ('unknown', 'uncertain', 'u', 'undetermined'):
        return 'Unknown'
    return ans.capitalize()


def load_g_results(path):
    with open(path) as f:
        data = json.load(f)
    out = {}
    for item in data:
        pid = item['pid']
        out[pid] = {
            'sica_g_answer': normalize_answer(item['sica_answer']),
            'sica_g_correct': item['sica_correct'],
            'sica_g_scores': item.get('scores', {}),
            'gt': normalize_answer(item['gt']),
        }
    return out


def load_r_results(path):
    with open(path) as f:
        data = json.load(f)
    out = {}
    if 'per_question' in data:
        for pid, item in data['per_question'].items():
            out[pid] = {
                'nli_answer': normalize_answer(item['deberta_pred']),
                'nli_probs': {normalize_answer(k): v for k, v in item['deberta_probs'].items()},
                'nli_correct': item.get('deberta_correct', False),
            }
    elif 'results' in data and isinstance(data['results'], list):
        for item in data['results']:
            pid = item['id']
            probs_mapped = {}
            for nli_label, prob in item.get('nli_probs', {}).items():
                ans = NLI_TO_ANSWER.get(nli_label, nli_label)
                probs_mapped[ans] = prob
            out[pid] = {
                'nli_answer': normalize_answer(item['nli_answer']),
                'nli_probs': probs_mapped,
                'nli_correct': item.get('nli_correct', False),
            }
    return out


def load_baseline(path):
    with open(path) as f:
        data = json.load(f)
    out = {}
    for item in data['results']:
        pid = item['problem_id']
        out[pid] = {
            'sc_answer': normalize_answer(item['sc_answer']),
            'sica_answer': normalize_answer(item['sica_answer']),
            'gt': normalize_answer(item['ground_truth']),
            'sc_correct': normalize_answer(item['sc_answer']) == normalize_answer(item['ground_truth']),
            'sica_correct': normalize_answer(item['sica_answer']) == normalize_answer(item['ground_truth']),
        }
    return out


def nli_confidence(nli_probs):
    if not nli_probs:
        return 0.0
    return max(nli_probs.values())


def nli_margin(nli_probs):
    if not nli_probs or len(nli_probs) < 2:
        return 0.0
    sorted_probs = sorted(nli_probs.values(), reverse=True)
    return sorted_probs[0] - sorted_probs[1]


# ── Combo Strategies ──

def strategy_gr_vote(g, r, baseline):
    """SICA-G + NLI as 2 votes; SC as tiebreaker."""
    votes = Counter()
    votes[g['sica_g_answer']] += 1
    votes[r['nli_answer']] += 1
    top = votes.most_common()
    if len(top) == 1 or top[0][1] > top[1][1]:
        return top[0][0]
    return baseline['sc_answer']


def strategy_gr_intersection(g, r, baseline):
    """Agree → use shared answer. Disagree → SC fallback."""
    if g['sica_g_answer'] == r['nli_answer']:
        return g['sica_g_answer']
    return baseline['sc_answer']


def strategy_gr_intersection_sica(g, r, baseline):
    """Agree → use shared answer. Disagree → original SICA fallback."""
    if g['sica_g_answer'] == r['nli_answer']:
        return g['sica_g_answer']
    return baseline['sica_answer']


def strategy_gr_cascade_nli_first(g, r, baseline, threshold=0.7):
    """NLI high confidence → NLI. Else → SICA-G."""
    if nli_confidence(r['nli_probs']) >= threshold:
        return r['nli_answer']
    return g['sica_g_answer']


def strategy_gr_cascade_g_first(g, r, baseline, margin_threshold=0.3):
    """SICA-G default. If G scores are close (margin < threshold) and NLI is confident → override with NLI."""
    g_scores = g.get('sica_g_scores', {})
    if g_scores:
        sorted_scores = sorted(g_scores.values(), reverse=True)
        if len(sorted_scores) >= 2:
            g_margin = sorted_scores[0] - sorted_scores[1]
        else:
            g_margin = sorted_scores[0] if sorted_scores else 0
    else:
        g_margin = 0

    if g_margin < margin_threshold and nli_confidence(r['nli_probs']) >= 0.7:
        return r['nli_answer']
    return g['sica_g_answer']


def strategy_nli_override_on_disagree(g, r, baseline, threshold=0.85):
    """Use SICA-G by default. If NLI disagrees with very high confidence → override."""
    if g['sica_g_answer'] != r['nli_answer'] and nli_confidence(r['nli_probs']) >= threshold:
        return r['nli_answer']
    return g['sica_g_answer']


def strategy_majority_3way(g, r, baseline):
    """3-way majority: SICA-G, NLI, SC."""
    votes = Counter()
    votes[g['sica_g_answer']] += 1
    votes[r['nli_answer']] += 1
    votes[baseline['sc_answer']] += 1
    return votes.most_common(1)[0][0]


def strategy_majority_4way(g, r, baseline):
    """4-way majority: SICA-G, NLI, SC, original SICA."""
    votes = Counter()
    votes[g['sica_g_answer']] += 1
    votes[r['nli_answer']] += 1
    votes[baseline['sc_answer']] += 1
    votes[baseline['sica_answer']] += 1
    top = votes.most_common()
    if top[0][1] > 1:
        return top[0][0]
    return baseline['sica_answer']


STRATEGIES = {
    'gr_vote': strategy_gr_vote,
    'gr_intersection_sc': strategy_gr_intersection,
    'gr_intersection_sica': strategy_gr_intersection_sica,
    'gr_cascade_nli_first_0.7': lambda g, r, b: strategy_gr_cascade_nli_first(g, r, b, 0.7),
    'gr_cascade_nli_first_0.8': lambda g, r, b: strategy_gr_cascade_nli_first(g, r, b, 0.8),
    'gr_cascade_nli_first_0.9': lambda g, r, b: strategy_gr_cascade_nli_first(g, r, b, 0.9),
    'nli_override_0.85': lambda g, r, b: strategy_nli_override_on_disagree(g, r, b, 0.85),
    'nli_override_0.90': lambda g, r, b: strategy_nli_override_on_disagree(g, r, b, 0.90),
    'majority_3way': strategy_majority_3way,
    'majority_4way': strategy_majority_4way,
}


# ── Statistical Tests ──

def mcnemar_test(correct_a, correct_b):
    """McNemar's test: are two classifiers significantly different?"""
    n01 = sum(1 for a, b in zip(correct_a, correct_b) if a and not b)
    n10 = sum(1 for a, b in zip(correct_a, correct_b) if not a and b)
    n = n01 + n10
    if n == 0:
        return {'chi2': 0, 'p_value': 1.0, 'n01': n01, 'n10': n10}
    chi2 = (abs(n01 - n10) - 1) ** 2 / n if n > 0 else 0
    from scipy.stats import chi2 as chi2_dist
    p = 1 - chi2_dist.cdf(chi2, df=1)
    return {'chi2': round(chi2, 4), 'p_value': round(p, 4), 'n01': n01, 'n10': n10}


def run_analysis(g_data, r_data, baselines, problem_ids):
    n = len(problem_ids)
    results = {}

    sc_correct = [baselines[pid]['sc_correct'] for pid in problem_ids]
    sica_correct = [baselines[pid]['sica_correct'] for pid in problem_ids]
    g_correct = [g_data[pid]['sica_g_correct'] for pid in problem_ids]

    baselines_summary = {
        'sc': {'accuracy': round(sum(sc_correct) / n, 4), 'correct': sum(sc_correct)},
        'sica': {'accuracy': round(sum(sica_correct) / n, 4), 'correct': sum(sica_correct)},
        'sica_g': {'accuracy': round(sum(g_correct) / n, 4), 'correct': sum(g_correct)},
    }

    per_problem = []
    strategy_results = {}

    for name, strategy_fn in STRATEGIES.items():
        preds = []
        corrects = []
        details = []
        for pid in problem_ids:
            g = g_data[pid]
            r = r_data[pid]
            b = baselines[pid]
            gt = g['gt']
            pred = strategy_fn(g, r, b)
            correct = pred == gt
            preds.append(pred)
            corrects.append(correct)
            details.append({
                'pid': pid,
                'gt': gt,
                'combo_answer': pred,
                'combo_correct': correct,
                'sica_g_answer': g['sica_g_answer'],
                'nli_answer': r['nli_answer'],
                'sc_answer': b['sc_answer'],
                'sica_answer': b['sica_answer'],
            })

        acc = sum(corrects) / n
        correct_count = sum(corrects)
        delta_sc = acc - baselines_summary['sc']['accuracy']
        delta_sica = acc - baselines_summary['sica']['accuracy']
        delta_g = acc - baselines_summary['sica_g']['accuracy']

        mcnemar_vs_sc = mcnemar_test(corrects, sc_correct)
        mcnemar_vs_sica = mcnemar_test(corrects, sica_correct)
        mcnemar_vs_g = mcnemar_test(corrects, g_correct)

        per_label = {}
        for label in ['True', 'False', 'Unknown']:
            label_ids = [pid for pid in problem_ids if g_data[pid]['gt'] == label]
            if label_ids:
                label_correct = sum(1 for d in details if d['gt'] == label and d['combo_correct'])
                per_label[label] = {
                    'n': len(label_ids),
                    'correct': label_correct,
                    'accuracy': round(label_correct / len(label_ids), 4),
                }

        strategy_results[name] = {
            'accuracy': round(acc, 4),
            'correct': correct_count,
            'delta_vs_sc': round(delta_sc, 4),
            'delta_vs_sica': round(delta_sica, 4),
            'delta_vs_sica_g': round(delta_g, 4),
            'per_label': per_label,
            'mcnemar_vs_sc': mcnemar_vs_sc,
            'mcnemar_vs_sica': mcnemar_vs_sica,
            'mcnemar_vs_sica_g': mcnemar_vs_g,
            'per_problem': details,
        }

    gr_agree = sum(1 for pid in problem_ids
                   if g_data[pid]['sica_g_answer'] == r_data[pid]['nli_answer'])
    gr_disagree = n - gr_agree
    agree_ids = [pid for pid in problem_ids
                 if g_data[pid]['sica_g_answer'] == r_data[pid]['nli_answer']]
    disagree_ids = [pid for pid in problem_ids
                    if g_data[pid]['sica_g_answer'] != r_data[pid]['nli_answer']]

    agree_correct = sum(1 for pid in agree_ids
                        if g_data[pid]['sica_g_correct'])
    disagree_g_correct = sum(1 for pid in disagree_ids
                             if g_data[pid]['sica_g_correct'])
    disagree_r_correct = sum(1 for pid in disagree_ids
                             if r_data[pid]['nli_correct'])
    disagree_both_wrong = sum(1 for pid in disagree_ids
                              if not g_data[pid]['sica_g_correct'] and not r_data[pid]['nli_correct'])

    agreement_analysis = {
        'agree': gr_agree,
        'disagree': gr_disagree,
        'agree_accuracy': round(agree_correct / max(gr_agree, 1), 4),
        'disagree_g_correct': disagree_g_correct,
        'disagree_r_correct': disagree_r_correct,
        'disagree_both_wrong': disagree_both_wrong,
    }

    return {
        'n_problems': n,
        'baselines': baselines_summary,
        'agreement_analysis': agreement_analysis,
        'strategies': {k: {kk: vv for kk, vv in v.items() if kk != 'per_problem'}
                       for k, v in strategy_results.items()},
        'per_problem_details': {k: v['per_problem'] for k, v in strategy_results.items()},
    }


def print_summary(results):
    n = results['n_problems']
    baselines = results['baselines']
    print(f'\n{"="*70}')
    print(f'G+R COMBO RESULTS (n={n})')
    print(f'{"="*70}')
    print(f'  SC baseline:     {baselines["sc"]["correct"]}/{n} = {baselines["sc"]["accuracy"]:.4f}')
    print(f'  SICA (original): {baselines["sica"]["correct"]}/{n} = {baselines["sica"]["accuracy"]:.4f}')
    print(f'  SICA-G (debiased): {baselines["sica_g"]["correct"]}/{n} = {baselines["sica_g"]["accuracy"]:.4f}')

    aa = results['agreement_analysis']
    print(f'\n  G vs R agreement: {aa["agree"]}/{n} ({aa["agree"]/n:.1%})')
    print(f'    Agree accuracy: {aa["agree_accuracy"]:.4f}')
    print(f'    Disagree: G correct={aa["disagree_g_correct"]}, R correct={aa["disagree_r_correct"]}, both wrong={aa["disagree_both_wrong"]}')

    print(f'\n{"─"*70}')
    print(f'  {"Strategy":<30} {"Acc":>6} {"Cor":>4} {"ΔSC":>7} {"ΔSICA":>7} {"ΔG":>7} {"p(SC)":>7} {"p(SICA)":>7}')
    print(f'  {"─"*30} {"─"*6} {"─"*4} {"─"*7} {"─"*7} {"─"*7} {"─"*7} {"─"*7}')

    for name, s in sorted(results['strategies'].items(), key=lambda x: -x[1]['accuracy']):
        p_sc = s['mcnemar_vs_sc']['p_value']
        p_sica = s['mcnemar_vs_sica']['p_value']
        sig_sc = '*' if p_sc < 0.05 else ''
        sig_sica = '*' if p_sica < 0.05 else ''
        print(f'  {name:<30} {s["accuracy"]:>6.4f} {s["correct"]:>4} '
              f'{s["delta_vs_sc"]:>+7.4f} {s["delta_vs_sica"]:>+7.4f} {s["delta_vs_sica_g"]:>+7.4f} '
              f'{p_sc:>6.4f}{sig_sc} {p_sica:>6.4f}{sig_sica}')
    print(f'{"="*70}')


def main():
    parser = argparse.ArgumentParser(description='G+R Combo: Decoupling + NLI Verifier')
    parser.add_argument('--g-results', required=True,
                        help='Path to G per-problem JSON (e.g. per_problem_conservative.json)')
    parser.add_argument('--r-results', required=True,
                        help='Path to R results JSON (r_nli_small or r_nli_large)')
    parser.add_argument('--baseline', required=True,
                        help='Path to exp033 results JSON')
    parser.add_argument('--output-dir', default=OUTPUT_DIR)
    args = parser.parse_args()

    print(f'Loading G results from {args.g_results}')
    g_data = load_g_results(args.g_results)
    print(f'  Loaded {len(g_data)} problems')

    print(f'Loading R results from {args.r_results}')
    r_data = load_r_results(args.r_results)
    print(f'  Loaded {len(r_data)} problems')

    print(f'Loading baseline from {args.baseline}')
    baselines = load_baseline(args.baseline)
    print(f'  Loaded {len(baselines)} problems')

    common_ids = sorted(set(g_data.keys()) & set(r_data.keys()) & set(baselines.keys()))
    missing_g = set(r_data.keys()) - set(g_data.keys())
    missing_r = set(g_data.keys()) - set(r_data.keys())
    if missing_g:
        print(f'  WARNING: {len(missing_g)} problems in R but not in G')
    if missing_r:
        print(f'  WARNING: {len(missing_r)} problems in G but not in R')
    print(f'  Common problems: {len(common_ids)}')

    if not common_ids:
        print('ERROR: No common problems found. Check file formats.')
        return

    results = run_analysis(g_data, r_data, baselines, common_ids)
    print_summary(results)

    os.makedirs(args.output_dir, exist_ok=True)

    summary_out = {k: v for k, v in results.items() if k != 'per_problem_details'}
    with open(os.path.join(args.output_dir, 'results.json'), 'w') as f:
        json.dump(summary_out, f, indent=2)

    with open(os.path.join(args.output_dir, 'per_problem.json'), 'w') as f:
        json.dump(results['per_problem_details'], f, indent=2)

    print(f'\nSaved to {args.output_dir}/')


if __name__ == '__main__':
    main()
