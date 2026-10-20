"""
Case study: run SICA pipeline on 3 specific problems with detailed constraint output.
"""
import json
import logging
import sys
import time
from collections import Counter

sys.path.insert(0, '/root/symb_invariant_consensus')

from sica.trace_generator import VLLMGenerator
from sica.constraint_extractor import ConstraintExtractor, VLLMBackend
from sica.z3_maxsat import ConstraintDeduplicator, MaxSATSolver
from sica.scorer import InvariantScorer
from sica.pipeline import _group_logic_answers, normalize_logic_answer

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
logger = logging.getLogger(__name__)

K = 12

def main():
    problems = json.load(open('data/case_study_3problems.json'))
    print(f"Loaded {len(problems)} problems")

    generator = VLLMGenerator(
        base_url="http://localhost:8000/v1",
        temperature=0.7,
        max_tokens=4096,
    )
    extractor = ConstraintExtractor(
        llm=VLLMBackend(base_url="http://localhost:8000/v1"),
        domain="logic",
    )
    deduplicator = ConstraintDeduplicator()
    solver = MaxSATSolver()
    scorer = InvariantScorer()

    all_results = []

    for prob in problems:
        pid = prob['id']
        gold = prob['answer']
        print(f"\n{'='*60}")
        print(f"Processing {pid} (gold={gold})")
        print(f"{'='*60}")

        t0 = time.time()

        # 1. Generate traces
        traces = generator.generate(prob['problem'], k=K)
        print(f"  Generated {len(traces)} traces")
        for t in traces:
            print(f"    trace_{t['trace_idx']}: answer={t['answer']}")

        # 2. Extract constraints per trace
        raw_constraints = extractor.extract_batch([t['trace'] for t in traces])
        print(f"  Extracted constraints from {len(raw_constraints)} traces")

        per_trace_data = []
        for i, (trace, constraints) in enumerate(zip(traces, raw_constraints)):
            per_trace_data.append({
                'trace_idx': i,
                'answer': trace['answer'],
                'num_constraints': len(constraints),
                'constraints': constraints,
                'trace_snippet': trace['trace'][:800],
            })
            print(f"    trace_{i}: {len(constraints)} constraints, answer={trace['answer']}")

        # 3. Deduplicate
        unique = deduplicator.deduplicate(raw_constraints)
        print(f"  Unique constraints after dedup: {len(unique)}")

        unique_data = []
        for uc in unique:
            unique_data.append({
                'expression': uc.expression,
                'z3_formula': str(uc.z3_formula),
                'weight': uc.weight,
                'source_traces': uc.source_traces,
            })

        # 4. MaxSAT
        maxsat_result = solver.solve(unique, timeout_ms=10000)
        print(f"  MaxSAT: {len(maxsat_result.satisfied)} satisfied, {len(maxsat_result.excluded)} excluded")

        satisfied_data = [{
            'expression': uc.expression,
            'z3_formula': str(uc.z3_formula),
            'weight': uc.weight,
            'source_traces': uc.source_traces,
        } for uc in maxsat_result.satisfied]

        excluded_data = [{
            'expression': uc.expression,
            'z3_formula': str(uc.z3_formula),
            'weight': uc.weight,
            'source_traces': uc.source_traces,
        } for uc in maxsat_result.excluded]

        # 5. Normalize logic answers before scoring
        for t in traces:
            if t.get('answer'):
                t['answer'] = normalize_logic_answer(t['answer'])

        # 5b. Score
        candidates = list(set(t['answer'] for t in traces if t['answer']))
        answer_counts = Counter(t['answer'] for t in traces if t['answer'])
        scores = scorer.score(maxsat_result, traces, candidates)
        sica_answer = scorer.select_answer(scores, answer_counts)

        # SC baseline
        groups = _group_logic_answers([t['answer'] for t in traces if t['answer']])
        sc_answer = max(groups, key=lambda k: len(groups[k]))
        sc_distribution = {k: len(v) for k, v in groups.items()}

        elapsed = time.time() - t0

        print(f"  SICA answer: {sica_answer} (scores={scores})")
        print(f"  SC answer:   {sc_answer} (dist={sc_distribution})")
        print(f"  Gold:        {gold}")
        print(f"  SICA correct: {sica_answer.lower().strip() == str(gold).lower().strip()}")
        print(f"  SC correct:   {sc_answer.lower().strip() == str(gold).lower().strip()}")
        print(f"  Time: {elapsed:.1f}s")

        result = {
            'id': pid,
            'gold': gold,
            'problem_text': prob['problem'],
            'sica_answer': sica_answer,
            'sc_answer': sc_answer,
            'sica_scores': scores,
            'sc_distribution': sc_distribution,
            'answer_counts': dict(answer_counts),
            'per_trace': per_trace_data,
            'unique_constraints': unique_data,
            'maxsat_satisfied': satisfied_data,
            'maxsat_excluded': excluded_data,
            'stats': {
                'total_extracted': sum(len(c) for c in raw_constraints),
                'traces_with_constraints': sum(1 for c in raw_constraints if c),
                'unique_after_dedup': len(unique),
                'maxsat_satisfied': len(maxsat_result.satisfied),
                'maxsat_excluded': len(maxsat_result.excluded),
                'total_weight': maxsat_result.total_weight,
                'solve_time_ms': maxsat_result.solve_time_ms,
            },
            'time_s': round(elapsed, 1),
        }
        all_results.append(result)

    import os
    os.makedirs('results', exist_ok=True)
    with open('results/case_study_constraints.json', 'w') as f:
        json.dump(all_results, f, indent=2, default=str)

    print(f"\n{'='*60}")
    print("SUMMARY")
    print(f"{'='*60}")
    for r in all_results:
        sica_ok = r['sica_answer'].lower().strip() == str(r['gold']).lower().strip()
        sc_ok = r['sc_answer'].lower().strip() == str(r['gold']).lower().strip()
        print(f"  {r['id']}: gold={r['gold']} SICA={r['sica_answer']}({'V' if sica_ok else 'X'}) SC={r['sc_answer']}({'V' if sc_ok else 'X'}) constraints={r['stats']['unique_after_dedup']} excluded={r['stats']['maxsat_excluded']}")
    print(f"\nResults saved to results/case_study_constraints.json")
    print("CASE_STUDY_DONE")


if __name__ == "__main__":
    main()
