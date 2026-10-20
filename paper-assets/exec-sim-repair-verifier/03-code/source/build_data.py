# Build (code, test) -> pass/fail training data from HumanEval + MBPP
# Mutations on canonical solutions generate fail examples; actual execution verifies labels.

import argparse
import ast
import json
import os
import random
import re
import subprocess
import sys
import textwrap
import time
from collections import Counter, defaultdict
from pathlib import Path

TIMEOUT = 5  # seconds per test execution
MUTANTS_PER_SOLUTION = 4
SEED = 42


# ── Mutation strategies ──────────────────────────────────────────────

def mutate_operators(code: str) -> list[str]:
    """Swap arithmetic/comparison operators."""
    swaps = [
        ('+', '-'), ('-', '+'), ('*', '/'), ('/', '*'),
        ('==', '!='), ('!=', '=='),
        ('<=', '<'), ('>=', '>'), ('<', '<='), ('>', '>='),
        (' and ', ' or '), (' or ', ' and '),
    ]
    results = []
    for old, new in swaps:
        if old in code:
            mutated = code.replace(old, new, 1)
            if mutated != code:
                results.append(mutated)
    return results


def mutate_off_by_one(code: str) -> list[str]:
    """Shift integer literals by ±1."""
    results = []
    # Find integer literals (not inside strings ideally, but good enough)
    for match in re.finditer(r'(?<![a-zA-Z_"\'])(\d+)(?![a-zA-Z_"\'])', code):
        val = int(match.group(1))
        for delta in [1, -1]:
            new_val = val + delta
            if new_val < 0:
                continue
            mutated = code[:match.start(1)] + str(new_val) + code[match.end(1):]
            if mutated != code:
                results.append(mutated)
    return results


def mutate_return_value(code: str) -> list[str]:
    """Modify return statements."""
    results = []
    lines = code.split('\n')
    for i, line in enumerate(lines):
        stripped = line.lstrip()
        if stripped.startswith('return '):
            expr = stripped[7:].strip()
            mutations = []
            if expr == 'True':
                mutations.append(line.replace('True', 'False'))
            elif expr == 'False':
                mutations.append(line.replace('False', 'True'))
            elif expr == 'None':
                mutations.append(line.replace('None', '0'))
            else:
                # Negate or wrap
                indent = line[:len(line) - len(stripped)]
                mutations.append(f"{indent}return None")
                if expr.isdigit():
                    mutations.append(f"{indent}return {int(expr) + 1}")
                else:
                    mutations.append(f"{indent}return not ({expr})")
            for m in mutations:
                new_lines = lines[:i] + [m] + lines[i+1:]
                results.append('\n'.join(new_lines))
    return results


def mutate_boundary(code: str) -> list[str]:
    """Remove early-return boundary checks (if ... return ...)."""
    results = []
    lines = code.split('\n')
    i = 0
    while i < len(lines):
        stripped = lines[i].lstrip()
        if stripped.startswith('if ') and i + 1 < len(lines):
            next_stripped = lines[i+1].lstrip()
            if next_stripped.startswith('return '):
                # Remove the if + return (2 lines)
                new_lines = lines[:i] + lines[i+2:]
                candidate = '\n'.join(new_lines)
                if candidate.strip():
                    results.append(candidate)
        i += 1
    return results


def mutate_variable_swap(code: str) -> list[str]:
    """Swap two variable names in function body."""
    results = []
    try:
        tree = ast.parse(code)
    except SyntaxError:
        return results

    # Collect variable names assigned in the function
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef):
            assigned = set()
            for child in ast.walk(node):
                if isinstance(child, ast.Name) and isinstance(getattr(child, 'ctx', None), ast.Store):
                    assigned.add(child.id)
            params = {a.arg for a in node.args.args}
            candidates = list(assigned - params)
            if len(candidates) >= 2:
                a, b = candidates[0], candidates[1]
                mutated = code.replace(a, '__TEMP__').replace(b, a).replace('__TEMP__', b)
                if mutated != code:
                    results.append(mutated)
            break
    return results


MUTATION_FUNCS = {
    'operator_swap': mutate_operators,
    'off_by_one': mutate_off_by_one,
    'return_value': mutate_return_value,
    'boundary_removal': mutate_boundary,
    'variable_swap': mutate_variable_swap,
}


