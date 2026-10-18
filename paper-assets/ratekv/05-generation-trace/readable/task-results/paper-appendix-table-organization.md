# paper appendix table organization

**When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_appendix_table_organization_20260516T092253_result.json`
- **Structured JSON:** [`0aa4be09963266b2072b.json`](../../sessions/0a/0aa4be09963266b2072b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

添加了两个表格：

1. **Table `\ref{tab:compounding_sweep}`**（第 13–35 行）— Compounding sweep 全量数据，3 个模型 × 9 个 k 值，含 PPL 和相对 baseline 倍数。数据源：`generate_compounding_curves.py`，与论文 Figure 3 一致。

2. **Table `\ref{tab:cross_dataset}`**（第 119–143 行）— Cross-dataset stability 表，上半部分是 Qwen 的交叉校准 PPL（WT2↔C4），下半部分是三个模型的 bit-assignment agreement（均 >96%）。数据源：论文正文 §Cross-Dataset Stability。

3. **Runtime**：已有 `\ref{tab:runtime}`，未改动。

---
