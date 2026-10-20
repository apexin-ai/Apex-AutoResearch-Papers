# monitor check 008 status

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_check_008_status_20260514T040637_result.json`
- **Structured JSON:** [`0539cf315cdb39bae55b.json`](../../sessions/05/0539cf315cdb39bae55b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

008a 的 65K eval 仍在进行中。汇总如下：

---

## 实验状态报告 (2026-05-14)

### 1. exp_008a — No Subsample, dt=2, H=15 | PID 106942 ✅ ALIVE (2h29m)

| Step | eval_return | value_mean | value/eval | actor_loss |
|------|------------|------------|------------|------------|
| 35K  | 500.84     | —          | —          | —          |
| 45K  | 563.41     | 131.95     | 23.4%      | -0.151     |
| 55K  | 487.92     | 183.54     | **37.6%**  | -0.102     |
| **65K** | **eval 进行中** | — | — | — |

- **当前 step**: 65K（eval episodes 正在跑，尚未写入结果）
- **趋势**: 501→563→488，55K 出现回落但未崩（006 同期已跌至 360）
- **value/eval ratio**: 23.4%→37.6%，持续上升但尚未破 40%
- **actor_loss**: -0.151→-0.102，向零趋近（策略改进信号减弱）
- **model_loss**: 4.11→3.99，稳定下降
- **⏳ 65K 决策点**: 数据未出，需等 eval 完成（估计 5-10 分钟）

### 2. exp_008c — No Subsample, dt=2, H=8 | PID 107021 ✅ ALIVE (2h29m)

| Step | eval_return | value_mean | value/eval | actor_loss |
|------|------------|------------|------------|------------|
| 35K  | 185.10     | —          | —          | —          |
| 45K  | 226.55     | —          | —          | —          |
| 55K  | 241.87     | 70.32      | 29.1%      | -0.082     |
| **65K** | **240.86** | **78.96**  | **32.8%**  | **-0.053** |

- **当前 step**: ~68K（train 数据已到 68K）
- **趋势**: 185→227→242→**241**，完全停滞在 ~241
- **value/eval ratio**: 29.1%→32.8%，健康范围
- **actor_loss**: -0.082→-0.053，继续弱化
- **诊断**: 没有崩塌，但性能天花板极低（baseline 55K=625.7，差距 -61%）。H=8 × dt=2 = 16 物理步覆盖不足以学到 walker_walk 所需的长时序行为。

### 3. exp_008d — Subsample ON, H=8 | PID 109519 ✅ ALIVE (1h45m)

| Step | eval_return | value_mean | value/eval | actor_loss |
|------|------------|------------|------------|------------|
| 25K  | 167.22     | 25.86      | 15.5%      | -0.195     |
| **35K** | **146.34** | **60.20**  | **41.1%** ⚠️ | -0.170   |

- **当前 step**: ~40K（train 数据到 40K，eval @45K 未到达）
- **趋势**: 167→**146**，eval 在下降
- **value/eval ratio**: 15.5%→**41.1%**，已突破 40% 警戒线
- **train_return @40K**: 96~134，也在下降
- **model_loss**: 5.33→5.07
- **⚠️ 45K 决策点**: 尚未到达（还需 ~30 分钟）。但 35K 数据已呈现预期的坏信号：eval 下跌 + value/eval > 40%。如果 45K 继续恶化（eval < 140 或 value/eval > 50%），符合预测的崩塌前兆。

---

### 关键判断

| 实验 | 状态 | 决策 |
|------|------|------|
| **008a** | ⏳ 等 65K eval | 55K 的 37.6% ratio 尚可。如果 65K eval ≥ 450 且 ratio < 45% → 继续；否则需要讨论 |
| **008c** | 📊 平台期 | 确认 H=8 + dt=2 性能天花板 ~241，作为对照数据点已足够 |
| **008d** | ⚠️ 早期崩塌信号 | eval 下跌 + ratio 41.1%，与预测一致（subsample 混合训练 → 崩塌）。等 45K 确认 |

---
