# debug read baseline r2

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_debug_read_baseline_r2_20260517T200401_result.json`
- **Structured JSON:** [`c3af6084d6a18241e82d.json`](../../sessions/c3/c3af6084d6a18241e82d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Got everything needed. The baseline condition from the current run doesn't save per-task R² or bootstrap CI to the log (only the final JSON at the end has that), but I have the summary metrics from the log. Note: the script prints `mean_R2` (mean of per-task R²) which is the key comparable metric.

```
=== 50-demo Baseline Action Probe R² ===
L1:  mean_R2 = 0.5567, overall_R2 = 0.6261 (epochs=50)
L8:  mean_R2 = 0.6199, overall_R2 = 0.6820 (epochs=26)
L13: mean_R2 = 0.6763, overall_R2 = 0.7296 (epochs=15)

(Bootstrap CI not yet available — only saved in final JSON after all conditions complete)

=== vs Control8 (from action_probe_50demos_control8.json) ===
Layer  | baseline | control8 |   Δ    | CI overlap?
-------|----------|----------|--------|------------
L1     |  0.5567  |  0.5732  | -0.0165 | baseline LOWER (within control8 CI [0.5149, 0.6321])
L8     |  0.6199  |  0.6311  | -0.0112 | baseline LOWER (within control8 CI [0.5773, 0.6834])
L13    |  0.6763  |  0.6787  | -0.0024 | essentially identical (within control8 CI [0.6322, 0.7255])
```

**Key finding**: Baseline (no ablation) has *slightly lower* mean_R² than control8 (ablating 8 non-instruction heads) at all layers. The differences are tiny (0.2-1.7%) and well within control8's bootstrap CIs. This is unexpected — ablating random non-instruction heads doesn't hurt (and may slightly help) action probe R².

The ablate_all24 condition is still running. Per-task R² and bootstrap CIs for baseline will be available in the final `action_probe_50demos.json` once all 3 conditions complete.

---
