# verify bib years m7

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_verify_bib-years-m7_20260516T011614_result.json`
- **Structured JSON:** [`27f5e6c728a359b9cb57.json`](../../sessions/27/27f5e6c728a359b9cb57.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

验证完成。

**结果**: 49 条 bib 全部通过验证 — 0 条虚构引用，0 个年份错误，0 个需要从预印本更新到正式版本的条目。

**本次修正**: 1 处
- `model_collapse_avoidable`: COLM venue 名称格式统一（去掉 "First" 和 "(COLM)"，与 `mapping_llm_science` 一致）

**之前修正（Rd1, 已确认正确）**: 3 处
- `curse_of_recursion` 作者顺序、`reliable_detection` 完整标题、`model_collapse_avoidable` arXiv→COLM

审计报告已更新至 `artifacts/bib_audit_report.md`。

---
