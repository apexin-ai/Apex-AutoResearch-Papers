# paper research

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_research_20260522T150026_result.json`
- **Structured JSON:** [`194b0353559fb523c501.json`](../../sessions/19/194b0353559fb523c501.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 验证摘要

| 类别 | 总数 | 验证通过 | 需注意 |
|------|------|----------|--------|
| Part A (literature_map) | 12 | 12 | Paper 11: 第一作者是 **Kuai** 非 Chen；标题被截断 |
| Part B (经典引用) | 10 | 10 | — |
| Part C (补充引用) | 6 → 7 | 6 | Paper 5 标题不匹配，已修正 |
| **合计** | **29 条 BibTeX** | **28 verified + 1 corrected** | |

**需要注意的问题：**

1. **`kuai2026independent`** — `literature_map.yaml` 中标注为 "Chen et al. 2026"，但第一作者实际是 Chenchen Kuai。论文中引用时需用 `\cite{kuai2026independent}`，或在 literature_map 中修正作者信息。

2. **`perez2022ignore`** — 任务指定的标题 "Ignore This Title and HackAPrompt" 实际属于 Schulhoff et al. (EMNLP 2023)。Perez & Ribeiro 的正确论文是 "Ignore Previous Prompt: Attack Techniques For Language Models"。两篇都已收录在 bib 中。

3. **`wang2023fair`** — arXiv 2023 预印本，后正式发表于 ACL 2024，已在 note 字段标注。

文件已写入 `docs/paper/references.bib`，共 29 个条目。

---
