# check 50k snapshot bjb1 45299

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_50k_snapshot_bjb1_45299_20260520T045315_result.json`
- **Structured JSON:** [`662eeae7c8083117b754.json`](../../sessions/66/662eeae7c8083117b754.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据齐全，汇总如下。

---

## 训练进度快照 (bjb1-45299)

### 进程状态
| 实验 | PID | GPU | 当前步数 | 目标 | 状态 |
|------|-----|-----|---------|------|------|
| exp_027_tcn_walker_s0 | 879360 | cuda:0 | **80K** | 105K | **运行中** |
| exp_028_rave_walker_s0 | 879641 | cuda:1 | **76K** | 105K | **运行中** |

无 loss NaN，无异常。

---

### exp_027_tcn_walker_s0 (TCN, sigma=0.5)

**eval_return 时间序列：**

| Step | eval_return | vs baseline (450-514) |
|------|------------|----------------------|
| 5K   | 37.4       | — |
| 15K  | 154.6      | — |
| 25K  | 223.6      | — |
| 35K  | **240.0**  | — |
| 45K  | 101.2      | 远低于 |
| 55K  | 70.0       | 远低于 |
| 65K  | 95.1       | 远低于 |
| 75K  | 189.2      | 远低于 |

**ve_ratio (NVE) 时间序列：**

| Step | ve_ratio | value_mean | CIVO alert |
|------|----------|------------|------------|
| 15K  | 0.020    | 3.08       | No |
| 25K  | 0.110    | 24.68      | No |
| 35K  | 0.235    | 56.36      | No |
| 45K  | 0.860    | 87.00      | No |
| 55K  | **1.679** | 117.46    | **Yes** |
| 65K  | **1.544** | 146.81    | No |
| 75K  | **0.831** | 157.26    | No |

**train_return @80K**: 38-152（波动大）

**判读**：NVE 在 55K 突破 1.5× 阈值（CIVO 发作），65K 仍在边界（1.54），但 **75K 已回落至 0.83 — CIVO 被抑制**。eval_return 从 35K 峰值 240 暴跌后在 75K 反弹至 189。Gate 锁定在 dt=2（entropy=0，无变化）。

---

### exp_028_rave_walker_s0 (RAVE, ceiling=2.0)

**eval_return 时间序列：**

| Step | eval_return | vs baseline (450-514) |
|------|------------|----------------------|
| 5K   | 37.4       | — |
| 15K  | 105.3      | — |
| 25K  | 191.9      | — |
| 35K  | **204.6**  | — |
| 45K  | 197.7      | 远低于 |
| 55K  | 193.0      | 远低于 |
| 65K  | 79.8       | 远低于 |
| 75K  | **44.5**   | 远低于 |

**ve_ratio (NVE) 时间序列：**

| Step | ve_ratio | value_mean | CIVO alert |
|------|----------|------------|------------|
| 15K  | 0.028    | 2.93       | No |
| 25K  | 0.127    | 24.40      | No |
| 35K  | 0.267    | 54.64      | No |
| 45K  | 0.439    | 86.80      | No |
| 55K  | 0.620    | 119.63     | **Yes** |
| 65K  | **1.832** | 146.10    | **Yes** |
| 75K  | **3.415** | 152.12    | **Yes** |

**train_return @76K**: 38-105（波动大）

**判读**：NVE 单调递增，55K 起持续报警，75K 已飙到 3.42 — **CIVO 完全失控，RAVE ceiling=2.0 未能抑制**。eval_return 从 35K 峰值 205 持续崩溃至 75K 仅剩 44.5。

---

### 关键对比

| 指标 | exp_027 (TCN) | exp_028 (RAVE) |
|------|--------------|----------------|
| NVE @75K | **0.83** (抑制成功) | **3.42** (完全失控) |
| eval_return @75K | 189 (反弹中) | 45 (崩溃中) |
| CIVO 状态 | 55K 发作 → 75K 恢复 | 55K 起持续恶化 |
| Gate | dt=2 锁死 | dt=2 锁死 |
| 两者 vs baseline@50K | 远低于 450-514 | 远低于 450-514 |

**结论**：TCN (sigma=0.5) 显示 CIVO 抑制信号（NVE 回落 < 1.5×），eval 有反弹趋势；RAVE (ceiling=2.0) 完全无效，NVE 持续爆表。但两者绝对 eval_return 都远低于 baseline。

---
