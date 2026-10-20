# paper verify appendix L363 L365

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_verify-appendix-L363-L365_20260519T154004_result.json`
- **Structured JSON:** [`1dba5b59f64a59711356.json`](../../sessions/1d/1dba5b59f64a59711356.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

三行已修正。汇报如下：

## 数据来源确认与修改

| 行 | 指标 | 原值 (N=16) | 新值 (N=8) | 来源确认 |
|---|---|---|---|---|
| L362 | Constant F1 | 61.7% | **未改** | 已是 N=8 三种子均值，正确 |
| L363 | Constant utility | 49% | **66%** | 原值来自 d108 分析的 `CoNLL_NER_N16`（1708/3453=49.5%）。N=8 两种子均值：(65.6%+65.7%)/2≈66% |
| L364 | Oracle gap closed | 41% | **36%** | 原值来自 d108 分析的 `CoNLL_NER_N16`（41.0%）。N=8 两种子均值：(38.4%+33.4%)/2≈36% |
| L365 | Within-inst SJ ρ | 0.994 | **0.985** | 原值来自 d108 分析的 `CoNLL_NER_N16`（median=0.9937）。N=8 两种子均值：(0.981+0.990)/2≈0.985 |

**注意**：CoNLL N=8 的 seed42 数据在旧服务器（autodl-5090）上，已不可用。新值为 seed123 + seed456 的两种子均值，而非与 SciERC 列一致的三种子均值。SciERC 两列和 Constant F1 行使用了包含 seed42 的三种子数据。如需完全一致，需要重跑 seed42 的 CoNLL N=8 实验。

---
