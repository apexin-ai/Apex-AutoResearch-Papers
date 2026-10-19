# infra check eval progress

**action cond info bottleneck** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_check-eval-progress_20260515T210822_result.json`
- **Structured JSON:** [`363e496ea0faba1124cd.json`](../../sessions/36/363e496ea0faba1124cd.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 状态汇报

### 1. baseline_std_v3 (smolvla_libero) — GPU 1, PID 109428
**状态：Running**，已运行 1h30m

当前 suite：`libero_spatial`（第 1/4 个），已完成 8/10 个 task：

| Task # | Success Rate | 耗时 |
|--------|-------------|------|
| 0 | 82% | 7:42 |
| 1 | 74% | 10:58 |
| 2 | 88% | 9:23 |
| 3 | 86% | 8:00 |
| 4 | 52% | 13:01 |
| 5 | 0% | 16:26 |
| 6 | 90% | 9:11 |
| 7 | 66% | 12:29 |

### 2. baseline_plus_v2 (smolvla_libero_plus) — GPU 0, PID 109501
**状态：Running**，已运行 1h30m

当前 suite：`libero_spatial`（第 1/4 个），已完成 8/10 个 task：

| Task # | Success Rate | 耗时 |
|--------|-------------|------|
| 0 | 98% | 6:34 |
| 1 | 82% | 10:41 |
| 2 | 92% | 8:48 |
| 3 | 94% | 7:54 |
| 4 | 74% | 11:36 |
| 5 | 32% | 14:39 |
| 6 | 94% | 9:45 |
| 7 | 86% | 10:45 |

### 3. GPU 使用
- GPU 0: RTX PRO 6000 (98GB)，2.2GB / 97.9GB，1% util
- GPU 1: RTX PRO 6000 (98GB)，2.2GB / 97.9GB，1% util

GPU 利用率很低，主要瓶颈在 CPU 端的 env stepping。

### 4. 进度预估
- 每个 task 平均约 10-11 分钟
- 每个 eval 剩余：2 tasks（libero_spatial）+ 30 tasks（3 suites × 10 tasks）= 32 tasks
- **预估剩余时间：约 5.5-6 小时**（两个并行跑，同时完成）

### 5. 初步对比
在 `libero_spatial` 已完成的 8 个 task 上，**plus 模型明显优于 std**：
- plus 平均 success rate：~81.5%
- std 平均 success rate：~67.3%
- 最大差距在 task 5（plus 32% vs std 0%）和 task 0（plus 98% vs std 82%）

---
