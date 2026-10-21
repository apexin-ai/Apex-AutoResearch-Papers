# infra extract teal30 bce30 results v2

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_extract_teal30_bce30_results_v2_20260517T222852_result.json`
- **Structured JSON:** [`063f9e60c7e74e390051.json`](../../sessions/06/063f9e60c7e74e390051.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Both evals are nearly done with GSM8K (the last benchmark task):

| Experiment | Server | PPL | GSM8K Progress | ETA |
|---|---|---|---|---|
| **qwen14b_teal30_eval** | westd-41718 | 8.7332 | 1273/1319 (97%) | ~12 min |
| **qwen14b_bce30_s42_eval** | westd-34887 | 8.7634 | 1265/1319 (96%) | ~13 min |

Both should finish within ~15 minutes. Results (arc_challenge, winogrande, mmlu, gsm8k scores) will only be printed to the log after GSM8K generation completes. I'll check back shortly.

---
