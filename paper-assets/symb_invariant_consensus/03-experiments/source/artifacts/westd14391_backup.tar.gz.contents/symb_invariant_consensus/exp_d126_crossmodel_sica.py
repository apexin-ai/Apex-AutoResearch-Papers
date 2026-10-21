#!/usr/bin/env python3
"""exp_d126_crossmodel_sica.py — Cross-Model SICA on ProofWriter D5 N=204

Tests whether cross-model constraint extraction breaks symbolic confirmation bias.

Setup: two vLLM servers running simultaneously
  GPU 0: Mistral-7B on port 8000
  GPU 1: Qwen3-14B on port 8001 (non-thinking mode)

Phase 1: Generate Mistral traces + all 4 extraction conditions
Phase 2: Z3 MAX-SAT + full metrics

Usage:
  python exp_d126_crossmodel_sica.py --phase 1   # needs both vLLM servers
  python exp_d126_crossmodel_sica.py --phase 2   # CPU only
  python exp_d126_crossmodel_sica.py --phase all
"""
import argparse
import json
import os
import sys
import re
import time
import logging
from collections import Counter
from concurrent.futures import ThreadPoolExecutor, as_completed

import httpx

sys.path.insert(0, '/root/symb_invariant_consensus')
from sica.constraint_extractor import LOGIC_EXTRACTION_PROMPT
from sica.z3_maxsat import ConstraintDeduplicator, MaxSATSolver, parse_z3_formula
from sica.scorer import InvariantScorer
from sica.trace_generator import extract_boxed_answer, SOLVE_PROMPT

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s",
                    handlers=[logging.StreamHandler(sys.stdout)])
log = logging.getLogger(__name__)

N = 204
K = 12
T_GEN = 0.7
T_EXT = 0.3
SEED = 42
MISTRAL_PORT = 8000
QWEN3_PORT = 8001

DATA_PATH = '/root/symb_invariant_consensus/data/proofwriter_full.json'
QWEN3_INTER_DIR = '/root/symb_invariant_consensus/results/exp033_qwen3_14b_pw600_nonthinking/intermediates'
OUT_DIR = '/root/symb_invariant_consensus/results/exp_d126_crossmodel_sica'

VALID_ANSWERS = {'True', 'False', 'Unknown'}

def normalize_answer(ans):
    s = str(ans).strip()
    if s.startswith('\\text{'):
        s = s[len('\\text{'):]
        if s.endswith('}'): s = s[:-1]
        s = s.strip()
    low = s.lower()
    mapping = {'true': 'True', 'false': 'False', 'unknown': 'Unknown',
               'yes': 'True', 'no': 'False', 'uncertain': 'Unknown',
               'undetermined': 'Unknown', 't': 'True', 'f': 'False', 'u': 'Unknown'}
    return mapping.get(low, s.capitalize())


def strip_thinking(text):
    idx = text.find('</think>')
    if idx >= 0:
        return text[idx + len('</think>'):].strip()
    idx = text.find('<think>')
    if idx >= 0:
        return ''
    return text


def majority_vote(answers):
    valid = [a for a in answers if a in VALID_ANSWERS]
    if not valid:
        return '', {}
    counts = Counter(valid)
    mx = max(counts.values())
    top = sorted([a for a, c in counts.items() if c == mx])
    return top[0], dict(counts)


def api_url(port):
    return f'http://localhost:{port}/v1'


def get_model_id(port):
    r = httpx.get(f'{api_url(port)}/models', timeout=10)
    return r.json()['data'][0]['id']


