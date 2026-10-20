# code r19 open closed dif

**Temporal Score Incomparability in LLM Benchmarks: A Large-Scale Psychometric Audit of 5,227 Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_r19_open_closed_dif_20260522T184758_result.json`
- **Structured JSON:** [`2b5488ba1e23377ffba1.json`](../../sessions/2b/2b5488ba1e23377ffba1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All three deliverables produced:

- **Script**: `artifacts/r19_open_closed_dif/open_closed_dif_analysis.py`
- **Report**: `artifacts/r19_open_closed_dif/open_closed_dif_report.md`
- **CSV**: `artifacts/r19_open_closed_dif/model_source_classification.csv`

## 结果摘要

**核心发现：METABENCH 中 closed-source 模型数量为 0。** 所有 5,227 个模型均来自 HF Open LLM Leaderboard，都有公开权重。名称中含 "gpt-4" 的模型是用 GPT-4 蒸馏数据微调的开源模型，不是 API 模型本身。

**Fallback 分析（distilled-from-API vs non-distilled）**：
- Distilled 组只有 148 个模型，temporal cohort 仅 43 (2023) vs 9 (2024)——严重 underpowered
- Distilled C% = 1.5%，Non-distilled C% = 30.2%（差异主要由样本量驱动）
- Size-matched control 显示 distilled 的 C% 落在随机抽样的 95% CI 内——无显著差异
- Jaccard overlap 仅 0.034，说明小样本组检测到的 C items 几乎是大样本组的子集

**结论：open-vs-closed 分析在 METABENCH 数据上不可行，这是数据集局限而非方法局限。**

---