def generate_mutants(code: str, n: int = MUTANTS_PER_SOLUTION) -> list[tuple[str, str]]:
    """Return up to n (mutated_code, mutation_type) pairs."""
    all_mutants = []
    for mtype, func in MUTATION_FUNCS.items():
        for m in func(code):
            all_mutants.append((m, mtype))

    random.shuffle(all_mutants)
    # Deduplicate
    seen = set()
    unique = []
    for m, mt in all_mutants:
        if m not in seen:
            seen.add(m)
            unique.append((m, mt))

    return unique[:n]


# ── Test execution ───────────────────────────────────────────────────

def execute_test(code: str, test: str, timeout: int = TIMEOUT) -> str:
    """Execute code + test, return 'pass', 'fail', 'timeout', or 'error'."""
    full_code = code + "\n" + test
    try:
        result = subprocess.run(
            [sys.executable, '-c', full_code],
            capture_output=True, text=True, timeout=timeout
        )
        if result.returncode == 0:
            return 'pass'
        else:
            return 'fail'
    except subprocess.TimeoutExpired:
        return 'timeout'
    except Exception:
        return 'error'


# ── HumanEval processing ────────────────────────────────────────────

def extract_humaneval_tests(test_code: str, entry_point: str) -> list[str]:
    """Extract individual assert statements from HumanEval test code."""
    lines = test_code.strip().split('\n')
    assert_lines = []
    for line in lines:
        stripped = line.strip()
        if 'assert' in stripped and ('candidate(' in stripped or f'{entry_point}(' in stripped):
            cleaned = stripped.replace('candidate(', f'{entry_point}(')
            if cleaned.startswith('assert'):
                assert_lines.append(cleaned)
    return assert_lines


def process_humaneval(dataset, dry_run: bool = False):
    """Process HumanEval dataset."""
    samples = []
    stats = {'total_problems': 0, 'skipped_no_test': 0, 'execution_results': Counter()}

    items = list(dataset['test'])
    if dry_run:
        items = items[:10]

    for item in items:
        task_id = item['task_id']
        prompt = item['prompt']
        canonical = item['canonical_solution']
        test_code = item['test']
        entry_point = item['entry_point']

        stats['total_problems'] += 1

        # Build full solution
        full_solution = prompt + canonical

        # Extract individual test cases
        # HumanEval tests are in a check(candidate) function format
        # We need to handle this properly
        test_assertions = extract_humaneval_tests(test_code, entry_point)

        if not test_assertions:
            stats['skipped_no_test'] += 1
            continue

        # For HumanEval, the test function wraps assertions with candidate = entry_point
        # We need to build executable test code
        for test_str in test_assertions:
            # Positive: canonical solution + test
            result = execute_test(full_solution, test_str)
            stats['execution_results'][result] += 1

            if result == 'pass':
                samples.append({
                    'code': full_solution,
                    'test': test_str,
                    'label': 1,
                    'source': 'humaneval',
                    'problem_id': task_id,
                    'mutation_type': 'original',
                })
            elif result in ('timeout', 'error'):
                continue
            else:
                # Canonical failed? Skip this test
                continue

            # Negative: mutants + test
            mutants = generate_mutants(full_solution)
            for mutant_code, mtype in mutants:
                mresult = execute_test(mutant_code, test_str)
                stats['execution_results'][f'mutant_{mresult}'] += 1

                if mresult == 'fail':
                    samples.append({
                        'code': mutant_code,
                        'test': test_str,
                        'label': 0,
                        'source': 'humaneval',
                        'problem_id': task_id,
                        'mutation_type': mtype,
                    })
                elif mresult == 'pass':
                    # Mutation didn't break it - still valid pass data
                    samples.append({
                        'code': mutant_code,
                        'test': test_str,
                        'label': 1,
                        'source': 'humaneval',
                        'problem_id': task_id,
                        'mutation_type': mtype,
                    })
                # timeout/error: skip

    return samples, stats


# ── MBPP processing ─────────────────────────────────────────────────

