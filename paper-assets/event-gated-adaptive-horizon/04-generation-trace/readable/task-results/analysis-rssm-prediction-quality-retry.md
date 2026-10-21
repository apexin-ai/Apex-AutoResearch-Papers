# analysis rssm prediction quality retry

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_rssm-prediction-quality-retry_20260514T110446_result.json`
- **Structured JSON:** [`c4dcb33eb8193c46f3a8.json`](../../sessions/c4/c4dcb33eb8193c46f3a8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 分析结果

上一个 Worker 的脚本已经跑完，结果如下：

| Model | dt1 obs_mse | dt2 obs_mse | obs gap | dt1 reward_mae | dt2 reward_mae | reward gap |
|-------|------------|------------|---------|---------------|---------------|------------|
| **baseline** | 13.49 | 27.50 | **2.04x** | 0.0102 | 0.0159 | 1.56x |
| **008d** (dt_emb, collapsed) | 41.31 | 53.67 | **1.30x** | 0.0568 | 0.1579 | **2.78x** |
| **008f** (no dt_emb, stable) | 8.01 | 22.04 | **2.75x** | 0.7469 | 0.7526 | 1.01x |

### 关键发现

1. **所有模型 dt>1 预测质量都下降**，支持 delusional critic 假说——world model 在多步 transition 上不准确，critic 信任这些不准的想象轨迹会导致 value overestimation。

2. **exp_008d 的 dt_embedding 是把双刃剑**：
   - obs 预测相对差距最小（1.30x vs baseline 2.04x），说明 dt_emb 确实帮助 RSSM 学习了 dt=2 的 observation dynamics
   - 但**绝对预测质量最差**（dt1 obs_mse=41.31，是 baseline 的 3x）
   - **reward 预测在 dt=2 时崩溃**（2.78x gap），这是三个模型中最大的 reward gap

3. **collapse 的根因更可能是 reward prediction**：008d 的 obs gap 虽小，但 reward gap 巨大（2.78x）。critic 基于严重偏差的 reward 预测做 value estimation → value overestimation → 策略 collapse。

4. **008f 没有 dt_emb，reward gap 几乎为 0**（1.01x），但 reward_mae 本身很高（~0.75），说明 reward model 整体欠拟合但至少在 dt 间一致，不会产生 systematic bias。

### 对假说的判断

**"trained dt_emb causes delusional critic because RSSM dt=2 predictions are less accurate"** — **部分支持，但机制更具体**：不是 obs 预测不准（dt_emb 反而改善了 obs gap），而是 **dt_emb 导致 reward prediction 在 dt=2 时严重恶化（2.78x gap）**，这才是 critic 被误导的直接原因。

---
