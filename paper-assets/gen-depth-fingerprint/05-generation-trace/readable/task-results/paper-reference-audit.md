# paper reference audit

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_reference-audit_20260515T050713_result.json`
- **Structured JSON:** [`b8d922b37db45fb0ba7a.json`](../../sessions/b8/b8d922b37db45fb0ba7a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

审计完成。报告已写入 `artifacts/_project/paper/reference_audit.md`。

核心发现：
- 43 条 bib 条目全部被引用，无孤立条目，无缺失引用
- 抽查 8 篇论文全部真实存在，无伪造引用
- **5 个条目 author 字段不完整**（仅有姓氏缺名字）：`diveye`、`ood_baseline`、`aaronson_watermark`、`writing_diversity`、`stamatatos_survey`，需补全以避免引用格式异常

---
