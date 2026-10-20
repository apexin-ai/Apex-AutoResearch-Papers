# code exp 076 debate pipeline

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp-076-debate-pipeline_20260519T170119_result.json`
- **Structured JSON:** [`eb5aeb39126188318a17.json`](../../sessions/eb/eb5aeb39126188318a17.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All tasks complete. Summary:

**`run_debate.py` deployed and validated on `westd-25068`.**

### Dry-run results (3 FOLIO problems)

| Problem | GT | Debate | SC | Debate ✓ | SC ✓ | Valid debates | Fallback |
|---------|------|---------|------|----------|------|--------------|----------|
| folio_0 | Unknown | Unknown | True | ✓ | ✗ | 2/3 | No |
| folio_1 | True | True | True | ✓ | ✓ | 0/3 | Yes |
| folio_2 | False | False | False | ✓ | ✓ | 0/3 | Yes |

- **Debate accuracy: 100% (3/3)** vs SC: 66.7% (2/3), delta +33.3%
- 157 total FOL constraints extracted, Z3 dedup + MAX-SAT scoring all working
- Fallback to SC trace extraction triggered correctly when critic failed to produce a different answer (2/3 problems)
- Output JSON at `results/exp076_debate_dryrun/results.json`, intermediates saved per-problem
- No vLLM cleanup needed (pre-existing instance)
- Wall time: 6.6 min for 3 problems

The pipeline is ready for full-scale runs on `folio_full.json` (204 problems).

---
