#!/usr/bin/env python3
"""
Dir-F2: Same-Model Self-Verification (30-problem pilot).

Mistral-7B verifies constraints extracted by Mistral-7B itself.
Data point for Method Exhaustion Table: even with different prompt,
same model cannot escape its own bias.
"""
import json
import sys
import time
import logging
from pathlib import Path
from collections import Counter

import requests

sys.path.insert(0, '/root/symb_invariant_consensus')
from sica.z3_maxsat import (
    parse_z3_formula, ConstraintDeduplicator, MaxSATSolver,
    UniqueConstraint,
)
from sica.scorer import InvariantScorer

logging.basicConfig(level=logging.WARNING)
logger = logging.getLogger(__name__)

RESULTS_DIR = Path('/root/symb_invariant_consensus/results/exp033_mistral_7b_folio204')
CACHE_DIR = RESULTS_DIR / 'constraint_cache'
INTER_DIR = RESULTS_DIR / 'intermediates'
FOLIO_PATH = Path('/root/symb_invariant_consensus/data/folio_full.json')
OUT_DIR = Path('/root/symb_invariant_consensus/results/dir_f2_self_verification')

VLLM_URL = "http://localhost:8012/v1/chat/completions"
MODEL_PATH = "/root/autodl-tmp/models/Mistral-7B-Instruct-v0.3"
N = 30
VERIFY_TEMPERATURE = 0.0
VERIFY_MAX_TOKENS = 16


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


def extract_premises(problem_text):
    marker = "Determine whether"
    idx = problem_text.find(marker)
    if idx == -1:
        idx = problem_text.lower().find(marker.lower())
    if idx == -1:
        return problem_text
    preamble = problem_text[:idx].strip()
    if preamble.startswith("Given the following premises:\n"):
        preamble = preamble[len("Given the following premises:\n"):].strip()
    return preamble


