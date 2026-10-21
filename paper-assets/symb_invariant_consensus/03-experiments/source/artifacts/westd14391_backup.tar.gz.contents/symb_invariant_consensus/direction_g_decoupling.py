"""
Direction G: Constraint-Answer Decoupling
Truncate conclusion portions of CoT traces before FOL extraction to reduce confirmation bias.
"""
import json
import os
import re
import sys
import time
from collections import Counter
import httpx

sys.path.insert(0, '/root/symb_invariant_consensus')
from sica.constraint_extractor import LOGIC_EXTRACTION_PROMPT
from sica.z3_maxsat import ConstraintDeduplicator, MaxSATSolver
from sica.scorer import InvariantScorer

API_BASE = 'http://localhost:8020/v1'
INTERMEDIATES_DIR = '/root/symb_invariant_consensus/results/exp033_mistral_7b_folio204/intermediates'
RESULTS_FILE = '/root/symb_invariant_consensus/results/exp033_mistral_7b_folio204/exp033_results.json'
OUTPUT_DIR = '/root/symb_invariant_consensus/results/direction_g_decoupling'

CONCLUSION_PATTERNS = [
    r'\\boxed\{[^}]*\}',
    r'\bfinal\s+answer\s*[:.].*',
    r'\bthe\s+answer\s+is\b.*',
    r'\btherefore\b.*',
    r'\bthus\b[,.].*',
    r'\bhence\b[,.].*',
    r'\bin\s+conclusion\b.*',
    r'\bso\s+the\s+(statement|conclusion)\b.*',
    r'\bthis\s+means\s+the\s+conclusion\b.*',
    r'\bwe\s+can\s+conclude\b.*',
    r'\b(True|False|Unknown|Uncertain)\s*\.?\s*$',
]

CONCLUSION_RE = re.compile('|'.join(CONCLUSION_PATTERNS), re.IGNORECASE)


def normalize_answer(ans):
    ans = str(ans).strip().lower()
    if ans in ('true', 'yes', 't'):
        return 'True'
    elif ans in ('false', 'no', 'f'):
        return 'False'
    elif ans in ('unknown', 'uncertain', 'u', 'undetermined'):
        return 'Unknown'
    return ans.capitalize()


def truncate_conservative(trace_text):
    """Remove only the last sentence containing a conclusion marker."""
    lines = trace_text.rstrip().split('\n')
    for i in range(len(lines) - 1, -1, -1):
        if CONCLUSION_RE.search(lines[i]):
            return '\n'.join(lines[:i]).rstrip(), len(lines) - i
    return trace_text, 0


def truncate_standard(trace_text):
    """Remove from the first conclusion marker found in the last 40% of text."""
    lines = trace_text.rstrip().split('\n')
    cutoff_line = int(len(lines) * 0.6)
    first_match = None
    for i in range(cutoff_line, len(lines)):
        if CONCLUSION_RE.search(lines[i]):
            first_match = i
            break
    if first_match is not None:
        return '\n'.join(lines[:first_match]).rstrip(), len(lines) - first_match
    return truncate_conservative(trace_text)


def truncate_aggressive(trace_text):
    """Remove the last 30% of the trace regardless of content."""
    lines = trace_text.rstrip().split('\n')
    keep = max(1, int(len(lines) * 0.7))
    return '\n'.join(lines[:keep]).rstrip(), len(lines) - keep


TRUNCATION_STRATEGIES = {
    'conservative': truncate_conservative,
    'standard': truncate_standard,
    'aggressive': truncate_aggressive,
}


