# paper related work draft

**The Embedding Alignment Gap: Why Diversity-Based Data Selection Accelerates Model Collapse in Iterative Self-Training** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_related_work_draft_20260513T213402_result.json`
- **Structured JSON:** [`b3fd2a7390766b8e47c0.json`](../../sessions/b3/b3fd2a7390766b8e47c0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有 36 篇引用的 citation key 均与 `references.bib` 一致。

文件已写入 `docs/paper/related_work.tex`，4 个 subsection：

1. **Model Collapse in Iterative Training** — 7 篇，建立 collapse 背景，末尾点明本文研究的不是 collapse 本身而是 diversity curation 为何加速 collapse
2. **Data Curation and Selection for LLM Training** — 8 篇，覆盖 SemDeDup/D4/DSIR/LESS/DsDm/QuRating/SelectIT，末尾指出这些方法假设 static dataset，iterative setting 引入新失效模式
3. **Embedding-Based Diversity and Representation Learning** — 11 篇，涵盖 submodular optimization、active learning、dimensional collapse，末尾说明几何坍缩在自训练中从良性变为病理性
4. **Representation Drift and Proxy Misalignment** — 10 篇，concept drift + Goodhart's law + diversity metrics，末尾解释 alignment gap 作为 proxy misalignment 实例，并说明选用 rare n-gram density 的原因

---
