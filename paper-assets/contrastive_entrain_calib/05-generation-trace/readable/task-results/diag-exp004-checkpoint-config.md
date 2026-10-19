# diag exp004 checkpoint config

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_exp004-checkpoint-config_20260518T191111_result.json`
- **Structured JSON:** [`ed299aef5a96bde2234b.json`](../../sessions/ed/ed299aef5a96bde2234b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇总结果：

## exp-004 Checkpoint 状态

| 项目 | 值 |
|---|---|
| **save_steps** | 500 |
| **max_steps** | config.json 写的 2（可能是 dry-run 残留），实际在跑 8000 |
| **当前进度** | step 1350 / 8000 |
| **SFT loss** | ~2.2e-05（已完全记忆，符合预期） |

### 已保存的 checkpoint
- `checkpoint-500` ✅
- `checkpoint-1000` ✅

### Director 要求的 checkpoint 覆盖情况

| 要求 step | 状态 |
|---|---|
| 500 | ✅ 已保存 |
| 1000 | ✅ 已保存 |
| 2000 | ⏳ 将在 ~step 2000 自动保存（save_steps=500 整除 2000） |
| 4000 | ⏳ 将自动保存（save_steps=500 整除 4000） |
| 8000 | ⏳ 将自动保存（save_steps=500 整除 8000） |

### 结论

**save_steps=500 无需修改。** 500 能整除 500、1000、2000、4000、8000，所有 Director 要求的 checkpoint 都会被自动保存。额外还会保存 1500、2500、3000、3500、4500、5000、5500、6000、6500、7000、7500 这些中间点（磁盘空间允许的话无害，还能提供更细粒度的分析选项）。

---
