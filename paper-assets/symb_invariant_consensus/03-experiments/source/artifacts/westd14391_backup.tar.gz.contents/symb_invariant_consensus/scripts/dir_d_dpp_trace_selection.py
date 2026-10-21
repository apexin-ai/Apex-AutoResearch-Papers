"""Dir-D: DPP Trace Selection for FOLIO 204 questions.
Greedy MAP DPP on TF-IDF embeddings, compare DPP-selected SC vs full SC.
"""
import json
import os
import glob
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from scipy.stats import binom
from collections import Counter

DATA_DIR = '/root/symb_invariant_consensus/results/exp033_mistral_7b_folio204/intermediates'
GOLD_FILE = '/root/symb_invariant_consensus/data/folio_full.json'
OUT_DIR = '/root/symb_invariant_consensus/results/dir_d_dpp_trace_selection'
K_SELECT_VALUES = [4, 6, 8]


def greedy_dpp_map(L, k):
    """Greedy MAP inference for DPP: select k items maximizing det(L_S).
    Uses Schur complement for conditional gain computation."""
    n = L.shape[0]
    if k >= n:
        return list(range(n))
    selected = []
    remaining = set(range(n))

    first = max(remaining, key=lambda i: L[i, i])
    selected.append(first)
    remaining.remove(first)

    for _ in range(k - 1):
        if not remaining:
            break
        S = np.array(selected)
        L_SS = L[np.ix_(S, S)]
        L_SS_inv = np.linalg.inv(L_SS + 1e-10 * np.eye(len(S)))

        best_idx, best_gain = None, -np.inf
        for i in remaining:
            L_iS = L[i, S]
            gain = L[i, i] - L_iS @ L_SS_inv @ L_iS
            if gain > best_gain:
                best_gain = gain
                best_idx = i

        selected.append(best_idx)
        remaining.remove(best_idx)

    return selected


def majority_vote(answers):
    valid = [a for a in answers if a and a.strip()]
    if not valid:
        return None
    counts = Counter(valid)
    return counts.most_common(1)[0][0]


def mcnemar_exact(correct_a, correct_b):
    """Two-sided McNemar exact test for paired binary outcomes."""
    b = sum(1 for a, bb in zip(correct_a, correct_b) if a and not bb)
    c = sum(1 for a, bb in zip(correct_a, correct_b) if not a and bb)
    n_disc = b + c
    if n_disc == 0:
        return 1.0, b, c
    p = 2 * min(binom.cdf(b, n_disc, 0.5), binom.cdf(c, n_disc, 0.5))
    return min(p, 1.0), b, c


def load_data():
    with open(GOLD_FILE) as f:
        gold_data = json.load(f)
    gold_labels = {item['id']: item['answer'] for item in gold_data}

    files = sorted(
        glob.glob(os.path.join(DATA_DIR, 'folio_*.json')),
        key=lambda x: int(os.path.basename(x).split('_')[1].split('.')[0])
    )

    questions = []
    for fpath in files:
        with open(fpath) as f:
            data = json.load(f)
        qid = data['problem']['id']
        gold = gold_labels.get(qid)
        if gold is None:
            continue
        traces = data['sica_result']['traces']
        questions.append({
            'id': qid,
            'gold': gold,
            'trace_texts': [t['trace'] for t in traces],
            'trace_answers': [t.get('answer', '') for t in traces],
        })
    return questions


def run_experiment(questions):
    results = {}

    for k_sel in K_SELECT_VALUES:
        full_correct = []
        dpp_correct = []
        per_q = []

        for q in questions:
            texts = q['trace_texts']
            answers = q['trace_answers']
            gold = q['gold']

            full_vote = majority_vote(answers)
            full_ok = (full_vote == gold) if full_vote else False
            full_correct.append(full_ok)

            vectorizer = TfidfVectorizer(max_features=5000, stop_words='english')
            tfidf = vectorizer.fit_transform(texts)
            L = cosine_similarity(tfidf)
            selected = greedy_dpp_map(L, k_sel)
            sel_answers = [answers[i] for i in selected]
            dpp_vote = majority_vote(sel_answers)
            dpp_ok = (dpp_vote == gold) if dpp_vote else False
            dpp_correct.append(dpp_ok)

            per_q.append({
                'id': q['id'],
                'gold': gold,
                'full_vote': full_vote,
                'full_correct': full_ok,
                'dpp_vote': dpp_vote,
                'dpp_correct': dpp_ok,
                'dpp_selected_indices': selected,
                'dpp_selected_answers': sel_answers,
                'all_answers': answers,
            })

        full_acc = sum(full_correct) / len(full_correct) * 100
        dpp_acc = sum(dpp_correct) / len(dpp_correct) * 100
        p_val, b, c = mcnemar_exact(dpp_correct, full_correct)

        n_dpp_only = sum(1 for pq in per_q if pq['dpp_correct'] and not pq['full_correct'])
        n_full_only = sum(1 for pq in per_q if pq['full_correct'] and not pq['dpp_correct'])
        n_both = sum(1 for pq in per_q if pq['dpp_correct'] and pq['full_correct'])
        n_neither = sum(1 for pq in per_q if not pq['dpp_correct'] and not pq['full_correct'])

        results[f'k_select_{k_sel}'] = {
            'k_select': k_sel,
            'dpp_sc_accuracy': round(dpp_acc, 2),
            'full_sc_accuracy_k12': round(full_acc, 2),
            'delta': round(dpp_acc - full_acc, 2),
            'mcnemar_p': round(p_val, 6),
            'mcnemar_b_dpp_only_correct': b,
            'mcnemar_c_full_only_correct': c,
            'contingency': {
                'both_correct': n_both,
                'dpp_only': n_dpp_only,
                'full_only': n_full_only,
                'neither': n_neither,
            },
            'n_questions': len(full_correct),
            'dpp_correct_count': sum(dpp_correct),
            'full_correct_count': sum(full_correct),
            'per_question': per_q,
        }

        print(f'K_select={k_sel}: DPP-SC={dpp_acc:.2f}%  Full-SC={full_acc:.2f}%  '
              f'delta={dpp_acc - full_acc:+.2f}%  McNemar p={p_val:.4f}  '
              f'(dpp_only={n_dpp_only}, full_only={n_full_only})')

    return results


if __name__ == '__main__':
    print('Loading data...')
    questions = load_data()
    print(f'Loaded {len(questions)} questions, each with 12 traces')

    print('\nRunning DPP trace selection experiment...')
    results = run_experiment(questions)

    os.makedirs(OUT_DIR, exist_ok=True)
    out_path = os.path.join(OUT_DIR, 'results.json')
    with open(out_path, 'w') as f:
        json.dump(results, f, indent=2)
    print(f'\nResults saved to {out_path}')
