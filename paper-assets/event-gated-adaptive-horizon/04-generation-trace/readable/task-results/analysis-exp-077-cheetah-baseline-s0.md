# analysis exp 077 cheetah baseline s0

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp_077_cheetah_baseline_s0_20260525T140900_result.json`
- **Structured JSON:** [`da3feae4eb1353cc922b.json`](../../sessions/da/da3feae4eb1353cc922b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Now I have all data. Here's the analysis:

---

## exp_077_cheetah_baseline_s0 结果分析

### 训练状态
**正常完成。** EXIT_CODE=0，训练跑到 112K steps（超过目标 105K），无 error/crash。

### Eval Return 趋势

| Step | Eval Return |
|------|------------|
| 5K | 12.2 |
| 15K | 18.4 |
| 25K | 182.9 |
| 35K | 356.0 |
| 45K | 377.2 |
| 55K | 441.0 |
| 65K | 317.3 |
| 75K | 340.9 |
| 85K | 309.3 |
| 95K | 418.4 |
| **105K** | **448.1** |

最后 3 个 eval 点均值：**~392**。训练 return 在 104K-108K 区间多数在 470-530，偶有低 episode（正常方差）。最终 eval return 448 处于 Cheetah Run baseline 合理范围（300-600）。

### VE Ratio 趋势

| Step | ve_ratio | delta_ve | alert |
|------|----------|----------|-------|
| 15K | 0.143 | 0.0 | 0 |
| 25K | 0.071 | -0.072 | 0 |
| 35K | 0.089 | +0.018 | 0 |
| 45K | 0.174 | +0.085 | 0 |
| 55K | 0.248 | — | 0 |
| 65K | 0.484 | — | 0 |
| 75K | 0.565 | +0.081 | 0 |
| 85K | **0.739** | +0.174 | 0 |
| 95K | 0.605 | -0.134 | 0 |
| **105K** | **0.611** | +0.006 | 0 |

ve_ratio 从早期 ~0.07-0.17 逐步上升到 ~0.6，在 85K 处有一个 peak（0.74）后回落并**稳定在 ~0.61**。这是正常的 value function 校准过程——随着 value 绝对值增大（从 ~3 → ~274），value-error 比例自然上升后收敛。关键指标：
- **alert 全程为 0**（无 CIVO 触发）
- **delta_ve 在 95K-105K 趋近 0**（已收敛）
- **无持续上升的 spike pattern**

### Model Loss
model_loss 从 14.3 (5K) 下降到 1.83 (105K)，持续下降，正常收敛。

### Conclusion: **SUCCESS — 有效 baseline**

- 训练正常完成，无异常
- ve_ratio 在后半程稳定于 ~0.6，无 compounding overestimation
- alert=0 全程，确认无 CIVO 特征
- 最终 eval return 448，作为 dt=1 baseline 表现合理
- **可用于归一化 exp_078 的 VE 值**

### Checkpoint Path
```
/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_077_cheetah_baseline_s0/latest.pt
```

---
