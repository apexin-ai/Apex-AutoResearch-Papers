# paper arr checklist

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_arr-checklist_20260523T183434_result.json`
- **Structured JSON:** [`e11e34a596ba20dfd31a.json`](../../sessions/e1/e11e34a596ba20dfd31a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 审计完成

### 修复了 3 处问题

**A2、B2、B3 引用了不存在的 "Ethics Statement"**：论文中没有 Ethics Statement 章节（只有 Limitations），但 checklist 三处引用了它。已删除悬空引用，改为自包含描述。

### 全部检查项结果

| 项 | 状态 |
|----|------|
| A1 Limitations | PASS |
| A2 Risks | FIXED — 删除悬空引用 |
| A3 Claims | PASS |
| B1 Citations | PASS |
| B2 Licenses | FIXED — 删除悬空引用 |
| B3 Intended use | FIXED — 删除悬空引用 |
| B4 PII | PASS |
| B5 Documentation | PASS |
| B6 Statistics | PASS |
| C1 Compute | PASS |
| C2 Hyperparameters | PASS |
| C3 Descriptive stats | PASS |
| C4 Packages | PASS |
| D Human annotators | PASS |
| E1 AI assistants | PASS — "Appendix ak" 问题已修复 |

无占位符、无遗漏引用、所有 `\ref{}` 和 `\cite{}` 目标均存在。

### 建议（未自动修改）

论文缺少 Ethics Statement 章节。虽然 ARR/EMNLP 2026 不强制要求，但建议在 main.tex 的 Limitations 前加一段简短的 `\section*{Ethics Statement}`，覆盖 B2/B3 中提到的 license 和 intended use 信息，避免 reviewer 质疑。

报告已写入 `artifacts/arr_checklist_audit.md`。

---
