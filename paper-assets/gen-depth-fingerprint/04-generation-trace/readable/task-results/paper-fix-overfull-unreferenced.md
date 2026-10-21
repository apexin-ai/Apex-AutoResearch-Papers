# paper fix overfull unreferenced

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_fix-overfull-unreferenced_20260522T185218_result.json`
- **Structured JSON:** [`8edb9281c3e71d74a841.json`](../../sessions/8e/8edb9281c3e71d74a841.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 报告

### Issue 1: baselines 表 overfull hbox
- `results.tex` L127 的 `\begin{tabular}{lcccc}` 用 `\resizebox{\columnwidth}{!}{...}` 包裹，与 L39 的 LOGO 表写法一致
- 编译后 overfull hbox: **0**（已消除）

### Issue 2: 未引用 appendix label
| Label | 处理 | 插入位置 |
|---|---|---|
| `app:convergence` | 补了引用 | results.tex L77 — "shape features remain flat **(per-feature trajectories in Appendix~\ref{app:convergence})**" |
| `app:holdout-split` | 补了引用 | results.tex L98 — "Permutation testing confirms the split as non-random; **disjoint generator-pool splits produce identical zone assignments (Appendix~\ref{app:holdout-split})**" |
| `app:ddr-causality` | 补了引用 | discussion.tex L9 — ANOVA 句后追加 "**Granger causality and feature-intervention tests confirm the causal direction (Appendix~\ref{app:ddr-causality})**" |
| `app:ddr-supplement` | 无需引用 | 父容器 section，子节已各自被引用 |

### 编译结果
- 0 errors, 0 undefined refs, 0 overfull hbox
- 唯一 warning: `fig2_framework.pdf` 缺失（已有问题）
- PDF 已拉回 `artifacts/_project/paper/` 和 `docs/paper/`

---
