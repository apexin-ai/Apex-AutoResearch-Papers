# analysis nli selection bias

**The Likert Blindspot: Measurement-Mode Divergence in LLM Judge Style Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_nli-selection-bias_20260522T200539_result.json`
- **Structured JSON:** [`1f70192286a648d6c2fc.json`](../../sessions/1f/1f70192286a648d6c2fc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果

### 字段列表
`instruction, response, source, label, id, original_text, counterfactual_text, double_rewrite_text, original_formality, bertscore_cf, bertscore_dr, nli_cf, nli_dr, passed_cf, passed_dr`

**无 `instruction_type` 或 `category` 字段**，改用 `source`、`original_formality`、`label` 做 selection bias 分析。

### NLI Selection Bias 分析（N=100）

**NLI_CF ≥ 0.90 划分**（Pass=88, Reject=12）：

| 维度 | χ² | p-value | 结论 |
|------|-----|---------|------|
| source | 1.30 | 0.730 | 不显著 |
| original_formality | 0.79 | 0.374 | 不显著 |
| label | 0.00 | 1.000 | 不显著 |

**NLI_DR ≥ 0.90 划分**（Pass=81, Reject=19）：

| 维度 | χ² | p-value | 结论 |
|------|-----|---------|------|
| source | 1.28 | 0.733 | 不显著 |
| original_formality | 0.79 | 0.375 | 不显著 |
| label | 0.29 | 0.591 | 不显著 |

**Combined Pass (passed_cf AND passed_dr)**（Pass=15, Reject=85）：

| 维度 | χ² | p-value | 结论 |
|------|-----|---------|------|
| source | 1.01 | 0.798 | 不显著 |
| original_formality | 3.64 | **0.056** | 边缘不显著 |

唯一接近显著的是 combined pass 下的 formality 分布（p=0.056）：通过样本中 casual 占 66.7%，而拒绝组中只占 36.5%——casual 文本更容易同时通过 CF 和 DR 验证。但在 0.05 水平下仍不显著。

结果已保存到 `artifacts/r13_fixes/nli_selection_bias.json`。

---
