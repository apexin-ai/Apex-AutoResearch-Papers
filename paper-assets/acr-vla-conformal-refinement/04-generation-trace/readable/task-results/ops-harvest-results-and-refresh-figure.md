# ops harvest results and refresh figure

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_harvest-results-and-refresh-figure_20260518T054842_result.json`
- **Structured JSON:** [`d4aeadfe12f01712491f.json`](../../sessions/d4/d4aeadfe12f01712491f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Done. Here's the summary:

## New Data Points Added (5)

| Method | Norm | Seed | SR | Source |
|--------|------|------|----|--------|
| perdof | 0.2 | 46 | 0.09 | bjb2-28827 |
| perdof | 0.2 | 47 | 0.11 | bjb2-28827 |
| obs_only | default | 46 | 0.15 | bjb1-32546 |
| obs_only | 0.05 | 43 | 0.14 | bjb1-32546 |
| perdof | default | 46 | 0.00 | bjb1-32546 |

Also noted: obs_only norm=0.2 K=5 seed42 = 0.14 on bjb1-18228 (excluded, different K).

## Updated Magnitude Curve Summary

| Method | Norm | Mean SR | Std | n |
|--------|------|---------|-----|---|
| **obs_only** | 0.03 | 16.0% | - | 1 |
| | 0.05 | **13.5%** | 0.71 | **2** |
| | 0.1 | 15.0% | 1.41 | 2 |
| | 0.2 | 17.5% | 2.81 | 6 |
| | 0.3 | 17.0% | 2.16 | 4 |
| | uncapped | **14.8%** | **2.95** | **5** |
| **perdof** | 0.03 | 14.0% | - | 1 |
| | 0.05 | 14.0% | - | 1 |
| | 0.1 | 10.75% | 2.50 | 4 |
| | 0.2 | **9.83%** | **0.98** | **6** |
| | 0.3 | 4.67% | 1.15 | 3 |
| | uncapped | **7.75%** | **5.44** | **4** |

Bold = changed values.

## Registry Fixes (8)

- `eval-openvla-object-vla-only-seed42`: failed → **negative** (completed, SR=0)
- `eval-acr-object-v3`: failed → **negative** (partial, all SR=0)
- `eval-acr-spatial-v3`: failed → **success** (SR=2.5%)
- 5 experiments: failed → **killed** (SIGTERM from errant kill-restart Worker)

## Figure Changes
- Removed stale "0%" annotation (perdof default now 7.75%, not 0%)
- Fixed argmin legend from hardcoded n=3 to n=1
- Added n=X labels for high-seed-count points

---
