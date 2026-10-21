# analysis api only diagnostic

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_api-only-diagnostic_20260523T073725_result.json`
- **Structured JSON:** [`0e3221d58f900308e823.json`](../../sessions/0e/0e3221d58f900308e823.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果：

```
=== API-only Diagnostic ===
K=3 API-only (84 panels):
  Pearson r (raw): 0.489
  Pearson r (log): 0.480
  VIF: 1.30

K=5 API-only (126 panels):
  Pearson r (raw): 0.853
  Pearson r (log): 0.879
  VIF: 4.40

Full set comparison:
  K=3 full r (raw): 0.70, API-only: 0.49
  K=5 full r (log): ~0.82, API-only: 0.88
```

关键发现：
- **K=3 API-only**: 相关性显著低于全集 (0.49 vs 0.70)，VIF=1.30 很低，multicollinearity 不是问题
- **K=5 API-only**: 相关性反而略高于全集 (0.88 vs ~0.82)，VIF=4.40 接近但未超过常用阈值 5，需注意

结果已保存到 `api_only_diagnostic.json`。

---
