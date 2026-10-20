# research f1 macro audit

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_f1-macro-audit_20260516T155949_result.json`
- **Structured JSON:** [`1c607f6fce44ef1642d4.json`](../../sessions/1c/1c607f6fce44ef1642d4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

审计完成。核心发现：

**论文侧**：Table 1（函数级）和 Table 2（scaling）完全没有 F1-macro 列——这是 reviewer 指出的主要问题。Table 3（repo 级）有 Macro F1 列但 CWM 8B s42 为 `---`。

**代码侧**：只有 `eval_repo_cwm.py` 显式输出 `f1_macro`。其余四个 eval 脚本都只计算 per-class F1（`average=None`），未聚合为 macro。修复只需加一行 `f1.mean()`。

报告已写入 `artifacts/f1-macro-audit.md`，含完整表格审计、脚本能力对照、差距清单和具体 diff 建议。

---
