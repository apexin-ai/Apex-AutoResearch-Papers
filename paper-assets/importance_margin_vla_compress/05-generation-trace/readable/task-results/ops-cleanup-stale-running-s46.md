# ops cleanup stale running s46

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_cleanup_stale_running_s46_20260528T223033_result.json`
- **Structured JSON:** [`4cfbbb749885032dcfad.json`](../../sessions/4c/4cfbbb749885032dcfad.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All 4 experiments were already transitioned to DONE by completion hooks (EXIT_CODE=0). I've updated metrics for the 3 accessible ones.

**Summary:**

| Experiment | SR | Status | Notes |
|---|---|---|---|
| `eval_pi05_random_k05_long_seed46_strict_w41` | **50.2%** | DONE/success | metrics updated |
| `eval_pi05_random_k095_long_seed46_strict_w41` | **60.8%** | DONE/success | metrics updated |
| `eval_pi05_attn_k095_long_seed46_strict_w38` | **75.2%** | DONE/success | metrics updated |
| `eval_pi05_l2norm_k095_long_seed46_strict_w27` | **unknown** | DONE/success (hook-confirmed) | westd-27271 unreachable, metrics pending — log at `~/runs/.../eval_pi05_l2norm_k095_long_seed46_strict_w27.log` when server is back |

The w27 experiment completed successfully (hook fired at 10:58 UTC, EXIT_CODE=0, wall_clock=2.11h), but the actual success rate needs to be read from the log once westd-27271 is reachable again.

---
