# analysis codellama13b full trace head2048 seed42

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_codellama13b_full_trace_head2048_seed42_20260518T033554_result.json`
- **Structured JSON:** [`979b439858e3e18d476a.json`](../../sessions/97/979b439858e3e18d476a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry updated to DONE, artifact registered.

## Summary

**CodeLlama-13B head-2048: accuracy = 79.92% (CI: 77.6-82.3%)** — hypothesis confirmed.

| Metric | Value |
|--------|-------|
| accuracy | 79.92% |
| majority_baseline | 71.51% |
| lift | +8.4pp |
| pass F1 | 0.860 |
| fail F1 | 0.644 |
| train_loss | 0.0452 |
| eval_loss | 0.111 |
| n_test | 1190 |

All 4 model families now cluster in 75-82% for head-2048, confirming signal positional concentration is architecture-independent. CodeLlama-13B tail-2048 result is still pending to compute the gap.

---
