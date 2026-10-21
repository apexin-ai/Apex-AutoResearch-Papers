# monitor flatnli r6 health

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_flatnli_r6_health_20260514T180832_result.json`
- **Structured JSON:** [`8304895088824989ddd1.json`](../../sessions/83/8304895088824989ddd1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## flatnli_r6 Health Check

- **Current step**: 25/100 (running on cuda:3, PID 76958)
- **frac_zero_std trend**: 0.6 → 0.7 → **0.9** — crossed 0.8 threshold, accelerating
- **f1_reward trend**: 0.023 → 0.012 → **0.0** — extraction completely dead
- **flat_nli_reward trend**: 0.018 → 0.023 → **0.0** — also dead
- **KL trend**: 123M (step 5) → 0.043 → 0.036 → 0.056 (stable post-spike)
- **grad_norm**: 0.037 → 0.271 (recovered, but irrelevant — nothing to learn)
- **completion_length**: 773 → 586 → 399 (shrinking — model outputting less)
- **Verdict**: **COLLAPSE_CONFIRMED**
- **Recommendation**: Kill the run. The model abandoned extraction entirely — reward is 100% format-only. The initial KL explosion to 123M at step 5 likely caused irreversible policy damage. Registry notes updated. Awaiting your decision to terminate.

---
