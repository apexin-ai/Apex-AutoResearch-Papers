# exp p0 vanilla sft diagnosis

**When Does Unpaired Error Injection Help LLM Agents? Hypotheses from a Failed Transfer to Embodied Planning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exp_p0-vanilla-sft-diagnosis_20260514T105430_result.json`
- **Structured JSON:** [`664a07d5d12aebcafe07.json`](../../sessions/66/664a07d5d12aebcafe07.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Current state:

| Job | Step | Total | ETA | Loss | Acc |
|-----|------|-------|-----|------|-----|
| mini-vanilla-sft-v3 | 45 | 1,566 | ~55 min | 0.70 | 0.79 |
| mini-taxei-sft-v3 | 45 | 2,832 | ~1h32m | 0.84 | 0.77 |
| mini-random-sft-v3 | 45 | 3,405 | ~1h50m | 0.80 | 0.77 |

My earlier `vanilla_sft_aligned_v2` job was killed at step 105/207 (no checkpoint saved). It's been superseded by these v3 jobs which are all using aligned format data from `data/mini_pipeline_v3/`, running 3 epochs with grad_accum=8.

All three v3 jobs are healthy — loss declining normally, training on GPUs 0/1/2. The vanilla job will finish first in ~55 min, then eval can begin. Want me to monitor and kick off eval once they complete?

---
