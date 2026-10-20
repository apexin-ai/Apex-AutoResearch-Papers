# check hopper gpu1 utilization

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_hopper-gpu1-utilization_20260527T031107_result.json`
- **Structured JSON:** [`be94b36a86a41f8ed6c5.json`](../../sessions/be/be94b36a86a41f8ed6c5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果

**GPU 状态 (cuda:1):**
- GPU util: 11%, 内存 3274MiB / 97887MiB
- GPU 0 (其他实验): 86%, 58540MiB

**判断：正常。** 原因：
- step 8K，dataset_size 仅 4000，train_episodes 仅 8 — 仍在 replay buffer 填充阶段，大部分时间花在环境交互（CPU-bound），不在 GPU 训练
- step 从 5000 → 8000 在正常增长，进程活跃
- 内存 3.2GB 对 DreamerV3 模型本身是合理的（模型不大，batch 数据少）
- 随着 dataset 增大、训练频率提高，GPU util 会逐步上升

**两个实验对比：**

| 指标 | trained_s0 (cuda:1) | baseline (cuda:0) |
|------|---------------------|-------------------|
| 当前 step | 8000 | 8000 |
| dataset_size | 4000 | 4000 |
| train_return | 0.28 | 0.28 |
| train_episodes | 8 | 8 |

两个实验进度完全一致，速率相同。gate 当前全部选择 dt=2（gate_dt_2_frac=1.0），尚未开始分化。

---
