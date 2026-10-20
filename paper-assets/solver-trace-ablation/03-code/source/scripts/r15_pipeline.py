#!/usr/bin/env python3
"""
R15 Classifier Validation Pipeline.
Collects stratified samples, runs independent verification,
computes inter-method agreement, threshold sensitivity, LaTeX table.
"""

import json
import os
import random
import re
import sys

sys.path.insert(0, os.path.dirname(__file__))

from classify_h7 import (
    is_h7_strict, is_h7b_obfuscated, is_h1_strict,
    is_h8_conjunction_collapse, normalize_fol,
)
from independent_verifier import classify_sample as iv_classify

EVAL_FILES = [
    '/root/autodl-tmp/outputs/plan001_exec_only_s44_1000_r2/eval_sta_results.json',
    '/root/autodl-tmp/outputs/plan009_sft_baseline_s42_1000/eval_sta_results.json',
    '/root/autodl-tmp/outputs/plan009_sft_baseline_s43_1000/eval_sta_results.json',
    '/root/autodl-tmp/outputs/plan009_sft_baseline_s44_1000/eval_sta_results.json',
    '/root/autodl-tmp/outputs/sweep_random_b005_s43/eval_sta_results.json',
    '/root/autodl-tmp/outputs/sweep_random_b005_s44/eval_sta_results.json',
    '/root/autodl-tmp/outputs/d129_1.7b_random_b01_s43/eval_sta_results.json',
    '/root/autodl-tmp/outputs/d129_1.7b_random_b01_s44/eval_sta_results.json',
    '/root/autodl-tmp/outputs/plan018_additive_random_b01_s44_r2/eval_sta_results.json',
    '/root/autodl-tmp/outputs/plan002_additive_b01_s45_1000/eval_sta_results.json',
]

OUTPUT_DIR = '/root/autodl-tmp/outputs/classifier_validation'


# ── original classifier label ──────────────────────────────────────────

def orig_label(premises, conclusion):
    """Map classify_h7 detections to paper naming (H1→CE, H7→TS, H8→PG)."""
    if not isinstance(premises, list):
        premises = [premises]
    h7a = is_h7_strict(premises, conclusion)
    h7b = False if h7a else is_h7b_obfuscated(premises, conclusion)
    h1 = False if (h7a or h7b) else is_h1_strict(premises, conclusion)
    h8 = is_h8_conjunction_collapse(premises, conclusion)
    if h7a or h7b:
        return 'TS'
    if h1:
        return 'CE'
    if h8:
        return 'PG'
    return 'genuine'


# ── Step 1: collect all proved samples ─────────────────────────────────

def collect_proved():
    all_samples = []
    for fpath in EVAL_FILES:
        if not os.path.exists(fpath):
            print(f'SKIP: {fpath}')
            continue
        with open(fpath) as f:
            data = json.load(f)
        results = data.get('results', data.get('samples', []))
        for r in results:
            if r.get('execution_reward', 0) != 1.0:
                continue
            det = r.get('details', {})
            premises = det.get('premises', [])
            conclusion = det.get('conclusion', '')
            context = r.get('context', '')
            if not isinstance(premises, list):
                premises = [premises]

            ol = orig_label(premises, conclusion)
            iv_primary, iv_triggered = iv_classify(premises, conclusion, context)

            nl_lines = [l.strip() for l in context.split('\n') if l.strip()]
            all_samples.append({
                'source_file': fpath,
                'sample_idx': r.get('index', -1),
                'id': r.get('id', '?'),
                'nl_premises': nl_lines,
                'nl_conclusion': r.get('question', ''),
                'fol_premises': premises,
                'fol_conclusion': conclusion,
                'original_classify_result': ol,
                'independent_classify_result': iv_primary,
                'independent_triggered': iv_triggered,
                'raw_output': r.get('formalization', ''),
                'isr': det.get('isr', 0),
                'context': context,
            })
    return all_samples


