# ops zombie stan cleanup

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_zombie-stan-cleanup_20260515T091105_result.json`
- **Structured JSON:** [`25d1a6853b30f06532d1.json`](../../sessions/25/25d1a6853b30f06532d1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Process 452348 and all 4 zombie children are gone. No GPU memory was held by this process, so no GPU impact.

**Summary:**
- PID 452348 (exp006 pooled IRT) was stuck — Stan sampling completed 10+ hours ago, results saved to `exp006_results.json`, but parent never reaped 4 zombie children
- Killed the parent; all 5 processes cleaned up
- No GPU memory was affected (process wasn't using any GPU)

---
