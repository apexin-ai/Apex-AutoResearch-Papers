# research ref audit websearch

**Temporal Score Incomparability in LLM Benchmarks: A Large-Scale Psychometric Audit of 5,227 Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_ref_audit_websearch_20260522T033511_result.json`
- **Structured JSON:** [`f89f5d7f03337ae4c552.json`](../../sessions/f8/f89f5d7f03337ae4c552.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

审计完成。报告已写入 `artifacts/ref_audit_report.md`。

关键发现：
- **必须修复**: `habba2026growingpains` 的第一作者名为 "Eliya"（非 "Eitam"），第二作者为 "Itay"（非 "Ido"）
- **格式问题**: arXiv 条目有两种格式混用（`@misc`+`eprint` vs `@article`+`journal`），建议统一为前者；ICLR/AAAI venue 命名各有 1 处不一致
- 其余 4 个 entry（`kolen2014equating`, `zhu2026bhi`, `carlini2022quantifying`, `french2010hierarchical`）均验证通过
- Director 指定的 key `french2010effect` 在 bib 中不存在，实际 key 为 `french2010hierarchical`

---