# ── Step 1b: stratified sampling ───────────────────────────────────────

def stratified_sample(all_samples, n_per=20, seed=42):
    random.seed(seed)
    buckets = {}
    for s in all_samples:
        lb = s['original_classify_result']
        buckets.setdefault(lb, []).append(s)

    sampled = []
    notes = {}
    for mode in ['CE', 'TS', 'PG', 'genuine']:
        pool = buckets.get(mode, [])
        random.shuffle(pool)
        take = min(n_per, len(pool))
        sampled.extend(pool[:take])
        notes[mode] = {'available': len(pool), 'sampled': take}
        if take < n_per:
            notes[mode]['note'] = f'Only {len(pool)} available'

    # CI: original classifier has no H9 detector. Detect via independent verifier
    # among samples not yet selected and labeled CI by IV.
    selected_ids = {(s['source_file'], s['sample_idx']) for s in sampled}
    ci_pool = [s for s in all_samples
               if s['independent_classify_result'] == 'CI'
               and (s['source_file'], s['sample_idx']) not in selected_ids]
    random.shuffle(ci_pool)
    ci_take = min(n_per, len(ci_pool))
    sampled.extend(ci_pool[:ci_take])
    notes['CI'] = {'available': len(ci_pool), 'sampled': ci_take}
    if ci_take < n_per:
        notes['CI']['note'] = f'Only {len(ci_pool)} available (detected by IV only)'

    return sampled, notes


# ── Step 3: comparison metrics ─────────────────────────────────────────

def compute_metrics(sampled):
    orig = [s['original_classify_result'] for s in sampled]
    indep = [s['independent_classify_result'] for s in sampled]
    n = len(sampled)
    all_modes = sorted(set(orig + indep))

    per_mode = {}
    for mode in ['CE', 'TS', 'PG', 'CI', 'genuine']:
        tp = sum(1 for o, i in zip(orig, indep) if o == mode and i == mode)
        fp = sum(1 for o, i in zip(orig, indep) if o != mode and i == mode)
        fn = sum(1 for o, i in zip(orig, indep) if o == mode and i != mode)
        prec = tp / (tp + fp) if (tp + fp) else 0.0
        rec = tp / (tp + fn) if (tp + fn) else 0.0
        f1 = 2 * prec * rec / (prec + rec) if (prec + rec) else 0.0
        n_orig = sum(1 for o in orig if o == mode)
        per_mode[mode] = dict(precision=prec, recall=rec, f1=f1,
                              tp=tp, fp=fp, fn=fn, n=n_orig)

    # Cohen's kappa
    agree = sum(1 for o, i in zip(orig, indep) if o == i)
    po = agree / n if n else 0
    pe = 0
    for mode in all_modes:
        pe += (sum(1 for o in orig if o == mode) / n) * \
              (sum(1 for i in indep if i == mode) / n) if n else 0
    kappa = (po - pe) / (1 - pe) if pe < 1 else 1.0

    return per_mode, kappa


# ── Step 4: threshold sensitivity ──────────────────────────────────────

