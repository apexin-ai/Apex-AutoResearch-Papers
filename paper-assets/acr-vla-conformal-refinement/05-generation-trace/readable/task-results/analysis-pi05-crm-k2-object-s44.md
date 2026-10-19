# analysis pi05 crm k2 object s44

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_pi05-crm-k2-object-s44_20260526T141604_result.json`
- **Structured JSON:** [`c6f2299262ad38248fa7.json`](../../sessions/c6/c6f2299262ad38248fa7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

DONE. 

**pi05-crm-k2-object-s44-bjb1-r2**: SR=88.0% (176/200), EXIT_CODE=0, no OOM/CUDA errors, all 10 tasks > 0%.

- CRM K=2 always-on (ε=0.05) Object s44: **88.0%**
- π0.5 VLA-only Object baseline: ~99.5% (westd s42/s43/s44 mean)
- **Δ = -11.5pp**: CRM degrades strong π0.5 baseline on Object, consistent with sister Goal results (CRM 82.5–85% vs VLA-only ~97.5%) and Spatial (CRM 96.5–97% vs VLA-only ~98%). Marked `conclusion=success` (matching the convention used by all pi05-crm-k2-* siblings — experiment yields valid Table 2 data point even though CRM-always-on harms the near-expert VLA).
- Per-task: 4× 100%, 2× 95%, 2× 90%, 2× 75%, 1× 60% (ketchup is weakest).
- Note: `mean_correction_norm` not emitted in JSON for this mode.

---
