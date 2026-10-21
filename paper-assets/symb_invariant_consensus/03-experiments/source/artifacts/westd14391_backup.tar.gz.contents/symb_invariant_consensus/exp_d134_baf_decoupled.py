# exp-d134-baf-decoupled: Bias Ratio analysis for decoupled constraint extraction
# Compares BR between full-trace and truncated-trace FOL constraint extraction
# Uses cached results from exp033 (full) and direction_g (truncated)

import json
import os
import numpy as np
from scipy import stats
from collections import Counter

EXP033_RESULTS = '/root/symb_invariant_consensus/results/exp033_mistral_7b_folio204/exp033_results.json'
DECOUPLING_DIR = '/root/symb_invariant_consensus/results/direction_g_decoupling'
OUTPUT_DIR = '/root/symb_invariant_consensus/results/exp_d134_baf_decoupled'

STRATEGIES = ['conservative', 'standard', 'aggressive']


def normalize_answer(ans):
    ans = str(ans).strip().lower()
    if ans in ('true', 'yes', 't'):
        return 'True'
    elif ans in ('false', 'no', 'f'):
        return 'False'
    elif ans in ('unknown', 'uncertain', 'u', 'undetermined'):
        return 'Unknown'
    return ans.capitalize()


def compute_br(scores, gt, predicted):
    """Compute bias ratio: score[wrong_answer] / score[gold_answer]."""
    if gt == predicted:
        return None
    wrong_score = scores.get(predicted, 0)
    gold_score = scores.get(gt, 0)
    if not isinstance(wrong_score, (int, float)) or not isinstance(gold_score, (int, float)):
        return None
    if gold_score > 0:
        return wrong_score / gold_score
    elif wrong_score > 0:
        return float('inf')
    return None


