# code table t1 t2 fix

**The Likert Blindspot: Measurement-Mode Divergence in LLM Judge Style Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_table_t1_t2_fix_20260524T085536_result.json`
- **Structured JSON:** [`b366af6dd085983074e1.json`](../../sessions/b3/b366af6dd085983074e1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

The verbosity paragraph doesn't mention the d value directly — it only references Style OR and Orig OR, which are unchanged. No additional prose edits needed.

All four LaTeX modifications are complete:

| Table | Row | Old d (p) | New d (p) |
|-------|-----|-----------|-----------|
| 23 | AEval×Llama-70B×Form | 1.120 (<.001) | .212 (.012) |
| 23 | MTB×GPT-4o×Form | .167 (.016) | .111 (.016) |
| 24 | AEval×Claude×Verb | −.243 (.005) | .252 (.002) |
| 24 | MTB×Claude×Form | .245 (<.001) | .233 (<.001) |

Verified via `verify_table_corrections.py` using the same pooled-d formula (ddof=0) as `compute_table1_likert.py`. No prose references to these specific d values found elsewhere in the paper — only the table cells needed changing.

---
