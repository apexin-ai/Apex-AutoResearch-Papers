# paper r25 m2 m5 citation highlight

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_r25_m2_m5_citation_highlight_20260522T074133_result.json`
- **Structured JSON:** [`012b21ef8e2e62984dc9.json`](../../sessions/01/012b21ef8e2e62984dc9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。

### 结果

**M2 — Suresh 引用**
- `references.bib`: 添加 `suresh2024rate` 条目
- `related_work.tex` L6，插入位置上下文：
  ```
  ...fu2025theoretical}, diversity contraction~\cite{...}, and predictable convergence~\cite{...}.
  Suresh et al.~\cite{suresh2024rate} derive precise collapse rates for discrete distributions under recursive MLE training, complementing the theoretical conditions established by Fu et al.~\cite{fu2025theoretical}.
  Our prompt-chain operates in the replace regime~\cite{kazdan2025collapse}...
  ```

**M5 — Table 2 boundary 高亮**
- 方案：**`\cellcolor`**（不同列 K\* 不同，无法用 rowcolor）
- 高亮 cells：
  - **0v1 行**：OLMo 的 AUC + CI 两个 cell（K\*=1 boundary）
  - **1v2 行**：Qwen-rw / Pythia / Qwen-cont / Qwen-7B 的 AUC + CI 共 8 个 cell（K\*=2 boundary）
  - OLMo 1v2 (.5080) 未高亮
- 添加表注："Shaded cells indicate the K\*\_empirical boundary (last depth pair with AUC > θ=0.60)."
- `\PassOptionsToPackage{table}{xcolor}` 置于 `\documentclass` 前（避免与 acl 包冲突）

**编译**：成功，22 页，525KB PDF 已同步到本地。

---
