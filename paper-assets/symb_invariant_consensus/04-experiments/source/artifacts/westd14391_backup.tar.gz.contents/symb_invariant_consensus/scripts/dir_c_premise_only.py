#!/usr/bin/env python3
"""
Dir-C Premise-Only Filtering: FOLIO 204

Filters out constraints whose expression text references the conclusion
(keyword overlap >= 50% AND at least min(2, n_keywords) matches),
re-runs Z3 MAX-SAT aggregation with remaining premise-only constraints.
Reports accuracy + McNemar vs SC baseline.
"""
import json
import logging
import os
import re
import sys
import time
from collections import Counter

from scipy.stats import binomtest

sys.path.insert(0, '/root/symb_invariant_consensus')
from sica.z3_maxsat import ConstraintDeduplicator, MaxSATSolver
from sica.scorer import InvariantScorer
from sica.pipeline import normalize_logic_answer

logging.basicConfig(level=logging.WARNING)

FOLIO_PATH = '/root/symb_invariant_consensus/data/folio_full.json'
CACHE_DIR = '/root/symb_invariant_consensus/results/exp033_mistral_7b_folio204/constraint_cache'
INTERMED_DIR = '/root/symb_invariant_consensus/results/exp033_mistral_7b_folio204/intermediates'
OUTPUT_DIR = '/root/symb_invariant_consensus/results/dir_c_premise_only_204'

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


def main():
    t_start = time.time()

    with open(FOLIO_PATH) as f:
        folio_data = json.load(f)
    folio_by_id = {p['id']: p for p in folio_data}

    deduplicator = ConstraintDeduplicator()
    solver = MaxSATSolver()
    scorer = InvariantScorer()

    per_problem = []
    total_before = 0
    total_after = 0
    n_sc_correct = 0
    n_po_correct = 0
    n_sica_orig_correct = 0
    pairs = []

    pids = sorted(folio_by_id.keys(), key=lambda x: int(x.split('_')[1]))

    for i, pid in enumerate(pids):
        problem = folio_by_id[pid]
        gt = normalize_logic_answer(problem['answer'])

        cache_path = os.path.join(CACHE_DIR, f"{pid}.json")
        if not os.path.exists(cache_path):
            print(f"SKIP {pid}: no cache")
            continue
        with open(cache_path) as f:
            cache = json.load(f)

        intermed_path = os.path.join(INTERMED_DIR, f"{pid}.json")
        with open(intermed_path) as f:
            intermed = json.load(f)
        traces = intermed['sica_result']['traces']
        for t in traces:
            if t.get('answer'):
                t['answer'] = normalize_logic_answer(t['answer'])

        sica_orig = normalize_logic_answer(intermed['sica_result'].get('answer', ''))
        n_sica_orig_correct += (sica_orig == gt)

        answer_counts = Counter(t['answer'] for t in traces if t.get('answer'))
        if not answer_counts:
            sc_answer = ""
        else:
            max_count = answer_counts.most_common(1)[0][1]
            sc_answer = next(a for a, c in answer_counts.items() if c == max_count)
        sc_ok = (sc_answer == gt)
        n_sc_correct += sc_ok

        conclusion_text = extract_conclusion_text(problem['problem'])
        conclusion_kw, entities = get_conclusion_keywords(conclusion_text)

        n_before = 0
        n_after = 0
        all_filtered = []
        for trace_data in cache['per_trace']:
            constraints = trace_data['constraints']
            n_before += len(constraints)
            filtered = [c for c in constraints
                        if not constraint_references_conclusion(c, conclusion_kw, entities)]
            n_after += len(filtered)
            all_filtered.append(filtered)

        total_before += n_before
        total_after += n_after

        unique = deduplicator.deduplicate(all_filtered)
        maxsat_result = solver.solve(unique)
        candidates = sorted(set(t['answer'] for t in traces if t.get('answer')))
        scores = scorer.score(maxsat_result, traces, candidates)
        po_answer = scorer.select_answer(scores, dict(answer_counts))
        po_ok = (po_answer == gt)
        n_po_correct += po_ok

        pairs.append((sc_ok, po_ok))

        per_problem.append({
            'pid': pid,
            'gt': gt,
            'sc_answer': sc_answer,
            'sica_orig_answer': sica_orig,
            'po_answer': po_answer,
            'sc_correct': sc_ok,
            'po_correct': po_ok,
            'constraints_before': n_before,
            'constraints_after': n_after,
            'n_unique_after_dedup': len(unique),
            'conclusion_keywords': sorted(conclusion_kw),
        })

        if (i + 1) % 50 == 0:
            print(f"  processed {i+1}/{len(pids)}...")

    n = len(per_problem)

    b = sum(1 for sc, po in pairs if sc and not po)
    c = sum(1 for sc, po in pairs if not sc and po)
    n_disc = b + c
    mcnemar_p = binomtest(c, n_disc, 0.5).pvalue if n_disc > 0 else 1.0

    kept_ratio = total_after / total_before if total_before > 0 else 0

    output = {
        'accuracy': round(n_po_correct / n, 4) if n else 0,
        'n_correct': n_po_correct,
        'n_total': n,
        'sc_accuracy': round(n_sc_correct / n, 4) if n else 0,
        'sc_n_correct': n_sc_correct,
        'sica_orig_accuracy': round(n_sica_orig_correct / n, 4) if n else 0,
        'sica_orig_n_correct': n_sica_orig_correct,
        'constraints_kept_ratio': round(kept_ratio, 4),
        'total_constraints_before': total_before,
        'total_constraints_after': total_after,
        'mcnemar_p': round(mcnemar_p, 6),
        'discordant_pairs': {
            'sc_right_po_wrong': b,
            'sc_wrong_po_right': c,
            'total': n_disc,
        },
        'per_problem': per_problem,
    }

    os.makedirs(OUTPUT_DIR, exist_ok=True)
    out_path = os.path.join(OUTPUT_DIR, 'results.json')
    with open(out_path, 'w') as f:
        json.dump(output, f, indent=2)

    elapsed = time.time() - t_start
    print(f"\n{'='*60}")
    print(f"DIR-C PREMISE-ONLY FILTERING (FOLIO 204)")
    print(f"{'='*60}")
    print(f"Problems:            {n}")
    print(f"SC Accuracy:         {n_sc_correct}/{n} = {n_sc_correct/n:.4f}")
    print(f"SICA Original:       {n_sica_orig_correct}/{n} = {n_sica_orig_correct/n:.4f}")
    print(f"Premise-Only Acc:    {n_po_correct}/{n} = {n_po_correct/n:.4f}")
    print(f"Delta PO vs SC:      {(n_po_correct - n_sc_correct)/n:+.4f}")
    print(f"Constraints kept:    {total_after}/{total_before} = {kept_ratio:.2%}")
    print(f"McNemar p-value:     {mcnemar_p:.6f}")
    print(f"Discordant:          SC+/PO- = {b}, SC-/PO+ = {c}")
    print(f"Time:                {elapsed:.1f}s")
    print(f"Output:              {out_path}")


if __name__ == '__main__':
    main()
