# paper unify delta subscript

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_unify-delta-subscript_20260514T144029_result.json`
- **Structured JSON:** [`e1d68d5a3be98c9693c9.json`](../../sessions/e1/e1d68d5a3be98c9693c9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部替换完成，不再有任何不统一变体。汇总：

| 文件 | 改动数 | 改了什么 |
|------|--------|----------|
| `artifacts/_project/paper/latex/introduction.tex` | 2 处 | `\Delta_{\text{no\_death}}` → `\Delta_{\text{nd}}` |
| `artifacts/_project/paper/latex/method.tex` | 3 处 | `\Delta_{\text{no\_death}}` → `\Delta_{\text{nd}}` |
| `artifacts/_project/paper/latex/experiments.tex` | 1 处 | `\Delta_{\text{no\_death}}` → `\Delta_{\text{nd}}` |
| `artifacts/_project/paper/latex/conclusion.tex` | 2 处 | `\Delta_\text{full}` → `\Delta_{\text{full}}`，`\Delta_\text{nd}` → `\Delta_{\text{nd}}`（加花括号） |
| `artifacts/_project/paper/conclusion.tex` | 2 处 | 同上（加花括号） |
| `docs/paper/abstract.tex` | 2 处 | `\Delta_{\text{no\_death}}` → `\Delta_{\text{nd}}` |
| `docs/paper/introduction.tex` | 1 处 | `\Delta_{\text{no\_death}}` → `\Delta_{\text{nd}}` |
| `docs/paper/method.tex` | 5 处 | `\Delta_{\text{no\_death}}` → `\Delta_{\text{nd}}` |
| `docs/paper/experiments.tex` | 2 处 | `\Delta_{\text{no\_death}}` → `\Delta_{\text{nd}}` |
| `docs/paper/conclusion.tex` | 1 处 | `\Delta_{\text{no\_death}}` → `\Delta_{\text{nd}}` |
| `artifacts/penalty_sensitivity_table.tex` | 5 处 | `\Delta_\text{full}` → `\Delta_{\text{full}}`，`\Delta_\text{nd}` → `\Delta_{\text{nd}}` |
| `artifacts/plan-012-penalty-sensitivity/report/penalty_sensitivity_table.tex` | 5 处 | 同上 |

共 12 个文件、31 处替换。全文现在统一使用 `\Delta_{\text{nd}}` 和 `\Delta_{\text{full}}`。`paper_framing.md` 中无 Delta 符号，无需修改。

---
