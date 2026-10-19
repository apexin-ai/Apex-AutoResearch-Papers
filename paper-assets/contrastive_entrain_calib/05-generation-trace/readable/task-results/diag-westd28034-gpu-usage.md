# diag westd28034 gpu usage

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_westd28034-gpu-usage_20260518T182438_result.json`
- **Structured JSON:** [`a0b1d007e9dc8937fb47.json`](../../sessions/a0/a0b1d007e9dc8937fb47.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断结果：

## GPU 显存占用

| GPU | 显存占用 | 进程 |
|-----|---------|------|
| **0** | **21,828 MiB / 32,607 MiB** | PID 18204 (exp-004 ACT baseline) |
| **1** | 2 MiB / 32,607 MiB | 空闲 |
| **2** | 2 MiB / 32,607 MiB | 空闲 |
| **3** | 2 MiB / 32,607 MiB | 空闲 |

## 关键发现

1. **exp-004 没有泄漏到 GPU 1**。PID 18204 启动时设置了 `CUDA_VISIBLE_DEVICES=0`，仅占用物理 GPU 0（21.8 GiB），GPU 1/2/3 完全空闲。

2. **之前 exp-014 OOM 的原因不是 exp-004 泄漏**。exp-014 用 `CUDA_VISIBLE_DEVICES=1,2` 启动时，visible GPU 0 = 物理 GPU 1，visible GPU 1 = 物理 GPU 2，两张卡都是空的。OOM 报的 "GPU 0 已满 21.32 GiB" 如果发生在当前状态下，说明是 exp-014 自身在单卡上分配超过 32 GiB 导致的，而非被 exp-004 挤占。

3. **可用于 exp-014 的 GPU 组合**：
   - **GPU 1 + 2**（各 32.6 GiB 空闲）— 满足 ~25.6 GB/卡需求
   - **GPU 2 + 3** 或 **GPU 1 + 3** 也可以
   - 甚至 **GPU 1 + 2 + 3** 三卡都可用

4. 无活跃 tmux 会话。exp-004 通过后台 bash 进程运行，正在正常训练（CPU 101%，GPU-Util 79%）。

**结论**：GPU 1+2 完全空闲，exp-014 可以安全启动。如果之前 OOM，需要检查 exp-014 的 DeepSpeed 配置本身（ZeRO-2 分片是否正确、batch size 是否过大等），而不是 GPU 冲突问题。

---
