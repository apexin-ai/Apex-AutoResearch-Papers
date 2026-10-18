# fix r15 sf4 fk nli filter

**The Likert Blindspot: Measurement-Mode Divergence in LLM Judge Style Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_r15-sf4-fk-nli-filter_20260523T064539_result.json`
- **Structured JSON:** [`05d7ca97987c7ed07cad.json`](../../sessions/05/05d7ca97987c7ed07cad.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

修复完成。以下是 NLI-only 门控 (nli_cf >= 0.90) 的完整数值：

## Descriptive

| | verbosity (n=86) | formality (n=88) |
|---|---|---|
| delta_fk_d | 0.501 | -0.120 |
| delta_sentlen_d | 0.399 | -0.042 |

## Regression

**Model 1** (delta_FK ~ style_axis):
- style_axis: β=2.688, SE=0.615, p=2.16e-05, R²=0.100

**Model 2** (delta_FK ~ style_axis + delta_sentlen):
- style_axis: β=1.066, SE=0.456, p=0.0204
- delta_sentlen: β=0.387, SE=0.030, p=3.12e-27
- R²=0.546

**Coefficient reduction**: 60.3%

## Mediation (Baron-Kenny)

- Sobel z=3.595, p=0.000324
- Proportion mediated: 60.3%

## Correlation (delta_sentlen vs delta_fk)

- verbosity: r=0.850, p=4.05e-25
- formality: r=0.432, p=2.58e-05
- pooled: r=0.729, p=3.78e-30

关键变化 vs 旧版 (passed_cf 门控)：formality 从 n=25 升至 n=88；Sobel 检验从边缘不显著 (p=0.053) 变为高度显著 (p=0.0003)；coefficient reduction 从 79% 降至 60%，但 mediation 现在有统计支持。

---
