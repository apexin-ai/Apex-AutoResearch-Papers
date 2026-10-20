#!/usr/bin/env python3
"""Wild 6: κ-aware adaptive SC — self-contained analysis + runner."""

import json, sys, math, os

def majority_vote(dist):
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

def analyze(data, name):
    problems = data.get('results', [])
    K = data.get('summary', {}).get('k', 12)
    n = len(problems)
    if n == 0:
        return None

    items = []
    for p in problems:
        dist = p.get('sc_vote_distribution', {})
        gt = p.get('ground_truth', '')
        answer, maj_frac, tv = majority_vote(dist)
        items.append({'dist': dist, 'gt': gt, 'sc_answer': answer,
                       'majority_frac': maj_frac, 'entropy': entropy(dist),
                       'total_votes': tv, 'id': p.get('problem_id', '')})

    sc_correct = sum(1 for it in items if it['sc_answer'] == it['gt'])
    sc_acc = sc_correct / n

    out = {'experiment': name, 'n': n, 'K': K,
           'standard_sc': {'accuracy': round(sc_acc, 6), 'correct': sc_correct}}

    # Per-regime accuracy
    regime_bounds = [
        ('unanimous', lambda mf: mf >= 1.0),
        ('strong_075_1', lambda mf: 0.75 <= mf < 1.0),
        ('moderate_05_075', lambda mf: 0.5 < mf < 0.75),
        ('weak_le05', lambda mf: mf <= 0.5),
    ]
    per_regime = {}
    for rname, pred in regime_bounds:
        ri = [it for it in items if pred(it['majority_frac'])]
        rc = sum(1 for it in ri if it['sc_answer'] == it['gt'])
        rn = len(ri)
        per_regime[rname] = {'n': rn, 'frac': round(rn/n, 4),
                              'correct': rc, 'accuracy': round(rc/rn, 6) if rn else None}
    out['per_regime'] = per_regime

    mfs = [it['majority_frac'] for it in items]
    hs = [it['entropy'] for it in items]
    out['dist_stats'] = {'mean_majority_frac': round(sum(mfs)/len(mfs), 4),
                          'mean_entropy': round(sum(hs)/len(hs), 4)}

    # Confidence threshold sweep
    threshold_sweep = {}
    for theta in [0.4, 0.5, 0.6, 0.667, 0.75, 0.8, 0.833, 0.9, 0.917, 1.0]:
        answered = [(it['sc_answer'], it['gt']) for it in items if it['majority_frac'] >= theta]
        c = sum(1 for a, g in answered if a == g)
        an = len(answered)
        threshold_sweep[str(theta)] = {
            'overall_acc': round(c/n, 6), 'cond_acc': round(c/an, 6) if an else None,
            'coverage': round(an/n, 4), 'answered': an, 'correct': c}
    out['threshold_sweep'] = threshold_sweep

    # Forward adaptive
    configs = {'conservative': {'high': 0.9, 'medium': 0.7, 'super': 0.8},
               'balanced': {'high': 0.8, 'medium': 0.6, 'super': 0.7},
               'aggressive': {'high': 0.7, 'medium': 0.5, 'super': 0.6}}
    adaptive_fwd = {}
    for cname, p in configs.items():
        correct = abstained = 0
        for it in items:
            mf = it['majority_frac']
            if mf >= p['high'] or mf < p['medium']:
                if it['sc_answer'] == it['gt']: correct += 1
            elif mf >= p['super']:
                if it['sc_answer'] == it['gt']: correct += 1
            else:
                abstained += 1
        adaptive_fwd[cname] = {'accuracy': round(correct/n, 6), 'correct': correct,
                                'abstained': abstained, 'delta': round(correct/n - sc_acc, 6), 'params': p}
    out['adaptive_forward'] = adaptive_fwd

    # Anti-groupthink abstain
    anti_gt = {}
    for theta in [0.9, 0.917, 0.95, 1.0]:
        correct = abstained = 0
        for it in items:
            if it['majority_frac'] >= theta:
                abstained += 1
            elif it['sc_answer'] == it['gt']:
                correct += 1
        anti_gt[str(theta)] = {'accuracy': round(correct/n, 6), 'correct': correct,
                                'abstained': abstained, 'delta': round(correct/n - sc_acc, 6)}
    out['antigroupthink'] = anti_gt

    # Second-answer flip
    flip = {}
    for theta in [0.9, 0.917, 0.95, 1.0]:
        correct = flipped = 0
        for it in items:
            if it['majority_frac'] >= theta and len(it['dist']) > 1:
                sa = sorted(it['dist'].items(), key=lambda x: (-x[1], x[0]))
                pred = sa[1][0] if len(sa) > 1 else it['sc_answer']
                flipped += 1
            else:
                pred = it['sc_answer']
            if pred == it['gt']: correct += 1
        flip[str(theta)] = {'accuracy': round(correct/n, 6), 'correct': correct,
                             'flipped': flipped, 'delta': round(correct/n - sc_acc, 6)}
    out['second_answer_flip'] = flip

    # Entropy-aware
    ent_res = {}
    for ht in [0.5, 1.0, 1.5]:
        for rmf in [0.8, 0.9, 1.0]:
            correct = abstained = 0
            for it in items:
                if it['entropy'] < ht:
                    if it['majority_frac'] >= rmf:
                        if it['sc_answer'] == it['gt']: correct += 1
                    else:
                        abstained += 1
                else:
                    if it['sc_answer'] == it['gt']: correct += 1
            ent_res[f'h<{ht}_req{rmf}'] = {'accuracy': round(correct/n, 6), 'correct': correct,
                                             'abstained': abstained, 'delta': round(correct/n - sc_acc, 6)}
    out['entropy_adaptive'] = ent_res

    # Wrong count by regime
    wrong = {}
    for rname, pred in regime_bounds:
        ri = [it for it in items if pred(it['majority_frac'])]
        wrong[rname] = sum(1 for it in ri if it['sc_answer'] != it['gt'])
    out['wrong_by_regime'] = wrong

    # Fine-grained accuracy bins
    bins = [(0, 0.33), (0.33, 0.5), (0.5, 0.67), (0.67, 0.75),
            (0.75, 0.83), (0.83, 0.92), (0.92, 1.0), (1.0, 1.01)]
    mono = []
    for lo, hi in bins:
        bi = [it for it in items if it['majority_frac'] >= lo] if hi > 1.0 else \
             [it for it in items if lo <= it['majority_frac'] < hi]
        bc = sum(1 for it in bi if it['sc_answer'] == it['gt'])
        bn = len(bi)
        mono.append({'range': f'[{lo},{hi})', 'n': bn, 'correct': bc,
                      'accuracy': round(bc/bn, 4) if bn else None})
    out['accuracy_by_bin'] = mono

    return out

