# paper prose tightening

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_prose_tightening_20260522T024335_result.json`
- **Structured JSON:** [`787a897b530478c07dd9.json`](../../sessions/78/787a897b530478c07dd9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 修改摘要

**results.tex — 5 处**

| # | 类型 | 位置 | 改动 |
|---|------|------|------|
| 1 | wordiness | §Results 首段 | 合并两句 "unless noted"，消除冗余重复 |
| 2 | wordiness | §Count Curves | "the elimination of" → "eliminating" |
| 3 | wordiness | §Pairwise | "which indicates" → "indicating" |
| 4 | sentence split | §Practical magnitude | 拆分 ~50 词的 amplification 长句（冒号→句号） |
| 5 | sentence split | §Multi-Dimensional | "Two factors" 句末拆分，将 factorial 结论独立成句 |

**discussion.tex — 2 处**

| # | 类型 | 位置 | 改动 |
|---|------|------|------|
| 6 | clarity | ¶Boundary conditions | "NER null not detected on" → "no NER BCS effect detected across"（消除歧义） |
| 7 | sentence split | ¶Boundary conditions | 拆分 ~45 词长句（冒号→句号） |

统计：wordiness 3 / sentence split 3 / clarity 1。无数值、术语、引用、逻辑变动。

---
