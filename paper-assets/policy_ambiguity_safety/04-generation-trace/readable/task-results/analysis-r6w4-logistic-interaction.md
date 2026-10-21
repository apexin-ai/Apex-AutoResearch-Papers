# analysis r6w4 logistic interaction

**Policy Ambiguity Is Nocuous: Clause-Level Causal Effects on Customer-Service Agent Safety** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_r6w4_logistic_interaction_20260521T152933_result.json`
- **Structured JSON:** [`424ad3ace1824b351e4f.json`](../../sessions/42/424ad3ace1824b351e4f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。结果摘要：

**Interaction test (C4)**: LR χ²(20) = 47.20, p = 0.00055 — 与 ANOVA (F(20)=1.97, p=0.006) **结论一致**，且 logistic regression 的 p 值更小，interaction 效应更显著。

**Main effects**: model χ²(4)=24.83, p<0.0001; type χ²(5)=28.45, p<0.0001，两个主效应都高度显著。

**Top-3 interaction terms** 都涉及 gpt-5.4，其在 incompleteness / conditional_precedence / coreferential 类型上的违规率相对 authorization_scope 基线显著偏低（coef ≈ -2.6 ~ -2.8, z ≈ -3.9 ~ -4.0）。

输出文件：
- `round6_supplementary/logistic_interaction_results.json`
- `round6_supplementary/compute_logistic_interaction.py`

---
