# analysis epsilon sensitivity

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_epsilon-sensitivity_20260522T032625_result.json`
- **Structured JSON:** [`0a6fe085d063321c849e.json`](../../sessions/0a/0a6fe085d063321c849e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果清晰，核心结论：

**arc_challenge×sycophancy（关键条件）：K_eff p=0.003 完全稳定。**

| ε | p(K_eff) | p(η_max) |
|---|----------|----------|
| 0.0001 | 0.0031 ** | 0.0010 ** |
| 0.001 | 0.0030 ** | 0.0009 *** |
| 0.01 | 0.0030 ** | 0.0006 *** |
| 0.1 | 0.0041 ** | 0.0005 *** |

- **K_eff**: p 在 [0.003, 0.004] 范围，4 个 ε 全部 p<0.01，**不是 ε 伪影**
- **η_max**: p 在 [0.0005, 0.001]，更稳定
- β 幅度随 ε 变化（log 变换的正常缩放效应），但显著性方向一致

**唯一不稳定的条件**：arc_challenge×score_manipulation 的 η_max，在 ε=0.1 时 p 从 0.03 漂移到 0.075 跨过 0.05 阈值。其余 11/12 个 predictor×condition 组合全部稳定。

结果已保存到 `epsilon_sensitivity.json`。

---
