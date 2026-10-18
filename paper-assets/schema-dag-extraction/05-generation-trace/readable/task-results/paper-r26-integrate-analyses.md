# paper r26 integrate analyses

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_r26_integrate_analyses_20260522T052238_result.json`
- **Structured JSON:** [`38514203ff78973102a1.json`](../../sessions/38/38514203ff78973102a1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Appendix starts on page 13; body is within 8 pages (pages 1–8 body + references on pages 9–12).

### 修改摘要

| 任务 | 位置 | 内容 |
|------|------|------|
| **A: Ridge Regression** | `main.tex` 原 line 329, subsection E.1 内新 `\paragraph{Ridge regression under multicollinearity.}` | RidgeCV λ=0.001, β_BCS=−1.53, β_centrality=0.78, R²=0.594; 解析证明 β_BCS<0 对所有 λ≥0 成立; 仅做方向性解读 |
| **B: Bootstrap CI** | 新 subsection E.3 (`sec:appendix_bootstrap_ci`, page 17) | 164 FewRel batches, 6 个 Jaccard 阈值下 cluster-robust SE = 0.96–0.97× OLS SE, slope 显著 (p<10⁻¹¹), R² CI 宽度变化 −6%~+6%, 结论 robust |
| **C: Domain Distribution** | 新 subsection E.4 (`sec:appendix_domain_distribution`, page 17) | χ²=230.74 (p<0.001), high-BCS→science/taxonomy 49.5% + event/temporal 26.0%, low-BCS→geography 45.5% + creative_work 25.5%; 解释为 mediator 非独立 confound |

**编译结果**: 0 errors, 0 undefined references, 27 pages total (body ≤ 8 pages, appendix 从 page 13 起)。`\ref{sec:appendix_partial_corr}` 正确解析为 E.1。

---
