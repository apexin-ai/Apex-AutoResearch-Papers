# code r1 8b layer supplement

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_r1_8b_layer_supplement_20260517T084838_result.json`
- **Structured JSON:** [`fa7296c315ccbdbc3c72.json`](../../sessions/fa/fa7296c315ccbdbc3c72.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Complete. Summary:

**R1-8B Full Layer Sweep (layers 0-24)**:
- Extracted early layers 0-11 for all 268 traces (249 new + 19 already cached)
- Best layer: **Layer 12** (38.7% depth), bal_acc = 0.7871
- Layer 14 (old best): bal_acc = 0.7830 (difference: +0.004, negligible)
- Best early layer: **Layer 3** (9.7% depth), bal_acc = 0.7841 (#2 overall, but no clear advantage)
- **No early layer beats the middle-layer range** for R1-8B
- R1-8B differs qualitatively from the 32B models (R1-32B, QwQ, OT-7B), which all peak at layers 0-2. The 8B model peaks at ~39-45% depth instead.
- Existing layer 14 selection remains valid. No registry update needed.

Report saved to `artifacts/r1_8b_layer_supplement/report.md` and registered as `art_20260517_eabada`.

---