def process_mbpp(dataset, dry_run: bool = False):
    """Process MBPP dataset."""
    samples = []
    stats = {'total_problems': 0, 'skipped_no_test': 0, 'execution_results': Counter()}

    items = list(dataset['test']) if 'test' in dataset else list(dataset['train'])
    # MBPP has train/test/validation splits; use all
    for split_name in dataset:
        if split_name == (list(dataset.keys())[0]):
            continue  # already got first split
        items.extend(list(dataset[split_name]))

    # Deduplicate by task_id
    seen_ids = set()
    unique_items = []
    for item in items:
        tid = item['task_id']
        if tid not in seen_ids:
            seen_ids.add(tid)
            unique_items.append(item)
    items = unique_items

    if dry_run:
        items = items[:10]

    for item in items:
        task_id = f"MBPP/{item['task_id']}"
        code = item['code']
        test_list = item['test_list']

        stats['total_problems'] += 1

        if not test_list:
            stats['skipped_no_test'] += 1
            continue

        for test_str in test_list:
            # Positive: canonical code + test
            result = execute_test(code, test_str)
            stats['execution_results'][result] += 1

            if result == 'pass':
                samples.append({
                    'code': code,
                    'test': test_str,
                    'label': 1,
                    'source': 'mbpp',
                    'problem_id': task_id,
                    'mutation_type': 'original',
                })
            elif result in ('timeout', 'error'):
                continue
            else:
                continue

            # Negative: mutants
            mutants = generate_mutants(code)
            for mutant_code, mtype in mutants:
                mresult = execute_test(mutant_code, test_str)
                stats['execution_results'][f'mutant_{mresult}'] += 1

                if mresult == 'fail':
                    samples.append({
                        'code': mutant_code,
                        'test': test_str,
                        'label': 0,
                        'source': 'mbpp',
                        'problem_id': task_id,
                        'mutation_type': mtype,
                    })
                elif mresult == 'pass':
                    samples.append({
                        'code': mutant_code,
                        'test': test_str,
                        'label': 1,
                        'source': 'mbpp',
                        'problem_id': task_id,
                        'mutation_type': mtype,
                    })

    return samples, stats


# ── Data splitting ───────────────────────────────────────────────────

def split_by_problem(samples: list[dict], train_ratio=0.8, val_ratio=0.1):
    """Split data by problem_id so same problem doesn't leak across splits."""
    problem_ids = sorted(set(s['problem_id'] for s in samples))
    random.shuffle(problem_ids)

    n = len(problem_ids)
    n_train = int(n * train_ratio)
    n_val = int(n * val_ratio)

    train_ids = set(problem_ids[:n_train])
    val_ids = set(problem_ids[n_train:n_train + n_val])
    test_ids = set(problem_ids[n_train + n_val:])

    train = [s for s in samples if s['problem_id'] in train_ids]
    val = [s for s in samples if s['problem_id'] in val_ids]
    test = [s for s in samples if s['problem_id'] in test_ids]

    return train, val, test


# ── Statistics ───────────────────────────────────────────────────────

def compute_stats(samples: list[dict], split_name: str = 'all') -> dict:
    """Compute dataset statistics."""
    if not samples:
        return {'split': split_name, 'total': 0}

    labels = [s['label'] for s in samples]
    sources = Counter(s['source'] for s in samples)
    mutation_types = Counter(s['mutation_type'] for s in samples)

    n_pass = sum(labels)
    n_fail = len(labels) - n_pass
    majority = max(n_pass, n_fail) / len(labels) if labels else 0

    # Per mutation_type fail rate
    mutation_fail_rates = {}
    for mt in mutation_types:
        mt_samples = [s for s in samples if s['mutation_type'] == mt]
        mt_fails = sum(1 for s in mt_samples if s['label'] == 0)
        mutation_fail_rates[mt] = {
            'count': len(mt_samples),
            'fail_count': mt_fails,
            'fail_rate': mt_fails / len(mt_samples) if mt_samples else 0,
        }

    # Per source stats
    source_stats = {}
    for src in sources:
        src_samples = [s for s in samples if s['source'] == src]
        src_pass = sum(1 for s in src_samples if s['label'] == 1)
        src_fail = len(src_samples) - src_pass
        source_stats[src] = {
            'total': len(src_samples),
            'pass': src_pass,
            'fail': src_fail,
            'pass_ratio': src_pass / len(src_samples),
        }

    return {
        'split': split_name,
        'total': len(samples),
        'pass': n_pass,
        'fail': n_fail,
        'pass_ratio': round(n_pass / len(labels), 4),
        'fail_ratio': round(n_fail / len(labels), 4),
        'majority_baseline_accuracy': round(majority, 4),
        'by_source': source_stats,
        'by_mutation_type': mutation_fail_rates,
    }


