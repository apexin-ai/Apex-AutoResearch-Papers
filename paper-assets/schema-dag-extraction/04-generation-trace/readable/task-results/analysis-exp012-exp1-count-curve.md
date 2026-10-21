# analysis exp012 exp1 count curve

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp012_exp1_count_curve_20260515T195527_result.json`
- **Structured JSON:** [`1e4d3e07bb1bedf4772b.json`](../../sessions/1e/1e4d3e07bb1bedf4772b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。核心结论：

**Channel 1 跨模型复现成功。** 

| | LLaMA-3.1-8B | Qwen3-8B |
|---|---|---|
| R(count_1) | 0.702 | 0.640 |
| R(count_64) | 0.273 | 0.304 |
| Recall decline | **-43pp** | **-34pp** |
| Min-R | 0.178 @ count_22 | 0.271 @ count_22 |

三个关键发现：

1. **Per-batch recall 相关性 r=0.7249** — 对同一 batch，两个模型的 recall 高度相关，说明难度来自 schema 配置本身而非模型特异性
2. **LLaMA 下降更陡**（-43pp vs -34pp），支持"弱模型对 schema 复杂度更敏感"的论述
3. **exact/relaxed F1 = 0 是预期行为** — 预测缺少字符偏移量（start/end），不是类型格式问题。text_match 是两个模型的正确对比指标

摘要已保存至 `artifacts/exp012/exp1_analysis_summary.txt`，registry metrics 已更新。

---
