# analysis error analysis rsft comparison

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_error_analysis_rsft_comparison_20260518T144730_result.json`
- **Structured JSON:** [`a2e32e2aa699c61802a0.json`](../../sessions/a2/a2e32e2aa699c61802a0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

核心结论汇总：

**RSFT 相对 SFT 的三大改善机制（三个模型尺度一致）：**

1. **Truncation FN 减少 16-22%** — 最大改善项。RSFT 筛选的样本让模型学会更紧凑的输出格式，减少输出截断丢失。1.7B 减少 841 个，效果最显著。

2. **Hallucinated FP 减少 6-12%** — 拒绝不忠实生成的训练信号直接降低幻觉。Llama 获益最大（-593，-11.8%）。

3. **Duplicates 减少 11-20%** — 格式规范性的副产品，小模型受益最大（1.7B: -20.2%）。

**未改善的：**
- Evidence quality 基本不变（exact match 变化 < 0.4pp），evidence grounding 需要专门的训练信号
- Relation confusion FP 不变（除 Llama -11.4%）
- Rare relation FN 不变

**k=1 vs k=3：** k=1 在 1.7B 和 Llama 上优于 k=3，8B 上 k=3 略优（Ign-F1 +0.57）。总体 k=1 更好。

**Per-relation 获益最大的关系类型：** participant, conflict, league, screenwriter, operator, contains administrative territorial entity 等。这些关系通常涉及较多跨句推理或长尾实体，RSFT 通过减少幻觉和截断帮助最大。

所有产出：
- `/root/autodl-tmp/analysis/error_analysis_sft/` — SFT 分析
- `/root/autodl-tmp/analysis/error_analysis_d102_k1/` — RSFT d102 k=1 分析
- `/root/autodl-tmp/analysis/error_analysis_plan006_k3/` — RSFT plan_006 k=3 分析
- `/root/autodl-tmp/analysis/error_analysis_comparison_report.md` — 完整对比报告

---
