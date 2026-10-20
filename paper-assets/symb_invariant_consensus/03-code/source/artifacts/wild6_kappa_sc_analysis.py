#!/usr/bin/env python3
"""Wild 6: κ-aware adaptive SC threshold analysis.

Analyzes whether per-question agreement level (majority fraction, entropy)
can be used to adaptively set SC voting thresholds.
"""

import json
import sys
import math
from collections import Counter


def load_results(path):
    with open(path) as f:
        return json.load(f)


def majority_vote(dist):
    """Standard majority vote with alphabetical tiebreak."""
    if not dist:
        return None, 0.0, 0
    total = sum(dist.values())
    if total == 0:
        return None, 0.0, 0
    max_count = max(dist.values())
    candidates = sorted([k for k, v in dist.items() if v == max_count])
    return candidates[0], max_count / total, total


def entropy(dist):
    total = sum(dist.values())
    if total == 0:
        return 0.0
    h = 0.0
    for count in dist.values():
        if count > 0:
            p = count / total
            h -= p * math.log2(p)
    return h


def analyze_experiment(data, name):
    problems = data.get('results', [])
    K = data.get('summary', {}).get('k', 12)
    n = len(problems)

    items = []
    for p in problems:
        dist = p.get('sc_vote_distribution', {})
        gt = p.get('ground_truth', '')
        answer, maj_frac, total_votes = majority_vote(dist)
        items.append({
            'id': p.get('problem_id', ''),
            'dist': dist,
            'gt': gt,
            'sc_answer': answer,
            'majority_frac': maj_frac,
            'total_votes': total_votes,
            'entropy': entropy(dist),
        })

    sc_correct = sum(1 for it in items if it['sc_answer'] == it['gt'])
    sc_acc = sc_correct / n

    out = {
        'experiment': name,
        'n': n,
        'K': K,
        'standard_sc': {'accuracy': round(sc_acc, 6), 'correct': sc_correct},
    }

    # === Per-regime accuracy (core analysis) ===
    regime_bounds = [
        ('unanimous',         lambda mf: mf >= 1.0),
        ('strong (>=0.75)',   lambda mf: 0.75 <= mf < 1.0),
        ('moderate (0.5-0.75)', lambda mf: 0.5 < mf < 0.75),
        ('weak (<=0.5)',      lambda mf: mf <= 0.5),
    ]
    per_regime = {}
    for rname, pred in regime_bounds:
        ri = [it for it in items if pred(it['majority_frac'])]
        rc = sum(1 for it in ri if it['sc_answer'] == it['gt'])
        rn = len(ri)
        per_regime[rname] = {
            'n': rn,
            'frac': round(rn / n, 4) if n else 0,
            'correct': rc,
            'accuracy': round(rc / rn, 6) if rn else None,
        }
    out['per_regime'] = per_regime

    # === Distribution stats ===
    mfs = [it['majority_frac'] for it in items]
    hs = [it['entropy'] for it in items]
    out['dist_stats'] = {
        'mean_majority_frac': round(sum(mfs) / len(mfs), 4),
        'mean_entropy': round(sum(hs) / len(hs), 4),
    }

    # === Strategy 1: Pure confidence threshold sweep ===
    threshold_sweep = {}
    for theta in [0.4, 0.5, 0.6, 0.667, 0.75, 0.8, 0.833, 0.9, 0.917, 1.0]:
        answered = [(it['sc_answer'], it['gt']) for it in items if it['majority_frac'] >= theta]
        c = sum(1 for a, g in answered if a == g)
        an = len(answered)
        threshold_sweep[str(theta)] = {
            'overall_acc': round(c / n, 6) if n else 0,
            'cond_acc': round(c / an, 6) if an else None,
            'coverage': round(an / n, 4) if n else 0,
            'answered': an,
            'correct': c,
        }
    out['threshold_sweep'] = threshold_sweep

    # === Strategy 2: Forward adaptive (medium zone needs supermajority) ===
    configs = {
        'conservative': {'high': 0.9, 'medium': 0.7, 'super': 0.8},
        'balanced':     {'high': 0.8, 'medium': 0.6, 'super': 0.7},
        'aggressive':   {'high': 0.7, 'medium': 0.5, 'super': 0.6},
    }
    adaptive_forward = {}
    for cname, p in configs.items():
        correct = 0
        abstained = 0
        for it in items:
            mf = it['majority_frac']
            if mf >= p['high'] or mf < p['medium']:
                if it['sc_answer'] == it['gt']:
                    correct += 1
            elif mf >= p['super']:
                if it['sc_answer'] == it['gt']:
                    correct += 1
            else:
                abstained += 1
        adaptive_forward[cname] = {
            'accuracy': round(correct / n, 6),
            'correct': correct,
            'abstained': abstained,
            'delta_vs_sc': round(correct / n - sc_acc, 6),
            'params': p,
        }
    out['adaptive_forward'] = adaptive_forward

    # === Strategy 3: Anti-groupthink (high agreement → abstain) ===
    anti_gt = {}
    for theta in [0.9, 0.917, 0.95, 1.0]:
        correct = 0
        abstained = 0
        for it in items:
            if it['majority_frac'] >= theta:
                abstained += 1
            elif it['sc_answer'] == it['gt']:
                correct += 1
        anti_gt[str(theta)] = {
            'accuracy': round(correct / n, 6),
            'correct': correct,
            'abstained': abstained,
            'delta_vs_sc': round(correct / n - sc_acc, 6),
        }
    out['antigroupthink_abstain'] = anti_gt

    # === Strategy 4: Second-answer flip for high agreement ===
    flip_results = {}
    for theta in [0.9, 0.917, 0.95, 1.0]:
        correct = 0
        flipped = 0
        for it in items:
            if it['majority_frac'] >= theta and len(it['dist']) > 1:
                sorted_a = sorted(it['dist'].items(), key=lambda x: (-x[1], x[0]))
                pred = sorted_a[1][0] if len(sorted_a) > 1 else it['sc_answer']
                flipped += 1
            else:
                pred = it['sc_answer']
            if pred == it['gt']:
                correct += 1
        flip_results[str(theta)] = {
            'accuracy': round(correct / n, 6),
            'correct': correct,
            'flipped': flipped,
            'delta_vs_sc': round(correct / n - sc_acc, 6),
        }
    out['second_answer_flip'] = flip_results

    # === Strategy 5: Entropy-aware (low entropy → require higher bar) ===
    entropy_results = {}
    for h_thresh in [0.5, 1.0, 1.5]:
        for req_mf in [0.8, 0.9, 1.0]:
            correct = 0
            abstained = 0
            for it in items:
                if it['entropy'] < h_thresh:
                    if it['majority_frac'] >= req_mf:
                        if it['sc_answer'] == it['gt']:
                            correct += 1
                    else:
                        abstained += 1
                else:
                    if it['sc_answer'] == it['gt']:
                        correct += 1
            key = f'h<{h_thresh}_req{req_mf}'
            entropy_results[key] = {
                'accuracy': round(correct / n, 6),
                'correct': correct,
                'abstained': abstained,
                'delta_vs_sc': round(correct / n - sc_acc, 6),
            }
    out['entropy_adaptive'] = entropy_results

    # === Oracle: best achievable by adaptive abstention ===
    # If we could perfectly predict which SC answers are wrong and abstain on those
    wrong_by_regime = {}
    for rname, pred in regime_bounds:
        ri = [it for it in items if pred(it['majority_frac'])]
        wrong = sum(1 for it in ri if it['sc_answer'] != it['gt'])
        wrong_by_regime[rname] = wrong
    out['wrong_by_regime'] = wrong_by_regime

    # Is accuracy monotonic with majority_frac? (key test of hypothesis)
    frac_bins = [(0, 0.33), (0.33, 0.5), (0.5, 0.67), (0.67, 0.75),
                 (0.75, 0.83), (0.83, 0.92), (0.92, 1.0), (1.0, 1.01)]
    monotonicity = []
    for lo, hi in frac_bins:
        if hi > 1.0:
            bi = [it for it in items if it['majority_frac'] >= lo]
        else:
            bi = [it for it in items if lo <= it['majority_frac'] < hi]
        bc = sum(1 for it in bi if it['sc_answer'] == it['gt'])
        bn = len(bi)
        monotonicity.append({
            'range': f'[{lo},{hi})',
            'n': bn,
            'correct': bc,
            'accuracy': round(bc / bn, 4) if bn else None,
        })
    out['accuracy_by_agreement_bin'] = monotonicity

    return out


def main():
    if len(sys.argv) < 3:
        print(f"Usage: {sys.argv[0]} <results_json> <experiment_name>")
        sys.exit(1)
    result = analyze_experiment(load_results(sys.argv[1]), sys.argv[2])
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