def threshold_sensitivity(all_samples):
    """
    classify_h7.py has no explicit numeric threshold.
    H7b Layer 2 uses: quantifier_count(conclusion) > quantifier_count(premise)
    AND premise_predicates ⊆ conclusion_predicates.

    We parameterize the minimum quantifier *difference* (delta) for the
    H7b heuristic: delta ∈ {0, 1, 2, 3, 4}  (original = 1, i.e. strictly >).
    We also vary a predicate overlap ratio: {0.5, 0.7, 0.8, 0.9, 1.0} (original = 1.0 = subset).
    """
    results = {}

    # -- H7b quantifier delta sensitivity --
    for delta in [0, 1, 2, 3, 4]:
        counts = {'TS': 0, 'CE': 0, 'PG': 0, 'genuine': 0}
        for s in all_samples:
            prems = s['fol_premises']
            conc = s['fol_conclusion']
            if not isinstance(prems, list):
                prems = [prems]
            # H7a: unchanged
            h7a = is_h7_strict(prems, conc)
            # H7b with varied delta
            h7b = False
            if not h7a and len(prems) == 1:
                p, c = prems[0], conc
                if normalize_fol(p) != normalize_fol(c):
                    p_qc = p.count('∀') + p.count('∃')
                    c_qc = c.count('∀') + c.count('∃')
                    if (c_qc - p_qc) >= delta:
                        p_preds = set(re.findall(r'\b([A-Z][A-Za-z0-9_]*)\s*\(', p))
                        c_preds = set(re.findall(r'\b([A-Z][A-Za-z0-9_]*)\s*\(', c))
                        if p_preds and p_preds.issubset(c_preds):
                            h7b = True
            h1 = False if (h7a or h7b) else is_h1_strict(prems, conc)
            h8 = is_h8_conjunction_collapse(prems, conc)
            if h7a or h7b:
                counts['TS'] += 1
            elif h1:
                counts['CE'] += 1
            elif h8:
                counts['PG'] += 1
            else:
                counts['genuine'] += 1
        results[f'quant_delta_{delta}'] = counts

    # -- predicate overlap ratio sensitivity --
    for min_overlap in [0.5, 0.7, 0.8, 0.9, 1.0]:
        counts = {'TS': 0, 'CE': 0, 'PG': 0, 'genuine': 0}
        for s in all_samples:
            prems = s['fol_premises']
            conc = s['fol_conclusion']
            if not isinstance(prems, list):
                prems = [prems]
            h7a = is_h7_strict(prems, conc)
            h7b = False
            if not h7a and len(prems) == 1:
                p, c = prems[0], conc
                if normalize_fol(p) != normalize_fol(c):
                    p_qc = p.count('∀') + p.count('∃')
                    c_qc = c.count('∀') + c.count('∃')
                    if c_qc > p_qc:
                        p_preds = set(re.findall(r'\b([A-Z][A-Za-z0-9_]*)\s*\(', p))
                        c_preds = set(re.findall(r'\b([A-Z][A-Za-z0-9_]*)\s*\(', c))
                        if p_preds:
                            overlap = len(p_preds & c_preds) / len(p_preds)
                            if overlap >= min_overlap:
                                h7b = True
            h1 = False if (h7a or h7b) else is_h1_strict(prems, conc)
            h8 = is_h8_conjunction_collapse(prems, conc)
            if h7a or h7b:
                counts['TS'] += 1
            elif h1:
                counts['CE'] += 1
            elif h8:
                counts['PG'] += 1
            else:
                counts['genuine'] += 1
        results[f'pred_overlap_{min_overlap}'] = counts

    return results


# ── Step 5: LaTeX table ────────────────────────────────────────────────

def gen_latex(per_mode, kappa, notes):
    modes = ['CE', 'TS', 'PG', 'CI', 'genuine']
    lines = [
        r'\begin{table}[t]',
        r'\centering',
        r'\caption{Classifier validation: independent verification agreement on stratified sample ($N$\,=\,%d).}' % sum(notes[m]['sampled'] for m in notes),
        r'\label{tab:classifier-validation}',
        r'\small',
        r'\begin{tabular}{lcccc}',
        r'\toprule',
        r'Mode & Precision & Recall & F1 & $N$ \\',
        r'\midrule',
    ]
    for mode in modes:
        m = per_mode.get(mode, {})
        n = notes.get(mode, {}).get('sampled', m.get('n', 0))
        if n == 0 and m.get('tp', 0) == 0 and m.get('fp', 0) == 0 and m.get('fn', 0) == 0:
            lines.append(r'%s & --- & --- & --- & 0 \\' % mode)
        else:
            lines.append(r'%s & %.2f & %.2f & %.2f & %d \\' % (
                mode, m['precision'], m['recall'], m['f1'], n))
    lines += [
        r'\midrule',
        r"\multicolumn{5}{l}{Cohen's $\kappa$ = %.3f} \\" % kappa,
        r'\bottomrule',
        r'\end{tabular}',
        r'\end{table}',
    ]
    return '\n'.join(lines)


