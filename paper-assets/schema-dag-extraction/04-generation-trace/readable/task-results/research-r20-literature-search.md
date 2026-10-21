# research r20 literature search

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_r20_literature_search_20260519T045626_result.json`
- **Structured JSON:** [`9296ec54b33dc5333817.json`](../../sessions/92/9296ec54b33dc5333817.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

文件已写入 `artifacts/r20_literature_additions.md`。

关键发现：
- **MR1** — Dubey et al. (2018) ECCV，pages 71-88，信息完整
- **MR2** — 标题与作者不匹配。"Exploiting Class Similarity..." 实际是 Gare & Galeotti (arXiv 2021)，而 Collier et al. 2021 是 "Correlated Input-Dependent Label Noise"（CVPR 2021, pages 1551-1560）。两篇都列出了 bib 和引用文本，请确认用哪篇
- **MR3** — Park et al. (2024) "Grammar-Aligned Decoding"，NeurIPS 2024，核心论点：constrained decoding 会扭曲 LLM 的概率分布，直接关联 schema 约束下的 calibration 问题

---
