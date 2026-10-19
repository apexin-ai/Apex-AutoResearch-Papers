# monitor object progress check

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_object-progress-check_20260515T044209_result.json`
- **Structured JSON:** [`193b4118d2eb9cd717bb.json`](../../sessions/19/193b4118d2eb9cd717bb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All registry entries updated. Here's the summary:

---

## Object Eval Progress (bjb1-32546, 2026-05-15 ~13:00 UTC)

### 1. eval-reconvla-object (cuda:0, pid=9659)
- **Status**: RUNNING (uptime 2h04m, GPU 22%)
- **Tasks**: 1/10 — currently on task 2
- **Results**: alphabet_soup = 0.0% (0/10)
- **Running avg**: 0.0% (0/10)

### 2. eval-acr-object-v4-perdof (cuda:1, pid=11116)
- **Status**: RUNNING (uptime 2h02m, GPU 23%)
- **Tasks**: 1/10
- **Results**: alphabet_soup = 0.0% (0/10)
- **Running avg**: 0.0% (0/10)

### 3. eval-acr-object-v4-obs-only (cuda:2, pid=13806)
- **Status**: RUNNING (uptime 1h48m, GPU 18%)
- **Tasks**: 1/10
- **Results**: alphabet_soup = 0.0% (0/10)
- **Running avg**: 0.0% (0/10)

### 4. eval-acr-object-v4-scalar (cuda:3, pid=14003)
- **Status**: RUNNING (uptime 1h48m, GPU 23%)
- **Tasks**: 1/10
- **Results**: alphabet_soup = 0.0% (0/10)
- **Running avg**: 0.0% (0/10)

### 5. eval-vla-only-object (cuda:4, pid=17222) — COMPLETED
- **Status**: **DONE** — process exited cleanly, results saved to `logs/eval_object_vla_only.json`
- **Tasks**: 10/10
- **Overall SR**: **12.0% (12/100)**
- **Per-task breakdown**:

| Task | SR |
|---|---|
| alphabet_soup | 0% (0/10) |
| cream_cheese | 10% (1/10) |
| salad_dressing | 20% (2/10) |
| bbq_sauce | 20% (2/10) |
| ketchup | 0% (0/10) |
| tomato_sauce | 10% (1/10) |
| butter | 0% (0/10) |
| milk | 10% (1/10) |
| chocolate_pudding | 20% (2/10) |
| orange_juice | 30% (3/10) |

> Previous "pending escalation retry" concern was unfounded — it completed successfully. No restart needed. cuda:4 is now free.

### 6. eval-vla-mean-object (cuda:5, pid=18808)
- **Status**: RUNNING (uptime 1h41m, GPU 21%)
- **Tasks**: 1/10
- **Results**: alphabet_soup = 0.0% (0/10)
- **Running avg**: 0.0% (0/10)

---

**Summary**: 5/6 experiments running normally with ~20% GPU utilization, all on task 1-2 of 10. With K=10, each task takes ~2h (vs ~10min for K=1), so expect completion in ~18-20h. eval-vla-only-object finished with 12.0% overall SR — this is the K=1 single-sample baseline for the object benchmark.

---
