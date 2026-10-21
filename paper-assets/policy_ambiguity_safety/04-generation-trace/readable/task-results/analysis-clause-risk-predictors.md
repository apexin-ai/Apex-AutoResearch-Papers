# analysis clause risk predictors

**Policy Ambiguity Is Nocuous: Clause-Level Causal Effects on Customer-Service Agent Safety** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_clause_risk_predictors_20260522T150934_result.json`
- **Structured JSON:** [`2f8af750218cc34060a6.json`](../../sessions/2f/2f8af750218cc34060a6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。两个产出文件已保存：
- `artifacts/analysis_clause_risk_predictors.json`
- `artifacts/analysis_clause_risk_predictors_summary.md`

核心发现：

**OLS 线性回归：R² 极低，没有单一显著预测因子**
- 语言特征 R²=0.069 > 类型 R²=0.037 > full R²=0.087
- 10 个语言特征中没有任何一个在 α=.05 下显著
- 类型控制语言特征后仅增量 ΔR²=0.018

**Random Forest 捕获非线性关系：R²=0.396**
- Top 3 特征：length_ratio (0.23)、polysemous_ratio (0.23)、token_delta (0.21)
- 这三个都与 ambiguous/unambiguous 版本之间的"信息差距"相关

**关键解读**：那 22% 的 clause-within-type variance 不是由简单的表面语言特征线性驱动的。风险分布在多个弱预测因子的非线性交互中——具体来说，clause 的危险程度与其 disambiguation 需要多少额外信息（length_ratio, token_delta）以及其词汇歧义度（polysemous_ratio）非线性相关。这意味着 clause 风险更多由深层语义/语用属性决定，而非表面句法复杂度。

---
