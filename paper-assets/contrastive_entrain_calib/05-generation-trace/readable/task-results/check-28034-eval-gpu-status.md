# check 28034 eval gpu status

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_28034-eval-gpu-status_20260520T022027_result.json`
- **Structured JSON:** [`1fafdb2a70783147494d.json`](../../sessions/1f/1fafdb2a70783147494d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇总

### 1. exp-008v3 Eval 结果

| 指标 | ckpt-500 | ckpt-1000 |
|------|----------|-----------|
| **ToF** | 0.0000 | 0.0055 |
| **NoF** | 0.9945 | 0.9945 |
| **SYCONScore** | 0.0000 | 0.0110 |
| 样本数 | 362 (181+181) | 362 (181+181) |
| 耗时 | 6502s | 6726s |

两个 checkpoint 的 sycophancy 指标都极低——模型几乎不会被 pressure 翻转立场（NoF ≈ 99.5%），ckpt-1000 仅比 ckpt-500 微弱上升（ToF 0.55%, SYCONScore 1.1%）。

### 2. GPU 状态（4× RTX 5090 32GB）

| GPU | 显存占用 | 利用率 |
|-----|---------|--------|
| GPU 0 | 31376 / 32607 MiB (96%) | 46% |
| GPU 1 | 5 / 32607 MiB (空闲) | 0% |
| GPU 2 | 5 / 32607 MiB (空闲) | 0% |
| GPU 3 | 30614 / 32607 MiB (94%) | 74% |

GPU 0 + GPU 3 被 exp-002v3 训练占用，GPU 1 + GPU 2 空闲。

### 3. exp-002v3 训练进度

- **PID 154537** 存活，已运行 **7h49m**
- 当前 step: **2013 / 8000**（25%），速度 ~10s/step
- 已保存 checkpoints: 500, 1000, 1500, 2000
- reward/combined_mean 在 0.49–0.67 之间波动，r2_mean 持续为 0，r3_mean ≈ 1.0
- 预计剩余 ~16h35m

**r2_mean 一直为 0 值得关注**——如果这是一个有意义的 reward 分量，可能存在问题。

---
