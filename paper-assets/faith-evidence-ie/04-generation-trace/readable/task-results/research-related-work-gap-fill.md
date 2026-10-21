# research related work gap fill

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_related_work_gap_fill_20260515T210911_result.json`
- **Structured JSON:** [`61c82e798616515a4891.json`](../../sessions/61/61c82e798616515a4891.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已生成并注册（`art_20260515_ab131b`）。

**7 个方法全部找到，无幻觉项**：

| 方法 | Venue | Role | 关键点 |
|------|-------|------|--------|
| **R1-RE** | arXiv 2025.07 | direct-competitor | GRPO+RLVR 做 RE，最直接 concurrent work |
| **RelPrior** | arXiv 2025.11 | direct-competitor | 两阶段过滤，LLM-based DocRE 最新 SOTA |
| **Ru-LLM** | NLPCC 2025 | direct-competitor | MCTS 挖逻辑规则+CoT 验证，explicit rule 路线 |
| **AutoRE** | ACL 2024 Demo | direct-competitor | QLoRA+RHF 三阶段，必引的 LLM DocRE baseline |
| **GLiDRE** | arXiv 2025.08 | related_method | Encoder-based zero/few-shot DocRE |
| **InFusE** | arXiv 2024.02 | evaluation | NLI-based 增量 faithfulness 评估，与 EDCR 概念相关 |
| **TRUE** | NAACL 2022 | background | Factual consistency evaluation 经典框架 |

**优先级建议**：R1-RE 和 AutoRE 必须重点讨论（分别是 GRPO for RE 的 concurrent work 和 QLoRA DocRE 的直接 baseline）。RelPrior/Ru-LLM 作为 LLM-based DocRE 近期方法补充。TRUE/InFusE 在 evaluation 相关段落简要引用。

---
