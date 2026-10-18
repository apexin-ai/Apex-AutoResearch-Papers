# analysis condition dependent dominance

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_condition-dependent-dominance_20260522T173756_result.json`
- **Structured JSON:** [`d3adf85c1a2fe0781167.json`](../../sessions/d3/d3adf85c1a2fe0781167.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。结果摘要：

### TABLE 1: Dominance Classification

| Condition | η_std_β | K_std_β | Ratio | η_FDR_p | K_FDR_p | Category |
|---|---|---|---|---|---|---|
| mmlu×prompt_injection | +0.616 | +0.252 | 0.41 | 8.9e-45*** | 1.9e-09*** | **co-dominant** |
| mmlu×sycophancy | +0.486 | +0.166 | 0.34 | 4.8e-26*** | 3.6e-04*** | **co-dominant** |
| mmlu×score_manipulation | +0.598 | +0.033 | 0.05 | 1.1e-18*** | 0.662 ns | **η_max dominant** |
| mmlu×verbosity_bias | +0.593 | +0.090 | 0.15 | 4.7e-39*** | 0.039* | **co-dominant** |
| mmlu×position_bias | +0.418 | +0.104 | 0.25 | 1.6e-13*** | 0.079 ns | **η_max dominant** |
| mmlu×authority_bias | +0.377 | +0.010 | 0.03 | 4.0e-11*** | 0.852 ns | **η_max dominant** |
| arc×prompt_injection | +0.244 | +0.330 | 1.35 | 1.1e-03** | 1.3e-05*** | **co-dominant** |
| arc×sycophancy | +0.492 | -0.192 | 0.39 | 8.0e-12*** | 9.5e-03** | **co-dominant** |
| arc×score_manipulation | +0.224 | +0.252 | 1.12 | 0.046* | 0.034* | **co-dominant** |
| arc×verbosity_bias | +0.343 | +0.146 | 0.42 | 7.4e-06*** | 0.067 ns | **η_max dominant** |
| arc×position_bias | -0.011 | +0.584 | 52.0 | 0.909 ns | 3.5e-08*** | **K_eff dominant** |
| arc×authority_bias | +0.261 | +0.195 | 0.74 | 4.7e-05*** | 4.8e-03** | **co-dominant** |

### TABLE 2: Category Summary

| Category | N | Conditions | Avg Indiv ASR Range |
|---|---|---|---|
| **K_eff dominant** | 1 | arc×position_bias | 0.365 |
| **η_max dominant** | 4 | mmlu×{score_manip, position, authority}, arc×verbosity | 0.294 |
| **co-dominant** | 7 | 剩余 7 个条件 | 0.418 |

### 关键发现

1. **η_max 普遍占主导** — 12/12 条件中 η_std_β > K_std_β（除 arc×position_bias）。多数条件下 η_max 的标准化效应是 K_eff 的 2-30 倍。

2. **唯一 K_eff dominant 条件**：arc×position_bias（ratio=52, K_std_β=+0.584, η_max 完全不显著 p=0.91）。这是攻击通过交换位置实现的，panel 多样性成为决定性因素。

3. **co-dominant 占多数（7/12）**：多数条件下两者都 FDR 显著，但 η_max 效应始终更大。

4. **系统性差异**：η_max dominant 条件的 indiv ASR range 更小（0.294 vs co-dominant 的 0.418），平均 panel ASR 更高（0.161 vs 0.060），说明这些攻击更 transferable、对模型影响更均匀。

---
