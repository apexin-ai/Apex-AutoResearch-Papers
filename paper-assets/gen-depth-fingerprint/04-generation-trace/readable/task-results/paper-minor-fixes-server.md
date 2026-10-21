# paper minor fixes server

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_minor-fixes-server_20260517T175018_result.json`
- **Structured JSON:** [`841bda5da4608fdc10a4.json`](../../sessions/84/841bda5da4608fdc10a4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Both fixes applied. Summary:

---

**Fix 6 (R11-M7): Figure 3 PNG→PDF**
- `results.tex` line 112: changed `fig3_baseline_comparison.png` → `fig3_baseline_comparison.pdf`
- The PDF already existed both on the server and locally; no file copy needed.

**Fix 10 (R12-M3): Generation failure rate causes**
- `method.tex` line 33: replaced vague "after removing generation failures, exact duplicates, and passages shorter than 50 tokens" with exact numbers.
- Server investigation results:
  - Theoretical total: 39,815 (not ~40,000)
  - **Chain breaks: 2,746** — caused by empty/degenerate outputs at intermediate depths (`len(output) == 0` or `len(input) < 10`), which halted the chain and lost all remaining depths for that seed
  - **Feature extraction filter: 11** — texts too short for NLL computation
  - **Exact duplicates: 0** — none found in the current 8-gen dataset
  - Final: 37,058
- The original wording listed three causes (failures, duplicates, short passages), but the actual data shows almost entirely chain breaks (99.6% of the loss), with no duplicates and negligible short-text filtering.

---
