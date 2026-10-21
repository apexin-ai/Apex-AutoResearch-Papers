# exp review exp c overall ci v2

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exp_review-exp-c-overall-ci-v2_20260515T123124_result.json`
- **Structured JSON:** [`325a9a0d626e0ca0518a.json`](../../sessions/32/325a9a0d626e0ca0518a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。结果汇总：

| 指标 | 值 |
|------|-----|
| **Overall 6-gen F1** | 0.7878 |
| **95% CI** | [0.783, 0.792] |
| **CI width** | 0.009 |
| Pipeline | bootstrap_ci_v2.py (class-balanced downsample) |
| Bootstrap n | 1000 |

Per-gen sanity check 全部通过，与 Table 1 registry 值最大偏差仅 0.0032pp。结果已保存至 `results/review_overall_ci_v2_results.json` 并更新 registry。

---
