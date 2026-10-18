# research third task type eval

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_third-task-type-eval_20260515T041309_result.json`
- **Structured JSON:** [`bdf37c6c66a0c3e2087a.json`](../../sessions/bd/bdf37c6c66a0c3e2087a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已写入并注册。核心结论：

**推荐加 RE，选 FewRel（100 types）。** 理由：
- 声称 task-agnostic 的 IE 论文标配是 NER + RE + EE 三类。只有 NER + ED（都是 sequence labeling）会被 reviewer 质疑
- FewRel 100 types、sentence-level、完全公开（GitHub/HuggingFace），数据准备成本最低
- 预估总耗时 ~6-8h（含 GPU），10 天内可承受
- 建议插入为 exp-005b (P0)，与原 DocRED (P1) 并行规划

---