def generate_traces(problem_text, port, model_id, k=K, temperature=T_GEN):
    prompt = SOLVE_PROMPT.format(problem=problem_text)
    traces = []

    def _gen_one(idx):
        payload = {
            'model': model_id,
            'messages': [{'role': 'user', 'content': prompt}],
            'max_tokens': 4096,
            'temperature': temperature,
            'top_p': 0.95,
        }
        resp = httpx.post(f'{api_url(port)}/chat/completions', json=payload, timeout=120)
        resp.raise_for_status()
        text = resp.json()['choices'][0]['message']['content'] or ''
        text = strip_thinking(text)
        ans = extract_boxed_answer(text)
        return {'trace': text, 'answer': normalize_answer(ans) if ans else '', 'trace_idx': idx}

    with ThreadPoolExecutor(max_workers=k) as ex:
        futs = {ex.submit(_gen_one, i): i for i in range(k)}
        for f in as_completed(futs):
            traces.append(f.result())
    traces.sort(key=lambda t: t['trace_idx'])
    return traces


def extract_constraints_single(trace_text, port, model_id, temperature=T_EXT):
    prompt = LOGIC_EXTRACTION_PROMPT.format(trace=trace_text)
    payload = {
        'model': model_id,
        'messages': [{'role': 'user', 'content': prompt}],
        'max_tokens': 2048,
        'temperature': temperature,
    }
    if 'Qwen3' in model_id or 'qwen3' in model_id.lower():
        payload['chat_template_kwargs'] = {'enable_thinking': False}
    try:
        resp = httpx.post(f'{api_url(port)}/chat/completions', json=payload, timeout=120)
        resp.raise_for_status()
        raw = resp.json()['choices'][0]['message']['content'] or ''
        text = strip_thinking(raw.strip())
        json_match = re.search(r'\{[\s\S]*\}', text)
        if not json_match:
            return {'error': 'no JSON', 'constraints': []}
        data = json.loads(json_match.group())
        return {'constraints': data.get('constraints', []),
                'extracted_answer': data.get('answer', '')}
    except json.JSONDecodeError:
        return {'error': 'JSON parse', 'constraints': []}
    except Exception as e:
        return {'error': str(e)[:200], 'constraints': []}


def extract_all_traces(traces, port, model_id, temperature=T_EXT, max_workers=6):
    per_trace = []

    def _extract(t):
        result = extract_constraints_single(t['trace'], port, model_id, temperature)
        return {
            'trace_idx': t['trace_idx'],
            'answer': normalize_answer(t['answer']) if t.get('answer') else '',
            'constraints': result.get('constraints', []),
            'extracted_answer': result.get('extracted_answer', ''),
            'error': result.get('error'),
        }

    with ThreadPoolExecutor(max_workers=max_workers) as ex:
        futs = {ex.submit(_extract, t): t['trace_idx'] for t in traces}
        for f in as_completed(futs):
            per_trace.append(f.result())
    per_trace.sort(key=lambda x: x['trace_idx'])
    return per_trace


def run_z3_sica(per_trace_constraints, traces):
    dedup = ConstraintDeduplicator()
    solver = MaxSATSolver()
    scorer = InvariantScorer()

    all_constraint_lists = []
    for ptc in per_trace_constraints:
        clist = ptc.get('constraints', [])
        all_constraint_lists.append(clist)

    unique = dedup.deduplicate(all_constraint_lists)
    maxsat_result = solver.solve(unique, timeout_ms=10000)

    for t in traces:
        if t.get('answer'):
            t['answer'] = normalize_answer(t['answer'])

    candidates = sorted(set(t['answer'] for t in traces if t.get('answer') and t['answer'] in VALID_ANSWERS))
    answer_counts = Counter(t['answer'] for t in traces if t.get('answer') and t['answer'] in VALID_ANSWERS)
    scores = scorer.score(maxsat_result, traces, candidates)
    selected = scorer.select_answer(scores, answer_counts)

    return {
        'sica_answer': selected,
        'scores': scores,
        'answer_counts': dict(answer_counts),
        'constraints_stats': {
            'total_extracted': sum(len(c) for c in all_constraint_lists),
            'traces_with_constraints': sum(1 for c in all_constraint_lists if c),
            'unique_after_dedup': len(unique),
        },
        'maxsat_stats': {
            'satisfied': len(maxsat_result.satisfied),
            'excluded': len(maxsat_result.excluded),
            'total_weight': maxsat_result.total_weight,
            'solve_time_ms': maxsat_result.solve_time_ms,
        },
    }