def run_analysis():
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    with open(EXP033_RESULTS) as f:
        exp033 = json.load(f)
    full_results = {r['problem_id']: r for r in exp033['results']}

    all_strategy_results = {}
    for strategy in STRATEGIES:
        path = os.path.join(DECOUPLING_DIR, f'per_problem_{strategy}.json')
        with open(path) as f:
            data = json.load(f)
        all_strategy_results[strategy] = {r['pid']: r for r in data}

    n_problems = len(full_results)
    print(f"Loaded {n_problems} problems from exp033")
    print(f"Strategies: {STRATEGIES}")
    print()

    output = {
        'exp_id': 'exp-d134-baf-decoupled',
        'dataset': 'FOLIO-204',
        'model': 'Mistral-7B-Instruct-v0.3',
        'K': 12,
        'n_problems': n_problems,
        'source_full': 'exp033_mistral_7b_folio204',
        'source_truncated': 'direction_g_decoupling',
    }

    # Full-trace baseline BR
    full_br_list = []
    full_wrong_pids = []
    for pid, r in full_results.items():
        gt = normalize_answer(r['ground_truth'])
        pred = normalize_answer(r['sica_answer'])
        if gt != pred:
            br = compute_br(r.get('sica_scores', {}), gt, pred)
            full_wrong_pids.append(pid)
            full_br_list.append({'pid': pid, 'gt': gt, 'pred': pred, 'br': br})

    full_finite_brs = [x['br'] for x in full_br_list if x['br'] is not None and x['br'] != float('inf')]
    n_full_wrong = len(full_wrong_pids)
    n_full_inf = sum(1 for x in full_br_list if x['br'] == float('inf'))

    output['full_trace'] = {
        'sica_acc': round(sum(1 for r in full_results.values() if normalize_answer(r['ground_truth']) == normalize_answer(r['sica_answer'])) / n_problems, 4),
        'sica_correct': sum(1 for r in full_results.values() if normalize_answer(r['ground_truth']) == normalize_answer(r['sica_answer'])),
        'n_sica_wrong': n_full_wrong,
        'br_mean': round(float(np.mean(full_finite_brs)), 4) if full_finite_brs else None,
        'br_median': round(float(np.median(full_finite_brs)), 4) if full_finite_brs else None,
        'br_std': round(float(np.std(full_finite_brs)), 4) if full_finite_brs else None,
        'n_br_finite': len(full_finite_brs),
        'n_br_infinite': n_full_inf,
        'constraints_total': sum(r.get('constraints_stats', {}).get('total_extracted', 0) for r in full_results.values()),
        'constraints_unique': sum(r.get('constraints_stats', {}).get('unique_after_dedup', 0) for r in full_results.values()),
    }

    print(f"{'='*70}")
    print(f"FULL-TRACE BASELINE")
    print(f"{'='*70}")
    print(f"  SICA acc:        {output['full_trace']['sica_acc']:.4f} ({output['full_trace']['sica_correct']}/{n_problems})")
    print(f"  SICA wrong:      {n_full_wrong}")
    print(f"  BR mean:         {output['full_trace']['br_mean']}")
    print(f"  BR median:       {output['full_trace']['br_median']}")
    print(f"  BR std:          {output['full_trace']['br_std']}")
    print(f"  Constraints:     {output['full_trace']['constraints_total']} total, {output['full_trace']['constraints_unique']} unique")
    print()

    output['strategies'] = {}

    for strategy in STRATEGIES:
        trunc_data = all_strategy_results[strategy]

        trunc_br_list = []
        trunc_wrong_pids = []
        for pid, r in trunc_data.items():
            gt = normalize_answer(r['gt'])
            pred = normalize_answer(r['sica_answer'])
            if gt != pred:
                br = compute_br(r.get('scores', {}), gt, pred)
                trunc_wrong_pids.append(pid)
                trunc_br_list.append({'pid': pid, 'gt': gt, 'pred': pred, 'br': br})

        trunc_finite_brs = [x['br'] for x in trunc_br_list if x['br'] is not None and x['br'] != float('inf')]
        n_trunc_wrong = len(trunc_wrong_pids)
        n_trunc_inf = sum(1 for x in trunc_br_list if x['br'] == float('inf'))

        trunc_correct = sum(1 for r in trunc_data.values() if r.get('sica_correct', False))
        trunc_acc = round(trunc_correct / n_problems, 4)

        avg_trunc_pct = np.mean([r.get('avg_pct_removed', 0) for r in trunc_data.values()])

        total_constraints = sum(r.get('constraints_stats', {}).get('total_extracted', 0) for r in trunc_data.values())
        unique_constraints = sum(r.get('constraints_stats', {}).get('unique_after_dedup', 0) for r in trunc_data.values())

        # --- Paired BR comparison ---
        # For problems where BOTH full and truncated got it wrong, compute paired BRs
        common_wrong = set(full_wrong_pids) & set(trunc_wrong_pids)
        full_br_map = {x['pid']: x['br'] for x in full_br_list}
        trunc_br_map = {x['pid']: x['br'] for x in trunc_br_list}

        paired_full = []
        paired_trunc = []
        paired_pids = []
        for pid in sorted(common_wrong):
            br_f = full_br_map.get(pid)
            br_t = trunc_br_map.get(pid)
            if br_f is not None and br_t is not None and br_f != float('inf') and br_t != float('inf'):
                paired_full.append(br_f)
                paired_trunc.append(br_t)
                paired_pids.append(pid)

        n_paired = len(paired_full)
        br_deltas = [t - f for f, t in zip(paired_full, paired_trunc)]

        wilcoxon_result = None
        if n_paired >= 10:
            try:
                stat, p_val = stats.wilcoxon(paired_trunc, paired_full, alternative='less')
                wilcoxon_result = {
                    'statistic': round(float(stat), 4),
                    'p_value': round(float(p_val), 6),
                    'n_pairs': n_paired,
                    'alternative': 'truncated < full (one-sided)',
                    'significant_005': bool(p_val < 0.05),
                }
            except Exception as e:
                wilcoxon_result = {'error': str(e), 'n_pairs': n_paired}

        # --- McNemar test: accuracy comparison full vs truncated ---
        a, b, c, d = 0, 0, 0, 0
        for pid in full_results:
            full_correct = normalize_answer(full_results[pid]['ground_truth']) == normalize_answer(full_results[pid]['sica_answer'])
            trunc_r = trunc_data.get(pid)
            if trunc_r is None:
                continue
            trunc_correct_i = trunc_r.get('sica_correct', False)
            if full_correct and trunc_correct_i:
                a += 1
            elif full_correct and not trunc_correct_i:
                b += 1
            elif not full_correct and trunc_correct_i:
                c += 1
            else:
                d += 1

        mcnemar_result = None
        if b + c > 0:
            try:
                # exact McNemar
                n_disc = b + c
                p_mcnemar = float(stats.binomtest(min(b, c), n_disc, 0.5).pvalue)
                mcnemar_result = {
                    'b_full_right_trunc_wrong': b,
                    'c_full_wrong_trunc_right': c,
                    'n_discordant': n_disc,
                    'p_value': round(p_mcnemar, 6),
                    'significant_005': bool(p_mcnemar < 0.05),
                    'accuracy_delta_pp': round((trunc_acc - output['full_trace']['sica_acc']) * 100, 2),
                }
            except Exception as e:
                mcnemar_result = {'error': str(e)}

        strategy_output = {
            'sica_acc': trunc_acc,
            'sica_correct': trunc_correct,
            'n_sica_wrong': n_trunc_wrong,
            'br_mean': round(float(np.mean(trunc_finite_brs)), 4) if trunc_finite_brs else None,
            'br_median': round(float(np.median(trunc_finite_brs)), 4) if trunc_finite_brs else None,
            'br_std': round(float(np.std(trunc_finite_brs)), 4) if trunc_finite_brs else None,
            'n_br_finite': len(trunc_finite_brs),
            'n_br_infinite': n_trunc_inf,
            'truncation_ratio_mean': round(float(avg_trunc_pct), 2),
            'constraints_total': total_constraints,
            'constraints_unique': unique_constraints,
        }

        comparison = {
            'br_delta_mean': round(float(np.mean(br_deltas)), 4) if br_deltas else None,
            'br_delta_median': round(float(np.median(br_deltas)), 4) if br_deltas else None,
            'n_paired': n_paired,
            'n_common_wrong': len(common_wrong),
            'n_br_decreased': sum(1 for d in br_deltas if d < 0),
            'n_br_increased': sum(1 for d in br_deltas if d > 0),
            'n_br_unchanged': sum(1 for d in br_deltas if d == 0),
            'wilcoxon': wilcoxon_result,
            'mcnemar': mcnemar_result,
        }

        output['strategies'][strategy] = {
            'truncated_trace': strategy_output,
            'comparison': comparison,
        }

        print(f"{'='*70}")
        print(f"STRATEGY: {strategy.upper()} (avg truncation: {avg_trunc_pct:.1f}%)")
        print(f"{'='*70}")
        print(f"  SICA acc:        {trunc_acc:.4f} ({trunc_correct}/{n_problems})")
        print(f"  SICA wrong:      {n_trunc_wrong}")
        print(f"  BR mean:         {strategy_output['br_mean']}")
        print(f"  BR median:       {strategy_output['br_median']}")
        print(f"  Constraints:     {total_constraints} total, {unique_constraints} unique")
        print()
        print(f"  --- Paired BR comparison (n={n_paired}, common wrong={len(common_wrong)}) ---")
        if br_deltas:
            print(f"  BR delta mean:   {comparison['br_delta_mean']} (negative = truncated lower)")
            print(f"  BR delta median: {comparison['br_delta_median']}")
            print(f"  BR decreased:    {comparison['n_br_decreased']}/{n_paired}")
            print(f"  BR increased:    {comparison['n_br_increased']}/{n_paired}")
        if wilcoxon_result and 'p_value' in wilcoxon_result:
            sig = '*' if wilcoxon_result['significant_005'] else 'ns'
            print(f"  Wilcoxon p:      {wilcoxon_result['p_value']:.6f} ({sig})")
        if mcnemar_result and 'p_value' in mcnemar_result:
            sig = '*' if mcnemar_result['significant_005'] else 'ns'
            print(f"  McNemar p:       {mcnemar_result['p_value']:.6f} ({sig}), delta={mcnemar_result['accuracy_delta_pp']:+.2f}pp")
            print(f"    b(full✓ trunc✗)={mcnemar_result['b_full_right_trunc_wrong']}, c(full✗ trunc✓)={mcnemar_result['c_full_wrong_trunc_right']}")
        print()

    # --- Per-question detail for standard strategy ---
    std_trunc = all_strategy_results['standard']
    per_question_detail = []
    for pid in sorted(full_results.keys()):
        fr = full_results[pid]
        tr = std_trunc.get(pid, {})

        gt = normalize_answer(fr['ground_truth'])
        full_pred = normalize_answer(fr['sica_answer'])
        trunc_pred = normalize_answer(tr.get('sica_answer', ''))
        full_correct = gt == full_pred
        trunc_correct = tr.get('sica_correct', False)

        full_br_val = compute_br(fr.get('sica_scores', {}), gt, full_pred) if not full_correct else None
        trunc_br_val = compute_br(tr.get('scores', {}), gt, trunc_pred) if not trunc_correct else None

        detail = {
            'pid': pid,
            'gt': gt,
            'full_pred': full_pred,
            'full_correct': full_correct,
            'full_scores': fr.get('sica_scores', {}),
            'full_br': full_br_val if full_br_val != float('inf') else 'inf',
            'trunc_pred': trunc_pred,
            'trunc_correct': trunc_correct,
            'trunc_scores': tr.get('scores', {}),
            'trunc_br': trunc_br_val if trunc_br_val != float('inf') else 'inf',
            'trunc_pct_removed': tr.get('avg_pct_removed', 0),
        }
        per_question_detail.append(detail)

    # Save results
    results_file = os.path.join(OUTPUT_DIR, 'results.json')
    with open(results_file, 'w') as f:
        json.dump(output, f, indent=2, ensure_ascii=False)
    print(f"Summary saved to {results_file}")

    detail_file = os.path.join(OUTPUT_DIR, 'per_question_detail.json')
    with open(detail_file, 'w') as f:
        json.dump(per_question_detail, f, indent=2, ensure_ascii=False)
    print(f"Per-question detail saved to {detail_file}")

    # --- Summary table ---
    print()
    print(f"{'='*70}")
    print(f"SUMMARY TABLE")
    print(f"{'='*70}")
    print(f"{'Condition':<20} {'Acc':>7} {'Wrong':>6} {'BR mean':>9} {'BR med':>8} {'Trunc%':>7}")
    print(f"{'-'*20} {'-'*7} {'-'*6} {'-'*9} {'-'*8} {'-'*7}")
    fa = output['full_trace']
    print(f"{'Full trace':<20} {fa['sica_acc']:>7.4f} {fa['n_sica_wrong']:>6} {fa['br_mean'] or 'N/A':>9} {fa['br_median'] or 'N/A':>8} {'0.0':>7}")
    for strategy in STRATEGIES:
        sa = output['strategies'][strategy]['truncated_trace']
        print(f"{'Trunc-'+strategy:<20} {sa['sica_acc']:>7.4f} {sa['n_sica_wrong']:>6} {sa['br_mean'] or 'N/A':>9} {sa['br_median'] or 'N/A':>8} {sa['truncation_ratio_mean']:>7.1f}")
    print(f"{'='*70}")


if __name__ == '__main__':
    run_analysis()