def verify_constraint(premises: str, constraint_expr: str) -> str:
    prompt = f"""Given the following premises:
{premises}

Does the following logical constraint logically follow from the premises alone?
Constraint: {constraint_expr}

Answer only: Yes / No / Uncertain"""

    payload = {
        "model": MODEL_PATH,
        "messages": [{"role": "user", "content": prompt}],
        "temperature": VERIFY_TEMPERATURE,
        "max_tokens": VERIFY_MAX_TOKENS,
    }

    try:
        resp = requests.post(VLLM_URL, json=payload, timeout=60)
        resp.raise_for_status()
        content = resp.json()["choices"][0]["message"]["content"].strip()
        last_line = content.strip().split('\n')[-1].strip().rstrip('.')
        ll = last_line.lower()
        if 'yes' in ll:
            return 'Yes'
        elif 'no' in ll and 'uncertain' not in ll:
            return 'No'
        else:
            return 'Uncertain'
    except Exception as e:
        logger.warning("Verification API error: %s", e)
        return 'Uncertain'


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
    folio_data = json.loads(FOLIO_PATH.read_text())
    folio_by_id = {d['id']: d for d in folio_data}

    pids = [f'folio_{i}' for i in range(N)]

    try:
        r = requests.get("http://localhost:8012/v1/models", timeout=10)
        r.raise_for_status()
        print(f"vLLM alive: {r.json()['data'][0]['id']}")
    except Exception as e:
        print(f"ERROR: vLLM not reachable on port 8012: {e}")
        sys.exit(1)

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    t_start = time.time()

    original_sica_correct = []
    filtered_sica_correct = []
    sc_correct_list = []
    per_question = []

    total_constraints = 0
    total_kept = 0

    for pi, pid in enumerate(pids):
        inter = json.loads((INTER_DIR / f'{pid}.json').read_text())
        cache = json.loads((CACHE_DIR / f'{pid}.json').read_text())

        traces = inter['sica_result']['traces']
        gt = norm_ans(inter['problem']['answer'])
        stored_sica = norm_ans(inter['sica_result']['answer'])
        sc_ans = sc_answer(traces)

        original_sica_correct.append(stored_sica == gt)
        sc_correct_list.append(sc_ans == gt)

        folio_entry = folio_by_id.get(pid, {})
        premises = extract_premises(folio_entry.get('problem', inter['problem']['problem']))

        all_trace_constraints = []
        for t_info in cache.get('per_trace', []):
            all_trace_constraints.append(t_info.get('constraints', []))

        deduper = ConstraintDeduplicator()
        unique = deduper.deduplicate(all_trace_constraints)
        n_unique = len(unique)
        total_constraints += n_unique

        kept = []
        verdicts = []
        for uc in unique:
            verdict = verify_constraint(premises, uc.expression)
            verdicts.append(verdict)
            if verdict == 'Yes':
                kept.append(uc)

        n_kept = len(kept)
        total_kept += n_kept

        filtered_ans, filtered_scores = solve_and_answer(kept, traces)
        filtered_correct = (filtered_ans == gt)
        filtered_sica_correct.append(filtered_correct)

        detail = {
            'pid': pid,
            'gt': gt,
            'sc_answer': sc_ans,
            'sc_correct': sc_ans == gt,
            'original_sica_answer': stored_sica,
            'original_sica_correct': stored_sica == gt,
            'filtered_sica_answer': filtered_ans,
            'filtered_sica_correct': filtered_correct,
            'n_constraints_before': n_unique,
            'n_constraints_after': n_kept,
            'keep_rate': round(n_kept / n_unique, 4) if n_unique > 0 else 0.0,
            'verdict_counts': dict(Counter(verdicts)),
            'filtered_scores': {k: round(v, 2) for k, v in filtered_scores.items()},
        }
        per_question.append(detail)

        status = "OK" if filtered_correct else "WRONG"
        flip = ""
        if (stored_sica == gt) != filtered_correct:
            flip = " FLIP!" if filtered_correct else " REGRESS!"
        print(f"  [{pi+1:2d}/{N}] {pid}: gt={gt} orig={stored_sica} filt={filtered_ans} "
              f"kept={n_kept}/{n_unique} {status}{flip}")

    elapsed = time.time() - t_start

    orig_acc = sum(original_sica_correct) / N
    filt_acc = sum(filtered_sica_correct) / N
    sc_acc_val = sum(sc_correct_list) / N
    keep_rate = total_kept / total_constraints if total_constraints > 0 else 0.0

    # McNemar: filtered vs SC
    a = sum(1 for i in range(N) if filtered_sica_correct[i] and sc_correct_list[i])
    b = sum(1 for i in range(N) if filtered_sica_correct[i] and not sc_correct_list[i])
    c = sum(1 for i in range(N) if not filtered_sica_correct[i] and sc_correct_list[i])
    d = sum(1 for i in range(N) if not filtered_sica_correct[i] and not sc_correct_list[i])

    from scipy.stats import binomtest
    n_discordant = b + c
    mcnemar_p = binomtest(min(b, c), n_discordant, 0.5).pvalue if n_discordant > 0 else 1.0

    # McNemar: filtered vs original SICA
    b2 = sum(1 for i in range(N) if filtered_sica_correct[i] and not original_sica_correct[i])
    c2 = sum(1 for i in range(N) if not filtered_sica_correct[i] and original_sica_correct[i])
    n_disc2 = b2 + c2
    mcnemar_p_vs_orig = binomtest(min(b2, c2), n_disc2, 0.5).pvalue if n_disc2 > 0 else 1.0

    print()
    print("=" * 70)
    print(f"Dir-F2: Same-Model Self-Verification (Method Exhaustion Table)")
    print(f"  N={N}, elapsed={elapsed:.1f}s")
    print(f"  Generator: Mistral-7B-Instruct-v0.3")
    print(f"  Verifier:  Mistral-7B-Instruct-v0.3 (same model, direct prompt)")
    print("=" * 70)
    print(f"  SC accuracy:              {sum(sc_correct_list):>3}/{N}  ({sc_acc_val:.1%})")
    print(f"  Original SICA accuracy:   {sum(original_sica_correct):>3}/{N}  ({orig_acc:.1%})")
    print(f"  Filtered SICA accuracy:   {sum(filtered_sica_correct):>3}/{N}  ({filt_acc:.1%})")
    print(f"  Constraint keep rate:     {keep_rate:.1%} ({total_kept}/{total_constraints})")
    print(f"  McNemar p (filt vs SC):   {mcnemar_p:.4f}")
    print(f"  McNemar p (filt vs orig): {mcnemar_p_vs_orig:.4f}")

    gains = [per_question[i]['pid'] for i in range(N)
             if filtered_sica_correct[i] and not original_sica_correct[i]]
    losses = [per_question[i]['pid'] for i in range(N)
              if not filtered_sica_correct[i] and original_sica_correct[i]]
    print(f"\n  Gains vs original SICA (+{len(gains)}): {gains}")
    print(f"  Losses vs original SICA (-{len(losses)}): {losses}")

    results = {
        'method': 'dir_f2_self_verification',
        'purpose': 'Method Exhaustion Table: same-model self-verification cannot escape bias',
        'generator_model': 'Mistral-7B-Instruct-v0.3',
        'verifier_model': 'Mistral-7B-Instruct-v0.3',
        'verifier_port': 8012,
        'verifier_temperature': VERIFY_TEMPERATURE,
        'prompt_style': 'direct_answer_only',
        'n_problems': N,
        'elapsed_s': round(elapsed, 1),
        'original_sica_acc': round(orig_acc, 4),
        'self_filtered_sica_acc': round(filt_acc, 4),
        'sc_acc': round(sc_acc_val, 4),
        'constraint_keep_rate': round(keep_rate, 4),
        'total_constraints_before': total_constraints,
        'total_constraints_kept': total_kept,
        'mcnemar_p_filt_vs_sc': round(mcnemar_p, 6),
        'mcnemar_p_filt_vs_orig': round(mcnemar_p_vs_orig, 6),
        'contingency_filt_vs_sc': {'both_correct': a, 'filt_only': b, 'sc_only': c, 'both_wrong': d},
        'contingency_filt_vs_orig': {'gains': len(gains), 'losses': len(losses)},
        'gains_vs_original': gains,
        'losses_vs_original': losses,
        'per_question_details': per_question,
    }

    out_path = OUT_DIR / 'results.json'
    with open(out_path, 'w') as f:
        json.dump(results, f, indent=2, ensure_ascii=False)
    print(f"\nSaved to {out_path}")


if __name__ == '__main__':
    main()
