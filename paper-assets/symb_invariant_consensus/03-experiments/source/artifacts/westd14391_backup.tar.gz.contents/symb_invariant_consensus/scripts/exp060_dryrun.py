#!/usr/bin/env python3
"""Dry-run for exp-060: test 3 problems with Qwen2.5-14B cross-extraction."""
import os, json, sys, time
sys.path.insert(0, "/root/symb_invariant_consensus")
from sica.constraint_extractor import ConstraintExtractor, APIBasedLLM
from sica.z3_maxsat import ConstraintDeduplicator, MaxSATSolver
from sica.scorer import InvariantScorer
from sica.pipeline import normalize_logic_answer
from baselines.self_consistency import SelfConsistency
from utils.math_equiv import is_equiv
from collections import Counter
from openai import OpenAI

traces_dir = "results/exp033_mistral_7b_folio204/intermediates"
files = sorted(f for f in os.listdir(traces_dir) if f.endswith(".json"))[:3]
print(f"Dry-run: {len(files)} files", flush=True)

client = OpenAI(base_url="http://localhost:8001/v1", api_key="[REDACTED]")
model_name = client.models.list().data[0].id
print(f"Model: {model_name}", flush=True)

llm = APIBasedLLM(base_url="http://localhost:8001/v1", model=model_name, temperature=0.3)
extractor = ConstraintExtractor(llm=llm)
deduplicator = ConstraintDeduplicator()
solver = MaxSATSolver()
scorer = InvariantScorer()
sc_baseline = SelfConsistency()

for fname in files:
    t0 = time.time()
    with open(os.path.join(traces_dir, fname)) as f:
        data = json.load(f)
    prob = data["problem"]
    sica_orig = data["sica_result"]
    traces = sica_orig["traces"]
    prob_id = prob["id"]
    extractor.domain = "logic"
    
    print(f"\n--- {prob_id} ({fname}) ---", flush=True)
    all_constraints = extractor.extract_batch([t["trace"] for t in traces])
    total_c = sum(len(c) for c in all_constraints)
    non_empty = sum(1 for c in all_constraints if c)
    unique_constraints = deduplicator.deduplicate(all_constraints)
    maxsat_result = solver.solve(unique_constraints, timeout_ms=10000)
    
    for t in traces:
        if t.get("answer"):
            t["answer"] = normalize_logic_answer(t["answer"])
    
    candidates = sorted(set(t["answer"] for t in traces if t["answer"]))
    answer_counts = Counter(t["answer"] for t in traces if t["answer"])
    scores = scorer.score(maxsat_result, traces, candidates)
    selected = scorer.select_answer(scores, answer_counts)
    
    sc_result = sc_baseline.run(
        prob,
        traces=[t["trace"] for t in traces],
        answers=[t["answer"] for t in traces],
    )
    sc_answer = sc_result.get("answer", "")
    
    cross_correct = is_equiv(selected, prob["answer"])
    orig_answer = sica_orig.get("answer", "")
    orig_correct = is_equiv(orig_answer, prob["answer"])
    sc_correct = is_equiv(sc_answer, prob["answer"])
    elapsed = time.time() - t0
    
    status_cross = "V" if cross_correct else "X"
    status_orig = "V" if orig_correct else "X"
    status_sc = "V" if sc_correct else "X"
    print(f"  cross={selected}({status_cross}) orig={orig_answer}({status_orig}) sc={sc_answer}({status_sc})", flush=True)
    print(f"  constraints: {total_c} -> {len(unique_constraints)} unique, time: {elapsed:.1f}s", flush=True)

print("\nDRY_RUN_OK", flush=True)