def extract_one(trace_text, model_id, max_retries=2):
    prompt = LOGIC_EXTRACTION_PROMPT.format(trace=trace_text)
    payload = {
        'model': model_id,
        'messages': [{'role': 'user', 'content': prompt}],
        'max_tokens': 2048,
        'temperature': 0.1,
    }
    for attempt in range(max_retries + 1):
        try:
            resp = httpx.post(f'{API_BASE}/chat/completions', json=payload, timeout=120)
            resp.raise_for_status()
            raw = resp.json()['choices'][0]['message']['content']
            text = re.sub(r'<think>.*?</think>', '', raw, flags=re.DOTALL).strip()
            json_match = re.search(r'\{[\s\S]*\}', text)
            if not json_match:
                return {'error': 'no JSON', 'constraints': []}
            data = json.loads(json_match.group())
            return {'constraints': data.get('constraints', []), 'extracted_answer': data.get('answer', '')}
        except json.JSONDecodeError:
            return {'error': 'JSON parse', 'constraints': []}
        except Exception as e:
            if attempt < max_retries:
                time.sleep(2)
                continue
            return {'error': str(e)[:200], 'constraints': []}


def run_sica_from_constraints(all_constraints, traces, candidates):
    deduplicator = ConstraintDeduplicator()
    solver = MaxSATSolver()
    scorer = InvariantScorer()

    unique = deduplicator.deduplicate(all_constraints)
    maxsat_result = solver.solve(unique, timeout_ms=10000)
    answer_counts = Counter(t['answer'] for t in traces if t.get('answer'))
    scores = scorer.score(maxsat_result, traces, candidates)
    selected = scorer.select_answer(scores, answer_counts)

    return {
        'answer': selected,
        'scores': scores,
        'constraints_stats': {
            'total_extracted': sum(len(c) for c in all_constraints),
            'unique_after_dedup': len(unique),
        },
        'maxsat_stats': {
            'satisfied': len(maxsat_result.satisfied),
            'excluded': len(maxsat_result.excluded),
            'total_weight': maxsat_result.total_weight,
        },
    }


def process_problem(pid, intermed, strategy_name, truncate_fn, model_id):
    traces = intermed['sica_result']['traces']
    gt = normalize_answer(intermed['problem']['answer'])

    truncation_stats = []
    all_constraints = []

    for t in traces:
        truncated, lines_removed = truncate_fn(t['trace'])
        original_len = len(t['trace'])
        truncated_len = len(truncated)
        chars_removed = original_len - truncated_len
        truncation_stats.append({
            'trace_idx': t['trace_idx'],
            'lines_removed': lines_removed,
            'chars_removed': chars_removed,
            'pct_removed': round(chars_removed / max(original_len, 1) * 100, 1),
            'matched': lines_removed > 0,
        })

        result = extract_one(truncated, model_id)
        all_constraints.append(result.get('constraints', []))

    normalized_traces = []
    for t in traces:
        nt = dict(t)
        nt['answer'] = normalize_answer(t.get('answer', ''))
        normalized_traces.append(nt)

    candidates = sorted(set(t['answer'] for t in normalized_traces if t['answer']))
    if not candidates:
        candidates = ['True', 'False', 'Unknown']

    sica_result = run_sica_from_constraints(all_constraints, normalized_traces, candidates)

    return {
        'pid': pid,
        'gt': gt,
        'strategy': strategy_name,
        'sica_answer': sica_result['answer'],
        'sica_correct': sica_result['answer'] == gt,
        'scores': sica_result['scores'],
        'constraints_stats': sica_result['constraints_stats'],
        'maxsat_stats': sica_result['maxsat_stats'],
        'truncation_stats': truncation_stats,
        'avg_pct_removed': round(
            sum(s['pct_removed'] for s in truncation_stats) / max(len(truncation_stats), 1), 1
        ),
        'traces_matched': sum(1 for s in truncation_stats if s['matched']),
    }


