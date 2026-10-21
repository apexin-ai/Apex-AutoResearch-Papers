# analysis t20 a100 s42 fp32

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_t20_a100_s42_fp32_20260520T165519_result.json`
- **Structured JSON:** [`429d3eef7840bf62461d.json`](../../sessions/42/429d3eef7840bf62461d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。核心结果：

## T=20 α=1.0 s42 fp32 — 结果摘要

```json
{
  "alpha": 1.0, "seed": 42, "T": 20, "n_generations": 21,
  "observed_permg_count": 6, "observed_rate": 0.75,
  "predicted_permg_count": 7, "predicted_rate": 0.832,
  "predicted_rate_95ci": [0.76, 0.96],
  "within_ci": false, "within_range": true,
  "robust_pairs_K3": 6, "robust_pairs_K4": 6,
  "permg_rev_fdr": 0, "ty_fwd_fdr": 1,
  "final_ppl": 2041.50, "final_entropy": 1.2052,
  "exit_code": 0,
  "conclusion": "NEGATIVE_MARGINAL"
}
```

### 5-Method Forward Significance

| Method | Count /8 |
|--------|----------|
| Naive XCorr | 8 |
| Diff XCorr FDR | 6 |
| Threshold Onset | 6 |
| PermG FDR | 6 |
| TY Granger | 1 |

### Robust Pairs 详情

| Pair | Votes | Methods |
|------|-------|---------|
| token_entropy → distinct_1 | 4/5 | naive, diff, threshold, perm |
| token_entropy → distinct_2 | 4/5 | naive, diff, threshold, perm |
| token_entropy → distinct_3 | 4/5 | naive, diff, threshold, perm |
| token_entropy → mauve | 1/5 | naive |
| ece → distinct_1 | **5/5** | naive, diff, threshold, perm, ty |
| ece → distinct_2 | 4/5 | naive, diff, threshold, perm |
| ece → distinct_3 | 4/5 | naive, diff, threshold, perm |
| ece → mauve | 1/5 | naive |

### 预测验证

- **observed_rate = 0.75，略低于 CI 下界 0.76** — within_ci = false
- PermG count = 6 在 predicted_range [6, 8] 内 — within_range = true
- **T=20 vs T=10 均为 6/8，√T Power Theory 未产生额外统计功效**
- 失败的 2 pairs 均为 mauve 相关，与 T=10 pattern 完全一致
- Reverse PermG = 0/8，方向性干净

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "data": {
    "alpha": 1.0,
    "seed": 42,
    "T": 20,
    "n_generations": 21,
    "observed_permg_count": 6,
    "observed_rate": 0.75,
    "predicted_permg_count": 7,
    "predicted_rate": 0.832,
    "predicted_rate_95ci": [
      0.76,
      0.96
    ],
    "within_ci": false,
    "within_range": true,
    "robust_pairs_K3": 6,
    "robust_pairs_K4": 6,
    "permg_rev_fdr": 0,
    "ty_fwd_fdr": 1,
    "final_ppl": 2041.5,
    "final_entropy": 1.2052,
    "exit_code": 0,
    "conclusion": "NEGATIVE_MARGINAL"
  }
}
```

</details>

---
