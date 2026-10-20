# urgent full system recovery check

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_urgent_full_system_recovery_check_20260521T152259_result.json`
- **Structured JSON:** [`b5dd69c98d33c0472f5b.json`](../../sessions/b5/b5dd69c98d33c0472f5b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

TracVLA Object now has complete trained+untrained data. Key trained vs untrained comparison:

**TracVLA Object — Trained vs Untrained**

| Metric | Trained | Untrained | Delta |
|--------|---------|-----------|-------|
| R² preaction PEAK | 0.764 @ L9 | 0.690 @ L23 | -0.074, peak shifts later |
| R² preaction L31 | **0.470** | **0.681** | +0.211 (no exit collapse in untrained) |
| R² image L31 | 0.748 | 0.736 | -0.012 (similar) |
| L1 instr-dominant | 30/32 | 32/32 | untrained has MORE instr-dom |
| Cross-instr L0 preact | 0.858 | 0.922 | untrained higher |

The critical signal: trained model shows **preaction R² collapse** at exit (L31=0.47), untrained does NOT (L31=0.68). This is the exit routing pattern. Per C001, we now have both arms — this comparison is valid.

Three jobs now active:
- **cuda:0**: `openvla_long_pipeline_v1` (Phase 1, Task 3/10)
- **cuda:1**: `tracvla_spatial_untrained_v1` (just started, ~15 min ETA)

---
