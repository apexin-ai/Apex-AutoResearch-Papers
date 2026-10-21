# audit reference verification

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_reference_verification_20260521T031451_result.json`
- **Structured JSON:** [`1849adbaba396fb7af38.json`](../../sessions/18/1849adbaba396fb7af38.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

审计完成。66 条 bib 条目全部已覆盖（43 条旧审计 + 26 条新增验证，3 条旧条目已删除）。

**发现并修正 4 处错误：**

| 条目 | 问题 | 严重程度 |
|------|------|---------|
| `attractor_cycles` | 9 个作者全部是 LLM 幻觉生成，标题被截断，缺 arXiv ID | **CRITICAL** |
| `ghostbuster` | 末位作者 Jurafsky→Klein，venue ACL→NAACL | HIGH |
| `qlora` | 标题 "Language Models"→"LLMs"（NeurIPS 官方标题） | LOW |
| `aaronson_watermark` | Hendrik Kirchner→Jan Hendrik Kirchner | LOW |

其余 22 条新增条目验证通过，无错误。

报告已写入 `artifacts/_project/analysis/reference_audit.md`。

---
