# check exp004 status gpu

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_exp004-status-gpu_20260513T105145_result.json`
- **Structured JSON:** [`1cc42f1aba2076e4377f.json`](../../sessions/1c/1cc42f1aba2076e4377f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 报告

### 1. GPU 利用率

| GPU | 型号 | GPU-Util | 显存占用 | 进程 |
|-----|------|----------|----------|------|
| 0 | RTX PRO 6000 Blackwell | **0%** | 4165 / 97887 MiB | python (PID 9409) |
| 1 | RTX PRO 6000 Blackwell | **22%** | 4173 / 97887 MiB | python (PID 36645) |

### 2. exp_004 (event_gated_v4_s1)

最新 eval（step 15000）：
- **eval_return**: 153.86
- **gate_scale**: 0.0
- **gate_dt_mean**: 1.0（gate 始终选择 dt=1，未激活）
- **gate_empirical_entropy**: 0.0
- **fps**: 8.1

最新 train（step 20000）：train_return 101~203，正在推进。

### 3. baseline (baseline_s1)

- **step**: 245000（刚开始该 step，尚无 eval）
- **train_return** @ 244000: 935~976

### 4. 异常分析

**GPU 0 利用率 0% 需关注。** 有 python 进程占用 4.1GB 显存但 GPU-Util 为 0%，可能处于环境交互/数据收集阶段（Dreamer 训练中正常的间歇性空闲），也可能进程挂起。GPU 1 的 22% 对 Dreamer 类算法属于正常偏低范围（环境交互和世界模型训练交替进行）。

**exp_004 gate 未激活是关键问题：** gate_scale=0.0 + gate_dt_mean=1.0 + gate_entropy=0.0 说明 gate 模块完全未参与决策，所有步都用 dt=1。如果 gate 按设计应在训练中逐步激活（warmup schedule），需要确认 warmup 结束的 step 是多少；如果已过 warmup 仍为 0，则 gate 配置可能有问题。

**baseline 远领先 exp_004**（245k vs 20k steps），两者不在同一训练阶段，无法直接对比 return。

---