def main():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--n', type=int, default=None, help='Number of problems (None=all)')
    parser.add_argument('--strategies', nargs='+', default=['conservative', 'standard', 'aggressive'])
    parser.add_argument('--dry-run', action='store_true')
    args = parser.parse_args()

    os.makedirs(OUTPUT_DIR, exist_ok=True)

    r = httpx.get(f'{API_BASE}/models', timeout=10)
    model_id = r.json()['data'][0]['id']
    print(f'Model: {model_id}', flush=True)

    with open(RESULTS_FILE) as f:
        results_data = json.load(f)

    problems = results_data['results']
    if args.n:
        problems = problems[:args.n]
    n = len(problems)

    if args.dry_run:
        print(f'=== DRY RUN: {n} problems, strategies={args.strategies} ===', flush=True)

    all_results = {}

    for strategy_name in args.strategies:
        truncate_fn = TRUNCATION_STRATEGIES[strategy_name]
        print(f'\n=== Strategy: {strategy_name} ({n} problems) ===', flush=True)
        t_start = time.time()

        strategy_results = []
        for i, prob in enumerate(problems):
            pid = prob['problem_id']
            intermed_file = os.path.join(INTERMEDIATES_DIR, f'{pid}.json')
            with open(intermed_file) as f:
                intermed = json.load(f)

            result = process_problem(pid, intermed, strategy_name, truncate_fn, model_id)
            strategy_results.append(result)

            if (i + 1) % 10 == 0 or (i + 1) == n:
                elapsed = time.time() - t_start
                correct = sum(1 for r in strategy_results if r['sica_correct'])
                acc = correct / len(strategy_results)
                avg_trunc = sum(r['avg_pct_removed'] for r in strategy_results) / len(strategy_results)
                matched = sum(r['traces_matched'] for r in strategy_results) / (len(strategy_results) * 12) * 100
                rate = (i + 1) / elapsed
                eta = (n - i - 1) / rate if rate > 0 else 0
                print(
                    f'  [{i+1}/{n}] acc={acc:.3f} ({correct}/{len(strategy_results)}) '
                    f'avg_trunc={avg_trunc:.1f}% matched={matched:.0f}% '
                    f'{rate:.2f} prob/s ETA={eta:.0f}s',
                    flush=True,
                )

        all_results[strategy_name] = strategy_results

    sc_correct = sum(1 for p in problems if normalize_answer(p['ground_truth']) == normalize_answer(p['sc_answer']))
    sica_correct = sum(1 for p in problems if normalize_answer(p['ground_truth']) == normalize_answer(p['sica_answer']))

    print(f'\n{"="*60}')
    print(f'RESULTS COMPARISON (n={n})')
    print(f'{"="*60}')
    print(f'  SC baseline:     {sc_correct}/{n} = {sc_correct/n:.4f}')
    print(f'  SICA (original): {sica_correct}/{n} = {sica_correct/n:.4f}')

    summary = {
        'n_problems': n,
        'baselines': {
            'sc_accuracy': round(sc_correct / n, 4),
            'sc_correct': sc_correct,
            'sica_accuracy': round(sica_correct / n, 4),
            'sica_correct': sica_correct,
        },
        'strategies': {},
    }

    for strategy_name, results in all_results.items():
        correct = sum(1 for r in results if r['sica_correct'])
        acc = correct / len(results)
        avg_trunc = sum(r['avg_pct_removed'] for r in results) / len(results)
        matched_pct = sum(r['traces_matched'] for r in results) / (len(results) * 12) * 100
        avg_constraints = sum(r['constraints_stats']['total_extracted'] for r in results) / len(results)

        print(f'  Truncated-SICA ({strategy_name}): {correct}/{n} = {acc:.4f} '
              f'(avg_trunc={avg_trunc:.1f}%, matched={matched_pct:.0f}%)')

        summary['strategies'][strategy_name] = {
            'accuracy': round(acc, 4),
            'correct': correct,
            'avg_pct_removed': round(avg_trunc, 1),
            'traces_with_match_pct': round(matched_pct, 1),
            'avg_constraints_per_problem': round(avg_constraints, 1),
        }

    print(f'{"="*60}')

    out_file = os.path.join(OUTPUT_DIR, 'results.json')
    with open(out_file, 'w') as f:
        json.dump(summary, f, indent=2)
    print(f'Summary saved to {out_file}', flush=True)

    for strategy_name, results in all_results.items():
        detail_file = os.path.join(OUTPUT_DIR, f'per_problem_{strategy_name}.json')
        with open(detail_file, 'w') as f:
            json.dump(results, f, indent=2)
        print(f'Details saved to {detail_file}', flush=True)


if __name__ == '__main__':
    main()
