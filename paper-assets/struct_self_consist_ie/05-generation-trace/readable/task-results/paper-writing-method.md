# paper writing method

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_writing_method_20260514T194021_result.json`
- **Structured JSON:** [`0676f69bed7749fb51bb.json`](../../sessions/06/0676f69bed7749fb51bb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Method 章节已写入 `docs/paper/sections/method.tex`。

要点：
- 三个小节：Problem Formulation (`sec:formulation`)、Confidence Signals (`sec:signals`)、Evaluation Framework (`sec:evaluation`)，label 与 experiments.tex 中的引用一致
- 信号分类与 experiments.tex 保持一致：Structural (Voting, SJ)、Surface (FK, EM)、Model-internal (logprob)
- 包含记号表（Table 1）
- 所有公式有 label，使用 equation 环境
- 仅引用 references.bib 中已有的 key：`wang2023selfconsistency`、`fleiss1971agreement`、`jaccard1901distribution`、`willard2023guided`
- 末尾自然过渡到 `\S\ref{sec:selection_gap}` 的实验分析
- 约 1000 词，无具体实验数字，无禁忌用语

---
