#!/usr/bin/env python3
"""Trace-only generation: skip extraction/MaxSAT, just save traces + SC answer.
Saves intermediates in same format as run_full_mvp.py for cross_model_extract.py compatibility.
"""
import json, os, sys, time, logging, glob
from collections import Counter

sys.path.insert(0, '/root/symb_invariant_consensus')
from sica.trace_generator import VLLMGenerator, extract_boxed_answer

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s",
                    handlers=[logging.StreamHandler(sys.stdout)])
log = logging.getLogger(__name__)

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
    return mapping.get(low, s.capitalize() if s else '')

def majority_vote(answers):
    valid = [a for a in answers if a in VALID_ANSWERS]
    if not valid:
        return ''
    counts = Counter(valid)
    mx = max(counts.values())
    top = sorted([a for a, c in counts.items() if c == mx])
    return top[0]

def main():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--api-base', default='http://localhost:8001/v1')
    parser.add_argument('--data', required=True)
    parser.add_argument('--output-dir', required=True)
    parser.add_argument('--k', type=int, default=12)
    parser.add_argument('--temperature', type=float, default=0.7)
    args = parser.parse_args()

    with open(args.data) as f:
        problems = json.load(f)
    log.info("Loaded %d problems", len(problems))

    os.makedirs(args.output_dir, exist_ok=True)

    existing = set()
    for fp in glob.glob(os.path.join(args.output_dir, '*.json')):
        existing.add(os.path.basename(fp).replace('.json', ''))
    log.info("Skipping %d already done", len(existing))

    generator = VLLMGenerator(
        base_url=args.api_base,
        temperature=args.temperature,
    )
    generator.domain = "math"

    remaining = [(i, p) for i, p in enumerate(problems) if p['id'] not in existing]
    log.info("Generating traces for %d remaining problems", len(remaining))

    times = []
    for progress, (idx, prob) in enumerate(remaining):
        t0 = time.time()
        prob_id = prob['id']
        print(f"\n--- [{progress+1}/{len(remaining)}] {prob_id} ---")

        traces = generator.generate(prob['problem'], k=args.k)
        for t in traces:
            raw_ans = t.get('answer', '')
            t['answer'] = normalize_answer(raw_ans)

        sc_answer = majority_vote([t['answer'] for t in traces])
        gt = prob.get('answer', '')
        sc_correct = sc_answer == gt

        elapsed = time.time() - t0
        times.append(elapsed)

        print(f"  SC: {sc_answer} ({'V' if sc_correct else 'X'}) | GT: {gt} | Time: {elapsed:.1f}s")
        if times:
            avg = sum(times) / len(times)
            rem = len(remaining) - progress - 1
            if rem > 0:
                print(f"  ETA: {avg * rem / 60:.1f} min ({rem} remaining)")

        intermediate = {
            "problem": prob,
            "sica_result": {
                "traces": traces,
                "answer": sc_answer,
                "answer_counts": dict(Counter(t['answer'] for t in traces)),
                "scores": {},
            }
        }
        out_path = os.path.join(args.output_dir, f"{prob_id}.json")
        with open(out_path, 'w') as f:
            json.dump(intermediate, f, indent=2, default=str)

        sys.stdout.flush()

    total = sum(times)
    done = len(existing) + len(remaining)
    log.info("Done: %d problems, wall time %.1f min", done, total / 60)
    print("TRACE_GEN_DONE")

if __name__ == '__main__':
    main()
