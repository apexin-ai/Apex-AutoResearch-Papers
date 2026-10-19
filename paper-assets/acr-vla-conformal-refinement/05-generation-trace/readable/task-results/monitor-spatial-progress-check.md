# monitor spatial progress check

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_spatial-progress-check_20260515T044157_result.json`
- **Structured JSON:** [`72872d317b3974ec5d2f.json`](../../sessions/72/72872d317b3974ec5d2f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry updated. Here's the summary:

---

### Spatial Eval Progress Report (2026-05-15)

**1. eval-argmin-only-spatial** (cuda:1, PID 231421) — `reconvla` mode
- **Status**: ALIVE, uptime 10h54m, **9/10 tasks done**, task 10 in progress
- Per-task SR:

| Task | SR |
|---|---|
| between_plate_and_ramekin | 60.0% (6/10) |
| next_to_ramekin | **100.0%** (10/10) |
| from_table_center | 0.0% (0/10) |
| on_cookie_box | 30.0% (3/10) |
| in_top_drawer | 10.0% (1/10) |
| on_ramekin | 10.0% (1/10) |
| next_to_cookie_box | 90.0% (9/10) |
| on_stove | 0.0% (0/10) |
| next_to_plate | 30.0% (3/10) |

- **Running avg (9 tasks): 36.7% (33/90)** — slightly down from last check (37.5%)
- **Closest to completion** — should finish within ~1h

---

**2. eval-acr-spatial-v4-small** (cuda:3, PID 253085) — `acr_vla` perdof, norm=0.1
- **Status**: ALIVE, uptime 8h12m, **7/10 tasks done**, task 8 in progress
- Per-task SR: between=60%, next_ramekin=**100%**, table_center=10%, cookie_box=40%, top_drawer=0%, on_ramekin=0%, next_cookie_box=90%
- **Running avg (7 tasks): 42.9% (30/70)** — stable vs last check (42.0%)

---

**3. eval-acr-spatial-v4-obs-only-r2** (cuda:0, PID 270097) — `crm_obs_only`, norm=0.1
- **Status**: ALIVE, uptime 6h21m, **6/10 tasks done**, task 7 in progress
- Per-task SR: between=**90%**, next_ramekin=**100%**, table_center=0%, cookie_box=40%, top_drawer=10%, on_ramekin=0%
- **Running avg (6 tasks): 40.0% (24/60)** — down from last check (48.0%)

---

**4. eval-acr-spatial-v4-scalar** (cuda:2, PID 288939) — `crm_scalar`, norm=0.1
- **Status**: ALIVE, uptime 3h07m, **3/10 tasks done**, task 4 in progress
- Per-task SR: between=60%, next_ramekin=**100%**, table_center=10%
- **Running avg (3 tasks): 56.7% (17/30)** — early estimate, down from 80% (was only 2 tasks)

---

### Key observations
- **argmin-only-spatial is 1 task from completion** — final task running now. At 36.7% it's tracking below the VLA mean baseline (~40%), suggesting argmin selection itself may be slightly problematic.
- **obs-only-r2 stands out** on task 1 (between_plate_and_ramekin) with 90% vs 60% for the other three methods.
- All four methods share the same pattern: next_to_ramekin = 100%, from_table_center ≈ 0-10%. The hard tasks (top_drawer, on_ramekin, on_stove) are universally low.
- scalar's early 56.7% will likely regress as it hits the harder tasks.

---
