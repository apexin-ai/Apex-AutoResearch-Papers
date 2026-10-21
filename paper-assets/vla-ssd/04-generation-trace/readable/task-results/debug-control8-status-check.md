# debug control8 status check

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_debug_control8_status_check_20260517T195558_result.json`
- **Structured JSON:** [`6a26b1f5436a607e4787.json`](../../sessions/6a/6a26b1f5436a607e4787.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

```
=== Control8 (cuda:1) Status ===
GPU status: IDLE (0% util, 0 MiB, no process)
Output file: EXISTS (4292 bytes, written 03:33)

Results — ablate_control8 (ablating 8 control heads):
  L1  R²: 0.5732  [95% CI: 0.5149 – 0.6321]  (44 epochs)
  L8  R²: 0.6311  [95% CI: 0.5773 – 0.6834]  (29 epochs)
  L13 R²: 0.6787  [95% CI: 0.6322 – 0.7255]  (15 epochs)

Per-task best (L13): turn_on_stove 0.8145, open_top_drawer 0.7597
Per-task worst (L13): put_wine_bottle_on_rack 0.5636, open_middle_drawer 0.5737

Per-dim R² (L13): [0.738, 0.755, 0.692, 0.605, 0.403, 0.747, 0.738]
  → dim4 consistently worst across all layers (~0.40)

=== Main 50demos (cuda:0) Status ===
GPU status: ACTIVE (84% util, 15812 MiB, PID 905829)
Output file: NOT YET (still running)
```

Control8 实验已完成，registry 需要更新。主实验（cuda:0）仍在运行中。

---
