# ops gpu patrol and deploy all servers

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_gpu-patrol-and-deploy-all-servers_20260518T054827_result.json`
- **Structured JSON:** [`1341d301382ae4bf7745.json`](../../sessions/13/1341d301382ae4bf7745.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## GPU Patrol Report — 2026-05-18 13:48 UTC

### bjb2-28827 (6 GPUs) — **0 free**

| GPU | Mem | Experiment |
|-----|-----|-----------|
| 0 | 4232 MiB | obs_only norm01 seed42 |
| 1 | 4268 MiB | random_selection seed43 |
| 2 | 5201 MiB | **obs_only K=5 seed43** |
| 3 | 4268 MiB | perdof norm01 seed42 |
| 4 | 4700 MiB | random_selection seed44 |
| 5 | 3804 MiB | perdof norm02 seed48 |

### bjb1-32546 (6 GPUs) — **0 free**

| GPU | Mem | Experiment |
|-----|-----|-----------|
| 0 | 4269 MiB | obs_only norm005 seed45 |
| 1 | 3805 MiB | obs_only norm005 seed44 |
| 2 | 3805 MiB | perdof norm005 seed44 |
| 3 | 3805 MiB | obs_only norm01 seed46 |
| 4 | 2876 MiB | perdof norm02 seed43 |
| 5 | 4269 MiB | perdof norm01 seed43 |

### bjb1-18228 (4 GPUs) — **0 free**

| GPU | Mem | Experiment |
|-----|-----|-----------|
| 0 | 5200 MiB | obs_only norm02 seed48 |
| 1 | 3342 MiB | **obs_only norm01 seed48** (Priority 3) |
| 2 | 3804 MiB | **obs_only norm03 seed48** (Priority 2) |
| 3 | 2875 MiB | perdof norm02 seed45 |

### bjb2-40593 (1 GPU) — **0 free**

| GPU | Mem | Experiment |
|-----|-----|-----------|
| 0 | 2338 MiB | random_selection seed42 |

---

### Deployment: nothing to deploy — all 17 GPUs occupied.

### Already-running overlap with your priority list:
- **Priority 2** (obs_only norm03 seed48) — already running on bjb1-18228 GPU 2
- **Priority 3** (obs_only norm01 seed48) — already running on bjb1-18228 GPU 1

### Pending when GPUs free up (in priority order):
1. **K=5 seed44** — highest priority, not running anywhere
2. obs_only norm02 seed43 — retry (Priority 4)
3. perdof norm03 seed44 (Priority 5)

---
