# check training progress 010b 019a

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_training-progress-010b-019a_20260516T132615_result.json`
- **Structured JSON:** [`ebcdb26d1065ce4ae2ad.json`](../../sessions/eb/ebcdb26d1065ce4ae2ad.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 训练进度汇总

### 进程状态

| 实验 | PID | 状态 | 已运行时间 |
|------|-----|------|-----------|
| 010b (Cheetah CIVO trigger) | 585826 | **ALIVE** | 21 min 28 sec |
| 019a (PickCube baseline) | 586751 | **ALIVE** | 5 min 42 sec |

### GPU 利用率

| GPU | 利用率 | 显存占用 |
|-----|--------|---------|
| 0 | 20% | 3951 / 97887 MiB (4%) |
| 1 | 41% | 4159 / 97887 MiB (4%) |

### 010b — Cheetah CIVO Trigger (目标 105K steps)

- **当前 step**: 16,000 (15.2%)
- **最新 eval_return** (step 15000): **66.55**
- **最新 train_return** (step 16000): 14.5 ~ 44.3 (波动中，均值 ~33)
- **FPS**: 10.6 (step 15000 时测得)
- **gate_dt**: 固定 2.0 (100% dt=2，门控尚未开始探索)
- **预估剩余**: 89000 steps / 10.6 fps ≈ **~2.3 小时**

趋势：eval_return 从 step 5000 的 13.5 涨到 step 15000 的 66.5，学习正常。

### 019a — PickCube Baseline (目标 200K steps)

- **当前 step**: 4,400 (2.2%)
- **最新 eval_return** (step 2500): **1.11**
- **最新 train_return** (step 4400): 2.2
- **FPS**: 估算 ~6.7 (基于 1900 steps / ~282 sec)
- **预估剩余**: 195600 steps / 6.7 fps ≈ **~8.1 小时**

019a 刚启动不久，reward 还在低位探索阶段。

---
