# experiment plan 007 cross strategy loo zscore

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_experiment_plan_007_cross_strategy_loo_zscore_20260515T050637_result.json`
- **Structured JSON:** [`9a5e1588ec75900db472.json`](../../sessions/9a/9a5e1588ec75900db472.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。结果摘要：

**Negative result**: Z-score 对 RF 无效（Δd1v2 ≤ +0.018，噪声级别）。

| Model | Holdout temp09 raw d1v2 | Z d1v2 | Δ |
|-------|------------------------|--------|---|
| Pythia | 0.576 | 0.594 | +0.018 |
| GPT-2 XL | 0.129 | 0.135 | +0.006 |
| OLMo | 0.253 | 0.250 | -0.003 |

**原因**：RF 是树模型，决策树分裂基于阈值比较，对特征的线性缩放/平移不变。z-score 不改变样本在每个特征上的排序，因此不改变任何分裂点。之前独立验证中 z-score 恢复 AUC（0.13→0.68）是用 LR 做的——LR 的线性决策边界对 scale 敏感，z-score 能修正 covariate shift。

**结论**：covariate shift 假说正确，但修复方案依赖分类器类型。RF 不需要（也无法受益于）z-score；LR 需要。Raw 结果与 cross_strategy_loo_001 完全一致，已注册 `cross_strategy_loo_zscore_001`（conclusion=negative）。

---
