# code z3 feedback refinement

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_z3-feedback-refinement_20260518T171721_result.json`
- **Structured JSON:** [`ca9046475396b08db62a.json`](../../sessions/ca/ca9046475396b08db62a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All files written and verified. Summary:

**Files created on remote server:**
- `sica/z3_feedback.py` (316 lines) — `Z3FeedbackRefiner` class with UNSAT core extraction, refinement prompt construction, LLM call, and multi-round feedback loop
- `run_z3_feedback_folio.py` (272 lines) — entry script that loads existing traces/constraints, runs Z3 feedback refinement, re-scores with dedup+MAX-SAT, outputs JSON with z3fb/vanilla/SC accuracy comparison
- `scripts/run_z3_feedback_folio.sh` (28 lines) — launcher with vLLM auto-start

**Verification results:**
- `--help` works, all imports resolve
- Z3 UNSAT core detection tested on synthetic + real data: correctly identifies SAT (empty core) and UNSAT (conflicting constraints)
- Scan of all 204 problems: **8 traces across 4 problems** have internal UNSAT (0.3%). One of those (`folio_23`) is currently wrong for both SICA and SC, so refinement could potentially fix it. The other 3 are already correct.

**To run the experiment** (when GPU is free):
```bash
bash scripts/run_z3_feedback_folio.sh 8000 0
```

---
