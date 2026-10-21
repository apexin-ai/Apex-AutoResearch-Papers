# fix figure3 caption and audit

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_figure3_caption_and_audit_20260519T150315_result.json`
- **Structured JSON:** [`0120ab3aa975d6a450f7.json`](../../sessions/01/0120ab3aa975d6a450f7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

### Part 3: 一致性验证

**修改清单：**

| # | 文件 | 修改内容 |
|---|------|----------|
| 1 | `appendix.tex:246` | caption 第一处：`\texttt{full\_trace} (red, squares)` → `\texttt{full\_trace} with label-only loss (red, squares)` |
| 2 | `appendix.tex:246` | caption 第二处：`while \texttt{full\_trace} plateaus` → `while \texttt{full\_trace} (label-only loss) plateaus` |
| 3 | `plot_dynamics.py` | legend 4 处：`"Full-trace"` → `"Full-trace (LO)"`，`"Full-trace pass/fail"` → `"Full-trace (LO) pass/fail"` |
| 4 | `figures/paper/training_dynamics.{pdf,png}` | 用修正后的脚本重新生成 |

**一致性确认：**
- 图例标签：`Full-trace (LO)` ✓
- Caption：`full\_trace with label-only loss` ✓
- `experiments.tex:89`：已写 "A label-only loss variant"，无需修改 ✓
- 附录表格：已写 `Full Trace (LO)` ✓
- `discussion.tex`：无 figure 环境，仅 section 引用，无需修改 ✓
- `\ref{fig:training_dynamics}`：全文无引用，无额外需要修改的正文描述

三者（图例、caption、正文描述）现在一致标注了 label-only loss。

---
