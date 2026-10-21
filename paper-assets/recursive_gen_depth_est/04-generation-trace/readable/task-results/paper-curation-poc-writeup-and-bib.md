# paper curation poc writeup and bib

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_curation_poc_writeup_and_bib_20260515T235442_result.json`
- **Structured JSON:** [`492ccc7461d89fa9d9ec.json`](../../sessions/49/492ccc7461d89fa9d9ec.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。产出报告：

---

### 1. Discussion 段落修改

**修改前**（核心句）：
> "The 70–85% in-distribution accuracy and EDD₀.₇₅=4 suggest depth-graduated filtering is feasible… The downstream effect on training quality remains to be validated empirically."

**修改后**（核心新增）：
- 新增 PoC 实验描述：Pythia-410M LoRA (r=16), 3 epochs, 8 conditions, 5 seeds
- RF vs random 显著性：strict 25% Δ=0.43 PPL p=0.002; moderate 50% Δ=0.24 p=0.02
- Data efficiency：rf_soft 用 44% 数据达到与 unfiltered 不可区分的 PPL (p=0.41)
- Oracle 悖论：oracle-strict 不优于 unfiltered (p=0.22)，classifier imprecision 保留了数据多样性
- 引用 Appendix Table (`\ref{app:curation_poc}`)
- 未 claim RF improves over unfiltered，未用 "significantly" 描述 RF vs unfiltered

### 2. Appendix 新增内容

`section_appendix.tex` 中 Extended Discussion 之前插入 `\subsection{Downstream Curation PoC}` (`\label{app:curation_poc}`)：
- **Table 1** (`tab:curation_poc`)：8 条件完整表（Mean PPL / Std / n / Δ / p / Cohen's d）
- **Table 2** (`tab:curation_comparisons`)：3 组 pairwise 对比（rf vs random strict/moderate, rf_soft vs unfiltered）

### 3. dohmatob bib 修正

确认 arXiv 2410.04840 发表于 **ICLR 2025**（非 2024）。修改：
- `references.bib`：key `dohmatob2024_strong_collapse` → `dohmatob2025_strong_collapse`，year 2024 → 2025
- `related_work.tex`：`\citet{dohmatob2024_strong_collapse}` → `\citet{dohmatob2025_strong_collapse}`
- `literature_map.yaml`：key 和 year 同步更新

### 4. artifacts bib 同步

`artifacts/_project/paper/references.bib` 已用 `docs/paper/references.bib` 覆盖。

---
