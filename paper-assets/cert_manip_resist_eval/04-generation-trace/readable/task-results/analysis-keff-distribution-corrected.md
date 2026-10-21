# analysis keff distribution corrected

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_keff-distribution-corrected_20260523T143348_result.json`
- **Structured JSON:** [`8f7cf2c349d5ebf6820a.json`](../../sessions/8f/8f7cf2c349d5ebf6820a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已写入 `docs/paper/data/keff_distribution_corrected.json`。

验证结果：
- K=5 range **[2.16, 4.30]** — 与 scatter plot worker 验证值完全一致
- 使用了正确公式 `K_eff = K - (1/K) Σᵢ Σⱼ≠ᵢ ρᵢⱼ²`，ρ 由 MI 通过 Gaussian copula 转换（`exp(-2·MI) = 1-ρ²`），每个 panel 的 K_eff 取 mmlu 和 arc_challenge 的均值
- 旧文件 K=5 range 是 [1.43, 3.55]（错误 Kish 公式），修正后所有 K 值的 K_eff 分布均上移

---
