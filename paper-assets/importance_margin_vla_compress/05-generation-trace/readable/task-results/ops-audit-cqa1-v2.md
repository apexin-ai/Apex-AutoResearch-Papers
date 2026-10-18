# ops audit cqa1 v2

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_audit_cqa1_v2_20260522T054027_result.json`
- **Structured JSON:** [`5db030377a6fe0de03e6.json`](../../sessions/5d/5db030377a6fe0de03e6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 审计结果

**服务器 westd-27271 只有 2 张 GPU，不是 4 张。** 用户预期的 4 个实验（random_k0925, random_k09, l2norm_k095, l2norm_k09）在此服务器上不存在——无日志、无进程、无 exit 文件。

### 实际 GPU 状态

| GPU | 实验 | PID | 状态 | 进度 |
|-----|------|-----|------|------|
| cuda:0 | `eval_pi05_random_k095_spatial_seed43` | 9470 | 运行中 | Task 7/10, 累计 79.4% (278/350) |
| cuda:1 | `eval_pi05_l2norm_k085_spatial_seed43` | 9613 | 运行中 | Task 8/10, 累计 87.8% (351/400) |

### 关键发现

- **无空闲 GPU**：2 张卡均被占用且正常运行
- **无崩溃实验**：两个实验都在健康推进
- **实验不匹配**：实际运行的是 random_k095 和 l2norm_k085，不是任务中列出的 4 个实验
- l2norm_k085 进展更快（已到 T8），成功率也更高（87.8% vs 79.4%）

### 行动

无需重启或部署新实验——两张 GPU 均满载运行中。预计两个实验都将在 ~20-30 分钟内完成（各剩 2-3 个 task）。如需部署任务中提到的 l2norm_k07 和 l2norm_k05 实验，需等当前实验完成后再提交。

---
