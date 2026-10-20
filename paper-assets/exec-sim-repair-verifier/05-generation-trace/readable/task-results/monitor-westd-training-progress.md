# monitor westd training progress

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_westd-training-progress_20260515T033133_result.json`
- **Structured JSON:** [`f8d401c147d454852397.json`](../../sessions/f8/f8d401c147d454852397.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据齐全了，汇总报告如下。

---

## 实验进度汇总 (2026-05-15 11:32 UTC)

### GPU 利用率
| GPU | 利用率 | 显存 | 温度 |
|-----|--------|------|------|
| cuda:0 | 77% | 19.2/32.6 GB | 68°C |
| cuda:1 | 97% | 27.3/32.6 GB | 72°C |
| cuda:2 | 95% | 30.7/32.6 GB | 70°C |
| cuda:3 | 87% | 30.9/32.6 GB | 70°C |

---

### 1. cuda:0 — cls8b-s42-ckpt1400-val8192-eval (PID 321785)
- **进度**: 8960/9335 (96%), running_acc=86.1%
- **速度**: ~6 samples/sec
- **剩余**: ~375 samples ≈ **1 分钟**
- **状态**: ✅ 即将完成

### 2. cuda:1 — repo-level-cls-8b-s42-resume (PID 295794)
- **当前 step**: 2273/6633 (34%), epoch 1.02
- **最新 eval** (step 2200): eval_loss=0.3063, train_loss=0.4066
- **速度**: ~200 steps/41min (含 eval)，checkpoint 间隔 200 步
- **剩余**: 4360 steps ≈ **14.9 小时**
- **ETA**: ~May 16 02:30
- **状态**: ✅ 正常训练中

### 3. cuda:2 — repo-level-cwm-8b-conda (PID 266816)
- **当前 step**: ~3000/6633 (45%), 正在做 eval (5047/9335, 54%)
- **速度**: ~100 steps/40min (含 eval)，checkpoint 间隔 100 步
- **剩余**: 3633 steps ≈ **24.2 小时**
- **ETA**: ~May 16 ~12:00
- **状态**: ✅ 正常训练中（当前在 eval 阶段）

### 4. cuda:3 — repo-level-cls-8b-seed123-conda-v3 (PID 266449)
- **当前 step**: 5814/6633 (88%), epoch 2.62
- **最新 eval** (step 5800): eval_loss=0.2855
- **速度**: ~200 steps/42min (含 eval)，checkpoint 间隔 200 步
- **剩余**: 833 steps ≈ **2.9 小时**
- **ETA**: ~May 15 14:25
- **状态**: ✅ 正常训练中，最快完成

---

**完成顺序预估**: eval(cuda:0, 1分钟) → seed123(cuda:3, ~3h) → cls-s42(cuda:1, ~15h) → cwm(cuda:2, ~24h)

---
