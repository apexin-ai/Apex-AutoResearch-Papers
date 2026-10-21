# code exp 001a r1 32b

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp_001a_r1_32b_20260516T215732_result.json`
- **Structured JSON:** [`b9897fbc58cb79ce8a76.json`](../../sessions/b9/b9897fbc58cb79ce8a76.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All 5 phases completed successfully. Here's the summary:

## exp_001a Results Summary

**Phase 1**: Extracted 100 R1-32B traces (3,506 steps, 64,727 tokens) into `artifacts/hidden_states_r1_32b/` (2.2GB, 0 errors).

**Phase 2 (Layer Sweep)**: Best layer = 2 (score=7.60). Early layers (0-2) dominate the ranking by the crossing_rate x lead_mean metric, though deeper layers (56-63) have higher raw accuracy (~0.73 vs ~0.62).

**Phase 3 (Temporal LR)**: Window=15 achieves best accuracy (0.70) but shortest lead (7.3 steps). Window=5 preserves longer lead time (10.6 steps) with lower accuracy (0.63).

**Phase 4 (GRU 3-seed)**: 
- Crossing rate: 0.667 +/- 0.085 (better than LR's 0.50-0.55)
- Lead mean: 11.2 +/- 0.76 steps
- Accuracy: 0.595 +/- 0.029

**Phase 5 (Bootstrap)**: No significant difference between temporal LR and GRU pre-CP FPR (p=0.54).

**vs R1-8B**: R1-32B shows lower absolute accuracy but longer lead times and different layer dynamics (early layers dominate vs mid-layers for 8B). The 32B model appears to encode safety-relevant signals earlier in its layer stack.

---
