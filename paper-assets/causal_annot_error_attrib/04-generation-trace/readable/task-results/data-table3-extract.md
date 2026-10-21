# data table3 extract

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_data_table3_extract_20260520T213524_result.json`
- **Structured JSON:** [`036a943f766b845b2cc0.json`](../../sessions/03/036a943f766b845b2cc0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据已提取并写入 `artifacts/table3_source_data.txt`。

关键发现：JSON 源数据与论文 Table 3 存在显著差异：

- **MC-SIMEX 差异最大**：frontdoor 论文 +8.7% vs 数据 -55.7%（符号翻转），collider 12.4% vs 37.1%（差 25pp），mediation 24.6% vs 42.4%（差 18pp）
- **PPI++ 小幅差异**：confounding 97.8→99.3，collider 98.6→97.0，iv 98.4→99.5
- **Naive/MLA**：论文用 "<0" 模糊处理，实际值为 frontdoor -53.5/-112.5，exposure -45.6/-89.9，iv -40.9/-59.2
- **Grand mean 完全一致**：所有 5 个方法的 grand mean 在论文和数据间精确匹配

Grand mean 匹配但个别值不匹配，可能论文写入时用了不同版本的中间结果或不同的聚合方式。建议用 JSON 源数据更新论文 Table 3。

---
