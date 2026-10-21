# monitor training progress v2

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_training_progress_v2_20260514T011037_result.json`
- **Structured JSON:** [`b17a18f789fd29f1fafe.json`](../../sessions/b1/b17a18f789fd29f1fafe.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

4 个进程全部存活。

| 实验 | GPU | 进度 | Loss | 速度 | 已运行 | 预计剩余 | 状态 |
|------|-----|------|------|------|--------|----------|------|
| uniform_seed42 | cuda:1 | 3496/6103 (57%) | 7.9435 | 2.12 s/it | 1h47m | ~1h32m | 正常 |
| uniform_seed123 | cuda:2 | 3483/6103 (57%) | 7.7178 | 2.13 s/it | 1h47m | ~1h33m | 正常 |
| uniform_seed456 | cuda:3 | 3487/6103 (57%) | 7.3315 | 2.12 s/it | 1h47m | ~1h33m | 正常 |
| grid_b_seed42_batch | cuda:0 | 2247/6103 (37%) | 10.119 | 2.12 s/it | 1h21m | ~2h16m | 正常 |

**GPU 利用率：**

| GPU | 利用率 | 显存占用 |
|-----|--------|----------|
| 0 (grid_b) | 55% | 46.5/97.9 GB |
| 1 (seed42) | 93% | 44.1/97.9 GB |
| 2 (seed123) | 97% | 44.1/97.9 GB |
| 3 (seed456) | 93% | 44.1/97.9 GB |

3 个 uniform 实验进度一致（~57%），预计约 1.5h 后完成。grid_b_seed42_batch 启动较晚，37% 进度，预计约 2h16m 后完成。GPU 0 利用率偏低（55%），可能是 grid_b 实验当前正在做 checkpoint 保存或 eval；其余 3 卡利用率正常（93-97%）。

---