# ── Main ─────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(description='Build (code, test) → pass/fail training data')
    parser.add_argument('--output-dir', default='data', help='Output directory')
    parser.add_argument('--dry-run', action='store_true', help='Process only 10 problems per dataset')
    parser.add_argument('--seed', type=int, default=SEED)
    args = parser.parse_args()

    random.seed(args.seed)
    os.makedirs(args.output_dir, exist_ok=True)

    print(f"Loading datasets...")
    from datasets import load_dataset

    print("Loading HumanEval...")
    try:
        humaneval = load_dataset("openai/openai_humaneval", trust_remote_code=True)
    except Exception as e:
        print(f"  Failed with openai/openai_humaneval: {e}")
        try:
            humaneval = load_dataset("openai_humaneval", trust_remote_code=True)
        except Exception as e2:
            print(f"  Also failed with openai_humaneval: {e2}")
            humaneval = None

    print("Loading MBPP...")
    try:
        mbpp = load_dataset("google-research-datasets/mbpp", trust_remote_code=True)
    except Exception as e:
        print(f"  Failed with google-research-datasets/mbpp: {e}")
        try:
            mbpp = load_dataset("mbpp", trust_remote_code=True)
        except Exception as e2:
            print(f"  Also failed with mbpp: {e2}")
            mbpp = None

    all_samples = []
    all_stats = {}
    removed = {'timeout': 0, 'error': 0}

    if humaneval is not None:
        print(f"\nProcessing HumanEval ({'dry-run' if args.dry_run else 'full'})...")
        he_samples, he_stats = process_humaneval(humaneval, dry_run=args.dry_run)
        print(f"  HumanEval: {len(he_samples)} samples from {he_stats['total_problems']} problems")
        print(f"  Execution results: {dict(he_stats['execution_results'])}")
        all_samples.extend(he_samples)
        all_stats['humaneval'] = he_stats

    if mbpp is not None:
        print(f"\nProcessing MBPP ({'dry-run' if args.dry_run else 'full'})...")
        mb_samples, mb_stats = process_mbpp(mbpp, dry_run=args.dry_run)
        print(f"  MBPP: {len(mb_samples)} samples from {mb_stats['total_problems']} problems")
        print(f"  Execution results: {dict(mb_stats['execution_results'])}")
        all_samples.extend(mb_samples)
        all_stats['mbpp'] = mb_stats

    if not all_samples:
        print("ERROR: No samples generated!")
        sys.exit(1)

    print(f"\nTotal samples before split: {len(all_samples)}")

    # Split
    train, val, test = split_by_problem(all_samples)

    # Compute stats
    overall_stats = compute_stats(all_samples, 'all')
    train_stats = compute_stats(train, 'train')
    val_stats = compute_stats(val, 'val')
    test_stats = compute_stats(test, 'test')

    # Save JSONL files
    for name, data in [('train', train), ('val', val), ('test', test)]:
        path = os.path.join(args.output_dir, f'{name}.jsonl')
        with open(path, 'w') as f:
            for s in data:
                f.write(json.dumps(s) + '\n')
        print(f"  Saved {path}: {len(data)} samples")

    # Save stats
    stats_summary = {
        'overall': overall_stats,
        'train': train_stats,
        'val': val_stats,
        'test': test_stats,
        'processing_stats': all_stats,
        'removed': removed,
    }
    stats_path = os.path.join(args.output_dir, 'stats.json')
    with open(stats_path, 'w') as f:
        json.dump(stats_summary, f, indent=2)
    print(f"  Saved {stats_path}")

    # Print summary
    print(f"\n{'='*60}")
    print(f"SUMMARY")
    print(f"{'='*60}")
    print(f"Total samples: {overall_stats['total']}")
    print(f"  Pass: {overall_stats['pass']} ({overall_stats['pass_ratio']:.1%})")
    print(f"  Fail: {overall_stats['fail']} ({overall_stats['fail_ratio']:.1%})")
    print(f"  Majority baseline: {overall_stats['majority_baseline_accuracy']:.1%}")
    print(f"Splits: train={len(train)}, val={len(val)}, test={len(test)}")
    print(f"\nBy source:")
    for src, s in overall_stats['by_source'].items():
        print(f"  {src}: {s['total']} (pass={s['pass']}, fail={s['fail']})")
    print(f"\nBy mutation type:")
    for mt, s in overall_stats['by_mutation_type'].items():
        print(f"  {mt}: {s['count']} samples, fail_rate={s['fail_rate']:.1%}")


if __name__ == '__main__':
    main()
