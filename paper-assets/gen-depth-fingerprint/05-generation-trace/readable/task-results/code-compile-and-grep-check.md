# code compile and grep check

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_compile-and-grep-check_20260517T103441_result.json`
- **Structured JSON:** [`1c3eb418ee16732e0fab.json`](../../sessions/1c/1c3eb418ee16732e0fab.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部结果已收集。汇总报告：

---

## 1. 编译结果

| 项目 | 结果 |
|------|------|
| **错误数** (`^!` in main.log) | **0** |
| **Undefined references/citations** | **0** (无任何 undefined) |
| **页数** | **18 页** |
| **警告** | 1 个 `dest name{section*.47} has been referenced but does not exist`（无害的 hyperref 警告） |

编译完全通过。

---

## 2. tail_decay 描述（method.tex 原文）

**Line 49:**
```latex
\item \textbf{tail\_decay}: slope of the vocabulary-level averaged log-probability
distribution in the mid-rank region (ranks 100--1000).
```

**Line 51:**
```latex
The slope captures how steeply the reference model's probability mass decays
beyond high-probability tokens, characterizing the shape of the distribution tail.
```

描述准确，符合要求。method.tex 中**无** "sensitivity analysis" 残留（grep 返回 0 匹配）。

---

## 3. 全文 grep 检查

### 3.1 "90th percentile" 残留
**0 匹配** — 已全部清除。

### 3.2 "sensitivity" 残留
共 6 处，均为**合理使用**（非旧版 sensitivity analysis 声明）：

| 文件 | 行 | 内容 |
|------|-----|------|
| appendix_classifier.tex | 31 | `\subsection*{Sampling Sensitivity Analysis}` — 附录中的采样敏感性分析标题 |
| appendix_classifier.tex | 32 | `\label{app:sampling-sensitivity}` — 对应 label |
| appendix_domain.tex | 25 | 引用 `Appendix~\ref{app:sampling-sensitivity}` |
| discussion.tex | 8 | 引用 `Appendix~\ref{app:sampling-sensitivity}` |
| limitations.tex | 27 | 引用 `Appendix~\ref{app:sampling-sensitivity}` |
| main.tex | 67 | `\section{Classifier Sensitivity}` — 附录 section 标题 |

这些都是对附录采样敏感性分析的正当引用，不是之前要求删除的 method.tex 中的 sensitivity analysis 声明。

### 3.3 Em-dash (—) 数量
**3 处，全部在注释行**（`%` 开头），不会出现在 PDF 中：

| 文件 | 行 | 内容 |
|------|-----|------|
| abstract.tex | 1 | `% Abstract — Depth Fingerprinting...` |
| appendix_length.tex | 1 | `% Appendix — Length Confound Analysis` |
| main.tex | 1 | `% EMNLP 2026 ARR Submission — ACL 2023 Template` |

**正文中 em-dash 为 0。**

### 3.4 解释性 en-dash (` – `)
**0 匹配** — 全文无解释性 en-dash。

---

**总结**：编译 0 错误 0 undefined，18 页。tail_decay 描述正确，旧版 sensitivity analysis 声明和 90th percentile 已全部清除，em-dash/en-dash 正文中为零。全部检查通过。

---
