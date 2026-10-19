# analysis harvest final bc results

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_harvest_final_bc_results_20260522T185033_result.json`
- **Structured JSON:** [`a928925d88f1ec74058d.json`](../../sessions/a9/a928925d88f1ec74058d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Both scripts are **still running**. Here's the situation:

**1. Bootstrap CI (PID 97210)** — started 02:47, 26 min CPU used
- In "Phase 1: Train probes + pre-compute test predictions..." (training 128 probes: 32 layers × 4 windows)
- After Phase 1, Phase 3 (1000 bootstrap iterations) is pure numpy indexing — should be fast
- **Estimate: likely 1-2 hours more total**

**2. Classifier Sensitivity (PID 93351)** — started 02:21, **5h47m CPU** used
- Completed only 1 of 9 metric×threshold combos: `composite: L3 (9.7%) = 0.2991`
- The script has a critical inefficiency: calls `evaluate_layer()` redundantly — 3 metrics × 32 layers × 4 windows = 384 calls per threshold, but only 128 unique (results are metric-independent). Plus `copy.deepcopy(traces)` copies 3.3GB per threshold.
- **At this rate: ~5h47m per metric × 3 metrics × 3 thresholds ≈ 50+ hours total**. Impractical.

The classifier sensitivity script needs to be killed and rewritten to cache `evaluate_layer` results across metrics. Want me to:
1. Kill PID 93351 and deploy an optimized version (should run in ~6 hours instead of 50+)
2. Leave it running and just wait for bootstrap CI

Or I can do both — kill & relaunch optimized sensitivity, and poll bootstrap CI until it finishes.

---
