# research plan 004 gsm1k data collection

**Temporal Score Incomparability in LLM Benchmarks: A Large-Scale Psychometric Audit of 5,227 Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_plan_004_gsm1k_data_collection_20260521T005054_result.json`
- **Structured JSON:** [`85b939a6890b742b5494.json`](../../sessions/85/85b939a6890b742b5494.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据收集完成。

**结果摘要：**
- 收集 **82 个模型**的 GSM1K 准确率（70 个有配对 GSM8K/GSM1K，12 个仅有 GSM1K）
- **34 个**匹配到 METABENCH model ID（41.5%）
- 污染 gap 范围：-0.025（Claude-3-Sonnet）到 +0.093（Deepseek-llm-67b-base）
- 高污染家族：Phi（+0.04~0.06）、Gemma/CodeGemma（+0.04~0.07）、Xwin-Math（+0.06）
- 低/负污染：GPT-4、Claude 系列、Llama-2 家族

**未匹配的主要原因**：API-only 模型（GPT/Claude/Gemini）不在 METABENCH 中；部分基座模型（Llama-2-7b/13b/70b-hf、Mistral-7B-v0.1）也不在 METABENCH 中。

产出已写入 `artifacts/plan_004/gsm1k_model_accuracy.csv` 和 `gsm1k_data_report.md`，并完成注册。

---
