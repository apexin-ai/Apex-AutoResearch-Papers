# monitor kl v2 progress check

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_kl_v2_progress_check_20260515T153211_result.json`
- **Structured JSON:** [`40ea4f3c475302f4c4ff.json`](../../sessions/40/40ea4f3c475302f4c4ff.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## KL v2 训练状态摘要

### 进程状态
两个进程均存活，已运行约 13 分 26 秒。

### GPU 使用
| GPU | 利用率 | 显存占用 |
|-----|--------|----------|
| cuda:0 (s42) | 100% | 67,569 / 97,887 MiB |
| cuda:1 (s123) | 100% | 67,569 / 97,887 MiB |

### 训练进度

| 指标 | s42 (seed=42) | s123 (seed=123) |
|------|---------------|-----------------|
| **当前步数** | 360 / 1000 (36%) | 360 / 1000 (36%) |
| **KL loss** | 0.2988 | 0.2910 |
| **KL loss 趋势** | 0.365→0.266 (下降中) | 0.334→0.260 (下降中) |
| **Sparsity** | 0.484 | 0.488 |
| **Lambda** | 1000.00 (已到 cap) | 1000.00 (已到 cap) |
| **Tau** | 0.676 | 0.676 |
| **Constraint** | 基本为 0（偶尔 0.012） | 基本为 0（偶尔 0.012） |

### 预估完成时间
13.4 分钟跑了 360 步 → 约 2.23 秒/步 → 剩余 640 步约需 **24 分钟**。

### 异常检查
- 无 NaN、无 OOM、无 warning
- KL loss 稳步下降，两个 seed 趋势一致
- Sparsity 在 0.477–0.506 范围波动，接近 0.5 目标，constraint penalty 几乎为 0，说明约束满足良好
- Lambda 已到 1000 cap，符合预期

**结论：两个实验运行正常，预计约 24 分钟后完成。**

---
