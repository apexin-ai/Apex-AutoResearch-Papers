# paper r20 fixes full

**When Debiasing Hurts: An Exact Bias Identity for LLM-Annotated Treatment Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_r20-fixes-full_20260524T120136_result.json`
- **Structured JSON:** [`e43260576ae5a1b9ae39.json`](../../sessions/e4/e43260576ae5a1b9ae39.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部 8 项修改已完成，编译通过。

**结果**：0 errors, 0 undefined refs, 主文 8 页（未超页），abstract ~170 words。

**修改清单**：
- **MF1**: method.tex L11 + experiments.tex L81-85 新增 (A2) 讨论，配套精简 James-Stein 解释、PPCI 段、对比段
- **MF2**: abstract.tex AUC 顺序改为 0.86 → 1.0 → 0.63
- **SF3**: 4 篇引用已补（Gligorić NAACL'25, Knox/Lucas/Cho ARPS'22, Ura QE'18, Knox/Lowe/Mummolo APSR'20），bib 条目已添加，ura2015→ura2018 已更新
- **SF1**: experiments.tex L78 补 Table 22 筛选结果（strict/relaxed screening）
- **SF4**: method.tex L56 补 PPCI 组合独立性充分条件
- **SF5**: method.tex L44 补 Eq.6 独立性假设 + 脚注
- **SF6**: experiments.tex L85 补 class imbalance 退化
- **Figure 2**: experiments.tex + theory.tex 中 fig:heatmap 引用已加 `(Appendix~\ref{app:dgp})`

报告已保存至 `artifacts/r20_fixes_report.md`。

---
