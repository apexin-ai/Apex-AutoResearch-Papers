# paper batch b intro

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_batch-b-intro_20260518T003146_result.json`
- **Structured JSON:** [`1c0cb903baedeb2d3af0.json`](../../sessions/1c/1c0cb903baedeb2d3af0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All three changes applied. Checklist:

1. **em-dash (`—`)**: 0 matches
2. **explanatory en-dash (` – `)**: 0 matches (only `--` for numeric ranges, which is correct LaTeX)
3. **`-ing,` pattern**: 0 matches
4. **Contribution list**: each item maps to a section (Contrib 1 → §3 method + §4 evaluation suite; Contrib 2 → §4 DDR results)
5. **7-17% citation**: retained on line 6, reframed as "evidence that LLM text already re-enters training pipelines at scale" rather than a problem-to-solve

Summary of changes:
- **B1**: Para 1 rewritten to open from "recursive generation dynamics" angle, citing model collapse literature (`curse_of_recursion`, `self_consuming_mad`) as theoretical motivation. 7-17% stat reframed as evidence of pipeline re-entry.
- **B2**: Contribution 2 now describes DDR as pure phenomenon (no F1 number). The 0.694 F1 remains in the results paragraph (line 17) for narrative flow.
- **B5**: Novelty sentence added at line 14, distinguishing DDR's structured decomposition from aggregate drift in model collapse literature.

---
