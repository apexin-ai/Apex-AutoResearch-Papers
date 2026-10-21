# paper table45 overlap fix

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_table45_overlap_fix_20260522T063749_result.json`
- **Structured JSON:** [`8cba9357ec5edb2f2632.json`](../../sessions/8c/8cba9357ec5edb2f2632.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

编译成功，无 float 相关 warning。仅有标准 hyperref/caption warnings。

---

## 结果

### Part 1: Table 4/5 重叠 — 已修复

**根因**：Table 4 (`tab:domain_kstar`) 在 `experiments_c1.tex` 中用 `\begin{minipage}` + `\captionof{table}`（inline 非 float），Table 5 (`tab:tab_filtering_main`) 在 `experiments_c3.tex` 中用 `\begin{table}[t]`（float）。LaTeX 将 float 放到 minipage 所在页面顶部导致重叠。

**修复**：将 Table 4 从 minipage 转为 `\begin{table}[t]` float，让 LaTeX 正确管理两个表的排版。

### Part 2: S12 caption — 已修复

**arXiv 数据来源**：**Qwen2.5-1.5B (base)**，不是 Instruct。证据：
- `exp024_arxiv_domain.sh` 头部注释: "模型: Qwen2.5-1.5B (base)"
- `exp024_bootstrap_ci.json`: "exp-024 Qwen2.5-1.5B-base arXiv continuation"
- MODEL 路径: `.hf_cache/Qwen/Qwen2.5-1.5B`（无 Instruct）

**修复**："Qwen2.5-1.5B-Instruct, continuation mode" → "Qwen2.5-1.5B, continuation mode"

注：S12 数据格仍为 `---` 占位符。

### Part 3: ANOVA caption — 已修复

- **旧版**："The non-significant Scorer main effect confirms scorer independence of depth discrimination."
- **新版**："Scorer is statistically significant but explains modest variance ($\eta^2_p{=}.166$)."

注：ANOVA 表数据格也仍为 `---` 占位符。

---
