# ops eval check and sweep start

**action cond info bottleneck** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_eval-check-and-sweep-start_20260517T013752_result.json`
- **Structured JSON:** [`e384e041697b6050fe4a.json`](../../sessions/e3/e384e041697b6050fe4a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果汇总

### 1. GPU 状态：占用中
- GPU 0: PID 104743 (seed1 eval), 5846 MiB, 运行 8h16m
- GPU 1: PID 111920 (seed2 eval), 6020 MiB, 运行 8h12m

**Alpha sweep 无法启动。**

### 2. Eval 结果（3/4 suites 完成）

| Suite | seed1 | seed2 | Baseline | seed1 delta | seed2 delta |
|-------|-------|-------|----------|-------------|-------------|
| libero_spatial | 58.4% | 51.4% | 66.0% | -7.6pp | -14.6pp |
| libero_object | 58.6% | 49.4% | 67.8% | -9.2pp | -18.4pp |
| libero_goal | 72.8% | 63.0% | 76.4% | -3.6pp | -13.4pp |
| libero_10 | **运行中** | **运行中** | 54.2% | — | — |
| **AVG (3 suites)** | **63.3%** | **54.6%** | **70.1%** | **-6.8pp** | **-15.5pp** |

### 3. libero_10 进度
- **seed1**: 正在跑 rollout（19%, 100/520 steps），running SR = 0.0%（刚开始一个 episode）
- **seed2**: 80% 完成（40/50 batches），running SR = 30.0%

### 4. ETA
- seed2 libero_10: ~4 min 剩余（10 batches × 26s/it）
- seed1 libero_10: 50 episodes × ~26s/ep，当前可能还在早期 task，估计还需 30-60 min

### 关键发现
v7_contrastive 两个 seed 均**低于 baseline**，seed2 尤其差（-15.5pp avg）。seed1 稍好但仍然全面低于 baseline。这表明 ACIB v7 contrastive 训练可能存在问题，alpha sweep 诊断仍然很有必要。seed2 eval 即将结束，seed1 eval 预计 30-60 min 后完成，之后 GPU 空闲可启动 alpha sweep。

---
