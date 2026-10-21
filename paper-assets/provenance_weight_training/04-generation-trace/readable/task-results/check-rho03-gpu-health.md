# check rho03 gpu health

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_rho03_gpu_health_20260522T211232_result.json`
- **Structured JSON:** [`8cfcaf726704947afe46.json`](../../sessions/8c/8cfcaf726704947afe46.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 健康检查结果

### PID 存活状态
全部 4 个进程 **存活**：

| PID | 运行时长 |
|-----|---------|
| 805034 | 2h16m16s |
| 805117 | 2h16m14s |
| 805886 | 2h13m51s |
| 805963 | 2h13m48s |

### GPU 利用率与显存

| GPU | 利用率 | 显存占用 |
|-----|--------|---------|
| GPU 0 | 100% | 28697 / 97887 MiB (29.3%) |
| GPU 1 | 96% | 28697 / 97887 MiB (29.3%) |
| GPU 2 | 86% | 28729 / 97887 MiB (29.3%) |
| GPU 3 | 99% | 28729 / 97887 MiB (29.3%) |

### 训练进度

| 实验 | 当前步数 | 进度 | 速度 | 已运行 | 预估剩余 |
|------|---------|------|------|--------|---------|
| rho03_adaptive_seed42 | 3117 / 6103 | **51.1%** | 2.64 s/it | 2h16m | ~2h12m |
| rho03_adaptive_seed123 | 3067 / 6103 | **50.2%** | 2.65 s/it | 2h14m | ~2h14m |
| rho03_uniform_seed42 | 3348 / 6103 | **54.9%** | 2.42 s/it | 2h16m | ~1h51m |
| rho03_uniform_seed123 | 3287 / 6103 | **53.9%** | 2.42 s/it | 2h14m | ~1h53m |

所有实验运行正常。uniform 比 adaptive 快约 8.5%（2.42 vs 2.64 s/it），uniform 两组预计约 ~1h52m 后完成，adaptive 两组预计约 ~2h13m 后完成。

---