def phase1():
    os.makedirs(OUT_DIR, exist_ok=True)
    for d in ['mistral_traces', 'extraction_mistral_same', 'extraction_mistral_cross_qwen3',
              'extraction_qwen3_same', 'extraction_qwen3_cross_mistral']:
        os.makedirs(os.path.join(OUT_DIR, d), exist_ok=True)

    log.info("Connecting to vLLM servers...")
    mistral_model = get_model_id(MISTRAL_PORT)
    qwen3_model = get_model_id(QWEN3_PORT)
    log.info(f"Mistral: {mistral_model}")
    log.info(f"Qwen3: {qwen3_model}")

    with open(DATA_PATH) as f:
        all_problems = json.load(f)
    problems = all_problems[:N]
    log.info(f"Loaded {len(problems)} ProofWriter problems (first {N} of {len(all_problems)})")

    log.info("Loading Qwen3 traces from exp033...")
    qwen3_traces = {}
    pid_list = [p['id'] for p in problems]
    for pid in pid_list:
        fp = os.path.join(QWEN3_INTER_DIR, f'{pid}.json')
        if not os.path.exists(fp):
            log.warning(f"Missing Qwen3 intermediate: {pid}")
            continue
        with open(fp) as f:
            data = json.load(f)
        qwen3_traces[pid] = data['sica_result']['traces']
    log.info(f"Loaded Qwen3 traces for {len(qwen3_traces)}/{N} problems")

    checkpoint_file = os.path.join(OUT_DIR, 'phase1_checkpoint.json')
    done_pids = set()
    if os.path.exists(checkpoint_file):
        with open(checkpoint_file) as f:
            done_pids = set(json.load(f).get('done_pids', []))
        log.info(f"Resuming from checkpoint: {len(done_pids)} done")

    t_start = time.time()
    total = len(problems)
    for pi, prob in enumerate(problems):
        pid = prob['id']
        if pid in done_pids:
            continue

        gt = prob['answer']
        log.info(f"[{pi+1}/{total}] {pid} (gt={gt})")

        # Step A: Generate Mistral traces
        mistral_trace_file = os.path.join(OUT_DIR, 'mistral_traces', f'{pid}.json')
        if os.path.exists(mistral_trace_file):
            with open(mistral_trace_file) as f:
                m_traces = json.load(f)
            log.info(f"  Loaded existing Mistral traces")
        else:
            m_traces = generate_traces(prob['problem'], MISTRAL_PORT, mistral_model)
            with open(mistral_trace_file, 'w') as f:
                json.dump(m_traces, f)
            log.info(f"  Generated {len(m_traces)} Mistral traces")

        # Step B: Same-model Mistral extraction
        ext_file = os.path.join(OUT_DIR, 'extraction_mistral_same', f'{pid}.json')
        if not os.path.exists(ext_file):
            ptc = extract_all_traces(m_traces, MISTRAL_PORT, mistral_model, T_EXT)
            with open(ext_file, 'w') as f:
                json.dump({'pid': pid, 'gt': gt, 'per_trace': ptc}, f, indent=2)
            nc = sum(len(t['constraints']) for t in ptc)
            log.info(f"  Mistral same-model extraction: {nc} constraints")
        else:
            log.info(f"  Mistral same-model extraction: cached")

        # Step C: Cross — Mistral extracts Qwen3 traces
        ext_file = os.path.join(OUT_DIR, 'extraction_mistral_cross_qwen3', f'{pid}.json')
        if not os.path.exists(ext_file) and pid in qwen3_traces:
            ptc = extract_all_traces(qwen3_traces[pid], MISTRAL_PORT, mistral_model, T_EXT)
            with open(ext_file, 'w') as f:
                json.dump({'pid': pid, 'gt': gt, 'per_trace': ptc}, f, indent=2)
            nc = sum(len(t['constraints']) for t in ptc)
            log.info(f"  Mistral->Qwen3 cross-extraction: {nc} constraints")
        else:
            log.info(f"  Mistral->Qwen3 cross-extraction: cached/skip")

        # Step D: Same-model Qwen3 extraction
        ext_file = os.path.join(OUT_DIR, 'extraction_qwen3_same', f'{pid}.json')
        if not os.path.exists(ext_file) and pid in qwen3_traces:
            ptc = extract_all_traces(qwen3_traces[pid], QWEN3_PORT, qwen3_model, T_EXT)
            with open(ext_file, 'w') as f:
                json.dump({'pid': pid, 'gt': gt, 'per_trace': ptc}, f, indent=2)
            nc = sum(len(t['constraints']) for t in ptc)
            log.info(f"  Qwen3 same-model extraction: {nc} constraints")
        else:
            log.info(f"  Qwen3 same-model extraction: cached/skip")

        # Step E: Cross — Qwen3 extracts Mistral traces
        ext_file = os.path.join(OUT_DIR, 'extraction_qwen3_cross_mistral', f'{pid}.json')
        if not os.path.exists(ext_file):
            ptc = extract_all_traces(m_traces, QWEN3_PORT, qwen3_model, T_EXT)
            with open(ext_file, 'w') as f:
                json.dump({'pid': pid, 'gt': gt, 'per_trace': ptc}, f, indent=2)
            nc = sum(len(t['constraints']) for t in ptc)
            log.info(f"  Qwen3->Mistral cross-extraction: {nc} constraints")
        else:
            log.info(f"  Qwen3->Mistral cross-extraction: cached/skip")

        done_pids.add(pid)
        with open(checkpoint_file, 'w') as f:
            json.dump({'done_pids': list(done_pids)}, f)

        elapsed = time.time() - t_start
        done_count = len(done_pids)
        remaining = total - pi - 1
        if done_count > 0:
            rate_per_prob = elapsed / done_count
            eta = remaining * rate_per_prob
        else:
            eta = 0
        if (pi + 1) % 10 == 0:
            log.info(f"  Progress: {pi+1}/{total}  elapsed={elapsed:.0f}s  ETA={eta:.0f}s")

    log.info(f"Phase 1 complete: {len(done_pids)}/{total} problems in {time.time()-t_start:.0f}s")


