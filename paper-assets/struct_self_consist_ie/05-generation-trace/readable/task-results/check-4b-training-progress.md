# check 4b training progress

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_4b_training_progress_20260515T185830_result.json`
- **Structured JSON:** [`72049d9e7afd96d65327.json`](../../sessions/72/72049d9e7afd96d65327.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 训练状态：正在运行，进度 85%

| 指标 | 值 |
|------|-----|
| **Step** | 3730 / 4390 (84.97%) |
| **Epoch** | 4.25 / 5.0 |
| **Loss** | 0.0093 |
| **LR** | 1.35e-05 |
| **已用时间** | 2h09m |
| **预计剩余** | ~23 min |
| **预计完成** | ~17:42 UTC (约 02:22 UTC+8) |

**进程健康**：
- `llamafactory-cl` 进程存活 (PID 205001)
- GPU 0: 14902 MiB 显存占用，35% 利用率
- 无 OOM，checkpoint 正常保存（已有 checkpoint-2800 ~ 3600，每 200 步一个）
- Loss 已降到 0.009-0.014 区间，收敛良好

---
