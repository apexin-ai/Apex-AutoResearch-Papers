# paper fix table captions and formatting

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_fix-table-captions-and-formatting_20260516T050923_result.json`
- **Structured JSON:** [`79b94c331e8129c60df2.json`](../../sessions/79/79b94c331e8129c60df2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All changes verified. Here's the summary:

---

## 修改清单

### Critical: Table caption 位置（9 个表）
- **experiments.tex**: Tables 1-3 (cross_model, ablation, density) — `\caption` + `\label` 从 `\end{tabular}` 之后移到 `\begin{tabular}` 之前
- **appendix.tex**: 6 个表 (trace_length, trace_length_pairwise, calibration, debugbench, dedup, regex) — 同样处理
- appendix.tex 中另外 5 个表已经是正确格式，无需修改

### Should-fix 1: VOTA-AE 命名统一
- appendix.tex per_class 表: `VOTA$-$AE` → `VOTA\_no\_ae`（统一为全文主流写法）

### Should-fix 2: \texttt{} 一致性
- experiments.tex 正文: 裸露的 `VOTA\_no\_ae` 加上 `\texttt{}`
- appendix.tex 3 个表 (train_time, full_qwen, full_deepseek): 去掉表内条件名的 `\texttt{}` 包裹，与其他表格保持一致（表内不用 \texttt{}，正文用）

### Should-fix 3 & 4: 无需修改
- full_trace 命名已统一（技术引用用 `\texttt{full\_trace}`，自然语言用 "full-trace"/"full traces"）
- Rounding 已一致（abstract/conclusion 用 85.6%，表格/实验正文用 85.63%）

### 编译验证
- pdflatex 两次编译通过，**无 error**，引用正常解析

---
