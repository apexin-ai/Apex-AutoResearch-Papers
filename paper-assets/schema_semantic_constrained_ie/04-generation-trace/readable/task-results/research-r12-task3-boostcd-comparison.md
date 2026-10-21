# research r12 task3 boostcd comparison

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_r12_task3_boostcd_comparison_20260520T174617_result.json`
- **Structured JSON:** [`9775203aa4c154706703.json`](../../sessions/97/9775203aa4c154706703.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个文件已写入。总结关键发现：

**Part A — BoostCD:**
- Šakota & West, EMNLP 2025, 代码公开 (epfl-dlab/BoostCD)
- **Reviewer 2 关于 BoostCD 用 SciERC/DocRED 的说法是错误的。** BoostCD 做的是 Closed IE（从文本提取 Wikidata KB 中的三元组），评估用 Wiki-cIE Code，与 OntoCoDec 的 open-schema IE 是完全不同的任务
- 模型也不同：FlanT5-base (250M) vs 我们的 7-8B
- 约束类型不同：KB 成员约束 vs 类型语义约束
- **直接实验对比不可行也不合理**，建议在 rebuttal 中纠正事实错误并做定性讨论

**Part B — "Koldehoff et al.":**
- **"Koldehoff" 是 Reviewer 2 幻觉的作者名**，该论文实际作者是 **David M. Schmidt & Philipp Cimiano** (Bielefeld University)
- 论文: "Grammar-Constrained Decoding for Structured IE with Fine-Tuned Generative Models Applied to Clinical Trial Abstracts"
- Frontiers in AI, Vol 7, 2025, DOI: 10.3389/frai.2024.1406857
- BibTeX entry 已写入，key 用 `schmidt2025grammar`

---
