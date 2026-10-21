# research ref audit worker A

**When Debiasing Hurts: An Exact Bias Identity for LLM-Annotated Treatment Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_ref-audit-worker-A_20260526T104737_result.json`
- **Structured JSON:** [`0e9a12902bd086f2399f.json`](../../sessions/0e/0e9a12902bd086f2399f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已写入 `artifacts/ref-audit-worker-A.md`。

核心发现：

**2 个 HIGH severity 问题：**
1. **`sui2026ppci`** — 论文实际是关于 kernel-localized 条件均值估计，与 outcome-side misclassification 完全无关，但在 4 个 tex 文件中被错误描述为"extends PPI to outcome-side misclassification"。可能应该引用 Cadei et al. (2025) 或其他论文。
2. **`black2000racial`** — 论文是关于煤炭行业经济波动对残障项目参与的影响，完全不涉及 racial misclassification，但 tex 中声称该论文"demonstrate that racial misclassification in administrative data biases disparity estimates"。

**3 个 MEDIUM severity 问题：**
- `pangakis2023automated` — venue 虚构（实际是 arXiv preprint，不是 Findings of EMNLP 2023）
- `mozer2026ppi` — 引用上下文将其描述为"arm-specific PPI"，不准确
- `wood2018challenges` — 页码错误（应为 4586-4598 而非 5179-5186）

**30 条引用从未在 tex 中被 cite**，建议投稿前清理。

---