def phase2():
    with open(DATA_PATH) as f:
        all_problems = json.load(f)
    problems = all_problems[:N]
    pid_list = [p['id'] for p in problems]
    gt_map = {p['id']: p['answer'] for p in problems}

    conditions = {
        'mistral_same': 'extraction_mistral_same',
        'mistral_cross_qwen3': 'extraction_mistral_cross_qwen3',
        'qwen3_same': 'extraction_qwen3_same',
        'qwen3_cross_mistral': 'extraction_qwen3_cross_mistral',
    }

    mistral_traces = {}
    for pid in pid_list:
        fp = os.path.join(OUT_DIR, 'mistral_traces', f'{pid}.json')
        if os.path.exists(fp):
            with open(fp) as f:
                mistral_traces[pid] = json.load(f)

    qwen3_traces = {}
    for pid in pid_list:
        fp = os.path.join(QWEN3_INTER_DIR, f'{pid}.json')
        if os.path.exists(fp):
            with open(fp) as f:
                data = json.load(f)
            qwen3_traces[pid] = data['sica_result']['traces']

    log.info(f"Loaded traces: Mistral={len(mistral_traces)}, Qwen3={len(qwen3_traces)}")

    def compute_sc(traces_map, gt_map):
        correct = 0
        total = 0
        per_problem = {}
        for pid, traces in traces_map.items():
            if pid not in gt_map:
                continue
            answers = [normalize_answer(t['answer']) for t in traces if t.get('answer')]
            sc_ans, counts = majority_vote(answers)
            gt = normalize_answer(gt_map[pid])
            is_correct = sc_ans == gt
            correct += int(is_correct)
            total += 1
            per_problem[pid] = {'sc_answer': sc_ans, 'sc_correct': is_correct, 'vote_dist': counts}
        return correct / total if total > 0 else 0, correct, total, per_problem

    mistral_sc_acc, mistral_sc_n, _, mistral_sc_pp = compute_sc(mistral_traces, gt_map)
    qwen3_sc_acc, qwen3_sc_n, _, qwen3_sc_pp = compute_sc(qwen3_traces, gt_map)
    log.info(f"SC accuracy: Mistral={mistral_sc_acc:.4f}, Qwen3={qwen3_sc_acc:.4f}")

    sica_results = {}
    for cond_name, cond_dir in conditions.items():
        log.info(f"Running Z3 SICA for condition: {cond_name}")

        if cond_name == 'mistral_same':
            traces_map = mistral_traces
        elif cond_name == 'qwen3_same':
            traces_map = qwen3_traces
        elif cond_name == 'mistral_cross_qwen3':
            traces_map = qwen3_traces
        elif cond_name == 'qwen3_cross_mistral':
            traces_map = mistral_traces
        else:
            traces_map = mistral_traces

        per_problem = {}
        correct = 0
        total = 0
        total_constraints = 0
        total_unique = 0
        total_excluded = 0

        for pid in pid_list:
            ext_file = os.path.join(OUT_DIR, cond_dir, f'{pid}.json')
            if not os.path.exists(ext_file):
                continue
            if pid not in traces_map:
                continue

            with open(ext_file) as f:
                ext_data = json.load(f)

            import copy
            traces = copy.deepcopy(traces_map[pid])
            ptc = ext_data['per_trace']
            gt = normalize_answer(gt_map[pid])

            result = run_z3_sica(ptc, traces)
            is_correct = result['sica_answer'] == gt

            per_problem[pid] = {
                'sica_answer': result['sica_answer'],
                'sica_correct': is_correct,
                'gt': gt,
                'scores': result['scores'],
                'answer_counts': result['answer_counts'],
                'constraints_stats': result['constraints_stats'],
                'maxsat_stats': result['maxsat_stats'],
            }
            correct += int(is_correct)
            total += 1
            total_constraints += result['constraints_stats']['total_extracted']
            total_unique += result['constraints_stats']['unique_after_dedup']
            total_excluded += result['maxsat_stats']['excluded']

        acc = correct / total if total > 0 else 0
        sica_results[cond_name] = {
            'accuracy': acc,
            'correct': correct,
            'total': total,
            'avg_constraints': total_constraints / total if total > 0 else 0,
            'avg_unique': total_unique / total if total > 0 else 0,
            'avg_excluded': total_excluded / total if total > 0 else 0,
            'per_problem': per_problem,
        }
        log.info(f"  {cond_name}: acc={acc:.4f} ({correct}/{total})")

    delta = {}
    for model in ['mistral', 'qwen3']:
        same_key = f'{model}_same'
        if model == 'mistral':
            cross_key = 'qwen3_cross_mistral'
            sc_acc = mistral_sc_acc
        else:
            cross_key = 'mistral_cross_qwen3'
            sc_acc = qwen3_sc_acc
        same_acc = sica_results.get(same_key, {}).get('accuracy', 0)
        cross_acc = sica_results.get(cross_key, {}).get('accuracy', 0)

        delta[model] = {
            'sc_acc': sc_acc,
            'same_sica_acc': same_acc,
            'cross_sica_acc': cross_acc,
            'delta_cross_vs_sc': cross_acc - sc_acc,
            'delta_cross_vs_same_sica': cross_acc - same_acc,
        }

    def mcnemar_test(per_problem_a, per_problem_b, key='sica_correct'):
        a_only = 0
        b_only = 0
        for pid in per_problem_a:
            if pid not in per_problem_b:
                continue
            a_ok = per_problem_a[pid][key]
            b_ok = per_problem_b[pid][key]
            if a_ok and not b_ok:
                a_only += 1
            elif b_ok and not a_ok:
                b_only += 1
        n = a_only + b_only
        if n == 0:
            return 1.0, a_only, b_only
        try:
            from scipy.stats import binom_test
            p = binom_test(min(a_only, b_only), n, 0.5)
        except ImportError:
            chi2 = (abs(a_only - b_only) - 1) ** 2 / max(n, 1)
            from math import exp, sqrt, pi
            p = 2 * (1 - 0.5 * (1 + (lambda x: x / (1 + 0.278393*x + 0.230389*x**2 + 0.000972*x**3 + 0.078108*x**4))(sqrt(chi2) / sqrt(2))))
            p = max(0, min(1, p))
        return p, a_only, b_only

    mcnemar_results = {}
    for model in ['mistral', 'qwen3']:
        same_key = f'{model}_same'
        cross_key = 'qwen3_cross_mistral' if model == 'mistral' else 'mistral_cross_qwen3'
        same_pp = sica_results.get(same_key, {}).get('per_problem', {})
        cross_pp = sica_results.get(cross_key, {}).get('per_problem', {})
        if same_pp and cross_pp:
            p, a, b = mcnemar_test(same_pp, cross_pp)
            mcnemar_results[f'{model}_same_vs_cross'] = {'p': round(p, 6), 'same_only': a, 'cross_only': b}
            log.info(f"  McNemar {model} same vs cross: p={p:.4f} ({a} vs {b})")

    def compute_br(per_problem_sica, pid_list):
        br_values = []
        for pid in pid_list:
            if pid not in per_problem_sica:
                continue
            entry = per_problem_sica[pid]
            if entry['sica_correct']:
                continue
            scores = entry.get('scores', {})
            if not scores:
                continue
            wrong_ans = entry['sica_answer']
            wrong_score = scores.get(wrong_ans, 0)
            total_score = sum(scores.values())
            if total_score > 0:
                br = wrong_score / total_score
                br_values.append(br)
        return sum(br_values) / len(br_values) if br_values else 0, len(br_values)

    br_results = {}
    for model in ['mistral', 'qwen3']:
        same_key = f'{model}_same'
        cross_key = 'qwen3_cross_mistral' if model == 'mistral' else 'mistral_cross_qwen3'
        same_pp = sica_results.get(same_key, {}).get('per_problem', {})
        cross_pp = sica_results.get(cross_key, {}).get('per_problem', {})
        same_br, same_n = compute_br(same_pp, pid_list)
        cross_br, cross_n = compute_br(cross_pp, pid_list)
        br_results[model] = {
            'same_br': round(same_br, 4), 'same_n': same_n,
            'cross_br': round(cross_br, 4), 'cross_n': cross_n,
            'delta_br': round(cross_br - same_br, 4),
        }
        log.info(f"  BR {model}: same={same_br:.4f}(n={same_n}), cross={cross_br:.4f}(n={cross_n})")

    def fleiss_kappa(traces_map, pid_list):
        categories = sorted(VALID_ANSWERS)
        n_items = 0
        P_i_sum = 0
        cat_totals = Counter()

        for pid in pid_list:
            if pid not in traces_map:
                continue
            answers = [normalize_answer(t['answer']) for t in traces_map[pid] if t.get('answer')]
            valid = [a for a in answers if a in VALID_ANSWERS]
            if len(valid) < 2:
                continue
            n_r = len(valid)
            counts = Counter(valid)
            P_i = (sum(counts[c] ** 2 for c in categories) - n_r) / (n_r * (n_r - 1)) if n_r > 1 else 0
            P_i_sum += P_i
            n_items += 1
            for c in categories:
                cat_totals[c] += counts.get(c, 0)

        if n_items == 0:
            return 0.0
        P_bar = P_i_sum / n_items
        total_votes = sum(cat_totals.values())
        P_e = sum((cat_totals[c] / total_votes) ** 2 for c in categories) if total_votes > 0 else 0
        if P_e >= 1:
            return 1.0
        return (P_bar - P_e) / (1 - P_e)

    kappa_within_mistral = fleiss_kappa(mistral_traces, pid_list)
    kappa_within_qwen3 = fleiss_kappa(qwen3_traces, pid_list)

    cross_traces = {}
    for pid in pid_list:
        if pid in mistral_traces and pid in qwen3_traces:
            combined = []
            for t in mistral_traces[pid][:6]:
                combined.append({'answer': t['answer'], 'trace_idx': len(combined)})
            for t in qwen3_traces[pid][:6]:
                combined.append({'answer': t['answer'], 'trace_idx': len(combined)})
            cross_traces[pid] = combined
    kappa_cross = fleiss_kappa(cross_traces, pid_list)

    kappa_results = {
        'within_mistral': round(kappa_within_mistral, 4),
        'within_qwen3': round(kappa_within_qwen3, 4),
        'cross_model': round(kappa_cross, 4),
    }
    log.info(f"  Fleiss kappa: mistral={kappa_within_mistral:.4f}, qwen3={kappa_within_qwen3:.4f}, cross={kappa_cross:.4f}")

    sica_summary = {}
    for k_name, v in sica_results.items():
        sica_summary[k_name] = {kk: vv for kk, vv in v.items() if kk != 'per_problem'}

    results = {
        'config': {'N': N, 'K': K, 'T_gen': T_GEN, 'T_ext': T_EXT, 'seed': SEED},
        'sc': {'mistral': round(mistral_sc_acc, 4), 'qwen3': round(qwen3_sc_acc, 4)},
        'sica': sica_summary,
        'delta_pp': delta,
        'mcnemar': mcnemar_results,
        'bias_ratio': br_results,
        'fleiss_kappa': kappa_results,
    }

    out_file = os.path.join(OUT_DIR, 'results.json')
    with open(out_file, 'w') as f:
        json.dump(results, f, indent=2)
    log.info(f"Results saved to {out_file}")

    detail_file = os.path.join(OUT_DIR, 'per_problem_details.json')
    details = {'mistral_sc': mistral_sc_pp, 'qwen3_sc': qwen3_sc_pp}
    for k_name, v in sica_results.items():
        details[k_name] = v.get('per_problem', {})
    with open(detail_file, 'w') as f:
        json.dump(details, f, indent=2)

    print("\n" + "="*70)
    print("Cross-Model SICA Results - ProofWriter D5 N=204")
    print("="*70)
    print(f"{'Condition':<35} {'Acc':>8} {'N':>5}")
    print("-"*50)
    print(f"{'Mistral SC':<35} {mistral_sc_acc:>8.4f} {mistral_sc_n:>5}")
    print(f"{'Qwen3 SC':<35} {qwen3_sc_acc:>8.4f} {qwen3_sc_n:>5}")
    for k_name, v in sica_summary.items():
        print(f"{k_name:<35} {v['accuracy']:>8.4f} {v['total']:>5}")
    print("-"*50)
    for model, d in delta.items():
        print(f"dpp {model} cross vs SC:       {d['delta_cross_vs_sc']:>+8.4f}")
        print(f"dpp {model} cross vs same SICA: {d['delta_cross_vs_same_sica']:>+8.4f}")
    print("-"*50)
    for model, br in br_results.items():
        print(f"BR {model}: same={br['same_br']:.4f}(n={br['same_n']}), cross={br['cross_br']:.4f}(n={br['cross_n']}), d={br['delta_br']:+.4f}")
    print("-"*50)
    print(f"Fleiss kappa: mistral={kappa_within_mistral:.4f}, qwen3={kappa_within_qwen3:.4f}, cross={kappa_cross:.4f}")
    for k_name, v in mcnemar_results.items():
        print(f"McNemar {k_name}: p={v['p']:.4f}")
    print("="*70)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--phase', choices=['1', '2', 'all'], default='all')
    args = parser.parse_args()

    if args.phase in ('1', 'all'):
        phase1()
    if args.phase in ('2', 'all'):
        phase2()
