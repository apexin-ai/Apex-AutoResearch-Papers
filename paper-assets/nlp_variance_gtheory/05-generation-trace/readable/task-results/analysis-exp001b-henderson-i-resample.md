# analysis exp001b henderson i resample

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp001b_henderson_i_resample_20260522T121910_result.json`
- **Structured JSON:** [`253e3cfeaea9c38cbccc.json`](../../sessions/25/253e3cfeaea9c38cbccc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果

| Sample | item_id% (Henderson I) | total_variance |
|--------|----------------------|----------------|
| sample1 | **73.18%** | 0.2021 |
| sample2 | **72.57%** | 0.2363 |
| sample3 | **69.00%** | 0.2163 |
| **Mean** | **71.59%** | — |
| **CV** | **3.15%** | — |

**与主分析对比**: 主分析 6-facet Henderson I = 58.39%，resampling 均值 = 71.59%，差距 ~13pp。

**关键发现**: Henderson I 和之前的 η² 分析结果完全一致。原因是 exp-001b 数据为完全平衡交叉设计（3×6×6×4×200 = 86,400），在这种设计下两种方法数学等价。

与 58.39% 参考值的差距并非方法差异导致，而是 **facet 数量不同**：
- 主分析有 6 facets（含 precision=3 levels），precision:item_id 交互占 ~6%，precision 主效应 ~1.7%，这些吸收了总方差的一部分
- exp-001b 只有 1 个 precision（bfloat16），缺失的 precision 方差被重新分配到 item_id 和残差中

如果需要真正可比的 6-facet resampling 数据，需要对 exp-001b 的 3 个 sample 补跑 float16 和 float32 条件。

---
