# analysis exp hopper frozen s0

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp_hopper_frozen_s0_20260527T085204_result.json`
- **Structured JSON:** [`d389f7c6e1543046d691.json`](../../sessions/d3/d389f7c6e1543046d691.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。

## exp_hopper_frozen_s0 结论：**NEGATIVE（假设被拒绝）**

### 核心发现

| 指标 | baseline (无gate) | trained_s0 | **frozen_s0** |
|------|-------------------|-----------|---------------|
| eval_return_final | 96.43 | 3.26 (→81.58@168K) | **0.0** |
| ve_ratio_peak | 3.48@65K | — | **4,335,664@105K** |
| CIVO alerts | 0 | 0 | **2** (65K, 105K) |

### 关键机制

Frozen dt_emb 产生了三个配置中**最差**的结果：
1. **完全学习失败**：eval_return 全程接近 0（peak 仅 3.6@85K，baseline 为 96.43）
2. **极端 value-reality 脱节**：value_mean 从 0.04 单调增长至 4.34，但实际回报为 0
3. **value-target 内部一致**：NVE(value vs target) < 0.06 — value 网络精确拟合自己的 bootstrap target，但二者共同虚高
4. **策略熵坍缩**：actor_entropy 从 5.5 → -1.6，策略变得确定性但完全无效

**"trained dt_emb 是 CIVO 的必要条件"** 这一假设被拒绝。Frozen dt_emb 不仅没阻止 CIVO，反而因丧失时间适应能力导致世界模型学到自洽但与现实完全脱节的 imaginary dynamics。

---
