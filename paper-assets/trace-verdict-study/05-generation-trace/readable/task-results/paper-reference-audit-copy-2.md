# paper reference audit

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_reference-audit_20260516T023811_result.json`
- **Structured JSON:** [`2bebe5d2fbcce6288a63.json`](../../sessions/2b/2bebe5d2fbcce6288a63.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

审计完成。汇总：

**28 条引用全部验证，0 缺失，0 孤立。**

| 状态 | 数量 | 说明 |
|------|------|------|
| FAIL（已修复） | 2 | `ferrando2025execute` 和 `appt2024`：作者名完全是 AI 幻觉，已替换为正确作者 |
| WARNING（已修复） | 8 | 年份错误 1 条、workshop 名错 1 条、作者名细节 1 条、标题格式 2 条、作者列表不完整 3 条 |
| PASS | 18 | 标题/作者/年份/venue/arXiv ID 全部正确 |

**已直接修复 `references.bib`**，所有 10 个问题条目均已更正。无引用上下文错误（张冠李戴）。报告写入 `artifacts/_project/paper/reference_audit_report.md`。

---
