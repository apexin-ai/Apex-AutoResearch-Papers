# audit westd 27271

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_westd-27271_20260526T133354_result.json`
- **Structured JSON:** [`b0240d06bbb45abdc229.json`](../../sessions/b0/b0240d06bbb45abdc229.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

```
SERVER: westd-27271
GPU_COUNT: 2

[cuda:0] 70% | 15964/97887 MiB | L2norm k=0.7 Goal (eval_openvla_l2norm_k07_goal_seed42) | running | Task 3/10
[cuda:1] 71% | 15964/97887 MiB | Random k=0.7 Goal v4 (eval_openvla_random_k07_goal_seed42_v4) | running | Task 9/10

COMPLETED_EXPERIMENTS:
NONE

FREE_GPUS:
NONE
```

Random k=0.7 Goal v4 接近完成（Task 9/10），L2norm k=0.7 Goal 还在早期（Task 3/10）。

---