# ── main ────────────────────────────────────────────────────────────────

def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    print('Step 1: Collecting proved samples from %d eval files...' % len(EVAL_FILES))
    all_samples = collect_proved()
    print(f'  Total proved: {len(all_samples)}')

    # distribution
    dist = {}
    for s in all_samples:
        dist[s['original_classify_result']] = dist.get(s['original_classify_result'], 0) + 1
    print(f'  Original distribution: {dist}')
    iv_dist = {}
    for s in all_samples:
        iv_dist[s['independent_classify_result']] = iv_dist.get(s['independent_classify_result'], 0) + 1
    print(f'  Independent distribution: {iv_dist}')

    print('\nStep 1b: Stratified sampling...')
    sampled, notes = stratified_sample(all_samples)
    print(f'  Sampled {len(sampled)} total')
    for mode, info in notes.items():
        print(f'  {mode}: {info}')

    # save stratified samples (strip context to reduce size)
    strat_out = []
    for s in sampled:
        strat_out.append({k: v for k, v in s.items() if k != 'context'})
    with open(os.path.join(OUTPUT_DIR, 'stratified_samples.json'), 'w') as f:
        json.dump({'notes': notes, 'samples': strat_out}, f, indent=2, ensure_ascii=False)
    print(f'  Saved stratified_samples.json')

    # save independent verification
    iv_out = []
    for s in sampled:
        iv_out.append({
            'source_file': s['source_file'],
            'sample_idx': s['sample_idx'],
            'id': s['id'],
            'original_label': s['original_classify_result'],
            'independent_label': s['independent_classify_result'],
            'independent_triggered': s['independent_triggered'],
            'n_fol_premises': len(s['fol_premises']),
            'n_nl_premises': len(s['nl_premises']),
        })
    with open(os.path.join(OUTPUT_DIR, 'independent_verification.json'), 'w') as f:
        json.dump(iv_out, f, indent=2)
    print(f'  Saved independent_verification.json')

    print('\nStep 3: Computing comparison metrics...')
    per_mode, kappa = compute_metrics(sampled)
    print(f"  Cohen's kappa = {kappa:.4f}")
    for mode in ['CE', 'TS', 'PG', 'CI', 'genuine']:
        m = per_mode[mode]
        print(f"  {mode}: P={m['precision']:.3f} R={m['recall']:.3f} F1={m['f1']:.3f} (tp={m['tp']} fp={m['fp']} fn={m['fn']})")
    with open(os.path.join(OUTPUT_DIR, 'precision_recall.json'), 'w') as f:
        json.dump({'per_mode': per_mode, 'cohens_kappa': kappa}, f, indent=2)
    print(f'  Saved precision_recall.json')

    print('\nStep 4: Threshold sensitivity analysis...')
    sens = threshold_sensitivity(all_samples)
    for key, counts in sens.items():
        total = sum(counts.values())
        parts = ', '.join(f'{m}={n}' for m, n in counts.items() if n)
        print(f'  {key}: {parts} (total={total})')
    with open(os.path.join(OUTPUT_DIR, 'threshold_sensitivity.json'), 'w') as f:
        json.dump(sens, f, indent=2)
    print(f'  Saved threshold_sensitivity.json')

    print('\nStep 5: Generating LaTeX table...')
    latex = gen_latex(per_mode, kappa, notes)
    with open(os.path.join(OUTPUT_DIR, 'validation_table.tex'), 'w') as f:
        f.write(latex)
    print(f'  Saved validation_table.tex')
    print('\n' + latex)

    print('\n--- Done ---')
    print(f'All output files in: {OUTPUT_DIR}')


if __name__ == '__main__':
    main()
