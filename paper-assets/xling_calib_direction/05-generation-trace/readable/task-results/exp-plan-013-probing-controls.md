# exp plan 013 probing controls

**Shifting the Cross-Lingual Calibration Pareto Frontier: Probe-Based Calibration Transfer via CaCLR** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exp_plan_013_probing_controls_20260520T232027_result.json`
- **Structured JSON:** [`8bb22d48e57f1e0fde2b.json`](../../sessions/8b/8bb22d48e57f1e0fde2b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。结果如下：

| Layer | Real AUROC | Perm AUROC | Perm std | Selectivity |
|------:|-----------:|-----------:|---------:|------------:|
| 0     | 0.8851     | 0.8275     | 0.0033   | 0.1496      |
| 4     | 0.8999     | 0.8330     | 0.0034   | 0.1675      |
| 8     | 0.9053     | 0.8331     | 0.0021   | 0.1780      |
| 12    | 0.9070     | 0.8344     | 0.0035   | 0.1786      |
| 16    | 0.9308     | 0.8383     | 0.0037   | 0.2146      |
| 20    | 0.9536     | 0.8364     | 0.0048   | 0.2584      |
| 24    | 0.9573     | 0.8356     | 0.0040   | 0.2660      |
| 27    | 0.9587     | 0.8394     | 0.0041   | 0.2600      |

**关键发现：selectivity 非常低（0.15–0.27），远低于 0.8 阈值。**

问题在于 permuted probes 的 AUROC 也很高（~0.83），这说明 probe 在随机 labels 上也能达到高 AUROC——典型的高维过拟合。88 次 LR 都在训练集上评估（没有 train/test split），3584 维 features 相对于样本数太高，导致即使随机标签也能被很好地"拟合"。

**根因：脚本用训练集 AUROC 而非测试集 AUROC。** `clf.fit(X_s, y)` 后直接 `roc_auc_score(y, clf.decision_function(X_s))`，没有 cross-validation。需要改用 CV 来获得有意义的 selectivity。

需要修改脚本用 cross-validated AUROC 重新跑吗？

---
