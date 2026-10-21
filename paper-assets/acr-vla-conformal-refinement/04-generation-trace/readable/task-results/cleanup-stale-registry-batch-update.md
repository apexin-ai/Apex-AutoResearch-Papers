# cleanup stale registry batch update

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_cleanup_stale-registry-batch-update_20260526T161748_result.json`
- **Structured JSON:** [`252b03f37dcb606af023.json`](../../sessions/25/252b03f37dcb606af023.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All 21 experiments updated.

**Summary:**

| Category | Count | Final state |
|---|---|---|
| Eval (success) | 8 | DONE, conclusion=success, metrics+log+ckpt set |
| Eval (negative) | 1 | DONE, conclusion=negative (pi05-adaptive-long-s44-cqa1, SR=0%) |
| Precompute | 2 | DONE, conclusion=success, cache metrics recorded |
| Failed/no-trace | 3 | DONE, conclusion=failed (smolvla-lerobot-{goal,spatial}-v3, supp-goal-k2mean-s47) |
| PREPARING→DONE | 7 | Transitioned via PREPARING→QUEUED→RUNNING(+spec)→DONE; 1 negative (pi05-s43), 6 success (5 D149 CRM evals + 1 spatial CRM) |

**State machine note:** PREPARING → DONE is not a valid direct transition. The allowed path is PREPARING → QUEUED → RUNNING (requires `spec` with command/server/data_path/data_count/model_name/seed/checkpoint_source/eval_data) → DONE (requires `log_path` and `checkpoint_path` first). The QUEUED transition bumps `retry_count` by 1.

---
