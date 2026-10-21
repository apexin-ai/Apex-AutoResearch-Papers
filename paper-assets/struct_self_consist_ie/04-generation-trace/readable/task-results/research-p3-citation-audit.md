# research p3 citation audit

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_p3-citation-audit_20260520T134900_result.json`
- **Structured JSON:** [`af566c2d50f1a30d5072.json`](../../sessions/af/af566c2d50f1a30d5072.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已保存到 `artifacts/r25_response/citation_audit.md`。

结果：
- **4 条未验证引用**：全部通过 WebSearch 验证为真实论文，元数据正确，无需修改
- **Orphan entries**：找到 **21 条**（多于预期的 17 条），全部可从 `references.bib` 中删除
- `venktesh2025trust` 既是未验证引用之一，也是 orphan（bib 中有但 tex 中未引用）

---
