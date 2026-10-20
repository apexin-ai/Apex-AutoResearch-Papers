# analysis skewness kurtosis ablation

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_skewness_kurtosis_ablation_20260521T062423_result.json`
- **Structured JSON:** [`7a0245a64c8dd1260ca3.json`](../../sessions/7a/7a0245a64c8dd1260ca3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。核心结论：

**Phase A（全量 37K 数据）**：加 cv 到 7-feature set 仅提升 +0.001 F1，可忽略。

**Phase B（1000 样本 token-NLL 子集）**：

| 证据维度 | 结果 |
|---------|------|
| **LOGO** | 加全部 6 个候选特征反而降低 3-class F1（0.733→0.722），无一对候选组合在两个任务上同时提升 |
| **LOFO** | 从 12 特征集中去掉 skewness/median/IQR 反而提升 F1（正 delta），说明它们引入噪声 |
| **DDR** | 全部 6 个候选特征都落在 drifting 区（\|ρ\|>0.63, d>0.77），与现有 entropy_mean/std 完全重叠 |
| **相关性** | median↔entropy_mean r=0.96, IQR↔entropy_std r=0.91, p90↔entropy_mean r=0.94 — 近乎完美线性冗余 |

排除理由清晰：候选特征与现有 7 features 高度冗余，不提供新的判别维度。

报告已保存到 `artifacts/_project/analysis/skewness_kurtosis_ablation.txt`。

---
