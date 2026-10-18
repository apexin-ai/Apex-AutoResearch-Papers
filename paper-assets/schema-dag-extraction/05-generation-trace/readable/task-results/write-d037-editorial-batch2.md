# write d037 editorial batch2

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_write_d037_editorial_batch2_20260516T034701_result.json`
- **Structured JSON:** [`aba9e0efd7e49e602302.json`](../../sessions/ab/aba9e0efd7e49e602302.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

编译成功，16 页，无错误。3 个 BibTeX warnings 来自 results.tex 中的引用键（另一个 Worker 负责的文件）。

### 修改总结

**已执行的修改：**

1. **C1 修正 + NER v1/v2 影响说明** — `experimental_setup.tex` §3.5：在 prompt 版本描述中插入 RE 单一 prompt 说明 + NER v1→v2 的定量影响（pred/gold ratio、precision/recall 变化）
2. **reflect-learn-2026 venue** — `references.bib`：确认 AAAI 2026 已正式接收，补充 pages 和 doi 字段

**无需修改的项目（已是最新状态）：**

- W1: 无 "framework" 出现
- W6: RE caveat 已在 discussion.tex
- W10: FewRel limitations 已在 main.tex
- W11: 51% floor 已用 "one possible explanation" 措辞
- W12: 无 "model-invariant" 出现
- C1 prompt cross-ref: 已有 `Appendix~\ref{sec:appendix_prompts}` 引用
- m1: Sentence-BERT 已在 bib 且已引用
- R2-REF: 两篇引用均已在 bib 且在 related_work.tex 中引用
- json-schema-bench-2025: 无 "and others"，格式正常

---
