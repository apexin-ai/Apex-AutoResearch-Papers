# ops check 009e status

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check-009e-status_20260515T100311_result.json`
- **Structured JSON:** [`5e16ad0854cb170135fb.json`](../../sessions/5e/5e16ad0854cb170135fb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇总如下：

## 009e 状态

**进程存活**：PID 119108，运行 4h02m，736% CPU，当前 step ≈ 80K / 105K（~76% 完成），预计还需 ~1.5h。

**Eval 轨迹**：

| step | eval_return | value_mean | v/e ratio |
|------|------------|------------|-----------|
| 5K   | 31.0       | 0.0        | 0.000     |
| 15K  | 153.7      | 3.4        | 0.022     |
| 25K  | 167.2      | 25.9       | 0.155     |
| 35K  | 146.3      | 60.2       | 0.411     |
| 45K  | 140.8      | 97.5       | 0.693     |
| **55K** | **82.7** | **137.9**  | **1.666** |
| 65K  | 250.0      | 173.8      | 0.695     |
| 75K  | 178.1      | 189.9      | 1.066     |

**Collapse 分析**：经典 value overestimation 模式正在复现。25K→55K 期间 eval 从 167→83 持续下降，而 value_mean 从 26→138 持续膨胀，v/e ratio 在 55K 飙到 1.666。65K 出现一次 eval 反弹到 250（可能是随机波动），但 75K 又回落到 178 且 v/e 回到 1.066。value_mean 仍在单调上升（174→190），和 008d 的 collapse pattern 一致。

**结论**：009e **正在复现 008d 的 collapse**。value 持续膨胀超过 actual return，eval 整体震荡下降。

---

## 009d (baseline) 状态

当前 step=65K，eval_return=615.9，value_mean=346.7。

Baseline 轨迹：5K→32, 15K→207, 25K→395, 35K→388, 45K→514, 55K→626, 65K→616。

**Baseline 健康**，eval 稳步上升到 600+ 区间，没有 collapse 迹象。v/e ratio 约 0.56，value 远未 overestimate。

---
