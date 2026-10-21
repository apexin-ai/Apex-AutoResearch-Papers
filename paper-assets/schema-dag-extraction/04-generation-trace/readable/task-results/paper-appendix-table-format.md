# paper appendix table format

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_appendix_table_format_20260522T024349_result.json`
- **Structured JSON:** [`e793903eb860893cc263.json`](../../sessions/e7/e793903eb860893cc263.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

No `\hline` anywhere. Here's the modification summary:

---

## 修改摘要

### 1. Caption 位置（29 个表格全部修改）

所有 29 个 appendix 表格的 `\caption` + `\label` 从 `\end{tabular}` 之后移到 `\begin{tabular}`（或 `\resizebox`）之前。涉及表格：

`tab:cross_model`, `tab:cross_model_bcs`, `tab:cross_model_ner_null`, `tab:error_taxonomy`, `tab:cross_model_error_taxonomy`, `tab:sdgd_results`, `tab:routing_strategies`, `tab:tost_sensitivity`, `tab:residualized_bcs`, `tab:partial_corr`, `tab:batch_composition`, `tab:prompt_variants`, `tab:bcs_aggregation`, `tab:bcs_controlled`, `tab:format_independence`, `tab:format_perbatch`, `tab:within_pool`, `tab:scs-ablation`, `tab:scs_baselines`, `tab:variance_decomposition`, `tab:cross_model_70b`, `tab:cross_model_gemini`, `tab:cross_model_bcs_summary`, `tab:fewshot_bcs`, `tab:top10_re`, `tab:top10_ner`, `tab:error_examples`, `tab:renaming`, `tab:relaxed_matching`

### 2. 列对齐修正（3 个表格）

| 表格 | 修改前 | 修改后 | 原因 |
|------|--------|--------|------|
| `tab:top10_re` | `{clllr}` | `{cllrr}` | SCS 列是数字，应右对齐 |
| `tab:top10_ner` | `{clllr}` | `{cllrr}` | 同上 |
| `tab:prompt_variants` | `{llrrrr}` (6 spec / 5 col) | `{lrrrr}` (5 spec / 5 col) | 列定义数与实际列数不匹配 |

### 3. 数字格式修正（1 个表格）

| 表格 | 位置 | 修改前 | 修改后 | 原因 |
|------|------|--------|--------|------|
| `tab:error_examples` | SCS 列 | `.97`, `.92`, `.90` | `0.97`, `0.92`, `0.90` | 其他所有表格的 SCS 值均使用 `0.xx` 格式 |

### 4. Booktabs 样式

已检查，所有 29 个表格均使用 `\toprule` / `\midrule` / `\bottomrule`，无 `\hline`。无需修改。

### 5. 数字精度

已检查所有表格内同列数字小数位数。除 `tab:error_examples` 的 SCS 前导零（已修复）外，各表内数字精度一致，无需修改。

---
