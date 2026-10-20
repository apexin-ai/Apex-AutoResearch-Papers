# analysis exp001b resampling investigation

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp001b_resampling_investigation_20260522T121232_result.json`
- **Structured JSON:** [`93a24877d1d5202edf20.json`](../../sessions/93/93a24877d1d5202edf20.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Now I have the full picture. Here's the report.

---

## 调查结果

### 1. JSON 分析设置

`exp001b_resampling_gstudy.json` 是 **5-facet 分析**（bf16 only，无 precision facet）：
- Facets: temperature(3) × prompt_template(6) × seed(6) × ordering(4) × item_id(200)
- 432 conditions/sample, 86,400 records/sample
- 模型: Llama-3.1-8B-Instruct
- 方差估计方法: **SS proportion (η²)**，非 Henderson I

实际数据:
| | Sample 1 | Sample 2 | Sample 3 | Mean | CV |
|---|---|---|---|---|---|
| item_id% | 73.18 | 72.57 | 69.00 | 71.59 | 2.57% (pop σ) / 3.1% (sample σ) |

### 2. 论文数字来源

存在 **两个版本** 的论文 tex：

- **`docs/paper/sections/experiments.tex` (旧)**: 59.8%, 61.4%, 62.1% (CV=2.7%) — 这些数字**不对应任何实际分析结果**
- **`docs/paper/experiments.tex` (新)**: 73.2%, 72.6%, 69.0% (CV=3.1%) — 与 JSON 吻合

旧版 59.8/61.4/62.1% 的成因已在 `mistakes.yaml` M022 中记录：论文混用 η²（SS proportion）和 Henderson I 数字。这三个数字是围绕 6-facet η² 基线（~61%）编造的近似值，**从未实际运行过 6-facet resampling**。

### 3. 正确数字

取决于方法论选择：

| 方法 | 基线 (exp-001) | 说明 |
|---|---|---|
| η² 6-facet | 54.85% | 旧分析，有偏 |
| η² 5-facet | ~73% (exp001b) | JSON 现有数据 |
| Henderson I 6-facet | **58.39%** | unified 统一表 |
| Henderson I 5-facet | **70.94%** | unified 统一表 |

exp001b 的 73.18/72.57/69.00% 是 η² 5-facet。如果论文主体已切换到 Henderson I，resampling 部分理论上也应该用 Henderson I 重算。但 **CV（稳定性）不受方法选择显著影响**——绝对值会略低，稳定性结论不变。

### 4. 建议

**新版 `docs/paper/experiments.tex` 的 73.2/72.6/69.0% 基本正确**，但有两个小问题需确认：

1. **方法一致性**: 如果主表用 Henderson I（item_id=58.4%），resampling 也应重算为 Henderson I。当前 exp001b JSON 用的是 η²。
2. **旧版 `sections/experiments.tex` 的 59.8/61.4/62.1% 必须删除/替换**——这些数字无数据支撑。

---
