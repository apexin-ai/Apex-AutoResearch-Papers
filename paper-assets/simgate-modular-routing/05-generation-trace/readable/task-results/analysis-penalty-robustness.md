# analysis penalty robustness

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_penalty-robustness_20260515T220012_result.json`
- **Structured JSON:** [`62843128fb590321e46a.json`](../../sessions/62/62843128fb590321e46a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。结果：

```
=== Penalty Robustness Analysis (245 episodes) ===

| Metric       |          P=-50 |    P=-100 (baseline) |         P=-200 |
|--------------|----------------|----------------------|----------------|
| Δ_full       |          16.33 |                29.60 |          56.13 |
| Δ_nd         |           2.84 |                 2.84 |           2.84 |
| DAF          |          82.6% |                90.4% |          95.0% |
| DAF 95% CI   |   [67.6, 98.4] |         [81.5, 99.1] |   [90.0, 99.5] |
| Pearson r    |         0.8876 |               0.9652 |         0.9905 |
```

**结论：ROBUST。**

- DAF 在三个 penalty 值下均 >80%（82.6%→90.4%→95.0%），95% CI 互相重叠
- Δ_nd = 2.84 是常数（不依赖 penalty），确认非死亡路径的分数差异很小
- Pearson r 随 penalty 增大单调递增（0.89→0.97→0.99），死亡回避始终是分数差距的主导因素
- DAF 随 penalty 增大而增大是数学必然（Δ_full = δ·P + Δ_nd），但即使在最低 penalty P=50 时仍有 82.6%

核心发现（DAF≈90%）不是特定 penalty 值的产物。脚本和结果已保存至 `results/penalty_robustness/`。

---
