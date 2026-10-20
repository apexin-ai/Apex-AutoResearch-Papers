# code exp 026 feature stability

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp_026_feature_stability_20260517T074346_result.json`
- **Structured JSON:** [`3c96ae14cdae2b9aae8b.json`](../../sessions/3c/3c96ae14cdae2b9aae8b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

exp_026 完成。汇总结果：

```
subset_size | num_tested | num_K*=2 | min_1v2_AUC | mean_1v2_AUC
---------------------------------------------------------------
15          | 1          | 0        | 0.9472      | 0.9472
10          | 5          | 0        | 0.8698      | 0.9202
8           | 5          | 0        | 0.8955      | 0.9156
5           | 5          | 0        | 0.8785      | 0.9081
3 (top-3)   | 1          | 0        | 0.8314      | 0.8314
```

**结论**：1v2 AUC 在所有 17 个 feature 子集中均远超 θ=0.60（最低 0.8314，来自仅用 top-3 特征）。Feature 子集选择对区分能力无实质影响。

注：实际 K\* 在该数据集上为 4（不是 2），即所有相邻 depth pair（0v1 到 3v4）的 AUC 均 > 0.60，表明 exp_008 retrain chain 数据中 depth 0-4 全程可区分。`num_K*=2` 列全为 0 是因为 K\* 始终为 4。

---
