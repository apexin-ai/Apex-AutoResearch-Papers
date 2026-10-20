# paper appendix 10k robustness

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_appendix_10k_robustness_20260522T141751_result.json`
- **Structured JSON:** [`b1eae82c1c9e35aec880.json`](../../sessions/b1/b1eae82c1c9e35aec880.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已完成。

**插入位置**：文件末尾，紧接 `\subsection{Bonferroni-Corrected Confidence Intervals}` 及其表格之后。

**添加内容**：
- `\subsection{Cross-Sample Robustness: 5K vs.\ 10K}`（`\label{sec:robustness_10k}`）
- 两段说明文字：第一段交代实验动机（between-sample variability），第二段报告 Pythia-1.4B 结果（K\*=2 一致，1v2 AUC Δ=-0.036，2v3 near chance），末尾留 pending 占位句
- `Table~\ref{tab:robustness_10k}`：6 行表格，Pythia 行填入完整数据，Qwen/LLaMA 5K 行交叉引用 Bonferroni CI 表，10K 行标 *pending*

---
