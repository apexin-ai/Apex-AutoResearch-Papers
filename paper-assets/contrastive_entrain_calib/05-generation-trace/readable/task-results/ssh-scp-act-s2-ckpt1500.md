# ssh scp act s2 ckpt1500

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_scp-act-s2-ckpt1500_20260522T082233_result.json`
- **Structured JSON:** [`d0b4aad01f9edf28454e.json`](../../sessions/d0/d0b4aad01f9edf28454e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果

| 实验 | 当前进度 | 预计剩余 |
|------|---------|---------|
| **exp-004-s2** (ACT seed2) | step 1590 / 8000 (~20%) | ~16h (按 ~9s/step) |
| **exp-003-s2** (R3-only seed2) | step 7003 / 8000 (~88%) | ~7h (按 ~25.7s/step) |

### SCP 传输完成

| Checkpoint | 来源路径 (29046) | 目标路径 (28034) | 状态 |
|-----------|-----------------|-----------------|------|
| exp-004-s2 ckpt-1500 | `outputs/exp-004-act-baseline-s2/checkpoint-1500/` | `exp004_s2/checkpoint-1500/` | OK |
| exp-003-s2 ckpt-7000 | `exp003_r3only_seed2/checkpoint-7000/` | `exp003_s2/checkpoint-7000/` | OK |

28034 上现有 checkpoint：
- **exp004_s2**: 500, 1000, **1500** (新)
- **exp003_s2**: 500–6500, **7000** (新)

---
