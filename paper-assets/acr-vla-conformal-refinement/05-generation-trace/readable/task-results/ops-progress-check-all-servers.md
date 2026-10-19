# ops progress check all servers

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_progress-check-all-servers_20260515T170904_result.json`
- **Structured JSON:** [`1c0d6d15090ab67e7caa.json`](../../sessions/1c/1c0d6d15090ab67e7caa.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All 10 registry entries updated. Here's the consolidated view:

---

## Progress Dashboard (2026-05-16 01:00 UTC)

### Seed=43 Six-Way (Object) — all 6 running, 0 complete

| Method | Server | Tasks | Status |
|--------|--------|-------|--------|
| crm_obs_only (norm=0.1) | bjb1-18228 | **4**/10 | T1:0 T2:10 T3:10 T4:30 |
| crm_perdof (norm=0.1) | bjb1-18228 | **2**/10 | T1:0 T2:0, T3 in-progress |
| reconvla | bjb1-18228 | **4**/10 | T1:0 T2:0 T3:20 T4:20 |
| crm_scalar (norm=0.1) | bjb1-32546 | **0**/10 | T1 at rollout 5/10 |
| vla_only (K=1) | bjb1-32546 | **2**/10 | T1:0 T2:10 |
| vla_mean (K=10) | bjb1-32546 | **1**/10 | T1:0 |

ETA: ~4-6 hours

### Object Magnitude Sweep

**obs_only:**
| 0.03 | 0.05 | 0.1 | 0.2 | 0.3 |
|------|------|-----|-----|-----|
| 0/10 | 0/10 | **19% DONE** | **9/10** ~21% | 0/10 |

**perdof:**
| 0.03 | 0.05 | 0.1 | 0.2 | 0.3 |
|------|------|-----|-----|-----|
| 0/10 | 0/10 | **11% DONE** | 0/10 | **MISSING** |

### Spatial Supplementary

**Completed:**
- obs_only: norm=0.05 → **35%**, norm=0.2 → **35%**
- perdof: norm=0.03 → **30%**, norm=0.05 → **31%**, norm=0.3 → **26%**

**Near-complete:**
- obs_only norm=0.3 (bjb1-18228): **9/10**, ~40% partial → ~30min
- perdof norm=0.2 (bjb2-28827): **9/10**, ~29% partial → ~30min
- obs_only norm=0.03 (bjb2-40593): **6/10**, ~38% partial → ~4h (slow 4090D)

### Action Items

1. **PID 42311 DEAD** — `eval-acr-object-v4-default` (perdof default-norm on object) died at 3/10 tasks. Needs restart.
2. **perdof object norm=0.3 MISSING** — not submitted anywhere. Gap in the 5-point sweep.
3. Several completed spatial experiments on bjb2-28827 (norm005, norm02, norm003, norm03) may need registry status → DONE.

---
