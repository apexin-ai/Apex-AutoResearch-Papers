# code phi3v r2 action probe

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_phi3v_r2_action_probe_20260520T012645_result.json`
- **Structured JSON:** [`be95155a09bb6d25187f.json`](../../sessions/be/be95155a09bb6d25187f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Extraction is actively running — first task `open_the_middle_drawer_of_the_cabinet.h5.tmp` is being written (269MB so far). GPU utilization is low because the forward passes are quick (single frame at a time with idle periods for data loading).

**Summary:**

- **Script**: `/root/vla-ssd/scripts/phi3v_r2_action_probe.py` — two-phase design:
  - Phase 1: Extract last-preaction hidden states (33 layers × 3072 dims) from TracVLA-Phi3V for all 10 tasks × 50 demos → saved to `/root/autodl-tmp/vla-ssd/features/phi3v_trained_libero_goal/`
  - Phase 2: Train per-layer MLP probes (5 seeds), compute R² → output to `/root/autodl-tmp/vla-ssd/results/functional_validation/phi3v_r2_action_probe.json`
- **Job**: Running on westd-19183 cuda:0, PID 402232
- **Registry**: `phi3v_r2_action_probe` → RUNNING
- **Log**: `/root/autodl-tmp/vla-ssd/logs/phi3v_r2_action_probe.log`
- **Estimated time**: Phase 1 (extraction) ~30-60 min for 10 tasks, Phase 2 (probing) ~15 min

---
