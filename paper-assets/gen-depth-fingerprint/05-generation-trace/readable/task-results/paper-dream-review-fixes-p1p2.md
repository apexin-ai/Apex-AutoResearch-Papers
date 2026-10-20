# paper dream review fixes p1p2

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_dream-review-fixes-p1p2_20260522T001017_result.json`
- **Structured JSON:** [`77c27814e730d2505cc6.json`](../../sessions/77/77c27814e730d2505cc6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

6 项任务完成情况：

| 任务 | 状态 | 说明 |
|------|------|------|
| **P1-1** R² 澄清 | ✓ | R² 不在 results.tex 而在 `appendix_feature_distributions.tex`。已在 L5 后添加说明：R² 基于 depth-level means（每 generator 5 个点）的 OLS 回归，非 per-sample 回归；Spearman ρ 提供互补的 per-sample 单调性度量。 |
| **P1-2** DDR 阈值 justification | 无需修改 | results.tex L90 的 Validation 段落已包含完整的 permutation test（$n$=10,000, $p$=0.030, silhouette=0.660 vs null 0.46）+ exhaustive enumeration，位于专门的 `\paragraph{Validation}` 中，足够突出。 |
| **P1-3** "structural regularity" | 无需修改 | 全文搜索确认该短语不出现在论文任何 .tex 文件中（仅在 dream report 中）。 |
| **P2-1** Feature ablation vs LOGO | ✓ | 在 results.tex Feature complementarity 段落（L94 后）添加一句，说明 `tab:feature-ablation` 用 10-fold stratified CV 评估 within-distribution feature contribution，而 `tab:logo-results` 用 LOGO 评估 cross-generator generalization。 |
| **P2-2** Prompt 模板 | ✓ | `appendix_prompt_type.tex` 已有三种 prompt 的简述。改写为正式 itemize 列表，包含完整的 `\texttt{}` 格式模板。 |
| **P2-3** Baseline 公平性注释 | ✓ | 在 results.tex baseline 段落（L109 后）添加：FastDetectGPT/Binoculars 是 binary real/fake 检测工具而非 ordinal depth estimator，Avg-LogProb 是最有意义的 single-feature baseline。 |

artifacts 和 docs 两份已同步。

---
