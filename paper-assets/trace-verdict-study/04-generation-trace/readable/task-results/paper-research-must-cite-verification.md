# paper research must cite verification

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_research_must_cite_verification_20260515T180431_result.json`
- **Structured JSON:** [`e1fa73e90c0b3b56e291.json`](../../sessions/e1/e1fa73e90c0b3b56e291.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

3 篇论文全部找到并验证，已更新到 literature_map.yaml 和 references.bib。

| 论文 | 状态 | 实际标题 | Venue | 注意事项 |
|------|------|----------|-------|----------|
| **TracePile** | verified | "Chain of Execution Supervision Promotes General Reasoning in Large Language Models" (Chen et al.) | NeurIPS 2025 | TracePile 是论文中的数据集名称，非论文标题。arxiv: 2510.23629 |
| **TRACED** | verified | "TRACED: Execution-aware Pre-training for Source Code" (Ding et al.) | ICSE 2024 | arxiv: 2306.07487 |
| **CRUXEval** | verified | "CRUXEval: A Benchmark for Code Reasoning, Understanding and Execution" (Gu et al.) | ICML 2024 | arxiv: 2401.03065。注意 paper_framing 可能标注为 "Gu et al., 2024"，venue 是 ICML 不是其他 |

paper_framing 中引用时需注意：TracePile 的正式引用应该是 `\cite{chen2025tracepile}`，论文标题是 "Chain of Execution Supervision..."，TracePile 只是数据集名。

---
