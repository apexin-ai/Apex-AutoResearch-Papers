# check k0925 and deploy

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_k0925-and-deploy_20260521T234744_result.json`
- **Structured JSON:** [`cacab6e7c757f5eb11ae.json`](../../sessions/ca/cacab6e7c757f5eb11ae.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

k=0.925 is still running, currently on Task 7 (out of 10). Results so far are excellent:

| Task | SR |
|------|-----|
| T0 | 98% |
| T1 | 98% |
| T2 | 96% |
| T3 | 100% |
| T4 | 100% |
| T5 | 100% |
| T6 | 100% |
| T7 | in progress (10/10 so far) |

Running total: 346/350 = **98.9%** through 7 tasks. GPU2 is occupied.

```
k=0.925: SR=98.9% (cumulative) [进行中 task 7/10, ep 10]
GPU2: 占用 (PID 985048, 10541 MiB)
random k=0.9 Spatial: 未部署（k=0.925 仍在跑）
```

Estimated ~15 min remaining (3 tasks left). k=0.925 is performing nearly identically to k=0.95 (98.8%), confirming the plateau region holds.

---
