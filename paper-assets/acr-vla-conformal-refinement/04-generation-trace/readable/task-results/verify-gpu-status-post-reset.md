# verify gpu status post reset

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_verify_gpu-status-post-reset_20260521T035638_result.json`
- **Structured JSON:** [`f13aac813a10361f27be.json`](../../sessions/f1/f13aac813a10361f27be.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

```
SERVER: bjb1-32546 (6x 4090)
  cuda:0 — PID 825135 ALIVE — norm003-seed76      — 24min elapsed, 5248 MiB
  cuda:1 — PID 814271 ALIVE — norm003-seed62-r3   — 41min elapsed, 5248 MiB
  cuda:2 — PID 805840 ALIVE — norm005-seed67 (old)— 1h12m elapsed, 2922 MiB
  cuda:3 — PID 814868 ALIVE — norm003-seed63-r3   — 41min elapsed, 5248 MiB
  cuda:4 — PID 815207 ALIVE — norm01-seed76       — 41min elapsed, 5248 MiB
  cuda:5 — PID 815997 ALIVE — norm01-seed77       — 41min elapsed, 5248 MiB

SERVER: bjb2-28827 (6x 4090)
  cuda:0 — PID 975409 ALIVE — adaptive-k-spatial-p90-seed44 — 54min, 4125 MiB
  cuda:1 — PID 979385 ALIVE — norm003-seed77      — 41min elapsed, 5248 MiB
  cuda:2 — PID 980044 ALIVE — norm003-seed78      — 41min elapsed, 5248 MiB
  cuda:3 — PID 981089 ALIVE — norm005-seed76      — 41min elapsed, 5248 MiB
  cuda:4 — PID 982680 ALIVE — norm005-seed77      — 41min elapsed, 5248 MiB
  cuda:5 — PID 969788 ALIVE — norm003-seed67 (old)— 1h12m elapsed, 3389 MiB

SERVER: bjb1-18228 (4x 4090)
  cuda:0 — PID 642428 ALIVE — norm003-seed66 (old)— 2h27m elapsed, 2922 MiB
  cuda:1 — PID 666593 ALIVE — norm01-seed67 (old) — 1h12m elapsed, 2922 MiB
  cuda:2 — PID 642506 ALIVE — norm005-seed66 (old)— 2h27m elapsed, 2922 MiB
  cuda:3 — PID 642775 ALIVE — norm01-seed66 (old) — 2h27m elapsed, 2922 MiB

SERVER: bjb2-40593 (1x 4090)
  cuda:0 — PID 811006 DEAD  — π0.5 baseline r2    — SR=0.0
  (also completed earlier: norm02-seed55 — SR=0.15)

SUMMARY:
  ALIVE: 16 (9 new norm sweep + 4 old bjb1-18228 + 2 old norm + 1 adaptive-k)
  COMPLETED:
    - π0.5 baseline r2 seed42 — SR=0.0 (confirmed zero again)
    - norm02-seed55 — SR=0.15
  FREE GPUs: bjb2-40593 cuda:0 (24 GB idle)

  All 9 new norm sweep experiments confirmed running.
```

---
