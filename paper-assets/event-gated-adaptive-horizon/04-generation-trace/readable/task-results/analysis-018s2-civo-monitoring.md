# analysis 018s2 civo monitoring

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_018s2-civo-monitoring_20260516T220305_result.json`
- **Structured JSON:** [`a19137769252e0805aac.json`](../../sessions/a1/a19137769252e0805aac.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据全了。以下是完整汇报：

---

## exp_018_full_sgs_s2 监控报告

**状态**: 进程存活 (PID 612876, 已运行 2h17m)  
**当前 step**: 85,000 / 105,000 (81% 完成)  
**Checkpoints**: checkpoint_25000.pt, checkpoint_75000.pt, latest.pt

---

### 指标时间线

| Step | eval_return | value_mean | NVE (V/E) | actor_entropy | actor_loss | 判断 |
|------|-------------|------------|-----------|---------------|------------|------|
| 5K   | 39.3        | 0.001      | ~0.00     | 8.25          | -0.123     | 初始化 |
| 15K  | 185.3       | 4.4        | 0.02      | 0.39          | -0.320     | 正常学习 |
| 25K  | 184.1       | 28.1       | 0.15      | -2.62         | —          | 正常 |
| 35K  | 154.6       | 57.3       | 0.37      | -2.62         | -0.136     | 正常 |
| 45K  | **28.6**    | 88.3       | **3.09**  | -2.71         | -0.080     | eval 异常低 |
| 55K  | 197.9       | 120.7      | 0.61      | -3.15         | -0.058     | eval 恢复 |
| 65K  | 98.0        | **152.9**  | **1.56**  | -4.03         | -0.023     | value peak |
| 75K  | 97.3        | 119.5      | 1.23      | -4.48         | +0.023     | value 回落中 |
| 85K  | **128.1**   | 92.1       | **0.72**  | -4.62         | +0.011     | value 已修正 |

---

### 诊断判断

**不符合 Pathway A collapse 模式。**

1. **NVE 已自修正**: 从 65K 的 1.56× 峰值降至 85K 的 0.72×（value 已低于 eval），value 过高估计只是暂态。之前背景描述的"NVE 2.8×"可能计算方式不同或指 45K 那个异常点（3.09×）。

2. **eval 有明确反弹**: 75K→85K 从 97.3 升至 128.1 (+31.7%)。这与 Pathway A 的"eval 单调下降"模式矛盾。

3. **entropy 仍在下降但速率趋缓**: 75K→85K 仅降 0.14（-4.48→-4.62），vs 55K→65K 降 0.87。正在收敛到稳态，不是 freefall。

4. **value_mean 从 152.9 peak 连续两个 eval 周期下降**（152.9→119.5→92.1），Full-SGS 的价值修正机制在起作用。

5. **45K eval=28.6 是异常值**（train_return 同期 ~35-40，下一个 eval 就恢复到 197），不代表系统性崩溃。

### 结论

**Full-SGS 正在按预期阻止 CIVO。** value 过估计在 65K 达到峰值后自行修正。当前 NVE<1 说明 value 甚至在保守估计。eval 在反弹。继续让其跑完 105K 即可，无需干预。

---
