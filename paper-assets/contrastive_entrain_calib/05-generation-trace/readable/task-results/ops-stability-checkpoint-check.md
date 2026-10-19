# ops stability checkpoint check

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_stability-checkpoint-check_20260519T051721_result.json`
- **Structured JSON:** [`cf62d6e3cb5fa72e07cf.json`](../../sessions/cf/cf62d6e3cb5fa72e07cf.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果汇总

| 检查项 | 状态 |
|--------|------|
| `measure_direction_stability.py` 存在 | OK (10480 bytes, May 19 09:47) |
| 语法检查 | OK |
| checkpoint-500 | **不存在** |

**当前训练进度**: step 385/8000, `save_steps=500`

**预计 checkpoint-500 到达时间**: 还需 115 步, 每步约 28.5 秒, 约 **55 分钟后** (约 14:12 UTC)。

训练在 GPU 0 上运行 (63594 MiB), GPU 1 被 exp003 占用。checkpoint-500 保存后即可运行稳定性测量。

---
