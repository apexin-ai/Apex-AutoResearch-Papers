# analysis magnitude curve data aggregation

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_magnitude-curve-data-aggregation_20260517T235456_result.json`
- **Structured JSON:** [`c8cacaa302924e994789.json`](../../sessions/c8/c8cacaa302924e994789.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Data collected from 67 JSON files across 4 servers, aggregated into `magnitude_curve_data.json` (artifact `art_20260518_8affa6`).

**Key findings for Figure 2:**

| ε | obs_only (mean±std, n) | perdof (mean±std, n) |
|---|---|---|
| 0.03 | 16.0% (n=1) | 14.0% (n=1) |
| 0.05 | 13.0% (n=1) | 14.0% (n=1) |
| 0.1 | 15.0±1.4% (n=2) | 10.8±2.5% (n=4) |
| 0.2 | **17.5±2.8%** (n=6) | 9.8±1.0% (n=4) |
| 0.3 | 17.0±2.2% (n=4) | 4.7±1.2% (n=3) |
| default | 14.8±3.4% (n=4) | 10.3±2.1% (n=3) |

**Baselines:** VLA-only 11.2%, ReconVLA 12.4%, VLA-mean 12.5%

**obs_only** peaks at ε=0.2 (17.5%), significantly above all baselines. Performance degrades slightly at default (uncapped), suggesting moderate capping helps.

**perdof** peaks at ε=0.03–0.05 (14%), degrades sharply at higher magnitudes (4.7% at ε=0.3), indicating per-DOF corrections are too aggressive without tight capping.

**Notes:** ε=0.03 and ε=0.05 have only 1 seed each — these points have no variance estimates. The ε=0.2 obs_only point has the most seeds (6) and is the most reliable.

---
