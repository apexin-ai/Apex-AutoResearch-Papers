# paper emnlp submission prep

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_emnlp-submission-prep_20260516T030521_result.json`
- **Structured JSON:** [`384340b2983582220845.json`](../../sessions/38/384340b2983582220845.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Checklist 写入 `artifacts/emnlp_submission_checklist.md` 并已注册。

**结果**：26 项通过，1 项必须修复，6 项需人工确认。

**必须修复**：
- `paper/_backup/` 目录必须从提交包中删除（含 24 个过期 .tex，部分有 `\cite{placeholder}`）

**需编译验证**：
- 页数估计 7–9 页，必须编译确认 ≤ 8 页（Discussion 86 行是首选裁减对象）
- PDF metadata 无作者信息泄露
- `acl.sty` 需包含在提交目录中
- `chart/` 下有 3 个未引用图片文件可清理
- `app:sampling-sensitivity` 是 Appendix G 的 `\subsection*`，交叉引用指向父节点而非子标题

---
