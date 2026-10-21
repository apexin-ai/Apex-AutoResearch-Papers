# analysis br bootstrap ci

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_br-bootstrap-ci_20260521T070003_result.json`
- **Structured JSON:** [`f1f4364b76d52cf54e2d.json`](../../sessions/f1/f1f4364b76d52cf54e2d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果：

| Model | BR | 95% CI | n_questions |
|---|---|---|---|
| Mistral-7B | 4.97× | [3.98, 6.37] | 83 |
| Qwen2.5-14B | 3.93× | [2.44, 7.11] | 52 |
| LLaMA-3.1-8B | 3.87× | [3.11, 4.98] | 86 |

数据验证：
- Mistral 和 Qwen 的 BR 点估计与 `crossmodel_results.json` 中的 `raw_bias_ratio` 完全吻合
- 论文提到的 2.88 在数据中未找到。实际值：Mistral=4.97, Qwen=3.93, LLaMA=3.87
- **所有 CI 下界 > 1**，说明三个 generator 的 confirmation bias 均显著
- Qwen CI 最宽 [2.44, 7.11]，因为只有 52 个 SICA-wrong 问题（最强模型，错误最少）
- LLaMA 数据来自 cross-model 实验的 4 条 traces，SICA answer 用约束数量多数决定（非 MaxSAT），86 个问题

已保存到 `artifacts/br_bootstrap_ci.json` 并注册。

---
