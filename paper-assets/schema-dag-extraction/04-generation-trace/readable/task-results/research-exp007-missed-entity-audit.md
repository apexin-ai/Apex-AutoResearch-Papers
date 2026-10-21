# research exp007 missed entity audit

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_exp007_missed_entity_audit_20260515T175845_result.json`
- **Structured JSON:** [`7e9c7e229a1a5bd3ced7.json`](../../sessions/7e/7e9c7e229a1a5bd3ced7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据溯源完成。以下是结论。

---

## 报告：exp007 NER Missed-Entity Percentage 数据溯源

### 1. Table 3 NER Missed 12%, 14%, 16% — 无数据来源

**这些数字无法从任何已有 artifact 推导出来。**

exp007 `error_taxonomy.py` 脚本只计算了 FP 分类（IntraSub/ExtraSub/Boundary/Halluc/Spurious 占 FP 的比例）和 FN 原始计数。没有任何脚本计算 NER 的 "missed_pct"。

从 raw data 重新计算的实际 NER missed rates（`artifacts/exp007/error_taxonomy_by_bcs.csv` + `predictions_exp1.json`）：

| BCS Bin | FN/total_gold (1-Recall) | Truly Missed (无任何预测覆盖) |
|---------|-------------------------|-------------------------------|
| zero    | 35.9%                   | 33.3%                         |
| low     | 47.6%                   | 42.8%                         |
| medium  | 72.2%                   | 64.8%                         |
| high    | 65.4%                   | 49.9%                         |

无论用哪种 "missed" 定义，实际值都在 **33-72%** 范围内，远非 12-16%，且**不是 flat**。

### 2. 与 Table 3 的一致性

**不一致。** Table 3 声称 NER Missed 为 12%, 14%, 16% 且 "remains flat"。实际数据显示：
- 值域是 33-72%，不是 12-16%
- 趋势不 flat（low→medium 急剧上升）

### 3. RE Missed 的对比

RE (FewRel) 的 missed_rate **有源数据**（`artifacts/fewrel_80rel_error_taxonomy.json`）：
- low: **10.42%** → Table 3 写 10% ✓
- medium: **11.30%** → Table 3 写 12%（向上取整 0.7pp）
- high: **13.05%** → Table 3 写 14%（向上取整 0.95pp）

RE 数据基本可追溯，但取整偏激进。

### 4. NER Missed 数字的可能来源

Table 3 中 NER Missed = RE Missed + 2%（逐格）：

| Bin  | RE Missed | NER Missed | 差值 |
|------|-----------|------------|------|
| Low  | 10%       | 12%        | +2%  |
| Mid  | 12%       | 14%        | +2%  |
| High | 14%       | 16%        | +2%  |

**NER Missed 的 12/14/16% 高度疑似基于 RE Missed 外推（+2pp 偏移），而非独立计算。** 服务器上无任何脚本或中间文件产生过这些数字。

### 正确数字

如果论文需要报告 NER per-BCS-bin missed rate，准确数字（truly missed = 无任何预测文本重叠的 gold 实体 / total gold）：

| BCS Bin | Truly Missed Rate |
|---------|-------------------|
| low     | **42.8%**         |
| medium  | **64.8%**         |
| high    | **49.9%**         |

来源：从 `artifacts/predictions_exp1.json` + Few-NERD test set 重新计算（脚本 `scripts/compute_missed_rate.py`）。

---