ROOT = "/root/symb_invariant_consensus"
EXPERIMENTS = [
    ("results/exp033_mistral_7b_folio204/exp033_results.json", "exp033", "Mistral-7B", "FOLIO-204"),
    ("results/exp067_mistral_folio_seed789/exp067_results.json", "exp067", "Mistral-7B(s789)", "FOLIO-204"),
    ("results/exp052_mistral_folio204_seed123/exp052_results.json", "exp052", "Mistral-7B(s123)", "FOLIO-204"),
    ("results/exp061_qwen25_7b_folio204/exp061_results.json", "exp061", "Qwen2.5-7B", "FOLIO-204"),
    ("results/exp066_qwen14b_folio_seed123/exp066_results.json", "exp066", "Qwen2.5-14B(s123)", "FOLIO-204"),
    ("results/exp036_qwen25_14b_folio204/results.json", "exp036", "Qwen2.5-14B", "FOLIO-204"),
    ("results/exp062_gemma27b_folio204/exp062_results.json", "exp062", "Gemma2-27B", "FOLIO-204"),
    ("results/exp-063-llama8b-folio204-16639/results.json", "exp063", "LLaMA-3.1-8B", "FOLIO-204"),
    ("results/exp069_mistral_logiqa200/exp069_results.json", "exp069m", "Mistral-7B", "LogiQA-200"),
    ("results/exp070_qwen7b_logiqa200/exp070_results.json", "exp070", "Qwen2.5-7B", "LogiQA-200"),
    ("results/exp069_llama8b_logiqa200/exp069_results.json", "exp069l", "LLaMA-3.1-8B", "LogiQA-200"),
]

def run_all():
    all_results = []
    for rel, name, model, dataset in EXPERIMENTS:
        path = os.path.join(ROOT, rel)
        if not os.path.exists(path):
            print(f"SKIP {name}: not found", file=sys.stderr)
            continue
        try:
            with open(path) as f:
                data = json.load(f)
            r = analyze(data, name)
            if r:
                r['model'] = model
                r['dataset'] = dataset
                all_results.append(r)
                print(f"OK   {name}: {model} {dataset} SC={r['standard_sc']['accuracy']:.4f}", file=sys.stderr)
        except Exception as e:
            print(f"ERR  {name}: {e}", file=sys.stderr)

    # Summary table
    summary = []
    for r in all_results:
        sc = r['standard_sc']['accuracy']
        best_name, best_acc, best_delta = 'standard_sc', sc, 0.0
        for sn, sd in r.get('adaptive_forward', {}).items():
            if sd['accuracy'] > best_acc:
                best_name, best_acc, best_delta = f'fwd_{sn}', sd['accuracy'], sd['delta']
        for sn, sd in r.get('threshold_sweep', {}).items():
            if sd['overall_acc'] > best_acc:
                best_name, best_acc = f'thresh_{sn}', sd['overall_acc']
                best_delta = sd['overall_acc'] - sc
        for sn, sd in r.get('entropy_adaptive', {}).items():
            if sd['accuracy'] > best_acc:
                best_name, best_acc, best_delta = f'ent_{sn}', sd['accuracy'], sd['delta']
        summary.append({'model': r['model'], 'dataset': r['dataset'], 'exp': r['experiment'],
                         'n': r['n'], 'standard_sc': round(sc, 4), 'best_adaptive': round(best_acc, 4),
                         'delta': round(best_delta, 4), 'best_strategy': best_name})

    combined = {'wild6_kappa_aware_sc': {'n_experiments': len(all_results),
                'experiments': all_results}, 'summary_table': summary}

    outdir = os.path.join(ROOT, 'results/wild6_kappa_aware_sc')
    os.makedirs(outdir, exist_ok=True)
    outpath = os.path.join(outdir, 'results.json')
    with open(outpath, 'w') as f:
        json.dump(combined, f, indent=2)
    print(f"\nSaved to {outpath}", file=sys.stderr)
    print(json.dumps(combined['summary_table'], indent=2))

if __name__ == '__main__':
    run_all()
