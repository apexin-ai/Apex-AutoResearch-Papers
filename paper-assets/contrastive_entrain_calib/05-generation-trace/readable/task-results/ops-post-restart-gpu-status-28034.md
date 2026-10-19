# ops post restart gpu status 28034

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_post-restart-gpu-status-28034_20260519T124556_result.json`
- **Structured JSON:** [`7e396a00fd9da64c7781.json`](../../sessions/7e/7e396a00fd9da64c7781.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 状态报告 — westd-28034 (4× RTX 5090 32GB)

**服务重启后所有进程均正常存活，无异常。**

### GPU 占用

| GPU | 显存占用 | GPU利用率 | 进程 |
|-----|---------|-----------|------|
| 0 | 21.8G / 32.6G | 41% | exp-004 (PID 18204) |
| 1 | 31.4G / 32.6G | 62% | exp-008v3 rank0 (PID 104503) |
| 2 | 30.7G / 32.6G | 63% | exp-008v3 rank1 (PID 104504) |
| 3 | 16.5G / 32.6G | 63% | exp-016 re-eval (PID 126897) |

### 各实验状态

**exp-004 (ACT baseline, GPU 0)**
- 运行中，已运行 20h51m，CPU 93.8%
- 当前 step 7930/8000，预计 ~12 分钟后完成
- 每步约 105s，loss 已收敛（sft≈0, total≈0.0001）

**exp-008v3 (Binary Probe GRPO, GPU 1+2)**
- 运行中，两个 rank 均存活（运行 6h05m）
- 当前 step 1091/8000 (14%)，每步约 19s
- reward/combined_mean 在 0.25~0.74 之间波动，r2 持续为 0

**exp-016 re-eval (GPU 3)**
- 运行中（运行 2h13m），CPU 400%
- 已完成 alpha=0.00 和 alpha=0.50，当前正在跑 alpha=1.00（进度 60/362）
- 还剩 alpha=1.00（剩余 300 条）、alpha=2.00、alpha=5.00 三组
- 结果目录已创建但尚无输出文件，预计还需 ~2-3 小时完成全部 5 个 alpha

### 无异常进程

所有 contrastive_entrain_calib 相关进程均为已知实验，无意外占用。

---
