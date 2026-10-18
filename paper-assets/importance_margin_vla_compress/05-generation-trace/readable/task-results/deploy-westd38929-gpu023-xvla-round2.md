# deploy westd38929 gpu023 xvla round2

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy-westd38929-gpu023-xvla-round2_20260524T005804_result.json`
- **Structured JSON:** [`2c9be9e72f029794f6e2.json`](../../sessions/2c/2c9be9e72f029794f6e2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**All proposed experiments are already complete.** The X-VLA k=0.5 CV matrix is nearly fully populated:

### X-VLA k=0.5 CV Status

| Suite | Method | seed42 | seed43 | Mean |
|-------|--------|--------|--------|------|
| Goal | Random | 67.2% | 68.6% | 67.9% |
| Goal | L2norm | 59.0% | 60.2% | 59.6% |
| Object | Random | 70.6% | 71.0% | 70.8% |
| Object | L2norm | 43.4% | 43.0% | 43.2% |
| Long | Random | 61.6% | 58.2% | 59.9% |
| Long | L2norm | 45.0% | **running** | — |
| Spatial | Random | 71.4% | 72.6% | 72.0% |
| Spatial | L2norm | 58.8% | 59.0% | 58.9% |

**Only remaining gap**: L2 Long seed43 on GPU 1 (PID 432791, currently Task 9 ep 8/50 — will finish within ~10 min).

**Harvested**: L2 Spatial seed43 = 59.0% (registry updated to DONE).

**GPU 0/2/3 are free** with no more R6-C1 CV experiments to deploy. Available for other work.

---
