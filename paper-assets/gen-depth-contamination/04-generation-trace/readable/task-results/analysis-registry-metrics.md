# analysis registry metrics 

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_registry_metrics____20260513T211333_result.json`
- **Structured JSON:** [`171b78cecd5da4821ee1.json`](../../sessions/17/171b78cecd5da4821ee1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两组数据都找到了。

```
config4_t12:
  0v1: 0.9982
  1v2: 0.7039
  2v3: 0.5823  (确认 < 0.60 ✓，K*=2 成立)
  3v4: 0.5293
  4v5: 0.5237
  top3_features_1v2: [freq_entropy, hapax_ratio, surp_skew]

qwen_cont_0v1:
  ci_lower: 0.9963
  ci_upper: 0.9978
  perm_p: 0.000
```

数据来源：
- config4_t12 → `results_exp003_t12/pairwise_auc.json` + `feature_importance.json`
- qwen_cont_0v1 → `artifacts/bootstrap_ci_4model.json` 中的 `exp_017_qwen_cont.0v1`（注意不在 `bootstrap_ci_results.json` 里，那个只有 3 个模型）

---
