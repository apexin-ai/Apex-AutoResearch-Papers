# code exp 026 feature stability v2

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp_026_feature_stability_v2_20260517T080737_result.json`
- **Structured JSON:** [`9a690e629db4ff109f65.json`](../../sessions/9a/9a690e629db4ff109f65.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。结果：

```
subset_size | num_tested | num_K*=2 | min_1v2_AUC | mean_1v2_AUC
15          | 1          | 1        | 0.6262      | 0.6262
10          | 5          | 5        | 0.6153      | 0.6191
8           | 5          | 5        | 0.6056      | 0.6159
5           | 5          | 2        | 0.5856      | 0.5998
3 (top-3)   | 1          | 0        | 0.5871      | 0.5871
```

关键发现：**Feature selection 在 K\*=2 边界处确实 matters。**

- **8D+ 子集 robust**：10D 和 8D 所有 5 次随机采样都 pass θ=0.60（min=0.6056）
- **5D 子集 fragile**：仅 2/5 pass θ，3 次掉到 0.585-0.594，mean=0.5998 刚好在边界
- **Top-3 特征 fail**：surp_d1_std + surp_std + surp_d2_std 只拿到 0.5871，不足以支撑 K\*=2

与 v1（retrain-chain, K\*=4）形成鲜明对比：v1 所有子集 trivially pass（min=0.8314）。数据源换对后，这个实验提供了论文需要的关键证据——在 K\* 边界处需要 ≥8D 特征才能稳健维持判别力。

Registry 和 artifact 均已更新。

---
