# analysis 3seed rsft summary

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_3seed-rsft-summary_20260515T162743_result.json`
- **Structured JSON:** [`18d6e5fdf4519a9d4a1d.json`](../../sessions/18/18d6e5fdf4519a9d4a1d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已完成。写入 memory.md 的全景分析要点：

- **RSFT 3-seed**: rel_f1 = 0.4596 ± 0.0128, evi_f1 = 0.8143 ± 0.0051, EDCR = 0.6434 ± 0.0115。vs SFT +5.39pp / +1.64pp / −6.84pp，std 2.8%，结果稳定。
- **方法排序**: CED reranker (0.4864) > RSFT mean (0.4596) > bf16 GRPO (0.4549) >> QLoRA GRPO (0.2167)
- **四个决策性洞察**: (1) RSFT ceiling 受限于 rejection pool；(2) CED reranker 是 upper-bound reference，8x 推理成本；(3) forgetting 确认 QLoRA-specific；(4) EDCR drop 是 recall-oriented training 的固有 trade-off，非 truncation artifact
- **待完成**: plan_015 隔离 confound、plan_014 SFT-no-evidence、plan_001 flat-NLI ablation

---
