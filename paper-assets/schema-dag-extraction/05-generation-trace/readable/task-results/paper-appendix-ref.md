# paper appendix ref 

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_appendix_ref____20260522T015924_result.json`
- **Structured JSON:** [`c2cd7b3b1161a9a852b0.json`](../../sessions/c2/c2cd7b3b1161a9a852b0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All 11 edits are in place. Here's the summary:

### 修改摘要

**main.tex（appendix 部分）：**

| Label | 行号 | 修改内容 |
|-------|------|----------|
| `tab:partial_corr` | 328 | 段首加 `As Table~\ref{tab:partial_corr} shows,` |
| `tab:error_examples` | 792 | 句末加 `Table~\ref{tab:error_examples} provides illustrative confusion instances with SCS values.` |
| `tab:prompt_variants` | 376 | 句末加 `(Table~\ref{tab:prompt_variants})` |
| `tab:variance_decomposition` | 666 | 段首加 `Table~\ref{tab:variance_decomposition} shows that` |
| `tab:bcs_aggregation` | 404 | 句末加 `(Table~\ref{tab:bcs_aggregation})` |
| `tab:format_independence` | 453 | 句末加 `(Table~\ref{tab:format_independence})` |
| `tab:scs_baselines` | 604 | 新增一句 `Table~\ref{tab:scs_baselines} compares SCS against simple baselines for pairwise confusion prediction.`（该 section 原本无正文） |
| `tab:relaxed_matching` | 883 | 句末加 `; Table~\ref{tab:relaxed_matching}` |
| `tab:fewshot_bcs` | 767 | 句末加 `(Table~\ref{tab:fewshot_bcs})` |
| `tab:renaming` | 861 | 句末加 `(Table~\ref{tab:renaming})` |

**results.tex：**

| Label | 行号 | 修改内容 |
|-------|------|----------|
| `tab:partial_corr` | 47 | `(Appendix~\ref{sec:appendix_partial_corr})` → `(Appendix~\ref{sec:appendix_partial_corr}, Table~\ref{tab:partial_corr})` |

**跳过的 labels：**
- `sec:conclusion`, `sec:metrics`, `sec:results` — 主文 section 标签，需从其他主文 section 引用，不改主文
- `sec:appendix_figures`, `sec:appendix_batch_composition`, `sec:appendix_prompt_sensitivity`, `sec:appendix_cross_model_70b`, `sec:appendix_type_defs` — appendix section 标签，通常从主文引用，appendix 内无自然引用位置
- `app:bcs-composition`, `app:cross-domain` — 同上，appendix 内无自然交叉引用位置

---
