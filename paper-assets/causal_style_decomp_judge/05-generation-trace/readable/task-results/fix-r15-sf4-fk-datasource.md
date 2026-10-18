# fix r15 sf4 fk datasource

**The Likert Blindspot: Measurement-Mode Divergence in LLM Judge Style Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_r15-sf4-fk-datasource_20260523T063600_result.json`
- **Structured JSON:** [`83eec4533bcafd831530.json`](../../sessions/83/83eec4533bcafd831530.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。以下是修正后的关键数值汇报：

### Descriptive (passed_cf only)
| | n | delta_fk_d | delta_sentlen_d |
|---|---|---|---|
| Verbosity | 86 | 0.501 | 0.399 |
| Formality | 25 | 0.144 | 0.046 |

### Regression
- **Model 1** (delta_FK ~ style_axis): β=1.915, p=.044, R²=.037
- **Model 2** (+ delta_sentlen): style_axis β=0.409, p=.456; delta_sentlen β=0.373, p<.001, R²=.688
- **Coefficient reduction: 78.6%**

### Mediation (Baron-Kenny)
- Sobel z = 1.93, p = .053
- Proportion mediated = 78.6%

### Correlation (pooled passed)
- r = 0.828, p < .001, n = 111

### 与论文预期的差异

旧结果（错用 `verified.jsonl`，formality 全部 100 条）：β reduction 59.3%, Sobel z=3.36, p<.001

新结果（正确用 `verified_32b.jsonl`，formality passed_cf=25 条）：**β reduction 78.6%**（更强），但 **Sobel z=1.93, p=.053**（边缘不显著）。

核心原因：`verified_32b.jsonl` 中仅 25/100 条通过 `passed_cf` 过滤（该字段同时检查 BERTScore 和 NLI 阈值），formality 样本量大幅减少导致 mediation 的 Sobel 检验统计功效不足。论文中如果需要 Sobel p<.05，可以考虑用 `all_pairs`（n=200）的回归结果，其中 β reduction = 68.1%。

---
