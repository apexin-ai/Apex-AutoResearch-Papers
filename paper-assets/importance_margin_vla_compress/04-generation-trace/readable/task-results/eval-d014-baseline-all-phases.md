# eval d014 baseline all phases

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_d014-baseline-all-phases_20260515T210325_result.json`
- **Structured JSON:** [`a5fd5788d1b905f68342.json`](../../sessions/a5/a5fd5788d1b905f68342.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Phase 2-3-4 全部完成。以下是完整报告。

---

## D014 Gate Report

### Phase 2: Baseline Final Eval (step_029999, 500 batches)

| 指标 | 值 |
|------|------|
| action_loss (clean, eps=0.0, prune=False) | **0.004077** |
| margin_median (clean) | **0.010022** |
| preservation_rate (eps=0.01) | 0.3352 |
| preservation_rate (eps=0.02) | 0.3362 |
| preservation_rate (eps=0.05) | 0.3381 |
| LED median (eps=0.02) | 0.0 (baseline 无 IMM，LED 恒为 0) |

### Phase 3: Mid-Checkpoint Evals (50 batches)

| Checkpoint | action_loss (clean) | margin_median (clean) |
|-----------|--------------------|-----------------------|
| step_005000 | **0.018910** | 0.010016 |
| step_010000 | **0.009740** | 0.010016 |
| step_029999 | **0.004077** | 0.010022 |

训练曲线正常：action_loss 随步数单调下降 (0.0189 → 0.0097 → 0.0041)。

### Phase 4: Gate Results (Baseline vs IMM)

| Gate | 指标 | 值 | 阈值 | 结果 |
|------|------|------|------|------|
| **G1** | margin_median ratio (IMM/BL) | **55.15** | ≥ 2.0 | **PASS** |
| **G2** | preservation_rate diff | **0.4427** (+44.3pp) | ≥ 0.10 | **PASS** |
| **G3** | clean action_loss ratio (IMM/BL) | **3.2813** (BL=0.00408, IMM=0.01338) | ≤ 1.10 | **FAIL** |
| **G4** | LED ratio median | **0.2726** | < 1.0 | **PASS** |

### Overall Verdict: **FAIL**

G3 未通过：IMM 的 clean action_loss (0.01338) 是 baseline (0.00408) 的 3.28 倍，远超 1.10 上限。G1/G2/G4 均大幅通过阈值。

---
