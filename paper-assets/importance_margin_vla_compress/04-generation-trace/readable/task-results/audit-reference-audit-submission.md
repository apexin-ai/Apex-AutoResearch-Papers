# audit reference audit submission

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_reference_audit_submission_20260528T170501_result.json`
- **Structured JSON:** [`0a3804b06ff3fd26b671.json`](../../sessions/0a/0a3804b06ff3fd26b671.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**审计结果：CONDITIONAL PASS**

62 条 bib 条目，26 条被编译论文引用，36 条 orphan。无幻觉引用，无缺失引用。

须修复的问题：

1. **[critical] `zheng2025xvla`** — 第一作者名错误：bib 写 "Yifu Zheng"，实际为 "Jinliang Zheng"（已通过 arXiv、GitHub、ICLR 2026 页面确认）
2. **[warning] `chen2024fastv`** — 作者列表不完整，仅列 1/7 位作者
3. **[warning] `black2025pi05`** — 已在 CoRL 2025 发表（PMLR 305），bib 仍标记为 arXiv preprint
4. **[warning] 36 条 orphan 条目** — 未被引用，建议清理或补引用

报告已写入 `artifacts/reference_audit_report.md` 并注册。

---
