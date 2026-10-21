# paper exp A crossscorer table

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_exp_A_crossscorer_table_20260515T112213_result.json`
- **Structured JSON:** [`c9624b91e17b1dd254c3.json`](../../sessions/c9/c9624b91e17b1dd254c3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已写入 `docs/paper/tables/tab_crossscorer.tex`。

设计说明：
- 按 Generator Data 分两组（Qwen-RW / Qwen-cont），每组首行为 self-scorer baseline
- K*=1 的行用 `\textcolor{red}{1†}` 标注
- AUC(1v2) < 0.60 的值（0.5923, 0.5858）用 `\underline{}` 标注
- Self-scorer baseline 缺失的列用 `---` 填充
- 风格与现有表格一致：booktabs、`\small`、无 float wrapper

需要 preamble 中有 `\usepackage{xcolor}` 支持 `\textcolor{red}{}`。

---
