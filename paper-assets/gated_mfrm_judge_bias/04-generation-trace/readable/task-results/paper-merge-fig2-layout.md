# paper merge fig2 layout

**Fair Scores via Joint Calibration: A Gated Many-Facet Rasch Model for Disentangling Judge Bias and Contamination in LLM Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_merge-fig2-layout_20260525T111137_result.json`
- **Structured JSON:** [`767bfeed248505c31144.json`](../../sessions/76/767bfeed248505c31144.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

编译成功，无 undefined reference。正文到 Limitations 在第 8 页，References 从第 9 页开始，满足 8 页限制。

### 汇报

**修改文件：** `background.tex`

**改动：**
- 删除两个独立 `\begin{figure}[t]`（原 fig2_ovb_bias 在第 4–9 行，原 fig4_bias_vs_rho 在第 27–32 行），替换为一个 `\begin{figure*}[t]` 双栏图（第 4–17 行），含两个 `minipage` 并列布局
- 合并 caption，加 (a)/(b) 子图标注
- 删除 `\label{fig:bias_vs_rho}`，统一用 `\label{fig:ovb_bias}`

**引用变化（第 50 行）：**
- `Figure~\ref{fig:bias_vs_rho}` → `Figure~\ref{fig:ovb_bias}b`
- `Figure~\ref{fig:ovb_bias}` → `Figure~\ref{fig:ovb_bias}a`

**编译：** 无 undefined reference，正文 8 页（Limitations 在第 8 页，References 从第 9 页起）。

---
