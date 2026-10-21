# analysis keff distribution stats

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_keff-distribution-stats_20260523T142835_result.json`
- **Structured JSON:** [`3c3bdc0f0341340326b4.json`](../../sessions/3c/3c3bdc0f0341340326b4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已输出到 `docs/paper/data/keff_distribution.json`。

计算方法：将 mmlu 和 arc_challenge 两个 benchmark 的 15×15 MI 矩阵取平均，然后对每个 K 枚举所有 C(15,K) 个 panel，用 K_eff = K / (1 + (K-1) × mean_pairwise_MI) 计算。

验证全部通过：
- panel 数量：455 / 3003 / 6435 ✓
- K_eff 范围均在 [1, K] 内 ✓
- mean K_eff 随 K 递增（1.92 → 2.32 → 2.54），增速递减 ✓

---
